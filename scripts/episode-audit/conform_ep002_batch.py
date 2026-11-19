"""Conform a batch of Episode 02 blocks at one uniform tempo factor.

Decision recorded in 09_PACING_DECISION.md, corrected in 11_FACTOR_CORRECTION.md.

atempo halves and doubles duration inversely: output = input / factor. A factor
below 1 therefore LENGTHENS the audio, which is what these takes need — 23.2 s of
speech has to reach 27.6 s to fill a 30 s slot the way Episode 01 did.

Uniform 0.84 is applied everywhere it is arithmetically possible. A take already
longer than 0.84 x 29.5 s cannot be stretched that far without overrunning, so it
gets the gentlest factor that fits: raw / 29.5. That is not per-block tuning, it
is the one clamp the geometry forces.

Uniform is the point. Every block is treated identically, so no block carries a
different amount of processing from its neighbour. The tool reports the spread
instead of hiding it, and refuses any block that would still overrun.
"""
import json
import sys
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import imageio_ffmpeg
import subprocess

ROOT = Path(__file__).resolve().parents[2]
FILM = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/story_film_35min'
PILOT = FILM / 'audio/pilot'
CONFORMED = FILM / 'audio/conformed'
RATE = 48000
SLOT = 30 * RATE
FACTOR = 0.84          # atempo < 1 LENGTHENS: 23.2s becomes 27.6s
MAX_SPEECH = 29.5      # seconds; a block may not fill more than this


def ffmpeg(args):
    return subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-hide_banner', '-nostdin', *args],
                          capture_output=True, text=True, check=True)


def duration(path):
    return float(subprocess.run(['.cache/bin/ffprobe', '-v', 'error', '-show_entries',
                                 'format=duration', '-of', 'csv=p=0', str(path)],
                                capture_output=True, text=True, check=True).stdout)


def take_for(n):
    """Plain take. The ellipsis passes were longer by design and do not belong
    in a batch that applies one uniform factor to every block."""
    return PILOT / f'B{n:03d}.mp3'


def main(numbers):
    CONFORMED.mkdir(parents=True, exist_ok=True)
    blocks = {b['n']: b for b in json.loads(
        (FILM / 'narration_blocks_v02.json').read_text())['blocks']}
    rows = []
    for n in numbers:
        source = take_for(n)
        if not source.exists():
            print(f'B{n:03d}: no take'); continue
        raw = duration(source)
        factor = max(FACTOR, raw / MAX_SPEECH) if raw / FACTOR > MAX_SPEECH else FACTOR
        tempo = CONFORMED / f'B{n:03d}_tempo.wav'
        master = CONFORMED / f'B{n:03d}_30s.wav'
        ffmpeg(['-y', '-v', 'error', '-i', str(source), '-af', f'atempo={factor:.6f}',
                '-ar', str(RATE), '-ac', '1', '-c:a', 'pcm_s16le', str(tempo)])
        with wave.open(str(tempo), 'rb') as reader:
            frames = reader.getnframes()
            data = reader.readframes(frames)
        if frames > SLOT:
            raise SystemExit(f'B{n:03d}: {frames / RATE:.3f}s still overruns after tempo')

        with wave.open(str(master), 'wb') as writer:
            writer.setnchannels(1)
            writer.setsampwidth(2)
            writer.setframerate(RATE)
            writer.writeframes(data + b'\x00\x00' * (SLOT - frames))
        ffmpeg(['-y', '-v', 'error', '-i', str(master), '-c:a', 'libmp3lame',
                '-b:a', '192k', str(master.with_suffix('.mp3'))])
        tempo.unlink()
        rows.append({'block': n, 'words': blocks[n]['words'], 'raw_seconds': round(raw, 2),
                     'speech_seconds': round(frames / RATE, 2),
                     'gap_seconds': round((SLOT - frames) / RATE, 2),
                     'samples': SLOT, 'tempo': round(factor, 4)})
        print(f'B{n:03d} {blocks[n]["words"]:3d}w  speech {frames / RATE:5.2f}s  '
              f'gap { (SLOT - frames) / RATE:4.2f}s  -> {master.name}')
    if rows:
        mean_speech = sum(r['speech_seconds'] for r in rows) / len(rows)
        mean_gap = sum(r['gap_seconds'] for r in rows) / len(rows)
        print(f'\n{len(rows)} blocks, target tempo {FACTOR}')
        print(f'mean speech {mean_speech:.2f}s of 30 (Ep01 delivered 28.72s)')
        print(f'mean gap {mean_gap:.2f}s (Ep01 delivered 1.28s)')
        print(f'gap spread {min(r["gap_seconds"] for r in rows):.2f}-'
              f'{max(r["gap_seconds"] for r in rows):.2f}s')
        report = FILM / '10_CONFORM_REPORT.json'
        existing = {}
        if report.exists():
            for row in json.loads(report.read_text())['blocks']:
                existing[row['block']] = row
        for row in rows:
            existing[row['block']] = row
        merged = [existing[k] for k in sorted(existing)]
        report.write_text(json.dumps({
            'tempo_target': FACTOR, 'blocks': merged,
            'conformed_blocks': len(merged),
            'mean_speech_seconds': round(sum(r['speech_seconds'] for r in merged) / len(merged), 2),
            'mean_gap_seconds': round(sum(r['gap_seconds'] for r in merged) / len(merged), 2),
            'max_gap_seconds': max(r['gap_seconds'] for r in merged),
        }, indent=1) + '\n')
        print(f'report: {report.relative_to(ROOT)}')


if __name__ == '__main__':
    nums = [int(x) for x in sys.argv[1:]] or list(range(1, 12))
    main(nums)
