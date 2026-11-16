"""Record visually inspected Batch087 replacements and preserve original evidence."""
import csv
import hashlib
import html
import json
from pathlib import Path
import zipfile
from PIL import Image

root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
audit=root/'audit'
assets=Path('assets/episode_audit/batch087')
ledger=json.loads((audit/'EP001_SHOT_AUDIT_LEDGER.json').read_text())
choices={862:('v02','A rough hand holds a reddish mineral sample against a veined rock wall; pick and narrow tunnel behind.','Better mineral-context match than posed portrait. Mineral composition remains illustrative, not verified.'),863:('v02','Crouching adult miner works a pick inside a low rough tunnel with timber supports and descending passage.','Interior labor replaces exterior portrait. Small baked-in black borders require delivery conform; no claim of heat or exact geography from image alone.'),865:('v03','Downward view of deep rock shaft, rope-suspended ore basket, ladders and small worker under cool overhead light.','Replaces surface panorama with shaft depth. v02 rejected for visible unrequested warm flames; v03 removes those. Rope/ladder safety mechanics remain production illustration, not engineering evidence.'),868:('v03','Cropped officials in dark sleeves and gold-trim cuff exchange linked iron restraints across a mine table.','Replaces generic face with a deliberate coercive-labor decision. Production-invented symbolic reconstruction, not a claimed canonical historical transaction. v02 not selected: face-led composition and costume weakened role clarity.'),869:('v02','Gold-ringed hand rests on a plain tablet beside linked rough iron wrist cuffs on dark tabletop.','Replaces late mineral insert with forced-labor decision detail. Tablet and sleeve continuity with 0868 still need conform; avoid holding both restraint inserts too long.')}
rows=[]
for num,(version,observation,limits) in choices.items():
    shot=ledger['shots'][num-1]
    p=assets/f'VAL-EP001-IMG{num:04d}_{version}.png'
    with Image.open(p) as im:
        im.load(); dims=im.size
    old=shot.get('original_local_file',shot['selected_local_file'])
    shot.update(original_local_file=old,replacement_file=str(p),selected_local_file=str(p),audit_status='REPLACED_PROVISIONAL',replacement_observation=observation,replacement_review=limits,replacement_md5=hashlib.md5(p.read_bytes()).hexdigest(),replacement_dimensions=list(dims),final_accepted=False,replacement_review_scope='Individually viewed generated image at tool display resolution; image decoded. No timed narration or all-pixel anatomy certification.')
    rows.append({'scene_id':shot['scene_id'],'selected_file':str(p),'original_file':old,'md5':shot['replacement_md5'],'dimensions':dims,'observation':observation,'limitations':limits})
(audit/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for row in ledger['shots'] for k in row))
with (audit/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for row in ledger['shots']:
        w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
(audit/'BATCH_087_REPLACEMENT_SELECTION.json').write_text(json.dumps({'status':'provisional edit selections; not final delivery approval','selections':rows,'excluded_candidates':['VAL-EP001-IMG0865_v02.png','VAL-EP001-IMG0868_v02.png'],'generated_and_inspected_this_pass':7,'selected_this_pass':5},indent=2)+'\n')
report='''# Batch087 correction pass

Replaced the five previously flagged slots in the provisional edit selection: IMG0862, IMG0863, IMG0865, IMG0868 and IMG0869. All seven generated versions were individually viewed; five selected versions decoded and checksummed. Originals retained, rejected versions excluded from selected set.

The revised progression shows mineral veins, underground work, shaft depth, refusal (existing IMG0866–0867), then the decision to use restraints. The officials/table scene is a production-invented illustration of the narration, not evidence of a specific canonical event. No narration or baseline shot-map changes. Versioned selection map and cumulative ledger identify replacement files explicitly.

Two candidates rejected: IMG0865_v02 contained unwanted small flames despite the prompt; IMG0868_v02 remained face-led with insufficient role clarity. IMG0865_v03 removes visible warm flames; IMG0868_v03 uses a face-free exchange. No new flame treatment selected.

These are stronger script matches, not final delivery approvals. Outstanding checks: IMG0863 borders, visual continuity of props/sleeves between 0868–0869, exact anatomy/mechanics at full resolution, timed narration and the cut into actual IMG0871. Surface context shots 0864 and 0870 remain context-only, not automatically rejected because they do not illustrate every spoken word literally.

Progress unchanged: 869/1050 original slots reviewed, zero final delivery approvals. Seven additional generated candidates inspected this pass (prior 117 count remains inherited, so not independently certified as a cumulative total). Next chronological batch: IMG0871–0880.
'''
(audit/'BATCH_087_CORRECTION_PASS.md').write_text(report)
page=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Batch087 corrections</title><style>body{background:#17191c;color:#eee;font:18px system-ui;max-width:1300px;margin:30px auto;padding:24px}img{width:100%}p{line-height:1.5}article{margin:70px 0}</style><h1>Batch087 — selected replacements</h1><p>Five provisional replacements. Originals preserved. No final delivery approvals.</p>']
for row in rows:
    name=Path(row['selected_file']).name
    page.append('<article><h2>'+row['scene_id']+'</h2><img src="replacements/'+name+'" alt="Inspected replacement"><p>'+html.escape(row['observation'])+'</p><p>'+html.escape(row['limitations'])+'</p></article>')
page.append('</html>')
preview=Path('.recovery/batch087/BATCH_087_CORRECTIONS.html'); preview.write_text('\n'.join(page))
package=Path('google_drive/EP001_BATCH_087_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
    z.write(preview,'BATCH_087_CORRECTIONS.html')
    for n in ['BATCH_087_CORRECTION_PASS.md','BATCH_087_REPLACEMENT_SELECTION.json','BATCH_087_MANIFEST.json','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv']:
        z.write(audit/n,n)
    for num in range(861,871):
        name=f'VAL-EP001-IMG{num:04d}.png';z.write(Path('google_drive')/name,'originals/'+name)
    for row in rows:
        p=Path(row['selected_file']);z.write(p,'replacements/'+p.name)
    for name in ['VAL-EP001-IMG0865_v02.png','VAL-EP001-IMG0868_v02.png']:
        z.write(assets/name,'rejected_evidence/'+name)
print(package,package.stat().st_size,hashlib.md5(package.read_bytes()).hexdigest())
