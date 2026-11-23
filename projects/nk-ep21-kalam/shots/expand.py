#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
NOPE = "no signboards, no lettering of any kind, no flags, no emblems"
LOOK = {
 "D": ("the last day, 27 July 2015", "North-east India in July 2015, the monsoon: low grey cloud, wet roads, pine-covered hills, soft overcast light, cars and clothes of the present day, " + NOPE, ""),
 "P": ("the last day, on the flight", "A passenger aircraft over India in July 2015, the monsoon: thick grey cloud outside the windows, soft cabin light, a present-day cabin with plain seats, no hills and no landscape in view, no lettering of any kind, no logos, no flags, no emblems", ""),
 "R": ("Rameswaram around 1940, as he remembered it", "Rameswaram island in South India around 1940, painted as a remembered childhood: warm sepia sunlight, sand lanes, palm trees, lime-washed houses with tiled roofs, the sea always near, steam trains, nothing modern, " + NOPE, ", the people in white cotton veshtis and plain saris, small in the frame or seen from behind"),
 "Y": ("1958 to 1980, the working years", "India between 1958 and 1980, in the faded colours of an old colour photograph: period clothes, period machines with dials and switches, nothing later than 1980, " + NOPE, ""),
 "S": ("symbolic still life", "A still life in a plain room, a single shaft of soft window light, deep shadows, no people, no lettering of any kind", ""),
 "O": ("setting given in the subject", "", ""),
}
# Fixed descriptions (refs). No face of a real person is shown anywhere in the film.
REF = {
 "K": "The elderly man is 83 and is shown only from behind, in silhouette or from far, never his face: silver-white hair worn long to the collar and parted in the middle, a slight stoop, a dark grey closed-collar suit.",
 "A": "His aide is a slim Indian man of about thirty in a plain light shirt, shown from behind or in part, never his face.",
 "G": "The guard is a lean young Indian soldier in black fatigues with a black cloth wrapped over his head and face so that only the eyes show, a rifle in his hand.",
 "B": "The boy is a thin Tamil boy of about ten with cropped black hair, a loose white shirt and dark shorts, barefoot, shown from behind or from far, never his face.",
 "Y": "The young man is a slim Tamil man of about twenty-six with thick wavy black hair, a white shirt and dark trousers, shown from behind or from far, never his face.",
 "M": "The project director is a slim Indian man in his late forties with thick wavy black hair that touches his collar, a plain light shirt with the sleeves rolled, shown from behind or from far, never his face.",
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
          "file": f"EP21_{n:03d}_{clip}q{q:02d}_{name}.jpg",
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
md = [f"# EP21 அப்துல் கலாமின் கடைசி நாள் (Abdul Kalam's last day, 27 July 2015): shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: every picture is an illustration, none is a photograph or a record. **No face of a real person is shown.** Dr Kalam appears only from behind, in silhouette, from far, or as hands "
      "(silver hair to the collar, dark closed-collar suit); the same holds for him as a boy, as a young man and as project director, and for his aide, Satish Dhawan and Swami Sivananda. "
      "The guard's face is covered, as the aide's account describes him. The collapse, the hospital room and the burial are not shown: an empty podium, a corridor and a crowd seen from far stand for them. "
      "Three looks keep the times apart: **D** the last day (monsoon, cool), **R** Rameswaram around 1940 (sepia), **Y** 1958 to 1980 (faded colour). "
      "No readable writing, logos, flags or emblems; every number, name and source is set in the edit (film/fx.mjs).\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
