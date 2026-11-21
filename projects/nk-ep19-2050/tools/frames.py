#!/usr/bin/env python3
"""Frame sheet from a render.  python tools/frames.py video.mp4 out.jpg t1 t2 ..."""
import sys, subprocess, os, io
from PIL import Image
FF = os.environ.get("HYPERFRAMES_FFMPEG_PATH", "ffmpeg")
v, out, ts = sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3:]]
ims = []
for t in ts:
    raw = subprocess.run([FF, "-v", "error", "-ss", str(t), "-i", v, "-frames:v", "1", "-vf", "scale=640:360", "-f", "image2pipe", "-vcodec", "mjpeg", "-q:v", "3", "-"], capture_output=True).stdout
    ims.append(Image.open(io.BytesIO(raw)).convert("RGB"))
cols = 3; rows = (len(ims) + cols - 1) // cols
S = Image.new("RGB", (cols * 640, rows * 360))
for i, im in enumerate(ims): S.paste(im, ((i % cols) * 640, (i // cols) * 360))
S.save(out, quality=82)
