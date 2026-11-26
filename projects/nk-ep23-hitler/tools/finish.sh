#!/bin/bash
# Package one chapter as a 1080p part once its clips are in out/renders/.
#   bash tools/finish.sh part <chapter>   → out/deliver/EP23_1080p_<NN>_<slug>.mp4   (chapter 0 = hook + title)
# Picture untouched (stream copy), sound levelled with ONE gain for the whole film: tools/gain.txt (dB), measured once on the
# narration of the hook and chapter 1 (target -14 LUFS for the voice) and kept, so every part matches. Peaks are limited.
# A part over 100 MB (the Drive upload limit) is compressed again (x264 crf 20).
#   VB=2300k bash tools/finish.sh 720 <name> <part files…>   → out/deliver/<name>.mp4, 1280x720, two-pass, from finished parts
set -e
. /tmp/hfenv.sh
cd "$(dirname "$0")/.."
mkdir -p out/deliver
G=$(cat tools/gain.txt)
AF="volume=${G}dB,alimiter=limit=0.8:attack=3:release=60:level=false"
case "$1" in
part)
  k=$2; cs=$(python3 tools/chclips.py $k)
  s=$([ "$k" = 0 ] && echo hook_title || printf "ch%02d" $k); o=$(printf "out/deliver/EP23_1080p_%02d_%s.mp4" $k $s)
  : > out/deliver/part.txt
  for c in $cs; do [ -s out/renders/$c.mp4 ] || { echo "missing $c"; exit 1; }; echo "file '../renders/$c.mp4'" >> out/deliver/part.txt; done
  ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i out/deliver/part.txt -c:v copy -af "$AF" -c:a aac -b:a 192k -ar 48000 -movflags +faststart $o
  if [ $(stat -c %s $o) -gt 100000000 ]; then
    ffmpeg -hide_banner -loglevel error -y -i $o -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a copy -movflags +faststart out/deliver/fit.mp4 && mv out/deliver/fit.mp4 $o
  fi
  echo "$o $(stat -c %s $o) $(ffprobe -v error -show_entries format=duration -of csv=p=0 $o)" ;;
720)
  name=$2; shift 2; : > out/deliver/list720.txt
  for f in "$@"; do echo "file '$(realpath $f)'" >> out/deliver/list720.txt; done
  o=out/deliver/$name.mp4
  V="-vf scale=1280:720:flags=lanczos -c:v libx264 -preset medium -b:v ${VB:-480k} -pix_fmt yuv420p -r 30"
  ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i out/deliver/list720.txt $V -pass 1 -passlogfile out/deliver/p720 -an -f mp4 /dev/null
  ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i out/deliver/list720.txt $V -pass 2 -passlogfile out/deliver/p720 -c:a aac -b:a 96k -ar 48000 -movflags +faststart $o
  echo "$o $(stat -c %s $o)" ;;
esac
