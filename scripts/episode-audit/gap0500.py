"""Create provenance-safe selection record for missing0500; never count missing original as reviewed."""
import csv,hashlib,json,zipfile
from pathlib import Path
from PIL import Image
A=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/audit');p=Path('google_drive/gap0500/VAL-EP001-IMG0500_gapfill_v01.png');md=lambda p:hashlib.md5(p.read_bytes()).hexdigest()
l=json.loads((A/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert l['reviewed_individually']==1049
s=l['shots'][499];assert s['scene_id']=='VAL-EP001-IMG0500' and s['audit_status']=='MISSING_SOURCE_NOT_REVIEWED'
with Image.open(p) as im:im.load();dims=list(im.size)
s.update(audit_status='MISSING_ORIGINAL_GAPFILL_PROVISIONAL_HOLD',source_recovery_status='Original still missing/unreviewed; new generated candidate only',drive_file_id=None,original_local_file=None,selected_local_file=str(p),replacement_file=str(p),native_checksum_verified=False,native_md5=None,original_individually_reviewed=False,replacement_individually_reviewed=True,replacement_md5=md(p),replacement_dimensions=dims,replacement_status='PROVISIONAL_CONTEXT_GEOGRAPHY_HOLD',final_accepted=False,reviewed_on='2026-11-15',visual_observation='Missing original cannot be described. New gapfill: rear silver-haired wool-cloaked adult-intended shepherd faces irregular dark cavern opening; blurred green pasture/sheep at left, narrow pale daylight sliver within opening.',editorial_action='Select gapfill_v01 provisionally for16:38–16:40, after complete16:30–17:00 paragraph review. Suggests uncertainty between pastoral life and unknown cavern arts, not proven eastern teachers or attested initiation. No visible spell, glyph, dragon or flame. New sheep and inner daylight sliver differ slightly from prompt; geography/cast/adjacent-shot continuity and timed sequence remain held. Original source remains missing and not counted as reviewed.',replacement_basis='Two active Drive filename searches found no0500 image; source folder listing still nine0491–0499, no next page. Historical Batch050 partial ZIP contains nine originals and0498_v02 only.',review_scope='New generated gapfill individually opened at returned display resolution and decoded; no all-pixel/reference certification. Source0498_v02 and0499 independently reopened for context. Not a recovered-original review.')
l['selected_candidate_coverage_slots']=sum(bool(x.get('selected_local_file')) for x in l['shots']);l['reviewed_individually']=1049
assert not any(x['final_accepted'] for x in l['shots'])
(A/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(l,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for x in l['shots'] for k in x))
with (A/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(l['shots'])
with (A/'UNACCEPTED_SHOTS_QUEUE.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['scene_id','timestamp','audit_status','selected_local_file','replacement_file','editorial_action'],extrasaction='ignore');w.writeheader();w.writerows(l['shots'])
(A/'GAP_0500_MANIFEST.json').write_text(json.dumps({'selection':s,'new_candidate_bytes':p.stat().st_size,'new_candidate_md5':md(p),'new_candidate_dimensions':dims,'source_archive_drive_id':'1WnX6TSBElldanbOWewBhy8exrH2FH4Q6','source_archive_md5':'ae59a68eec101cb6f332f032cdb71ace','source_folder_drive_id':'1Atkd3zScJVgA9M8Mr1IPTX6UOk2QlWeC','reviewed_originals':1049,'selected_path_coverage':l['selected_candidate_coverage_slots'],'final_accepted':0},indent=2)+'\n')
(A/'GAP_0500_REVIEW.md').write_text('''# Missing IMG0500 — transparent provisional gap fill

## Outcome

New **VAL-EP001-IMG0500_gapfill_v01.png** generated, individually viewed and provisionally selected for16:38–16:40. It is NOT a recovered original. **1049 originals/slots remain recorded as reviewed; original0500 remains missing/unreviewed; zero final approvals.** New selected-path coverage recorded separately rather than inflating original-review count. A ledger path is not proof every historical media file is locally available or approved.

## Recovery evidence

Two current active Drive searches: IMG0500/BATCH050 query found source folder and historical partial audit, no0500 image; broader0500/IMG500 query returned only source folder. Direct source folder1Atkd3zScJVgA9M8Mr1IPTX6UOk2QlWeC returned nine0491–0499 originals, no next page. This is scoped negative search evidence, not proof file cannot exist in trash/other accounts/archives.

Downloaded historical partial ZIP1WnX6TSBElldanbOWewBhy8exrH2FH4Q6,42,165,973 bytes,MD5 ae59a68eec101cb6f332f032cdb71ace matched. It has nine originals and0498_v02, no0500. Historical ledger inside ZIP was NOT restored over cumulative current ledger. Independently reopened0498_v02 pastoral candidate and0499 cavern original for context, plus read current ledger0495–0505. Earlier0498 remains candidate-only in inherited ledger; this turn does not silently promote it.

## Script and choice

Read16:00–16:30 skeptical-scholar paragraph, full16:30–17:00 alternative-origin paragraph, and following horn/spell/blood discussions. Slot says “sorcery. Whether sparked by”; narration explicitly offers eastern teaching, survival and centuries of trial as alternatives. Image therefore uses a rear anonymous adult-intended silver-haired shepherd confronting a naturally dark cave, not a factual eastern lesson, formal initiation, magic demonstration, known principal or approved dragon.

Generated result inspected: coarse dark wool and loose silver hair foreground, no visible face/hands; blurred pasture and sheep behind, irregular cavern entrance with small pale daylight sliver. No obvious emissive flame, glyph, horn, dragon, injury or blood. Inner pale sliver reads daylight opening rather than requested completely opaque darkness; not called magical light. Sheep were added by generator. No blanket anatomy/material/pixel certification.

## Holds

Geographic and cast continuity with existing ritual-heavy0499/0501 remains unresolved: gapfill does not repair those neighbors. It intentionally does not replicate their questionable formal ordeal. Governing principal/creature direction not recovered and no identity match claimed. This new metaphor still needs timed sequence/pacing review. Script/map unchanged; no audio/timeline edits or final conform/acceptance.

## Next

Original recovery remains open, but there is now an inspected provisional gap-fill selection. Resume substantive mismatch correction queue chronologically, starting earliest unresolved replacement/recommended correction, not assume chronological pass fixed all earlier mismatches. Current queue regenerated without clearing older holds. End-pass reconciliation files are historical pre-gap checkpoint; this addendum supersedes only0500's empty-selection state, not the1049 original-review or zero-approval totals. Historical generated-candidate counter still unreconciled, not quoted as total.
''')
out=Path('google_drive/EP001_GAP0500_PROVISIONAL_AUDIT.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 z.write(p)
 for name in ['GAP_0500_REVIEW.md','GAP_0500_MANIFEST.json','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv','UNACCEPTED_SHOTS_QUEUE.csv']:z.write(A/name)
 z.write(Path(__file__))
print(out,out.stat().st_size,md(out));print('Selected-path coverage',l['selected_candidate_coverage_slots'])
