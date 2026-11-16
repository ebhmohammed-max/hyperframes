"""Persist Batch094 individually inspected originals and provisional corrections."""
import csv, hashlib, json, zipfile
from pathlib import Path
from PIL import Image
root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
a=root/'audit'; assets=Path('assets/episode_audit/batch094')
ids=['1u-U4RQo-ON_u7xtJ7mpzYEp5YoOf9GCj', '12jIz3z68Zkp0F-kTbXx4hDgiYzyN8pfV', '18buxFYHGrLc61XFHHOFesoGi-gFONnq5', '1Rkt79nO-1blWIDb67HVksGfAYZ-fnGQg', '1h3fly9BH5fR-9qsrs5NdIybMUnmkYyN5', '13_4v9cMmtdFskfFPi3vHtDgMT2F-fdMX', '1VnWu-3USapxBSQu_bFFbk2udkrPZEuWP', '1gY5A_KFfx6uq_mb9ONRy0l2sTu2Nbuz9', '1vgO5AgdZ25HwDvLnHbQnRG4ys_FeJf_J', '10ETD4L5Px6BZcZLv1fw6DwyUBUydkU85']
checks=['7be13a0e8ccfce1a1e3a7cb287f10f95', '3e82dbad4bcde6dbec6ba6f81d9c1d73', '7b0913a88156684706ccd6820606fe35', '5e3cacb47649b97600ee3dec7a448a86', '00c29fe0a02a311f7071d794e5ffedbd', 'aa741aa1391c56fba4e0e3724a56cb77', '0588488a9e24c137bc93435ca3eaba3e', '63eb5da4dbcdf0278bd7bfb4bf85242f', '04da5d8922c9d498effbb9bb295a60a4', 'af643ede9763e3f129bfafb0c1c92562']
notes=[('KEEP_CONTEXT_ONLY', 'Weathered cloaked adult on timber landing with sea and distant volcanic silhouette.', 'Supports returning traveler; profession and actual voyage unverified. Not same proven mariner as other shots.'), ('KEEP_CANDIDATE', 'Two adults converse at open harbor-side table with sealed scroll, cup and bread.', 'Supports report exchange. Scroll is invented prop, not canonical dispatch; distant lighthouse and ship design unverified.'), ('KEEP_CANDIDATE', 'Standing adult gestures to crowded seated tavern listeners beside harbor windows.', 'Directly supports spreading reports. Hands/repeated faces and costume continuity not certified at all pixels.'), ('KEEP_CONTEXT_ONLY', 'Two plain-clothed adults stand before rows of seated listeners in stone hall.', 'Can stand for a foreign court hearing, not identified monarch, named court or Valyrian royal institution. Valyria remains kingless.'), ('KEEP_CANDIDATE', 'Bearded adult gestures while speaking in tavern close-up.', 'Narrator reaction/cutaway over start of tower description; full paragraph supports this, not a literal tower shot. Speaker identity does not match all other tavern men.'), ('REPLACE', 'Cluster of enormous jagged black rock needles by misty water without obvious inhabited architecture.', 'Natural-looking pinnacles fail built tower description; replace with visibly inhabited architectural towers.'), ('KEEP_CANDIDATE', 'Detail of long silver hair, pale woven shoulder and dark metal neck ring.', 'Supports silver-haired description; costume/metal provenance invented. No need to add literal flame to every word fragment.'), ('KEEP_CANDIDATE', 'Silver-haired adult pair in gray drapery and dark scale shoulder ornaments in colonnade.', 'Supports lords and ladies; violet-looking irises visible, not overtly emissive at display resolution. Named identity, wardrobe and set match remain unverified.'), ('REPLACE', 'Numerous silver-haired figures in monumental hall; some foreground eyes appear bright luminous purple.', 'Unmotivated emissive eyes overstates plum-colored irises and repeats assembly imagery; replace with natural-eye noble portrait.'), ('REPLACE', 'Coastal farmland and tiled rooftops beneath tiny bird-like flying marks.', 'Flying forms cannot establish winged leviathans; replace with readable dragon above volcanic pasture.')]
repl={936: ('Three towering inhabited dark structures with windows, balconies and flowing buttresses above civic paths.', 'Built-tower defect corrected. Gothic ornament and visible blockwork on side buildings remain PARTIAL_ARCHITECTURE_HOLD; main tower surfaces more continuous. City direction not recovered.'), 939: ('Silver-haired adult noblewoman with muted dark plum-looking irises, ordinary pupils and no visible eye glow; blurred adult behind.', 'Removes overt emissive eyes. Different person/wardrobe from 0938: use as another noble, not exact reverse-angle match. Iris hue and skin/grade conform remain provisional.'), 940: ('Single clearly winged reptilian silhouette over green grazing land and distant volcanic mountain.', 'Selected v03 replaces v02, whose foreground creature had ambiguous folded membrane/body anatomy. v03 reads as winged reptile with two visible wings, legs and tail; flight pose, scale, full anatomy and creature-reference match remain PARTIAL_CREATURE_HOLD. Still cannot establish circling motion or plural dragons by itself.')}
ledger=json.loads((a/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==929
manifest=[]
for j,(status,obs,action) in enumerate(notes):
 n=931+j; p=Path(f'google_drive/VAL-EP001-IMG{n:04d}.png'); md=hashlib.md5(p.read_bytes()).hexdigest(); assert md==checks[j]
 with Image.open(p) as im: im.load(); dims=list(im.size)
 s=ledger['shots'][n-1];assert s['scene_id']==p.stem
 s.update(audit_status=status,drive_file_id=ids[j],selected_local_file=str(p),original_local_file=str(p),visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md,reviewed_on='2026-11-15',review_scope='Individually opened at tool display resolution, decoded and MD5 matched; no audio timing or all-pixel anatomy certification.')
 if n in repl:
  rp=assets/f"{p.stem}_{'v03' if n==940 else 'v02'}.png"
  with Image.open(rp) as im:im.load();rd=list(im.size)
  s.update(audit_status=('REPLACED_PARTIAL_ARCHITECTURE_HOLD' if n==936 else 'REPLACED_PARTIAL_CREATURE_HOLD' if n==940 else 'REPLACED_PROVISIONAL'),selected_local_file=str(rp),replacement_file=str(rp),replacement_md5=hashlib.md5(rp.read_bytes()).hexdigest(),replacement_dimensions=rd,replacement_observation=repl[n][0],replacement_review=repl[n][1])
 manifest.append(dict(s,native_dimensions=dims,native_bytes=p.stat().st_size))
ledger['reviewed_individually']=939
(a/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (a/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(a/'BATCH_094_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
report="""# Batch094 — IMG0931–0940 (31:00–31:20)

Ten originals individually viewed, decoded and matched to Drive MD5. Four generated versions individually viewed, three selected. 939/1050 slots reviewed; zero final approvals.

## Full paragraph context (31:00–31:30)

Sailors spread reports to harbor taverns and royal courts of Essos: seamless black towers, silver-haired lords and ladies with plum-colored eyes, dragons circling volcanic peaks. Across the Gulf of Grief an empire listens with displeasure. This batch covers the reports and wonders; the paragraph continues through IMG0945. Preceding paragraph concerns maritime trade; next introduces Old Ghis and its brick pyramids. Script and shot map unchanged, no timed edit or audio timing verified.

## Individual decisions

"""
for s in manifest:
 report+=f"### {s['scene_id']} — {s['audit_status']}\n\nObserved original: {s['visual_observation']}\n\n{s['editorial_action']}\n\n"
 if s.get('replacement_observation'):report+=f"Selected replacement: {s['replacement_observation']}\n\nRemaining hold: {s['replacement_review']}\n\n"
report+="""## Remaining gates

0936 architecture and 0940 creature conformity remain explicit PARTIAL holds. 0939 selected provisionally, not a certified identity match. 0940_v02 rejected and preserved: ambiguous folded wing/body silhouette; v03 chosen for clearer extended-wing read. Creature pose/anatomy still held, and one still does not prove circling motion. No new flames or luminous magic. Warm tower windows are visible but no exposed flame is certified. Architecture is production interpretation, not recovered preferred city reference. Court/tavern events and anonymous identities are invented illustrations of script narration, not independently established historical events. Prior mechanics, road, architecture and missing-image holds remain unresolved. Originals preserved; no final approvals.

Next Batch095 IMG0941–0950 finishes this paragraph and begins Old Ghis. Compare actual next dragon/harbor images before any geographic or flight continuity lock.
"""
(a/'BATCH_094_REVIEW.md').write_text(report)
z=Path('google_drive/EP001_BATCH_094_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as out:
 for s in manifest:
  out.write(s['original_local_file'])
  if s.get('replacement_file'):out.write(s['replacement_file'])
 for rp in assets.glob('*v02.png'):
  if str(rp) not in [s.get('replacement_file') for s in manifest]:out.write(rp)
 for p in [a/'BATCH_094_REVIEW.md',a/'BATCH_094_MANIFEST.json',a/'EP001_SHOT_AUDIT_LEDGER.json',a/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:out.write(p)
print(z,z.stat().st_size,hashlib.md5(z.read_bytes()).hexdigest())
assert not any(s['final_accepted'] for s in ledger['shots'])
