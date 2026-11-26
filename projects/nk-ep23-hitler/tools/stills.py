#!/usr/bin/env python3
"""Stills of every graphic before a render.  $PY tools/stills.py [clips…]  → /tmp/stills/<clip>/ and google_drive/_sheet_<prefix><n>.jpg
Times: chapter card, each line with a graphic (stat, big, vs: near the end of the line; flash: inside each word), the subscribe pop-up, title."""
import json, os, subprocess, sys, glob, re
from PIL import Image, ImageDraw
A = json.load(open("narration/align.json")); L = json.load(open("script/lines.json"))
CL = {c["id"]: c for c in json.load(open("script/clips.json"))}
clips = [c for c in sys.argv[1:] if not c.startswith("--")] or ["TITLE"] + list(CL)
prefix = next((c[2:] for c in sys.argv[1:] if c.startswith("--")), "E23S")
shots = []
for c in clips:
    if c == "TITLE": ts = [(2.0, "queue"), (5.0, "balcony"), (7.6, "title"), (10.5, "title")]
    else:
        card = bool(CL[c]["title"]); lead = 2.55 if card else 0.4; ts = [(1.3, "card")] if card else [(0.6, "first")]
        for l in [x for x in L if x["clip"] == c]:
            a = A[c]["lines"][l["q"]]; fx = l.get("fx") or {}
            if "flash" in fx:
                for k, u in enumerate(a["un"]):
                    if k < len(fx["flash"]) and (fx["flash"][k] or fx.get("strike")): ts.append((lead + (u[0] + u[1]) / 2 + (0.25 if fx.get("strike") else 0), f"q{l['q']} flash{k}"))
            for g in ("stat", "big", "vs", "dots", "line", "split"):
                if g in fx: ts.append((lead + a["a1"] - 0.35, f"q{l['q']} {g}"))
            if c == "N03" and l["q"] == 2: ts.append((lead + a["a0"] + 2.6, "q2 subscribe"))
    ts = sorted((round(t, 2), n) for t, n in ts)
    d = f"/tmp/stills/{c}"; subprocess.run(["rm", "-rf", d])
    subprocess.run(["hyperframes", "snapshot", "--at", ",".join(str(t) for t, _ in ts), "--no-end", "-o", d], cwd=f"film/{c}", capture_output=True)
    fs = sorted(glob.glob(d + "/frame-*.png")); assert len(fs) == len(ts), (c, len(fs), len(ts))
    shots += [(f, f"{c} {t}s {n}") for f, (t, n) in zip(fs, ts)]
    print(c, len(ts))
for i in range(0, len(shots), 12):
    part = shots[i:i + 12]; rows = (len(part) + 2) // 3
    S = Image.new("RGB", (1920, rows * 360), (20, 20, 20)); d = ImageDraw.Draw(S)
    for k, (f, t) in enumerate(part):
        x, y = (k % 3) * 640, (k // 3) * 360
        S.paste(Image.open(f).convert("RGB").resize((640, 360), Image.LANCZOS), (x, y)); d.rectangle([x, y, x + 8 + 6 * len(t), y + 14], fill=(0, 0, 0)); d.text((x + 4, y + 1), t, fill=(255, 255, 255))
    S.save(f"../../google_drive/_sheet_{prefix}{i // 12 + 1}.jpg", quality=88); print("sheet", f"{prefix}{i // 12 + 1}", len(part))
