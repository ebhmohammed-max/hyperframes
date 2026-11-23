#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
TEMPLE = "The Big Temple at Thanjavur in South India: a pyramid-shaped tower of grey-brown granite rising in thirteen receding carved tiers above the sanctum, crowned by a ribbed stone dome with a small gilded finial"
LOOK = {
 "T": ("the temple today", TEMPLE + ". The present day, natural light, a stone-paved courtyard, no signboards, no lettering of any kind, no flags", ", any visitors are ordinary Tamil people in everyday clothes, small in the frame or seen from behind"),
 "C": ("1010 CE, a sober reconstruction", "Thanjavur in the year 1010, in the time of the Chola kings, painted as a sober historical reconstruction: red earth, grey-brown granite, bamboo and timber scaffolding, coir ropes, log rollers, wooden levers, elephants; only hand tools, nothing modern, no lettering of any kind, no flags. Where the temple appears it is " + TEMPLE[0].lower() + TEMPLE[1:], ", the men bare-chested in short white cotton waist cloths, the women in plain draped cotton saris"),
 "L": ("the legend, as it is told", "The legend as it is told, painted like a remembered story: warm golden dust haze, soft dreamlike light, slightly grander than life. South India a thousand years ago, red earth, elephants, coir ropes and log rollers, nothing modern, no lettering of any kind, no flags. Where the temple appears it is " + TEMPLE[0].lower() + TEMPLE[1:], ", the men bare-chested in short white cotton waist cloths, the women in plain draped cotton saris"),
 "H": ("Tamil Nadu today, away from the temple", "The countryside and small towns of the Kaveri delta in Tamil Nadu in the present day, natural light, no signboards, no lettering of any kind, no flags", ", ordinary Tamil people in everyday clothes: saris, shirts, veshtis and lungis"),
 "D": ("symbolic still life", "A still life on old dark wood or stone, a single shaft of warm light, deep shadows, no people, no lettering of any kind", ""),
 "O": ("setting given in the subject", "", ""),
}
REF = {}
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
          "file": f"EP20_{n:03d}_{clip}q{q:02d}_{name}.jpg",
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
md = [f"# EP20 80 டன் கல்லு 200 அடி உயரத்துக்கு எப்படி போச்சு? (How did an 80-ton stone get 200 feet up?): shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: every picture is an illustration, none is a photograph or a record, and none shows the real temple exactly. Three looks keep the claims apart: **L** the legend as it is told (golden and dreamlike: the long ramp, the single stone), "
      "**C** a sober reconstruction of 1010 (what scholars suggest; it is not a record, nobody recorded the building work), **T** the temple today. "
      "The king is seen only from behind; every worker, scholar and visitor is invented and no real or living person is shown. No close view of any deity. "
      "Inscriptions appear only as worn, illegible chisel marks: no readable writing, no logos, no flags. Every number, name and source is set in the edit (film/fx.mjs).\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
