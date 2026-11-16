"""Persist Batch097 individually inspected originals and provisional corrections."""
import csv, hashlib, json, zipfile
from pathlib import Path
from PIL import Image
root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
a=root/'audit'; assets=Path('assets/episode_audit/batch097')
ids=['1C-A1qhyGzsk9FjopCIZ6oUymZX5B1UO7', '1xF4Mt92VfOhnZHkw3HvANeGazeFx77kg', '1Jxr3NafO8ub_XzgI6QRjp5NcLefNKMoB', '16SHtfVhaMEupcDnthPLGnDeHi_SYFP4F', '1yjiECHFvJ1L-E3RQdwwsjFpfT4sYTHZI', '1RA7POZv6Ic6Q0QbA28MSiQI2uXNNvZQm', '1Jd3fTSY-jArrXpLrg7ybHH3OhzuY12Lm', '1m91BURsCVxm1nMoBPle9qluHNG8Em271', '1wCuqPW8BOI-p9ks8Ku0oF6hPS0g8wvdM', '1OikpSk5gLTGDxdIaaN2hBIXqMX_m8HN0']
checks=['30ceb248334880367c5d5b2b6011a003', '567a31bbd0135942034a1b4551480ae3', '9febbee3f64f374b5fdb143c8c58f7f1', '87287b8335631c933737101c0a93eff6', '6393ecf0042bb8a90f7a2be68905d448', '4f6ab76d3e357b836ffe9fdb54126400', '35f54f496ed2fd6dbb7c13c0c7d97922', '6f98a3edaea6bbb8d05357c4811f1eb8', 'eab416e02aefe95c7fbe9e26c1a01cfa', 'b7293996fb3795a9abef71e09833fa55']
notes=[('KEEP_CONTEXT_ONLY', 'Brick parapet faces huge rocky mountain across narrow water with terraced low structures.', 'Water/rival-resource transition only. Do not label opposing shores Ghis and Valyria: frame suggests narrow local channel, not established Gulf of Grief geography.'), ('KEEP_CONTEXT_ONLY', 'Gold-draped adult observes terraced quarry slope across water.', 'Can imply Ghiscari concern over rival extraction, not literal view from Ghis to Valyrian mine. Wardrobe, identity and quarry mineral remain unverified.'), ('REPLACE', 'Abandoned timber hut and empty animal pen beside water opposite scarred flat ground.', 'Former shepherd motif alone misses current mining wealth and implies abandonment; replace ore sorting at mine.'), ('KEEP_CONTEXT_ONLY', 'Brick waterfront city, small vessels and carts beside channel and extensive pools on opposite side.', 'Regional commerce insert only. Pools not proven mines or salt works; no literal mountains of gold depicted. New 0963 carries extraction beat.'), ('KEEP_CANDIDATE', 'Balance scale with stacked silver-colored disks, bundles of tally sticks and partial hand.', 'Supports price/wealth motif, not measured price increase by still alone. Disks unusually uniform; currency design, balance mechanics and silver content unverified.'), ('REPLACE', 'Empty long market street with barred openings, jars, sticks and suspended timber frame.', 'No captive-price negotiation visible; replace populated coastal transaction with restrained adults.'), ('KEEP_CONTEXT_ONLY', 'Two partial figures at wooden table with sealed folded dark document or pouch between them.', 'Can be diplomatic refusal bridge, not readable treaty or verified historical event. Sleeved ornate wardrobe held.'), ('REPLACE', 'Long rows of upright spears bearing helmets in courtyard with empty chair.', 'Military inventory motif weakens explicit Bronze Harpy homage refusal; replace diplomatic emblem scene.'), ('KEEP_CONTEXT_ONLY', 'Vertical aerial of gray dense city blocks with tiny street figures and canal.', 'Broad rival-capital scale cut before dragon report, not proof city layout or named place. Keep brief; new 0970 carries creature beat.'), ('REPLACE', 'Aerial gray dense city blocks and tiny figures, same broad motif as preceding shot.', 'Does not establish sighting or tamed dragon; replace calm creature near silver-haired adult.')]
repl={963: ('Gold-colored nuggets and silver-white mineral pieces on timber sorting table beside baskets and pick; adults carry ore at mine entrance.', 'Gold/silver wealth legible as illustration, not certified mineralogy. Background carrying basket and hands mechanics need enlarged inspection; invented mine layout/overseer identity. Provisional selection.'), 966: ('Two adults negotiate over balance and silver-colored pieces while three cuffed adults sit behind under guard at coastal quay.', 'Replaces empty market with coercive trade. Buyer hair reads gray rather than distinctly silver-white; identity, costumes, balance/hands/cuff topology and period coins remain PARTIAL_ANATOMY_MECHANICS_HOLD. Cannot demonstrate actual price rise alone.'), 968: ('Two silver-haired standing delegates face gold-fringed envoy across table with winged female relief plaque and untouched bowl.', 'Refusal represented by staging, not proven action. Emblem lacks clearly readable canonical thunderbolt/harpy anatomy; costumes are tailored courtwear rather than certified tokar. PARTIAL_ICONOGRAPHY_WARDROBE_HOLD; invented diplomatic event.'), 970: ('Large crouched dark winged reptile rests near standing silver-haired adult on green volcanic terrain.', 'Calm proximity suggests taming, not proof of blood bond. Folded wings obscure full limb count/attachment; creature anatomy, feet and design match remain PARTIAL_CREATURE_HOLD. Anonymous figure not confirmed recurring rider.')}
ledger=json.loads((a/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==959
manifest=[]
for j,(status,obs,action) in enumerate(notes):
 n=961+j; p=Path(f'google_drive/VAL-EP001-IMG{n:04d}.png'); md=hashlib.md5(p.read_bytes()).hexdigest(); assert md==checks[j]
 with Image.open(p) as im: im.load(); dims=list(im.size)
 s=ledger['shots'][n-1];assert s['scene_id']==p.stem
 s.update(audit_status=status,drive_file_id=ids[j],selected_local_file=str(p),original_local_file=str(p),visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md,reviewed_on='2026-11-15',review_scope='Individually opened at tool display resolution, decoded and MD5 matched; no audio timing or all-pixel anatomy certification.')
 if n in repl:
  rp=assets/f'{p.stem}_v02.png'
  with Image.open(rp) as im:im.load();rd=list(im.size)
  s.update(audit_status=('REPLACED_PARTIAL_ANATOMY_MECHANICS_HOLD' if n==966 else 'REPLACED_PARTIAL_ICONOGRAPHY_WARDROBE_HOLD' if n==968 else 'REPLACED_PARTIAL_CREATURE_HOLD' if n==970 else 'REPLACED_PROVISIONAL'),selected_local_file=str(rp),replacement_file=str(rp),replacement_md5=hashlib.md5(rp.read_bytes()).hexdigest(),replacement_dimensions=rd,replacement_observation=repl[n][0],replacement_review=repl[n][1])
 manifest.append(dict(s,native_dimensions=dims,native_bytes=p.stat().st_size))
ledger['reviewed_individually']=969
(a/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (a/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(a/'BATCH_097_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
report="""# Batch097 — IMG0961–0970 (32:00–32:20)

Ten originals individually viewed, decoded and MD5 matched against Drive metadata. Four generated v02 versions individually viewed and selected provisionally. 969/1050 slots reviewed; zero final approvals.

## Full paragraph context (32:00–32:30)

Valyria, across the gulf, has risen from sheepherders into a republic extracting gold and silver, raising enslaved-captive prices in coastal markets and refusing Bronze Harpy homage. Tamed-dragon sightings alarm Ghiscari warlords, who see both intolerable danger and irresistible prize. Paragraph continues through IMG0975. Previous paragraph establishes Ghis wealth, tokars, galleys, chains and legions; next describes Ghiscari commanders planning to kill dragons using bolts, arrows or denial of riders. Script/map unchanged; no audio timing or timeline edits verified.

## Individual decisions

"""
for s in manifest:
 report+=f"### {s['scene_id']} — {s['audit_status']}\n\nObserved original: {s['visual_observation']}\n\n{s['editorial_action']}\n\n"
 if s.get('replacement_observation'):report+=f"Selected v02: {s['replacement_observation']}\n\nRemaining hold: {s['replacement_review']}\n\n"
report+="""## Remaining gates

0963 is provisional; 0966 anatomy/mechanics, 0968 iconography/wardrobe and 0970 creature anatomy remain explicit PARTIAL holds. New scenes improve missing story beats but do not certify historical transactions, mineral composition, formal diplomatic incident or actual taming behavior. 0961/0962 must not imply a literal narrow-channel view between Old Ghis and Valyria. No new fire, glowing eyes or sorcery. All market captives depicted as clothed adults without graphic injury. Prior unresolved 0885 mechanics, city direction, road, wardrobe and creature holds persist. Final acceptance requires recovered design-reference conformity, enlarged anatomy/props/rigging inspection, sequence continuity and timed narration gate.

Next Batch098 IMG0971–0980 finishes dragon danger/prize paragraph then enters Ghiscari war planning (32:30 onward). Read full paragraphs and inspect actual next images before continuity claims.
"""
(a/'BATCH_097_REVIEW.md').write_text(report)
z=Path('google_drive/EP001_BATCH_097_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as out:
 for s in manifest:
  out.write(s['original_local_file'])
  if s.get('replacement_file'):out.write(s['replacement_file'])
 for p in [a/'BATCH_097_REVIEW.md',a/'BATCH_097_MANIFEST.json',a/'EP001_SHOT_AUDIT_LEDGER.json',a/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:out.write(p)
print(z,z.stat().st_size,hashlib.md5(z.read_bytes()).hexdigest())
assert not any(s['final_accepted'] for s in ledger['shots'])
