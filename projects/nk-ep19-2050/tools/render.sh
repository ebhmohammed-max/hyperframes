#!/bin/bash
# Render every film clip that is not yet in out/renders/ (about 4.5 s of work per film second on 2 CPUs).
#   bash tools/render.sh [clips…]      default: TITLE N01 END N02 … N07
# Before: bash tools/setup.sh; narration mp3s in narration/; pictures in out/img;
#         node film/gen.mjs N01 … N07 && node film/title.mjs && node film/end.mjs
. /tmp/hfenv.sh
cd "$(dirname "$0")/.."
ln -sfn ../narration shared/vo; ln -sfn ../out/img shared/plates
mkdir -p out/renders
for c in ${@:-TITLE N01 END N02 N03 N04 N05 N06 N07}; do
  o=$PWD/out/renders/$c.mp4
  [ -s "$o" ] && { echo "skip $c"; continue; }
  t0=$(date +%s)
  (cd film/$c && hyperframes render --quality looks --crf 18 --output /tmp/render_$c.mp4 > /tmp/render_$c.log 2>&1)
  if [ -s /tmp/render_$c.mp4 ]; then mv /tmp/render_$c.mp4 "$o"; echo "DONE $c $(( $(date +%s) - t0 ))s $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$o")"
  else echo "FAIL $c"; tail -5 /tmp/render_$c.log; fi
done
echo QUEUE-END
