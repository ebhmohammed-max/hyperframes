"""Audit recovered Batch100 native ensemble without overriding inherited treatment."""
import csv
import hashlib
import json
import zipfile
from pathlib import Path
from PIL import Image
root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
a=root/'audit'
prior=Path('.recovery/batch100_prior')
pm=json.loads((prior/'06_BATCH_100_MANIFEST.json').read_text())
ids=['1aNTuGxywiVdDWHT8L_omos2sBucq8RZy','1lQznwIM3B2OeUEkObGUV7y3SN2rfu2Bi','1xgpYvlH_BxYZ5jlR8ApENFy30XXWfugR','18yPNlH8fPRyaDYCZMtVI-lrmE6kBK10J','1-psSo2v2a197DDKoZdXiTXRTXPf4uwA7','1PsjSCcw9ybTacfW3xcYXYeJ8lT8CJOSb','1YA5gKgjyL2Fgt1FeKNyYr3mUt5mIW-NK','1VhIeI0Jv3Xi6bK5IJkq82vylYcSmujSc','1skb2_rH1u1WHnQwXljigcPWPCmy-4NfZ','1jLi0T2j3lN4RkcfVjtfuaqoKFvnJH-sz']
checks=['61c1f68250884f3c60ecc9fd0b9b844e','e6ce07e910dcc4d8ecd690d3e93e66c1','a5e5162d36d3282221631de615feed35','b7ac9a22a4a3b057c0194961b7a98533','0b8164ae6e8941b336d7f87145f4e494','d3fd94c9d14779692ecefbef283c0305','237ddfeb07539b3636a65137c0371dc2','0e922149344a90b9c0a555a3ba2ed8e1','b01f80c91d02c2fdc06891c96fc944e0','58b39b84fc20a2a0984059725fb4ada5']
notes=[('KEEP_CONTEXT_ONLY','Three distant silver-haired adults stand on projecting dark pitted volcanic promontory above sea.','Supports defiant group lookout. Rock reads geological, not proven fused architecture; overhang engineering and distant people not certified. No continuous geography asserted.'),('KEEP_CANDIDATE','Rear view of heavily braided pale-haired adult in dark scale shoulders and crimson cloth watching three distant low ships.','Supports watchful Freehold. Anonymous house delegate, not approved principal identity; metal is not certified Valyrian steel. Vessels too distant to verify rams or nationality.'),('KEEP_CANDIDATE','Five silver-haired adults in varied gray dress watch line of small ships from dark rocky coast.','Strong ensemble/fleet beat; observed seven distant hull-like silhouettes, not a certified military count or proven eastern origin. Costume and scale fine detail held.'),('KEEP_CANDIDATE','Wide cold rocky cape with grouped distant low hulls near horizon.','Supports multiplying fleet when edited with preceding shots, not proof temporal multiplication or heading. Tiny oars/rigging/type unverified.'),('KEEP_CANDIDATE','Silver-haired adult woman in dark indigo-gray cloth, fine temple chains and one visible dark drop earring, violet-looking irises.','Supports resolve. Recovered manifest labels DREVAN supporting noblewoman; house identity/dress doctrine not independently recovered. Iris hue non-emissive at display resolution; no identity approval.'),('KEEP_CANDIDATE','Five pale-haired adults stand in varied muted clothing under dark curved rock opening looking seaward.','Supports shared refusal of submission. Background geological/fused distinction and ensemble hand/accessory details remain held. No principal character identity claim.'),('KEEP_CANDIDATE','Silver-haired adult woman in pale wool, broad side/nape braid and flat silver-colored torc against dark rock.','Recovered manifest identifies supporting SYTHIS rather than earlier unapproved principal. Preserve that distinction; no scar or principal reference conformity asserted. House doctrine remains unresolved.'),('KEEP_CONTEXT_ONLY','Dormant empty caldera with two tiny adults at rim and large wool scrap weighted by stone in foreground.','Recalled volcanic/shepherd history rather than literal present fiery mouth. Prior manifest explicitly keeps dormant/no-new-emitter treatment. Cloth/stone metaphor invented, scale and grade held; not fourteen counted volcanoes.'),('KEEP_CONTEXT_ONLY','Three silver-haired adults overlook layered dormant mountains and empty nearby dark roost-like outcrop.','Prior ensemble treatment keeps dragon off-camera. Supports remembered homeland/binding, not visible dragon or literal binding event. No exact fourteen count or canon map established.'),('KEEP_PARTIAL_ARCHITECTURE_HOLD','Five distant pale-haired adults look toward isolated monumental dark ribbed fused-looking coastal mass with narrow irregular openings and green ledges.','Prior manifest explicitly retains mineral buttress rhythm for director review. Preserve hold: fortress reads isolated amid largely empty valley rather than verified city; style/reference conformity unresolved. No road seen; do not restore older road brief.')]
ledger=json.loads((a/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==989
package=Path('google_drive/EP001_BATCH_100_DELIVERY_1376x768_REVIEW.zip')
assert hashlib.md5(package.read_bytes()).hexdigest()=='579f1c825e0e13de75dfbb281249d00a'
manifest=[]
for j,(status,obs,action) in enumerate(notes):
 n=991+j;p=Path(f'google_drive/VAL-EP001-IMG{n:04d}.png');md=hashlib.md5(p.read_bytes()).hexdigest();assert md==checks[j]
 with Image.open(p) as im:im.load();dims=list(im.size)
 old=pm['records'][j];assert old['scene_id']==p.stem;assert old['md5']==md;assert old['dimensions']==dims
 delivery=prior/'images'/p.name
 with Image.open(delivery) as im:im.load();assert im.size==(1376,768)
 s=ledger['shots'][n-1];assert s['scene_id']==p.stem
 s.update(audit_status=status,drive_file_id=ids[j],selected_local_file=str(p),original_local_file=str(p),visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md,reviewed_on='2026-11-15',review_scope='Native independently opened at tool display resolution, decoded and MD5 matched; no enlarged all-pixel certification or timed audio. Prior resized delivery files decoded only, not independently visually certified.',inherited_treatment='Recovered manifest records house ensemble, DRG-VAL-002 off-camera and no new Chapter VII emitters. Source governing documents not yet recovered; no direct historical user authorization independently verified.')
 manifest.append(dict(s,native_dimensions=dims,native_bytes=p.stat().st_size,prior_manifest_md5_match=True,prior_delivery_file=str(delivery),prior_delivery_md5=hashlib.md5(delivery.read_bytes()).hexdigest(),prior_delivery_dimensions=[1376,768],prior_delivery_visual_review='Not independently visually reviewed this pass; decoded only.'))
ledger['reviewed_individually']=999
(a/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (a/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(a/'BATCH_100_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
report='''# Batch100 — IMG0991–1000 (33:00–33:20)

Ten current native Drive candidates individually viewed, decoded and MD5 matched to both Drive listing and recovered prior manifest. Zero new images generated: existing ensemble revision retained. 999/1050 slots reviewed, zero final approvals. IMG0500 remains inherited missing/unresolved; reaching IMG1000 is not 1000 reviewed.

## Recovery and treatment

Unlike preceding folders, Batch100 already contains ensemble revisions and a separate 1376×768 delivery review ZIP. Downloaded ZIP ID 19kXEXknLTMrDIJLwH_Z4h8pGd7yBCqyp, 15,357,474 bytes, MD5 579f1c825e0e13de75dfbb281249d00a verified. Its manifest records prior user selection of house ensemble, dragon off-camera, dormant volcano imagery and no newly authorized Chapter VII emitters. That is recovered documentary evidence, not independent access to historical chat. Preserve this treatment, do not replace it with new dragons/flame merely to illustrate narration literally.

The four referenced art-direction/house-dress/Appendix-A documents were searched by filename in Drive and returned zero matches; their contents are not recovered or certified. Named DREVAN/SYTHIS identities below are inherited labels, not independently verified design conformity. Prior source metadata includes superseded generation briefs; latest review notes take precedence as recovery evidence. Governing-document recovery and broader retrospective conformity of earlier batches remain open, not silently waived.

## Narration context

33:00–33:30: Freehold observes eastern war-galleys without dread/submission, recalls shepherd ancestry, fiery mouths of fourteen volcanoes and binding living flame, and refuses kings or Ghis pyramids. The current off-camera/dormant treatment reads the central material as historical recollection, not new emitted flame. Next paragraph explicitly reflects on unresolved dragon origins/Asshai accounts. Script and shot map unchanged. No timed narration or timeline edits verified.

## Native vs delivery

Prior delivery PNGs all decode at 1376×768; they are distinct resized/cropped derivatives, not native bytes. Prior conform report discloses centered subpixel crop/LANCZOS with up to ~0.83% area trim. This pass did not create a new crop or independently visually certify those delivery copies. Native source dimensions/checksums retained in manifest. Original prior report and manifest archived as recovery evidence, not final approval.

## Individual decisions

'''
for s in manifest:report+=f"### {s['scene_id']} — {s['audit_status']}\n\nObserved: {s['visual_observation']}\n\n{s['editorial_action']}\n\n"
report+='''## Remaining gates

IMG1000 explicit architecture hold retained. All ten remain provisional/context-only, no final masters. Full-pixel anatomy, eye hue, braid/jewelry/house dress and architectural reference/grade/geographic continuity remain open. Existing prior corrections not overwritten. No new media generation or flame permissions inferred. Older basket, road, anatomy, city, wardrobe and creature holds persist. This audit package includes native candidates, cumulative ledger, and recovered prior manifest/conform report; prior delivery ZIP remains separately linked through its known ID.

Next Batch101 IMG1001–1010: finish defiance paragraph then begin reflective uncertainty passage at 33:30. Check existing revisions/authorizations before generating anything.
'''
(a/'BATCH_100_REVIEW.md').write_text(report)
z=Path('google_drive/EP001_BATCH_100_AUDIT_WITH_RECOVERED_ENSEMBLE.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as out:
 for s in manifest:out.write(s['original_local_file'])
 for p in [a/'BATCH_100_REVIEW.md',a/'BATCH_100_MANIFEST.json',a/'EP001_SHOT_AUDIT_LEDGER.json',a/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:out.write(p)
 for name in ['06_BATCH_100_MANIFEST.json','18_BATCH_100_DELIVERY_CONFORM_2026-11-14.md']:out.write(prior/name,arcname='recovered_prior/'+name)
assert not any(s['final_accepted'] for s in ledger['shots'])
print(z,z.stat().st_size,hashlib.md5(z.read_bytes()).hexdigest())
