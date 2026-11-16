"""Batch104 native audit; run after103 only."""
import csv,hashlib,json,zipfile
from pathlib import Path
from PIL import Image
A=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/audit');P=Path('.recovery/batch104_prior');D=Path('google_drive/batch104')
md=lambda p:hashlib.md5(p.read_bytes()).hexdigest()
z=Path('google_drive/EP001_BATCH_104_REVIEW_BACKUP.zip');assert z.stat().st_size==57278867 and md(z)=='843e8de99d779b068a202a40e61f5662'
prior=json.loads((P/'06_BATCH_104_MANIFEST.json').read_text());ledger=json.loads((A/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==1029
notes=[
('KEEP_PARTIAL_IDENTITY_ARCHITECTURE_HOLD','Three silver-haired adult delegates in gray, blue and pale clothing converse before dense dark towers; central man wears double chain.','Supports houses of silver/violet, not literal forty count. Eyes too small for hue certification; named identities, jewelry/house doctrine and conventional jointed architecture unverified.'),
('KEEP_PARTIAL_ANATOMY_HOLD','Pale hand in plain gray sleeve and metal bangle touches continuous flowing dark stone rail or rib.','Good material insert for seamless fused stone. Four fingers visible, thumb hidden, not missing-digit proof; hand anatomy, bangle and costume continuity remain held.'),
('REPLACED_PARTIAL_WARDROBE_HOLD','Sweaty dark-haired adult miner close-up in rough mine, daylight from opening; original pointed shirt collar and placket read modern.','AI v02 replaces modern collar with rough frayed round-slit tunic and cord tie. Sweat/hair and setting retained; textile period accuracy and facial continuity not blanket-approved. Captive context relies on adjacent restraints shot.'),
('KEEP_PARTIAL_RESTRAINT_ANATOMY_HOLD','Dirty sweaty hands grip thick twisted rope beside wood container, one wrist visibly cuffed.','Supports captive labor. No full hauling system visible; force direction, chain closure, hand grip, digits and continuity to portrait remain unresolved. No claim rope operates a certified cart.'),
('REPLACED_PARTIAL_CREATURE_ARCHITECTURE_HOLD','Dragon with small seated rider flies over harbor and dark city while two rear figures observe; original upper wing cut by frame.','AI v02 scales/repositions dragon so wing tips and tail fit within frame. Full silhouette improved, not certified rider tack, limb/wing mechanics or named creature match. Conventional paving/architecture and geography remain held. Living fire illustrated by dragon, no new flame emitter.'),
('KEEP_PARTIAL_WARDROBE_NAVAL_HOLD','Two dark-haired bronze-scale guards stand beside timber galley and warm stepped brick city.','Appropriate Ghiscari counter-world contrast. Guards look similar; costume/iconography, galley ram/rigging and background labor anatomy unverified. Does not show both worlds on physically adjacent shores.'),
('REPLACED_PARTIAL_IDENTITY_CREATURE_HOLD','Rear braided silver-haired adult in dark crimson scale-paneled dress watches distant fleet, grounded dragon-like silhouette on side terrace; original letterboxed.','AI v02 expands full-bleed composition and makes main balcony flowing fused-looking stone. Human smaller in frame. Identity/hair/wardrobe, small hands, distant dragon anatomy and fleet nationality/heading unverified. Distant land not certified as Ghis.'),
('KEEP_PARTIAL_NAVAL_MECHANICS_HOLD','Two foreground sailors handle rope coils aboard vessel while several sail-and-oar ships face viewer on sea.','Supports gathering fleets before war. Vessel count, rigs, oar geometry, fleet heading and rope handling not mechanically certified; no battle or literal geographic channel asserted.'),
('KEEP_PARTIAL_FORMATION_NAVAL_HOLD','Wide warm-brick harbor with many docked ancient galleys and dense ordered troops carrying shields and upright spears.','Supports old military empire. Tiny bodies/gear, exact formation, spear number, ram/rigging and city/iconography reference not certified. No battle underway.'),
('REPLACED_PARTIAL_ARMOR_ANATOMY_HOLD','Three bronze-scale infantrymen in diagonal rank with spears and shield before brick wall and galley; original faces near-duplicates, spear tips gray.','AI v02 differentiates foreground, older bearded middle and youthful rear adult-intended soldier; spear tips warmer bronze-colored. Rear face reads very youthful: adult age cannot be certified from appearance. Front spearhead remains cropped, grips/hidden shield support and exact armor doctrine held; no full unit triple-spear certification.')]
records=[]
for j,old in enumerate(prior['records']):
 n=1031+j;original=P/'native'/f'VAL-EP001-IMG{n}.png';assert md(original)==old['md5'] and original.stat().st_size==old['bytes']
 with Image.open(original) as im:im.load();assert list(im.size)==old['dimensions']
 gen=n in (1033,1035,1037,1040);selected=D/f'VAL-EP001-IMG{n}_v02.png' if gen else original
 with Image.open(selected) as im:im.load();dims=list(im.size)
 status,obs,action=notes[j];s=ledger['shots'][n-1];assert s['scene_id']==old['scene_id']
 s.update(audit_status=status,drive_file_id=None,source_archive_drive_id='1LnXY0kkBuKsr07dOcK8U8b2fQcni7dZZ',original_local_file=str(original),selected_local_file=str(selected),replacement_file=str(selected) if gen else None,visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md(original),selected_md5=md(selected),reviewed_on='2026-11-15',review_scope='Ten recovered native originals and four generated v02 edits individually viewed at returned display resolution and decoded. Archive MD5 matched Drive metadata; original hashes/bytes/dimensions matched historical manifest. No all-pixel, named identity/reference or audio timing certification.')
 records.append(dict(s,selected_dimensions=dims,selected_bytes=selected.stat().st_size,correction_type='AI edit' if gen else 'none'))
ledger['reviewed_individually']=1039;assert not any(s['final_accepted'] for s in ledger['shots'])
(A/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (A/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(A/'BATCH_104_MANIFEST.json').write_text(json.dumps(records,indent=2)+'\n')
report='''# Batch104 — IMG1031–1040 (34:20–34:40)

**1039/1050 reviewed; zero final approvals.** Ten native originals individually inspected. Four AI edits generated, individually inspected and provisionally selected:1033 clothing,1035 dragon framing,1037 full-bleed lookout,1040 face variation/bronze-colored spearheads. All remain partial holds, no originals overwritten.

## Provenance / narration

Recovered review ZIP1LnXY0kkBuKsr07dOcK8U8b2fQcni7dZZ,57,278,867 bytes,MD5 843e8de99d779b068a202a40e61f5662 matched Drive metadata. All ten native hashes/bytes/dimensions match enclosed manifest; native sizes vary. Archive is generated-review-pending, not final acceptance. No independent PNG Drive IDs claimed. Actual preferred Screenshot(105) city crop and governing character/house/creature references remain unrecovered; prior manifest records preference but does not certify matching.

Read full34:00–34:30 and34:30–35:00 paragraphs. First five finish houses of silver/violet, seamless stone, captive sweat and living fire; next five contrast Valyria with bronze-armed military Ghis across gathering sea. Dragons need not emit literal flame to represent living fire. No new flame ruling inferred. Ghiscari brick/bronze world deliberately differs from Valyrian fused-stone world: do not remove Ghiscari brick architecture as if it were a Valyrian defect. No exact forty count, fourteen peaks, navigation geography, or literal visible Ghis opposite Valyria certified. No script/map/timeline edits or timed-audio verification.

## Corrections / limits

1033 original had modern-looking folded pointed shirt collar/placket; v02 uses frayed round-slit tunic and tie.1035 original wing clipped by upper edge; v02 fits dragon silhouette but rider equipment and anatomy stay held.1037 original bars removed through AI expanded framing, not a technical crop or stretch; composition now substantially wider and human smaller.1040 original near-duplicate faces differentiated and gray tips warmed to bronze color; front tip still cropped and rear face youthful. These edits improve identified defects without claiming complete correction or final doctrine compliance. Architecture/paving joints persist in1035; no silent clearance.

## Individual findings

'''
for s in records:report+=f"### {s['scene_id']} — {s['audit_status']}\n\n{s['visual_observation']}\n\n{s['editorial_action']}\n\n"
report+='''## Remaining gates / next

Fine-pixel anatomy/hands, restraints, naval rigs/oars/rams, armor/iconography, creature identity and limb mechanics, urban/shore geography and grade remain open where noted. Selected media dimensions/checksums recorded, not a blanket ten-shot delivery conform. All prior holds persist, IMG0500 inherited missing remains. Next Batch105 IMG1041–1050 completes final20 seconds. After chronological pass, distinguish reviewed slots from all defects resolved and final acceptance; do not report episode complete while inherited missing/partial holds remain. Do not rerun earlier builders out of sequence.
'''
(A/'BATCH_104_REVIEW.md').write_text(report)
out=Path('google_drive/EP001_BATCH_104_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as f:
 for p in (P/'native').glob('*.png'):f.write(p,'recovered_prior/native/'+p.name)
 f.write(P/'06_BATCH_104_MANIFEST.json','recovered_prior/06_BATCH_104_MANIFEST.json')
 for p in D.glob('*.png'):f.write(p)
 for p in [A/'BATCH_104_MANIFEST.json',A/'BATCH_104_REVIEW.md',A/'EP001_SHOT_AUDIT_LEDGER.json',A/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:f.write(p)
print(out,out.stat().st_size,md(out))
