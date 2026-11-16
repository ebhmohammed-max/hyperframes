"""Build the Batch087 review package from inspected originals; never generates approvals."""
import csv
import hashlib
import html
import json
from pathlib import Path
import zipfile
from PIL import Image

ROOT = Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
AUDIT = ROOT / 'audit'
OUT = Path('.recovery/batch087')
OUT.mkdir(parents=True, exist_ok=True)
ids = ['1EExkxaxNnfaBcu2O71cErdNC1KRontqx','1OPr-0QPicbce1zX7FBALpBr9W0iWW_cJ','1FA_EjsK-txJXOoL3L3pqGJXTMz4LQe4u','1PSyY6FQ0vULTyuUW-C1pCzAxv7LuteD2','12FO3GscnbMnoidlnbSSE4s5RwdflMXdl','1b0eHHFpvz-S3lNQKo5oD3oahjwB88g0V','1bfJfJ2kNLaLLS0kI05wmYmeQZniPC7gW','1XdMa868KWGq6OoExiHK14flBNCqp8q4g','1rkYDVmGr1hIjwcqA_PXgleFwZEXQOErS','1XNP8uDWyIMhdf7izvXJgOB3HJDf3tLQi']
checks = ['0a992ee296a1115f0a734a66a74711b8','b443f55efebb21916e443c4393db45ee','f4372ba174fb7ba4a238d55ffb12a86a','783921ab0978e20afd575bb59ee16e8d','18103d6a9f1412862e4e5f468b096f25','98ac35b13ffa9b2c40d7d082684bc60e','e86cb75f8e6202188d7234c5bfcb3303','108f6f223e56e02e32c78348712b4d30','95a30363f7f67f416457db91128a615a','5bf8acb8cc44822ccfdce7a82e18f0d5']
notes = [
('KEEP_CANDIDATE','Long pale-haired black-robed figure sorts metallic-looking blocks at a dark stone table; mineral shelves behind.','Useful demand/material insert, but colors do not authenticate gold, silver or copper. Retain provisionally; establish mine geography in adjacent shots.'),
('REPLACE','Two pale-haired black-robed figures face camera against mineral-streaked rock; a third sits behind.','Posed portrait does not develop ore extraction or depth. Replace with ore-bearing wall and a legible inspection action, without inventing mineral certainty.'),
('RELOCATE_OR_REPLACE','Black-robed figure stands arms folded outside a dark rock opening; two lighter-clothed figures stand behind; orange fissures inside.','Exterior threshold is not deep underground. Consider relocating to refusal beat; otherwise replace with cramped interior shaft. Existing glow is observed, not authorization for new emitters.'),
('KEEP_CONTEXT_ONLY','Wide black rocky hill with several dark entrances, a winding path and three small ascending figures; carved pale parapet foreground.','Usable surface geography, not blistering roots. Avoid repeating the next wide. Check whether carved pale stone belongs to established location grammar.'),
('REPLACE','Aerial volcanic plain with peaks, many pale linear routes, distant coastal towers and faint orange lines.','Another surface vista cannot communicate suffocating shafts. Replace with a constrained mine-depth composition. Do not claim fourteen countable peaks or approved emitter treatment.'),
('KEEP_CANDIDATE','Seven pale-haired figures outside a mine opening; central raised fist, folded arms, picks and basket abandoned in foreground.','Strongest refusal-of-labor beat. Keep provisionally; near-repeated faces and uncertain gestures require character differentiation and closer inspection before final acceptance.'),
('KEEP_CANDIDATE','Clean folded hands over red cloth beside a pick on black ground; bracelet and violet-stone ring visible.','Useful refusal/privilege detail after 0866, though abrupt costume change needs identity/cut continuity. Do not call hands injured or enslaved.'),
('RELOCATE_OR_REPLACE','Low-angle close portrait of pale-haired figure with light violet-looking eyes and dark neck ring against carved pale stone.','May serve an elite reaction but lacks causal action. Relocate only if character and pale-stone setting can be established; otherwise replace with an explicit labor-demand decision.'),
('RELOCATE_OR_REPLACE','Macro of rough hand beside gold-colored mineral chunks on dark stone.','Useful mineral-demand motif but late placement interrupts transition toward slavery. Move earlier within paragraph or replace; gold color alone is not mineral identification.'),
('KEEP_CONTEXT_ONLY','Dark coastal cliff city and stone causeway; black-robed foreground observer faces a distant single-file procession.','Potential ominous bridge to next paragraph. Chains, captivity and guard roles are not legible at display scale; do not label procession enslaved. Compare with actual IMG0871 before locking cut.')]
ledger = json.loads((AUDIT/'EP001_SHOT_AUDIT_LEDGER.json').read_text())
assert ledger['reviewed_individually'] in (859,869)
manifest=[]
for j, (status, observation, action) in enumerate(notes):
    number=861+j
    shot=ledger['shots'][number-1]
    name=f'VAL-EP001-IMG{number:04d}.png'
    path=Path('google_drive')/name
    raw=path.read_bytes()
    md5=hashlib.md5(raw).hexdigest()
    assert md5 == checks[j], name
    with Image.open(path) as im:
        im.load()
        dimensions=im.size
    assert shot['scene_id'] == name[:-4]
    shot.update(audit_status=status,drive_file_id=ids[j],selected_local_file=str(path),visual_observation=observation,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md5,review_scope='Individually opened at tool display resolution; no enlarged all-pixel anatomy certification; no timed audio or next-batch image comparison.',reviewed_on='2026-11-15')
    manifest.append(dict(scene_id=shot['scene_id'],drive_file_id=ids[j],md5=md5,bytes=len(raw),dimensions=dimensions,status=status,observation=observation,action=action))
