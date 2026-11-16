"""Batch102 native audit and explicitly versioned correction selections."""
import csv,hashlib,json,zipfile
from pathlib import Path
from PIL import Image
A=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/audit');P=Path('.recovery/batch102_prior');D=Path('google_drive/batch102')
md=lambda p:hashlib.md5(p.read_bytes()).hexdigest()
z=Path('google_drive/EP001_BATCH_102_REVIEW_BACKUP.zip');assert z.stat().st_size==42335220 and md(z)=='a2af8e4ca0b824da3ba8637fa0aa4c23'
prior=json.loads((P/'06_BATCH_102_MANIFEST.json').read_text());ledger=json.loads((A/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==1009
notes=[
('REPLACED_PARTIAL_ARCHITECTURE_HOLD','Mist-veiled dark city of domes, slender towers, bridges and stone dragon-head ornaments; thin top bar in original.','Framing-only v02 removes bar proportionally. Statues are not live dragons. Dome/spire language, visible surface joints and continuity to Batch101 remain unapproved.'),
('REPLACED_PARTIAL_ARCHITECTURE_HOLD','Empty organic arch frames dark recess and dormant distant mountain. Original has rectangular horizontal joints.','Generated v02 removes prominent block joints and top bar, adds continuous mineral ribs. Some cracks/ledge seams remain; fused-material and reference conformity held. No historical event depicted.'),
('REPLACED_PARTIAL_FRAMING_ARCHITECTURE_HOLD','Empty carved flowing terrace leads to tower foot; deep city and mountains beyond. Original has heavy letterbox bars.','Framing-only v02 removes bars using proportional centered source-box crop. Tighter composition loses about 10.16% of active-image width, not a content regeneration. Chipped balustrade, joints and urban style remain held.'),
('KEEP_CONTEXT_ONLY','Tall patterned dark tower on circular balcony above green empty basin, walled complex behind.','Context for present marvel, not literal hatchery. Background blocky fortress and joints need style/reference conformity. No dragon hatching asserted.'),
('KEEP_CONTEXT_ONLY','Elevated view of dormant cones extending along coast, isolated ornate complex at lower right.','Geographic context, not exact fourteen count or approved map. Architecture is small and isolated, not city-wide reference proof; no prehistoric origin certified.'),
('REPLACED_PARTIAL_ARCHITECTURE_HOLD','Low-angle dark tapering ribbed tower, green ledges and gray sky; original infill visibly coursed.','Generated v02 replaces infill blocks with smooth flowing fused-looking surfaces. New ground still has straight seam-like lines; retain architecture/grade hold, no blanket defect clearance.'),
('KEEP_CONTEXT_ONLY','Glossy black folded glassy material exposed in chipped gray architectural relief, pale lichen beside it.','Material metaphor, not confirmed dragon fossil, egg or magical evidence. Obsidian-like reflectivity is not emission. Chipped/weathered appearance and style continuity remain held.'),
('REPLACED_PARTIAL_ARCHITECTURE_HOLD','Empty shadowed asymmetric opening with flowing smooth rim and lattice-like dark ribs. Original has thin top/bottom bars.','Framing-only v02 removes bars proportionally. Empty aperture avoids asserting Asshai masters really taught binding. Decorative style/material and camera continuity remain held.'),
('KEEP_CONTEXT_ONLY','Extreme close-up rough dark mineral folds beside narrow unlit fissure.','Abstract whisper/unknown-history insert, not writing or verified spell. No glow at display resolution; does not prove literal binding.'),
('REPLACED_PARTIAL_ARCHITECTURE_HOLD','Coastal urban panorama, bridge to monumental tower, gardens and dormant mountains. Original laid-block bridge and conventional stacked towers.','Generated v02 makes bridge and major towers continuous sculptural fused-looking forms. Smaller masonry-like buildings persist and main glossy organic style differs from earlier pair; partial improvement only, architectural continuity held. No literal Asshai scene implied.')]
records=[]
for j,old in enumerate(prior['records']):
 n=1011+j;original=P/'native'/f'VAL-EP001-IMG{n}.png';assert md(original)==old['md5'] and original.stat().st_size==old['bytes']
 with Image.open(original) as im:im.load();assert list(im.size)==old['dimensions']
 gen=n in (1012,1016,1020);crop=n in (1011,1013,1018)
 selected=D/f'VAL-EP001-IMG{n}_v02{ "_framing" if crop else ""}.png' if gen or crop else original
 with Image.open(selected) as im:im.load();dims=list(im.size)
 status,obs,action=notes[j];s=ledger['shots'][n-1];assert s['scene_id']==old['scene_id']
 s.update(audit_status=status,drive_file_id=None,source_archive_drive_id='1msfairY9MfoUQ7xD4oxkR1N5vz9ZVt9I',original_local_file=str(original),selected_local_file=str(selected),replacement_file=str(selected) if gen or crop else None,visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md(original),selected_md5=md(selected),reviewed_on='2026-11-15',review_scope='Ten originals, three generated corrections and three framing derivatives individually viewed at returned display resolution; decoded. Archive MD5 matched Drive metadata and native originals matched recovered manifest. No all-pixel/reference conformity, timing or final approval.')
 r=dict(s,selected_dimensions=dims,selected_bytes=selected.stat().st_size,correction_type='AI edit' if gen else 'proportional source-box crop/LANCZOS' if crop else 'none')
 if crop:
  t,b={1011:(11,768),1013:(39,729),1018:(12,756)}[n];w=(b-t)*1376/768;x=(1376-w)/2;r['source_box']=[x,t,1376-x,b];r['original_canvas_area_removed_percent']=100*(1-w*(b-t)/(1376*768))
 records.append(r)
ledger['reviewed_individually']=1019;assert not any(s['final_accepted'] for s in ledger['shots'])
(A/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (A/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(A/'BATCH_102_MANIFEST.json').write_text(json.dumps(records,indent=2)+'\n')
report='''# Batch102 — IMG1011–1020 (33:40–34:00)

**1019/1050 reviewed, zero final approvals.** Ten recovered originals individually viewed. Three AI correction versions generated and inspected (1012,1016,1020); three framing-only derivatives created and inspected (1011,1013,1018). All six selected provisionally with holds, not final delivery acceptance. All originals preserved.

## Provenance / context

Backup Drive ID 1msfairY9MfoUQ7xD4oxkR1N5vz9ZVt9I, 42,335,220 bytes, MD5 a2af8e4ca0b824da3ba8637fa0aa4c23 matched metadata. All ten native byte sizes, dimensions and hashes match recovered first-pass manifest. Backup generated-review-pending status is not approval. No independent Drive IDs claimed for enclosed PNGs.

Recovered manifest records preference for cinematic city in Screenshot (105).png and architectural improvisation, not literal book reproduction. That reference/crop itself is not in this backup and remains unrecovered; no exact style match asserted. This reinforces rather than clears broader urban-design continuity holds, including Batch101 and older city imagery.

Read complete 33:30–34:00 narration and following ending context. Narration explicitly says history cannot prove whether dragons originated only in Fourteen Flames or elsewhere, or whether Asshai masters taught binding. Empty city, geology and shadow inserts preserve uncertainty rather than fabricating a witnessed hatching or spell lesson. No new dragons, people, magic/fire emitters, script edits or audio/timeline timing claims. Stone dragon ornaments in1011 are not live creatures.

## Corrections and limits

AI edits address prominent masonry courses in1012/1016 and bridge/tower construction in1020. Inspected results improve primary surfaces, but cracks, smaller block-like architecture, grade and style differences persist: all retain partial architecture holds. They are selections, not a claim that every defect has been resolved.

Framing derivatives remove baked black bars without stretching: centered source-box crops retaining original aspect followed by proportional LANCZOS to1376×768. Source boxes are recorded in manifest. 1013 requires a substantial ~10.16% trim of active-image width; tighter crop accepted only provisionally, original preserved. 1011/1018 trims are smaller. These are technical framing changes, not newly generated content. No full ten-shot delivery certification implied; native edit sizes recorded individually.

## Individual decisions

'''
for s in records:report+=f"### {s['scene_id']} — {s['audit_status']}\n\n{s['visual_observation']}\n\n{s['editorial_action']}\n\n"
report+='''## Remaining gates / next

Full-pixel QC, actual preferred reference recovery, fused architecture, urban geography and grade consistency remain open. Repeated empty-city inserts may need pacing review against actual audio; no timed edit performed. IMG0500 inherited missing and all older holds persist. Next Batch103 IMG1021–1030 begins34:00–34:30 marvel/terror recap; inspect existing revisions before generating and read whole paragraph including later bondage/dragon material. Do not rerun earlier builders out of sequence.
'''
(A/'BATCH_102_REVIEW.md').write_text(report)
out=Path('google_drive/EP001_BATCH_102_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as f:
 for p in (P/'native').glob('*.png'):f.write(p,'recovered_prior/native/'+p.name)
 f.write(P/'06_BATCH_102_MANIFEST.json','recovered_prior/06_BATCH_102_MANIFEST.json')
 for p in D.glob('*.png'):f.write(p)
 for p in [A/'BATCH_102_MANIFEST.json',A/'BATCH_102_REVIEW.md',A/'EP001_SHOT_AUDIT_LEDGER.json',A/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:f.write(p)
print(out,out.stat().st_size,md(out))
