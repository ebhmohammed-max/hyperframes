#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
NOPE = "no signboards, no lettering of any kind, no flags, no emblems"
FRAME = "full-bleed 16:9 image filling the whole frame edge to edge with no black bars"
TAIL = "Painted-realism concept art, photographic realism like a film still, not a cartoon and no drawn outlines, " + FRAME + ", muted teal and amber palette, deep shadows, 35mm film grain. No readable writing anywhere. No text, no captions, no watermark."
TAIL_C = "Realistic astronomical illustration with photographic realism, like a long-exposure space photograph, not a cartoon and no drawn outlines, " + FRAME + ", deep navy, black and warm gold palette, fine film grain. No readable writing anywhere. No text, no labels, no captions, no watermark."
TAIL_B = "Detailed scientific illustration with photographic realism, like a hand-coloured electron-microscope image, not a cartoon and no drawn outlines, " + FRAME + ", teal and amber palette on a dark ground, soft depth of field. No readable writing anywhere. No text, no labels, no arrows, no captions, no watermark."
LOOK = {
 "H": ("you, tonight", "Tamil Nadu in the present day, at night: warm lamp light against a deep blue night sky, plain everyday surroundings, " + NOPE, ""),
 "B": ("inside the body", "The inside of the human body at microscopic scale: translucent glowing forms floating in dark fluid, no people, no instruments", "", TAIL_B),
 "T": ("deep time", "Prehistoric Earth, painted like a natural-history museum reconstruction: no humans, no buildings, nothing modern", ""),
 "E": ("Earth today", "Planet Earth in the present day, like a frame from a nature documentary, " + NOPE, ""),
 "C": ("space", "Outer space: a deep black sky with sharp stars, true-to-science colours, no lettering of any kind, no logos, no flags", "", TAIL_C),
 "S": ("one object", "A still life: one object in a dim plain setting, a single shaft of soft light, deep shadows, no people, no lettering of any kind", ""),
 "O": ("setting given in the subject", "", ""),
}
# Fixed descriptions (refs). No face of a real person is shown anywhere in the film.
REF = {
 "V": "The viewer is a young Tamil adult with short black hair in a plain light cotton shirt, shown only from behind or as a dark silhouette, never the face.",
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
          "file": f"EP22_{n:03d}_{clip}q{q:02d}_{name}.jpg",
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
md = [f"# EP22 27 உண்மைகள் (27 facts that make you question your existence): shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: every picture is an illustration, none is a photograph, a telescope image or a record. The pictures show what a fact is about; they are not evidence for it. "
      "**No face of a real person is shown.** The recurring viewer (a young person on a house terrace at night) appears only from behind or as a silhouette. "
      "No readable writing, logos, flags or emblems; every number, name and source is set in the edit (film/fx.mjs).\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
