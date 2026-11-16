"""Batch103 recovered recreated-set audit. Run after102 only."""
import csv,hashlib,json,zipfile
from pathlib import Path
from PIL import Image
A=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/audit');P=Path('.recovery/batch103_prior');D=Path('google_drive/batch103')
md=lambda p:hashlib.md5(p.read_bytes()).hexdigest()
z=Path('google_drive/EP001_BATCH_103_RECREATED_REVIEW_BACKUP.zip');assert z.stat().st_size==45591550 and md(z)=='09bf3c12da6f70f8ee8ec05e864d458b'
prior=json.loads((P/'06_BATCH_103_MANIFEST.json').read_text());ledger=json.loads((A/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==1019
notes=[
('KEEP_PARTIAL_CREATURE_IDENTITY_HOLD','Silver-haired adult pair on monumental dark stairs beneath one flying dragon and carved dragon ornaments.','Supports marvel and dominance. Flying anatomy, identities, wardrobe, masonry-like stairs and city reference continuity unverified; no flame visible.'),
('REPLACED_PARTIAL_ANATOMY_ARCHITECTURE_HOLD','Two silver-haired women converse above harbor, one facing camera with open hand, distant flying dragon. Original letterboxed.','Select framing-only v02, no AI alteration. Hand anatomy, iris hue, necklace, character identity and conventional masonry remain held. Contextual house custom, not proof of a specific custom.'),
('REPLACED_PARTIAL_CREATURE_ARCHITECTURE_HOLD','Great grounded dark dragon beside crimson-clothed silver-haired adult; two distant observers, misty skyline. Original letterboxed.','AI v02 expands full-bleed framing without tight cropping dragon. Core pose remains similar. Folded-wing/limb articulation and creature identity not certified; pavement tiles persist despite prompt. Partial framing improvement, not resolved anatomy or architecture.'),
('KEEP_PARTIAL_GEOGRAPHY_CREATURE_HOLD','Two cloaked silver-haired shepherds, crook and sheep on green shore opposite dense dark city, one flying dragon.','Strong pastoral transformation context. Snow patches and fjord-like mountains require peninsula geography/grade review; sheep and distant dragon anatomy unresolved. No claim of approved house identity.'),
('KEEP_PARTIAL_ANATOMY_PROP_HOLD','Silver-haired working woman holding black bowl above table with spindle, wool cloth and metal torc; other workers behind.','Craft transformation context, not literal industrial engine. Hand grips, bowl function, house/social identity and tiny warm background points not certified; no new flame permission inferred.'),
('KEEP_PARTIAL_RITUAL_ANATOMY_HOLD','Two silver-haired adults hold hands above empty black bowl on terrace; third observer behind.','Recovered non-emissive ritual treatment retained. Gesture is illustrative, not proven historical spell/custom. Fingers, bowl purpose, paving seams and reference conformity held.'),
('REPLACED_PARTIAL_ARCHITECTURE_WARDROBE_HOLD','Three adult silver-haired delegates debate around oval black table with bowl, three dull tokens and folded wool.','AI v02 removes prominent masonry-like joints and smooths flowing room/tower surfaces. Three delegates are not literal forty count or king. Hands, costume/identity and more glossy new material grade remain held.'),
('REPLACED_PARTIAL_RESTRAINT_MECHANICS_HOLD','Two captive mine workers under silver-haired overseer: one holds pick at rock wall, second sorts ore in basket.','AI v02 removes unheld cart/ambiguous hauling shafts, clearer underground labor and ankle chain to low ring. Added dangling wrist chain despite no-wrist-chain prompt; pick has no certified impact/contact and grip/anchor mechanics remain held. Select as partial narrative improvement only; non-graphic oppression, no suffering glorification.'),
('KEEP_PARTIAL_CRAFT_ARCHITECTURE_HOLD','Silver-haired pair handle wool with carding-board-like tools and fleeces near sheep, rough-stone hut and dense city, distant dragon.','Direct wool/ash association. Carding-tool teeth/use, anatomy, basket mechanics and ash material not certified. Rough rural stone hut not automatically a violation of urban fused-spire direction; city styles and creature identity remain held.'),
('KEEP_PARTIAL_ARCHITECTURE_CREATURE_HOLD','Three rear silver-haired adults on terrace overlook dense harbor city, boats and two flying dragons.','Houses as political families, not literal forty buildings or count. Conventional buildings, railings, vessels, creature anatomy and prior paired-pylon skyline continuity remain unresolved.')]
records=[]
for j,old in enumerate(prior['records']):
 n=1021+j;original=P/'native'/f'VAL-EP001-IMG{n}.png';assert md(original)==old['md5'] and original.stat().st_size==old['bytes']
 with Image.open(original) as im:im.load();assert list(im.size)==old['dimensions']
 gen=n in (1023,1027,1028);crop=n==1022
 selected=D/f'VAL-EP001-IMG{n}_v02{"_framing" if crop else ""}.png' if gen or crop else original
 with Image.open(selected) as im:im.load();dims=list(im.size)
 status,obs,action=notes[j];s=ledger['shots'][n-1];assert s['scene_id']==old['scene_id']
 s.update(audit_status=status,drive_file_id=None,source_archive_drive_id='11cv4NjqOZ4I5iRbB5wYSdthHPDR43CfB',original_local_file=str(original),selected_local_file=str(selected),replacement_file=str(selected) if gen or crop else None,visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md(original),selected_md5=md(selected),reviewed_on='2026-11-15',review_scope='Ten recovered recreated natives, three AI edits and one framing derivative individually viewed at returned display resolution and decoded. Archive MD5 matched Drive metadata; native dimensions/bytes/hashes matched historical manifest. No all-pixel, identity/reference or timed-audio certification.')
 r=dict(s,selected_dimensions=dims,selected_bytes=selected.stat().st_size,correction_type='AI edit' if gen else 'proportional source-box crop/LANCZOS' if crop else 'none')
 if crop:r['source_box']=[69.875,39,1306.125,729];r['active_width_trim_percent']=100*(1-1236.25/1376)
 records.append(r)
ledger['reviewed_individually']=1029;assert not any(s['final_accepted'] for s in ledger['shots'])
(A/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (A/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(A/'BATCH_103_MANIFEST.json').write_text(json.dumps(records,indent=2)+'\n')
report='''# Batch103 — IMG1021–1030 (34:00–34:20)

**1029/1050 slots reviewed; zero final approvals.** Ten recovered recreated natives individually inspected. Three generated corrections (1023,1027,1028) and one framing-only derivative (1022) individually inspected and provisionally selected, all with explicit holds. One initial1028 generation failed with no output; retry succeeded. No earlier assets overwritten.

## Provenance and scope

Recovered recreated review ZIP ID11cv4NjqOZ4I5iRbB5wYSdthHPDR43CfB,45,591,550 bytes,MD5 09bf3c12da6f70f8ee8ec05e864d458b matched metadata. Ten native checksums/bytes/dimensions match enclosed manifest. This is an unapproved recreated set, not untouched pre-recreation originals: earlier eight empty candidates are described as preserved separately, not recovered in this ZIP. No independent PNG Drive IDs claimed.

Manifest records a historical user request for people, customs, dragons, dragonlords, objects and sorcery. Preserve that recovered treatment; do not empty the scenes again or generalize earlier off-camera dragon treatment to this recreated batch. This note is recovered evidence, not independently accessed historical chat. Preferred Screenshot(105) city reference and governing house/character/creature documents remain unrecovered, so none of these faces, dragons or outfits are reference-approved. No new emitter/flame authorization inferred; ritual remains non-emissive.

## Narration

Read full34:00–34:30 marvel/terror paragraph and34:30–35:00 transition. First ten slots progress from marvel/terror to pastoral transformation, sorcery/republic, underground bondage, wool/ash and forty houses. Later1031–1035 completes silver/violet, seamless spires, captive sweat and skies ruled by living fire. Contextual images need not literally illustrate each two-second fragment. Script/map unchanged, no audio timing/timeline edits. No exact forty delegates/structures, fourteen volcanoes or canon map certified.

## Corrections

1023 AI edit removes bars by expanded framing, not a tight crop of dragon silhouette. Creature pose remains similar and paving joints persist: partial framing improvement, no anatomy clearance.1027 AI edit replaces prominent masonry-like room joints with continuous flowing surfaces; grade/style and identity holds persist.1028 AI edit replaces unclear cart-hauling scene with pick/basket labor and an ankle tether. Added dangling wrist chain and uncertain pick contact remain explicit partial mechanics hold; narrative improvement is not a claim of perfect restraints.

1022 framing-only version uses centered source box[69.875,39,1306.125,729], proportional LANCZOS to1376×768, no stretching. Removes bars at cost of~10.16% active-image width; tighter crop inspected and selected provisionally, original preserved. All selected dimensions/hashes recorded; no blanket delivery conform approval.

## Individual findings

'''
for s in records:report+=f"### {s['scene_id']} — {s['audit_status']}\n\n{s['visual_observation']}\n\n{s['editorial_action']}\n\n"
report+='''## Remaining gates

Fine anatomy/hands, creature limb configuration and recurring dragon reference, house clothing/customs, portrait identity, bowl purpose, restraints/tool mechanics and all urban/geographic/grade continuity unresolved where noted. Tiny warm points in1025 background require emitter review, not assumed flames or permission. No final approval granted. All older holds and IMG0500 inherited missing remain. Next Batch104 IMG1031–1040 finishes recap and opens two-worlds transition; recover versions and read both full paragraphs first. Do not rerun prior builders out of sequence.
'''
(A/'BATCH_103_REVIEW.md').write_text(report)
out=Path('google_drive/EP001_BATCH_103_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as f:
 for p in (P/'native').glob('*.png'):f.write(p,'recovered_prior/native/'+p.name)
 f.write(P/'06_BATCH_103_MANIFEST.json','recovered_prior/06_BATCH_103_MANIFEST.json')
 for p in D.glob('*.png'):f.write(p)
 for p in [A/'BATCH_103_MANIFEST.json',A/'BATCH_103_REVIEW.md',A/'EP001_SHOT_AUDIT_LEDGER.json',A/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:f.write(p)
print(out,out.stat().st_size,md(out))
