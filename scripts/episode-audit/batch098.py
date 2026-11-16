"""Persist Batch098 individually inspected originals and provisional corrections."""
import csv, hashlib, json, zipfile
from pathlib import Path
from PIL import Image
root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
a=root/'audit'; assets=Path('google_drive/batch098')
ids=['1InjccndORiQwgUqB_NLdL49lCsAYL8ei', '1GCKbL-P9Tlv1JFTT-8cCDzBqOgl302-7', '10jJNGxaQcrOiHFG0xH0kDmUoU5cuQ1KM', '1y_7My2Vt9Z0ymNVGSOQX8QT-MKHTa9uA', '1HqwV1LGDjj___XChiAn4q7bsDVUuN3Et', '1wNaCpGFtH73fhje77jCS6mGSPrgzTvMw', '1ZACyh3uRCjuufxQAIIK2JrRIDNuL4zDF', '1ADGSUIYQ0ShiOqDfucii4npLE-ezyMN7', '1E6rzByN43GVys9UMb0BfcQFaamRRD1Yd', '1IU_LrwSQzxZIZVc0kEs2xkw0c32Eb6-G']
checks=['9956d890a3a5bf76e001753b8f5d966e', 'cb841a27c1d5a52f59c10ce89a31d7d9', '25a3f26b0b5a4aeaaccdeba4ef08c842', '355ff69089705801dd774b9901917192', 'ee5a7ebe68bf1fe74cc3d3357fd67d83', '26fcfbc5b512afe28059cd8676c09610', '48b4cd21aa47d9218305851d50920ebf', '812fbe5840ce1c719c75e9d6d331c760', '0b92f4fb08bfdf68e11d7ccbcdd701b2', '28a8520f3f3d0495428e7de422d6c459']
notes=[('REPLACE', 'Low view of tall tapering brick tower and armored human statue with medieval-looking closed helmet and plate forms.', 'Weak warlord introduction and unsuitable armor language; replace report reception by bronze-equipped commanders.'), ('KEEP_CONTEXT_ONLY', 'Bronze-colored pointed projectiles in fitted dark tray.', 'Can foreshadow later bolt/arrow plans within full context; projectile scale, metallurgy and launcher type not proven. Avoid presenting already successful dragon kill.'), ('KEEP_CANDIDATE', 'Older adult with short gray hair, earring and gold-fringed cloth looks stern with hand under chin.', 'Supports danger/concern reaction. Anonymous warlord not named historical person; wardrobe and hand anatomy held.'), ('REPLACE', 'Open empty red-lined dark chest with small ring near edge.', 'Empty box is weak symbol for coveted living dragons; replace explicitly metaphorical dragon figurine and reaching hand.'), ('KEEP_CONTEXT_ONLY', 'View from dark dock toward pale distant cliffs across broad blue water.', 'Inter-imperial water bridge only; not literal Gulf width, exact opposite shore, ice/snow geography or Ghis ownership proof.'), ('KEEP_CONTEXT_ONLY', 'Low angle on upper courses of tiered dark brick building.', 'Supports Ghis brick/pyramid context, but does not depict Harpy thunderbolt. New council emblem carries intended symbol only provisionally.'), ('KEEP_CONTEXT_ONLY', 'Two turbaned adults overlook huge distant rectangular troop formations.', 'Commander/army-scale motif; headwear invented and not canonical uniform. Exact troop count, anatomy and geography unverified.'), ('REPLACE', 'Rows of seated dark-clothed adults face empty doorway in long vaulted hall.', 'No clear active war council or appraisal of neighbor; replace human-scale planning discussion.'), ('REPLACE', 'Long empty avenue and spear-like lines among repeated tiered tiled roof buildings.', 'Roof forms suggest unrelated East Asian architectural grammar and spear racks not clear army. Replace brick city and actual infantry ranks.'), ('KEEP_CANDIDATE', 'Armored forearms and hands rest along dark reflective council table beside bowl.', 'Useful restrained confidence/decision insert; armor and full-pixel hands unverified. Not proof agreement or victory.')]
repl={971: ('Three bronze-scale-equipped adults listen to mariner at wooden table with clay creature and ship models in brick harbor room.', 'Removes medieval statue and makes warlords active. Anonymous staged report, not documented event; toy creature generic, armor/wardrobe and enlarged hands still held. Provisional selection.'), 974: ('Small metal winged reptile figurine beside gold-colored pieces with adult hand reaching toward its tail.', 'Prize metaphor clearer; not an actual captive dragon or canonical treasure. Figurine has quadruped-like anatomy plus wings and is not live-creature reference; ornate sleeve/coins/hand require design gate. Provisional metaphor only.'), 978: ('Five commanders confer around table with clay dragon, heavy projectile and spear, winged relief behind.', 'Council beat clearer. Relief reads bird-headed rather than clear female-headed harpy; thunderbolt partly legible. Some armor resembles sculpted plate, and dragon model is generic. PARTIAL_ICONOGRAPHY_ARMOR_HOLD; do not certify canonical emblem or uniform.'), 979: ('Two bronze-helmeted observers overlook dense infantry ranks in flat-roof brick city below stepped pyramid.', 'Corrects unrelated roof grammar and empty weapon lines. Repeated figures, gear/limbs, exact spear formation and military count remain PARTIAL_FORMATION_ANATOMY_HOLD. City layout interpretive, no lockstep motion proven.')}
ledger=json.loads((a/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==969
manifest=[]
for j,(status,obs,action) in enumerate(notes):
 n=971+j; p=Path(f'google_drive/VAL-EP001-IMG{n:04d}.png'); md=hashlib.md5(p.read_bytes()).hexdigest(); assert md==checks[j]
 with Image.open(p) as im: im.load(); dims=list(im.size)
 s=ledger['shots'][n-1];assert s['scene_id']==p.stem
 s.update(audit_status=status,drive_file_id=ids[j],selected_local_file=str(p),original_local_file=str(p),visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md,reviewed_on='2026-11-15',review_scope='Individually opened at tool display resolution, decoded and MD5 matched; no audio timing or all-pixel anatomy certification.')
 if n in repl:
  rp=assets/f'{p.stem}_v02.png'
  with Image.open(rp) as im:im.load();rd=list(im.size)
  s.update(audit_status=('REPLACED_PARTIAL_ICONOGRAPHY_ARMOR_HOLD' if n==978 else 'REPLACED_PARTIAL_FORMATION_ANATOMY_HOLD' if n==979 else 'REPLACED_PROVISIONAL'),selected_local_file=str(rp),replacement_file=str(rp),replacement_md5=hashlib.md5(rp.read_bytes()).hexdigest(),replacement_dimensions=rd,replacement_observation=repl[n][0],replacement_review=repl[n][1])
 manifest.append(dict(s,native_dimensions=dims,native_bytes=p.stat().st_size))
ledger['reviewed_individually']=979
(a/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (a/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(a/'BATCH_098_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
report="""# Batch098 — IMG0971–0980 (32:20–32:40)

Ten originals individually viewed, decoded and matched to Drive MD5. Four generated v02 versions individually viewed and selected provisionally. 979/1050 slots reviewed; zero final approvals.

## Full-paragraph context

32:00–32:30 describes Valyrian wealth, captive-market prices, refused Bronze Harpy homage and tamed dragons as both danger and prize in Ghiscari eyes. 32:30–33:00 describes confident Ghiscari commanders reasoning dragons could be killed by scorpion bolts/arrows or deprived of riders, contrasting forty kingless houses with huge legion armies and triple spears. Following paragraph shifts to Valyrian refusal to submit. Current batch spans both paragraphs; no victory or actual successful dragon killing should be implied. Script/map unchanged; no audio timing or timeline edits verified.

## Individual decisions

"""
for s in manifest:
 report+=f"### {s['scene_id']} — {s['audit_status']}\n\nObserved original: {s['visual_observation']}\n\n{s['editorial_action']}\n\n"
 if s.get('replacement_observation'):report+=f"Selected v02: {s['replacement_observation']}\n\nRemaining hold: {s['replacement_review']}\n\n"
report+="""## Remaining gates and storage

0978 iconography/armor and 0979 formation/anatomy retain PARTIAL holds. 0971/0974 provisional, not certified masters. Report/council events, model objects and geography are interpretive production choices. Figurines are not live-dragon anatomy references; 0974 has four-leg toy grammar. The council relief is not approved canonical Harpy design. No exposed flame, magic glow or battle violence added. Prior missing-image, mechanics, road, city-style, wardrobe and creature holds persist. Final gates include enlarged anatomy/props, reference matching, sequence grade and timed narration.

New full-resolution corrections are stored under google_drive/batch098 (excluded local media staging) and preserved in this batch Drive ZIP, rather than further inflating Git media. Manifest records exact paths/checksums; retrieve ZIP using upload receipt if staging is unavailable. No existing original or earlier selected asset was removed.

Next Batch099 IMG0981–0990: Ghiscari assumptions about dragon flesh, scorpion bolts, arrows, rider denial, forty houses and legion triple spears. Read full 32:30–33:00 paragraph before review.
"""
(a/'BATCH_098_REVIEW.md').write_text(report)
z=Path('google_drive/EP001_BATCH_098_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as out:
 for s in manifest:
  out.write(s['original_local_file'])
  if s.get('replacement_file'):out.write(s['replacement_file'])
 for p in [a/'BATCH_098_REVIEW.md',a/'BATCH_098_MANIFEST.json',a/'EP001_SHOT_AUDIT_LEDGER.json',a/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:out.write(p)
print(z,z.stat().st_size,hashlib.md5(z.read_bytes()).hexdigest())
assert not any(s['final_accepted'] for s in ledger['shots'])
