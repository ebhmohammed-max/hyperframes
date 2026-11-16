"""Record Batch091 individual visual review and selected script-alignment corrections."""
import csv
import hashlib
import html
import json
from pathlib import Path
import zipfile
from PIL import Image

root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
audit=root/'audit'
assets=Path('assets/episode_audit/batch091')
ids=['1YqpyvX4xojcT5w6flCNjZLmzsK6GQ0Cu','1GfMIj9_VTk6f3V-WWNdKirgh7DN3RKy0','1NjtA8GKSDamoGB6bJ6LyXB-MuLuJRGwf','1K6OSF0P7ZybMkcIN42JCeDgQVpS-gIfx','10_zsmOYFJrR-uGkTadGK6xgAaDcI_ggQ','1DX7q09JyRViWzfasSWS-uJI-JnH7gEbT','1BRdUezJLU1e7Z_n9rugSRO372wwfUWt_','1IKCNiNHLJcwVC6IaNs_hZKxGr4gRz-1y','11EJHwgx2tdcBbpbFw0fGlWe400-RCkqU','17nVnxjvlhesxi_-P_xFi3QZIrDHimApA']
checks=['8fa17fa463d540060555779ab5641c59','4cb14a12b50185391d1e49094583884c','1a5f29eb8981c62a85a5598f8cf8b515','172c32dcd62e20d250f6c30f72a5d2ac','02eca2dabef4e54dbc1f3db662496b29','bb3d662ebd2b4bb969e6be3895b51b6f','71bdbfa51df87f42549f90bec960d003','a6abb01381e6ab9783039e965d44da1e','dab56ffacbb8f96c9625bd3cf3449218','7db8e3a1b8a3d693b0803f07bd3b7b51']
notes=[
('KEEP_CONTEXT_ONLY','Tall jagged dark spires rooted into rock, small queue leading to low opening under gray sky.','Can bridge preceding labor arrival into bedrock metaphor; by itself not a prosperous city. Keep only as brief contrast context, not another city establishing shot.'),
('KEEP_CANDIDATE','Over-shoulder pale-haired black-robed observer looks toward terraced rocky mine with workers, entrances and timber structures.','Useful elite-versus-labor scale contrast before rise above. Individual captivity and exact geometry not certified at this distance.'),
('REPLACE','Isolated jagged dark castle-like rock formation by coast under gray sky, few tiny figures near base.','Third bleak spire view delays living commonwealth. Replace with visibly inhabited urban stonework rooted in bedrock.'),
('REPLACE','Broad dark peaked geological mass above white clouds; few legible doors or inhabitants.','Clouds match text but inhabited civilization unclear. Replace with occupied upper towers above low clouds.'),
('REPLACE','Single pale-haired adult in blue embroidered robe and jewelry poses against gray coastal sky.','Another noble portrait does not establish shining commonwealth or civic life. Replace with citizens and trade in intact urban arcade.'),
('KEEP_CANDIDATE','Many pale-haired adults sit and stand around open circular polished black hall, tall columns and metal stands.','Supports assembly without an obvious crowned ruler. Central tall seat may read as privileged chair; do not claim exact forty-house count or that scene proves republican equality.'),
('REPLACE','Two near-identical pale-haired figures with dark cracked stone-like facial texture face each other beside rectangular black pedestal.','Unintended nonhuman skin and duplicated identities undermine human noble assembly. Replace with differentiated human delegates debating.'),
('KEEP_CANDIDATE','Two pale-haired adults converse near black table between colossal human-faced scaled winged stone creatures; vines hang beyond.','Supports debate amid sphinx-like sculpture. Full crouched-dragon morphology, eye material and garden continuity need enlarged/sequence review; no new emitted eye light inferred.'),
('REPLACE','Long cliff path with tiny procession above large dark holes and pale plumes, sparse vines on rock.','No legible maintained hanging gardens; image returns below too early. Replace with inhabited planted civic terraces.'),
('REPLACE','Aerial barren mined landscape with pits and winding tracks; remote city-like silhouette appears above low cloud on horizon.','Vast exterior panorama weakens bodily cost under sandals and risks floating-city reading. Replace with chained labor inside cramped mine.')]
replacements={
903:('v02','Busy coastal avenue amid intact dark towers, domes, arches and gold/bronze trim; many small residents and market stalls.','Clearer living civilization. Architecture mixes domes and tower styles; not yet matched to recovered user-preferred city references. Distant anatomy/windows need inspection; city design remains provisional.'),
904:('v02','Occupied dark curved towers with balconies and muted bronze domes rise above low cloud, sea and lower city visible.','Built inhabited towers clearer than geology. Matching exact city layout to 0903 and previous chapters remains unverified; no floating-landmass claim.'),
905:('v02','Silver-haired woman examines worked object offered by dark-haired artisan in busy dark-stone arcade; other adults converse.','Shows civic trade instead of portrait. Some tailored garments read later-period; wardrobe continuity held. Supporting residents need not all be assumed nobles or one ethnicity.'),
907:('v02','Five distinct human delegates in differentiated dark/plum robes around shared table, two exchanging gestures, simple tablets before them.','Normal skin and distinct identities improve assembly beat. Physical set/wardrobe continuity with original 0906 and 0908 remains held; tablets are unmarked, not readable laws.'),
909:('v02','Maintained terraced dark-stone balconies with cascading plants, flowers and residents overlooking coastal city.','Readable hanging gardens. Brighter sun and lighter distant buildings differ from surrounding cool palette; grade and architectural continuity held. No identity assumed for conversing pair.'),
910:('v03','Two exhausted differentiated adults haul ore basket through timber-braced tunnel; foreground wrist cuff and short chain visible.','v02 rejected for near-repeated worker faces; v03 changes background to bald gray-bearded adult. Hand/basket grip, chain attachment and full-pixel anatomy remain held. Contrast with above-ground gardens now explicit.')}

