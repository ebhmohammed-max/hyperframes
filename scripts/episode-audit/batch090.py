"""Record Batch090 individual visual review and selected script-alignment corrections."""
import csv
import hashlib
import html
import json
from pathlib import Path
import zipfile
from PIL import Image

root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
audit=root/'audit'
assets=Path('assets/episode_audit/batch090')
ids=['17LTkO5pYTtgjJhFznps_jaIB3qprnjIf','1UvH_PQtlV2uiPIdROvhPDKSjgUwHvhfp','1LyyaMcGQIMg91A-dnfxlNRSCBcggoMq-','1zyY5D0SrZmflwjO_9KxgNhWMap75lac-','1sAeFTfv78jeKv37FwynoPW7vS2oVImYa','1jy_EGTXePUK7Ufa-B0eAOL11ek-W8gHb','1d0_BicOEI17M4xxLIUWq1AWaxZ-pni7D','1KJYT1B9XHZYP-Fs8AEKT0oCize1uBiTo','1msRyjN91QW3FWWtUqCMi34TMTVCoCOhI','1048whOX2JzMD8zhjxCm6FfrgSKGtNY1r']
checks=['15b7de0d85a49fc40f9c14c01a6e3aba','a95572133eacfaf7f4c485f1d1b63c0c','6341c32973c45d33da961bd9b4d79ca8','1f9b7c9b2504e177788dc02a8f516d97','68c9d0671794a830b4cbe04321b6627d','2aa5eb3ff4c43e9475c9152613b04f7e','7255a93105c24be44595bd0519fcb7eb','80748454f25a42b6261eae4d710810f5','c556e1d8e83dac69f0e7fce54acb6bf1','9434ec862c756dc0c7b38edca585248e']
notes=[
('REPLACE','Standing adult workers look upward beside hanging basket and large regular columns; low greenish haze, black-robed observer.','Does not convey gang overcome without warning; polished monumental columns weaken mine continuity. Replace with slumped gang aftermath.'),
('KEEP_CANDIDATE','Empty narrow rough tunnel recedes into darkness with small reddish line far away.','Useful deepest-shaft transition. Original small red line observed only; not authorization for new emitter.'),
('KEEP_CANDIDATE','Foreground adult raises pick at dark wall, two adult workers behind, warm overhead light.','Clear pickaxe working beat. Tool grip, repeating faces and wrist materials need enlarged review.'),
('KEEP_CANDIDATE','Miner raises pick beside branching orange fissures, two figures shield faces in dusty cavern.','Supports dangerous breakthrough. Existing orange fissures are original evidence, not a newly approved effect. Exact thermal physics not certified.'),
('REPLACE','Dark field of pits with thin orange lines and wisps; no identifiable creature visible.','Narrated creature reveal missing. Replace with clear pale wingless burrower under no-new-emitter ruling.'),
('REPLACE','Large pale annular body crosses bright breakout with airborne debris and falling silhouettes; head not visible.','Creature identity and anatomy unreadable. Replace using same newly inspected 0895 creature reference; no blast-light effect.'),
('KEEP_CANDIDATE','Detached pick head, broken handle, chain and dark rag on circular darkened floor patch.','Indirect ominous aftermath supports narrated violence without graphic imagery. Do not assert the patch is a body or that its cause is proven.'),
('KEEP_CONTEXT_ONLY','Close pale-haired black-robed adult with violet-looking eyes looks sideways against dark stone.','Can bridge from disaster to elite indifference, but decision is not visible. Original identity not newly certified; retain only in sequence context.'),
('REPLACE','Pale hand with ornate gold snake-like bracelet lies beside massive dark metal loop on black ground.','Ambiguous jewelry insert does not communicate deeper-shaft demand. Replace with administrative directing gesture and work materials.'),
('REPLACE','Pale-haired nobles sit at huge round table; immense crowd/column extends along road through opening behind.','Council-to-army impression muddles more mine labor. Replace with captives receiving ore baskets under supervision.')]
replacements={
891:('v02','Kneeling adult supports slumped worker, another sags seated beside wall, pick and basket foreground.','Clearer non-graphic gang-overcome aftermath. Image alone does not determine death or gas chemistry; no literal whole-gang count asserted.'),
895:('v03','Pale annular legless wingless burrower with blunt wedge head and small dark eyes emerges from right rock aperture; fallen pick gives scale.','Production creature design, not canonical anatomical proof. v02 rejected for modern-looking helmet/clothing on generated human; v03 removes human. No flame/glow generated in selected image.'),
896:('v02','Same pale annular burrower thrusts farther left from rock aperture with displaced fragments and dust.','Generated with selected 0895_v03 as reference. Broad head/eye/hide/body traits consistent at display resolution; detailed mesh/scale continuity not certified. Body partly occluded; no full-anatomy proof.'),
899:('v02','Face-free officials in dark gold-trim sleeves at stone table; one points while resting other hand on unmarked slab, rope, slats, ore and cuff nearby.','Clearer insistence/administration. Generated tablet reads as stone slab rather than wax: record observation, do not claim written orders. Pointing direction and mine descent are contextual, not diagrammed.'),
900:('v02','Ragged adult queue with visible wrist restraints; front adult receives woven basket from dark-robed supervisor by mine opening.','More-labor motif clearer than council/army tableau. Queue blocking could read outward movement, so intake direction and exact cut remain provisional. Original faces and costume continuity need review.')}

