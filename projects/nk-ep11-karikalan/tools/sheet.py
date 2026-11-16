#!/usr/bin/env python3
"""Contact sheet + 1920x1080 film copies.  python tools/sheet.py 1 10  -> out/sheets/sheet_001_010.jpg, out/img/NNN.jpg"""
import sys, os
from PIL import Image, ImageDraw
a, b = int(sys.argv[1]), int(sys.argv[2])
os.makedirs("out/sheets", exist_ok=True); os.makedirs("out/img", exist_ok=True)
cols = 5; tw, th = 384, 216
rows = (b - a + 1 + cols - 1) // cols
S = Image.new("RGB", (cols * tw, rows * th), (20, 20, 20)); d = ImageDraw.Draw(S)
for i, n in enumerate(range(a, b + 1)):
    p = f"out/raw/{n:03d}.jpg"
    if not os.path.exists(p): print("missing", n); continue
    im = Image.open(p).convert("RGB")
    w, h = im.size
    if i == 0: print("size", w, h, os.path.getsize(p))
    # centre-crop to 16:9, 1920x1080
    if w / h > 16 / 9: nw = int(h * 16 / 9); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else: nh = int(w * 9 / 16); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im = im.resize((1920, 1080), Image.LANCZOS)
    im.save(f"out/img/{n:03d}.jpg", quality=84)
    t = im.resize((tw, th), Image.LANCZOS)
    S.paste(t, ((i % cols) * tw, (i // cols) * th))
    d.rectangle([(i % cols) * tw, (i // cols) * th, (i % cols) * tw + 40, (i // cols) * th + 18], fill=(0, 0, 0))
    d.text(((i % cols) * tw + 4, (i // cols) * th + 3), f"{n:03d}", fill=(255, 220, 120))
S.save(f"out/sheets/sheet_{a:03d}_{b:03d}.jpg", quality=80)
