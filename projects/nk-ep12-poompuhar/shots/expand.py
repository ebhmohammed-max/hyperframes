#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = cast keys in shots/CAST.md)"""
import json, collections
MEN = ", bare-chested men in white dhotis with hair in topknots, women in simple draped cotton cloth"
LOOK = {
 "P": ("the ancient port, daylight", "Daylight, ancient Tamil port city of the Sangam age two thousand years ago, brick and timber buildings with thatch and tile roofs, coconut and palmyra palms, any ships are ancient single-masted vessels with one square sail and plain low hulls, never multi-masted European galleons" + MEN),
 "D": ("the ancient port, dusk", "Dusk, ancient Tamil coast of the Sangam age two thousand years ago, oil lamps, coconut and palmyra palms, any ships are ancient single-masted vessels with one square sail and plain low hulls, never multi-masted European galleons" + MEN),
 "L": ("ancient lamp-lit interior", "Night interior lit by brass oil lamps, ancient South India of the Sangam age, timber pillars and brick walls" + MEN),
 "B": ("the Manimekalai tale (storybook)", "Storybook illustration mood, moonlight and lamp glow, ancient Tamil coast, any ships are ancient single-masted vessels with one square sail and plain low hulls, never multi-masted European galleons" + MEN),
 "Y": ("the later town (5th to 12th century)", "Daylight, early medieval Tamil Nadu coast, granite and brick temples, palmyra palms" + MEN),
 "E": ("1960s excavation", "Archaeological excavation in coastal Tamil Nadu in the 1960s, hard tropical sunlight, palmyra palms, Indian workers in white dhotis and plain cotton shirts"),
 "N": ("survey at sea around 1990", "Bay of Bengal off the Tamil Nadu coast around 1990, the shore a flat low line of palms with no hills or mountains, hazy morning light, Indian crew in plain shirts and shorts, plain older equipment, no logos"),
 "R": ("ship's cabin around 1990", "Cabin of an Indian research vessel around 1990, dim green instrument light, plain unlabelled equipment"),
 "U": ("underwater", "Underwater in the Bay of Bengal, murky green-blue tropical water, a bare seabed of sand and silt with only thin weed, no coral reef, soft shafts of sunlight from the surface, drifting particles"),
 "M": ("survey at sea, present day", "Present day, Bay of Bengal off the Tamil Nadu coast, the shore a flat low line of palms with no hills or mountains, soft morning light, Indian crew in plain work clothes, no logos, no signboards"),
 "T": ("the coast today", "Present day, soft morning light, coastal Tamil Nadu, palmyra palms and sand, no wires, no poles, no signboards"),
 "G": ("computer laboratory", "Dark modern Indian laboratory room, glow of computer screens, bare walls, no posters"),
 "A": ("scholar's desk", "Indian scholar's study, warm desk-lamp light, bare walls, no posters"),
 "I": ("end of the Ice Age", "South India at the end of the Ice Age, a warm wide dry coastal plain of scrub and scattered trees under a pale sky, no snow, no ice, dark-skinned hunter-gatherers wearing only simple hide loincloths, no furs, no buildings"),
 "W": ("ancient West Asia", "Ancient West Asia, bright dry Persian Gulf coast, date palms, mud-brick buildings, men in long plain tunics and head cloths"),
 "X": ("symbolic still life", "Dark Indian room, a single shaft of light on a plain wooden table"),
 "C": ("lamp still life", "Still life on dark wood, one brass oil lamp, South Indian setting"),
 "O": ("setting given in the subject", ""),
}
TAIL = "Painted-realism concept art, wide 16:9 cinematic film still filling the whole frame, muted teal and amber palette, deep shadows, 35mm film grain. No readable writing anywhere. No text, no captions, no watermark."
# Added after 159 came out looking like a built wall: used for the U-shape pictures from 160 on.
RIDGE = "The ridge is a low rounded bank about as high as a man, thickly coated in marine growth, with no cut blocks and no built masonry. "
RIDGE_SKIP = ("level_rows_hint", "natural_beachrock")
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
    if "no people" in subj: setting = setting.split(MEN)[0].split(", Indian workers")[0].split(", Indian crew")[0].split(", dark-skinned")[0]
    r_ = {"n": n, "clip": clip, "q": q, "k": per[(clip, q)] - 1, "name": name, "look": look,
          "file": f"EP12_{n:03d}_{clip}q{q:02d}_{name}.jpg",
          "prompt": f"{subj[0].upper()+subj[1:]}. " + (RIDGE if look == "U" and "ridge" in subj and n >= 160 and name not in RIDGE_SKIP else "") + (setting + ". " if setting else "") + TAIL}
    if refs: r_["refs"] = refs.split(",")
    rows.append(r_)
bad = 0
for clip, cs in counts.items():
    for q, c in enumerate(cs):
        if per[(clip, q)] != c: bad += 1; print("count", clip, q, "want", c, "have", per[(clip, q)])
for k, v in names.items():
    if v > 1: print("duplicate name", k)
json.dump(rows, open("shots/prompts.json", "w"), indent=1, ensure_ascii=False)
md = [f"# EP12 Poompuhar: shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: reconstruction art, not photographs. Karikala Chola, the poet, the king and the princess of the Manimekalai tale have invented faces, kept consistent with the reference pictures in shots/CAST.md (marked `refs`). Modern and living people (archaeologists, divers, the writer, the professor) are shown from behind, as hands only, or behind dive masks. "
      "The U-shaped structure is always drawn as a low, heavily overgrown ridge and never as clear walls, steps or carvings, because nobody knows yet what it is. The 11,000-year and 15,000-year claims are shown only as sketches, screens or dreamlike illustrations, never as realistic scenes. No readable writing (all text is set in the edit).\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
