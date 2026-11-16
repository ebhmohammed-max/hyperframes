"""Persist Batch096 individually inspected originals and provisional corrections."""
import csv, hashlib, json, zipfile
from pathlib import Path
from PIL import Image
root=Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria')
a=root/'audit'; assets=Path('assets/episode_audit/batch096')
ids=['1JhMdpxGDn9FAbbwMa6F5AIOKwC21WcOA', '1VQWw09hjHXsjcgqwSmv15wKnbsPJx5HZ', '1pysSwHA3p-7Ak7XIkGPgu8N7xZCkFpMk', '1TrA_863ekFDfGWF5uEE8rKKiVqEjYWM1', '1R9WFOtP5_lu6uSaBgOe19hw7kZu-iRXK', '1KsXDgxppV7CDDru-eLUYKeGPG9hqfN34', '1Z-4H6mgCABkCMpZzrBe81a2WXo53YbFA', '1SRM3P5F4BhqJfjv660bcaTfHYoKWZ28P', '1GH6fNlsaIOiwuCKp2E6e50kFlaZv8Axj', '1sJm-dfGqkqddDoDZaSrFcrmxGl8E8iGa']
checks=['27d8183964a81e763c2bed1d547c1277', '1c9a4cc072b0afe56fad2e7c82d2a9fa', 'ebe0954681c3aeb8c5b04675abfbae55', 'f1be3e39352c5bdcd2696d779caf8354', '58cb5991b8480d5cbb63c0318cb3f8cd', '692b2679e79b80e3e3a2bd16fb9158ed', '47f49edb266de3ea432896e69528a4ed', 'e3cbc26adf11bcedabb416ce33db97aa', '1a16603c3f7632b0a8897138e6dec1a6', 'bd3c91148dd9a2ed1f053cde831a45a8']
notes=[('KEEP_CONTEXT_ONLY', 'Two adults in patterned gold-edged drapery overlook harbor from shaded brick terrace.', 'Supports terrace wealth; wardrobe reads coat-like in places, not certified canonical tokar. Anonymous elites only; grade/set match held.'), ('REPLACE', 'Adult in tailored black robe with sleeve cuff leans on terrace beside stepped brick pyramid.', 'Tailored coat reads poorly for gold-fringed wrapped tokar; replace with visibly wrapped fringed cloth.'), ('KEEP_CANDIDATE', 'Three adults seen from behind in rich gold-fringed drapery overlook low oared hulls.', 'Good cloth/fringe and patrician survey beat. Exact unsewn tokar wrapping, hands and harbor identity unverified.'), ('REPLACE', 'Multiple high-sided wooden ships seen stern-on below gantry-like dock structures.', 'Does not show bronze bow rams. Replace with clearer low galley bow and bronze ram.'), ('REPLACE', 'Top view of tightly repeated empty oared hulls and boxlike transports at piers.', 'Fleet scale fits but transport purpose unproven and repetition diagrammatic; replace identifiable guarded captive transport.'), ('KEEP_CANDIDATE', 'Large intact baked-brick arched gateway and empty paved ramp.', 'Supports Ghiscari brick/civic order in full paragraph, not specific legal institution. Empty gateway insert acceptable within populated surrounding sequence.'), ('KEEP_CONTEXT_ONLY', 'Two bronze-colored weights, dark circular disk, pointed stylus-like tool and folded cloth.', 'Can imply regulated commerce/law; object identities and legal purpose not proven. Do not claim official Ghiscari standards or readable law code.'), ('KEEP_CANDIDATE', 'Heavy dark chain over brick beside small round metal lock-like object.', 'Direct brick/chains material motif; metallurgy, lock operation and chain topology not certified at full pixels.'), ('KEEP_CANDIDATE', 'Three differently sized metal spearheads beside broad curved bronze-colored object.', 'Useful spear-wall lead-in; triple spear lengths suggest editorial motif, not proof exact legion equipment. Curved object not conclusively shield.'), ('KEEP_CANDIDATE', 'Compact distant ranks with upright spears and red/dark shields beyond brick arch on broad paved way.', 'Supports disciplined legion formation. Still cannot verify synchronized lockstep, exact count or full anatomy; equipment and scale held.')]
repl={952: ('Anonymous patrician in burgundy wrapped cloth with large gold fringes, one bare arm and held drapery, stepped brick monument and low vessels behind.', 'Coat/cuffs removed. Still partly toga-like with light underlayer; exact Ghiscari tokar wrap and continuity with 0951/0953 remain PARTIAL_WARDROBE_HOLD.'), 954: ('Low oared wooden galley with solid bronze wedge-like waterline ram and brick harbor behind.', 'v02 rejected for hollow cannon-like tube and invented winged hull emblem. Edited v03 removes emblem and shows closed solid beak. Ram mounting/size, oar topology, crew anatomy and naval design remain PARTIAL_NAVAL_MECHANICS_HOLD; not certified engineering.'), 955: ('Clothed adult captives seated on broad wooden transport under two helmeted guards, visible wrist restraints, sacks and amphorae.', 'Makes coercive transport readable. More adults than prompt, some faces repeated; cuffs/hands, gangplank support, rigging and hull mechanics remain PARTIAL_ANATOMY_MECHANICS_HOLD. Anonymous invented illustration, not named voyage.')}
ledger=json.loads((a/'EP001_SHOT_AUDIT_LEDGER.json').read_text());assert ledger['reviewed_individually']==949
manifest=[]
for j,(status,obs,action) in enumerate(notes):
 n=951+j; p=Path(f'google_drive/VAL-EP001-IMG{n:04d}.png'); md=hashlib.md5(p.read_bytes()).hexdigest(); assert md==checks[j]
 with Image.open(p) as im: im.load(); dims=list(im.size)
 s=ledger['shots'][n-1];assert s['scene_id']==p.stem
 s.update(audit_status=status,drive_file_id=ids[j],selected_local_file=str(p),original_local_file=str(p),visual_observation=obs,editorial_action=action,final_accepted=False,native_checksum_verified=True,native_md5=md,reviewed_on='2026-11-15',review_scope='Individually opened at tool display resolution, decoded and MD5 matched; no audio timing or all-pixel anatomy certification.')
 if n in repl:
  rp=assets/f"{p.stem}_{'v03' if n==954 else 'v02'}.png"
  with Image.open(rp) as im:im.load();rd=list(im.size)
  s.update(audit_status=('REPLACED_PARTIAL_WARDROBE_HOLD' if n==952 else 'REPLACED_PARTIAL_NAVAL_MECHANICS_HOLD' if n==954 else 'REPLACED_PARTIAL_ANATOMY_MECHANICS_HOLD'),selected_local_file=str(rp),replacement_file=str(rp),replacement_md5=hashlib.md5(rp.read_bytes()).hexdigest(),replacement_dimensions=rd,replacement_observation=repl[n][0],replacement_review=repl[n][1])
 manifest.append(dict(s,native_dimensions=dims,native_bytes=p.stat().st_size))
