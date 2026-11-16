"""Conform B011–B015 and assemble the05:00–07:30 review segment.

Keeps per-block lossless FLAC instead of duplicate large PCM files. Does not
synthesize speech, listen, approve pronunciation, or certify image alignment.
"""
import json
import re
import tempfile
from pathlib import Path

from conform_35min_batch01 import A, F, RATE, ROOT, digest, read_wav, run, tokens, write_wav


def encode_lossless(pcm_path, flac_path, scratch):
    """Encode and prove exact PCM roundtrip, including sample count."""
    frames, data = read_wav(pcm_path)
    run(['-y', '-v', 'error', '-i', str(pcm_path), '-c:a', 'flac', str(flac_path)])
    run(['-y', '-v', 'error', '-xerror', '-i', str(flac_path), '-c:a', 'pcm_s16le', str(scratch)])
    check_frames, check_data = read_wav(scratch)
    assert (frames, data) == (check_frames, check_data)
    return frames


def main():
    authored = json.loads((F / 'narration_blocks_v02.json').read_text())
    config = json.loads((F / 'recording_batch03_inputs.json').read_text())
    protected = json.loads((F / '06_VALIDATION_REPORT.json').read_text())['baseline_hashes_after']
    for path, expected in protected.items():
        assert digest(ROOT / path) == expected
    previous = json.loads((F / '12_RECORDING_BATCH02_MANIFEST.json').read_text())
    assert previous['technically_conformed_blocks'] == 10
    assert digest(ROOT / previous['master']['file']) == previous['master']['sha256']
    records, outputs, pieces = [], [], []
    with tempfile.TemporaryDirectory() as folder:
        tmp = Path(folder)
        for name, text in config['takes'].items():
            n = int(name[1:4])
            assert tokens(text) == tokens(authored[n - 1])
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
            pieces.append(pcm)
            outputs.append({'block': f'B{n:03d}', 'selected_take': name,
                            'placed_interval_seconds': [(n - 1) * 30, n * 30],
                            'image_range': [(n - 1) * 15 + 1, n * 15],
                            'atempo_factor': factor, 'tempo_change_percent': (factor - 1) * 100,
                            'boundary_pad_samples': pad, 'boundary_pad_seconds': pad / RATE,
                            'samples': frames, 'duration_seconds': 30,
                            'file': str(out.relative_to(ROOT)), 'sha256': digest(out),
                            'pcm_roundtrip_byte_identical': True, 'final_approved': False})
        assert [r['block'] for r in outputs] == [f'B{n:03d}' for n in range(11, 16)]
        combined = tmp / 'segment.wav'
        write_wav(combined, b''.join(pieces))
        master = A / 'review/EP001_CHAPTER_II_PART1_05m00s-07m30s_v01.flac'
        frames = encode_lossless(combined, master, tmp / 'roundtrip.wav')
        assert frames == 150 * RATE
        preview = master.with_suffix('.mp3')
        run(['-y', '-v', 'error', '-i', str(master), '-c:a', 'libmp3lame', '-b:a', '192k', str(preview)])
        run(['-v', 'error', '-xerror', '-i', str(preview), '-f', 'null', '-'])
        stats = run(['-i', str(master), '-af', 'volumedetect', '-f', 'null', '-']).stderr
        peak = re.search(r'max_volume: ([\-\d.]+) dB', stats)
        report = {'status': 'B011_B015_TECHNICALLY_CONFORMED_LISTENING_PENDING',
                  'voice_id': 'voice-01', 'takes_this_batch': records, 'new_conformed_blocks': outputs,
                  'technically_conformed_blocks_cumulative': 15, 'remaining_unrecorded_blocks': 55,
                  'cumulative_editorial_coverage_seconds': [0, 450],
                  'segment_editorial_interval_seconds': [300, 450], 'segment_image_range': [151, 225],
                  'previous_master_manifest': '12_RECORDING_BATCH02_MANIFEST.json',
                  'master': {'file': str(master.relative_to(ROOT)), 'sha256': digest(master),
                             'sample_rate': RATE, 'samples': frames, 'duration_seconds': 150,
                             'format': 'lossless FLAC mono48kHz16bit', 'pcm_roundtrip_byte_identical': True,
                             'max_sample_volume_dbfs': float(peak[1]) if peak else None},
                  'preview_mp3': {'file': str(preview.relative_to(ROOT)), 'sha256': digest(preview)},
                  'not_performed': ['listening/ASR QC', 'pronunciation approval', 'picture synchronization',
                                    'visual QC', 'music/sound mix or mastering'], 'final_approved': False}
        for path, expected in protected.items():
            assert digest(ROOT / path) == expected
        (F / '14_RECORDING_BATCH03_MANIFEST.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps({'master': report['master'], 'new_blocks': [{
            'block': r['block'], 'tempo_percent': r['tempo_change_percent'],
            'pad_seconds': r['boundary_pad_seconds']} for r in outputs]}, indent=2))


if __name__ == '__main__':
    main()
