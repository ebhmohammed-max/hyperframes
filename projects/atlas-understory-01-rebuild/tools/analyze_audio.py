#!/usr/bin/env python3
"""Speech-activity analysis of master audio (16k mono WAV): RMS blocks vs Draft VO boundaries."""
import wave, struct, json, sys, pathlib

WAV = '/tmp/master16k.wav'
FPS = 24
w = wave.open(WAV)
n = w.getnframes()
raw = w.readframes(n)
import array
a = array.array('h'); a.frombytes(raw)
sr = w.getframerate()
WIN = int(sr * 0.05)  # 50ms
nw = n // WIN
rms = []
for i in range(nw):
    seg = a[i * WIN:(i + 1) * WIN]
    s = sum(x * x for x in seg) / len(seg)
    rms.append(s ** 0.5)
import math
db = [20 * math.log10(r / 32768.0) if r > 0 else -120.0 for r in rms]

def blocks(threshold_db, min_gap_s=0.7, min_dur_s=1.2):
    act = [d > threshold_db for d in db]
    out = []
    i = 0
    gap_w = int(min_gap_s / 0.05)
    while i < len(act):
        if act[i]:
            j = i
            last = i
            while j < len(act):
                if act[j]: last = j
                elif j - last > gap_w: break
                j += 1
            dur = (last - i) * 0.05
            if dur >= min_dur_s: out.append((i * 0.05, (last + 1) * 0.05))
            i = j
        else:
            i += 1
    return out

for th in (-34, -30, -26):
    b = blocks(th)
    print(f'threshold {th} dB -> {len(b)} speech blocks')
    if th == -30:
        for k, (s, e) in enumerate(b):
            print(f'  blk{k+1:02d} {s:7.2f} .. {e:7.2f}  ({e-s:5.1f}s)')

d = json.loads(open(pathlib.Path(__file__).parent.parent / 'data' / 'command.json').read())
print('\nDraft VO windows vs nearest speech-block starts (threshold -30):')
b = blocks(-30)
starts = [s for s, e in b]
for v in d['vo']:
    ds = v['start_f'] / FPS
    near = min(starts, key=lambda x: abs(x - ds)) if starts else None
    print(f"  {v['id']} draft_start {ds:7.2f}  nearest block start {near:7.2f}  delta {near-ds:+6.2f}s" if near is not None else v['id'])