ledger=json.loads((audit/'EP001_SHOT_AUDIT_LEDGER.json').read_text())
assert ledger['reviewed_individually'] in (889,899)
manifest=[]
for j,(decision,observation,action) in enumerate(notes):
    num=891+j
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
ledger['reviewed_individually']=899
(audit/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for row in ledger['shots'] for k in row))
with (audit/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for row in ledger['shots']:
        w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
(audit/'BATCH_090_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
summary='# Batch090 — IMG0891–0900, 29:40–30:00\n\nTen originals individually opened at tool display resolution; all native MD5s matched fresh Drive metadata, and PNGs decoded. Full 29:30–30:00 and following 30:00–30:30 narration read.\n\nFive provisional replacement slots: 0891 gang-overcome aftermath, 0895 creature reveal, 0896 matching creature breakout, 0899 administrative demand, 0900 captives receiving baskets. Six generated versions individually inspected; five selected. Rejected 0895_v02 contained a modern-looking helmet/clothed human; selected v03 removes the figure.\n\nFour originals are keep candidates (0892, 0893, 0894, 0897); 0898 retained as context-only elite reaction. Prior IMG0890 support/collapse shot leads into new 0891 aftermath thematically; identities and exact geography are not established as a match cut.\n\nTreatment ruling predates prompts. Selected creature pair is pale, wingless, legless, annular-bodied with blunt wedge head and small dark eyes. 0896 uses selected 0895 as reference; broad traits are consistent at display scale, not a full anatomical certification. This is production-invented creature anatomy. No new flames, luminous body, magical beam or incineration effect selected. Existing 0897 broken/charred-tool insert supplies indirect aftermath; cause of scorching is not independently established. Literal new flame/incineration treatment remains held. Script and baseline shot map unchanged.\n\nRemaining gates: full-pixel human/tool/chain anatomy, creature detail and scale continuity, original warm-to-new-cool light changes, interpretation of unmarked slab in 0899 (not readable orders), queue direction in 0900, transition to actual IMG0901, timed narration. Prior Batch089 IMG0885 partial lifting-mechanics hold remains unresolved.\n\nProgress: 899/1050 original slots reviewed; zero final delivery approvals. Six additional generated versions inspected this pass. IMG0500 remains inherited missing/unresolved. Next Batch091 IMG0901–0910 covers the above/below contradiction; compare both full paragraphs and the held transition.\n'
(audit/'BATCH_090_REVIEW.md').write_text(summary)
page=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Batch090 audit and corrections</title><style>body{background:#17191c;color:#eee;font:18px system-ui;max-width:1300px;margin:30px auto;padding:24px}img{width:100%}p{line-height:1.5}article{margin:70px 0}</style><h1>Batch090 — individual audit and corrections</h1><p>29:40–30:00. Five provisional replacements, four keep candidates, one context hold. No final approvals.</p>']
for row in manifest:
    name=row['scene_id']+'.png'
    page.append('<article><h2>'+row['scene_id']+'</h2><h3>Original</h3><img src="originals/'+name+'" alt="Preserved original"><p>'+html.escape(row['original_observation']+' '+row['action'])+'</p>')
    if 'replacement_md5' in row:
        page.append('<h3>Selected provisional replacement</h3><img src="replacements/'+Path(row['selected_file']).name+'" alt="Inspected replacement"><p>'+html.escape(row['replacement_observation']+' '+row['replacement_limitations'])+'</p>')
    page.append('</article>')
page.append('</html>')
out=Path('.recovery/batch090');out.mkdir(parents=True,exist_ok=True)
preview=out/'BATCH_090_INDIVIDUAL_AUDIT.html';preview.write_text('\n'.join(page))
package=Path('google_drive/EP001_BATCH_090_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
    z.write(preview,preview.name)
    for n in ['BATCH_090_REVIEW.md','BATCH_090_TREATMENT_RULING.md','BATCH_090_MANIFEST.json','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv']:
        z.write(audit/n,n)
    for row in manifest:
        name=row['scene_id']+'.png';z.write(Path('google_drive')/name,'originals/'+name)
        if 'replacement_md5' in row:
            p=Path(row['selected_file']);z.write(p,'replacements/'+p.name)
    z.write(assets/'VAL-EP001-IMG0895_v02.png','rejected_evidence/VAL-EP001-IMG0895_v02.png')
print(package,package.stat().st_size,hashlib.md5(package.read_bytes()).hexdigest())
