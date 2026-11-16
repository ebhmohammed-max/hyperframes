"""Batch101 recovered candidate audit; run only after Batch100."""
import csv,hashlib,json,shutil,zipfile
from pathlib import Path
from PIL import Image
A=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/audit')
P=Path('.recovery/batch101_prior'); D=Path('google_drive/batch101');D.mkdir(exist_ok=True)
md=lambda p:hashlib.md5(p.read_bytes()).hexdigest()
z=Path('google_drive/EP001_BATCH_101_ALL_REVISIONS_REVIEW_BACKUP.zip');assert md(z)=='e3c371ceac9de44295b7df70a223576e' and z.stat().st_size==34847802
prior=json.loads((P/'06_BATCH_101_MANIFEST.json').read_text())
ledger=json.loads((A/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==999
notes=[
('KEEP_CONTEXT_ONLY','Upright silver-haired rear figure in crimson robe and dark scale shoulders beneath tall isolated black rock.','Defiant upright posture fits refusal to kneel. Geological cutaway, not proof of urban scale. Principal identity and wardrobe remain unverified.'),
('KEEP_PARTIAL_ANATOMY_HOLD','Pale hand resting flat on dark rock, crimson sleeve and overlapping dark scales.','Supports resolve without crown or kneeling. Four fingers visible, thumb occluded; wrist/hand anatomy and principal costume continuity not certified.'),
('REPLACED_PARTIAL_WARDROBE_HOLD','Rear braid and scale-shoulder close-up; revision replaces block-like portal with irregular flowing dark rock and dulls metal hardware.','Select recovered revision_02 over first pass. Main background defect improved; numerous braid rings/rivets and shoulder scale layout remain wardrobe/continuity holds. No face identity claim.'),
('KEEP_CANDIDATE','Dark leather boot planted on black ledge below crimson hem.','Supports never kneel; no literal Old Ghis brick in this contextual Valyrian cutaway. Boot finishing and costume reference need detailed check.'),
('KEEP_CONTEXT_ONLY','Upright rear silver-haired crimson-robed figure beside black cliff, looking over empty gray sea.','Refusal beat, not a literal view of Old Ghis. No invented giant pyramids across implausibly narrow water; identity, hand detail and geographic continuity held.'),
('KEEP_CONTEXT_ONLY','Empty narrow ledge at foot of enormous dark fractured wall, sparse hanging vegetation and gray sky.','Reflective pause insert reads geology rather than city; compatible with the paragraph but no certified location reference match.'),
('KEEP_CONTEXT_ONLY','Foreground rock shoulder frames narrow ridge and broad dormant volcanic valley.','Knife-edge metaphor without adding a person or battle. Not exact fourteen count or confirmed canon geography.'),
('REPLACED_PARTIAL_ARCHITECTURE_HOLD','Empty wet dark terrace overlooks wide bay and dense sculptural coastal city with bridges and paired soaring pylons.','Select recovered revision_03: city now legible rather than isolated columnar bluff. Recovered direction note records user-selected original concept inspired by book reference; actual concept/reference images not yet recovered. Detailed fused architecture, scale, engineering and earlier-shot continuity held.'),
('REPLACED_PARTIAL_ARCHITECTURE_HOLD','Wider inland volcanic terrain curves around bay toward distant dense city and paired tall pylons in haze.','Select recovered revision_03 over first-pass castle skyline and revision_02 empty bluff. Intended landmark relationship improves, but camera geography, shoreline and skyline continuity are not certified. Haze limits structure detail.'),
('KEEP_CONTEXT_ONLY','Close-up of folded dark rock divided by narrow unlit black fissure.','Veiled-history metaphor; no literal hatchery, binding magic or Asshai truth asserted. No obvious glow or creature at display resolution.')]
records=[];inventory=[]
for p in sorted(P.rglob('*.png')):
 with Image.open(p) as im:im.load();dims=list(im.size)
 inventory.append({'file':str(p.relative_to(P)),'md5':md(p),'dimensions':dims,'bytes':p.stat().st_size,'individually_viewed':True})
for j,old in enumerate(prior['records']):
 n=1001+j;name=f'VAL-EP001-IMG{n}.png';original=P/name
 assert md(original)==old['md5'] and original.stat().st_size==old['bytes']
 version='revision_02' if n==1003 else 'revision_03' if n in (1008,1009) else ''
 selected=P/version/name if version else original
 dest=D/version/name if version else D/name;dest.parent.mkdir(exist_ok=True);shutil.copy2(selected,dest)
 status,obs,action=notes[j];s=ledger['shots'][n-1];assert s['scene_id']==name[:-4]
 s.update(audit_status=status,drive_file_id=None,source_archive_drive_id='1MeSLpdmW-8XCZViUlcnpgxAfLPhRkBcK',original_local_file=str(original),selected_local_file=str(dest),replacement_file=str(dest) if version else None,visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md(original),selected_md5=md(dest),reviewed_on='2026-11-15',review_scope='All ten first-pass natives and four recovered revisions individually opened at returned display resolution. Archive MD5 matched Drive metadata; originals matched historical manifest. Revision digests newly recorded, not independently listed per-file by Drive. No all-pixel QC, final acceptance or audio timing.')
 records.append(dict(s,selected_version=version or 'first_pass',historical_first_pass_note=old['review_note']))
ledger['reviewed_individually']=1009
assert not any(s['final_accepted'] for s in ledger['shots'])
(A/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (A/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(A/'BATCH_101_MANIFEST.json').write_text(json.dumps({'records':records,'recovered_image_inventory':inventory},indent=2)+'\n')
report='''# Batch101 — IMG1001–1010 (33:20–33:40)

## Result

Ten first-pass native frames plus four recovered revisions individually inspected. Three existing corrections provisionally selected: **1003 revision_02, 1008 revision_03, 1009 revision_03**. No new image generation. **1009/1050 slots reviewed; zero final approvals**. IMG0500 inherited missing/unresolved; all older holds persist.

## Provenance and recovered direction

Recovered EP001_BATCH_101_ALL_REVISIONS_REVIEW_BACKUP.zip, Drive ID 1MeSLpdmW-8XCZViUlcnpgxAfLPhRkBcK, 34,847,802 bytes, MD5 e3c371ceac9de44295b7df70a223576e matched. Archive explicitly says REVIEW BACKUP ONLY, not selected delivery. All ten original hashes/byte sizes match its first-pass manifest. Revision hashes recorded separately; archive checksum establishes transfer integrity, not artistic approval. No separate Drive PNG IDs claimed.

Recovered direction note records a book illustration supplied as inspiration, followed by selection of an original peninsula concept with dense habitation, sculptural towers, bridges and harbor geography. It says not to literally reconstruct the illustration or return to an empty basalt ridge. This is documentary recovery, not direct access to historical conversation. The actual selected concept and book-reference images are not in this ZIP, so exact reference conformity remains unresolved. Do not generalize Batch100 house ensemble permission: first five are inherited principal-intended rear/details, without a certified identity match. Dragon remains off-camera and no new emitted flame is introduced. Preserve full original revision history.

## Script context

Read complete 33:00–34:00 paragraphs and ending context: first five complete refusal to kneel to a Valyrian king or Old Ghis; next five open a reflective pause and acknowledge uncertain dragon origins/Asshai tradition. Absence of literal pyramids in a coastal Valyrian reaction insert is not a script contradiction. Dormant geology and dark fissure are reflective metaphors, not proof of historical origin. No script/map edits, timed audio or timeline synchronization performed.

## Individual findings

'''
for s in records:report+=f"### {s['scene_id']} — {s['audit_status']}\n\n{s['visual_observation']}\n\n{s['editorial_action']}\n\n"
report+='''## Not selected / remaining gates

1003 first pass rejected for masonry-like portal and bright excessive hardware; recovered revision improves these, wardrobe hold remains. 1008 first pass not selected: fortress/bluff lacks inhabited-city reading. 1009 first pass not selected: isolated pointed castle mass; revision_02 not selected: removes castle but leaves empty bluff. Later revision_03 pair selected on its recovered newer direction, not the superseded broad-ridge corrective brief.

All 14 files visually reviewed at returned display resolution and decoded. No blanket magnified anatomy/architecture approval. Native dimensions vary; no delivery conform performed. House doctrine, principal references, architecture style/scale/engineering, matching grades and shoreline continuity remain open. New city direction may require retrospective conformity review of older city frames, including IMG1000; no earlier selection silently cleared or overwritten.

Next Batch102 IMG1011–1020 finishes the 33:30–34:00 uncertainty paragraph. Recover existing versions and direction before generating literal hatchlings or Asshai masters; narration explicitly does not establish those accounts as fact.
'''
(A/'BATCH_101_REVIEW.md').write_text(report)
out=Path('google_drive/EP001_BATCH_101_AUDIT_RECOVERED_SELECTIONS.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as f:
 for p in P.rglob('*'):
  if p.is_file():f.write(p,'recovered_prior/'+str(p.relative_to(P)))
 for p in [A/'BATCH_101_MANIFEST.json',A/'BATCH_101_REVIEW.md',A/'EP001_SHOT_AUDIT_LEDGER.json',A/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:f.write(p)
print(out,out.stat().st_size,md(out))