ledger['reviewed_individually']=869
(AUDIT/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
# Keep all inherited columns and serialize nested values explicitly.
keys=list(dict.fromkeys(k for row in ledger['shots'] for k in row))
with (AUDIT/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys); w.writeheader()
    for row in ledger['shots']:
        w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
(AUDIT/'BATCH_087_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
summary='''# Batch087 — IMG0861–0870, 28:40–29:00

Ten originals individually opened; native MD5 matched Drive for all ten and all PNGs decoded. Review is at displayed resolution, not full-pixel anatomy certification. No corrections generated, no final approvals.

Read full 28:30–29:00 narration and surrounding paragraphs before review. Sequence must move from elite mineral demand into dangerous mine labor and the turn to slavery. Current surface vistas and posed portraits weaken that progression. Two replace decisions, three relocate-or-replace decisions, three provisional keep candidates and two context-only holds. These are audit decisions, not approved masters.

IMG0866 is the clearest refusal beat. IMG0867 may support it but changes costume. IMG0870 is only a potential transition: distant procession does not establish captivity. Actual next-batch cut remains uninspected. No new flame/sorcery treatment authorized or generated. Script and original shot map unchanged; timing has not been checked against narration audio.

Progress: 869/1050 individually reviewed per cumulative ledger; 0 final approvals. IMG0500 remains inherited missing/unresolved, not newly searched. Candidate count unchanged from prior screenshot report (117; not independently recounted here).

Next: Batch088, IMG0871–0880. Compare actual IMG0871 to held IMG0870 transition. Corrections from this batch remain pending, not silently substituted.
'''
(AUDIT/'BATCH_087_REVIEW.md').write_text(summary)
page=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Batch087 individual audit</title><style>body{background:#151719;color:#eee;font:18px system-ui;max-width:1400px;margin:32px auto;padding:20px}img{width:100%}article{margin:50px 0}p{line-height:1.6}</style><h1>Batch087 — individual original-image audit</h1><p>No final approvals. No generated corrections. 28:40–29:00.</p>']
for row in manifest:
    name=row['scene_id']+'.png'
    page.append('<article><h2>'+html.escape(row['scene_id']+' — '+row['status'])+'</h2><img alt="Original under audit" src="originals/'+name+'"><p>'+html.escape(row['observation'])+'</p><p>'+html.escape(row['action'])+'</p><p>Verified MD5: '+row['md5']+'</p></article>')
page.append('</html>')
(OUT/'BATCH_087_INDIVIDUAL_AUDIT.html').write_text('\n'.join(page))
package=Path('google_drive/EP001_BATCH_087_AUDIT.zip')
with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
    z.write(OUT/'BATCH_087_INDIVIDUAL_AUDIT.html','BATCH_087_INDIVIDUAL_AUDIT.html')
    for n in ['BATCH_087_REVIEW.md','BATCH_087_MANIFEST.json','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv']:
        z.write(AUDIT/n,n)
    for row in manifest:
        name=row['scene_id']+'.png'; z.write(Path('google_drive')/name,'originals/'+name)
print(package,package.stat().st_size,hashlib.md5(package.read_bytes()).hexdigest())
