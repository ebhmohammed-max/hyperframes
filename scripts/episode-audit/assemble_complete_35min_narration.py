"""Assemble only verified fixed-window masters; technical QC, not listening approval."""
import json
import tempfile
from pathlib import Path

from conform_35min_batch01 import A, F, RATE, ROOT, digest, read_wav, run, write_wav
from conform_35min_batch09 import encode_lossless


def main():
    protected = json.loads((F / '06_VALIDATION_REPORT.json').read_text())['baseline_hashes_after']
    rows = []
    for path in sorted(F.glob('*MANIFEST.json')):
        report = json.loads(path.read_text())
        if 'new_conformed_blocks' in report:
            rows.extend(report['new_conformed_blocks'])
        elif path.name == '08_RECORDING_PILOT_MANIFEST.json':
            rows.append({**report, **report['master']})
    assert len(rows) == 70
    for path, expected in protected.items():
        assert digest(ROOT / path) == expected
    chapters = [
        ('12_RECORDING_BATCH02_MANIFEST.json', 300),
        ('16_RECORDING_BATCH04_MANIFEST.json', 300),
        ('21_RECORDING_BATCH06_MANIFEST.json', 300),
        ('27_RECORDING_BATCH08_MANIFEST.json', 330),
        ('33_RECORDING_BATCH10_MANIFEST.json', 300),
        ('39_RECORDING_BATCH12_MANIFEST.json', 300),
        ('45_RECORDING_BATCH14_MANIFEST.json', 270),
    ]
    with tempfile.TemporaryDirectory() as folder:
        tmp = Path(folder)
        pieces = []
        for i, row in enumerate(rows):
            assert row['placed_interval_seconds'] == [i * 30, (i + 1) * 30]
            assert row['image_range'] == [i * 15 + 1, (i + 1) * 15]
            path = ROOT / row['file']
            assert digest(path) == row['sha256']
            decoded = tmp / 'block.wav'
            run(['-y', '-v', 'error', '-xerror', '-i', str(path), '-ar', str(RATE),
                 '-ac', '1', '-c:a', 'pcm_s16le', str(decoded)])
            frames, pcm = read_wav(decoded)
            assert frames == 30 * RATE
            pieces.append(pcm)
        pcm = b''.join(pieces)
        offset = 0
        chapter_records = []
        for name, seconds in chapters:
            master = json.loads((F / name).read_text())['master']
            path = ROOT / master['file']
            assert digest(path) == master['sha256']
            decoded = tmp / 'chapter.wav'
            run(['-y', '-v', 'error', '-xerror', '-i', str(path), '-c:a', 'pcm_s16le', str(decoded)])
            frames, chapter_pcm = read_wav(decoded)
            assert frames == seconds * RATE
            assert pcm[offset:offset + len(chapter_pcm)] == chapter_pcm
            offset += len(chapter_pcm)
            chapter_records.append({'manifest': name, 'duration_seconds': seconds,
                                    'matches_conformed_block_pcm': True, **master})
        assert offset == len(pcm) == 2100 * RATE * 2
        combined = tmp / 'complete.wav'
        write_wav(combined, pcm)
        master = A / 'review/EP001_COMPLETE_NARRATION_35m00s_v01.flac'
        frames = encode_lossless(combined, master, tmp / 'roundtrip.wav')
        assert frames == 100800000
        preview = master.with_suffix('.mp3')
        run(['-y', '-v', 'error', '-i', str(master), '-c:a', 'libmp3lame', '-b:a', '192k', str(preview)])
        run(['-v', 'error', '-xerror', '-i', str(preview), '-f', 'null', '-'])
        report = {'status': 'FULL_35MIN_TECHNICALLY_CONFORMED_LISTENING_PENDING',
                  'voice_id': 'voice-01', 'blocks': 70, 'image_slots': 1050,
                  'editorial_interval_seconds': [0, 2100], 'chapters': chapter_records,
                  'master': {'file': str(master.relative_to(ROOT)), 'sha256': digest(master),
                             'samples': frames, 'sample_rate': RATE, 'duration_seconds': 2100,
                             'format': 'lossless FLAC mono48kHz16bit',
                             'pcm_roundtrip_byte_identical': True},
                  'preview_mp3': {'file': str(preview.relative_to(ROOT)), 'sha256': digest(preview)},
                  'baseline_hashes_unchanged': True,
                  'not_performed': ['listening/ASR QC', 'pronunciation approval', 'join review',
                                    'word-to-image synchronization', 'visual approval',
                                    'music/sound mix or mastering', 'film render'],
                  'final_approved': False}
        for path, expected in protected.items():
            assert digest(ROOT / path) == expected
        (F / '47_COMPLETE_35MIN_AUDIO_MANIFEST.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps(report['master'], indent=2))


if __name__ == '__main__':
    main()
