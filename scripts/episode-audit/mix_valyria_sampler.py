#!/usr/bin/env python3
"""Mix eight90-second sampler chapters without changing the original soundtrack."""
import hashlib
import json
import os
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'projects/valyria_style_sampler'
E=ROOT/'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria'
FF=os.environ.get('FFMPEG','ffmpeg')
WORK=ROOT/'.cache/valyria-sampler-audio';WORK.mkdir(parents=True,exist_ok=True)
M=json.loads((P/'production/SAMPLER_MANIFEST.json').read_text())
A=E/'documentary_film/assets/audio/licensed'
tracks=['night-vigil.mp3','mana-two-part-1.mp3','ancient-rite.mp3','ancient-winds-part-1.mp3','ancient-rite.mp3','ancient-winds-part-1.mp3','night-vigil.mp3','night-vigil.mp3']

def run(args):
 subprocess.run([FF,'-hide_banner','-nostdin','-y','-loglevel','warning',*args],check=True)

for c,track in zip(M['chapters'],tracks):
 n=c['number'];out=WORK/f'chapter-{n:02}.wav'
 inputs=['-i',str(P/c['intro_asset']),'-ss',str(c['source_narration_start']),'-t','60','-i',str(E/'documentary_film/assets/audio/narration.mp3'),'-i',str(A/track),'-i',str(A/('bookFlip1.ogg' if n in [2,3] else 'cloth1.ogg'))]
 graph=';'.join(['[0:a]aresample=48000,aformat=channel_layouts=stereo,adelay=1000:all=1[intro]',
 '[1:a]aresample=48000,aformat=channel_layouts=stereo,adelay=22000:all=1[excerpt]',
 '[intro][excerpt]amix=inputs=2:normalize=0,apad,atrim=duration=90,asplit=2[voice][key]',
 '[2:a]atrim=duration=90,highpass=f=85,loudnorm=I=-30:TP=-6:LRA=9,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=3,afade=t=out:st=85:d=5[music]',
 '[music][key]sidechaincompress=threshold=0.02:ratio=4:attack=30:release=700[ducked]',
 '[3:a]aresample=48000,aformat=channel_layouts=stereo,volume=0.12,adelay=22000:all=1[sfx]',
 '[voice][ducked][sfx]amix=inputs=3:normalize=0,apad,atrim=duration=90[out]'])
 run([*inputs,'-filter_complex',graph,'-map','[out]','-ar','48000','-ac','2',str(out)])
 print('Mixed chapter',n,flush=True)
listing=WORK/'concat.txt';listing.write_text(''.join(f"file '{WORK/f'chapter-{n:02}.wav'}'\n" for n in range(1,9)))
pre=WORK/'premix.wav';run(['-f','concat','-safe','0','-i',str(listing),'-c:a','copy',str(pre)])
r=subprocess.run([FF,'-hide_banner','-nostdin','-i',str(pre),'-af','loudnorm=I=-16:TP=-1.5:LRA=9:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
measure,_=json.JSONDecoder().raw_decode(r.stderr[r.stderr.rfind('{'):])
norm='loudnorm=I=-16:TP=-1.5:LRA=9:linear=true:'+':'.join(f'{key}={measure[val]}' for key,val in [('measured_I','input_i'),('measured_TP','input_tp'),('measured_LRA','input_lra'),('measured_thresh','input_thresh'),('offset','target_offset')])
out=P/'assets/audio/soundtrack.m4a';run(['-i',str(pre),'-af',norm,'-ar','48000','-ac','2','-t','720','-c:a','aac','-b:a','160k',str(out)])
(P/'production/SOUND_MIX.json').write_text(json.dumps({'duration':720,'intro_placement':1,'source_excerpt_placement':22,'music':tracks,'premix_measurements':measure,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'bytes':out.stat().st_size,'listening_approval':'PENDING'},indent=2)+'\n')
print('Sampler soundtrack complete',flush=True)
