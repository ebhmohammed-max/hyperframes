#!/usr/bin/env python3
"""Build SRT/VTT sidecars from verified actual-audio phrase cues (text checked == Appendix A verbatim)."""
import json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
old = json.loads((ROOT.parent / 'atlas-understory-01' / 'data' / 'captions.json').read_text())
cmd = json.loads((ROOT / 'data' / 'command.json').read_text())
VO = {v['id']: v for v in cmd['vo']}

def norm(t):
    return re.sub(r'\s+', ' ', t.replace('’', "'")).strip().lower()

from collections import defaultdict
byseg = defaultdict(list)
for c in old['cues']:
    byseg[c['segment']].append(c)
for vid, v in VO.items():
    joined = ' '.join(c['text'] for c in byseg[vid])
    assert norm(joined) == norm(v['text']), f'text mismatch {vid}'

def wrap(text, width=36):
    words = text.split()
    lines, cur = [], ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur); cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur: lines.append(cur)
    if len(lines) <= 2: return lines
    # rebalance into 2 lines
    total = len(text); best, acc = None, 0
    for i, w in enumerate(words[:-1]):
        acc += len(w) + 1
        if best is None or abs(2 * acc - total) < best[0]: best = (abs(2 * acc - total), i)
    i = best[1]
    return [' '.join(words[:i + 1]), ' '.join(words[i + 1:])]

def ts(s, vtt=False):
    ms = round(s * 1000)
    h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); sec, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{sec:02d}' + ('.' if vtt else ',') + f'{ms:03d}'

cues = old['cues']
srt, vtt = [], ['WEBVTT', '']
maxcps = 0; maxline = 0
for i, c in enumerate(cues, 1):
    lines = wrap(c['text'])
    assert len(lines) <= 2, c['text']
    maxline = max(maxline, *(len(l) for l in lines))
    maxcps = max(maxcps, len(c['text']) / max(c['out_s'] - c['start_s'], 0.01))
    srt.append(f"{i}\n{ts(c['start_s'])} --> {ts(c['out_s'])}\n" + '\n'.join(lines) + '\n')
    vtt.append(f"{ts(c['start_s'], True)} --> {ts(c['out_s'], True)}\n" + '\n'.join(lines) + '\n')

(ROOT / 'HF03_Atlas_Understory_01_captions.srt').write_text('\n'.join(srt), encoding='utf-8')
(ROOT / 'HF03_Atlas_Understory_01_captions.vtt').write_text('\n'.join(vtt), encoding='utf-8')
print(f'cues: {len(cues)}  max CPS: {maxcps:.1f}  max line chars: {maxline}  span: {cues[0]["start_s"]:.2f}..{cues[-1]["out_s"]:.2f}s')
print('text check: all 48 segments identical to Appendix A (normalized)')
