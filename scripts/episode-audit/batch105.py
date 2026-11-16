"""Final chronological batch; not final episode acceptance."""
import collections,csv,hashlib,json,zipfile
from pathlib import Path
from PIL import Image
A=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/audit');P=Path('.recovery/batch105_prior');D=Path('google_drive/batch105')
md=lambda p:hashlib.md5(p.read_bytes()).hexdigest()
z=Path('google_drive/EP001_BATCH_105_RECREATED_REVIEW_BACKUP.zip');assert z.stat().st_size==60661803 and md(z)=='9abd9359dea4f985b441c5782771a66a'
prior=json.loads((P/'06_BATCH_105_MANIFEST.json').read_text());ledger=json.loads((A/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==1039
notes=[
('KEEP_PARTIAL_ARMOR_IDENTITY_HOLD','Bronze-scale officer with broad metal collar and red sash between two shield-bearing guards before brick pyramid and harbor.','Supports Ghiscari pride. Named identity, collar/armor doctrine, shield grip and incidental decorative markings not verified; no legible script asserted.'),
('KEEP_PARTIAL_WARDROBE_IDENTITY_HOLD','Silver-haired adult pair, violet-looking eyes, abundant jewelry and embroidered gray-blue clothes above dense city.','Supports Valyrian power, not approved principal identities. Jewelry/house dress, hand anatomy, non-emissive iris hue and architecture remain held.'),
('REPLACED_PARTIAL_CREATURE_IDENTITY_HOLD','Silver-haired jeweled adult touching large rust-red dragon head/neck before dark skyline; original broad muzzle read stylized beside realistic person.','AI v02 darkens muted red scales and weathers horns/face. Basic broad muzzle remains stylized; only partial material realism improvement, not complete photoreal creature correction or reference conformity. Hand contact, hidden body anatomy and identity remain held.'),
('KEEP_PARTIAL_WARDROBE_EMITTER_HOLD','Three silver-haired adults including elder central woman in elaborate pale clothing and blue jewels, green dragon above city.','Family/lineage tableau, not literal bloodshed or named house approval. Static portrait pacing, fine hands/jewelry, dragon anatomy and tiny warm background points require review; no new emitter permission inferred.'),
('REPLACED_PARTIAL_DRUM_NAVAL_MECHANICS_HOLD','Two drummers overlook troops and galleys in warm brick harbor; original dark drums read wood.','AI v02 clearly shows patinated bronze-colored shell, broad rim, hide and lacing. Foreground now has two visible beaters. Membrane/lacing/support, grips, rigs/oars and unit formations remain mechanically uncertified. Supports explicit bronze drums clause.'),
('KEEP_PARTIAL_DRUM_ANATOMY_HOLD','Low-angle adult drummers with padded beaters and broad hide heads beneath stepped brick pyramid and troops.','Appropriate Old Ghis drum context. Shell material not independently confirmed, fingers/beater contact and crowd detail held; no actual audio synchronization claimed.'),
('KEEP_PARTIAL_MARCH_ANATOMY_HOLD','Low-level view of bronze shields, spear butts and sandal-clad feet advancing over paving.','Good lockstep teaser. Single still does not prove synchronized gait; toes, straps, leg ownership and consistent shield/spear carriage remain held.'),
('KEEP_PARTIAL_ARMOR_CONTINUITY_HOLD','Serious dark-haired bronze-helmeted infantryman behind shield and spear, rear soldiers soft.','Appropriate legion expression insert; actual motion, recurring identity, scale armor construction and spear socket detail unverified. Not a battlefield event.'),
('KEEP_PARTIAL_HAND_WEAPON_HOLD','Hand grips dark wooden shaft close to socket of broad bronze-colored spearhead aboard vessel.','Strong explicit spears insert. Fine grip/digit anatomy, socket fastening and exact metal alloy not certified; no combat contact or dragon resistance shown.'),
('REPLACED_PARTIAL_CREATURE_ARCHITECTURE_HOLD','Two flying dragons above dark coastal city, two rear silver-haired observers on balcony. Original had conspicuous white city dots and lit windows.','AI v02 removes prominent bright city dots and warm window glow at display resolution. Dragons and city composition retained. Not all-pixel emitter certification; creature anatomy/identity, snowy geography, architecture/grade and shoreline continuity remain held.')]
records=[]
for j,old in enumerate(prior['records']):
 n=1041+j;original=P/'native'/f'VAL-EP001-IMG{n}.png';assert md(original)==old['md5'] and original.stat().st_size==old['bytes']
 with Image.open(original) as im:im.load();assert list(im.size)==old['dimensions']
 gen=n in (1043,1045,1050);selected=D/f'VAL-EP001-IMG{n}_v02.png' if gen else original
 with Image.open(selected) as im:im.load();dims=list(im.size)
 status,obs,action=notes[j];s=ledger['shots'][n-1];assert s['scene_id']==old['scene_id']
 s.update(audit_status=status,drive_file_id=None,source_archive_drive_id='1eRAhCJceyjyngZOqVyhCSNeMr8cMVA4B',original_local_file=str(original),selected_local_file=str(selected),replacement_file=str(selected) if gen else None,visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md(original),selected_md5=md(selected),reviewed_on='2026-11-15',review_scope='Ten recovered recreated natives and three generated edits individually viewed at returned display resolution and decoded. Archive MD5 matched Drive metadata; original hashes/bytes/dimensions matched enclosed manifest. No all-pixel, identity/reference or audio timing certification.')
 records.append(dict(s,selected_dimensions=dims,selected_bytes=selected.stat().st_size,correction_type='AI edit' if gen else 'none'))
ledger['reviewed_individually']=1049;assert len(ledger['shots'])==1050 and not any(s['final_accepted'] for s in ledger['shots'])
assert not any(s['audit_status']=='NOT_YET_INDIVIDUALLY_REVIEWED' for s in ledger['shots'])
assert [s['scene_id'] for s in ledger['shots'] if s['audit_status']=='MISSING_SOURCE_NOT_REVIEWED']==['VAL-EP001-IMG0500']
(A/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (A/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(A/'BATCH_105_MANIFEST.json').write_text(json.dumps(records,indent=2)+'\n')
report='''# Batch105 — IMG1041–1050 (34:40–35:00)

**Chronological pass reaches IMG1050:1049/1050 reviewed; zero final approvals.** IMG0500 remains missing/unreviewed. Ten recovered recreated natives individually inspected. Three generated v02 edits individually inspected and selected provisionally:1043 material realism,1045 bronze drum,1050 city-light removal. Every selection retains explicit holds; no originals overwritten.

## Provenance / script

Recovered recreated-review ZIP1eRAhCJceyjyngZOqVyhCSNeMr8cMVA4B,60,661,803 bytes,MD5 9abd9359dea4f985b441c5782771a66a matched Drive metadata. All ten original native hashes,bytes,dimensions match enclosed generated-review-pending manifest. This recreated set is not final delivery; earlier alternatives not in this ZIP are not claimed recovered. No independent enclosed-PNG Drive IDs claimed. Preferred Screenshot(105) city crop and governing character/house/creature references remain unrecovered.

Read whole34:30–35:00 paragraph: contrast Ghiscari bronze/discipline/pride against Valyrian fire/blood, then tease next episode's invasion drums and marching legions against dragons. No battle, spear impact, dragonfire emission or literal bloodshed needs inventing in these teaser stills. Ghiscari brick/bronze and Valyrian dark city remain distinct. No new emitter authorization inferred, no script/map/timeline edits or audio timing verification.

## Corrections

1043 edit adds muted dark material/weathered horns but retains broad stylized muzzle: partial realism improvement only, not resolved creature design.1045 changes dark wood-looking drum shell to clearly patinated bronze-colored shell with hide/lacing; physical percussion rig still held.1050 removes conspicuous city light dots/window glow at returned display resolution; not blanket all-pixel emitter approval. All three are AI edits, not pixel-identical crops. Native sizes/hashes recorded; no full delivery conform.

## Individual findings

'''
for s in records:report+=f"### {s['scene_id']} — {s['audit_status']}\n\n{s['visual_observation']}\n\n{s['editorial_action']}\n\n"
report+='''## Next phase

Do not call the episode finished or approved. Recover/replace missing0500 transparently, prioritize remaining script-mismatch correction queue, recover governing design references, and resolve partial anatomy/architecture/mechanics/emitter holds before timed sequence review and delivery acceptance. See CHRONOLOGICAL_PASS_RECONCILIATION.md and full UNACCEPTED_SHOTS_QUEUE.csv. No older hold cleared by reaching the last shot.
'''
(A/'BATCH_105_REVIEW.md').write_text(report)
counts=collections.Counter(s['audit_status'] for s in ledger['shots'])
summary={'total_slots':1050,'reviewed_individually':1049,'missing_unreviewed':['VAL-EP001-IMG0500'],'not_yet_reviewed_status_count':0,'final_accepted':0,'unaccepted_slots':1050,'status_counts':dict(sorted(counts.items())),'scope':'Inherited earlier reviews plus completed087–105 continuation; not a new visual re-review of all1050. Status labels heterogeneous, not normalized defect counts.'}
(A/'CHRONOLOGICAL_PASS_RECONCILIATION.json').write_text(json.dumps(summary,indent=2)+'\n')
qkeys=['scene_id','timestamp','audit_status','selected_local_file','replacement_file','editorial_action']
with (A/'UNACCEPTED_SHOTS_QUEUE.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=qkeys,extrasaction='ignore');w.writeheader();w.writerows(ledger['shots'])
(A/'CHRONOLOGICAL_PASS_RECONCILIATION.md').write_text('''# Chronological audit checkpoint — not delivery approval

- Total mapped slots:1050.
- Individually reviewed count:1049, including inherited earlier reviews; not a new reinspection of every frame this turn.
- Missing/unreviewed:IMG0500,16:38–16:40.
- No remaining NOT_YET_INDIVIDUALLY_REVIEWED status rows.
- Final accepted:0. All1050 slots remain unaccepted, not all1050 proven defective.
- Latest batch:105,IMG1041–1050,end35:00.

## Honest interpretation

Reaching the end closes the chronological coverage pass only. Many earlier rows still say correction recommended, queued replacement, hold or conditional keep. New corrections do not retroactively resolve them. Existing ledger labels are heterogeneous and some inherited review evidence is external; status counts are exact labels, not a clean count of distinct defects or independently reverified approvals. Root historical replacement_candidates_generated counter has not been reconciled to per-batch generated files and must not be quoted as current total.

## Prioritized continuation

1. Recover source0500 if available; otherwise create a clearly labeled replacement after reading whole16:30 paragraph and adjacent shots. Never invent source provenance or count unseen missing original as reviewed.
2. Resume substantive script-mismatch correction queue in chronological order, especially queued/recommended replacements still unresolved in inherited earlier reviews. Full queue includes all1050 unaccepted slots with original labels/actions, not a claim every frame needs replacement.
3. Recover preferred city concept/crop, house dress/character/dragon references and emitter direction. Retrospective city continuity remains open after later peninsula clarification.
4. Resolve partial mechanics/anatomy/creature/wardrobe/architecture/grade/emitter holds through actual inspected versions. Preserve rejected attempts and originals.
5. Check actual narration timing and sequence/pacing, then delivery conform, full technical QC and explicit final acceptance. None performed by this still-image audit.

All prior named holds persist, including0858 partial and0885 basket mechanics, and later architecture/road/naval/creature holds. Scripts/shot map unchanged. Do not rerun completed builders out of sequence.
''')
out=Path('google_drive/EP001_BATCH_105_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as f:
 for p in (P/'native').glob('*.png'):f.write(p,'recovered_prior/native/'+p.name)
 f.write(P/'06_BATCH_105_MANIFEST.json','recovered_prior/06_BATCH_105_MANIFEST.json')
 for p in D.glob('*.png'):f.write(p)
 for name in ['BATCH_105_MANIFEST.json','BATCH_105_REVIEW.md','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv','CHRONOLOGICAL_PASS_RECONCILIATION.md','CHRONOLOGICAL_PASS_RECONCILIATION.json','UNACCEPTED_SHOTS_QUEUE.csv']:f.write(A/name)
 f.write(Path(__file__))
print(out,out.stat().st_size,md(out))
