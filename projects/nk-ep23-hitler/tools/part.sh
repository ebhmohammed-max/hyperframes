#!/bin/bash
# Package a part by hand from rendered clips: bash tools/part.sh 03_ch03a N19 N20 N21 N22
# -> out/deliver/EP23_1080p_<name>.mp4 (stream copy of the picture, one gain and limiter on the sound;
#    two-pass x264 sized to 95 MB if the copy is over 99 MB). Upload only after PARTS-END.
set -e
. /tmp/hfenv.sh
cd "$(dirname "$0")/.."
name=$1; shift
mkdir -p out/deliver
G=$(cat tools/gain.txt)
AF="volume=${G}dB,alimiter=limit=0.75:attack=2:release=60:level=false"
o=out/deliver/EP23_1080p_$name.mp4
: > out/deliver/part.txt
for c in "$@"; do [ -f out/renders/$c.mp4 ] || { echo "MISSING $c"; exit 1; }; echo "file '../renders/$c.mp4'" >> out/deliver/part.txt; done
ffmpeg -nostdin -hide_banner -loglevel error -y -f concat -safe 0 -i out/deliver/part.txt -c:v copy -af "$AF" -c:a aac -b:a 192k -ar 48000 -movflags +faststart $o
echo "COPY $(stat -c %s $o)"
if [ $(stat -c %s $o) -gt 99000000 ]; then
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $o)
  vb=$(python3 -c "print(int(95*8192/$dur-192))")
  echo "TWOPASS ${vb}k"
  ffmpeg -nostdin -hide_banner -loglevel error -y -i $o -c:v libx264 -preset medium -b:v ${vb}k -pix_fmt yuv420p -pass 1 -passlogfile out/deliver/pfit -an -f mp4 /dev/null
  ffmpeg -nostdin -hide_banner -loglevel error -y -i $o -c:v libx264 -preset medium -b:v ${vb}k -pix_fmt yuv420p -pass 2 -passlogfile out/deliver/pfit -c:a copy -movflags +faststart out/deliver/fit.mp4 && mv out/deliver/fit.mp4 $o
fi
echo "PART $o $(stat -c %s $o) $(ffprobe -v error -show_entries format=duration -of csv=p=0 $o)"
echo PARTS-END
