#!/usr/bin/env python3
"""Flag film copies (out/img) whose outer rows/columns or corners are near black: a baked-in frame or bar.
python tools/edges.py 110 119"""
import sys, warnings
from PIL import Image
warnings.simplefilter("ignore")
a, b = int(sys.argv[1]), int(sys.argv[2])
for n in range(a, b + 1):
    im = Image.open(f"out/img/{n:03d}.jpg").convert("L"); W, H = im.size
    px = im.load()
    row = lambda y: sum(px[x, y] for x in range(W // 4, 3 * W // 4, 8)) // len(range(W // 4, 3 * W // 4, 8))
    col = lambda x: sum(px[x, y] for y in range(H // 4, 3 * H // 4, 8)) // len(range(H // 4, 3 * H // 4, 8))
    blk = lambda x, y: sum(px[x + i, y + j] for i in range(0, 14, 2) for j in range(0, 14, 2)) // 49
    e = {"T": [row(y) for y in (0, 8, 16, 24, 40)], "B": [row(H - 1 - y) for y in (0, 8, 16, 24, 40)],
         "L": [col(x) for x in (0, 8, 16, 24, 40)], "R": [col(W - 1 - x) for x in (0, 8, 16, 24, 40)]}
    c = [blk(0, 0), blk(W - 14, 0), blk(0, H - 14), blk(W - 14, H - 14)]
    ci = [blk(70, 70), blk(W - 84, 70), blk(70, H - 84), blk(W - 84, H - 84)]
    flags = [k for k, v in e.items() if v[0] < 12 and v[4] > v[0] + 25]
    if sum(1 for x, y in zip(c, ci) if x < 10 and y > x + 20) >= 2: flags.append("corners")
    print(f"{n:03d}", "FLAG " + ",".join(flags) if flags else "ok", e, "corners", c, ci)
