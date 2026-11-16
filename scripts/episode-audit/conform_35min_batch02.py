"""Conform B007–B010 and assemble Chapter I, without changing any narration words.

Run using .venv/bin/python. Requires raw generated MP3s and existing B001–B006
PCM windows. Technical timing/decode checks do not constitute listening approval.
"""
import json
import re
import tempfile
from pathlib import Path

from conform_35min_batch01 import A, F, RATE, ROOT, digest, read_wav, run, tokens, write_wav

TAKES = {
    'B007_take01': "At the far eastern edge of the known world stood Asshai beside the River Ash... a place later accounts describe through darkness, strange sorcery, and stone that seems to swallow light.\n\nIts beginnings are obscure.\n\nWe cannot simply project every later description unchanged into the distant past.\n\nBut remember its name.\n\nWhen we reach the secret of dragon mastery... an eastern tradition will claim that Valyria owed everything to forgotten teachers.",
    'B008_take01': "For worldly power, however... our story turns toward Old Ghis.\n\nIts stepped brick pyramids rose above a civilization of conquest and wealth, watched over by the harpy with its thunderbolt.\n\nWhere Valyria offers us a beginning among flocks... Ghis presents the confidence of an established empire.\n\nIts monuments declared that power could be made permanent.\n\nIts armies existed... to persuade anyone who doubted that declaration.",
    'B009_take01': "Grazdan the Great was remembered as the founder of Ghiscari greatness... and the lockstep legions as its terrible instrument.\n\nShields, swords, and spears mattered. So did the discipline that made many soldiers move like one.\n\nBehind the military achievement... lay an economy built on slavery.\n\nConquest brought captives; captivity supported wealth.\n\nKeep that chain in mind.\n\nValyria would challenge this empire... without escaping its most brutal logic.",
    'B010_take01': "Set the two worlds beside each other... brick pyramids and pasture, marching soldiers and wandering flocks, the certainty of an empire and the obscurity of a peninsula.\n\nWe cannot recover a Ghiscari captain's thoughts as he watched the horizon.\n\nBut we know what the contrast conceals.\n\nThe mountains above those shepherds held something... the legions did not possess.\n\nTo understand Valyria's future... we must climb toward them.",
}


