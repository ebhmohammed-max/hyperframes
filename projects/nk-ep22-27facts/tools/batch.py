#!/usr/bin/env python3
"""Zip a picture batch for Drive and build a review sheet.
  $PY tools/batch.py <batch no> <first> <last> [big picture numbers ...]
Writes google_drive/ep22_up/EP22_Bnn_images_aaa-bbb.zip (and a copy in out/up/) and google_drive/_sheet_E22Bnn.jpg
(4 thumbnails per row, the 'big' pictures at half size underneath). Run tools/restore.sh first."""
import json, zipfile, os, shutil, sys
from PIL import Image, ImageDraw
B, a, b = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); big = [int(x) for x in sys.argv[4:]]
R = {r["n"]: r for r in json.load(open("shots/prompts.json", encoding="utf8"))}
G = os.path.abspath("../../google_drive"); os.makedirs(f"{G}/ep22_up", exist_ok=True); os.makedirs("out/up", exist_ok=True)
ns = list(range(a, b + 1)); name = f"EP22_B{B:02d}_images_{a:03d}-{b:03d}.zip"; p = f"{G}/ep22_up/{name}"
z = zipfile.ZipFile(p, "w", zipfile.ZIP_STORED)
for n in ns: z.write(f"out/raw/{n:03d}.jpg", R[n]["file"])
z.close(); shutil.copy(p, "out/up/"); print(name, os.path.getsize(p))
rows = (len(ns) + 3) // 4; H = rows * 270 + (540 if big else 0)
S = Image.new("RGB", (1920, H), (20, 20, 20)); d = ImageDraw.Draw(S)
for i, n in enumerate(ns):
    x, y = (i % 4) * 480, (i // 4) * 270
    S.paste(Image.open(f"out/img/{n:03d}.jpg").resize((480, 270)), (x, y))
    d.rectangle([x, y, x + 34, y + 14], fill=(0, 0, 0)); d.text((x + 4, y + 1), f"{n:03d}", fill=(255, 255, 255))
for i, n in enumerate(big[:2]): S.paste(Image.open(f"out/img/{n:03d}.jpg").resize((960, 540)), (i * 960, rows * 270))
S.save(f"{G}/_sheet_E22B{B:02d}.jpg", quality=88)  # a new name per batch: the viewer can show an old copy of a reused name
