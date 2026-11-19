"""Pre-mix the Episode 02 audio track outside the renderer.

The renderer builds its own audio mix and, on this box, ran out of disk writing a
2100 s float32 intermediate. Mixing here, once, in mono at 48 kHz, removes that
whole failure mode and makes the level check explicit.

  voice    flat, as delivered (the master is already -16.1 LUFS territory)
  beds     seven chapter beds, each normalised to -30 LUFS, i.e. ~10 dB under voice
  effects  one cue per card / chapter card / place name, at the volume the build used

Writes assets/audio/mix.m4a and production/MIX_REPORT.json.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P = ROOT / "projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/documentary_v2"
FF = str(ROOT / ".cache/bin/ffmpeg")
FP = str(ROOT / ".cache/bin/ffprobe")
FILM = 2100.0
TARGET_BED_LUFS = -30.0


def run(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, check=True, **kw)


def lufs(path):
    out = run([FF, "-hide_banner", "-nostdin", "-i", str(path),
               "-af", "loudnorm=I=-30:TP=-2:print_format=json", "-f", "null", "-"])
    m = re.search(r'"input_i"\s*:\s*"(-?[\d.]+)"', out.stderr)
    return float(m.group(1))


def dur(path):
    return float(run([FP, "-v", "error", "-show_entries", "format=duration",
                      "-of", "csv=p=0", str(path)]).stdout)


def main():
    shot = json.loads((P / "production/SHOT_LIST.json").read_text())
    beds = shot["beds"]
    sfx = shot["sfx"]

    inputs = [str(P / "assets/audio/narration.mp3")]
    for name in sorted(beds):
        inputs.append(str(P / "assets/audio/bed" / name))

    ff_inputs = []
    for i in inputs:
        ff_inputs += ["-i", i]

    chain = []
    # voice: input 0, straight through, trimmed/padded to the film length
    chain.append("[0]aresample=48000,apad,atrim=0:%.3f,"
                 "afade=t=in:st=0:d=0.05[voz]" % FILM)

    mix_labels = ["[voz]"]
    for k, name in enumerate(sorted(beds)):
        gain = 10 ** ((TARGET_BED_LUFS - beds[name]) / 20)
        idx = k + 1
        chapter_start = float(re.search(r"data-start=\"([\d.]+)\"",
                             (P / "index.html").read_text().split(f"bed{name}")[0].split("<audio")[-1]).group(1)) \
            if False else None
        chain.append(f"[{idx}]aresample=48000,volume={gain:.4f},apad,atrim=0:{FILM:.3f}[bed{k}]")
        mix_labels.append(f"[bed{k}]")

    # effects: delayed copies of a few source files
    sfx_files = sorted({s["file"] for s in sfx})
    for f in sfx_files:
        inputs.append(str(P / "assets/audio/sfx" / f))
        ff_inputs += ["-i", str(P / "assets/audio/sfx" / f)]
    base = len(beds) + 1
    for j, s in enumerate(sfx):
        idx = base + sfx_files.index(s["file"])
        ms = int(round(s["start"] * 1000))
        chain.append(f"[{idx}]aresample=48000,adelay={ms}|{ms},volume={s['vol']:.2f}[fx{j}]")
        mix_labels.append(f"[fx{j}]")

    mixed = "".join(mix_labels)
    chain.append(f"{mixed}amix=inputs={len(mix_labels)}:duration=first:normalize=0,"
                 f"alimiter=limit=0.94,atrim=0:{FILM:.3f}[out]")

    out = P / "assets/audio/mix.m4a"
    run([FF, "-hide_banner", "-nostdin", "-y", *ff_inputs,
         "-filter_complex", ";".join(chain), "-map", "[out]",
         "-ar", "48000", "-ac", "1", "-c:a", "aac", "-b:a", "192k", str(out)])

    report = {"film_seconds": round(dur(out), 3),
              "voice_lufs": round(lufs(P / "assets/audio/narration.mp3"), 2),
              "mix_lufs": round(lufs(out), 2),
              "beds": beds, "bed_target_lufs": TARGET_BED_LUFS,
              "sfx_cues": len(sfx), "bed_cues": len(beds),
              "file": str(out.relative_to(ROOT))}
    (P / "production/MIX_REPORT.json").write_text(json.dumps(report, indent=1) + "\n")
    print(json.dumps(report, indent=1))


if __name__ == "__main__":
    sys.exit(main())
