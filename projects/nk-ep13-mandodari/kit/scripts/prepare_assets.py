"""Prepare shared assets from the EP06 Act 1 source set.
- plates: Lanczos upscale 1376x768 -> 2304x1286 + light unsharp, JPEG q88
- audio: cut the cold-open narration excerpts from the Act 1 master
Run: python scripts/prepare_assets.py <ffmpeg> <act1_narration.mp3>
"""
import sys, subprocess, glob, os
from PIL import Image, ImageFilter
ff, master = sys.argv[1], sys.argv[2]
USED = "SH010 SH014 SH001 SH011 SH005A SH005_ SH002 SH008 SH003 SH007 SH004 SH006 SH012 SH015 SH017 SH018_ SH023".split()
for f in sorted(glob.glob('source/plates/*.jpg')):
    b = os.path.basename(f)
    if not any(b.startswith(u) for u in USED): continue
    im = Image.open(f).convert('RGB')
    im = im.resize((2304, 1286), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=1.6, percent=55, threshold=2))
    out = 'shared/plates/' + b.split('_')[0].lower() + '.jpg'
    im.save(out, quality=88, optimize=True, progressive=True)
    print(out, os.path.getsize(out)//1024, 'KB')
def cut(name, ss, t):
    subprocess.run([ff,'-hide_banner','-loglevel','error','-y','-ss',str(ss),'-t',str(t),'-i',master,
      '-af',f'afade=t=in:st=0:d=0.04,afade=t=out:st={t-0.25}:d=0.25,loudnorm=I=-15:TP=-1.5:LRA=11',
      '-ar','48000','-ac','2','-c:a','libmp3lame','-b:a','192k',f'shared/audio/{name}.mp3'],check=True)
cut('vo_full', 0, 51.6)
cut('vo_a', 0, 20.62)
cut('vo_b', 20.5, 31.1)
