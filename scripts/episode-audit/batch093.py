"""Persist Batch093 individually inspected originals and provisional corrections."""
import csv, hashlib, json, zipfile
from pathlib import Path
from PIL import Image
root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
a=root/'audit'; assets=Path('assets/episode_audit/batch093')
ids=['1U_VRVdh143tXQcce4ZvciMOEDdSK9XYL','1GVQb4oOEsDpMYKJD4U5Rxurp8-2NHD_X','1tBRreC3SE1q13_M8sPF8hvi_dKL-_Q9o','1OjfDnNzLqOgnKAYtfP8IkBVfvWx0y7yt','1yuRnqL4bmuZgJpY_dmPd9PHZdhaUrr9X','1zNsCWgeoOXvjfQwsBespbIGQiFbILBzb','1XhDqBl1LReh8YCtL-Iwj6PpYxuZLso1A','158_hfWBH7pebqGG57xXjFvNDYw2m-FA2','1Qbz9lG8SCelY72yBKO29NT0queWv_yqp','16YLUKXC1zSSv8cm-W2QRtIYDIulBfMYT']
checks=['64511196cdd90522c41d145acfb5e2b7','164af590ca804716cbf2597872f44a93','34505b5b94e1086f8537f3ec679e0333','bb8b95f9d06b528944ebedcbcc8a0d2d','dcdb457e0d355edf869af31d606978bb','f67b72d27ac2060dc91e116ea1e58da7','5a48f114adf1bc45cdd988966997f782','ff9bfdd0c5985399799360c9c93b0196','14e4680bfb06d8cc4dbca0bb4bd279ab','97e0b7aa3c68f783a21b0b8555c7deaf']
notes=[
('KEEP_CONTEXT_ONLY','Pale-haired cloaked adult overlooks barren volcanic shoreline.','Southern cape context only; not proof of dominion or exact cape. Cut from 0920 northern traveler is editorial geographic montage, not same person or continuous journey.'),
('KEEP_CANDIDATE','Blurred pale-haired observer at left looks toward distant green mountainous island.','Supports green island mention; cedar species and exact Isle of Cedars geography unverified.'),
('KEEP_CONTEXT_ONLY','Dark-haired and silver-haired adults face one another on rocky coast.','May suggest local contact under Freehold, but no visible oath, treaty or trade. Do not assert named characters or historical submission event.'),
('REPLACE','Nearly empty rocky bays with low dark settlement forms and rough breakwaters.','Lacks thriving turquoise harbor commerce; replace with inhabited active harbor.'),
('REPLACE','Aerial barren gridded coastline with repeated empty coves and low gray settlement forms.','Reads desolate rather than generational prosperity. Replace with cultivated inhabited coastal overview.'),
('REPLACE','Dense tall multi-masted high-sided wooden ships with complex rigging crowd harbor.','Crowding fits, but vessel silhouette suggests later tall-ship era. Replace with low single-masted ancient merchant hulls.'),
('KEEP_CANDIDATE','Wet dark irregular stone quay face with iron ring, rope and barnacles.','Useful harbor material insert. Irregular fissures not proven masonry joints; not alone proof of magically fused stone. Match sunlit harbor grade.'),
('KEEP_CANDIDATE','Tray of gold-colored chains, silver-colored jewelry and dark coins/carved object.','Supports luxury trade; material composition and Valyrian provenance unverified. Do not certify dark carved object as obsidian or coin design as canon.'),
('KEEP_CANDIDATE','Fine silver-colored wirework pendant with polished dark stone beside golden curved metal.','Strong fine-metalwork insert. Obsidian identity not testable; production-invented jewelry, not canonical artifact.'),
('KEEP_CONTEXT_ONLY','Three small sailboats beyond long wet rocky barrier under cloudy sky.','Useful outgoing mariner bridge to next paragraph. Origin and distant-coast identity not established; grade transition held.')]
repl={924:('Busy turquoise harbor with smooth curving dark structures, quays, many small ships and cultivated hills.','Main activity defect corrected. Some foreground domes show visible block courses; fused-stone architecture conformity remains partial. Different design from 0916/0926; set/grade matching held.'),925:('Green cultivated coastal valleys with multiple inhabited bays, small ships and distant green island.','Prosperity corrected. Terracotta village roofs and castle-like black landmark remain generic rather than established Valyrian direction. Interpretive geography, not exact map; architecture partial.'),926:('Low open single-mast wooden cargo hulls with simple rigging, dockside amphorae, sacks and adult mariners; dark harbor wall.','Late tall-ship silhouette corrected. Background cylindrical tower design not matched to established city references; hands, cargo mechanics and rigging not certified at all pixels. Architecture continuity partial.')}
ledger=json.loads((a/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==919
manifest=[]
for j,(status,obs,action) in enumerate(notes):
 n=921+j; p=Path(f'google_drive/VAL-EP001-IMG{n:04d}.png'); md=hashlib.md5(p.read_bytes()).hexdigest(); assert md==checks[j]
 with Image.open(p) as im: im.load(); dims=list(im.size)
 s=ledger['shots'][n-1];assert s['scene_id']==p.stem
 s.update(audit_status=status,drive_file_id=ids[j],selected_local_file=str(p),original_local_file=str(p),visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md,reviewed_on='2026-11-15',review_scope='Individually opened at tool display resolution, decoded and MD5 matched; no audio timing or all-pixel anatomy certification.')
 if n in repl:
  rp=assets/f'{p.stem}_v02.png'
  with Image.open(rp) as im:im.load();rd=list(im.size)
  s.update(audit_status='REPLACED_PARTIAL_ARCHITECTURE_HOLD',selected_local_file=str(rp),replacement_file=str(rp),replacement_md5=hashlib.md5(rp.read_bytes()).hexdigest(),replacement_dimensions=rd,replacement_observation=repl[n][0],replacement_review=repl[n][1])
 manifest.append(dict(s,native_dimensions=dims,native_bytes=p.stat().st_size))
ledger['reviewed_individually']=929
(a/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (a/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(a/'BATCH_093_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
report='''# Batch093 — IMG0921–0930 (30:40–31:00)

Ten originals individually viewed, decoded and matched to Drive MD5. Three generated v02 replacements individually viewed and provisionally selected. 929/1050 slots reviewed; zero final approvals.

## Full-paragraph context

30:30–31:00 describes generational transformation, valleys from northern foothills to southern capes facing the green Isle of Cedars, turquoise Summer Sea bays, merchant hulls beneath fused-stone breakwaters, and gold/silver/obsidian/fine metalwork traded with distant mariners. Next paragraph concerns sailors reporting Valyrian wonders abroad. Original script and 1050-shot map remain unchanged; this is still selection, not a timed edit.

## Decisions

'''
for s in manifest:
 report+=f"### {s['scene_id']} — {s['audit_status']}\n\nObserved original: {s['visual_observation']}\n\n{s['editorial_action']}\n\n"
 if s.get('replacement_observation'):report+=f"Selected v02: {s['replacement_observation']}\n\nRemaining hold: {s['replacement_review']}\n\n"
report+='''## Remaining gates

All three corrections resolve their principal commerce/vessel mismatch but remain PARTIAL_ARCHITECTURE_HOLD, not final masters. No actor likeness reference used. City direction still unrecovered; do not certify canonical harbor geometry or geography. New bright shots need grading against retained cloudy coastal/material inserts and preceding 0916–0919. 0928/0929 dark materials are not verified obsidian: a dedicated rough obsidian insert may be needed if edit demands unambiguous illustration. No new flame or sorcery introduced. Prior 0885 mechanics, 0916 architecture and 0918 road conformity holds remain unresolved; this pass does not clear them. Original files and cumulative prior decisions preserved. No audio timing verified.

Next: Batch094 IMG0931–0940, sailors' reports of Valyrian wonders.
'''
(a/'BATCH_093_REVIEW.md').write_text(report)
z=Path('google_drive/EP001_BATCH_093_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as out:
 for s in manifest:
  out.write(s['original_local_file'])
  if s.get('replacement_file'):out.write(s['replacement_file'])
 for p in [a/'BATCH_093_REVIEW.md',a/'BATCH_093_MANIFEST.json',a/'EP001_SHOT_AUDIT_LEDGER.json',a/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:out.write(p)
print(z,z.stat().st_size,hashlib.md5(z.read_bytes()).hexdigest())
assert not any(s['final_accepted'] for s in ledger['shots'])
