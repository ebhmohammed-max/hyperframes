"""Technical conform of B002–B006, preserving every authored word and fixed slot.

All takes are retained. This script does not synthesize, listen, align words to images,
or approve performances. Requires imageio-ffmpeg and existing raw MP3s.
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
F = EP / 'story_film_35min'
A = F / 'audio'
RATE = 48000
TAKES = {
    'B002_take01': "The answer begins... far from a throne.\n\nBeneath fourteen volcanic mountains, flocks moved through pasture... and families worked the wool that sustained them.\n\nNo surviving chronicle gives us the first shepherd's name. No witness describes the first successful flight.\n\nBut between those two images... a flock below and a rider above... lies one of history's greatest transformations.\n\nFirst came discovery.\n\nThen came the struggle... to possess it.",
    'B002_take02': "The answer begins far from a throne.\n\nBeneath fourteen volcanic mountains, flocks moved through pasture and families worked the wool that sustained them.\n\nNo surviving chronicle gives us the first shepherd's name. No witness describes the first successful flight.\n\nBut between those two images... a flock below and a rider above... lies one of history's greatest transformations.\n\nFirst came discovery.\n\nThen came the struggle... to possess it.",
    'B003_take01': "To follow that transformation... we must travel thousands of years before Aegon's Conquest, into an age whose dates remain uncertain.\n\nLater histories place Valyria's rise roughly five thousand years before the Conquest... but distance has blurred the chronology.\n\nBeyond those fragile records stretches an older darkness... the Long Night.\n\nAcross Essos, peoples remembered a catastrophe so vast... that its ending became the foundation of legend.",
    'B004_take01': "Along the Rhoyne... the darkness survived in stories of frozen water and a world waiting for the dawn.\n\nOne tradition tells of a hero who persuaded the quarreling children of Mother Rhoyne... to sing together and bring back daylight.\n\nThe Crab King and the Old Man of the River belong to that telling.\n\nHere, salvation was remembered... not simply as conquest... but as voices joining against the night.",
    'B004_take02': "Along the Rhoyne... the darkness survived in stories of frozen water... and a world waiting for the dawn.\n\nOne tradition tells of a hero... who persuaded the quarreling children of Mother Rhoyne... to sing together and bring back daylight.\n\nThe Crab King and the Old Man of the River... belong to that telling.\n\nHere, salvation was remembered... not simply as conquest... but as voices joining against the night.",
    'B005_take01': "Farther east... the traditions of Yi Ti tell a different story.\n\nThe Bloodstone Emperor murdered his sister, the Amethyst Empress... and the Blood Betrayal helped cast the world into darkness.\n\nElsewhere, heroes bearing different names fought that darkness with living fire.\n\nThese are related echoes... not one reliable eyewitness account.\n\nWhat unites them is the memory of a world broken... and the struggle to make it habitable again.",
    'B006_take01': "Out of those uncertain ages emerge the peoples of ancient Essos... river settlements, grassland kingdoms, and communities whose histories are now fragments.\n\nAlong the Mother Rhoyne, craft, trade, and river life nourished a civilization remembered for accomplishments... very different from Valyria's.\n\nThe continent was not empty... waiting for dragonlords to invent greatness.\n\nIt already held worlds of its own.\n\nValyria began at their margins... not their center.",
    'B006_take02': "Out of those uncertain ages emerge the peoples of ancient Essos: river settlements, grassland kingdoms, and communities whose histories are now fragments.\n\nAlong the Mother Rhoyne, craft, trade, and river life nourished a civilization remembered for accomplishments... very different from Valyria's.\n\nThe continent was not empty... waiting for dragonlords to invent greatness.\n\nIt already held worlds of its own.\n\nValyria began at their margins... not their center.",
}
SELECTED = {2: 2, 3: 1, 4: 2, 5: 1, 6: 2}


def run(args):
    return subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-hide_banner', '-nostdin', *args],
                          capture_output=True, text=True, check=True)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_wav(path):
    with wave.open(str(path), 'rb') as w:
        assert (w.getframerate(), w.getnchannels(), w.getsampwidth()) == (RATE, 1, 2)
        return w.getnframes(), w.readframes(w.getnframes())


def write_wav(path, data):
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(data)


def tokens(text):
    return re.findall(r"\b\w+(?:['’\-]\w+)*\b", text.lower())


def main():
    paragraphs = json.loads((F / 'narration_blocks_v02.json').read_text())
    protected = json.loads((F / '06_VALIDATION_REPORT.json').read_text())['baseline_hashes_after']
    for path, expected in protected.items():
        assert digest(ROOT / path) == expected
    (A / 'review').mkdir(exist_ok=True)
    records, outputs = [], []
    with tempfile.TemporaryDirectory() as folder:
        tmp = Path(folder)
        for name, text in TAKES.items():
            n = int(name[1:4])
            assert tokens(text) == tokens(paragraphs[n - 1]), name
            raw, decoded = A / f'raw/{name}.mp3', tmp / f'{name}.wav'
            run(['-y', '-v', 'error', '-xerror', '-i', str(raw), '-ar', str(RATE),
                 '-ac', '1', '-c:a', 'pcm_s16le', str(decoded)])
            count, _ = read_wav(decoded)
            selected = name == f'B{n:03d}_take{SELECTED[n]:02d}'
            records.append({'take': name, 'voice_id': 'voice-01', 'submitted_text': text,
                            'word_sequence_matches_authored_block': True,
                            'decoded_samples': count, 'decoded_seconds': count / RATE,
                            'file': str(raw.relative_to(ROOT)), 'sha256': digest(raw),
                            'decode_check': 'passed', 'selected_for_technical_conform': selected,
                            'auditory_qc': 'not performed'})
        for n, take in SELECTED.items():
            name = f'B{n:03d}_take{take:02d}'
            row = next(r for r in records if r['take'] == name)
            factor = row['decoded_seconds'] / 29.9
            assert 0.92 <= factor <= 1.08, (name, factor)
            processed = tmp / 'processed.wav'
            run(['-y', '-v', 'error', '-i', str(tmp / f'{name}.wav'), '-af',
                 f'atempo={factor:.12f}', '-c:a', 'pcm_s16le', str(processed)])
            count, data = read_wav(processed)
            pad = RATE * 30 - count
            assert 0 <= pad <= RATE * 0.2, (name, pad)
            out = A / f'review/B{n:03d}_30sec_v01.wav'
            write_wav(out, data + b'\x00\x00' * pad)
            assert read_wav(out)[0] == 30 * RATE
            outputs.append({'block': f'B{n:03d}', 'selected_take': name,
                            'placed_interval_seconds': [(n - 1) * 30, n * 30],
                            'image_range': [(n - 1) * 15 + 1, n * 15],
                            'atempo_factor': factor, 'tempo_change_percent': (factor - 1) * 100,
                            'processed_samples_before_pad': count, 'boundary_pad_samples': pad,
                            'boundary_pad_seconds': pad / RATE, 'duration_seconds': 30,
                            'file': str(out.relative_to(ROOT)), 'sha256': digest(out),
                            'final_approved': False, 'listening_qc': 'pending'})
        pilot = json.loads((F / '08_RECORDING_PILOT_MANIFEST.json').read_text())
        first = ROOT / pilot['master']['file']
        assert digest(first) == pilot['master']['sha256']
        pieces = [first] + [ROOT / r['file'] for r in outputs]
        pcm = []
        for p in pieces:
            count, data = read_wav(p)
            assert count == 30 * RATE
            pcm.append(data)
        master = A / 'review/EP001_OPENING_00m00s-03m00s_v01.wav'
        write_wav(master, b''.join(pcm))
        count, _ = read_wav(master)
        assert count == 180 * RATE
        preview = master.with_suffix('.mp3')
        run(['-y', '-v', 'error', '-i', str(master), '-c:a', 'libmp3lame', '-b:a', '192k', str(preview)])
        run(['-v', 'error', '-xerror', '-i', str(preview), '-f', 'null', '-'])
        stats = run(['-i', str(master), '-af', 'volumedetect', '-f', 'null', '-']).stderr
        peak = re.search(r'max_volume: ([\-\d.]+) dB', stats)
        report = {'status': 'B001_B006_TECHNICALLY_CONFORMED_LISTENING_PENDING',
                  'narrator': 'voice-01', 'total_blocks_in_film': 70,
                  'technically_conformed_blocks': 6, 'remaining_unrecorded_blocks': 64,
                  'image_range': [1, 90], 'takes_this_batch': records, 'new_conformed_blocks': outputs,
                  'previous_block_manifest': '08_RECORDING_PILOT_MANIFEST.json',
                  'master': {'file': str(master.relative_to(ROOT)), 'sha256': digest(master),
                             'sample_rate': RATE, 'samples': count, 'duration_seconds': 180,
                             'max_sample_volume_dbfs': float(peak[1]) if peak else None},
                  'preview_mp3': {'file': str(preview.relative_to(ROOT)), 'sha256': digest(preview)},
                  'checks': ['all eight new takes fully decoded', 'input word sequence matches authored blocks',
                             'selected tempo factors within0.92–1.08', 'each PCM window exactly30seconds',
                             'combined PCM exactly180seconds', 'preview MP3 fully decoded',
                             'protected baseline script/map/ledger hashes unchanged'],
                  'not_performed': ['listening/ASR QC', 'pronunciation approval', 'word-to-image alignment',
                                    'visual QC', 'sound design/music/mastering'], 'final_approved': False}
        for path, expected in protected.items():
            assert digest(ROOT / path) == expected
        (F / '10_RECORDING_BATCH01_MANIFEST.json').write_text(json.dumps(report, indent=2) + '\n')
        print(json.dumps({'master': report['master'], 'blocks': outputs}, indent=2))


if __name__ == '__main__':
    main()
