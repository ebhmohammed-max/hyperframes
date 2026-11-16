#!/bin/bash
# out/ is not saved between sessions. The pictures live in pics/ (saved, not in git); this relinks them
# and rebuilds the film copies. If pics/ is empty too: download the EP11_Bnn zips and EP11_cast.zip from
# the Drive images folder into <repo>/google_drive/ first, then run this.
#   bash tools/restore.sh      (needs /tmp/nkvenv; bash tools/setup.sh builds it)
set -e
cd "$(dirname "$0")/.."
mkdir -p pics/raw pics/cast out/sheets out/up out/renders
[ -e out/raw ] || ln -s ../pics/raw out/raw
[ -e out/cast ] || ln -s ../pics/cast out/cast
GD=../../google_drive
for z in $GD/EP11_B*_images_*.zip; do
  [ -f "$z" ] || continue
  python3 - "$z" <<'PY'
import sys, zipfile
z = zipfile.ZipFile(sys.argv[1])
for n in z.namelist():
    open(f"pics/raw/{n.split('_')[1]}.jpg", "wb").write(z.read(n))
print("restored", sys.argv[1], len(z.namelist()))
PY
done
if [ -f $GD/EP11_cast.zip ]; then python3 - <<'PY'
import zipfile, os
z = zipfile.ZipFile("../../google_drive/EP11_cast.zip")
for n in z.namelist():
    if n.endswith(".jpg"): open("pics/cast/" + os.path.basename(n), "wb").write(z.read(n))
print("cast", [n for n in z.namelist()])
PY
fi
PY=/tmp/nkvenv/bin/python
last=$(ls pics/raw | tail -1 | cut -c1-3); last=$((10#$last))
for a in $(seq 1 10 $last); do b=$((a+9)); $PY tools/sheet.py $a $b 2>/dev/null | grep -v "^size" || true; done
$PY tools/crops.py
echo "pictures: $(ls pics/raw | wc -l), cast: $(ls pics/cast | wc -l)"
