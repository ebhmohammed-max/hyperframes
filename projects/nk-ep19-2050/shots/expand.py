#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
PEO = "ordinary Tamil people in everyday clothes: saris, salwar suits, shirts and trousers, veshtis and lungis"
NOW = "Tamil Nadu, South India, in the present day: ordinary real life in natural light, real streets, homes and public places, no signboards, no name boards, no lettering of any kind, no brand names, no flags"
LOOK = {
 "N": ("today, Tamil Nadu and India", NOW, ", " + PEO),
 "F": ("the year 2050, a believable near future", "A South Indian coastal city in the year 2050, shown as a believable near future and not as science fiction: the same kind of streets, flats and houses as today, only denser and taller, with solar panels on the roofs, electric buses and scooters, shade trees and an elevated metro line; no flying vehicles, no holograms, no walking robots, no neon, no chrome, no glass domes; no signboards and no lettering of any kind", ", " + PEO),
 "W": ("the world", "A documentary view of the world in the present day, natural light, no signboards, no lettering of any kind, no flags, no logos", ", any people small in the frame or seen from behind"),
 "C": ("the Tamil Nadu coast", "The coast of Tamil Nadu on the Bay of Bengal: grey-green sea, small fibreglass fishing boats, coconut and palmyra palms, low concrete and tiled houses, a heavy monsoon sky, no signboards and no lettering of any kind", ", fishing families in lungis and saris, seen from behind or far away"),
 "D": ("symbolic still life", "A still life on old dark wood or stone, a single shaft of warm light, deep shadows, no people, no lettering of any kind", ""),
 "P": ("the year 1990, like an old colour print", "Tamil Nadu, South India, in the year 1990, shown like a faded colour photograph of that time: washed-out colours, soft focus, a slight yellow cast, nothing modern, no lettering of any kind", ", people in the clothes of 1990"),
 "S": ("a film cliche, painted as a fantasy", "A science-fiction film cliche painted like a glossy old film poster and clearly a fantasy: saturated magenta and cyan, chrome, lens flares, theatrical light, no lettering of any kind", "",
       "Glossy airbrushed film-poster illustration, full-bleed 16:9 image filling the whole frame edge to edge with no black bars. No readable writing anywhere. No text, no captions, no watermark."),
 "O": ("setting given in the subject", "", ""),
}
REF = {
 "nila": "The young woman is the same as in the reference picture: Nila, a Tamil woman of 24 with warm brown skin, a long black plait down her back, a mustard-yellow cotton kurta over dark blue trousers and a small grey cloth shoulder bag.",
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
          "file": f"EP19_{n:03d}_{clip}q{q:02d}_{name}.jpg",
          "prompt": f"{subj[0].upper()+subj[1:]}. " + "".join(REF[k] + " " for k in refs) + (setting + ". " if setting else "") + (LOOK[look][3] if len(LOOK[look]) > 3 else TAIL)}
    if refs: r_["refs"] = refs
    rows.append(r_)
bad = 0
for clip, cs in counts.items():
    for q, c in enumerate(cs):
        if per[(clip, q)] != c: bad += 1; print("count", clip, q, "want", c, "have", per[(clip, q)])
for k, v in names.items():
    if v > 1: print("duplicate name", k)
json.dump(rows, open("shots/prompts.json", "w"), indent=1, ensure_ascii=False)
md = [f"# EP19 2050-ல் உலகம் எப்படி இருக்கும்? (What will the world be like in 2050?): shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: every picture is an illustration, none is a photograph or a record. Pictures of 2050 (look F) show a believable near future, not science fiction; they illustrate a projection and are not a prediction of how any real place will look. "
      "Nila, her grandmother and every other person are invented; no real, living or identifiable person is shown. The three film cliches of the hook (flying car, robot servant, house on Mars) have their own poster look (S) so that they read as fantasy. "
      "The 2019 Chennai water shortage and the floods are illustrated, not shown from news footage. No readable writing, no logos, no flags, no emblems: every number, name and source is set in the edit (film/fx.mjs). "
      "Lines that carry a full-screen graphic (the hundred dots) have no picture.\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
