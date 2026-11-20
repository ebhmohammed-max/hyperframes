#!/usr/bin/env bash
# Join the episode 02 chunks into the master.
#
# Differs from the episode 01 assembler in one important way: each chunk records
# the preroll it was rendered with in <name>.lead, and the join trims exactly that
# many seconds. The old assembler trimmed a hardcoded 2 s and assumed every chunk
# had the same lead, which is how a half-finished fade survived to the master.
set -euo pipefail

cd /home/user/hyperframes || exit 1
export PATH=/home/user/hyperframes/.cache/bin:$PATH

SEG=renders/segments_ep002
WORK=.cache/assemble_ep002
OUT=renders/EP002_HARPY_AND_DRAGON_35MIN_1080p.mp4

mkdir -p "$WORK"; rm -f "$WORK"/*.mp4 "$WORK"/list.txt 2>/dev/null || true

for f in "$SEG"/ch*.mp4; do
  name=$(basename "$f" .mp4)
  lead_file="$SEG/$name.lead"
  lead=0
  [ -f "$lead_file" ] && lead=$(cat "$lead_file")
  if python3 -c "import sys; sys.exit(0 if float('$lead')<=0 else 1)"; then
    cp "$f" "$WORK/$name.mp4"; echo "== $name kept whole"
  else
    ffmpeg -hide_banner -loglevel error -ss "$lead" -i "$f" -c copy "$WORK/$name.mp4" -y
    echo "== $name trimmed ${lead}s of preroll"
  fi
done

for f in "$WORK"/ch*.mp4; do echo "file '$(realpath "$f")'" >> "$WORK/list.txt"; done
ffmpeg -hide_banner -loglevel error -f concat -safe 0 -i "$WORK/list.txt" \
       -c copy "$WORK/joined.mp4" -y

echo "== joined: $(ffprobe -v error -show_entries format=duration -of csv=p=0 "$WORK/joined.mp4") s"

ffmpeg -hide_banner -loglevel error -i "$WORK/joined.mp4" \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11" \
  -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart "$OUT" -y

echo "== delivered $OUT"; ls -lh "$OUT"
