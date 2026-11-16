"""Record Batch088 individual visual review and selected script-alignment corrections."""
import csv
import hashlib
import html
import json
from pathlib import Path
import zipfile
from PIL import Image

root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
audit=root/'audit'
assets=Path('assets/episode_audit/batch088')
ids=['1aaH_vmkdGLNeHfI4mN-qi0qgFl6lSBCG','1Nsp00A2gNsELiJgFx_vlM9raLXMla_-b','1Fx35oAaTHzPq2QMXvJV9e0qywlflW4Ho','1xiFIpBQKJkOdhcNNMKflcnpwm6wRQG-x','1tJH14ofazPvFQdo77NBmeAhE7ilsKfis','1nhbLWJpY6Q9rinnpX75I_LNQ9ESANEuZ','1wpK4oNc4g-Z0XCXR9Ldwm56oaxqZDaZP','12uQmcCb3FqxQDHBC5pP0BIDVEBRLX--q','1NRhA0QhLFVn-dPeEqe19IOlw4EoAjkwI','1BjarHF5ZQAvLXe0QpUR-9Awe3KRUzVPJ']
checks=['eec3a351aa90e415c86cf1ac2a7aacb6','9be1ffd004e390467eeb24f3f064328b','c0501698bbca4635c78c76010222aabd','dc07a50e322a00eefbd859cc1b0a9793','2bf1de04363b56afd6c9f87f4e14574a','5873ca6cf9f498f7bfae7c9d0eac64f2','11cc32bb06a78a69763f895b40657f20','890d13fc36f4b359e8890d0a0593ef19','2e5685cf996a942548cf7d0a5a626215','d1fbb67b0e5116871ee7033c96166fb2']
notes=[
('KEEP_CONTEXT_ONLY','Coastal basalt tower with three distant pale-haired observers; long column on road escorted by riders.','Escorted arrival supports captivity context after IMG0870 causeway, but no raid or debt transaction is visible. Tower top looks irregular; do not assume ruins or exact canon architecture.'),
('KEEP_CANDIDATE','Under fabric awnings, three adults kneel before chest and ore-like pile, with a standing row of bound adults and pale-haired handler.','Readable coercive market context. Specific debt-bondage origin is not established by image. Inspect hands and rope connections at full resolution before final acceptance.'),
('KEEP_CANDIDATE','Two pale-haired black-robed figures examine a small pale object opposite an ornate-clothed intermediary; seated man and standing woman have linked ankle restraints.','Supports commerce in captives. Object is not confidently identifiable as currency; no invented market location or historical transaction asserted.'),
('KEEP_CONTEXT_ONLY','High wide view of black rocky hill with several entrances and three long thin processions converging on it.','Useful arrival scale before descent. Chains and individual roles not legible at this distance; keep as contextual scale, not evidence of each person being enslaved.'),
('KEEP_CANDIDATE','Close view of restrained adult in coarse tunic; black-robed figure grips upper arm, with queue and dark doorway behind.','Clear coercion and entry beat. Does not by itself show downward motion. Cuff/chain and gripping-hand anatomy require enlarged inspection.'),
('REPLACE','Outside cave, chained line advances between two pale-haired guards; dog lies near foreground, faint orange fissures inside.','Repeats threshold rather than taking viewer underground. Replace with interior descending steps. Existing glow not authorization for new emitters.'),
('REPLACE','Soot-covered adults queue through narrow open-air rock cleft, front face in profile against dark wall.','Human reaction useful, but open sky interrupts underground progression. Replace with hunched captive inside low tunnel.'),
('KEEP_CANDIDATE','Adults cover mouths with forearms in thick warm haze; pale-haired figure also covers face, small orange lines in rock behind.','Communicates breathing distress. Haze chemistry cannot be inferred; orange glow is original evidence, not new emission approval. Adjacent new images use cooler light, requiring grade continuity.'),
('REPLACE','Exterior camp of small tents below hill doorway with figures and wagons; pale haze across ground.','Camp panorama does not sustain narrated suffocating underground atmosphere. Replace with interior dust/haze and breathing distress.'),
('REPLACE','Large flat-topped rocky hill with many entrances and long switchback processions, distant city and volcano.','Second exterior scale shot stalls shift to chained mining. Replace with working miner and clearly legible restraint.')]
replacements={
876:('v02','Three adults with restrained wrists descend rough steps into low mine tunnel; hooded guard stands above.','Clearer descent. Guard is not established as a recurring character; costume/identity continuity and chain mechanics remain held.'),
877:('v02','Hunched adult with short curly hair and wrist cuff beneath very low stone lintel; two blurred figures behind.','Clear interior human vulnerability. Does not establish same individual as previous shot; treat as different captive rather than false match cut.'),
879:('v02','Two ragged adults cover nose and mouth in narrow dusty passage; pick leans against rock.','Improved oppressive-air match. Haze is illustrative, not chemical identification. Small baked-in black borders need delivery conform; repeated coughing gesture should be assessed with 0878 in animatic.'),
880:('v03','Crouching miner grips pick at natural vein; iron ankle cuff and single chain visible, second worker beside basket behind.','Clearer chained-labor match. v02 rejected for rope restraint/tangled floor chain, v03 inspected with iron cuff and simplified chain. Tool grip, chain linkage and anatomy still require full-resolution acceptance gate.')}
ledger=json.loads((audit/'EP001_SHOT_AUDIT_LEDGER.json').read_text())
assert ledger['reviewed_individually'] in (869,879)
manifest=[]
for j,(decision,observation,action) in enumerate(notes):
    num=871+j
    shot=ledger['shots'][num-1]
    name=f'VAL-EP001-IMG{num:04d}.png'
    source=Path('google_drive')/name
    md5=hashlib.md5(source.read_bytes()).hexdigest()
    assert md5==checks[j],name
    with Image.open(source) as im:
        im.load(); dims=list(im.size)
    assert shot['scene_id']==name[:-4]
    shot.update(audit_status=decision,drive_file_id=ids[j],selected_local_file=str(source),original_local_file=str(source),visual_observation=observation,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md5,reviewed_on='2026-11-15',review_scope='Individually opened at tool display resolution; no enlarged all-pixel anatomy certification or timed audio inspection.')
    record=dict(scene_id=shot['scene_id'],drive_file_id=ids[j],native_md5=md5,native_bytes=source.stat().st_size,native_dimensions=dims,original_observation=observation,decision=decision,action=action,selected_file=str(source))
    if num in replacements:
        version,obs,limits=replacements[num]
        p=assets/f'VAL-EP001-IMG{num:04d}_{version}.png'
        with Image.open(p) as im:
            im.load(); rdims=list(im.size)
        rmd5=hashlib.md5(p.read_bytes()).hexdigest()
        shot.update(audit_status='REPLACED_PROVISIONAL',selected_local_file=str(p),replacement_file=str(p),replacement_observation=obs,replacement_review=limits,replacement_md5=rmd5,replacement_dimensions=rdims)
        record.update(selected_file=str(p),replacement_observation=obs,replacement_limitations=limits,replacement_md5=rmd5,replacement_dimensions=rdims)
    manifest.append(record)
