"""Single parser for the Episode 02 narration script.

Every derived artefact (recording script, timing plan, block JSON, pilot) must read
blocks through this module. An earlier inline regex greedily swallowed the
`## Chapter` heading into the preceding block, which put a stage direction into the
recording script. The lookahead here stops at headings, horizontal rules and the
next cue, so prose can never capture document structure.
"""
import re
from pathlib import Path

CUE = re.compile(
    r'^\[(\d\d:\d\d)–(\d\d:\d\d) \| HAR-EP002-IMG(\d+)–IMG(\d+)\]\n\n(.+?)(?=\n\n\[|\n\n##|\n\n---|\Z)',
    re.S | re.M,
)
HEADING = re.compile(r'^## (.+)$', re.M)


def parse(path):
    path = Path(path)
    text = path.read_text(encoding='utf-8')
    blocks = []
    for match in CUE.finditer(text):
        body = ' '.join(match.group(5).split())
        if not body:
            raise ValueError(f'empty narration block at {match.group(1)}')
        if body.lstrip().startswith('#'):
            raise ValueError(f'heading leaked into block at {match.group(1)}')
        blocks.append({
            'n': len(blocks) + 1,
            'start': match.group(1),
            'end': match.group(2),
            'img_from': int(match.group(3)),
            'img_to': int(match.group(4)),
            'text': body,
            'words': len(body.split()),
        })
    validate(blocks)
    return blocks


def chapters(path):
    """Chapter titles paired with the block number they open, in document order."""
    text = Path(path).read_text(encoding='utf-8')
    out = []
    for heading in HEADING.finditer(text):
        title = heading.group(1).strip()
        if not title.lower().startswith('chapter'):
            continue
        following = CUE.search(text, heading.end())
        if following:
            plan_minute = (len(CUE.findall(text[:following.start()])))
            out.append({'title': title, 'block': plan_minute + 1, 'start': following.group(1)})
    return out


def validate(blocks):
    assert len(blocks) == 70, f'expected 70 blocks, found {len(blocks)}'
    for i, block in enumerate(blocks, 1):
        assert block['n'] == i
        minute, second = divmod((i - 1) * 30, 60)
        assert block['start'] == f'{minute:02d}:{second:02d}', f'block {i} cue {block["start"]}'
        assert block['img_from'] == 1 + (i - 1) * 15, f'block {i} first slot'
        assert block['img_to'] == i * 15, f'block {i} last slot'
        assert 55 <= block['words'] <= 74, f'block {i} is {block["words"]} words'
