"""Conform opening narration pilot; exact 30s PCM, no truncation of spoken content.

Requires imageio-ffmpeg. This is a technical check, not listening approval.
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
EP = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria'
FILM = EP / 'story_film_35min'
AUDIO = FILM / 'audio'
RATE = 48000

TEXTS = {
    'B001_take01': "Long before the Iron Throne was forged from surrendered blades, before Aegon Targaryen turned his gaze toward Westeros, another people learned to command the sky.\n\nTheir home was a smoking peninsula in southern Essos.\n\nTheir descendants would break empires and raise wonders from black stone.\n\nYet the first Valyrians were shepherds.\n\nHow did they become dragonlords?\n\nAnd who paid for the world they built?",
    'B001_take02': "Long before the Iron Throne was forged from surrendered blades... before Aegon Targaryen turned his gaze toward Westeros... another people learned to command the sky.\n\nTheir home... was a smoking peninsula in southern Essos.\n\nTheir descendants would break empires... and raise wonders from black stone.\n\nYet the first Valyrians... were shepherds.\n\nHow did they become dragonlords?\n\nAnd who paid... for the world they built?",
}


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


def main():
    source = json.loads((FILM / 'narration_blocks_v02.json').read_text())[0]
    records = []
    output = AUDIO / 'review/B001_00m00s-00m30s_v01.wav'
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as folder:
        tmp = Path(folder)
        for name, text in TEXTS.items():
            assert tokens(text) == tokens(source), 'Synthesis text word sequence changed'
            raw = AUDIO / f'raw/{name}.mp3'
            decoded = tmp / f'{name}.wav'
            run(['-y', '-v', 'error', '-xerror', '-i', str(raw), '-ar', str(RATE),
                 '-ac', '1', '-c:a', 'pcm_s16le', str(decoded)])
            frames, _ = wav_data(decoded)
            records.append({'take': name, 'voice_id': 'voice-01', 'text': text,
                            'file': str(raw.relative_to(ROOT)), 'sha256': sha(raw),
                            'decoded_samples': frames, 'decoded_seconds': frames / RATE,
                            'decode_check': 'passed',
                            'word_sequence_matches_authored_block': True})
        selected = records[1]
        target_speech_seconds = 29.9
        factor = selected['decoded_seconds'] / target_speech_seconds
        assert 0.92 <= factor <= 1.08, 'Over permitted pilot tempo adjustment; regenerate instead'
        processed = tmp / 'processed.wav'
        run(['-y', '-v', 'error', '-i', str(tmp / 'B001_take02.wav'),
             '-af', f'atempo={factor:.12f}', '-c:a', 'pcm_s16le', str(processed)])
        frames, data = wav_data(processed)
        missing = 30 * RATE - frames
        assert 0 <= missing <= int(0.2 * RATE), 'Unexpected processing length; do not trim words'
        with wave.open(str(output), 'wb') as writer:
            writer.setnchannels(1)
            writer.setsampwidth(2)
            writer.setframerate(RATE)
            writer.writeframes(data + b'\x00\x00' * missing)
        final_frames, _ = wav_data(output)
        assert final_frames == 30 * RATE
        mp3 = output.with_suffix('.mp3')
        run(['-y', '-v', 'error', '-i', str(output), '-c:a', 'libmp3lame', '-b:a', '192k', str(mp3)])
        run(['-v', 'error', '-xerror', '-i', str(mp3), '-f', 'null', '-'])
        stats = run(['-i', str(output), '-af', 'volumedetect', '-f', 'null', '-']).stderr
        peak = re.search(r'max_volume: ([\-\d.]+) dB', stats)
        manifest = {'status': 'B001_TECHNICALLY_CONFORMED_LISTENING_PENDING',
                    'scope': 'Opening pilot only; remaining69blocks not recorded',
                    'block': 'B001', 'image_range': [1, 15], 'placed_interval_seconds': [0, 30],
                    'takes': records, 'selected_take': selected['take'],
                    'atempo_factor': factor, 'speed_increase_percent': (factor - 1) * 100,
                    'processed_samples_before_boundary_pad': frames,
                    'boundary_pad_samples': missing, 'boundary_pad_seconds': missing / RATE,
                    'master': {'file': str(output.relative_to(ROOT)), 'sample_rate': RATE,
                               'channels': 1, 'pcm_bits': 16, 'samples': final_frames,
                               'duration_seconds': 30, 'sha256': sha(output),
                               'max_sample_volume_dbfs': float(peak[1]) if peak else None},
                    'review_mp3': {'file': str(mp3.relative_to(ROOT)), 'sha256': sha(mp3),
                                   'note': 'Lossy preview; exact timing authority is PCM master, not MP3 container duration'},
                    'not_performed': ['listening QC', 'speech recognition/word-level forced alignment',
                                      'image synchronization/QC', 'music or sound mix'],
                    'final_approved': False}
        (FILM / '08_RECORDING_PILOT_MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n')
        print(json.dumps({k: v for k, v in manifest.items() if k != 'takes'}, indent=2))


if __name__ == '__main__':
    main()
