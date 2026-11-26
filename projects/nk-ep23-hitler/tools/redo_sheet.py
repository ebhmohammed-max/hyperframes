#!/usr/bin/env python3
"""Review sheet for remade pictures.  $PY tools/redo_sheet.py <sheet name> <n> <n> ...  -> google_drive/_sheet_<name>.jpg
3 per row at 640x360, from out/img (run tools/restore.sh first so out/img holds the new crops)."""
import sys, os
from PIL import Image, ImageDraw
name, ns = sys.argv[1], [int(x) for x in sys.argv[2:]]
G = os.path.abspath("../../google_drive"); rows = (len(ns) + 2) // 3
S = Image.new("RGB", (1920, rows * 360), (20, 20, 20)); d = ImageDraw.Draw(S)
for i, n in enumerate(ns):
    x, y = (i % 3) * 640, (i // 3) * 360
    S.paste(Image.open(f"out/img/{n:03d}.jpg").resize((640, 360), Image.LANCZOS), (x, y))
    d.rectangle([x, y, x + 34, y + 14], fill=(0, 0, 0)); d.text((x + 4, y + 1), f"{n:03d}", fill=(255, 255, 255))
S.save(f"{G}/_sheet_{name}.jpg", quality=88); print("sheet", name, len(ns))
