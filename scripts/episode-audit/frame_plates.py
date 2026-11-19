"""Derive 15 plate framings from one scene master.

Every frame is a true 16:9 window fully inside the master, so no crop can run
past an edge and introduce the black bars that a naive fractional crop gives.
The window slides and tightens across the scene, which is what a camera does
inside one shot.
"""
import sys, os
from PIL import Image

W_OUT, H_OUT = 1376, 768
AR = W_OUT / H_OUT

# (zoom, focus_x, focus_y). zoom 1.0 = whole frame; higher = tighter.
# focus is the point of interest in 0..1 master coordinates.
SHOTS = [
    (1.00, 0.50, 0.50), (1.08, 0.45, 0.52), (1.16, 0.58, 0.48),
    (1.06, 0.35, 0.55), (1.10, 0.68, 0.50), (1.28, 0.52, 0.46),
    (1.35, 0.40, 0.52), (1.20, 0.30, 0.58), (1.14, 0.62, 0.54),
    (1.05, 0.50, 0.38), (1.45, 0.55, 0.50), (1.30, 0.35, 0.62),
    (1.22, 0.65, 0.58), (1.12, 0.45, 0.66), (1.18, 0.50, 0.50),
]

def frame(im, zoom, fx, fy, out=W_OUT, h_out=H_OUT):
    W, H = im.size
    # largest 16:9 window at this zoom that fits the master
    w = W / zoom
    h = w / AR
    if h > H:
        h = H / (zoom / 1.0) if False else H
        h = H
        w = h * AR
    if w > W:
        w = W
        h = w / AR
    # clamp the window inside the image, honouring the focus point
    x = min(max(fx * W - w / 2, 0), W - w)
    y = min(max(fy * H - h / 2, 0), H - h)
    box = (int(round(x)), int(round(y)), int(round(x + w)), int(round(y + h)))
    return im.crop(box).resize((out, h_out), Image.LANCZOS)

def main(master, outdir, start=1, count=15):
    os.makedirs(outdir, exist_ok=True)
    im = Image.open(master).convert("RGB")
    made = []
    for i in range(count):
        z, fx, fy = SHOTS[i % len(SHOTS)]
        p = os.path.join(outdir, f"{start + i:04d}.jpg")
        frame(im, z, fx, fy).save(p, quality=82, progressive=True, optimize=True)
        made.append(p)
    return made

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 1)
