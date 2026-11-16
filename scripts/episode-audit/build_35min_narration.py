"""Build and validate the fixed 35-minute narration documents, without editing sources.

Input: seventy authored paragraphs, the preserved scene map, and the current ledger.
No audio synthesis, retiming, image approvals or historical-source certification.
"""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EPISODE = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria'
OUTPUT = EPISODE / 'story_film_35min'

CHAPTERS = [
    (1, 10, 'I', 'The world before the dragonlords'),
    (11, 20, 'II', 'The mountains gave twice'),
    (21, 30, 'III', 'The creature inside the mountain'),
    (31, 41, 'IV', 'The missing secret'),
    (42, 51, 'V', 'Who gets to rise?'),
    (52, 61, 'VI', 'The beautiful surface, the darkness below'),
    (62, 70, 'VII', 'The harpy looks west'),
]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def words(text):
    return len(re.findall(r"\b\w+(?:['’\-]\w+)*\b", text))


def clock(seconds):
    return f'{seconds // 60:02d}:{seconds % 60:02d}'


def dump_csv(path, rows):
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main():
    source = EPISODE / 'original_baseline/02_COMPLETE_NARRATION_SCRIPT.md'
    scene_source = EPISODE / 'original_baseline/03_SCENE_BREAKDOWN_1050_SCENES.json'
    ledger_source = EPISODE / 'audit/EP001_SHOT_AUDIT_LEDGER.json'
    protected = [source, scene_source, ledger_source]
    before = {str(p.relative_to(ROOT)): sha(p) for p in protected}
    paragraphs = json.loads((OUTPUT / 'narration_blocks_v02.json').read_text())
    baseline = re.findall(r'(\[\d\d:\d\d–\d\d:\d\d \| VAL-EP001-IMG\d{4}–IMG\d{4}\])\n(.+?)(?=\n\n)', source.read_text(), re.S)
    shots = json.loads(scene_source.read_text())
    ledger = json.loads(ledger_source.read_text())
    by_id = {row['scene_id']: row for row in ledger['shots']}
    assert len(paragraphs) == len(baseline) == 70
    assert len(shots) == len(by_id) == 1050
    assert all(isinstance(t, str) and t.strip() and '\n' not in t for t in paragraphs)
    blocks, candidate_rows = [], []
    markdown = ['# Before the Dragons: The Rise of Old Valyria',
                '## Complete narration · fixed 35-minute edition · v02',
                '**AUTHORITATIVE SCOPE: 35:00 · 1,050 image slots · 2 seconds per slot · 70 narration blocks of 30 seconds.**',
                'The earlier 15:57 recording is a rejected condensed alternative, NOT this film’s soundtrack. This document contains the complete revised narration for the original image order. Cue lines and headings are not spoken. Every paragraph is spoken. All times are editorial targets; no new 35-minute audio has yet been recorded or timing-verified. The original script, map, images and audit ledger are preserved.']
    for index, text in enumerate(paragraphs):
        number = index + 1
        start, end = index * 30, (index + 1) * 30
        first, last = index * 15 + 1, (index + 1) * 15
        chapter = next(item for item in CHAPTERS if item[0] <= number <= item[1])
        if number == chapter[0]:
            markdown.append(f'## Chapter {chapter[2]} — {chapter[3]}')
        cue = f'[{clock(start)}–{clock(end)} | VAL-EP001-IMG{first:04d}–IMG{last:04d}]'
        assert cue == baseline[index][0], (number, cue, baseline[index][0])
        markdown.extend([cue, text])
        block = {'block': f'B{number:03d}', 'chapter': chapter[2], 'start_seconds': start,
                 'end_seconds': end, 'duration_seconds': 30, 'first_scene': first,
                 'last_scene': last, 'spoken_words': words(text),
                 'required_wpm_if_30_seconds': round(words(text) * 2, 2),
                 'target_speech_seconds': 29, 'planned_boundary_breath_seconds': 1,
                 'required_wpm_if_29_seconds': round(words(text) * 60 / 29, 2),
                 'audio_status': 'NOT_RECORDED', 'measured_speech_seconds': None,
                 'new_line_to_image_alignment': 'PENDING_LISTENING_AND_CONFORM',
                 'text': text}
        blocks.append(block)
        for n in range(first, last + 1):
            scene = shots[n - 1]
            scene_id = f'VAL-EP001-IMG{n:04d}'
            assert scene['scene_id'] == scene_id
            assert scene['timestamp'] == f'{clock((n - 1) * 2)}–{clock(n * 2)}'
            old = by_id[scene_id]
            candidate = old.get('selected_local_file') or ''
            candidate_rows.append({'scene_id': scene_id, 'block': block['block'],
                                   'start_seconds': (n - 1) * 2, 'end_seconds': n * 2,
                                   'duration_seconds': 2, 'chapter': scene['chapter'],
                                   'candidate_path_from_ledger': candidate,
                                   'candidate_locally_present': bool(candidate and (ROOT / candidate).is_file()),
                                   'inherited_candidate_status': old.get('audit_status'),
                                   'inherited_original_narration_slice_NOT_new_alignment': scene['narration_slice'],
                                   'original_visual_beat': scene['visual_beat'],
                                   'prior_editorial_action': old.get('editorial_action', ''),
                                   'new_narration_alignment': 'REVIEW_REQUIRED',
                                   'new_exact_spoken_slice': '',
                                   'final_accepted': False})
    assert [r['scene_id'] for r in candidate_rows] == [s['scene_id'] for s in shots]
    assert len(set(r['scene_id'] for r in candidate_rows)) == 1050
    assert candidate_rows[0]['start_seconds'] == 0
    assert candidate_rows[-1]['end_seconds'] == 2100
    assert sum(r['duration_seconds'] for r in candidate_rows) == 2100
    assert sum(r['duration_seconds'] for r in blocks) == 2100
    assert all(a['end_seconds'] == b['start_seconds'] for a, b in zip(candidate_rows, candidate_rows[1:]))
    total_words = sum(r['spoken_words'] for r in blocks)
    assert 4550 <= total_words <= 5075
    (OUTPUT / '01_COMPLETE_NARRATION_35MIN_v02.md').write_text('\n\n'.join(markdown) + '\n')
    (OUTPUT / '02_RECORDING_SCRIPT_35MIN_v02.txt').write_text('\n\n'.join(paragraphs) + '\n')
    (OUTPUT / '03_BLOCK_TIMING_PLAN.json').write_text(json.dumps({'target_duration_seconds': 2100,
        'image_count': 1050, 'spoken_words': total_words, 'voice_id_candidate': 'voice-01',
        'audio_timing_verified': False, 'blocks': blocks}, indent=2) + '\n')
    dump_csv(OUTPUT / '03_BLOCK_TIMING_PLAN.csv', [{k: v for k, v in row.items() if k != 'text'} for row in blocks])
    dump_csv(OUTPUT / '04_IMAGE_CANDIDATE_CONFORM_1050.csv', candidate_rows)
    after = {str(p.relative_to(ROOT)): sha(p) for p in protected}
    assert before == after
    report = {'status': 'TEXT_AND_SLOT_STRUCTURE_VALIDATED_NOT_RECORDED',
              'chapter_count': len(CHAPTERS), 'narration_block_count': len(blocks),
              'image_slots': len(candidate_rows), 'total_slot_seconds': 2100,
              'spoken_words': total_words, 'minimum_block_words': min(map(words, paragraphs)),
              'maximum_block_words': max(map(words, paragraphs)),
              'average_wpm_over_35min': round(total_words / 35, 2),
              'new_audio_duration_seconds': None,
              'locally_present_candidate_paths': sum(r['candidate_locally_present'] for r in candidate_rows),
              'candidate_paths_requiring_recovery': sum(not r['candidate_locally_present'] for r in candidate_rows),
              'original_reviews_inherited': ledger['reviewed_individually'],
              'final_approved_images': sum(bool(r['final_accepted']) for r in ledger['shots']),
              'baseline_hashes_before': before, 'baseline_hashes_after': after,
              'passed': ['70 original half-minute cue ranges retained verbatim',
                         '1050 IDs in original order with no duplicate or omitted slots',
                         'each image has2seconds; each block has15 images and30seconds',
                         'gapless slot coverage00:00–35:00',
                         'full spoken word count within preserved4550–5075 baseline target',
                         'protected source/scene-map/ledger hashes unchanged'],
              'not_certified': ['audio performance length/pace/pronunciation',
                                'new exact word-to-image synchronization',
                                'new candidate visual suitability or full asset availability',
                                'independent book-level lore/source verification',
                                'music/sound mix, composition or rendered film']}
    (OUTPUT / '06_VALIDATION_REPORT.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k not in ('passed', 'not_certified', 'baseline_hashes_before', 'baseline_hashes_after')}, indent=2))


if __name__ == '__main__':
    main()
