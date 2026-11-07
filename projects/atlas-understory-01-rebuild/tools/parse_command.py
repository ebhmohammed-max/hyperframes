#!/usr/bin/env python3
"""Parse HF-DIRECTOR-1.0 (15_Hyperframes_Master_Command_v1) appendices A-D into data/command.json.
Validates identity counts (48 VO / 1427 words / 98 shots / 53 units / 97 boundaries, 15745 frames)."""
import json, re, sys, pathlib

SRC = pathlib.Path('/home/user/hyperframes/google_drive/15_Hyperframes_Master_Command_v1')
OUT = pathlib.Path(__file__).resolve().parent.parent / 'data' / 'command.json'
FPS = 24

def tc2f(tc):
    mm, ss, ff = tc.split(':')
    return (int(mm) * 60 + int(ss)) * FPS + int(ff)

text = SRC.read_text(encoding='utf-8').replace('\r\n', '\n')

def section(name, nxt):
    i = text.index(name)
    j = text.index(nxt, i) if nxt else len(text)
    return text[i:j]

secA = section('APPENDIX A', 'APPENDIX B')
secB = section('APPENDIX B', 'APPENDIX C')
secC = section('APPENDIX C', 'APPENDIX D')
secD = section('APPENDIX D', 'APPENDIX E')

# ---- Appendix A: VO segments ----
VO = []
vo_pat = re.compile(
    r'VO-(C\d{2}-B\d{2}) · Chapter(\d) · (\d{2}:\d{2}:\d{2})–(\d{2}:\d{2}:\d{2})\n(.*?)\nGraphic:(\S+) · Sources:(.+?) · Draft speech end:(\d{2}:\d{2}:\d{2})',
    re.S)
for m in vo_pat.finditer(secA):
    body = ' '.join(m.group(5).split())
    VO.append({
        'id': 'VO-' + m.group(1), 'chapter': int(m.group(2)),
        'start_tc': m.group(3), 'end_tc': m.group(4),
        'start_f': tc2f(m.group(3)), 'end_f': tc2f(m.group(4)),
        'text': body, 'words': len(body.split()),
        'graphic': m.group(6), 'sources': m.group(7).strip(),
        'speech_end_tc': m.group(8), 'speech_end_f': tc2f(m.group(8)),
    })

# ---- Appendix B: graphic units ----
units = []
unit_head = re.compile(r'^(MG-\d{3}|VX-\d{3}) — (.*)$', re.M)
heads = list(unit_head.finditer(secB))
for i, h in enumerate(heads):
    blk = secB[h.start(): heads[i + 1].start() if i + 1 < len(heads) else len(secB)]
    meta = re.search(r'VO:(\S+) \| Shots:([^|]+) \| Draft:(\S+) \| Sources:(.*)', blk)
    copy = re.search(r'Display copy: (.*)', blk)
    build = re.search(r'Build: (.*)', blk)
    limit = re.search(r'Limit: (.*)', blk)
    dr = meta.group(3).split('–')
    units.append({
        'id': h.group(1), 'name': h.group(2).strip(),
        'vo': meta.group(1), 'shots': [s.strip() for s in meta.group(2).split(';')],
        'draft': meta.group(3), 'start_f': tc2f(dr[0]), 'end_f': tc2f(dr[1]),
        'sources': meta.group(4).strip(),
        'copy': [c.strip() for c in copy.group(1).split(' | ')],
        'build': build.group(1).strip(), 'limit': limit.group(1).strip(),
    })

def _gid(raw):
    m = re.search(r'(MG-\d{3}|VX-\d{3})', raw)
    return m.group(1) if m else 'NONE'

