"""Procedural textures + baked looks used by the style samples (deterministic, seeded)."""
import numpy as np, glob, os
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
rs = np.random.RandomState(6)
def save(a, p, **k): Image.fromarray(np.clip(a,0,255).astype('uint8')).save(p, **k); print(p, os.path.getsize(p)//1024,'KB')

# 1. film grain tile: neutral grey noise, used with overlay blend
g = rs.normal(128, 26, (512,512))
g = np.array(Image.fromarray(np.clip(g,0,255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.6)), dtype=float)
save(np.stack([g,g,g],-1), 'shared/tex/grain.png', optimize=True)

# 2. OLA palm-leaf / laid paper ground 1920x1080
H,W = 1080,1920
base = np.array([232,219,187], float)  # Palm #E8DBBB
n = rs.normal(0,1,(H,W))
fib = np.array(Image.fromarray(((n-n.min())/(n.max()-n.min())*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1)).resize((W,H)),float)/255-0.5
# long horizontal fibres (palm leaf veins)
lines = rs.normal(0,1,(H,1)); lines = np.repeat(lines, W, 1)
lines = np.array(Image.fromarray(((lines-lines.min())/(lines.max()-lines.min())*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2)),float)/255-0.5
blot = rs.normal(0,1,(H//40,W//40)); blot = np.array(Image.fromarray(((blot-blot.min())/(blot.max()-blot.min())*255).astype('uint8')).resize((W,H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(30)),float)/255-0.5
yy,xx = np.mgrid[0:H,0:W]; d = np.sqrt(((xx-W/2)/(W/2))**2+((yy-H/2)/(H/2))**2)
vig = np.clip(1-0.16*np.clip(d-0.55,0,None)**1.4*3,0.7,1)
lum = 1 + fib*0.10 + lines*0.09 + blot*0.10
img = base[None,None,:]*lum[...,None]*vig[...,None]
img[...,2] *= (1 - 0.03*np.clip(d,0,1.4))[...]
save(img, 'shared/tex/ola_paper.jpg', quality=88)

# 3. dark archive board (felt/desk) 1920x1080
n = rs.normal(0,1,(H,W))
f = np.array(Image.fromarray(((n-n.min())/(n.max()-n.min())*255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.8)),float)/255-0.5
b2 = np.array([30,33,31],float)[None,None,:]*(1+f*0.55+blot*0.5)[...,None]*np.clip(1.08-0.38*d,0.5,1.1)[...,None]
save(b2, 'shared/tex/board.jpg', quality=86)

# 4. sepia / orthochromatic bake of the plates for the vintage-film style, 4:3 centre crop
for p in sorted(glob.glob('shared/plates/*.jpg')):
    im = Image.open(p).convert('RGB')
    w,h = im.size; cw = int(h*4/3); im = im.crop(((w-cw)//2,0,(w-cw)//2+cw,h)).resize((1600,1200), Image.LANCZOS)
    a = np.array(im,float)
    lumi = a[...,0]*0.2+a[...,1]*0.55+a[...,2]*0.25          # blue-sensitive stock: reds fall dark
    lumi = 255*np.clip((lumi/255-0.5)*1.28+0.52,0,1)**0.92
    lumi = np.array(Image.fromarray(lumi.astype('uint8')).filter(ImageFilter.GaussianBlur(0.9)),float)
    halo = np.array(Image.fromarray(lumi.astype('uint8')).filter(ImageFilter.GaussianBlur(14)),float)
    lumi = np.clip(lumi*0.86+np.clip(halo-150,0,None)*0.55+14,0,255)   # lifted blacks, glowing highlights
    t = lumi/255
    sep = np.stack([t*255*1.02+6, t*255*0.90+3, t*255*0.72],-1)
    save(sep, 'shared/plates_sepia/'+os.path.basename(p), quality=86)
