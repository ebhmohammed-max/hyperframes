"""Persist Batch095 individually inspected originals and provisional corrections."""
import csv, hashlib, json, zipfile
from pathlib import Path
from PIL import Image
root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
a=root/'audit'; assets=Path('assets/episode_audit/batch095')
ids=['1Myq6pexwFWmPrGp33HroHHTFUL-Be7lM', '1dhZH95XhccBc8yIxIWaEcJ1xDdRRsV-s', '1GZdYSC5YXjtS7FfPevo6HXpwEW5ighvd', '1sjlauWC2eSbaAmXKlO3CbpKteshPUl5-', '1KWJwM3OdP7NC2m1AqFgYuVVX9XPuYsCI', '15xt0E2xG_HMCCfxoiWdeDk_q02TEOkqM', '1eb1vvGl4UnMzUnrNooZre7EwN9CrDG6h', '135P3lDzrrDZsC8XT_JyCPPJ-toxVhId_', '1a3OitnQLQMUy462TNj75lIsHNooA__2G', '1sSPBPNv0E2sWRZObe-6Xs1qtTvo7jHPb']
checks=['52265316826efd95b2e3a43e3b9c8ee9', '0082cd0ea86da6ce987ee4d9ec9e9759', '56a01dde23eafeff8e2d4e606b3c9217', 'fb547e9756a7fd8be4789091c80d6f46', '242be2056d4edad05ec23b76fd65515f', '9037a9c1a10e411f31704b25b05dc953', '00907f700cb11f3ae983f4c17b909495', '597da64a58bf57fa42d64822ed64f4d1', '6447538d3ae41cb5d602e15bae2f51d4', '6a6b7cc1427396008113b36d804f3649']
notes=[('REPLACE', 'Grassland beneath long vertical basalt cliffs with two tiny bird-like flying marks.', 'Does not clearly establish dragon over volcanic peak; replace readable winged reptile.'), ('KEEP_CONTEXT_ONLY', 'Feather caught in thorny grass beside water and distant plateau.', 'Literal hawk comparison/pasture insert only; feather is not evidence dragons have feathers. Do not imply exact location or a dragon artifact.'), ('KEEP_CONTEXT_ONLY', 'Small waves wash dark rock and shell fragment with distant opposite shore.', 'Supports water crossing transition, not measured Gulf of Grief width or exact coastline.'), ('REPLACE', 'Barnacled timber, tangled encrusted rope and broken pottery on wet sand.', 'Beach debris does not carry shift toward imperial listener; replace with Ghiscari report reception.'), ('KEEP_CONTEXT_ONLY', 'Hazy coastal settlement with distant pyramid silhouettes along broad water.', 'Can bridge into Ghis, but geometry and apparent pointed pyramid forms not a certified city model. Not proof actual Gulf geography.'), ('KEEP_CANDIDATE', 'Large tiered brick monumental building beside water with palms and tiny figures.', 'Strong stepped-brick Ghis introduction. Interpretive structure not exact capital plan; no need to call it Grazdan palace.'), ('KEEP_CANDIDATE', 'Older adult in brown gold-edged drapery observes crowded low oared vessels from brick terrace.', 'Supports patrician and naval wealth in full paragraph. Gold fringe/tokar construction, bronze rams and transport purpose not established at this distance.'), ('REPLACE', 'Almost empty gridded city with repeated pyramids and low flat masonry structures.', 'Reads abandoned archaeological site rather than living imperial capital; replace with populated brick harbor city.'), ('KEEP_CONTEXT_ONLY', 'High pyramid terrace overlooks vast coastal plains, thin routes, scattered settlements and distant vessels.', 'Suggests imperial scale, not independently verified centuries of rule, central Essos map or practical sightline. Keep brief.'), ('KEEP_CANDIDATE', 'Adult in red draped gold-fringed garment and earring beside brick colonnade.', 'Useful anonymous patrician portrait. Not Grazdan himself or proven descendant identity; exact tokar wrap design held.')]
repl={941: ('Clearly visible large winged reptilian creature above green valley and jagged mountain slopes.', 'More readable dragon than original. Creature is much larger in frame than requested; full anatomy, wing attachment, flight pose and design match with 0940_v03 remain PARTIAL_CREATURE_HOLD. Mountain volcanism not provable from appearance.'), 944: ('Three richly draped adults listen gravely to a plain-clothed mariner on brick harbor terrace.', 'Stronger imperial-listener beat, an invented report scene not named event. Gold-edged cloth not certified tokar; background pyramid has pointed smooth upper cap rather than fully stepped silhouette. PARTIAL_WARDROBE_ARCHITECTURE_HOLD; human hands/faces full-pixel gate remains.'), 948: ('Populated brick city with tiered monuments, crowded market street and active harbor with low wooden ships.', 'Corrects deserted city read. Plan is invented; terrace rail, vessel mechanics and monument forms need production-design match. Different city layout from 0915/0944/0946, not continuous surveyed geography; provisional only.')}
ledger=json.loads((a/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==939
manifest=[]
for j,(status,obs,action) in enumerate(notes):
 n=941+j; p=Path(f'google_drive/VAL-EP001-IMG{n:04d}.png'); md=hashlib.md5(p.read_bytes()).hexdigest(); assert md==checks[j]
 with Image.open(p) as im: im.load(); dims=list(im.size)
 s=ledger['shots'][n-1];assert s['scene_id']==p.stem
 s.update(audit_status=status,drive_file_id=ids[j],selected_local_file=str(p),original_local_file=str(p),visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md,reviewed_on='2026-11-15',review_scope='Individually opened at tool display resolution, decoded and MD5 matched; no audio timing or all-pixel anatomy certification.')
 if n in repl:
  rp=assets/f'{p.stem}_v02.png'
  with Image.open(rp) as im:im.load();rd=list(im.size)
  s.update(audit_status=('REPLACED_PARTIAL_CREATURE_HOLD' if n==941 else 'REPLACED_PARTIAL_WARDROBE_ARCHITECTURE_HOLD' if n==944 else 'REPLACED_PROVISIONAL'),selected_local_file=str(rp),replacement_file=str(rp),replacement_md5=hashlib.md5(rp.read_bytes()).hexdigest(),replacement_dimensions=rd,replacement_observation=repl[n][0],replacement_review=repl[n][1])
 manifest.append(dict(s,native_dimensions=dims,native_bytes=p.stat().st_size))
ledger['reviewed_individually']=949
(a/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (a/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(a/'BATCH_095_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
report="""# Batch095 — IMG0941–0950 (31:20–31:40)

Ten originals individually viewed, decoded and matched against Drive MD5. Three generated v02 corrections individually viewed and selected provisionally. 949/1050 original slots reviewed; zero final approvals.

## Full-paragraph context

31:00–31:30: returning sailors spread reports of seamless towers, silver-haired nobles with plum eyes, dragons circling volcanic peaks like hawks above pasture. Across Gulf of Grief an empire listens with displeasure. 31:30–32:00 introduces Old Ghis, heirs of Grazdan, centuries of rule, stepped brick pyramids, gold-fringed tokars, bronze-rammed galleys/slave transports, law/brick/chains/lockstep legions. This batch spans the paragraph boundary. Next paragraph concerns Valyrian wealth, captive prices and Ghiscari alarm at dragons.

Script and 1050-shot map remain unchanged. This is selection audit, not actual timeline replacement; no audio timing verified.

## Individual decisions

"""
for s in manifest:
 report+=f"### {s['scene_id']} — {s['audit_status']}\n\nObserved original: {s['visual_observation']}\n\n{s['editorial_action']}\n\n"
 if s.get('replacement_observation'):report+=f"Selected v02: {s['replacement_observation']}\n\nRemaining hold: {s['replacement_review']}\n\n"
report+="""## Remaining gates

0941 creature anatomy/pose/design continuity and 0944 wardrobe/background-pyramid conformity remain PARTIAL holds. 0948 is provisional living-city improvement, not a locked geographic reconstruction. No new flames, eye glow or magic effects. Single dragon still cannot prove circling motion or plural creatures. Retained feather insert is hawk-comparison imagery only. Reports, anonymous identities and city layout are production interpretation, not independently verified historical event. Prior 0885 mechanics, 0918 road and all city/creature holds remain unresolved. Originals preserved. Final acceptance requires reference/design match, enlarged anatomy/rigging review, sequence grade/geographic continuity, and timed narration inspection.

Next Batch096 IMG0951–0960: shaded terraces, stepped pyramids, gold-fringed tokars, naval harbor and lockstep legions. Check actual originals before certifying clothing or naval types.
"""
(a/'BATCH_095_REVIEW.md').write_text(report)
z=Path('google_drive/EP001_BATCH_095_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as out:
 for s in manifest:
  out.write(s['original_local_file'])
  if s.get('replacement_file'):out.write(s['replacement_file'])
 for p in [a/'BATCH_095_REVIEW.md',a/'BATCH_095_MANIFEST.json',a/'EP001_SHOT_AUDIT_LEDGER.json',a/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:out.write(p)
print(z,z.stat().st_size,hashlib.md5(z.read_bytes()).hexdigest())
assert not any(s['final_accepted'] for s in ledger['shots'])