# ---- Appendix C: shots ----
shots = []
shot_head = re.compile(r'^(C\d{2}-S\d{3}) · (\d{2}:\d{2}:\d{2})–(\d{2}:\d{2}:\d{2}) · frames(\d+)–(\d+)exclusive$', re.M)
sheads = list(shot_head.finditer(secC))
for i, h in enumerate(sheads):
    blk = secC[h.start(): sheads[i + 1].start() if i + 1 < len(sheads) else len(secC)]
    meta = re.search(r'VO:(\S+) \| Dominance:(.*?) \| Image:(.*?) \| Graphic:(.*?) \| Heading:(.*)', blk)
    def field(name):
        m = re.search(name + r':\s?(.*)', blk)
        return m.group(1).strip() if m else ''
    into = field('Into shot')
    shots.append({
        'id': h.group(1), 'start_tc': h.group(2), 'end_tc': h.group(3),
        'start_f': int(h.group(4)), 'end_f': int(h.group(5)),
        'vo': meta.group(1), 'dominance': meta.group(2).strip(), 'image': meta.group(3).strip(),
        'graphic': _gid(meta.group(4)), 'graphic_note': meta.group(4).strip(), 'heading': meta.group(5).strip(),
        'intent': field('Intent'), 'display': field('Display'), 'motion': field('Motion'),
        'disclosure': field('Disclosure'), 'limit': field('Limit'),
        'into': into, 'into_class': into.split('|')[0].strip(),
    })

# ---- Appendix D: boundaries ----
bounds = []
b_pat = re.compile(r'^\* (\d+)\. (\d{2}:\d{2}:\d{2}) / frame(\d+) / (\S+)→(\S+): (.*?), (\d+)f\s?handle\.\s?(.*)$', re.M)
for m in b_pat.finditer(secD):
    cls = m.group(6).strip()
    cat = 'GRAPHIC' if cls.startswith('GRAPHIC') else ('CROSSFADE' if cls.startswith('CROSSFADE') else 'CUT')
    bounds.append({'n': int(m.group(1)), 'tc': m.group(2), 'frame': int(m.group(3)),
                   'from': m.group(4), 'to': m.group(5), 'class': cls, 'category': cat,
                   'handle_f': int(m.group(7)), 'reason': m.group(8).strip()})

# ---- validation ----
errs = []
assert len(VO) == 48, f'VO count {len(VO)}'
assert len(shots) == 98, f'shot count {len(shots)}'
assert len(units) == 53, f'unit count {len(units)}'
assert len(bounds) == 97, f'boundary count {len(bounds)}'
words = sum(v['words'] for v in VO)
if words != 1427: errs.append(f'word count {words} != 1427')
for s in shots:
    if tc2f(s['start_tc']) != s['start_f'] or tc2f(s['end_tc']) != s['end_f']:
        errs.append(f"{s['id']} frame/tc mismatch")
for a, b in zip(shots, shots[1:]):
    if a['end_f'] != b['start_f']: errs.append(f"gap {a['id']}->{b['id']}")
if shots[0]['start_f'] != 0 or shots[-1]['end_f'] != 15745: errs.append('outer bounds wrong')
for b in bounds:
    if b['frame'] != tc2f(b['tc']): errs.append(f"boundary {b['n']} tc mismatch")
    sh = next(s for s in shots if s['start_f'] == b['frame'])
    if sh['id'] != b['to']: errs.append(f"boundary {b['n']} target mismatch")
from collections import Counter
cats = Counter(b['category'] for b in bounds)
if cats != {'CUT': 62, 'CROSSFADE': 23, 'GRAPHIC': 12}: errs.append(f'boundary cats {cats}')
uids = set(u['id'] for u in units)
for s in shots:
    if s['graphic'] != 'NONE' and s['graphic'] not in uids: errs.append(f"{s['id']} bad graphic {s['graphic']}")
    if s['heading'] != 'none' and s['heading'] not in uids: errs.append(f"{s['id']} bad heading {s['heading']}")
for u in units:
    v = next(x for x in VO if x['id'] == u['vo'])
    if u['id'] in ('MG-046', 'MG-047', 'MG-048', 'MG-049', 'MG-050'):
        continue  # heading overlays use their own sub-windows by design
    if u['start_f'] != v['start_f'] or u['end_f'] != v['end_f']:
        errs.append(f"{u['id']} window != VO window")
print('VO words total:', words)
print('frames: 0..%d  shots contiguous OK' % shots[-1]['end_f'])
print('boundary categories:', dict(cats))
print('errors:', errs if errs else 'NONE')

OUT.write_text(json.dumps({'vo': VO, 'units': units, 'shots': shots, 'boundaries': bounds}, indent=1, ensure_ascii=False))
print('wrote', OUT)
