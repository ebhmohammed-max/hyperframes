"""Record Batch089 individual visual review and selected script-alignment corrections."""
import csv
import hashlib
import html
import json
from pathlib import Path
import zipfile
from PIL import Image

root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
audit=root/'audit'
assets=Path('assets/episode_audit/batch089')
ids=['1pZvcFXhmlcNEAlcP7MRvricle9HnD4ZR','1l_nirCYBy49-5Baozanzmb_UTLuHurGC','1rsKza0YNFplnUfXVAvhwdc74m6mYXLIg','1YYyNPo4XQU7xPzX3s8KsUBKyzdM5rLeB','1Py3Dq8SdjaQV5_oG8CdXi46rnjl5rA3Q','1QiSEZpAfNpllVO-6Y2qObtxleoVJgZEp','1sM78LAhYbRm5UyX_1i7KwWfteEiEH91G','10AM5rRkb_s4aDu1Qe_B1ltEOMbP6kQt-','1XxmJ_B4AE-H_AlUJIQRk5gT4pzall2VC','193vZiBahoPzt22ZehJvbvSr92ld8Y-x5']
checks=['05e4683968e62b7665ddbc7bf7ce37e1','02810bb3ae7f17c8d97f51762ae25391','6d7a6e994392354c9e7a6ea617f4081f','131fbfbc9c6c61a9fe61e241d9a17454','1cef8424721541c09fb4dd401dc2c868','d6431124789465f8191e10d2f24d6540','1d87f77424e821a8d977216f9f34d4c4','14452d565f31993b62ccdc88abd161e8','7a82bc2519e2686c994116616fbd28b6','7de9cb2066d74133390aa88b093b09e4']
notes=[
('KEEP_CANDIDATE','Two ragged miners with tools at metallic-looking rock in a steep shaft; more figures, ladder and suspended basket above.','Supports ore extraction and forced labor. Mineral identity, chain connections and lifting mechanics not certified. Original orange fissure observed, not authorization for new glow.'),
('KEEP_CANDIDATE','Close texture of pale crystalline vein with gold/copper-colored inclusions in dark stone.','Useful material detail. Mineral assay and rock temperature cannot be inferred from image.'),
('REPLACE','Close face of head-wrapped bearded adult, slight smile, hand near rock at left edge.','Calm portrait weakens heat-danger beat; replace with concerned withdrawn-hand reaction.'),
('KEEP_CANDIDATE','Four dirt-covered hands grip coarse rope above ore-filled woven basket; frayed cloth wraps at wrists.','Clear exertion detail for hoisting. Hands and rope crossings require enlarged inspection; no claim that wrist wraps are iron shackles.'),
('REPLACE','Two pale-haired black-robed figures stand by huge open-air pit; long line of figures descends edge.','Exterior pit breaks subterranean hoist progression and unclear unsafe geometry distracts. Replace with basket in shaft.'),
('REPLACE','Chained queue enters very tall dark opening between two pale-haired black-robed figures.','Repeats arrival imagery instead of escalating tunnel danger. Replace with abandoned tools and ominous depth.'),
('KEEP_CANDIDATE','Over-shoulder view down long dark tunnel, narrow pale plume at right wall and distant figures.','Useful existing hazard foreshadowing. Plume temperature, pressure and chemistry not visually established; no new emitter treatment inferred.'),
('REPLACE','Kneeling restrained queue between pale-haired figures; low haze and two distant hunched figures before orange line.','Static guard-led arrangement weakens sudden danger. Use indirect non-graphic reaction under separately documented treatment ruling; literal red-steam depiction remains held.'),
('REPLACE','Huge glossy honeycomb-like cavern, many rounded apertures, low greenish haze and hanging chain; over-shoulder foreground.','Over-stylized alien cavern disrupts recognizable mine geography. Replace with rough working tunnel and indirect dangerous-air aftermath.'),
('KEEP_CANDIDATE','Two adults support a sagging central adult beside dark doorway; pale-haired black-clothed observer at right and pale low haze.','Communicates collapse and assistance without requiring gore. Does not prove death or identify gas. Continuity from new 0889 remains provisional.')]
replacements={
883:('v03','Concerned crouching miner examines an open hand drawn back near chest away from rock; pick against wall.','v02 rejected because hand still touched stone. v03 improves reaction. No burn shown and temperature implied only by narration; full-pixel hand anatomy remains held.'),
885:('v03','Ore-filled woven basket suspended in deep basalt shaft, vertical rope above and tail below, ladder on wall.','v02 rejected for unclear separation of hauling rope from basket. v03 simplifies view and conveys depth; basket support attachment and rope mechanics still require a close inspection and remain PARTIAL, not a final master. Small borders need conform.'),
886:('v02','Abandoned pick, tipped basket and loose chain in foreground of dark working tunnel, two small figures far behind.','Ominous bridge into dangerous paragraph without repeating entrance. Suggests danger rather than asserting those figures dead.'),
888:('v02','Two crouching miners recoil with raised arms and cloth, dense neutral pale vapor behind.','Indirect reaction treatment: no emitted jet, red glow or injured bodies. Does not literally depict red steam or establish boiling; narration carries severity. Hand/arm anatomy and repeated reaction rhythm need final review.'),
889:('v02','Timber-braced rough tunnel with fallen pick, basket, spilled rocks and low gray haze; distant adult supports another.','More coherent working-mine aftermath than honeycomb architecture. Gas chemistry and lethality not established from haze. Small baked-in borders and similarity to 0886 need conform/pacing review.')}

