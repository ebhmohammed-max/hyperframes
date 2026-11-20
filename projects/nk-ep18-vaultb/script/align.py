#!/usr/bin/env python3
"""Line timings for the narration clips, measured from the audio (no speech model available here).
   /tmp/nkvenv/bin/python script/align.py  ->  narration/align.json, narration/align_report.txt
1. ffmpeg silencedetect -> speech segments between pauses.
2. Each segment gets a syllable estimate: peaks of the 300-3400 Hz energy envelope (syllable nuclei).
3. The script is split into sentences/phrases; a dynamic programme assigns consecutive segments to
   each unit so that syllable estimates match the text's syllable counts, and line ends fall on pauses.
Lines whose measured rate is far from the clip's rate are flagged for a listening check."""
import json, re, subprocess, os, sys
import numpy as np
FF = os.environ.get("HYPERFRAMES_FFMPEG_PATH", "ffmpeg")
lines = json.load(open("script/lines.json", encoding="utf8"))
clips = sorted({l["clip"] for l in lines})
only = sys.argv[1:] or clips

def syl(text):
    n = 0.0; cp = list(text)
    for i, ch in enumerate(cp):
        c = ord(ch)
        if 0x0B85 <= c <= 0x0B94: n += 1
        elif 0x0B95 <= c <= 0x0BB9: n += 0.0 if i + 1 < len(cp) and cp[i + 1] == "\u0bcd" else 1
        elif ch.isdigit(): n += 2
    return max(n, 1.0)

def units_of(text):  # sentence-level pieces of one line
    parts = [p.strip() for p in re.split(r"(?<=[.?!…])\s+", text) if p.strip()]
    return parts or [text]

def pcm(path, sr=8000):
    raw = subprocess.run([FF, "-v", "error", "-i", path, "-af", "highpass=f=300,lowpass=f=3400", "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"],
                         capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0, sr

def envelope(x, sr, hop=0.005, win=0.03):
    h, w = int(sr * hop), int(sr * win)
    n = (len(x) - w) // h
    e = np.array([np.sqrt(np.mean(x[i * h:i * h + w] ** 2)) for i in range(n)])
    k = np.hanning(9); k /= k.sum()
    return np.convolve(e, k, mode="same"), hop

def peaks(e, lo, hi, hop, thr):
    seg = e[lo:hi]; out = []
    last = -99
    for i in range(1, len(seg) - 1):
        if seg[i] > seg[i - 1] and seg[i] >= seg[i + 1] and seg[i] > thr:
            # prominence: dip of at least 12% between this and the previous accepted peak
            if out and (i - last) * hop < 0.075:
                if seg[i] > seg[last]: out[-1] = i; last = i
                continue
            if out:
                dip = seg[last:i].min()
                if dip > 0.88 * min(seg[last], seg[i]):
                    if seg[i] > seg[last]: out[-1] = i; last = i
                    continue
            out.append(i); last = i
    return len(out)

res, report = {}, []
if os.path.exists("narration/align.json"): res = json.load(open("narration/align.json"))
for cid in only:
    L = [l for l in lines if l["clip"] == cid]
    x, sr = pcm(f"narration/{cid}.mp3")
    e, hop = envelope(x, sr)
    dur = len(x) / sr
    thr_sil = max(0.012, 0.06 * np.percentile(e, 95))
    # speech segments: envelope above threshold, pauses >= 0.13 s split
    act = e > thr_sil
    segs, i, N = [], 0, len(act)
    while i < N:
        if act[i]:
            j = i
            while j < N and act[j]: j += 1
            segs.append([i, j]); i = j
        else: i += 1
    merged = []
    for s in segs:
        if merged and (s[0] - merged[-1][1]) * hop < 0.13: merged[-1][1] = s[1]
        else: merged.append(s)
    segs = [s for s in merged if (s[1] - s[0]) * hop > 0.09]
    est = np.array([max(1, peaks(e, a, b, hop, thr_sil * 1.3)) for a, b in segs], dtype=float)
    segt = [[a * hop + 0.012, b * hop + 0.012] for a, b in segs]
    gaps = [segt[i + 1][0] - segt[i][1] for i in range(len(segt) - 1)]
    # units
    U = []
    for q, l in enumerate(L):
        ps = units_of(l["say"])
        for k, p in enumerate(ps): U.append({"q": q, "last": k == len(ps) - 1, "syl": syl(p), "txt": p})
    n, m = len(U), len(segt)
    assert m >= n, f"{cid}: {m} segments for {n} sentence units"
    scale = est.sum() / sum(u["syl"] for u in U)
    cum = np.concatenate([[0], np.cumsum(est)])
    INF = 1e18
    best = np.full((n + 1, m + 1), INF); back = np.zeros((n + 1, m + 1), dtype=int)
    best[0, 0] = 0
    for i in range(1, n + 1):
        exp = U[i - 1]["syl"] * scale
        for j in range(i, m - (n - i) + 1):
            for k in range(max(i - 1, j - 9), j):
                if best[i - 1, k] >= INF: continue
                a = cum[j] - cum[k]
                c = (a - exp) ** 2 / (exp + 1.0)
                c += 0.25 * (j - k - 1)                                   # prefer few inner pauses
                if j < m:
                    g = gaps[j - 1]
                    c -= (1.6 if U[i - 1]["last"] else 1.0) * min(g, 0.75)     # sentence ends sit on long pauses
                v = best[i - 1, k] + c
                if v < best[i, j]: best[i, j], back[i, j] = v, k
    j, cuts = m, []
    for i in range(n, 0, -1):
        k = back[i, j]; cuts.append((k, j)); j = k
    cuts.reverse()
    out = []
    for q, l in enumerate(L):
        idx = [i for i, u in enumerate(U) if u["q"] == q]
        k, j = cuts[idx[0]][0], cuts[idx[-1]][1]
        a0, a1 = segt[k][0], segt[j - 1][1]
        r = (cum[j] - cum[k]) / (syl(l["say"]) * scale)
        sps = syl(l["say"]) / max(0.2, sum(b - a for a, b in segt[k:j]))
        out.append({"q": q, "a0": round(a0, 3), "a1": round(a1, 3), "sps": round(sps, 2),
                    "ph": [[round(a, 3), round(b, 3)] for a, b in segt[k:j]],
                    "un": [[round(segt[cuts[i][0]][0], 3), round(segt[cuts[i][1] - 1][1], 3)] for i in idx]})
    med = float(np.median([o["sps"] for o in out]))
    for o, l in zip(out, L):
        flag = "" if 0.68 * med <= o["sps"] <= 1.42 * med else "  <<< check"
        report.append(f"{cid} q{o['q']:02d} {o['a0']:7.2f}-{o['a1']:7.2f} {o['a1']-o['a0']:5.2f}s {o['sps']:4.1f} syl/s segs={len(o['ph'])} {l['say'][:44]}{flag}")
    res[cid] = {"dur": round(dur, 3), "sps": round(med, 2), "lines": out}
json.dump(res, open("narration/align.json", "w"), indent=1)
open("narration/align_report.txt", "w", encoding="utf8").write("\n".join(report) + "\n")
bad = [r for r in report if "check" in r]
print(len(report), "lines;", len(bad), "flagged")
for b in bad: print(b)