def main():
    authored = json.loads((F / 'narration_blocks_v02.json').read_text())
    protected = json.loads((F / '06_VALIDATION_REPORT.json').read_text())['baseline_hashes_after']
    for path, expected in protected.items():
        assert digest(ROOT / path) == expected
    rows = []
    with tempfile.TemporaryDirectory() as folder:
        tmp = Path(folder)
        for name, text in TAKES.items():
            n = int(name[1:4])
            assert tokens(text) == tokens(authored[n - 1]), name
            raw = A / f'raw/{name}.mp3'
            decoded = tmp / f'{name}.wav'
            run(['-y', '-v', 'error', '-xerror', '-i', str(raw), '-ar', str(RATE),
                 '-ac', '1', '-c:a', 'pcm_s16le', str(decoded)])
            frames, _ = read_wav(decoded)
            factor = frames / RATE / 29.9
            assert 0.92 <= factor <= 1.08, (name, factor)
            processed = tmp / 'processed.wav'
            run(['-y', '-v', 'error', '-i', str(decoded), '-af', f'atempo={factor:.12f}',
                 '-c:a', 'pcm_s16le', str(processed)])
            count, data = read_wav(processed)
            padding = 30 * RATE - count
            assert 0 <= padding <= RATE * 0.2
            out = A / f'review/B{n:03d}_30sec_v01.wav'
            write_wav(out, data + b'\x00\x00' * padding)
            assert read_wav(out)[0] == 30 * RATE
            rows.append({'block': f'B{n:03d}', 'voice_id': 'voice-01',
                         'selected_take': name, 'submitted_text': text,
                         'word_sequence_matches_authored_block': True,
                         'raw_file': str(raw.relative_to(ROOT)), 'raw_sha256': digest(raw),
                         'raw_decoded_samples': frames, 'raw_decoded_seconds': frames / RATE,
                         'atempo_factor': factor, 'tempo_change_percent': (factor - 1) * 100,
                         'boundary_pad_samples': padding, 'boundary_pad_seconds': padding / RATE,
                         'placed_interval_seconds': [(n - 1) * 30, n * 30],
                         'image_range': [(n - 1) * 15 + 1, n * 15],
                         'file': str(out.relative_to(ROOT)), 'sha256': digest(out),
                         'samples': 30 * RATE, 'duration_seconds': 30,
                         'decode_check': 'passed', 'listening_qc': 'pending', 'final_approved': False})
        pilot = json.loads((F / '08_RECORDING_PILOT_MANIFEST.json').read_text())
        prior = json.loads((F / '10_RECORDING_BATCH01_MANIFEST.json').read_text())
        prior_rows = [pilot['master']] + prior['new_conformed_blocks']
        all_paths = []
        for row in prior_rows:
            path = ROOT / row['file']
            assert digest(path) == row['sha256']
            all_paths.append(path)
        all_paths += [ROOT / row['file'] for row in rows]
        assert len(all_paths) == 10
        pcm = []
        for path in all_paths:
            frames, data = read_wav(path)
            assert frames == 30 * RATE
            pcm.append(data)
        combined = tmp / 'chapter01.wav'
        combined_pcm = b''.join(pcm)
        write_wav(combined, combined_pcm)
        assert read_wav(combined)[0] == 300 * RATE
        # Persist lossless FLAC rather than another large duplicate PCM file.
        flac = A / 'review/EP001_CHAPTER_I_00m00s-05m00s_v01.flac'
        run(['-y', '-v', 'error', '-i', str(combined), '-c:a', 'flac', str(flac)])
        check = tmp / 'roundtrip.wav'
        run(['-y', '-v', 'error', '-xerror', '-i', str(flac), '-c:a', 'pcm_s16le', str(check)])
        check_frames, check_pcm = read_wav(check)
        assert check_frames == 300 * RATE and check_pcm == combined_pcm
        preview = flac.with_suffix('.mp3')
        run(['-y', '-v', 'error', '-i', str(flac), '-c:a', 'libmp3lame', '-b:a', '192k', str(preview)])
        run(['-v', 'error', '-xerror', '-i', str(preview), '-f', 'null', '-'])
        stats = run(['-i', str(flac), '-af', 'volumedetect', '-f', 'null', '-']).stderr
        peak = re.search(r'max_volume: ([\-\d.]+) dB', stats)
        report = {'status': 'CHAPTER_I_TECHNICALLY_CONFORMED_LISTENING_PENDING',
                  'voice_id': 'voice-01', 'technically_conformed_blocks': 10,
                  'remaining_unrecorded_blocks': 60, 'remaining_unrecorded_seconds': 1800,
                  'image_range': [1, 150], 'new_conformed_blocks': rows,
                  'prior_manifests': ['08_RECORDING_PILOT_MANIFEST.json', '10_RECORDING_BATCH01_MANIFEST.json'],
                  'master': {'file': str(flac.relative_to(ROOT)), 'sha256': digest(flac),
                             'format': 'lossless FLAC, mono, 48kHz, 16-bit', 'samples': check_frames,
                             'duration_seconds': 300, 'pcm_roundtrip_byte_identical': True,
                             'max_sample_volume_dbfs': float(peak[1]) if peak else None},
                  'preview_mp3': {'file': str(preview.relative_to(ROOT)), 'sha256': digest(preview),
                                  'timing_note': 'Codec delay may affect displayed MP3 duration; lossless master governs'},
                  'not_performed': ['listening/ASR QC', 'pronunciation approval',
                                    'word-to-image synchronization', 'visual QC', 'music or mastering'],
                  'final_approved': False}
        for path, expected in protected.items():
            assert digest(ROOT / path) == expected
        (F / '12_RECORDING_BATCH02_MANIFEST.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps({'master': report['master'], 'new_blocks': [{
            'block': r['block'], 'decoded_seconds': r['raw_decoded_seconds'],
            'tempo_percent': r['tempo_change_percent'], 'pad_seconds': r['boundary_pad_seconds']}
            for r in rows]}, indent=2))


if __name__ == '__main__':
    main()