ledger['reviewed_individually']=959
(a/'EP001_SHOT_AUDIT_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n')
keys=list(dict.fromkeys(k for s in ledger['shots'] for k in s))
with (a/'EP001_SHOT_AUDIT_LEDGER.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(ledger['shots'])
(a/'BATCH_096_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
report="""# Batch096 — IMG0951–0960 (31:40–32:00)

Ten originals individually viewed, decoded and matched to Drive MD5. Four generated versions individually viewed, three selected. 959/1050 slots reviewed; zero final approvals.

## Full paragraph context (31:30–32:00)

Old Ghis and heirs of Grazdan have ruled central Essos for centuries. Patricians in gold-fringed tokars survey harbors from shaded stepped-brick pyramid terraces: bronze-rammed war-galleys and slave transports. Law, brick, chains and disciplined spear-wall legions define imperial self-image. Prior paragraph covers sailors reporting Valyrian wonders and Ghiscari displeasure; next describes Valyrian metal wealth, captive prices, refused homage and tamed dragons as danger/prize. Script and shot map unchanged; no timed timeline edits or audio verification.

## Individual decisions

"""
for s in manifest:
 report+=f"### {s['scene_id']} — {s['audit_status']}\n\nObserved original: {s['visual_observation']}\n\n{s['editorial_action']}\n\n"
 if s.get('replacement_observation'):report+=f"Selected v02: {s['replacement_observation']}\n\nRemaining hold: {s['replacement_review']}\n\n"
report+="""## Remaining gates

All three selected corrections retain explicit PARTIAL holds: 0952 wardrobe; 0954 naval mechanics; 0955 anatomy/mechanics. 0954_v02 is rejected evidence, not selection: hollow cannon-like bow shape and invented winged emblem. v03 replaces these with solid bronze beak/plain hull, but ram engineering remains unverified. Original 0951 wardrobe is context-only, not certified tokar; 0953 is stronger drapery candidate. Ship purposes, legal objects, identities and exact imperial layout should not be overclaimed. No flames or magic added. All captive figures clothed adults, no graphic violence. Prior unresolved city, creature, road and basket-mechanics holds remain. Final delivery requires design-reference match, enlarged faces/hands/rigging/equipment inspection, sequence grade and timed narration gate.

Next Batch097 IMG0961–0970 starts 32:00–32:30: Valyrian wealth, enslaved-captive prices, refused homage and dragon threat. Read full paragraph before decisions.
"""
(a/'BATCH_096_REVIEW.md').write_text(report)
z=Path('google_drive/EP001_BATCH_096_AUDIT_WITH_CORRECTIONS.zip')
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as out:
 for s in manifest:
  out.write(s['original_local_file'])
  if s.get('replacement_file'):out.write(s['replacement_file'])
 for rp in assets.glob('*v02.png'):
  if str(rp) not in [s.get('replacement_file') for s in manifest]:out.write(rp)
 for p in [a/'BATCH_096_REVIEW.md',a/'BATCH_096_MANIFEST.json',a/'EP001_SHOT_AUDIT_LEDGER.json',a/'EP001_SHOT_AUDIT_LEDGER.csv',Path(__file__)]:out.write(p)
print(z,z.stat().st_size,hashlib.md5(z.read_bytes()).hexdigest())
assert not any(s['final_accepted'] for s in ledger['shots'])
