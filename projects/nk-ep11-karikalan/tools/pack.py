#!/usr/bin/env python3
"""Zip pictures a..b (original size, shot-list file names) for Drive.  python tools/pack.py 11 20"""
import json, sys, zipfile, os
a, b = int(sys.argv[1]), int(sys.argv[2])
R = {r["n"]: r for r in json.load(open("shots/prompts.json", encoding="utf8"))}
os.makedirs("out/up", exist_ok=True)
p = f"out/up/EP11_images_{a:03d}-{b:03d}.zip"
z = zipfile.ZipFile(p, "w", zipfile.ZIP_STORED)
for n in range(a, b + 1): z.write(f"out/raw/{n:03d}.jpg", R[n]["file"])
z.close(); print(p, os.path.getsize(p))
