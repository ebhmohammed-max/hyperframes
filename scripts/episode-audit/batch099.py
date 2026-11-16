"""Persist Batch099 individually inspected originals and provisional corrections."""
import csv, hashlib, json, zipfile
from pathlib import Path
from PIL import Image
root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
a=root/'audit'; assets=Path('google_drive/batch099')
ids=['1mZPC0LTKQgnx5d3zPIdB4LN5si56xIvT', '1-x1FNJ-Ck0K8TCx5tcCvWklfdNNkYGH7', '1stv4wX4L1hb7IMfWH_CIv_SVRolG0cc5', '1qc8nGJBsVo-inaZpmzANFZmSH91XAcFZ', '1ionGplLZX28-6qcGe8oOrklYxQf5lzxY', '1TG63wWU14E2K1GO_MeewNRX1kDSB-EE7', '1hP9WV0dcYog0_gvX6FZ6cKToAiljCzXW', '1WIjv4878LosjGyt_SkZP5bZC4P6YRX3r', '1UyawDuZSZw5NbBOlizlrcfWzrpYnu6ql', '1Em3bnNqW_CPrW1-Y4H5_7r9-HqcnAZla']
checks=['ef714c69b2aee69ea8e965a44774cf88', 'c1dcd01facfc43d479b9127e0b913f23', '4d73aa802acd483366d2dfa26437e12b', '1d4a91ca16ae8a43c5a1d9d5df8114dd', 'aeed0dfc01f2e924f61e417a34a6f3a9', 'd05372601a290f9191eab52899a21a64', '8faa3e51d6f00ae55a3f95eb3a263568', '1d390a726e970dc7d5b5e8a86c6ff7a1', '40231362f9a1197ca4df901c2286f4df', 'c7e00daa14ead19862ef1b32f85b22a1']
notes=[('REPLACE', 'Standing adult in tailored dark buttoned military-looking uniform addresses long seated council in monumental hall.', 'Uniform reads modern compared with ancient Ghiscari setting; replace human-scale bronze/linen council.'), ('KEEP_CONTEXT_ONLY', 'Serious adult face with gold-brown draped cloth against blurred dark setting.', 'Reaction cutaway supports confident reasoning, not a dragon flesh illustration or named commander. Identity/set continuity unverified.'), ('REPLACE', 'Artificers beside large wheeled timber engine with one huge curved raised beam and rope drums.', 'Ambiguous asymmetrical engine does not clearly read scorpion bolt thrower; replace smaller two-arm torsion layout.'), ('KEEP_CANDIDATE', 'Ranks of arrows, bows and straps on racks in empty workshop courtyard.', 'Supports missile preparation; no actual blinding or successful dragon strike implied. Exact bow design/metallurgy and equipment count unverified.'), ('KEEP_CONTEXT_ONLY', 'High view of neat rectangular blocks of supplies and weapons in large empty courtyard.', 'Military logistics scale motif; individual objects too small to establish bronze arrow volley. New engine and retained arrows carry planning context.'), ('REPLACE', 'Extreme oversized view along timber mechanism with enormous rope bundles and bronze drum over tiny workers.', 'Unclear engineering/scale and tiny exposed light at lower left; misses rider-denial beat. Replace figurine strategy metaphor without emitted fire.'), ('REPLACE', 'Groups of wooden tally sticks arranged beside small balance scale.', 'Not a clear representation or accurate count of forty noble houses; replace kingless assembly with restrained disagreement.'), ('KEEP_CONTEXT_ONLY', 'Bronze-colored helmet with patterned cloth in foreground, spear infantry behind.', 'Can stand for Ghiscari army confidence across full paragraph, not Valyrian crown or king. Anonymous gear only.'), ('KEEP_CANDIDATE', 'Close layered array of spearheads on wooden shafts.', 'Supports spear mass but not exact troop count, bronze composition or triple-spear organization by itself.'), ('KEEP_CANDIDATE', 'Huge dense infantry ranks holding upright spears before brick fortification across a paved approach.', 'Good legion scale closer; exact count, triple-spear distribution, repeated faces and synchronized marching unverified.')]
repl={981: ('Bronze-scale and linen-clothed commanders listen to elder in gold-fringed drapery beside clay dragon model in brick room.', 'Removes modern uniform. Model and meeting invented; not actual dragon autopsy or anatomy reference. Armor/cloth and enlarged hands remain provisional.'), 983: ('Human-scale timber bolt thrower with two lateral arms, paired rope bundles, central guide and rear winch; separate heavy bolt on bench.', 'Clearer scorpion silhouette. Bowstring/trigger alignment, torsion load path and firing operation not certified; PARTIAL_ENGINEERING_HOLD, not functional reconstruction.'), 986: ('Commander points toward separate tiny human figurine beside clay winged reptile and arrowheads.', 'Illustrates denial of riders as strategy, not literal starvation/abuse or proven kill. Model anatomy generic and partly quadruped-like; not live-dragon reference. Hand/armor design held; provisional metaphor.'), 987: ('Silver-haired adult women and men debate as equals at circular dark table with no throne or crown.', 'Kingless disputing-house motif clearer; not exact forty houses or named meeting. Main walls show block joints despite fused-stone request, visible unreadable document markings; PARTIAL_ARCHITECTURE_PROP_HOLD. Wardrobe/identities and full-pixel hands held.')}
ledger=json.loads((a/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==979
manifest=[]
for j,(status,obs,action) in enumerate(notes):
 n=981+j; p=Path(f'google_drive/VAL-EP001-IMG{n:04d}.png'); md=hashlib.md5(p.read_bytes()).hexdigest(); assert md==checks[j]
 with Image.open(p) as im: im.load(); dims=list(im.size)
 s=ledger['shots'][n-1];assert s['scene_id']==p.stem
 s.update(audit_status=status,drive_file_id=ids[j],selected_local_file=str(p),original_local_file=str(p),visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md,reviewed_on='2026-11-15',review_scope='Individually opened at tool display resolution, decoded and MD5 matched; no audio timing or all-pixel anatomy certification.')
 if n in repl:
  rp=assets/f'{p.stem}_v02.png'
  with Image.open(rp) as im:im.load();rd=list(im.size)
  s.update(audit_status=('REPLACED_PARTIAL_ENGINEERING_HOLD' if n==983 else 'REPLACED_PARTIAL_ARCHITECTURE_PROP_HOLD' if n==987 else 'REPLACED_PROVISIONAL'),selected_local_file=str(rp),replacement_file=str(rp),replacement_md5=hashlib.md5(rp.read_bytes()).hexdigest(),replacement_dimensions=rd,replacement_observation=repl[n][0],replacement_review=repl[n][1])
 manifest.append(dict(s,native_dimensions=dims,native_bytes=p.stat().st_size))
ledger['reviewed_individually']=989
(a/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (a/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(a/'BATCH_099_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
report="""# Batch099 — IMG0981–0990 (32:40–33:00)

Ten originals individually viewed, decoded and matched to Drive MD5. Four generated v02 versions individually viewed and selected provisionally. 989/1050 slots reviewed; zero final approvals.

## Full paragraph context (32:30–33:00)

Ghiscari commanders confidently weigh their neighbor under Harpy symbolism, reasoning dragons are flesh and can be brought down by scorpion bolts, blinded by bronze-tipped arrows or deprived of riders. They contrast forty squabbling kingless houses with tens of thousands behind triple spears. These are their assumptions, not verified successful tactics or a battle outcome. Prior paragraph presents dragon danger/prize; next shifts to Valyrian defiance and eastern war-galleys. Script/map unchanged; still selections not timed timeline edits; no audio timing verified.

## Individual decisions

"""
for s in manifest:
 report+=f"### {s['scene_id']} — {s['audit_status']}\n\nObserved original: {s['visual_observation']}\n\n{s['editorial_action']}\n\n"
 if s.get('replacement_observation'):report+=f"Selected v02: {s['replacement_observation']}\n\nRemaining hold: {s['replacement_review']}\n\n"
report+="""## Remaining gates and storage

0983 engine remains PARTIAL_ENGINEERING_HOLD; 0987 council remains PARTIAL_ARCHITECTURE_PROP_HOLD. 0981/0986 are provisional illustrations. Figurines are planning metaphors, not approved dragon anatomy. No exact forty-house count, tens-of-thousands census, triple-spear pattern or actual marching certified. New images add no visible flame, magic glow or battle injury; original 0986 small exposed light is excluded by replacement. All older missing-image, mechanics, geography, wardrobe and creature holds remain. Final delivery requires enlarged anatomy and props review, engineering/design conformity, sequence grade and timed narration gate.

Full-resolution corrections staged under excluded google_drive/batch099 and preserved in uploaded batch ZIP, with manifest paths/checksums. Restore archive from upload receipt if local staging missing. Earlier media/originals untouched.

Next Batch100 IMG0991–1000 (33:00–33:20): Valyrian defiance and gathering eastern galleys; read complete 33:00–33:30 paragraph first.
"""
(a/'BATCH_099_REVIEW.md').write_text(report)
z=Path('google_drive/EP001_BATCH_099_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as out:
 for s in manifest:
  out.write(s['original_local_file'])
  if s.get('replacement_file'):out.write(s['replacement_file'])
 for p in [a/'BATCH_099_REVIEW.md',a/'BATCH_099_MANIFEST.json',a/'EP001_SHOT_AUDIT_LEDGER.json',a/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:out.write(p)
print(z,z.stat().st_size,hashlib.md5(z.read_bytes()).hexdigest())
assert not any(s['final_accepted'] for s in ledger['shots'])
