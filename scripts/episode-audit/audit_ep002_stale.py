"""Report which rendered chunks no longer match the art they were built from.

A chunk is stale if any master inside its span was changed after the chunk's
mp4 was written. This exists because the failure is silent and expensive: the
assembler will happily join a chunk captured against a superseded plate and the
only symptom is a wrong image somewhere in the middle of the film, which is
then found by eye, late, after a re-render.

Scene N occupies block N-1, and each block is 30 s, so scene N spans
[(N-1)*30, N*30). Chunk spans come from render_ep002_documentary.sh.

    .venv/bin/python scripts/episode-audit/audit_ep002_stale.py [--json]

Exit 0 = every existing chunk is current. Exit 1 = at least one is stale or
missing. Missing chunks are reported but do not fail the run, because a
partially rendered film is a normal state to resume from.
"""
import glob
import json
import os
import subprocess
import sys
import time

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SEG = os.path.join(REPO, "renders", "segments_ep002")
MASTERS = os.path.join(
    REPO,
    "projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/art_dev/masters",
)

# name, start, end -- keep in step with CHUNKS in render_ep002_documentary.sh
CHUNKS = [
    ("ch01", 0.0, 296.5),
    ("ch02", 296.5, 596.5),
    ("ch03", 596.5, 896.5),
    ("ch04", 896.5, 1200.0),
    ("ch05", 1200.0, 1500.0),
    ("ch06", 1500.0, 1800.0),
    ("ch07", 1800.0, 2100.0),
]
BLOCK = 30.0


def master_mtimes():
    """Last-commit time for each master, falling back to filesystem mtime.

    Commit time is used rather than file mtime because a rebuild of the plates
    does not rewrite the masters; what matters is when the image itself last
    changed.
    """
    out = {}
    for path in sorted(glob.glob(os.path.join(MASTERS, "*.jpg"))):
        n = int(os.path.basename(path)[:3])
        r = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", path],
            capture_output=True,
            text=True,
            cwd=REPO,
        )
        stamp = r.stdout.strip()
        out[n] = int(stamp) if stamp else int(os.path.getmtime(path))
    return out


def main(argv):
    want_json = "--json" in argv
    fixed = master_mtimes()
    rows = []
    stale_found = False

    for name, start, end in CHUNKS:
        path = os.path.join(SEG, f"{name}.mp4")
        first = int(start // BLOCK) + 1
        last = int((end - 0.001) // BLOCK) + 1
        if not os.path.exists(path):
            rows.append({"chunk": name, "status": "missing", "scenes": [], "rendered": None})
            continue
        rendered = int(os.path.getmtime(path))
        stale = [n for n in range(first, last + 1) if fixed.get(n, 0) > rendered]
        if stale:
            stale_found = True
        rows.append(
            {
                "chunk": name,
                "status": "stale" if stale else "current",
                "scenes": stale,
                "rendered": time.strftime("%Y-%m-%d %H:%M", time.gmtime(rendered)),
            }
        )

    if want_json:
        print(json.dumps(rows, indent=2))
    else:
        print(f"{'chunk':6} {'status':9} {'rendered':17} stale scenes")
        for r in rows:
            when = r["rendered"] or "-"
            scenes = " ".join(f"{n:03d}" for n in r["scenes"]) or "-"
            print(f"{r['chunk']:6} {r['status']:9} {when:17} {scenes}")

    return 1 if stale_found else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
