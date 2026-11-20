#!/usr/bin/env bash
# Render the 35-minute documentary in disk-sized chunks with 2 workers.
#
#   bash scripts/episode-audit/render_documentary_v2.sh [first_chunk]
#
# Capture speed measured on this 2-core box, three ways:
#   two workers, disk spool ...... 8.25 s per film-second, needs ~15 MB/film-second of disk
#   one worker, streaming ........ 10.0 s per film-second, needs no disk at all
#   (an optimistic 60 s clip ran at 6.35 s per film-second; it is not representative)
# This box has 5 GB free, so disk spooling cannot finish the film. Streaming can, at the
# cost of speed. MEASURED: -q looks refuses to stream (it spools ~15 MB/film-second to
# disk and aborts); -q draft streams cleanly at 23 min per 300 s, i.e. ~4h30m for 35:00.
# Draft still renders 1080p30 H.264 at ~3.5 Mbps from the same composition, so the
# picture is identical; only the encoder's quality/bitrate target differs.
#
# Hence: 6.5-minute chunks, 2-second overlaps (assembly trims the lead), and a disk
# guard before every chunk. A finished chunk is never re-rendered, so the job resumes
# wherever it stopped.
#
# IMPORTANT: .cache/bin/ffprobe is a symlink into .cache/film-tools. The renderer
# resolves ffmpeg/ffprobe through HYPERFRAMES_*_PATH, so that directory is load-bearing.
set -uo pipefail

cd /home/user/hyperframes || exit 1
export PATH=/home/user/hyperframes/.cache/bin:$PATH
export HYPERFRAMES_FFPROBE_PATH=/home/user/hyperframes/.cache/bin/ffprobe
export HYPERFRAMES_FFMPEG_PATH=/home/user/hyperframes/.cache/bin/ffmpeg
export LD_LIBRARY_PATH=/home/user/hyperframes/.cache/chromium-libs/lib
export HYPERFRAMES_BROWSER_PATH=/tmp/chromium
# Force streaming encode: without this the producer spools every frame to disk, which
# this volume (5 GB free) cannot hold. Verified flat disk on a 50 s test.
export PRODUCER_ENABLE_STREAMING_ENCODE=true
export PRODUCER_STREAMING_ENCODE_DURATION_CAP_ENABLED=false

PROJ=projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/documentary_v2
SEG=renders/segments_ep002
LOG=.cache/render-ep002
mkdir -p "$SEG" "$LOG"

# Chunk boundaries come from plan_ep002_chunks.py, which refuses to place a seam
# within 3 s of a chapter start, a chapter card's reveal, or its exit.
#
# The previous plan used 300/600/900/1200/1500/1800 — and chapters II, III and IV
# begin at exactly 300, 600 and 900. The join cut through a transition still in
# flight, so the outgoing chunk's last frames were captured half-faded and the
# incoming chunk snapped back. That is the hitch the viewer saw as lag.
#
# Each chunk also carries its own preroll: capture starts PREROLL seconds before
# the first wanted frame so every animation already running has settled, and
# assembly trims exactly that amount rather than assuming 2 s.
#
# name      start    end      preroll
CHUNKS=(
  "ch01:0.0:296.5:0.0"
  "ch02:296.5:596.5:3.0"
  "ch03:596.5:896.5:3.0"
  "ch04:896.5:1200.0:3.0"
  "ch05:1200.0:1500.0:3.0"
  "ch06:1500.0:1800.0:3.0"
  "ch07:1800.0:2100.0:3.0"
)
WORKERS="${WORKERS:-1}"

START_AT="${1:-ch01}"
MIN_FREE_MB=1200    # streaming needs almost nothing; this only guards the output

probe() { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1" 2>/dev/null | head -1; }

sweep() {  # only ever remove render scratch and finished temp output
  # NEVER call this while a chunk is capturing. The renderer writes live frames
  # into /tmp/hf-render-span-*, and deleting that directory mid-chunk leaves the
  # capture loop waiting on frames that no longer exist: heartbeats stop, nothing
  # errors, and the job hangs forever. It happened once, by hand, from outside
  # this script. Only sweep between chunks, or with no render running at all.
  rm -rf /tmp/hf-render-span-* /tmp/.org.chromium.* 2>/dev/null
  rm -rf "$PROJ/.hyperframes/artifacts" 2>/dev/null
}

for spec in "${CHUNKS[@]}"; do
  IFS=: read -r name a b pre <<<"$spec"
  [[ "$name" < "$START_AT" ]] && continue
  out="$SEG/$name.mp4"
  want=$(python3 -c "print(f'{$b-$a:.1f}')")
  cap_start=$(python3 -c "print(f'{max(0.0, $a-$pre):.3f}')")
  lead=$(python3 -c "print(f'{$a-$cap_start:.3f}')")

  if [ -f "$out" ]; then
    got=$(probe "$out")
    if python3 -c "import sys; sys.exit(0 if abs(float('${got:-0}')-$want)<0.6 else 1)"; then
      echo "== $name already done (${got}s)"
      continue
    fi
    echo "== $name short (${got:-0}s of ${want}s) — re-rendering"
    rm -f "$out"
  fi

  avail=$(df -Pm /home/user | awk 'NR==2{print $4}')
  if [ "${avail:-0}" -lt "$MIN_FREE_MB" ]; then
    echo "== low on disk (${avail} MB), sweeping render scratch"
    sweep
    avail=$(df -Pm /home/user | awk 'NR==2{print $4}')
  fi
  echo "== $name  [$a -> $b]  ${want}s  ${avail} MB free  $(date -u +%H:%M:%SZ)"
  echo "== $name  [$a -> $b]  ${want}s  ${avail} MB free" >> "$LOG/job.log"

  node packages/cli/bin/hyperframes.mjs render "$PROJ" -o "$out" \
      --start "$cap_start" --end "$b" -q "${QUALITY:-draft}" --workers "$WORKERS" 2>&1 \
      | tee "$LOG/$name.log" | grep -E "rendered in|Render failed|Disk capture|✗|◇" | tail -4

  got=$(probe "$out")
  want_cap=$(python3 -c "print(f'{$b-$cap_start:.1f}')")
  if [ -n "${got:-}" ] && python3 -c "import sys; sys.exit(0 if abs(float('${got}')-$want_cap)<0.6 else 1)"; then
    echo "== $name captured ${got}s (incl. ${lead}s preroll)"
  fi
  if [ -z "${got:-}" ]; then
    echo "!! $name produced nothing — see $LOG/$name.log"
    echo "!! $name FAILED $(date -u +%H:%M:%SZ)" >> "$LOG/job.log"
    exit 1
  fi
  echo "${lead}" > "$SEG/$name.lead"
  echo "== $name done ${got}s  lead ${lead}s  $(du -h "$out" | cut -f1)  $(date -u +%H:%M:%SZ)"
  echo "${lead}" > "$SEG/$name.lead"
  echo "== $name done ${got}s  lead ${lead}s  $(du -h "$out" | cut -f1)  $(date -u +%H:%M:%SZ)" >> "$LOG/job.log"
  rm -rf /tmp/hf-render-span-* 2>/dev/null
done

echo "== all chunks rendered  $(date -u +%H:%M:%SZ)"
ls -lh "$SEG"
