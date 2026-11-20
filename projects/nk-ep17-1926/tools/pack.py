#!/usr/bin/env python3
"""Zip pictures a..b (original size, shot-list file names) for Drive.  python tools/pack.py 11 20   (optional 3rd argument = batch number, e.g. pack.py 100 109 11)"""
import json, sys, zipfile, os
a, b = int(sys.argv[1]), int(sys.argv[2])
R = {r["n"]: r for r in json.load(open("shots/prompts.json", encoding="utf8"))}
os.makedirs("out/up", exist_ok=True)
B = int(sys.argv[3]) if len(sys.argv) > 3 else (a - 1) // 10 + 1
p = f"out/up/EP17_B{B:02d}_images_{a:03d}-{b:03d}.zip"
z = zipfile.ZipFile(p, "w", zipfile.ZIP_STORED)
for n in range(a, b + 1):
    if os.path.exists(f"out/raw/{n:03d}.jpg"): z.write(f"out/raw/{n:03d}.jpg", R[n]["file"])
    else: print("missing", n)
z.close(); print(p, os.path.getsize(p))
import shutil; shutil.copy(f"out/sheets/sheet_{a:03d}_{b:03d}.jpg", f"out/up/EP17_B{B:02d}_sheet.jpg")
