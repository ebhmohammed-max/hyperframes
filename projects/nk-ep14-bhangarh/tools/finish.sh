#!/bin/bash
# Join, level and package the film once every clip is in out/renders/.
#   bash tools/finish.sh parts   → out/deliver/EP14_1080p_NN_<slug>.mp4, seven parts (picture untouched, sound levelled)
#   VB=1000k bash tools/finish.sh 720   → out/deliver/EP14_Bhangarh_full_720p.mp4 (one file under 100 MB; 1000k fits a film of about 10 min 45 s, 690k fits 16 min)
# One gain for the whole film (measured on the joined sound, target -14 LUFS, peaks limited), so every part matches.
set -e
. /tmp/hfenv.sh
cd "$(dirname "$0")/.."
ORDER="N01:hook TITLE:title N02:ch1 N03:ch2 N04:ch3 N05:ch4 N06:ch5 N07:ch6 END:endcard"
mkdir -p out/deliver
L=out/deliver/list.txt; : > $L
for x in $ORDER; do c=${x%%:*}; [ -s out/renders/$c.mp4 ] || { echo "missing $c"; exit 1; }; echo "file '../renders/$c.mp4'" >> $L; done
if [ ! -s out/deliver/gain.txt ]; then
  ffmpeg -hide_banner -nostats -f concat -safe 0 -i $L -vn -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2> out/deliver/measure.txt
  $PY - <<'PY'
import json,re
t=open('out/deliver/measure.txt').read(); j=json.loads(t[t.rindex('{'):t.rindex('}')+1])
g=round(-14-float(j['input_i']),2)
open('out/deliver/gain.txt','w').write(str(g))
print('measured', j['input_i'], 'LUFS, peak', j['input_tp'], 'dBTP → gain', g, 'dB')
PY
fi
G=$(cat out/deliver/gain.txt)
AF="volume=${G}dB,alimiter=limit=0.8:attack=3:release=60:level=false"
case "$1" in
parts)
  # seven parts in running order; the title rides with the hook and the end card with the last chapter
  rm -f out/deliver/EP14_1080p_*.mp4
  i=0
  for x in N01+TITLE:hook_title N02:ch1 N03:ch2 N04:ch3 N05:ch4 N06:ch5 N07+END:ch6_endcard; do
    cs=${x%%:*}; s=${x##*:}; i=$((i+1)); o=$(printf "out/deliver/EP14_1080p_%02d_%s.mp4" $i $s)
    : > out/deliver/part.txt; for c in ${cs//+/ }; do echo "file '../renders/$c.mp4'" >> out/deliver/part.txt; done
    ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i out/deliver/part.txt -c:v copy -af "$AF" -c:a aac -b:a 192k -ar 48000 -movflags +faststart $o
    # the Drive upload takes at most 100 MB per file: a larger part is compressed again (x264 crf 20), sound untouched
    if [ $(stat -c %s $o) -gt 100000000 ]; then
      ffmpeg -hide_banner -loglevel error -y -i $o -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a copy -movflags +faststart out/deliver/fit.mp4 && mv out/deliver/fit.mp4 $o
    fi
    echo "$o $(stat -c %s $o) $(ffprobe -v error -show_entries format=duration -of csv=p=0 $o)"
  done ;;
720)
  o=out/deliver/EP14_Bhangarh_full_720p.mp4
  V="-vf scale=1280:720:flags=lanczos -c:v libx264 -preset medium -b:v ${VB:-840k} -pix_fmt yuv420p -r 30"
  ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i $L $V -pass 1 -passlogfile out/deliver/p720 -an -f mp4 /dev/null
  ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i $L $V -pass 2 -passlogfile out/deliver/p720 -af "$AF" -c:a aac -b:a 112k -ar 48000 -movflags +faststart $o
  echo "$o $(stat -c %s $o)" ;;
esac
