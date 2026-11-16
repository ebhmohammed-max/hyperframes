#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json."""
import json, re, collections
LOOK = {
 "P": ("daylight", "Daylight, tenth-century Chola South India, bare-chested men in white dhotis with topknots"),
 "D": ("dusk", "Dusk, tenth-century Chola South India, bare-chested men in white dhotis with topknots"),
 "L": ("lamp-lit interior", "Night interior lit by brass oil lamps, tenth-century Chola South India, bare-chested men in dhotis with topknots"),
 "W": ("battlefield", "Battlefield haze at dusk, tenth-century South India"),
 "S": ("stone macro", "Weathered carved granite, raking side light"),
 "C": ("copper still life", "Still life on dark wood, one oil lamp"),
 "A": ("scholar's desk", "Twentieth-century Indian scholar's study, warm desk-lamp light"),
 "T": ("present day", "Present day, soft morning light, rural Tamil Nadu"),
 "K": ("1950s Madras", "Madras in the 1950s, warm tungsten light"),
 "N": ("novel (storybook)", "Storybook illustration mood, moonlight and lamp glow, tenth-century South Indian palace"),
 "X": ("symbolic still life", "Dark room, a single shaft of light"),
}
TAIL = "Painted-realism concept art, wide 16:9 cinematic film still, muted teal and amber palette, deep shadows, 35mm film grain. No faces shown. Any writing is weathered and illegible. No text, no captions, no watermark."
lines = json.load(open("script/lines.json", encoding="utf8"))
cap = {(l["clip"], l["q"]): l["cap"] for l in lines}
counts = json.load(open("shots/counts.json"))
rows, per = [], collections.Counter()
for raw in open("shots/shots.txt", encoding="utf8"):
    raw = raw.strip()
    if not raw or raw.startswith("#"): continue
    clip, q, name, look, subj = raw.split("|", 4)
    q = int(q); per[(clip, q)] += 1
    n = len(rows) + 1
    rows.append({"n": n, "clip": clip, "q": q, "k": per[(clip, q)] - 1, "name": name, "look": look,
                 "file": f"EP11_{n:03d}_{clip}q{q:02d}_{name}.jpg",
                 "prompt": f"{subj[0].upper()+subj[1:]}. {LOOK[look][1].split(', bare-chested')[0] if 'no people' in subj else LOOK[look][1]}. {TAIL}"})
bad = 0
for clip, cs in counts.items():
    for q, c in enumerate(cs):
        if per[(clip, q)] != c: bad += 1; print("count", clip, q, "want", c, "have", per[(clip, q)])
json.dump(rows, open("shots/prompts.json", "w"), indent=1, ensure_ascii=False)
md = [f"# EP11 Aditya Karikalan: shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules used in every prompt: reconstruction art, not photographs; people are shown from behind, as silhouettes or as hands only; no bodies or injuries; no readable writing (all text is set in the edit).\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}] ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
