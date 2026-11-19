"""Report which Episode 02 scene masters exist and which are still to make.

The per-turn image limit is ten, so batches are ten scenes. This keeps the
next batch honest instead of guessing where the last one stopped.
"""
import os, json

MASTERS = ("projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/"
           "art_dev/masters")
BATCH = 10

def status():
    have = sorted(int(f[:3]) for f in os.listdir(MASTERS)
                  if f.endswith(".jpg") and f[:3].isdigit())
    missing = [i for i in range(1, 71) if i not in have]
    return have, missing

if __name__ == "__main__":
    have, missing = status()
    print(f"masters present: {len(have)}/70  ({len(have)*15} of 1050 plates)")
    if have:
        print(f"range: {have[0]:03d}..{have[-1]:03d}")
    # any gap inside the range is a real fault, not just an unfinished tail
    gaps = [i for i in range(have[0], have[-1] + 1) if i not in have] if have else []
    print("gaps inside range:", gaps or "none")
    if missing:
        nxt = missing[:BATCH]
        print(f"next batch: {nxt[0]:03d}-{nxt[-1]:03d}")
