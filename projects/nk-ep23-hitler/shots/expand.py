#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
NOPE = "no signboards, no lettering of any kind, no flags, no emblems"
FRAME = "full-bleed 16:9 image filling the whole frame edge to edge with no black bars"
TAIL = "Painted-realism concept art, photographic realism like a still from a period film, not a cartoon and no drawn outlines, " + FRAME + ", desaturated palette of cold grey-blue, sepia and a little amber lamp light, deep shadows, 35mm film grain. No readable writing anywhere. No text, no captions, no watermark."
PEOPLE = ", people only from behind, far away or as dark silhouettes, no face clearly visible"
LOOK = {
 "L": ("Upper Austria, 1889 to 1907", "A small town in Upper Austria around 1900: plastered houses with steep roofs, cobbled lanes, oil lamps and candles, horse carts, clothes of the period, " + NOPE, PEOPLE),
 "V": ("Vienna, 1907 to 1913", "Vienna around 1910 in winter: grand stone buildings, gas street lamps, trams and horse cabs, snow and coal smoke, men in worn overcoats and hats, " + NOPE, PEOPLE),
 "X": ("what came later (1933 to 1945)", "Germany between 1933 and 1945, shown from far and in shadow, nothing celebrated: " + NOPE + ", no symbols on any cloth or wall, no insignia", PEOPLE),
 "S": ("one object", "A still life around 1900: one object in a dim plain room, a single shaft of soft window light, deep shadows, no people, no lettering of any kind", ""),
 "O": ("setting given in the subject", "", ""),
}
# Fixed descriptions (refs). No face of a real person is shown anywhere in the film: see shots/CAST.md.
REF = {
 "A": "The young man is thin, about twenty, with dark unkempt hair grown over his collar, in a worn dark overcoat too long for him; he is shown only from behind, from far away or as a dark silhouette, never the face.",
 "B": "The boy is slight, with dark hair cut short at the sides, in a plain jacket, knee breeches and boots of around 1900; he is shown only from behind or as a small figure far away, never the face.",
 "Y": "The youth is thin, about seventeen, with dark hair, in a neat dark coat and hat with a slim walking cane, shown only from behind or far away, never the face.",
 "K": "The mother is a quiet woman in her forties in a plain dark high-collared dress, her hair pinned up, shown only from behind, in shadow or as hands, never the face.",
 "F": "The father is a heavy-set man in his sixties in a dark civil-service coat, shown only from behind or as a dark shape, never the face.",
}
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
    if refs: r_["refs"] = refs
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
