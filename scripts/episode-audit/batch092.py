"""Record Batch092 individual visual review and selected script-alignment corrections."""
import csv
import hashlib
import html
import json
from pathlib import Path
import zipfile
from PIL import Image

root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
audit=root/'audit'
assets=Path('assets/episode_audit/batch092')
ids=['1tEb3w3yc7xu8z_HgolzJP3bWptHynhQa','1v4yNxhLCaSn84EFjuTwHqvRQJIY1AbAw','1-8K0Yb0HMLaLbfYYU5U-ORypDtciuH0G','15Bczym8ADQluyC8gHUckRNBTIdV5Mcgs','1u7yQrCTgfWiSpPcMdHH8Ai-lFfKDRdeC','1J4mK0YW9DFRrVOWXMfzFnUFlF1_JllgT','1mvN2S-tMN7M-E8fDpqecj55fhUBA5IPf','1Fm-ION0WV4p8US4ynd8zykq7PUPNV35S','1-2a4x_CIbMT23i2MrnuXslTxFfedAFp6','1YwO4gCivZ6B0caVMC2B6mGZ1rCivSJ7V']
checks=['a27c328a1de4b9db9ac0396a8a8ad2be','072fc199a4d6e9b923bfc5147db0b88b','6d39fca3470ad9bc064facae9b394d70','2700469e7be28e8df68ae1fafcc07576','89e3a4fef92cee44741b561d4c76c0f2','b95a6cc0211710842c41e3a823c76317','f59a3e18eb4481acfacbf319479a4e5f','c72a5a98bb287ec1a397e27d29954601','8cf5cbcb0c60cde471588dad05d52aad','1ddcb253c133c120ae22e24eca54524d']
notes=[
('KEEP_CONTEXT_ONLY','Deep vertical stone shaft with many chain-suspended timber platforms and winches; remote light opening above, few tiny figures.','Supports underworld scale after selected 0910 labor close view. Repeated large winches/platform engineering unverified; not evidence of practical safe machinery or captive identity.'),
('KEEP_CANDIDATE','Coiled heavy iron chain, metallic-looking ore chunk and rope on dark dusty stone.','Clear material appetite/chain motif; ore identity and physical continuity with prior shot not established.'),
('REPLACE','Close pale-haired adult portrait with violet-looking eyes and earring against blurred dark rock.','Repetitive generic portrait weakens link from labor appetite to wider empire. Replace with coastal labor-supply negotiation.'),
('KEEP_CONTEXT_ONLY','Curved decorated golden-bronze object beside heavy dark chain on rocky ground.','Can foreshadow competing imperial wealth and chains, but not identifiable as canonical Ghiscari insignia. Do not call it Bronze Harpy or proven currency.'),
('REPLACE','Large dark floating landmass above barren terraced pits and long tiny processions.','Unmotivated levitation contradicts grounded geography. Replace with grounded brick harbor/city as editorial teaser of Old Ghis.'),
('REPLACE','Huge solitary black tapered spire by largely empty coast, small dock and a few sails.','Weak opening for generational transformation and bustling harbors. Replace with living Summer Sea port.'),
('KEEP_CANDIDATE','Over-shoulder pale-haired observer sees dark crowded harbor with timber dock structures, boats and large stepped quay-like platform.','Supports commerce context, but identity/location and dark monumental silhouette need matching against brighter new port. Do not assume exact Ghiscari or Valyrian harbor based only on form.'),
('REPLACE','Raised pale curving causeway on tall supports crosses valley toward distant built area and volcanic mountains.','Conflicts with earlier baseline ground-level fused dragonroad grammar. Replace with at-grade broad straight road through settled valley.'),
('KEEP_CANDIDATE','Aerial coastal valleys with patchwork fields, branching roads, many settlements and projecting piers under gray sky.','Useful regional transformation scale. Not an exact map, surveyed coastline or counted fourteen volcanoes.'),
('KEEP_CONTEXT_ONLY','Dark-haired bearded adult traveler looks upward in rocky snow-streaked mountain pass.','Can stand for northern foothill travel within full paragraph, not literal geographic proof. Isolated portrait should remain brief; actor uniqueness not guaranteed.')]
replacements={
913:('v03','Two officials negotiate with ore-like samples and plain tally board at wharf; three restrained adults sit behind under guard.','v02 rejected for English-like boat-name lettering. v03 removes lettering and adjusts official hair. Period wardrobe, repeated captive faces and full-pixel hands/chain mechanics remain held; negotiation is production invention.'),
915:('v02','Grounded brick-walled coastal city with stepped pyramids, protected harbor, oared wooden vessels and small port figures.','Removes floating terrain. Editorial Old Ghis teaser based on script later brick-pyramid description, not exact map or verified capital layout. Match city design to later Ghis originals before locking.'),
916:('v02','Bright turquoise bay with wooden sailing hulls, busy quays, intact breakwaters and inhabited hillside port against volcanic foothills.','Stronger chapter-opening commerce. Masonry reads gray blockwork rather than seamless fused black stone; architecture/reference conformity remains PARTIAL. Sunlight is intended chapter transition, but grade/set matching to 0917 needs work.'),
918:('v02','Straight smooth dark at-grade road through farm plots to coastal town, simple carts and travelers, volcanic mountains behind.','Corrects elevated causeway. Exact three-wagon width and half-foot elevation not certified; apparent road width may still need correction. Supporting buildings read generic stone cottages; architectural continuity held.')}

