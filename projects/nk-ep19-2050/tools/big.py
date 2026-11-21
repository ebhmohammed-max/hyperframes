#!/usr/bin/env python3
"""Larger check sheets than tools/sheet.py: pictures a..b in grids of six (3 x 2, 640 px wide each), with the number in the corner.
   /tmp/nkvenv/bin/python tools/big.py 21 30  ->  out/sheets/big_021.jpg, big_027.jpg"""
import sys, os
from PIL import Image, ImageDraw
a, b = int(sys.argv[1]), int(sys.argv[2])
for s in range(a, b + 1, 6):
    ns = [n for n in range(s, min(s + 5, b) + 1) if os.path.exists(f"out/raw/{n:03d}.jpg")]
    sheet = Image.new("RGB", (1920, 360 * ((len(ns) + 2) // 3)), "black")
    for i, n in enumerate(ns):
        im = Image.open(f"out/raw/{n:03d}.jpg").convert("RGB").resize((640, 360), Image.LANCZOS)
        d = ImageDraw.Draw(im); d.rectangle([0, 0, 44, 18], fill="black"); d.text((6, 3), f"{n:03d}", fill="white")
        sheet.paste(im, ((i % 3) * 640, (i // 3) * 360))
    sheet.save(f"out/sheets/big_{s:03d}.jpg", quality=85); print(f"out/sheets/big_{s:03d}.jpg", ns)