ledger['reviewed_individually']=879
(audit/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for row in ledger['shots'] for k in row))
with (audit/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for row in ledger['shots']:
        w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
(audit/'BATCH_088_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
summary='''# Batch088 — IMG0871–0880, 29:00–29:20

All ten originals individually opened at tool display resolution; native MD5s matched fresh Drive listing and all PNGs decoded. Full 29:00–29:30 narration paragraph and neighboring paragraphs read before review.

Four mismatched/redundant exterior shots replaced in provisional selection: IMG0876 (interior descent), IMG0877 (captive under low tunnel ceiling), IMG0879 (breathing distress in dust), IMG0880 (working miner with iron ankle cuff). Five generated versions individually viewed; four selected. IMG0880_v02 rejected for rope ankle restraint/tangled chain; v03 corrects this. Originals and rejected evidence retained separately.

Remaining originals: four provisional keep candidates (0872, 0873, 0875, 0878), two context-only holds (0871, 0874). Arrival/market/scale images need not literally illustrate every two-second narration fragment; they support the complete paragraph. Specific debt origin, geographic origin, currency identity, gas chemistry and individual identity are not inferred from images.

The previous IMG0870 causeway procession and current IMG0871 coastal escort support an arrival transition at broad scale, but chain visibility and precise spatial continuity remain unverified. New mine shots are production reconstructions, not claims of canonical staging. Cool replacement light versus warm existing IMG0878, repetitive coughing beats at 0878–0879, borders on 0879, full-pixel anatomy/chain mechanics and timed narration remain acceptance gates. No new flame/sorcery treatment selected. Script and original shot map unchanged.

Progress: 879/1050 original slots reviewed; zero final delivery approvals. Five additional generated versions inspected this pass. IMG0500 remains inherited missing/unresolved. Next Batch089: IMG0881–0890, including the 29:30 transition; read both full paragraphs before deciding treatment for dangerous steam/firewyrm spans. Do not infer new emitter authorization from general replacement authority.
'''
(audit/'BATCH_088_REVIEW.md').write_text(summary)
page=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Batch088 audit and corrections</title><style>body{background:#17191c;color:#eee;font:18px system-ui;max-width:1300px;margin:30px auto;padding:24px}img{width:100%}p{line-height:1.5}article{margin:70px 0}</style><h1>Batch088 — individual audit and corrections</h1><p>29:00–29:20. Four provisional replacements, four keep candidates, two context holds. No final approvals.</p>']
for row in manifest:
    name=row['scene_id']+'.png'
    page.append('<article><h2>'+row['scene_id']+'</h2><h3>Original</h3><img src="originals/'+name+'" alt="Preserved original"><p>'+html.escape(row['original_observation']+' '+row['action'])+'</p>')
    if 'replacement_md5' in row:
        page.append('<h3>Selected provisional replacement</h3><img src="replacements/'+Path(row['selected_file']).name+'" alt="Inspected replacement"><p>'+html.escape(row['replacement_observation']+' '+row['replacement_limitations'])+'</p>')
    page.append('</article>')
page.append('</html>')
out=Path('.recovery/batch088');out.mkdir(parents=True,exist_ok=True)
preview=out/'BATCH_088_INDIVIDUAL_AUDIT.html';preview.write_text('\n'.join(page))
package=Path('google_drive/EP001_BATCH_088_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
    z.write(preview,preview.name)
    for n in ['BATCH_088_REVIEW.md','BATCH_088_MANIFEST.json','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv']:
        z.write(audit/n,n)
    for row in manifest:
        name=row['scene_id']+'.png';z.write(Path('google_drive')/name,'originals/'+name)
        if 'replacement_md5' in row:
            p=Path(row['selected_file']);z.write(p,'replacements/'+p.name)
    z.write(assets/'VAL-EP001-IMG0880_v02.png','rejected_evidence/VAL-EP001-IMG0880_v02.png')
print(package,package.stat().st_size,hashlib.md5(package.read_bytes()).hexdigest())
