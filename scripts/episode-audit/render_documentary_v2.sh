#!/usr/bin/env bash
# Render the 35-minute documentary in chapter chunks, verifying each one.
#
#   bash scripts/episode-audit/render_documentary_v2.sh [first_chunk]
#
# Why chunks: measured capture is ~6.3 s of wall clock per second of film, so the full
# 35:00 is about 3h45m. One process that long is a single point of failure; seven
# chapter renders of 25-35 min each survive a stall, and the job resumes where it
# stopped because a finished segment is never re-rendered.
#
# Chunks overlap by 2 s so nothing is lost at a cut: chapter assembly trims the lead.
set -uo pipefail

cd /home/user/hyperframes
export PATH=/home/user/hyperframes/.cache/bin:$PATH
# The renderer resolves its own ffmpeg/ffprobe through these, and .cache/bin/ffprobe is a
# symlink into .cache/film-tools (a real ffmpeg-static install). Deleting that directory
# to free disk breaks every render with "ffprobe not found" — it is load-bearing.
export HYPERFRAMES_FFPROBE_PATH=/home/user/hyperframes/.cache/bin/ffprobe
export HYPERFRAMES_FFMPEG_PATH=/home/user/hyperframes/.cache/bin/ffmpeg
export LD_LIBRARY_PATH=/home/user/hyperframes/.cache/chromium-libs/lib
export HYPERFRAMES_BROWSER_PATH=/tmp/chromium

PROJ=projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/documentary_v2
SEG=renders/segments_v2
LOG=.cache/render-docv2
mkdir -p "$SEG" "$LOG"

# name  start  end  (the two-second lead is trimmed at assembly)
CHUNKS=(
  "ch1:0:300"
  "ch2:298:600"
  "ch3:598:900"
  "ch4:898:1230"
  "ch5:1228:1530"
  "ch6:1528:1830"
  "ch7:1828:2100"
)

START_AT="${1:-ch1}"

probe() {  # duration of a media file, in seconds
  ffprobe -v error -show_entries format=duration -of csv=p=0 "$1" 2>/dev/null | head -1
}

for spec in "${CHUNKS[@]}"; do
  IFS=: read -r name a b <<<"$spec"
  if [ "$name" \< "$START_AT" ]; then continue; fi
  out="$SEG/$name.mp4"
  want=$(python3 -c "print(f'{$b-$a:.1f}')")

  if [ -f "$out" ]; then
    got=$(probe "$out")
    ok=$(python3 -c "print('yes' if abs(${got:-0}-$want) < 0.6 else 'no')")
    if [ "$ok" = "yes" ]; then
      echo "== $name already rendered (${got}s), skipping"
      continue
    fi
    echo "== $name exists but is short (${got:-0}s vs ${want}s), re-rendering"
    rm -f "$out"
  fi

  avail=$(df -Pm /home/user | awk 'NR==2{print $4}')
  if [ "${avail:-0}" -lt 3000 ]; then
    echo "!! only ${avail} MB free; stopping before $name so the segment is not truncated"
    exit 2
  fi
  echo "== $name  [$a -> $b]  $want s  (${avail} MB free)  $(date -u +%H:%M:%SZ)"
  node packages/cli/bin/hyperframes.mjs render "$PROJ" -o "$out" \
      --start "$a" --end "$b" -q looks 2>&1 | tee "$LOG/$name.log" | tail -3

  got=$(probe "$out")
  if [ -z "${got:-}" ]; then echo "!! $name produced nothing"; exit 1; fi
  echo "== $name done: ${got}s, $(du -h "$out" | cut -f1)  $(date -u +%H:%M:%SZ)"
done

echo "== all requested chunks rendered  $(date -u +%H:%M:%SZ)"
ls -lh "$SEG"
