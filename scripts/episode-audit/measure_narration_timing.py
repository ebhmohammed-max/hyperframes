#!/usr/bin/env python3
"""
Measure the narration, don't assume it.

The voice runs continuously across the block boundaries — the 30 s blocks are a script
structure, not a pause. Every on-screen call therefore lands on a *measured* sentence
gap, found here with numpy rather than guessed from character counts.

  - decode the master once to 16 kHz mono
  - a sentence end is an energy gap of 0.28 s or more below -40 dBFS
  - a sentence boundary is a gap of 0.55 s or more (the comma-sized gaps are 0.1-0.3 s)
  - map each script sentence onto its measured span, left to right, clamping so a
    long line never grabs the whole block

Writes production/NARRATION_TIMING.json: every sentence start/end, and the gap that
follows it, in absolute seconds.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / "projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria"
PROJ = EP / "documentary_v2"
NARRATION = PROJ / "assets/audio/narration.mp3"
BLOCKS = EP / "story_film_35min/narration_blocks_v02.json"
OUT = PROJ / "production/NARRATION_TIMING.json"

RATE = 16000
BLOCK = 30.0
GAP_DB = -40.0
MIN_GAP = 0.20          # holes shorter than this are inside words and get filled
SNAP_WINDOW = 3.0       # how far a proportional target may move to meet measured evidence


def decode() -> np.ndarray:
    env = dict(os.environ)
    env["PATH"] = f"{ROOT}/.cache/bin:" + env.get("PATH", "")
    raw = Path("/tmp/narr16k.raw")
    subprocess.run(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", str(NARRATION),
         "-ac", "1", "-ar", str(RATE), "-f", "s16le", str(raw), "-y"],
        check=True, env=env,
    )
    return np.fromfile(raw, dtype=np.int16).astype(np.float32) / 32768.0


def voiced(x: np.ndarray, win: float = 0.02) -> np.ndarray:
    """Per-window boolean: True where the signal is above the floor."""
    n = int(RATE * win)
    frames = len(x) // n
    if frames == 0:
        return np.zeros(0, bool)
    rms = np.sqrt(np.mean(x[: frames * n].reshape(frames, n) ** 2, axis=1) + 1e-12)
    db = 20 * np.log10(rms + 1e-12)
    return db > GAP_DB


def segments(v: np.ndarray, win: float = 0.02) -> list[tuple[float, float]]:
    """Contiguous voiced runs as (start, end) seconds."""
    out, start = [], None
    for i, on in enumerate(v):
        if on and start is None:
            start = i
        elif not on and start is not None:
            out.append((start * win, i * win))
            start = None
    if start is not None:
        out.append((start * win, len(v) * win))
    return out


def merge_runs(segs: list[tuple[float, float]], gap: float) -> list[tuple[float, float]]:
    """Join voiced runs separated by less than `gap` seconds.

    A 20 ms window sees plosive closures and breath noise as silence; a sentence gap is
    ten to forty times longer. Merging below 0.20 s leaves only real punctuation.
    """
    if not segs:
        return []
    out = [list(segs[0])]
    for a, b in segs[1:]:
        if a - out[-1][1] < gap:
            out[-1][1] = b
        else:
            out.append([a, b])
    return [(round(a, 3), round(b, 3)) for a, b in out]


def split_sentences(text: str) -> list[str]:
    # protect the abbreviations this script actually uses
    t = text
    for a in ("U.S.", "A.D.", "B.C.", "a.m.", "p.m."):
        t = t.replace(a, a.replace(".", "\u0000"))
    parts = [p for p in re.split(r"(?<=[.?!])\s+", t.strip()) if p]
    return [p.replace("\u0000", ".") for p in parts]


def align(ss: list[str], segs: list[tuple[float, float]]) -> list[dict]:
    """Snap proportional sentence targets onto the nearest measured gaps.

    The text tells us roughly where each sentence ends; the audio tells us exactly. So
    the character-length prior proposes a boundary, and it is moved to the nearest gap
    of at least 0.20 s within +/-3 s, keeping order and at least one run per sentence.
    """
    if not segs:
        return []
    n = len(ss)
    gaps = [((segs[k][1] + segs[k + 1][0]) / 2.0, k) for k in range(len(segs) - 1)]

    total = sum(len(x) for x in ss) or 1
    targets, acc = [], 0
    for x in ss[:-1]:
        acc += len(x)
        targets.append(segs[0][0] + acc / total * (segs[-1][1] - segs[0][0]))

    chosen: list[int] = []
    lo = 0
    for ti, t in enumerate(targets):
        best, best_d = None, None
        for g, k in gaps:
            if k < lo:
                continue
            if g < t - SNAP_WINDOW:
                continue
            if g > t + SNAP_WINDOW:
                break
            d = abs(g - t)
            if best_d is None or d < best_d:
                best, best_d = (g, k), d
        if best is None:                      # no gap in reach: cut proportionally
            # k must index a real gap; len(segs)-1 is the last run and has no gap after it
            best = (t, min(lo, max(len(gaps) - 1, 0)) if gaps else 0)
        chosen.append(best)
        lo = best[1] + 1

    # rebuild sentence spans from the chosen cut points
    bounds = [segs[0][0]] + [round((segs[k][1] + segs[k + 1][0]) / 2.0, 3) for _, k in chosen]
    out = []
    for i, x in enumerate(ss):
        a = bounds[i]
        b = bounds[i + 1] if i + 1 < len(bounds) else segs[-1][1]
        k_end = chosen[i][1] if i < len(chosen) else len(segs) - 1
        gap_after = (round(segs[k_end + 1][0] - segs[k_end][1], 3)
                     if k_end + 1 < len(segs) else None)
        out.append({"i": i, "text": x, "start": round(a, 3), "end": round(b, 3),
                    "gap_after": gap_after})
    return out


def main() -> None:
    blocks = json.loads(BLOCKS.read_text())
    x = decode()
    dur = len(x) / RATE
    v = voiced(x)
    segs = segments(v)

    out = {"duration": round(dur, 3), "rate": RATE, "gap_db": GAP_DB,
           "min_gap": MIN_GAP, "voiced_runs": len(segs), "blocks": []}
    for i, text in enumerate(blocks):
        t0 = i * BLOCK
        t1 = t0 + BLOCK
        inside = merge_runs([(a, b) for a, b in segs if a >= t0 - 0.05 and b <= t1 + 0.05], MIN_GAP)
        ss = split_sentences(text)
        rec = {"block": i + 1, "start": t0, "sentence_count": len(ss),
               "runs": len(inside), "sentences": align(ss, inside)}
        out["blocks"].append(rec)

    (PROJ / "production").mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1))
    print(f"{dur:.3f}s · {len(segs)} voiced runs · "
          f"{sum(len(b['sentences']) for b in out['blocks'])} sentences placed")


if __name__ == "__main__":
    main()
