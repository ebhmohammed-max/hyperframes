#!/bin/bash
# Rebuilds the render toolchain in /tmp (it is not saved between sessions). ~2 min.
#   bash tools/setup.sh      then      . /tmp/hfenv.sh
# Needs only registry.npmjs.org and pypi.org.
set -e
mkdir -p /tmp/hf && cd /tmp/hf
[ -f package.json ] || npm init -y >/dev/null
[ -x node_modules/.bin/hyperframes ] || npm i hyperframes@0.8.223 @sparticuz/chromium @ffprobe-installer/ffprobe >/tmp/hf/npm.log 2>&1
[ -x /tmp/nkvenv/bin/python ] || { python3 -m venv /tmp/nkvenv && /tmp/nkvenv/bin/pip -q install imageio-ffmpeg pillow numpy; }
# Chromium (headless shell) + the NSS libraries it needs
cat > chrome.mjs <<'JS'
import chromium from "@sparticuz/chromium";
console.log(await chromium.executablePath());
JS
[ -x /tmp/chromium ] || node chrome.mjs >/dev/null
if [ ! -f /tmp/al2023/lib/libnss3.so ]; then
  node -e 'const z=require("zlib"),fs=require("fs");fs.writeFileSync("/tmp/hf/al2023.tar",z.brotliDecompressSync(fs.readFileSync("node_modules/@sparticuz/chromium/bin/al2023.tar.br")))'
  mkdir -p /tmp/al2023 && tar -xf al2023.tar -C /tmp/al2023
fi
mkdir -p /tmp/hfbin
ln -sf "$(/tmp/nkvenv/bin/python -c 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())')" /tmp/hfbin/ffmpeg
FP=$(ls /tmp/hf/node_modules/@ffprobe-installer/linux-x64/ffprobe); chmod +x "$FP"; ln -sf "$FP" /tmp/hfbin/ffprobe
cat > /tmp/hfenv.sh <<'ENV'
export PATH=/tmp/hfbin:/tmp/hf/node_modules/.bin:$PATH
export LD_LIBRARY_PATH=/tmp/al2023/lib:/tmp:$LD_LIBRARY_PATH
export PRODUCER_HEADLESS_SHELL_PATH=/tmp/chromium
export HYPERFRAMES_FFMPEG_PATH=/tmp/hfbin/ffmpeg
export HYPERFRAMES_FFPROBE_PATH=/tmp/hfbin/ffprobe
export HYPERFRAMES_SKIP_SKILLS=1 DO_NOT_TRACK=1 HYPERFRAMES_NO_UPDATE_CHECK=1
hf() { hyperframes "$@"; }
PY=/tmp/nkvenv/bin/python
ENV
echo "toolchain ready: . /tmp/hfenv.sh"
