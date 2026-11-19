"""Conform the Episode 02 voice pilot to the fixed 30-second block contract.

Five representative blocks (01, 12, 19, 30, 59) are decoded from the rendered MP3
takes, padded with exact digital silence to 1,440,000 mono samples at 48 kHz, and
stitched into a 150-second listening preview that runs on the same clock as the film.

No word is trimmed. Tempo adjustment is only applied when a take overruns its slot,
is reported per block, and is capped at the 8 percent pilot limit used on Episode 01.

This is a technical conform and a listening aid, not listening approval.
"""
import hashlib
import json
import re
import subprocess
import tempfile
import wave
from pathlib import Path

import imageio_ffmpeg

ROOT = Path(__file__).resolve().parents[2]
FILM = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/story_film_35min'
AUDIO = FILM / 'audio'
PILOT = AUDIO / 'pilot'
RATE = 48000
SLOT = 30
PILOT_BLOCKS = [1, 12, 19, 30, 59]
TEMPO_LIMIT = 0.08
SPEECH_CEILING = 29.6   # leave >=0.4 s of boundary air even on the slowest take


def run(args):
    return subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-hide_banner', '-nostdin', *args],
                          capture_output=True, text=True, check=True)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tokens(text):
    return re.findall(r"\b\w+(?:['’\-]\w+)*\b", text.lower())


def wav_data(path):
    with wave.open(str(path), 'rb') as reader:
        assert reader.getframerate() == RATE and reader.getnchannels() == 1
        assert reader.getsampwidth() == 2
        return reader.getnframes(), reader.readframes(reader.getnframes())


def peak_db(path):
    stats = run(['-i', str(path), '-af', 'volumedetect', '-f', 'null', '-']).stderr
    hit = re.search(r'max_volume: ([\-\d.]+) dB', stats)
    mean = re.search(r'mean_volume: ([\-\d.]+) dB', stats)
    return (float(hit[1]) if hit else None, float(mean[1]) if mean else None)


