"""Place the opening eleven Episode 02 blocks on the film clock for listening.

Each block is decoded, padded with digital silence to exactly 30.000 s at 48 kHz,
and laid end to end. Nothing is time-stretched: the point is to hear how much of
each slot the voice actually fills, so the gap is audible rather than inferred.

Run after the takes for blocks 1-11 exist in audio/pilot/.
"""
import sys
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import imageio_ffmpeg
import ep002_blocks as E
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
FILM = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/story_film_35min'
PILOT = FILM / 'audio/pilot'
RATE = 48000
SLOT = 30 * RATE
BLOCKS = list(range(1, 12))


def run(args):
    return subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-hide_banner', '-nostdin', *args],
                          capture_output=True, text=True, check=True)


def frames(path):
    with wave.open(str(path), 'rb') as reader:
        return reader.getnframes(), reader.readframes(reader.getnframes())


def take_for(n):
    """Prefer the delivered ellipsis pass where one was rendered."""
    paced = PILOT / f'B{n:03d}_e.mp3'
    return paced if paced.exists() else PILOT / f'B{n:03d}.mp3'


def main():
    blocks = {b['n']: b for b in E.parse(FILM / '01_COMPLETE_NARRATION_35MIN_v02.md')}
    out = PILOT / 'EP002_OPENING_11_BLOCKS_ON_CLOCK.wav'
    report = []
    with tempfile.TemporaryDirectory() as folder:
        tmp = Path(folder)
        with wave.open(str(out), 'wb') as writer:
            writer.setnchannels(1)
            writer.setsampwidth(2)
            writer.setframerate(RATE)
            for n in BLOCKS:
                take = take_for(n)
                decoded = tmp / f'B{n:03d}.wav'
                run(['-y', '-v', 'error', '-xerror', '-i', str(take), '-ar', str(RATE),
                     '-ac', '1', '-c:a', 'pcm_s16le', str(decoded)])
                count, data = frames(decoded)
                assert count <= SLOT, f'block {n} overruns its slot at {count / RATE:.2f}s'
                writer.writeframes(data + b'\x00\x00' * (SLOT - count))
                report.append((n, blocks[n]['words'], count / RATE, (SLOT - count) / RATE,
                               take.name))
    mp3 = out.with_suffix('.mp3')
    run(['-y', '-v', 'error', '-i', str(out), '-c:a', 'libmp3lame', '-b:a', '160k', str(mp3)])
    total_w = sum(r[1] for r in report)
    total_s = sum(r[2] for r in report)
    print(f"{'blk':>3} {'words':>5} {'speech':>7} {'dead air':>9}  take")
    for n, w, s, gap, name in report:
        print(f'{n:3d} {w:5d} {s:7.2f} {gap:9.2f}  {name}')
    print(f'\n{total_w} words in {total_s:.1f}s of speech across {len(report) * 30}s of film')
    print(f'speech fills {total_s / (len(report) * 30) * 100:.1f}% of the clock')
    print(f'mean dead air per block: {(len(report) * 30 - total_s) / len(report):.2f}s')
    print(f'preview: {out.relative_to(ROOT)}  ({len(report) * 30}s)')


if __name__ == '__main__':
    main()
