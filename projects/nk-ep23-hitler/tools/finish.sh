#!/bin/bash
# Package one chapter as a 1080p part once its clips are in out/renders/.
#   bash tools/finish.sh part <chapter>   → out/deliver/EP23_1080p_<NN>_<slug>.mp4   (chapter 0 = hook + title)
# Picture untouched (stream copy), sound levelled with ONE gain for the whole film: tools/gain.txt (dB), measured once on the
# narration of the hook and chapter 1 (target -14 LUFS for the voice) and kept, so every part matches. Peaks are limited.
# A chapter longer than about 5 minutes is cut at clip borders into pieces (…ch01a.mp4, …ch01b.mp4). A piece over 99 MB (the Drive
# upload limit is 100 MB) is encoded again, two-pass x264 sized to 95 MB. That can take several minutes: run it as a background process.
#   VB=2300k bash tools/finish.sh 720 <name> <part files…>   → out/deliver/<name>.mp4, 1280x720, two-pass, from finished parts
set -e
. /tmp/hfenv.sh
cd "$(dirname "$0")/.."
mkdir -p out/deliver
G=$(cat tools/gain.txt)
AF="volume=${G}dB,alimiter=limit=0.8:attack=3:release=60:level=false"
case "$1" in
part)
  k=$2; s=$([ "$k" = 0 ] && echo hook_title || printf "ch%02d" $k)
  # one file per chapter if it fits; otherwise the chapter is cut at clip borders into pieces of at most about 5 minutes (a, b, …)
  python3 - "$k" > out/deliver/groups.txt <<'PY'
import sys, subprocess, os
cs = subprocess.check_output(["python3", "tools/chclips.py", sys.argv[1]]).decode().split()
miss = [c for c in cs if not os.path.exists(f"out/renders/{c}.mp4") or os.path.getsize(f"out/renders/{c}.mp4") == 0]
if miss: print("MISSING " + " ".join(miss)); sys.exit(0)
d = [float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"out/renders/{c}.mp4"])) for c in cs]
n = max(1, -(-int(sum(d)) // 310)); want = sum(d) / n; g, t = [[]], 0
for c, x in zip(cs, d):
    if g[-1] and len(g) < n and t + x / 2 > want * len(g): g.append([])
    g[-1].append(c); t += x
for q in g: print(" ".join(q))
PY
  if grep -q MISSING out/deliver/groups.txt; then cat out/deliver/groups.txt; exit 1; fi
  ng=$(wc -l < out/deliver/groups.txt); i=0
  while read -r cs; do
    suf=""; [ "$ng" -gt 1 ] && suf=$(echo abcdefgh | cut -c$((i+1)))
    o=$(printf "out/deliver/EP23_1080p_%02d_%s%s.mp4" $k $s "$suf"); i=$((i+1))
    : > out/deliver/part.txt
    for c in $cs; do echo "file '../renders/$c.mp4'" >> out/deliver/part.txt; done
    ffmpeg -nostdin -hide_banner -loglevel error -y -f concat -safe 0 -i out/deliver/part.txt -c:v copy -af "$AF" -c:a aac -b:a 192k -ar 48000 -movflags +faststart $o
    if [ $(stat -c %s $o) -gt 99000000 ]; then
      # over the Drive upload limit: two-pass x264 sized to 95 MB
      dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $o)
      vb=$(python3 -c "print(int(95*8192/$dur-192))")
      ffmpeg -nostdin -hide_banner -loglevel error -y -i $o -c:v libx264 -preset medium -b:v ${vb}k -pix_fmt yuv420p -pass 1 -passlogfile out/deliver/pfit -an -f mp4 /dev/null
      ffmpeg -nostdin -hide_banner -loglevel error -y -i $o -c:v libx264 -preset medium -b:v ${vb}k -pix_fmt yuv420p -pass 2 -passlogfile out/deliver/pfit -c:a copy -movflags +faststart out/deliver/fit.mp4 && mv out/deliver/fit.mp4 $o
    fi
    echo "PART $o $(stat -c %s $o) $(ffprobe -v error -show_entries format=duration -of csv=p=0 $o)"
  done < out/deliver/groups.txt
  echo PARTS-END ;;
720)
  name=$2; shift 2; : > out/deliver/list720.txt
  for f in "$@"; do echo "file '$(realpath $f)'" >> out/deliver/list720.txt; done
  o=out/deliver/$name.mp4
  V="-vf scale=1280:720:flags=lanczos -c:v libx264 -preset medium -b:v ${VB:-480k} -pix_fmt yuv420p -r 30"
  ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i out/deliver/list720.txt $V -pass 1 -passlogfile out/deliver/p720 -an -f mp4 /dev/null
  ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i out/deliver/list720.txt $V -pass 2 -passlogfile out/deliver/p720 -c:a aac -b:a 96k -ar 48000 -movflags +faststart $o
  echo "$o $(stat -c %s $o)" ;;
esac
