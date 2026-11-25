import sys
from PIL import Image
ns=sys.argv[1:]
W,H=960,540
cols=2; rows=(len(ns)+1)//2
S=Image.new("RGB",(W*cols,H*rows))
for i,n in enumerate(ns):
    S.paste(Image.open(f"out/img/{n}.jpg").resize((W,H)),((i%cols)*W,(i//cols)*H))
S.save("/tmp/pair.jpg",quality=85)
