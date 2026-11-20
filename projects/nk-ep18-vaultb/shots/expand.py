#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
KER = "Thiruvananthapuram in Kerala, South India: old houses with steep clay-tiled roofs and pillared verandas, white lime-washed walls, coconut palms, jackfruit and mango trees, humid tropical light"
MEN = "South Indian men of Kerala in white mundus (a white cloth wrapped at the waist and reaching the ankles), in white shirts or bare-chested with a white cloth over one shoulder, short hair, moustaches, no beards unless named, no turbans and no head cloths"
LOOK = {
 "T": ("the temple town, 2011 to today", KER + ", the present day, ordinary street life, no signboards, no name boards and no lettering of any kind, no brand names", ", " + MEN + ", women in saris; all people seen from behind or far away"),
 "V": ("under the temple: corridor and vault", "Under an old South Indian temple in Kerala in 2011: a low corridor and small chambers built of large rough-dressed granite blocks, walls black with age, no windows, light only from hand torches and a hurricane lamp, dust hanging in the beams, deep shadows, nothing carved and nothing written on the walls", ", " + MEN + ", elderly, seen only from behind or as dark silhouettes, faces never visible"),
 "G": ("the treasure", "Antique gold in darkness on rough granite under an old South Indian temple, lit by a single torch beam: old unpolished gold with a soft worn glow, dust on everything, deep black shadows, not shiny new jewellery, no display cases", ""),
 "D": ("inside the temple", "Inside an old temple in Kerala, South India: dark granite walls and pillars, rows of small oil lamps in brass holders, tall brass standing lamps, incense smoke, a deep warm glow and heavy shadows; the image of the god is never shown clearly, at most an indistinct dark shape behind lamp flames; a quiet, reverent mood", ", worshippers seen from behind: men bare-chested in white mundus with a white cloth over one shoulder, women in cream Kerala saris with a gold border and hair in a bun"),
 "K": ("Travancore, 18th century", "Travancore in Kerala, South India, in the 18th century: temple and palace buildings of granite, carved dark wood and steep clay-tiled roofs, brass oil lamps, coconut palms, nothing modern", ", men of old Kerala bare-chested in white mundus with a white shoulder cloth and their hair tied in a knot above the forehead, no turbans, no beards, no crowns"),
 "S": ("the pepper trade, ancient times", "The Malabar coast of Kerala, South India, about two thousand years ago: a river-mouth port under coconut palms, wooden boats, heaps of spice, bright sea light, nothing modern", ", dark-skinned South Indian traders in white waist cloths, bare-chested, and a few foreign merchants in plain tunics, all small in the scene"),
 "C": ("courts and offices", "India between 2011 and 2025: a sober court or government office setting, wooden furniture, files tied with cloth tape, ceiling fans, plain daylight, no readable writing, no emblems, no flags, no logos, no judge's hammer", ", any people seen from behind or as hands only"),
 "L": ("a legend, painted as a legend", "A legend as people tell it, painted like a dream and clearly imagined: a dark stone vault in deep blue-green night tones with a cold unearthly glow, drifting mist, soft edges", ""),
 "X": ("still life", "A still life on old dark wood or stone in South India, a single shaft of warm light, deep shadows, no people", ""),
 "O": ("setting given in the subject", "", ""),
}
REF = {
 "temple": "The temple tower is the same as in the reference picture: a broad seven-tiered South Indian gateway tower of pale cream-grey stone that narrows toward the top, covered in rows of small carved niches, with a line of seven small golden finials along its top ridge, standing behind a large rectangular tank with granite steps, low tiled-roof buildings and coconut palms on both sides.",
 "irondoor": "The door is the same as in the reference picture: one tall leaf of dark iron plates held by rows of round rivets, set in a frame of rough granite blocks, three thick sliding bolts down its right side, rust and dust, completely plain with no carving, no figures, no symbols and no writing.",
 "petitioner": "The old man is the same as in the reference picture and is seen only from behind: about seventy, thin and a little stooped, white hair reaching his collar and the edge of a long white beard just visible past his shoulder, bare-chested with a white cloth over his left shoulder, a white mundu to the ankles, a cloth bag on one shoulder.",
}
TAIL = "Painted-realism concept art, photographic realism like a film still, not a cartoon and no drawn outlines, full-bleed 16:9 image filling the whole frame edge to edge with no black bars, muted teal and amber palette, deep shadows, 35mm film grain. No readable writing anywhere. No text, no captions, no watermark."
lines = json.load(open("script/lines.json", encoding="utf8"))
cap = {(l["clip"], l["q"]): l["cap"] for l in lines}
counts = json.load(open("shots/counts.json"))
rows, per, names = [], collections.Counter(), collections.Counter()
for raw in open("shots/shots.txt", encoding="utf8"):
    raw = raw.strip()
    if not raw or raw.startswith("#"): continue
    clip, q, name, look, subj = raw.split("|", 4)
    look, _, refs = look.partition("@")
    q = int(q); per[(clip, q)] += 1; names[name] += 1
    n = len(rows) + 1
    setting = LOOK[look][1] + ("" if "no people" in subj else LOOK[look][2])
    refs = refs.split(",") if refs else []
    for k in refs: assert k in REF, (n, k)
    r_ = {"n": n, "clip": clip, "q": q, "k": per[(clip, q)] - 1, "name": name, "look": look,
          "file": f"EP18_{n:03d}_{clip}q{q:02d}_{name}.jpg",
          "prompt": f"{subj[0].upper()+subj[1:]}. " + "".join(REF[k] + " " for k in refs) + (setting + ". " if setting else "") + TAIL}
    if refs: r_["refs"] = refs
    rows.append(r_)
bad = 0
for clip, cs in counts.items():
    for q, c in enumerate(cs):
        if per[(clip, q)] != c: bad += 1; print("count", clip, q, "want", c, "have", per[(clip, q)])
for k, v in names.items():
    if v > 1: print("duplicate name", k)
json.dump(rows, open("shots/prompts.json", "w"), indent=1, ensure_ascii=False)
md = [f"# EP18 Padmanabhaswamy temple, Vault B: shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: no photograph of the vaults or of the treasure has been published, so every picture is an illustration of what the published accounts describe, not a record. "
      "The image of the god is never shown clearly: at most an indistinct dark shape behind lamps, and the small golden figure from the vault is shown wrapped in cloth. "
      "Real people (the petitioner T. P. Sundararajan, the observers, the auditor, judges, lawyers, priests, the royal family) are seen only from behind, as hands, or not at all; nobody's face is shown. The petitioner's death is shown only through an empty chair and a lamp at a doorstep. "
      "Legends (the serpent, the spell, the sea behind the door, the sage and the eagle) are painted in their own dream-like look so that they cannot be taken for record. The iron door is always plain, as the 2011 observers described it. "
      "No readable writing: reports, registers and newspapers are blurred lines; the map, the vault plan and the report page are built in the edit. "
      "Lines that carry a full-screen graphic have no picture.\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
