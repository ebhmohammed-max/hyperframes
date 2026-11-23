#!/usr/bin/env python3
"""Loudness pass for a rendered style: copies the picture untouched and re-levels the mix to
-14 LUFS integrated / -2 dBTP (two-pass loudnorm), writing deliver/<name>.mp4.
usage: finish.py <ffmpeg> <in.mp4> <out.mp4> [target_lufs]"""
import json, re, subprocess, sys
ff, src, dst = sys.argv[1:4]
I = float(sys.argv[4]) if len(sys.argv) > 4 else -14.0
base = f"loudnorm=I={I}:TP=-2.0:LRA=11"
p = subprocess.run([ff, "-hide_banner", "-nostats", "-i", src, "-af", base + ":print_format=json", "-f", "null", "-"], capture_output=True, text=True)
m = json.loads(re.findall(r"\{[^{}]*\"input_i\"[^{}]*\}", p.stderr)[-1])
af = (f"{base}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
      f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true,aresample=48000")
subprocess.run([ff, "-v", "error", "-y", "-i", src, "-c:v", "copy", "-af", af, "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", dst], check=True)
print(f"{dst}: in {m['input_i']} LUFS / {m['input_tp']} dBTP -> target {I}")