ledger=json.loads((audit/'EP001_SHOT_AUDIT_LEDGER.json').read_text())
assert ledger['reviewed_individually'] in (909,919)
manifest=[]
for j,(decision,observation,action) in enumerate(notes):
    num=911+j
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
    if num in (916,918):
        hold='REPLACED_PARTIAL_ARCHITECTURE_HOLD' if num==916 else 'REPLACED_PARTIAL_ROAD_CONFORM_HOLD'
        shot['audit_status']=hold
        record['selection_status']=hold
    manifest.append(record)
ledger['reviewed_individually']=919
(audit/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for row in ledger['shots'] for k in row))
with (audit/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for row in ledger['shots']:
        w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
(audit/'BATCH_092_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
summary='# Batch092 — IMG0911–0920, 30:20–30:40\n\nTen originals individually opened at display resolution, decoded and MD5 matched fresh Drive listing. Full paragraphs 30:00–30:30 and 30:30–31:00 plus next paragraph read. No new flame/sorcery emitter generated.\n\nFour replacement selections: 0913 coastal labor-supply negotiation, 0915 grounded Old Ghis brick harbor teaser instead of floating terrain, 0916 living Summer Sea harbor, 0918 at-grade road instead of raised causeway. Five generated versions inspected; 0913_v02 rejected for boat-name lettering, corrected v03 inspected.\n\nIMPORTANT: 0916 remains PARTIAL_ARCHITECTURE_HOLD because generated stonework reads block masonry rather than seamless fused black stone. 0918 remains PARTIAL_ROAD_CONFORM_HOLD: ground level is corrected but exact width/elevation is not certified and may need widening. Do not call all four corrected final masters.\n\nOriginal keep candidates: 0912, 0917, 0919. Context-only holds: 0911 shaft machinery, 0914 unidentified curved bronze object, 0920 foothill traveler. Previous selected 0910 basket labor to 0911 deep shaft is a thematic scale cut, not exact spatial continuity. New 0915 depicts Old Ghis as a brief editorial teaser, then 0916 returns to Valyria; avoid implying both cities are one location. Next matching must include actual upcoming harbor shots.\n\nSearch of connected Drive for preferred_cinematic_city, preferred_city_art, VALYRIA_ORIGINAL_PENINSULA and REFERENCE_DIRECTION filenames returned no matches. This does not establish that references do not exist elsewhere. Earlier city-reference direction remains unresolved; no new city image is reference-certified.\n\nRemaining gates: architectural style and recovered user direction, road width, boat rigging/hull anatomy, period clothing, repeated faces, chain/hands at enlarged scale, original dark harbor versus bright transition lighting, geography/location labels, timed narration. Previous IMG0885 mechanics hold remains open. Narration and baseline shot map unchanged; no audio retiming verified.\n\nProgress: 919/1050 original slots reviewed; zero final approvals. Five generated versions inspected this pass. IMG0500 remains inherited missing/unresolved. Next Batch093 IMG0921–0930 completes the first Chapter VII paragraph: capes, Isle of Cedars, harbor trade and metalwork.\n'
(audit/'BATCH_092_REVIEW.md').write_text(summary)
page=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Batch092 audit and corrections</title><style>body{background:#17191c;color:#eee;font:18px system-ui;max-width:1300px;margin:30px auto;padding:24px}img{width:100%}p{line-height:1.5}article{margin:70px 0}</style><h1>Batch092 — individual audit and corrections</h1><p>30:20–30:40. Four replacement selections including two partial holds; three keep candidates and three context holds. No final approvals.</p>']
for row in manifest:
    name=row['scene_id']+'.png'
    page.append('<article><h2>'+row['scene_id']+'</h2><h3>Original</h3><img src="originals/'+name+'" alt="Preserved original"><p>'+html.escape(row['original_observation']+' '+row['action'])+'</p>')
    if 'replacement_md5' in row:
        page.append('<h3>Selected provisional replacement</h3><img src="replacements/'+Path(row['selected_file']).name+'" alt="Inspected replacement"><p>'+html.escape(row['replacement_observation']+' '+row['replacement_limitations'])+'</p>')
    page.append('</article>')
page.append('</html>')
out=Path('.recovery/batch092');out.mkdir(parents=True,exist_ok=True)
preview=out/'BATCH_092_INDIVIDUAL_AUDIT.html';preview.write_text('\n'.join(page))
package=Path('google_drive/EP001_BATCH_092_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
    z.write(preview,preview.name)
    for n in ['BATCH_092_REVIEW.md','BATCH_092_MANIFEST.json','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv']:
        z.write(audit/n,n)
    for row in manifest:
        name=row['scene_id']+'.png';z.write(Path('google_drive')/name,'originals/'+name)
        if 'replacement_md5' in row:
            p=Path(row['selected_file']);z.write(p,'replacements/'+p.name)
    z.write(assets/'VAL-EP001-IMG0913_v02.png','rejected_evidence/VAL-EP001-IMG0913_v02.png')
print(package,package.stat().st_size,hashlib.md5(package.read_bytes()).hexdigest())
