#!/bin/bash
# Files ignored by git (out/, *.zip, *.mp3 ...) are NOT kept between sessions here; untracked files that
# are not ignored are kept. So the pictures live outside the project's .gitignore, in
#   <repo>/google_drive/ep12_pics/raw/NNN.jpg  and  <repo>/google_drive/ep12_pics/cast/<key>.jpg
# and out/raw, out/cast are symlinks to them. This script relinks, unpacks any EP12 zips downloaded from
# the Drive images folder into <repo>/google_drive/, and rebuilds out/img and the contact sheets.
#   bash tools/restore.sh      (needs /tmp/nkvenv with pillow; bash tools/setup.sh builds everything)
set -e
cd "$(dirname "$0")/.."
GD=../../google_drive; ST=$GD/ep12_pics
mkdir -p $ST/raw $ST/cast out/sheets out/up out/renders
[ -e out/raw ] || ln -s ../$ST/raw out/raw
[ -e out/cast ] || ln -s ../$ST/cast out/cast
for z in $GD/EP12_B*_images_*.zip; do
  [ -f "$z" ] || continue
  python3 - "$z" "$ST" <<'PY'
import sys, zipfile
z = zipfile.ZipFile(sys.argv[1])
for n in z.namelist():
    open(f"{sys.argv[2]}/raw/{n.split('_')[1]}.jpg", "wb").write(z.read(n))
print("restored", sys.argv[1], len(z.namelist()))
PY
  rm -f "$z"
done
# Redo zips (EP12_R1_..., EP12_R2_...) hold pictures made again later: unpack them after the batch zips so they win.
for z in $(ls $GD/EP12_R*_images_*.zip 2>/dev/null | sort); do
  python3 - "$z" "$ST" <<'PY'
import sys, zipfile
z = zipfile.ZipFile(sys.argv[1])
for n in z.namelist():
    open(f"{sys.argv[2]}/raw/{n.split('_')[1]}.jpg", "wb").write(z.read(n))
print("restored redo", sys.argv[1], len(z.namelist()))
PY
  rm -f "$z"
done
if [ -f $GD/EP12_cast.zip ]; then python3 - "$GD/EP12_cast.zip" "$ST" <<'PY'
import sys, zipfile, os
z = zipfile.ZipFile(sys.argv[1])
for n in z.namelist():
    if n.endswith(".jpg"): open(f"{sys.argv[2]}/cast/" + os.path.basename(n), "wb").write(z.read(n))
PY
rm -f $GD/EP12_cast.zip; fi
PY=/tmp/nkvenv/bin/python
last=$(ls $ST/raw | tail -1 | cut -c1-3); last=$((10#$last))
for a in $(seq 1 10 $last); do b=$((a+9)); $PY tools/sheet.py $a $b 2>/dev/null | grep -v "^size" || true; done
$PY tools/crops.py
echo "pictures: $(ls $ST/raw | wc -l), cast: $(ls $ST/cast | wc -l)"
