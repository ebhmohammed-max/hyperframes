#!/usr/bin/env python3
"""Build the fixed 2100-second narration-first mix from registered licensed assets.
Requires ffmpeg/ffprobe on PATH (or FFMPEG/FFPROBE env overrides).
This is a technical mix, not a claim of subjective listening approval.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/documentary_film'
WORK = ROOT / '.cache/documentary-sound'
FF = os.environ.get('FFMPEG', 'ffmpeg')
WORK.mkdir(parents=True, exist_ok=True)
A = D / 'assets/audio/licensed'
# Deliberate breathing spaces; no music cue is longer than its source recording.
CUES = [
    (0, 200, 'night-vigil.mp3'), (212, 88, 'ancient-winds-part-1.mp3'),
    (304, 210, 'ancient-winds-part-1.mp3'), (524, 70, 'mana-two-part-1.mp3'),
    (602, 108, 'ancient-rite.mp3'), (720, 174, 'ancient-winds-part-1.mp3'),
    (902, 108, 'ancient-rite.mp3'), (1020, 204, 'night-vigil.mp3'),
    (1234, 190, 'ancient-winds-part-1.mp3'), (1434, 90, 'ancient-rite.mp3'),
    (1534, 200, 'night-vigil.mp3'), (1744, 80, 'ancient-winds-part-1.mp3'),
    (1834, 108, 'ancient-rite.mp3'), (1952, 148, 'night-vigil.mp3'),
]
# Restrained chapter punctuation only, not purported scene-synchronous foley.
SFX = [(30.2, 'bookOpen.ogg', 0.12), (300.4, 'cloth1.ogg', 0.12),
       (600.4, 'cloth1.ogg', 0.12), (900.4, 'bookFlip1.ogg', 0.10),
       (1230.4, 'cloth1.ogg', 0.12), (1530.4, 'bookFlip1.ogg', 0.10),
       (1830.4, 'cloth1.ogg', 0.12)]

def run(args):
    subprocess.run([FF, '-hide_banner', '-nostdin', '-y', '-loglevel', 'warning', *args], check=True)

# Normalize each musical cue before placement; seven-second boundary fades.
inputs = []
for i, (start, duration, name) in enumerate(CUES):
    dest = WORK / f'cue-{i:02}.wav'
    run(['-i', str(A / name), '-t', str(duration), '-af',
         f'highpass=f=85,lowpass=f=10000,loudnorm=I=-30:TP=-6:LRA=9,aresample=48000,afade=t=in:d=5,afade=t=out:st={duration-7}:d=7',
         '-ar', '48000', '-ac', '2', str(dest)])
    inputs += ['-i', str(dest)]
filters = []
for i, (start, duration, name) in enumerate(CUES):
    filters.append(f'[{i}:a]adelay={round(start*1000)}:all=1[m{i}]')
filters.append(''.join(f'[m{i}]' for i in range(len(CUES))) + f'amix=inputs={len(CUES)}:normalize=0,apad,atrim=duration=2100[music]')
run([*inputs, '-filter_complex', ';'.join(filters), '-map', '[music]', '-ar', '48000', '-ac', '2', str(WORK / 'score.wav')])
inputs = ['-i', str(D / 'assets/audio/narration.mp3'), '-i', str(WORK / 'score.wav')]
filters = ['[0:a]aresample=48000,aformat=channel_layouts=stereo,asplit=2[voice][key]',
           '[1:a][key]sidechaincompress=threshold=0.02:ratio=4:attack=30:release=700:makeup=1[ducked]']
for i, (start, name, gain) in enumerate(SFX, 2):
    inputs += ['-i', str(A / name)]
    filters.append(f'[{i}:a]aresample=48000,aformat=channel_layouts=stereo,volume={gain},adelay={round(start*1000)}:all=1[s{i}]')
labels = '[voice][ducked]' + ''.join(f'[s{i}]' for i in range(2, 2+len(SFX)))
filters.append(labels + f'amix=inputs={2+len(SFX)}:normalize=0,apad,atrim=duration=2100[mix]')
premix = WORK / 'premix.wav'
run([*inputs, '-filter_complex', ';'.join(filters), '-map', '[mix]', '-ar', '48000', '-ac', '2', str(premix)])
# Two-pass integrated loudness normalization.
r = subprocess.run([FF, '-hide_banner', '-nostdin', '-i', str(premix), '-af',
                    'loudnorm=I=-16:TP=-1.5:LRA=9:print_format=json', '-f', 'null', '-'], capture_output=True, text=True, check=True)
measure, _ = json.JSONDecoder().raw_decode(r.stderr[r.stderr.rfind('{'):])
normalizer = ('loudnorm=I=-16:TP=-1.5:LRA=9:linear=true:' +
              ':'.join(f'{key}={measure[val]}' for key, val in [('measured_I','input_i'),('measured_TP','input_tp'),('measured_LRA','input_lra'),('measured_thresh','input_thresh'),('offset','target_offset')]))
output = D / 'assets/audio/final-mix.mp3'
run(['-i', str(premix), '-af', normalizer, '-ar', '48000', '-ac', '2', '-t', '2100', '-c:a', 'libmp3lame', '-b:a', '192k', str(output)])
report = {'duration_seconds': 2100, 'target_lufs': -16, 'target_true_peak_db': -1.5,
          'music_cues': [{'start': s, 'duration': d, 'asset': n} for s,d,n in CUES],
          'sfx_cues': [{'start':s,'asset':n,'gain':g} for s,n,g in SFX],
          'premix_measurements':measure, 'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),
          'output_bytes':output.stat().st_size, 'listening_approval':'PENDING',
          'note':'No narration timing, word order or picture duration changed. Does not establish image alignment or publication readiness.'}
(D / 'production/SOUND_MIX_REPORT.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
