"""Emit the exact prompt for any scene master, from one source of truth.

Every image is generated from this file's output, never from a prompt written
by hand inside a conversation. Hand-written prompts are how the Roman legions,
the Greek aspides and the Victorian counter scale got in: the direction text
drifted from the film's world and nothing checked it.

  python ep002_prompts.py 7            # one scene
  python ep002_prompts.py 1 7 62       # several
  python ep002_prompts.py --missing    # only scenes with no master
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MASTERS = (HERE.parents[1] / "projects/ancient_world_of_ice_and_fire/episodes"
           / "ep002_harpy_and_dragon/art_dev/masters")

spec = importlib.util.spec_from_file_location("dirs", HERE / "ep002_scene_directions.py")
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)


def prompt(n: int) -> str:
    desc, palette = D.SCENES[n]
    return f"{desc} Palette: {palette}. {D.STYLE} {D.BAN}"


def missing() -> list[int]:
    have = {int(f[:3]) for f in (p.name for p in MASTERS.iterdir())
            if f.endswith(".jpg")}
    return [n for n in sorted(D.SCENES) if n not in have]


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--missing"]:
        nums = missing()
        if not nums:
            print("all 70 present")
    elif args == ["--all"]:
        nums = sorted(D.SCENES)
    else:
        nums = [int(a) for a in args]
    for n in nums:
        if args == ["--missing"]:
            print(f"--- {n:03d}")
        else:
            print(f"--- {n:03d}")
        print(prompt(n))
        print()
