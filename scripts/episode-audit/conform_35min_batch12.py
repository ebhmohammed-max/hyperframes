"""Conform B057–B061; assemble complete Chapter VI with verified prior prefix.

Technical timing/decode checks only; does not claim listening or picture approval.
"""
import json
import re
import tempfile
from pathlib import Path

from conform_35min_batch01 import A, F, RATE, ROOT, digest, read_wav, run, tokens, write_wav
from conform_35min_batch03 import encode_lossless


def main():
    authored = json.loads((F / 'narration_blocks_v02.json').read_text())
    config = json.loads((F / 'recording_batch12_inputs.json').read_text())
    protected = json.loads((F / '06_VALIDATION_REPORT.json').read_text())['baseline_hashes_after']
    for path, expected in protected.items():
        assert digest(ROOT / path) == expected
    prior = json.loads((F / '36_RECORDING_BATCH11_MANIFEST.json').read_text())
    assert prior['technically_conformed_blocks_cumulative'] == 56
    prior_chapter = json.loads((F / '33_RECORDING_BATCH10_MANIFEST.json').read_text())
    for old in [prior['master'], prior_chapter['master']]:
        assert digest(ROOT / old['file']) == old['sha256']
    records, outputs, new_pieces = [], [], []
    with tempfile.TemporaryDirectory() as folder:
        tmp = Path(folder)
        for name, text in config['takes'].items():
            n = int(name[1:4])
            assert tokens(text) == tokens(authored[n - 1]), name
            raw, decoded = A / f'raw/{name}.mp3', tmp / f'{name}.wav'
            run(['-y', '-v', 'error', '-xerror', '-i', str(raw), '-ar', str(RATE),
                 '-ac', '1', '-c:a', 'pcm_s16le', str(decoded)])
            frames, _ = read_wav(decoded)
            records.append({'take': name, 'voice_id': 'voice-01', 'submitted_text': text,
                            'word_sequence_matches_authored_block': True,
                            'file': str(raw.relative_to(ROOT)), 'sha256': digest(raw),
                            'decoded_samples': frames, 'decoded_seconds': frames / RATE,
                            'decode_check': 'passed', 'listening_qc': 'pending'})
        for n, take in sorted((int(k), v) for k, v in config['selected_takes'].items()):
            name = f'B{n:03d}_take{take:02d}'
            rec = next(r for r in records if r['take'] == name)
            factor = rec['decoded_seconds'] / 29.9
            assert 0.92 <= factor <= 1.08, (name, factor)
            processed = tmp / 'processed.wav'
            run(['-y', '-v', 'error', '-i', str(tmp / f'{name}.wav'), '-af',
                 f'atempo={factor:.12f}', '-c:a', 'pcm_s16le', str(processed)])
            count, data = read_wav(processed)
            pad = 30 * RATE - count
            assert 0 <= pad <= RATE * 0.2
            final = tmp / 'final.wav'
            pcm = data + b'\x00\x00' * pad
            write_wav(final, pcm)
            out = A / f'review/B{n:03d}_30sec_v01.flac'
            frames = encode_lossless(final, out, tmp / 'roundtrip.wav')
            assert frames == 30 * RATE
            new_pieces.append(pcm)
            outputs.append({'block': f'B{n:03d}', 'selected_take': name,
                            'placed_interval_seconds': [(n - 1) * 30, n * 30],
                            'image_range': [(n - 1) * 15 + 1, n * 15],
                            'atempo_factor': factor, 'tempo_change_percent': (factor - 1) * 100,
                            'boundary_pad_samples': pad, 'boundary_pad_seconds': pad / RATE,
                            'samples': frames, 'duration_seconds': 30,
                            'file': str(out.relative_to(ROOT)), 'sha256': digest(out),
                            'pcm_roundtrip_byte_identical': True, 'final_approved': False})
        assert [r['block'] for r in outputs] == [f'B{n:03d}' for n in range(57, 62)]
        prefix = tmp / 'prefix.wav'
        run(['-y', '-v', 'error', '-xerror', '-i', str(ROOT / prior['master']['file']),
             '-c:a', 'pcm_s16le', str(prefix)])
        prefix_frames, prefix_pcm = read_wav(prefix)
        assert prefix_frames == 150 * RATE
        # Re-check all prior block masters against the first-half assembly.
        check_pieces = []
        for row in prior['new_conformed_blocks']:
            path = ROOT / row['file']
            assert digest(path) == row['sha256']
            decoded = tmp / 'oldblock.wav'
            run(['-y', '-v', 'error', '-xerror', '-i', str(path), '-c:a', 'pcm_s16le', str(decoded)])
            count, pcm = read_wav(decoded)
            assert count == 30 * RATE
            check_pieces.append(pcm)
        assert b''.join(check_pieces) == prefix_pcm
        combined = tmp / 'chapter06.wav'
        write_wav(combined, prefix_pcm + b''.join(new_pieces))
        master = A / 'review/EP001_CHAPTER_VI_25m30s-30m30s_v01.flac'
        frames = encode_lossless(combined, master, tmp / 'roundtrip.wav')
        assert frames == 300 * RATE
        preview = master.with_suffix('.mp3')
        run(['-y', '-v', 'error', '-i', str(master), '-c:a', 'libmp3lame', '-b:a', '192k', str(preview)])
        run(['-v', 'error', '-xerror', '-i', str(preview), '-f', 'null', '-'])
        stats = run(['-i', str(master), '-af', 'volumedetect', '-f', 'null', '-']).stderr
        peak = re.search(r'max_volume: ([\-\d.]+) dB', stats)
        report = {'status': 'CHAPTER_VI_TECHNICALLY_CONFORMED_LISTENING_PENDING',
                  'voice_id': 'voice-01', 'takes_this_batch': records, 'new_conformed_blocks': outputs,
                  'technically_conformed_blocks_cumulative': 61, 'remaining_unrecorded_blocks': 9,
                  'cumulative_editorial_coverage_seconds': [0, 1830],
                  'chapter_editorial_interval_seconds': [1530, 1830], 'chapter_image_range': [766, 915],
                  'previous_part_manifest': '36_RECORDING_BATCH11_MANIFEST.json',
                  'previous_chapter_manifest': '33_RECORDING_BATCH10_MANIFEST.json',
                  'master': {'file': str(master.relative_to(ROOT)), 'sha256': digest(master),
                             'sample_rate': RATE, 'samples': frames, 'duration_seconds': 300,
                             'format': 'lossless FLAC mono48kHz16bit', 'pcm_roundtrip_byte_identical': True,
                             'prefix_matches_previous_part': True,
                             'max_sample_volume_dbfs': float(peak[1]) if peak else None},
                  'preview_mp3': {'file': str(preview.relative_to(ROOT)), 'sha256': digest(preview)},
                  'not_performed': ['listening/ASR QC', 'pronunciation approval', 'picture synchronization',
                                    'visual QC', 'music/sound mix or mastering'], 'final_approved': False}
        for path, expected in protected.items():
            assert digest(ROOT / path) == expected
        (F / '39_RECORDING_BATCH12_MANIFEST.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps({'master': report['master'], 'new_blocks': [{
            'block': r['block'], 'tempo_percent': r['tempo_change_percent'],
            'pad_seconds': r['boundary_pad_seconds']} for r in outputs]}, indent=2))


if __name__ == '__main__':
    main()
