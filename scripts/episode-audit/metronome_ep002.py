"""Fit each Episode 02 voice take into its 30-second slot, or refuse it.

Why this exists: the speech engine is non-deterministic — the same text rendered
three times gave 21.79 s, 22.94 s and 22.73 s. "Render until it fits" is therefore a
lottery, not a method. What is reproducible is measurement and a bounded correction.

Measured reference (Episode 01, the film the user approved):
    articulation 161.5 wpm, pause share 16.8 %, 11-15 pauses per block,
    speech filling 26.9-29.4 s of each 30 s slot.

For each block this tool:
  1. decodes the take and measures speech vs pause using silencedetect;
  2. reports the articulation rate and how far it is from the Ep01 reference;
  3. if the take is short, fits a tempo factor to land speech at 28.8 s;
  4. rejects the take if the factor leaves the acceptable band, because a voice
     pulled 30 percent slow stops sounding like a documentary narrator;
  5. refuses any take whose articulation rate is more than 15 percent above the
     Ep01 reference, regardless of whether the arithmetic works, because that
     take is a *different performance*, not a slow one.
"""
import json
import re
import subprocess
import sys
import wave
from pathlib import Path

import imageio_ffmpeg

ROOT = Path(__file__).resolve().parents[2]
FILM = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/story_film_35min'
PILOT = FILM / 'audio/pilot'
RATE = 48000
SLOT_SAMPLES = 30 * RATE

# Episode 01 delivered reference
EP01_ARTICULATION = 165.3   # raw Ep01 takes, same silencedetect method as here
EP01_PAUSE_SHARE = 0.156
TARGET_SPEECH = 28.8
FACTOR_MIN, FACTOR_MAX = 0.82, 1.00     # never stretch faster than natural, never slower than 18 %
ARTICULATION_TOLERANCE = 0.15


def ffmpeg(args):
    return subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-hide_banner', '-nostdin', *args],
                          capture_output=True, text=True, check=True)


def duration(path):
    return float(subprocess.run(['.cache/bin/ffprobe', '-v', 'error', '-show_entries',
                                 'format=duration', '-of', 'csv=p=0', str(path)],
                                capture_output=True, text=True, check=True).stdout)


def pause_stats(path, floor=-40, minimum=0.25):
    """Pause total and count, using a threshold near the Ep01 measurement floor."""
    stderr = ffmpeg(['-i', str(path), '-af', f'silencedetect=noise={floor}dB:d={minimum}',
                     '-f', 'null', '-']).stderr
    return [float(x) for x in re.findall(r'silence_duration: ([\d.]+)', stderr)]


def measure(path, words):
    total = duration(path)
    pauses = pause_stats(path)
    pause_total = sum(pauses)
    speech = total - pause_total
    return {
        'file': path.name, 'total_seconds': round(total, 2), 'words': words,
        'pauses': len(pauses), 'pause_total_seconds': round(pause_total, 2),
        'pause_share_percent': round(pause_total / total * 100, 1),
        'speech_seconds': round(speech, 2),
        'articulation_wpm': round(words / speech * 60, 1),
    }


def judge(measurement):
    art = measurement['articulation_wpm']
    ceiling = EP01_ARTICULATION * (1 + ARTICULATION_TOLERANCE)
    speech = measurement['speech_seconds']
    factor = TARGET_SPEECH / speech if speech < TARGET_SPEECH else 1.0
    verdict, reason = 'usable', ''
    if art > ceiling:
        verdict = 'reject'
        reason = (f'articulation {art:.0f} wpm is more than 15 % above the Episode 01 '
                  f'reference {EP01_ARTICULATION:.0f}; slowing this would not make it the '
                  f'same performance')
    elif factor < FACTOR_MIN:
        verdict = 'reject'
        reason = (f'would need tempo {factor:.3f} ({speech:.1f}s -> {TARGET_SPEECH}s), '
                  f'slower than the {FACTOR_MIN:.2f} limit')
    return {'verdict': verdict, 'reason': reason, 'tempo_factor': round(factor, 4),
            'projected_speech_seconds': round(speech * factor, 2)}


def conform(source, factor, destination):
    """Apply tempo, then pad to exactly 30.000 s mono 48 kHz 16-bit."""
    worked = destination.with_name(destination.stem + '_tempo.wav')
    if abs(factor - 1.0) > 1e-6:
        ffmpeg(['-y', '-v', 'error', '-i', str(source), '-af', f'atempo={factor:.10f}',
                '-ar', str(RATE), '-ac', '1', '-c:a', 'pcm_s16le', str(worked)])
    else:
        ffmpeg(['-y', '-v', 'error', '-i', str(source), '-ar', str(RATE), '-ac', '1',
                '-c:a', 'pcm_s16le', str(worked)])
    with wave.open(str(worked), 'rb') as reader:
        frames = reader.getnframes()
        data = reader.readframes(frames)
    pad = SLOT_SAMPLES - frames
    if pad < 0:
        raise ValueError(f'{destination.name}: {frames / RATE:.3f}s will not fit the slot')
    with wave.open(str(destination), 'wb') as writer:
        writer.setnchannels(1)
        writer.setsampwidth(2)
        writer.setframerate(RATE)
        writer.writeframes(data + b'\x00\x00' * pad)
    ffmpeg(['-y', '-v', 'error', '-i', str(destination), '-c:a', 'libmp3lame',
            '-b:a', '192k', str(destination.with_suffix('.mp3'))])
    worked.unlink(missing_ok=True)
    return {'samples': frames + pad, 'seconds': (frames + pad) / RATE,
            'boundary_pad_seconds': round(pad / RATE, 3)}


def main(argv):
    blocks = json.loads((FILM / 'narration_blocks_v02.json').read_text())['blocks']
    words = {b['n']: b['words'] for b in blocks}
    numbers = [int(x) for x in argv] if argv else list(range(2, 12))
    results = []
    for n in numbers:
        candidates = sorted(PILOT.glob(f'B{n:03d}[_a-z0-9]*.mp3')) + sorted(PILOT.glob(f'B{n:03d}.mp3'))
        candidates = [c for c in candidates if not c.stem.endswith(('_30s', '_tempo'))]
        if not candidates:
            print(f'B{n:03d}: no take on disk'); continue
        print(f'\n=== block {n} ({words[n]} words) ===')
        for take in dict.fromkeys(candidates):
            m = measure(take, words[n])
            j = judge(m)
            print(f"  {m['file']:14s} {m['total_seconds']:6.2f}s  speech {m['speech_seconds']:6.2f}s  "
                  f"pauses {m['pauses']:2d} ({m['pause_share_percent']:4.1f}%)  "
                  f"artic {m['articulation_wpm']:5.1f}  ->  {j['verdict']}"
                  + (f'  [{j["reason"]}]' if j['reason'] else ''))
            results.append({'block': n, **m, **j})
    out = FILM / '06_METRONOME_REPORT.json'
    out.write_text(json.dumps(results, indent=1) + '\n', encoding='utf-8')
    usable = [r for r in results if r['verdict'] == 'usable']
    print(f'\n{len(usable)} of {len(results)} takes usable; report written to {out.relative_to(ROOT)}')


if __name__ == '__main__':
    main(sys.argv[1:])
