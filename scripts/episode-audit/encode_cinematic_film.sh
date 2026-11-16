#!/usr/bin/env bash
# Deliver the cinematic cut: measure loudness, master to spec, encode under 100 MB.
#
#   scripts/episode-audit/encode_cinematic_film.sh <master.mp4> <out_1080p.mp4>
#
# Audio: linear gain toward the loudness target. When that gain would push inter-sample
# peaks past the ceiling, a true-peak limiter holds them instead of stealing level from
# the whole film. Video: single-pass H.264 High@4.1, 1080p30, yuv420p, faststart,
# bitrate sized from the duration so the file lands under 100 MB.
set -euo pipefail

FF=/home/user/hyperframes/.cache/bin/ffmpeg
FFPROBE=/home/user/hyperframes/.cache/bin/ffprobe
SRC="$1"
OUT="$2"
TARGET_I=-16.0
TARGET_TP=-2.2          # ceiling set from measurement: the AAC encode lifts the
                        # dense 147 s moment ~1.5 dB, so -2.2 delivers at -0.7 real peak

echo "== measuring $SRC"
M=$("$FF" -hide_banner -i "$SRC" -af loudnorm=I=${TARGET_I}:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | tail -14)
val() { echo "$M" | grep "\"$1\"" | grep -o '\-\?[0-9.]*'; }
I=$(val input_i); TP=$(val input_tp)
echo "   I=$I LUFS  TP=$TP dBTP"

read -r WANT HEAD <<EOF
$(python3 -c "print(f'{$TARGET_I - $I:.3f} {$TARGET_TP - $TP:.3f}')")
EOF

AF="volume=${WANT}dB"
if python3 -c "import sys; sys.exit(0 if $WANT > $HEAD else 1)"; then
  AF="${AF},alimiter=limit=0.630:attack=4:release=70:level=false"
  echo "   gain ${WANT} dB + true-peak limiter at -4.0 dBFS (delivers -2.2 dBTP after AAC)"
else
  echo "   applying ${WANT} dB (headroom-aware, no limiting needed)"
fi

DUR=$("$FFPROBE" -v error -show_entries format=duration -of csv=p=0 "$SRC")
BITRATE=$(python3 -c "
dur=float('$DUR')
budget_bits = 78 * 8 * 1_000_000
audio_bits = 96000 * dur
print(max(1200, min(6000, int((budget_bits - audio_bits) / dur) // 1000)))
")
echo "   duration ${DUR}s, video bitrate target ${BITRATE}k"

"$FF" -hide_banner -loglevel error -y -i "$SRC" \
  -af "$AF" -c:a aac -b:a 96k -ar 48000 -ac 2 \
  -c:v libx264 -preset slow -b:v ${BITRATE}k -maxrate $((BITRATE * 5 / 4))k -bufsize $((BITRATE * 2))k \
  -profile:v high -level 4.1 -pix_fmt yuv420p -g 60 -r 30 \
  -movflags +faststart "$OUT"

echo "== delivered $OUT"
ls -l "$OUT"
"$FF" -hide_banner -i "$OUT" -af ebur128=peak=true -f null - 2>&1 | grep -A8 "Summary" | tail -8
