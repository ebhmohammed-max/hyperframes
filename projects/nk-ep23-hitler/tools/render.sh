#!/bin/bash
# Render film clips that are not yet in out/renders/ (about 6 to 7 s of work per film second).
#   bash tools/render.sh [clips…]      e.g.  bash tools/render.sh N01 N02 TITLE      (no arguments: nothing; name the clips)
#   bash tools/render.sh ch 1          every clip of chapter 1 (ch 0 = hook: N01 N02 TITLE)
# Before: bash tools/setup.sh; narration mp3s in narration/; pictures in out/img; node film/gen.mjs <clips> (and film/title.mjs)
. /tmp/hfenv.sh
cd "$(dirname "$0")/.."
ln -sfn ../narration shared/vo; ln -sfn ../out/img shared/plates
mkdir -p out/renders
if [ "$1" = ch ]; then set -- $(python3 tools/chclips.py $2); fi
for c in "$@"; do
  o=$PWD/out/renders/$c.mp4
  [ -s "$o" ] && { echo "skip $c"; continue; }
  t0=$(date +%s)
  (cd film/$c && hyperframes render --quality looks --crf 18 --output /tmp/render_$c.mp4 > /tmp/render_$c.log 2>&1)
  if [ -s /tmp/render_$c.mp4 ]; then mv /tmp/render_$c.mp4 "$o"; echo "DONE $c $(( $(date +%s) - t0 ))s $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$o")"
  else echo "FAIL $c"; tail -5 /tmp/render_$c.log; fi
done
echo QUEUE-END