ledger=json.loads((audit/'EP001_SHOT_AUDIT_LEDGER.json').read_text())
assert ledger['reviewed_individually'] in (899,909)
manifest=[]
for j,(decision,observation,action) in enumerate(notes):
    num=901+j
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
ledger['reviewed_individually']=909
(audit/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for row in ledger['shots'] for k in row))
with (audit/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for row in ledger['shots']:
        w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items()})
(audit/'BATCH_091_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
summary="# Batch091 — IMG0901–0910, 30:00–30:20\n\nTen originals individually viewed at tool display resolution, decoded and native MD5s matched to fresh Drive listing. Full 30:00–30:30 narration paragraph and prior paragraph read before review. No new flame/sorcery/emitter treatment generated.\n\nSix script-alignment replacements selected provisionally: 0903 living city street, 0904 occupied towers above low cloud, 0905 civic trade, 0907 differentiated human assembly, 0909 maintained hanging gardens, 0910 chained underground basket labor. Seven generated versions individually inspected; 0910_v02 rejected for near-repeated worker faces and v03 selected after differentiation.\n\nThree original keep candidates (0902, 0906, 0908), one context-only bridge (0901). Current selected 0900 basket distribution to 0901 rocky queue is thematically compatible as labor-arrival context, not established exact geography or identity continuity. Original 0906 central chair must not be presented as a king; 0908 sphinx-like sculptures still require full morphology review.\n\nThe revised sequence makes the above/below contradiction more legible, rather than repeating barren rock formations and noble portraits. New architecture is not verified against old agent's user-preferred city reference files. Domes, towers and civic sets need cross-shot/cross-chapter matching; 0905 wardrobe reads later-period in places, 0909 is brighter and its distant city lighter. These are substantive continuity holds, not passed masters. Human faces and garden occupants are production invention, not named canonical people.\n\nNo script or baseline shot-map changes. All originals retained, rejected candidate separated, versioned replacement selection in cumulative ledger and manifest. Remaining gates: architecture/reference direction, wardrobe, grade, assembly/sphinx identity, full-pixel hands/chain/basket mechanics and timed narration. Previous IMG0885 partial lifting-mechanics hold remains open.\n\nProgress: 909/1050 original slots reviewed; zero final delivery approvals. Seven new generated versions inspected. IMG0500 remains inherited missing/unresolved. Next Batch092 IMG0911–0920 crosses into Chapter VII at 30:30; read both complete narration paragraphs and check actual opening frame against selected 0910.\n"
(audit/'BATCH_091_REVIEW.md').write_text(summary)
page=['<!doctype html><html lang="en"><meta charset="utf-8"><title>Batch091 audit and corrections</title><style>body{background:#17191c;color:#eee;font:18px system-ui;max-width:1300px;margin:30px auto;padding:24px}img{width:100%}p{line-height:1.5}article{margin:70px 0}</style><h1>Batch091 — individual audit and corrections</h1><p>30:00–30:20. Six provisional replacements, three keep candidates, one context hold. No final approvals.</p>']
for row in manifest:
    name=row['scene_id']+'.png'
    page.append('<article><h2>'+row['scene_id']+'</h2><h3>Original</h3><img src="originals/'+name+'" alt="Preserved original"><p>'+html.escape(row['original_observation']+' '+row['action'])+'</p>')
    if 'replacement_md5' in row:
        page.append('<h3>Selected provisional replacement</h3><img src="replacements/'+Path(row['selected_file']).name+'" alt="Inspected replacement"><p>'+html.escape(row['replacement_observation']+' '+row['replacement_limitations'])+'</p>')
    page.append('</article>')
page.append('</html>')
out=Path('.recovery/batch091');out.mkdir(parents=True,exist_ok=True)
preview=out/'BATCH_091_INDIVIDUAL_AUDIT.html';preview.write_text('\n'.join(page))
package=Path('google_drive/EP001_BATCH_091_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(package,'w',zipfile.ZIP_DEFLATED) as z:
    z.write(preview,preview.name)
    for n in ['BATCH_091_REVIEW.md','BATCH_091_MANIFEST.json','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv']:
        z.write(audit/n,n)
    for row in manifest:
        name=row['scene_id']+'.png';z.write(Path('google_drive')/name,'originals/'+name)
        if 'replacement_md5' in row:
            p=Path(row['selected_file']);z.write(p,'replacements/'+p.name)
    z.write(assets/'VAL-EP001-IMG0910_v02.png','rejected_evidence/VAL-EP001-IMG0910_v02.png')
print(package,package.stat().st_size,hashlib.md5(package.read_bytes()).hexdigest())
