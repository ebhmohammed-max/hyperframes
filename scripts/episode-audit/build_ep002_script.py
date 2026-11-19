"""Regenerate every Episode 02 derived artefact from the single narration source.

Reads 01_COMPLETE_NARRATION_35MIN_v02.md through ep002_blocks.parse and writes the
recording script, the timing plan (CSV + JSON) and the block JSON. Also re-runs the
similarity sweep, because scripted block surgery has silently duplicated blocks five
times on this project and word counts alone do not catch it.
"""
import csv
import difflib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ep002_blocks as E

ROOT = Path(__file__).resolve().parents[2]
FILM = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep002_harpy_and_dragon/story_film_35min'
SOURCE = FILM / '01_COMPLETE_NARRATION_35MIN_v02.md'
WPM = 146.4          # measured from Ep01's 70 take01 files
SLOT = 30
SLOTS = 2

CHAPTER_MAP = {1: 'I', 11: 'II', 21: 'III', 31: 'IV', 42: 'V', 52: 'VI', 62: 'VII'}


def duplicates(blocks, threshold=0.55, window=160):
    out = []
    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            a = blocks[i]['text'][:window]
            b = blocks[j]['text'][:window]
            ratio = difflib.SequenceMatcher(None, a, b).ratio()
            if ratio >= threshold:
                out.append((blocks[i]['n'], blocks[j]['n'], round(ratio, 3)))
    return out


def main():
    blocks = E.parse(SOURCE)
    found = E.chapters(SOURCE)
    assert len(found) == 7, f'expected 7 chapters, found {len(found)}'
    for chapter in found:
        assert CHAPTER_MAP[chapter['block']] == chapter['title'].split()[1].rstrip('.'), chapter

    total_words = sum(b['words'] for b in blocks)
    est = round(total_words / WPM * 60)

    recording = ['THE HARPY AND THE DRAGON — Episode 02 of The Long Night',
                 'Recording script v02. Speak only the numbered paragraphs.',
                 '70 blocks of 30 seconds. Do not read the headings or the bracketed cues.', '']
    for chapter in found:
        recording.append(f'--- {chapter["title"]} ---')
        recording.append('')
        for block in blocks:
            if block['n'] < chapter['block']:
                continue
            nxt = next((c['block'] for c in found if c['block'] > chapter['block']), 71)
            if block['n'] >= nxt:
                continue
            recording.append(f'[BLOCK {block["n"]:02d} | {block["start"]}–{block["end"]}]')
            recording.append(block['text'])
            recording.append('')
    (FILM / '02_RECORDING_SCRIPT_35MIN_v02.txt').write_text('\n'.join(recording), encoding='utf-8')

    with (FILM / '03_BLOCK_TIMING_PLAN_v02.csv').open('w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(['block', 'start', 'end', 'seconds', 'words',
                         'est_seconds_at_146_4_wpm', 'img_from', 'img_to', 'chapter'])
        for block in blocks:
            chapter = [CHAPTER_MAP[c['block']] for c in found if c['block'] <= block['n']][-1]
            writer.writerow([block['n'], block['start'], block['end'], SLOT, block['words'],
                             round(block['words'] / WPM * 60, 1), block['img_from'],
                             block['img_to'], chapter])

    payload = {
        'episode': 'HAR-EP002', 'title': 'The Harpy and the Dragon',
        'channel': 'The Long Night', 'version': 'v02 story-led',
        'source': str(SOURCE.relative_to(ROOT)),
        'measured_wpm_source': 'Ep01 take01 mean 146.4 wpm',
        'planned_wpm': WPM,
        'blocks': blocks,
        'chapters': found,
        'total_words': total_words,
        'words_per_block': {'min': min(b['words'] for b in blocks),
                            'max': max(b['words'] for b in blocks),
                            'mean': round(total_words / len(blocks), 1)},
        'estimated_speech_seconds': est,
        'film_seconds': 2100,
        'headroom_seconds': 2100 - est,
        'image_slots': 1050, 'seconds_per_slot': SLOTS,
        'duplicate_pairs': duplicates(blocks),
    }
    assert not payload['duplicate_pairs'], payload['duplicate_pairs']
    (FILM / 'narration_blocks_v02.json').write_text(
        json.dumps(payload, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')

    print(json.dumps({k: v for k, v in payload.items() if k not in ('blocks', 'chapters')}, indent=1))
    print('chapters:', [(c['block'], c['title']) for c in found])


if __name__ == '__main__':
    main()
