"""Second-pass opening correction selections; does not rerun chronological builders."""
import csv,hashlib,json,zipfile
from pathlib import Path
from PIL import Image
A=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/audit');D=Path('google_drive/correction001');md=lambda p:hashlib.md5(p.read_bytes()).hexdigest()
l=json.loads((A/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert l['reviewed_individually']==1049
notes={
1:('REPLACED_PARTIAL_CREATURE_HOOK_HOLD','Large dark wyvern-like dragon and rear silver-haired leather/wool-clothed adult on coastal ledge in warm dawn rim light.','Replaces empty rock slab with editorial future-power teaser, not chronological assertion that shepherds already rode dragons. Stronger hook; mature creature identity, folded wing articulation, tail cropping, person-to-dragon scale and costume remain held. No Aegon/principal identity claimed.'),
2:('REPLACED_PROVISIONAL_CONTEXT_HOLD','Overlapping gray steel-looking swords with leather hilts and crossguards on dark stone in warm light.','Replaces bronze spear/axe/copper dagger insert under surrendered-blades line. Illustrative comparison to later conquest, not literal thousand count, verified Iron Throne construction or early Valyrian steel artifact. Blade/guard intersections and period design remain held.'),
5:('REPLACED_PARTIAL_PASTORAL_CONTINUITY_HOLD','Two rear silver-haired cloaked adults lead sheep toward low fieldstone sheepfold in green/gold volcanic foothills.','Replaces third successive landscape with contextual pastoral humanity. Not labeled Westeros or named shepherds. Staff carried across shoulder, not planted; hands, flock overlaps/anatomy, sheepfold timber and chronology relative to spoken Westeros clause remain held. Timed montage review required.'),
9:('REPLACED_PARTIAL_CRAFT_CAST_HOLD','Woman in plain brown wool and headcloth handles large fleece at rustic hut; rear silver-haired adult carries wicker basket toward sheepfold.','Replaces another volcanic scenery insert with humble work before Valyria name reveal. Woman hair largely covered, visible wisps pale but full silver-hair conformity not certified. Hand/fleece contact, basket grip, timber construction and grade/geography continuity held; no specific textile technique or named identity claimed.')}
records=[]
for n,(status,obs,action) in notes.items():
 s=l['shots'][n-1];old=dict(s);p=D/f'VAL-EP001-IMG{n:04d}_v02.png';o=Path(f'google_drive/VAL-EP001-IMG{n:04d}.png')
 with Image.open(p) as im:im.load();dims=list(im.size)
 with Image.open(o) as im:im.load();odims=list(im.size)
 if n==1:assert md(o)=='6b7a710fc0a7c60b0ff2f432d0ea31a0'
 s.update(audit_status=status,original_local_file=str(o),selected_local_file=str(p),replacement_file=str(p),replacement_md5=md(p),replacement_dimensions=dims,replacement_status=status,replacement_individually_reviewed=True,prior_visual_observation=old['visual_observation'],visual_observation=obs,editorial_action=action,reviewed_on='2026-11-15',final_accepted=False,review_scope='Four originals downloaded/reopened; four new versions individually opened at returned display resolution and decoded. Original0001 MD5 matched current Drive metadata; other original hashes newly recorded without fresh independent Drive checksum comparison. Inherited original verification not represented as new verification. No all-pixel, named-reference, timeline or audio timing certification.')
 records.append({'scene_id':s['scene_id'],'timestamp':s['timestamp'],'prior_ledger_row':old,'current_ledger_row':dict(s),'original_md5_this_pass':md(o),'original_dimensions':odims,'original_fresh_drive_md5_match':True if n==1 else None,'selected_bytes':p.stat().st_size})
assert l['reviewed_individually']==1049 and not any(s['final_accepted'] for s in l['shots'])
(A/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(l,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in l['shots'] for k in s))
with (A/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(l['shots'])
with (A/'UNACCEPTED_SHOTS_QUEUE.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['scene_id','timestamp','audit_status','selected_local_file','replacement_file','editorial_action'],extrasaction='ignore');w.writeheader();w.writerows(l['shots'])
(A/'CORRECTION_001_MANIFEST.json').write_text(json.dumps(records,indent=2)+'\n')
report='''# Correction pass001 — opening priorities

Four unresolved substantive opening items versioned and provisionally selected: **IMG0001,0002,0005,0009**. Four downloaded originals independently reopened and four new candidates individually inspected/decoded. This is a second-pass correction set, NOT four newly counted original reviews. **1049 original reviews unchanged;1050 selected paths;zero final approvals.** Missing0500 original and all older holds remain.

## Narrative rationale

Read complete00:00–00:30 opening and00:30–01:00 transformation question, plus following chapter context. Opening explicitly juxtaposes much later Iron Throne/Aegon with Valyria's remote rise.0001 is an editorial flash-forward teaser to mature dragon power, not evidence of riding before discovery.0002 illustrates later surrendered swords, not Bronze-Age tools literally forged into steel throne.0005/0009 insert humble pastoral labor to break repeated scenery and set up transformation; these contextual Valyrian inserts under comparative clauses are not labeled Westeros. Their exact rhythm/chronology requires actual audio/timeline review. No script or map changes or added spoken labels.

Warm sandstone dawn/navy shadows retained for opening; later ChapterVII cold/dormant rules not retroactively imposed. No fire/emitter introduced. Governing creature/principal references remain unrecovered, anonymous cast/design studies only. Original opening source assets preserved, not relocated or deleted. No final delivery conform.

## Findings

'''
for r in records:
 s=r['current_ledger_row'];report+=f"### {s['scene_id']} — {s['audit_status']}\n\nOriginal: {s['prior_visual_observation']}\n\nNew: {s['visual_observation']}\n\n{s['editorial_action']}\n\n"
report+='''## Verification / next

Original0001 current Drive size/MD5 matched:2374077 bytes,6b7a710fc0a7c60b0ff2f432d0ea31a0. Other original hashes recorded locally; inherited verification retained but no fresh independent metadata checks claimed for them. All new hashes/dimensions in manifest. All eight inspected at returned display resolution; no blanket magnified anatomy/material certification.0001 full tail not visible despite intended visible tail; creature scale less monumental than requested.0009 headcloth hides most hair; these remain explicit partial holds, not prompts treated as QC success.

Next continue chronological correction triage fromIMG0011 onward; conditional0003/0004/0006–0008/0010 still need sequence/detail review and are NOT silently final-approved. Resolve substantive earlier mismatches while preserving partial versions. This package includes cumulative queue with exact row actions; do not interpret selected-path coverage as verified local availability of all prior external assets. Historical end-pass status-count report is a checkpoint, not refreshed totals after second-pass changes. Do not rerun old batch builders or quote unreconciled historical generation count.
'''
(A/'CORRECTION_001_REVIEW.md').write_text(report)
out=Path('google_drive/EP001_CORRECTION_PASS_001_OPENING.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for n in notes:
  for p in [Path(f'google_drive/VAL-EP001-IMG{n:04d}.png'),D/f'VAL-EP001-IMG{n:04d}_v02.png']:z.write(p)
 for name in ['CORRECTION_001_MANIFEST.json','CORRECTION_001_REVIEW.md','EP001_SHOT_AUDIT_LEDGER.json','EP001_SHOT_AUDIT_LEDGER.csv','UNACCEPTED_SHOTS_QUEUE.csv']:z.write(A/name)
 z.write(Path(__file__))
print(out,out.stat().st_size,md(out))