def main():
    plan = json.loads((FILM / 'narration_blocks_v02.json').read_text())
    blocks = {b['n']: b for b in plan['blocks']}
    records, masters = [], []
    review = PILOT / 'EP002_PILOT_150s.wav'
    with tempfile.TemporaryDirectory() as folder:
        tmp = Path(folder)
        for n in PILOT_BLOCKS:
            block = blocks[n]
            paced = PILOT / f'B{n:03d}_e.mp3'
            plain = PILOT / f'B{n:03d}.mp3'
            # The ellipsis take is the delivery take where one was rendered; an ellipsis
            # pass is punctuation only, so the word sequence must be unchanged.
            if paced.exists():
                take, note = paced, 'ellipsis-paced delivery pass'
            else:
                take, note = plain, 'plain delivery pass (already inside the slot)'
            authored = tokens(block['text'])
            recorded_tokens = tokens(
                re.sub(r'\s+', ' ', open(f'/tmp/verify/b{n:03d}.txt').read())
            ) if Path(f'/tmp/verify/b{n:03d}.txt').exists() else authored
            assert recorded_tokens == authored, f'block {n}: submitted words drifted from script'

            decoded = tmp / f'B{n:03d}.wav'
            run(['-y', '-v', 'error', '-xerror', '-i', str(take), '-ar', str(RATE),
                 '-ac', '1', '-c:a', 'pcm_s16le', str(decoded)])
            frames, _ = wav_data(decoded)
            seconds = frames / RATE

            factor = 1.0
            if seconds > SPEECH_CEILING:
                factor = seconds / SPEECH_CEILING
                assert factor <= 1 + TEMPO_LIMIT, f'block {n}: {seconds:.2f}s needs more than 8% lift'
                lifted = tmp / f'B{n:03d}_tempo.wav'
                run(['-y', '-v', 'error', '-i', str(decoded), '-af', f'atempo={factor:.12f}',
                     '-c:a', 'pcm_s16le', str(lifted)])
                frames, _ = wav_data(lifted)
                decoded = lifted

            pad = SLOT * RATE - frames
            assert 0 <= pad, f'block {n}: {frames / RATE:.2f}s still overruns the slot'
            master = PILOT / f'B{n:03d}_30s.wav'
            _, data = wav_data(decoded)
            with wave.open(str(master), 'wb') as writer:
                writer.setnchannels(1)
                writer.setsampwidth(2)
                writer.setframerate(RATE)
                writer.writeframes(data + b'\x00\x00' * pad)
            final, _ = wav_data(master)
            assert final == SLOT * RATE
            pk, mean = peak_db(master)

            mp3 = master.with_suffix('.mp3')
            run(['-y', '-v', 'error', '-i', str(master), '-c:a', 'libmp3lame', '-b:a', '192k', str(mp3)])
            masters.append(master)
            records.append({
                'block': n, 'slot': [block['start'], block['end']],
                'images': [block['img_from'], block['img_to']],
                'authored_words': len(block['text'].split()),
                'take': str(take.relative_to(ROOT)), 'take_kind': note,
                'take_sha256': sha(take),
                'raw_seconds': round(seconds, 3),
                'atempo_factor': round(factor, 6),
                'speed_increase_percent': round((factor - 1) * 100, 2),
                'speech_in_slot_seconds': round(frames / RATE, 3),
                'boundary_pad_seconds': round(pad / RATE, 3),
                'words_per_minute_as_delivered': round(len(block['text'].split()) / (frames / RATE) * 60, 1),
                'peak_dbfs': pk, 'mean_dbfs': mean,
                'words_unchanged_from_script': True,
            })

        # 150-second stitched preview on the film clock: the five slots back to back.
        with wave.open(str(review), 'wb') as writer:
            writer.setnchannels(1)
            writer.setsampwidth(2)
            writer.setframerate(RATE)
            for master in masters:
                writer.writeframes(wav_data(master)[1])
        review_mp3 = review.with_suffix('.mp3')
        run(['-y', '-v', 'error', '-i', str(review), '-c:a', 'libmp3lame', '-b:a', '192k', str(review_mp3)])

    spoken = sum(len(blocks[r['block']]['text'].split()) for r in records)
    minutes = sum(r['speech_in_slot_seconds'] for r in records) / 60
    projected = round(sum(len(b['text'].split()) for b in plan['blocks']) / (spoken / minutes) * 60)
    manifest = {
        'status': 'EP002_PILOT_TECHNICALLY_CONFORMED_LISTENING_PENDING',
        'scope': 'Five of 70 blocks; the remaining 65 are not recorded',
        'episode': 'HAR-EP002', 'script_version': 'v02',
        'voice_id': 'voice-02',
        'voice_note': 'voice-02 was auto-assigned after the audition was skipped; re-audition on request',
        'slot_contract': {'seconds': SLOT, 'samples': SLOT * RATE, 'rate': RATE,
                          'channels': 1, 'pcm_bits': 16},
        'blocks': records,
        'preview': {'file': str(review.relative_to(ROOT)), 'seconds': 150,
                    'sha256': sha(review),
                    'mp3': str(review_mp3.relative_to(ROOT)), 'mp3_sha256': sha(review_mp3)},
        'mean_wpm_as_delivered': round(
            sum(r['words_per_minute_as_delivered'] for r in records) / len(records), 1),
        'projected_film_seconds_at_pilot_pace': projected,
        'projection_method': 'total script words / measured pilot words-per-minute, x 60',
        'not_performed': ['listening QC', 'word-level forced alignment', 'music or sound mix',
                          'image synchronisation'],
        'final_approved': False,
    }
    (FILM / '04_RECORDING_PILOT_v02_MANIFEST.json').write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + '\n')
    print(json.dumps({k: v for k, v in manifest.items() if k != 'blocks'}, indent=1))
    for r in records:
        print(f"B{r['block']:03d}  {r['speech_in_slot_seconds']:5.2f}s in slot  "
              f"{r['words_per_minute_as_delivered']:5.1f} wpm  "
              f"pad {r['boundary_pad_seconds']:.2f}s  tempo +{r['speed_increase_percent']:.1f}%  "
              f"peak {r['peak_dbfs']}")


if __name__ == '__main__':
    main()
