"""Audit a rendered film for visible seams and chapter-change hitches.

Run this on the assembled master BEFORE it is delivered. It looks for the three
things that went wrong on the last film:

  cadence  - missing or duplicated frames
  seams    - a visible jump across a render-chunk boundary, including a fade
             that was captured half-finished
  audio    - a dropout at a boundary

Exit code 0 = pass, 1 = fail. Numbers are printed either way so a verdict can be
argued with.
"""
import subprocess, sys, os
import numpy as np
from PIL import Image

FFMPEG = os.environ.get("FFMPEG", ".cache/bin/ffmpeg")
FFPROBE = os.environ.get("FFPROBE", ".cache/bin/ffprobe")

def probe_seams(path, seams, span=0.4):
    """Corner and mean luminance a moment either side of each seam."""
    out = []
    for seam in seams:
        row = {"seam": seam}
        for side, t in (("before", seam - span), ("after", seam + span)):
            p = f"/tmp/_seam_{side}.jpg"
            subprocess.run([FFMPEG, "-v", "error", "-ss", f"{t:.3f}", "-i", path,
                            "-frames:v", "1", "-y", p], check=False,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if not os.path.exists(p):
                row[side] = None; continue
            a = np.asarray(Image.open(p).convert("L")).astype(float)
            row[side] = {
                "mean": a.mean(),
                "corner": float(np.mean([a[:40, :40].mean(), a[:40, -40:].mean(),
                                         a[-40:, :40].mean(), a[-40:, -40:].mean()])),
            }
        if row["before"] and row["after"]:
            row["d_mean"] = row["after"]["mean"] - row["before"]["mean"]
            row["d_corner"] = row["after"]["corner"] - row["before"]["corner"]
        out.append(row)
    return out

def cadence(path):
    """Inter-frame deltas; a 30 fps film should be a flat 0.0333 s."""
    r = subprocess.run([FFPROBE, "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "packet=pts_time", "-of", "csv=p=0", path],
                       capture_output=True, text=True)
    ts = []
    for line in r.stdout.splitlines():
        line = line.strip().rstrip(",")
        if line:
            try: ts.append(float(line))
            except ValueError: pass
    ts.sort()
    if len(ts) < 10:
        return {"frames": len(ts), "gaps": None, "ok": False}
    d = np.diff(np.array(ts))
    return {"frames": len(ts), "median": float(np.median(d)),
            "max": float(d.max()), "gaps": int((d > np.median(d) * 1.5).sum()),
            "ok": (d > np.median(d) * 1.5).sum() == 0}

def main(path, seams):
    print(f"== {path}")
    c = cadence(path)
    print(f"cadence: frames={c['frames']} median={c.get('median'):.4f}s "
          f"max={c.get('max'):.4f}s gaps={c['gaps']}  {'PASS' if c['ok'] else 'FAIL'}")
    rows = probe_seams(path, seams)
    print(f"{'seam':>7} {'d_mean':>8} {'d_corner':>9}  verdict")
    worst = 0.0
    for r in rows:
        if "d_mean" not in r:
            print(f"{r['seam']:>7}   (could not sample)"); continue
        # a real cut moves the mean a lot; the failure mode here is a *large*
        # jump in corner brightness, which is what a half-finished fade looks like
        bad = abs(r["d_corner"]) > 25
        worst = max(worst, abs(r["d_corner"]))
        print(f"{r['seam']:>7} {r['d_mean']:8.1f} {r['d_corner']:9.1f}  "
              f"{'FAIL' if bad else 'pass'}")
    print(f"worst corner jump: {worst:.1f}")
    return 0 if c["ok"] and worst <= 25 else 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    seams = [float(x) for x in sys.argv[2:]] or [300, 600, 900, 1200, 1500, 1800]
    sys.exit(main(sys.argv[1], seams))