ledger=json.loads((audit/'EP001_SHOT_AUDIT_LEDGER.json').read_text())
assert ledger['reviewed_individually'] in (879,889)
manifest=[]
for j,(decision,observation,action) in enumerate(notes):
    num=881+j
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
    if num == 885:
        shot['audit_status']='REPLACED_PARTIAL_MECHANICS_HOLD'
        record['selection_status']='PARTIAL_MECHANICS_HOLD'
    manifest.append(record)
ledger['reviewed_individually']=889
(audit/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for row in ledger['shots'] for k in row))
with (audit/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for row in ledger['shots']:
        w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
(audit/'BATCH_089_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
summary='# Batch089 — IMG0881–0890, 29:20–29:40\n\nTen originals individually viewed at tool display resolution, decoded and MD5 matched against fresh Drive metadata. Both full 29:00–29:30 and 29:30–30:00 narration paragraphs read before review.\n\nFive replacement slots: 0883 withdrawn-hand heat reaction, 0885 basket in shaft, 0886 abandoned tools/tunnel danger, 0888 indirect steam-hazard reaction, 0889 recognizable mine aftermath. Seven generated versions individually viewed, five selected provisionally. Two rejected versions preserved: 0883_v02 still touched rock; 0885_v02 had unclear hauling mechanics. IMG0885_v03 remains PARTIAL because basket support/rope mechanics need close inspection; this is not a final master.\n\nFive originals retained as keep candidates: 0881, 0882, 0884, 0887 and 0890. None is finally approved. The revised sequence keeps extraction, material detail and exertion, then turns toward danger and collapse. Original 0881 is compatible in subject with preceding selected IMG0880, but identity, lighting and exact cut still require continuity review.\n\nTreatment ruling written before prompts: no new flame, lava, luminous fissure, red magical light or explicit vent jet generated/selected. 0888 is an indirect neutral-vapor reaction, NOT a literal visualization of red steam boiling people. That literal treatment stays held. 0889 low haze is not chemical identification. No new firewyrm treatment authorized by this pass. Script and baseline shot map unchanged.\n\nRemaining gates: 0885 lifting mechanics; small borders on 0885/0889; hand/tool/chain anatomy at enlarged resolution; repeated reaction/abandoned-tool motifs; visual identity and grade continuity; timed narration. All replacements are production reconstructions, not canonical documentation.\n\nProgress: 889/1050 original slots reviewed; zero final delivery approvals. Seven generated versions inspected this pass. Missing IMG0500 remains unresolved. Next Batch090 IMG0891–0900 includes firewyrm span; inspect originals and resolve per-span treatment before any new emitter imagery.\n'
(audit/'BATCH_089_REVIEW.md').write_text(summary)
page=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Batch089 audit and corrections</title><style>body{background:#17191c;color:#eee;font:18px system-ui;max-width:1300px;margin:30px auto;padding:24px}img{width:100%}p{line-height:1.5}article{margin:70px 0}</style><h1>Batch089 — individual audit and corrections</h1><p>29:20–29:40. Five provisional replacements including one partial mechanics hold; five keep candidates. No final approvals.</p>']
for row in manifest:
    name=row['scene_id']+'.png'
    page.append('<article><h2>'+row['scene_id']+'</h2><h3>Original</h3><img src="originals/'+name+'" alt="Preserved original"><p>'+html.escape(row['original_observation']+' '+row['action'])+'</p>')
    if 'replacement_md5' in row:
        page.append('<h3>Selected provisional replacement</h3><img src="replacements/'+Path(row['selected_file']).name+'" alt="Inspected replacement"><p>'+html.escape(row['replacement_observation']+' '+row['replacement_limitations'])+'</p>')
    page.append('</article>')
page.append('</html>')
out=Path('.recovery/batch089');out.mkdir(parents=True,exist_ok=True)
preview=out/'BATCH_089_INDIVIDUAL_AUDIT.html';preview.write_text('\n'.join(page))
package=Path('google_drive/EP001_BATCH_089_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
    z.write(preview,preview.name)
    for n in ['BATCH_089_REVIEW.md','BATCH_089_TREATMENT_RULING.md','BATCH_089_MANIFEST.json','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv']:
        z.write(audit/n,n)
    for row in manifest:
        name=row['scene_id']+'.png';z.write(Path('google_drive')/name,'originals/'+name)
        if 'replacement_md5' in row:
            p=Path(row['selected_file']);z.write(p,'replacements/'+p.name)
    for name in ['VAL-EP001-IMG0883_v02.png','VAL-EP001-IMG0885_v02.png']:
        z.write(assets/name,'rejected_evidence/'+name)
print(package,package.stat().st_size,hashlib.md5(package.read_bytes()).hexdigest())
