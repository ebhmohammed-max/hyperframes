#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
NOPE = "no signboards, no lettering of any kind, no flags, no emblems"
FRAME = "full-bleed 16:9 image filling the whole frame edge to edge with no black bars"
TAIL = "Cinematic film still from a period drama feature film, photographed on 35mm anamorphic lenses with shallow depth of field and natural motivated light, real human actors with expressive faces and real skin, photographic realism, not a painting, not a cartoon, " + FRAME + ", composed for a 2.2:1 widescreen crop so heads and key action stay clear of the top and bottom edges, desaturated palette of cold grey-blue, sepia and a little amber lamp light, deep shadows, fine film grain. No readable writing anywhere. No text, no captions, no watermark."
# EP23, from the second review on: faces are shown (the user asked for his real face and for a film feel). Crowds of the later years stay far and dark.
PEOPLE = ""
FAR = ", crowds seen from far or in shadow, nothing celebrated"
LOOK = {
 "L": ("Upper Austria, 1889 to 1907", "A small town in Upper Austria around 1900: plastered houses with steep roofs, cobbled lanes, oil lamps and candles, horse carts, clothes of the period, " + NOPE, PEOPLE),
 "V": ("Vienna, 1907 to 1913", "Vienna around 1910 in winter: grand stone buildings, gas street lamps, trams and horse cabs, snow and coal smoke, men in worn overcoats and hats, " + NOPE, PEOPLE),
 "X": ("what came later (1933 to 1945)", "Germany between 1933 and 1945, an ominous mood, nothing celebrated: " + NOPE + ", no symbols on any cloth or wall, no insignia, no armbands, no salutes", FAR),
 "S": ("one object", "A still life around 1900: one object in a dim plain room, a single shaft of soft window light, deep shadows, no people, no lettering of any kind", ""),
 "O": ("setting given in the subject", "", ""),
}
# Fixed descriptions (refs) and the reference picture passed with each (out/cast/<file>). Hitler is shown with his real face at every age:
# B and H use period photographs as likeness references; Y and A (no photograph of him exists between 1901 and 1914) use cast portraits
# made from those two. The parents are played by invented actors of the right type. See shots/CAST.md.
REF = {
 "A": "The young man is the same person as in the reference portrait: Adolf Hitler at twenty, in Vienna in 1909: thin and pale with hollow cheeks, a long narrow face, pale blue staring eyes, dark brown hair grown long over his collar with a lock falling across the forehead, an unshaven fluffy dark beard on the chin and a thin moustache, in a worn dark overcoat too long for him.",
 "B": "The boy is the same person as in the reference photograph: Adolf Hitler at about eleven: slight, with dark brown hair cut short with a fringe brushed to one side, ears that stand out a little, a serious closed face, in a plain dark jacket with a white collar, knee breeches and boots of around 1900.",
 "Y": "The youth is the same person as in the reference portrait: Adolf Hitler at seventeen, in Linz in 1906: thin and pale, a long narrow face, pale blue eyes, dark brown hair parted at the side, the first thin moustache, neatly dressed in a dark coat and a black broad-brimmed hat, with a slim black walking cane.",
 "H": "The man is the same person as in the reference photograph: Adolf Hitler in his forties: dark brown hair with a side parting and a lock falling over the forehead, a small clipped dark moustache, pale blue hard eyes, a pale heavy face. He is never lit like a hero: the light is cold or from below and the mood is a warning.",
 "K": "The mother is the same woman as in the reference portrait: a quiet woman in her forties with large sad grey-blue eyes, brown hair parted in the middle and pinned back, in a plain dark high-collared dress.",
 "F": "The father is the same man as in the reference portrait: a heavy-set stern man in his sixties, bald on top, with a big grey moustache and side-whiskers, in a dark civil-service uniform coat with plain brass buttons.",
}
REFIMG = {"A": "A.jpg", "B": "B_photo.jpg", "Y": "Y.jpg", "H": "H_photo.jpg", "K": "K.jpg", "F": "F.jpg"}
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
          "file": f"EP23_{n:03d}_{clip}q{q:02d}_{name}.jpg",
          "prompt": f"{subj[0].upper()+subj[1:]}. " + "".join(REF[k] + " " for k in refs) + (setting + ". " if setting else "") + (LOOK[look][3] if len(LOOK[look]) > 3 else TAIL)}
    if refs: r_["refs"] = refs; r_["images"] = ["google_drive/ep23_pics/cast/" + REFIMG[k] for k in refs]
    rows.append(r_)
bad = 0
for clip, cs in counts.items():
    for q, c in enumerate(cs):
        if per[(clip, q)] != c: bad += 1; print("count", clip, q, "want", c, "have", per[(clip, q)])
for k, v in names.items():
    if v > 1: print("duplicate name", k)
json.dump(rows, open("shots/prompts.json", "w"), indent=1, ensure_ascii=False)
md = [f"# EP23 ஹிட்லர்: வீடில்லாதவனில் இருந்து ராட்சசன் வரை (Hitler: From Homeless to Monster): shot list\n\n{len(rows)} images so far (the list grows chapter by chapter). File names carry the running number, narration clip and line.\n",
      "Rules: every picture is an illustration made for this film; none is a photograph or a record. **No face of a real person is shown**: he and the people around him appear only from behind, far away, in silhouette or as hands. "
      "No flags, emblems, symbols, insignia or readable writing in any picture; every number, name, date and source is set in the edit (film/fx.mjs). Nothing in the pictures celebrates him. Full rules: shots/CAST.md.\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
