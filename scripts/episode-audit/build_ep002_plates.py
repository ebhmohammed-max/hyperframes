"""Turn scene masters into the 1,050 plate slots the film expects.

Slot n belongs to scene ceil(n/15). If a scene's master exists, its fifteen
slots are filled from it with the framing table; if not, the slot is left
alone so a partial build can never corrupt a complete one.

Writes to a staging directory by default, because the render reads
assets/images continuously and a half-swapped set would blend two episodes.
"""
import os, sys, shutil
sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
from frame_plates import frame, SHOTS

MASTERS = "projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/art_dev/masters"
STAGE   = "projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/art_dev/plates"
PLATES_PER_SCENE = 15

def build(outdir=STAGE, scenes=None):
    os.makedirs(outdir, exist_ok=True)
    todo = scenes or range(1, 71)
    done, empty = [], []
    for sc in todo:
        m = os.path.join(MASTERS, f"{sc:03d}.jpg")
        if not os.path.exists(m):
            empty.append(sc); continue
        im = Image.open(m).convert("RGB")
        base = (sc - 1) * PLATES_PER_SCENE
        for k in range(PLATES_PER_SCENE):
            z, fx, fy = SHOTS[k]
            p = os.path.join(outdir, f"{base + k + 1:04d}.jpg")
            frame(im, z, fx, fy).save(p, quality=76, progressive=True, optimize=True)
        done.append(sc)
    return done, empty

if __name__ == "__main__":
    d, e = build()
    print(f"scenes built: {len(d)}  ->  {len(d)*PLATES_PER_SCENE} plates")
    print(f"scenes with no master yet: {e}")
