#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = cast keys in shots/CAST.md)"""
import json, collections
EPIC = ", people in ancient Indian epic-age dress of draped silk and gold jewellery, modest"
LOOK = {
 "L": ("Lanka palace interior", "Interior of a legendary golden palace in ancient Lanka, tall gold-plated pillars, brass oil lamps, polished dark stone floor, sheer curtains, warm lamp light and deep shadow" + EPIC),
 "G": ("Lanka, the golden city", "Legendary golden city of ancient Lanka on a hill above a tropical sea, gold-roofed towers and high ramparts, palms" + EPIC),
 "F": ("forest of the epic age", "Ancient Indian forest of the epic age, tall sal and banyan trees, shafts of soft light, mist" + EPIC),
 "H": ("hermitage and penance", "Ancient India of the epic age, a forest hermitage or bare mountain, thatched huts, sacred fire, sages with matted hair in bark cloth, dawn or dusk light"),
 "K": ("Mount Kailash", "Mythic Himalaya, a great snow peak under a starry sky, cold blue light with a warm glow near the summit"),
 "A": ("the Ashoka grove", "A walled garden grove in ancient Lanka, ashoka trees with red-orange blossom, stone lamps, dusk or moonlight" + EPIC),
 "W": ("the battlefield", "The plain below the ramparts of ancient Lanka at dusk after a battle of the epic age, broken chariots, fallen plain banners, drifting smoke, a red sky, no blood, no gore, no wounds" + EPIC),
 "J": ("later tales (storybook)", "Storybook illustration mood, soft moonlight and lamp glow, ancient India" + EPIC),
 "M": ("manuscripts and poets", "Old Indian scriptorium, warm oil-lamp light, palm-leaf manuscripts carrying only faint illegible scratches"),
 "T": ("North India today", "Present day, dry north-western or central India, soft morning light, old sandstone and whitewashed buildings, no signboards, no wires, no poles, no logos, any people seen from behind"),
 "X": ("symbolic still life", "Dark room, a single shaft of light on dark stone"),
 "O": ("setting given in the subject", ""),
}
TAIL = "Painted-realism concept art, wide 16:9 cinematic film still filling the whole frame, muted teal and amber palette, deep shadows, 35mm film grain. No readable writing anywhere. No text, no captions, no watermark."
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
    setting = LOOK[look][1]
    if "no people" in subj: setting = setting.split(EPIC)[0].split(", sages with")[0].split(", any people")[0]
    r_ = {"n": n, "clip": clip, "q": q, "k": per[(clip, q)] - 1, "name": name, "look": look,
          "file": f"EP13_{n:03d}_{clip}q{q:02d}_{name}.jpg",
          "prompt": f"{subj[0].upper()+subj[1:]}. " + (setting + ". " if setting else "") + TAIL}
    if refs: r_["refs"] = refs.split(",")
    rows.append(r_)
bad = 0
for clip, cs in counts.items():
    for q, c in enumerate(cs):
        if per[(clip, q)] != c: bad += 1; print("count", clip, q, "want", c, "have", per[(clip, q)])
for k, v in names.items():
    if v > 1: print("duplicate name", k)
json.dump(rows, open("shots/prompts.json", "w"), indent=1, ensure_ascii=False)
md = [f"# EP13 Mandodari: shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: illustration of a story told in old texts, not history and not photographs. Ravana, Mandodari, Maya and Indrajit have invented faces, kept consistent with the reference pictures in shots/CAST.md (marked `refs`). Ravana is drawn with one head; the ten heads appear only as a shadow, a statue or a stone relief. "
      "Rama, Sita, Lakshmana, Hanuman and Shiva are never shown by face: only from behind, far away, as a silhouette, or as a hand or a foot. No blood or wounds. Present-day people are seen from behind or as hands only. No readable writing (all text is set in the edit).\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
