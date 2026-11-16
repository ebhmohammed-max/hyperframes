"""Build editable HyperFrames documentary and auditable source-recovery manifest.

Never substitutes a different image for an unavailable candidate. Review slates
are intentional, and prevent this assembly being mistaken for a final film.
"""
import csv
import hashlib
import html
import io
import json
import shutil
import zipfile
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria'
F = EP / 'documentary_film'
CHAPTERS = [
    (1, 0, 300, 'Before the dragonlords', 'The question', 'pastoral', '#cbbda2'),
    (2, 300, 300, 'A world beneath fire', 'The peninsula', 'landscape', '#c99365'),
    (3, 600, 300, 'In the shadow of wings', 'The discovery', 'revelation', '#b9c7ce'),
    (4, 900, 330, 'The struggle for the sky', 'The binding', 'tension', '#bb805a'),
    (5, 1230, 300, 'Blood and the Freehold', 'The ruling houses', 'dynasty', '#d0b47b'),
    (6, 1530, 300, 'The price of greatness', 'Stone / steel / servitude', 'reckoning', '#b5aaa0'),
    (7, 1830, 270, 'The harpy and the dragon', 'The coming wars', 'confrontation', '#c4a679'),
]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    F.mkdir(parents=True, exist_ok=True)
    for folder in ['assets/images', 'assets/vendor', 'assets/audio', 'compositions', 'production']:
        (F / folder).mkdir(parents=True, exist_ok=True)
    ledger = json.loads((EP / 'audit/EP001_SHOT_AUDIT_LEDGER.json').read_text())
    observations = {row['scene_id']: row for row in ledger['shots']}
    source_rows = list(csv.DictReader((EP / 'story_film_35min/04_IMAGE_CANDIDATE_CONFORM_1050.csv').open()))
    assert len(source_rows) == 1050
    archive_members = {}
    for path in sorted((ROOT / 'google_drive').glob('*.zip')):
        with zipfile.ZipFile(path) as archive:
            for name in archive.namelist():
                if name.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                    archive_members.setdefault(Path(name).name, []).append((path, name))
    overrides_path = F / 'production/EDITORIAL_OVERRIDES.json'
    overrides = json.loads(overrides_path.read_text()) if overrides_path.exists() else {}
    shots = []
    for i, source in enumerate(source_rows):
        candidate = source['candidate_path_from_ledger']
        path = ROOT / candidate
        origin, data = None, None
        override = overrides.get(f'{i + 1:04d}')
        if override:
            correction = F / override['asset']
            data = correction.read_bytes()
            origin = {'type': 'ai_generated_editorial_correction', 'path': str(correction.relative_to(ROOT)),
                      'replaces_candidate': candidate, 'reason': override['reason'],
                      'visual_observation': override['observation']}
        elif path.is_file():
            data = path.read_bytes()
            origin = {'type': 'local_selected_candidate', 'path': candidate}
        elif Path(candidate).name in archive_members:
            matches = archive_members[Path(candidate).name]
            # All same-name archive copies must be identical; do not guess between revisions.
            variants = []
            for archive_path, member in matches:
                with zipfile.ZipFile(archive_path) as archive:
                    raw = archive.read(member)
                variants.append((sha(raw), raw, archive_path, member))
            hashes = {v[0] for v in variants}
            if len(hashes) == 1:
                _, data, archive_path, member = variants[0]
                origin = {'type': 'exact_basename_archive_recovery',
                          'archive': str(archive_path.relative_to(ROOT)), 'member': member}
        local = None
        dimensions = None
        if data is not None:
            with Image.open(io.BytesIO(data)) as im:
                im.load()
                dimensions = list(im.size)
                proxy = ImageOps.exif_transpose(im).convert('RGB')
                proxy.thumbnail((1376, 920), Image.Resampling.LANCZOS)
                local = f'assets/images/{i + 1:04d}.jpg'
                proxy.save(F / local, quality=79, optimize=True)
        chapter = next(c for c in CHAPTERS if c[1] <= i * 2 < c[1] + c[2])
        # Lower motion for human suffering. No fake camera shake or invented parallax layers.
        palettes = {1: ['push', 'hold', 'pan-left', 'hold', 'pull'],
                    2: ['pan-left', 'push', 'pan-right', 'hold', 'pull'],
                    3: ['push', 'pull', 'push', 'pan-left', 'hold'],
                    4: ['hold', 'push', 'hold', 'pan-right', 'push'],
                    5: ['pull', 'hold', 'push', 'hold', 'pan-left'],
                    6: ['hold', 'hold', 'push', 'hold', 'pull'],
                    7: ['push', 'pan-left', 'hold', 'pan-right', 'push']}
        move = palettes[chapter[0]][i % 5]
        if chapter[0] == 6 and i >= 855:
            move = 'hold' if i % 3 else 'push'
        shots.append({'scene_id': source['scene_id'], 'index': i + 1, 'block': source['block'],
                      'chapter': chapter[0], 'start': i * 2, 'duration': 2,
                      'source_candidate': candidate, 'source_origin': origin,
                      'source_sha256': sha(data) if data else None, 'native_dimensions': dimensions,
                      'proxy': local, 'proxy_sha256': sha((F / local).read_bytes()) if local else None,
                      'motion': move, 'inherited_audit_status': source['inherited_candidate_status'],
                      'visual_beat': source['original_visual_beat'],
                      'inherited_actual_observation': observations.get(source['scene_id'], {}).get('visual_observation'),
                      'inherited_editorial_action': observations.get(source['scene_id'], {}).get('editorial_action'),
                      'word_image_alignment': 'PENDING', 'final_approved': False,
                      'availability': 'AVAILABLE_UNAPPROVED' if local else 'SOURCE_RECOVERY_PENDING'})
    shutil.copyfile(ROOT / '.cache/film-tools/node_modules/gsap/dist/gsap.min.js', F / 'assets/vendor/gsap.min.js')
    narration = F / 'assets/audio/narration.mp3'
    target = Path('../../../story_film_35min/audio/review/EP001_COMPLETE_NARRATION_35m00s_v01.mp3')
    if not narration.exists() and not narration.is_symlink():
        narration.symlink_to(target)
    assert narration.is_file(), narration.resolve()
    for name in ['whoosh-cinematic.mp3', 'impact-bass-1.mp3', 'CREDITS.md']:
        shutil.copyfile(ROOT / f'skills/media-use/audio/assets/sfx/{name}', F / f'assets/audio/{name}')
    root_hosts = []
    titles = {c[1] // 30 + 1: c for c in CHAPTERS}
    for block in range(1, 71):
        id_ = f'b{block:03d}'
        part = shots[(block - 1) * 15:block * 15]
        chapter = CHAPTERS[part[0]['chapter'] - 1]
        tags, animations = [], []
        for j, shot in enumerate(part):
            sid = f's{shot["index"]:04d}'
            start = j * 2
            if shot['proxy']:
                content = f'<img id="{sid}-image" src="{shot["proxy"]}" alt="" draggable="false">'
                # Use source aspect without losing anatomy: full plate fits in the cinema aperture.
                scale_from, scale_to, x_from, x_to = {
                    'push': (1, 1.035, 0, 0), 'pull': (1.035, 1, 0, 0),
                    'pan-left': (1.025, 1.025, 10, -10),
                    'pan-right': (1.025, 1.025, -10, 10), 'hold': (1, 1, 0, 0),
                }[shot['motion']]
                animations.append(f'tl.fromTo("#{sid}-image",{{scale:{scale_from},x:{x_from}}},{{scale:{scale_to},x:{x_to},duration:1.999,ease:"none"}},{start});')
            else:
                content = f'<div class="missing"><span>SOURCE PENDING</span><h2>{shot["index"]:04d}</h2></div>'
            tags.append(f'<div id="{sid}" class="clip plate" data-start="{start}" data-duration="2" data-track-index="1" data-track-kind="graphics" data-layout-allow-overflow="true">{content}</div>')
        if block == 1:
            tags.append('<div id="b001-disclosure" class="clip disclosure" data-start="0" data-duration="9" data-track-index="2">AI-ILLUSTRATED RECONSTRUCTION</div>')
            cards = [(20, 9.9, 'THE QUESTION', 'Who paid for their power?')]
        elif block in titles:
            c = titles[block]
            cards = [(0.4, 8, f'CHAPTER {c[0]:02d}  /  {c[4].upper()}', 'RISE OF OLD VALYRIA' if block == 2 else c[3])]
        elif block == 2:
            cards = [(0.2, 8, 'ANCIENT WORLD OF ICE AND FIRE  /  EPISODE 01', 'Rise of Old Valyria')]
        elif block == 70:
            cards = [(23, 6.99, 'AN ILLUSTRATED FAN DOCUMENTARY', 'Next: the Five Wars')]
        else:
            cards = []
        for k, (start, duration, kicker, title) in enumerate(cards):
            cid = f'{id_}-title{k}'
            tags.append(f'<div id="{cid}" class="clip title" data-start="{start}" data-duration="{duration}" data-track-index="2" data-track-kind="graphics"><div class="lockup"><span class="kicker">{html.escape(kicker)}</span><h1>{html.escape(title)}</h1></div></div>')
            # Adapted from registry/components/titlecard-calm: staggered kicker/headline, fixed envelopes.
            animations.extend([
                f'tl.fromTo("#{cid} .kicker",{{opacity:0,y:16}},{{opacity:1,y:0,duration:0.5,ease:"power2.out"}},{start});',
                f'tl.fromTo("#{cid} h1",{{opacity:0,y:24}},{{opacity:1,y:0,duration:0.72,ease:"power3.out"}},{start + .28});',
                f'tl.fromTo("#{cid} .lockup",{{opacity:1}},{{opacity:0,duration:0.55,ease:"power2.in"}},{start + duration - .55});',
            ])
        if block == 69:
            tags.append('<div id="audio-credits" class="clip" data-start="8" data-duration="22" data-track-index="3" data-track-kind="graphics" style="position:absolute;left:170px;right:170px;bottom:140px;padding:32px 40px;background:rgba(9,9,8,.94);font:30px/1.55 Arial,sans-serif;color:#f4ede1">MUSIC — Kevin MacLeod (incompetech.com)<br>Ancient Rite · Night Vigil · Mana Two - Part 1 · Ancient Winds<br>Creative Commons Attribution 4.0<br>creativecommons.org/licenses/by/4.0/<br>SOUND EFFECTS — Kenney RPG Audio · CC0 · kenney.nl<br><span style="color:#c5baaa">Music edited, excerpted and mixed. No artist endorsement.</span></div>')
        markup = '\n'.join(tags)
        script = '\n'.join(animations)
        doc = f'''<template>
<style>
#root{{position:absolute;inset:0;overflow:hidden;background:#0b0b0a;color:#f4ede1;--accent:{chapter[6]};}}
.plate{{position:absolute;inset:78px 0;overflow:hidden;display:flex;align-items:center;justify-content:center;background:#0b0b0a;}}
.plate img{{width:100%;height:100%;object-fit:contain;transform-origin:50% 50%;}}
.missing{{width:80%;padding:60px;border-left:3px solid #bd9563;background:#181713;font-family:Arial,sans-serif;}}
.missing span{{color:#d6b481;font-size:28px;letter-spacing:5px;}} .missing h2{{font-size:72px;font-weight:400;margin:22px 0;}} .missing p{{font-size:32px;line-height:1.4;color:#d2cabd;}}
.disclosure{{position:absolute;top:112px;left:192px;background:rgba(9,9,8,.92);padding:14px 20px;color:#e1c79d;font:28px Arial,sans-serif;letter-spacing:3px;}}
.title{{position:absolute;left:192px;bottom:160px;max-width:1500px;z-index:5;}}
.lockup{{padding:28px 36px 34px;background:rgba(9,9,8,.92);border-left:3px solid var(--accent);}}
.kicker{{display:block;font-family:Arial,sans-serif;font-size:28px;letter-spacing:5px;color:#e1c79d;}}
h1{{font-family:Georgia,'Times New Roman',serif;font-weight:400;font-size:76px;line-height:1.15;letter-spacing:1px;margin:16px 0 0;}}
</style>
<div id="root" data-composition-id="{id_}" data-width="1920" data-height="1080" data-duration="30">
{markup}
</div>
<script>
(function(){{const tl=gsap.timeline({{paused:true}});{script}
window.__timelines=window.__timelines||{{}};window.__timelines["{id_}"]=tl;}})();
</script>
</template>
'''
        (F / f'compositions/{id_}.html').write_text(doc)
        root_hosts.append(f'<div id="{id_}" class="clip" data-composition-id="{id_}" data-composition-src="compositions/{id_}.html" data-start="{(block - 1) * 30}" data-duration="30" data-width="1920" data-height="1080" data-track-index="1" data-track-kind="graphics"></div>')
    hosts = '\n'.join(root_hosts)
    # The licensed mix already includes narration and chapter punctuation.
    # Never double narration or layer the legacy unverified whoosh over it.
    soundtrack = 'final-mix.mp3' if (F / 'assets/audio/final-mix.mp3').is_file() and (F / 'production/SOUND_MIX_REPORT.json').is_file() else 'narration.mp3'
    audio = [f'<audio id="narration" class="clip" src="assets/audio/{soundtrack}" data-start="0" data-duration="2100" data-track-index="0" data-volume="1"></audio>']
    doc = f'''<!doctype html><html lang="en"><head><meta charset="UTF-8"><title>Rise of Old Valyria — documentary assembly</title>
<script src="assets/vendor/gsap.min.js"></script><style>*{{box-sizing:border-box}}html,body{{margin:0;width:1920px;height:1080px;overflow:hidden;background:#0b0b0a}}#film{{position:relative;width:1920px;height:1080px;overflow:hidden}}#film>.clip:not(audio){{position:absolute;inset:0}}</style></head><body>
<div id="film" data-composition-id="film" data-width="1920" data-height="1080" data-fps="30" data-start="0" data-duration="2100">
{hosts}
{''.join(audio)}
</div><script>window.__timelines=window.__timelines||{{}};window.__timelines.film=gsap.timeline({{paused:true}});</script></body></html>'''
    (F / 'index.html').write_text(doc)
    (F / 'hyperframes.json').write_text(json.dumps({'$schema': 'https://hyperframes.heygen.com/schema.json', 'name': 'rise-of-old-valyria', 'skill': 'hyperframes'}, indent=2) + '\n')
    available = sum(bool(s['proxy']) for s in shots)
    missing = [s for s in shots if not s['proxy']]
    manifest = {'status': 'WORK_IN_PROGRESS_NOT_FINAL_FILM', 'duration_seconds': 2100,
                'fps': 30, 'frame_count': 63000, 'image_slots': 1050, 'available_candidates': available,
                'missing_candidates': len(missing), 'final_approved_images': ledger['final_accepted'],
                'narration_manifest': '../story_film_35min/47_COMPLETE_35MIN_AUDIO_MANIFEST.json',
                'score_status': 'LICENSED_TECHNICAL_MIX_LISTENING_PENDING' if soundtrack == 'final-mix.mp3' else 'NARRATION_ONLY', 'spoken_word_qc': 'PENDING',
                'narration_word_alignment': 'BLOCK_WINDOWS_ONLY_NOT_WORD_LEVEL',
                'protected_ledger_sha256': sha((EP / 'audit/EP001_SHOT_AUDIT_LEDGER.json').read_bytes()),
                'chapters': [dict(zip(['number', 'start', 'duration', 'title', 'subtitle', 'treatment', 'accent'], c)) for c in CHAPTERS],
                'shots': shots}
    (F / 'production/FILM_MANIFEST.json').write_text(json.dumps(manifest, indent=2) + '\n')
    with (F / 'production/SOURCE_RECOVERY_QUEUE.csv').open('w') as stream:
        writer = csv.DictWriter(stream, fieldnames=['scene_id', 'source_candidate', 'start', 'visual_beat'])
        writer.writeheader()
        for shot in missing:
            writer.writerow({k: shot[k] for k in writer.fieldnames})
    (F / 'production/SHOT_PLAN.csv').write_text('scene_id,start_frame,end_frame,motion,source_status\n' + ''.join(f'{s["scene_id"]},{s["index"] * 60 - 60},{s["index"] * 60 - 1},{s["motion"]},{s["availability"]}\n' for s in shots))
    print(json.dumps({k: manifest[k] for k in ['duration_seconds', 'image_slots', 'available_candidates', 'missing_candidates', 'final_approved_images']}, indent=2))


if __name__ == '__main__':
    main()
