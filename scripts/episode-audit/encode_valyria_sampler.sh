#!/usr/bin/env bash
# Build delivery encodes of the Old Valyria style sampler from the rendered master.
#
#   scripts/episode-audit/encode_valyria_sampler.sh <master.mp4> [work-dir]
#
# Produces, beside the master:
#   OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_1080p.mp4  2-pass ~760k video + 96k AAC (<100 MB)
#   OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_720p.mp4   720p fallback, same audio
#
# Rationale: the Drive connector caps uploads near 100 MB, so the delivered comparison
# copy is an efficient full-length H.264 encode of the master, never a truncated clip.
set -euo pipefail
MASTER="${1:?master mp4 required}"
SCRIM="${SCRIM:-}"
WORK="${2:-.cache/sampler-encode}"
OUT_DIR="$(dirname "$MASTER")"
FFMPEG="${FFMPEG:-/home/user/hyperframes/.cache/bin/ffmpeg}"
mkdir -p "$WORK"

audio=(-c:a aac -b:a 96k -ar 48000 -ac 2 -movflags +faststart)
video=(-c:v libx264 -preset medium -profile:v high -level 4.1 -pix_fmt yuv420p
       -b:v 760k -maxrate 1100k -bufsize 2200k -g 60)

if [ -n "$SCRIM" ]; then
  FILTER_IN=(-i "$SCRIM")
  FILTER_V=(-filter_complex "[0:v][1:v]overlay=0:0:format=auto")
  FILTER_VM=(-filter_complex "[0:v][1:v]overlay=0:0:format=auto[v]" -map "[v]")
  FILTER_VM720=(-filter_complex "[0:v][1:v]overlay=0:0:format=auto,scale=1280:720:flags=lanczos[v]" -map "[v]")
else
  FILTER_IN=()
  FILTER_V=()
  FILTER_VM=(-map 0:v:0)
  FILTER_VM720=(-map 0:v:0 -vf scale=1280:720:flags=lanczos)
fi

# Pass 1: analysis only (no audio, null output).
"$FFMPEG" -hide_banner -nostdin -y -v warning -stats -i "$MASTER" "${FILTER_IN[@]}" \
  "${FILTER_V[@]}" "${video[@]}" -pass 1 -passlogfile "$WORK/pass1080" -an -f null /dev/null

# Pass 2: final 1080p file with the sampler soundtrack.
"$FFMPEG" -hide_banner -nostdin -y -v warning -stats -i "$MASTER" "${FILTER_IN[@]}" \
  "${FILTER_VM[@]}" -map 0:a:0 "${video[@]}" -pass 2 -passlogfile "$WORK/pass1080" \
  "${audio[@]}" "$OUT_DIR/OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_1080p.mp4"

# 720p fallback for slow connections.
"$FFMPEG" -hide_banner -nostdin -y -v warning -stats -i "$MASTER" "${FILTER_IN[@]}" \
  "${FILTER_VM720[@]}" -map 0:a:0 \
  -c:v libx264 -preset medium -profile:v high -crf 24 -pix_fmt yuv420p -g 60 \
  "${audio[@]}" "$OUT_DIR/OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_720p.mp4"

ls -l "$OUT_DIR"/OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_*.mp4
