"""Validate and assemble the eleven generated story-film narration clips.

Does not synthesize speech, change the historical shot ledger, or claim listening QC.
Run with the project .venv (mutagen and imageio-ffmpeg required).
"""
import csv
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

import imageio_ffmpeg
from mutagen.mp3 import MP3

ROOT = Path(__file__).resolve().parents[2]
FILM = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/story_film'
AUDIO = FILM / 'audio'
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args):
    return subprocess.run([FFMPEG, '-hide_banner', '-nostdin', *args], check=True,
                          capture_output=True, text=True)


def normalized(text):
    return re.sub(r'\s+', ' ', text).strip()


def main():
    manifest_path = FILM / '05_AUDIO_MANIFEST.json'
    manifest = json.loads(manifest_path.read_text())
    clips = manifest['clips']
    assert [row['clip'] for row in clips] == list(range(1, 12))
    recording = (FILM / '02_RECORDING_SCRIPT_v01.txt').read_text()
    assert normalized(' '.join(row['text'] for row in clips)) == normalized(recording)
    offset = 0.0
    for row in clips:
        path = AUDIO / f"{row['clip']:02d}.mp3"
        # Full decode, not just readable container headers.
        run(['-v', 'error', '-xerror', '-i', str(path), '-f', 'null', '-'])
        info = MP3(path).info
        assert info.length > 0 and path.stat().st_size > 0
        row.update(status='generated_full_decode_passed', file=str(path.relative_to(ROOT)),
                   bytes=path.stat().st_size, sha256=digest(path),
                   duration_seconds=info.length, estimated_concat_start_seconds=offset,
                   sample_rate=info.sample_rate, channels=info.channels,
                   auditory_qc='not performed', alignment='not forced-aligned')
        offset += info.length
    output = AUDIO / 'EP001_COMPLETE_NARRATION_v01.mp3'
    # A local temporary concat manifest avoids shell quoting/interpolation.
    with tempfile.TemporaryDirectory() as folder:
        playlist = Path(folder) / 'concat.txt'
        playlist.write_text(''.join(f"file '{(AUDIO / f'{i:02d}.mp3').as_posix()}'\n"
                                    for i in range(1, 12)))
        run(['-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', str(playlist),
             '-map', '0:a:0', '-vn', '-ar', '44100', '-ac', '1', '-c:a', 'libmp3lame',
             '-b:a', '128k', '-metadata', 'title=Before the Dragons - Complete Narration v01',
             str(output)])
    run(['-v', 'error', '-xerror', '-i', str(output), '-f', 'null', '-'])
    # Measure encoded output peaks/mean; not a loudness-normalization or listening pass.
    stats = run(['-i', str(output), '-af', 'volumedetect', '-f', 'null', '-']).stderr
    peaks = re.search(r'max_volume: ([\-\d.]+) dB', stats)
    mean = re.search(r'mean_volume: ([\-\d.]+) dB', stats)
    duration = MP3(output).info.length
    manifest.update(status='COMPLETE_REVIEW_AUDIO_11_OF_11', full_audio_complete=True,
                    total_generated_duration_seconds=offset,
                    timing_status='Measured audio duration; speech-to-text alignment pending',
                    complete_track={'file': str(output.relative_to(ROOT)), 'bytes': output.stat().st_size,
                                    'sha256': digest(output), 'duration_seconds': duration,
                                    'decode_check': 'passed', 'auditory_qc': 'not performed',
                                    'max_volume_dbfs': float(peaks[1]) if peaks else None,
                                    'mean_volume_dbfs': float(mean[1]) if mean else None,
                                    'assembly': 'concat in numeric order, decoded and re-encoded mono 44.1kHz 128kbps; no added gaps, fades, music or normalization',
                                    'boundary_timing_note': 'Chunk starts estimated from source MP3 durations; encoder delay may cause small deviations. Not subtitle timing.'})
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    with (FILM / '07_AUDIO_CHUNK_CUES.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=['clip', 'start_seconds_approx', 'source_duration_seconds', 'opening_words', 'closing_words'])
        writer.writeheader()
        for row in clips:
            words = row['text'].split()
            writer.writerow({'clip': row['clip'], 'start_seconds_approx': round(row['estimated_concat_start_seconds'], 3),
                             'source_duration_seconds': round(row['duration_seconds'], 3),
                             'opening_words': ' '.join(words[:12]), 'closing_words': ' '.join(words[-12:])})
    print(json.dumps(manifest['complete_track'], indent=2))


if __name__ == '__main__':
    main()
