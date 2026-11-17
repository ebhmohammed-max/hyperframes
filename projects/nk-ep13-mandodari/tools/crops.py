#!/usr/bin/env python3
"""Apply shots/crops.json to the film copies in out/img (run after tools/sheet.py)."""
import json, os
from PIL import Image
C = json.load(open("shots/crops.json"))
for n, v in C.items():
    if n == "_": continue
    src, x0, y0, x1, y1 = v
    if not os.path.exists(f"out/raw/{src}.jpg"): continue
    im = Image.open(f"out/raw/{src}.jpg").convert("RGB"); w, h = im.size
    box = [int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)]
    bw, bh = box[2] - box[0], box[3] - box[1]
    if bw / bh > 16 / 9: nw = int(bh * 16 / 9); box[0] += (bw - nw) // 2; box[2] = box[0] + nw
    else: nh = int(bw * 9 / 16); box[1] += (bh - nh) // 2; box[3] = box[1] + nh
    im.crop(box).resize((1920, 1080), Image.LANCZOS).save(f"out/img/{n}.jpg", quality=86)
    print(n, "from", src, box)
