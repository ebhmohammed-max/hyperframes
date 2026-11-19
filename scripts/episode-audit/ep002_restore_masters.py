"""Move connector-downloaded masters into the masters folder, verifying each.

The Drive connector drops downloads at google_drive/<name> relative to the repo
root. Masters must end up in art_dev/masters/<NNN>.jpg with the exact name the
plate builder expects, and a truncated or wrong-sized file must never be
silently accepted as a master.
"""
import os, shutil, sys
from PIL import Image

SRC = "google_drive"
DST = ("projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/"
       "art_dev/masters")

def main():
    os.makedirs(DST, exist_ok=True)
    moved, bad = [], []
    for f in sorted(os.listdir(SRC)):
        if not f.endswith(".jpg"):
            continue
        src = os.path.join(SRC, f)
        try:
            im = Image.open(src); im.verify()          # catches truncation
            im = Image.open(src)
            w, h = im.size
            if (w, h) != (1376, 768):
                raise ValueError(f"unexpected size {w}x{h}")
        except Exception as e:
            bad.append((f, str(e)[:60])); continue
        # Drive names them NNN_master.jpg; the builder wants NNN.jpg.
        # Getting this wrong fails silently: the file is present, valid, and
        # never matches a scene, so the plate set quietly stays short.
        stem = f.split("_")[0]
        dest = os.path.join(DST, f"{stem}.jpg")
        shutil.move(src, dest)
        moved.append(os.path.basename(dest))
    print(f"moved {len(moved)}: {', '.join(moved) if moved else 'none'}")
    if bad:
        print("REJECTED:")
        for f, e in bad:
            print(" ", f, e)
    have = sorted(int(f[:3]) for f in os.listdir(DST) if f.endswith(".jpg"))
    print(f"masters now: {len(have)}/70")
    return 0 if not bad else 1

if __name__ == "__main__":
    sys.exit(main())
