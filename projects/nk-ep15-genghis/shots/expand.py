#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
MON = ", people in Mongol dress of that age, long wrap-over deel robes tied with sashes, felt boots, fur-trimmed hats, men with their hair in braided loops behind the ears, faces small or turned away"
LOOK = {
 "S": ("steppe life, late 12th century", "The Mongolian steppe in the late 12th century, wide rolling grassland under a huge sky, round white felt gers, small sturdy horses, soft natural light" + MON),
 "R": ("the khan and his army, early 13th century", "The Mongol world of the early 13th century, riders on small sturdy steppe horses, leather lamellar armour, fur-trimmed helmets, composite bows and quivers, horsehair standards, wide open land, nobody shown being hurt, no blood, no bodies"),
 "N": ("legend and funeral mood", "The Mongolian steppe of the 13th century at dusk or before dawn, low mist, cold blue light with a little torch glow, the mood of a legend, nobody shown being hurt, no blood, no bodies, faces not visible"),
 "C": ("the cities of Khwarazm, about 1220", "Central Asia in the early 13th century, mud-brick city walls, turquoise glazed domes, tall brick minarets, people in long robes and turbans with faces small or turned away, dusty warm light, nobody shown being hurt, no blood, no bodies"),
 "J": ("northern China, about 1211 to 1215", "Northern China in the early 13th century, grey brick city walls with timber gate towers and curved tiled roofs, dry winter hills, nobody shown being hurt, no blood, no bodies"),
 "T": ("Mongolia today", "Present-day north-eastern Mongolia, forested mountain ridges, river valleys and open grassland, soft daylight, no roads, no wires, no signboards, any people seen from behind"),
 "X": ("symbolic still life", "Inside a dim felt tent of the 13th century, a single shaft of light on dark felt and old wood, only a small clay oil lamp if any lamp, no glass, no bookshelves"),
 "O": ("setting given in the subject", ""),
}
REF = {
 "temujin_boy": "The boy is the same boy as in the reference picture: same face, head shaved on top with a short forelock and two small braided loops by the ears, plain worn brown deel robe tied with a cord.",
 "temujin": "The young man is the same man as in the reference picture: same face, black hair in braided loops behind the ears, thin moustache, dark blue deel robe with a leather belt.",
 "khan": "The khan is the same man as in the reference picture: same broad weathered face, long moustache and pointed beard streaked with grey, hair in braided loops behind the ears, white fur-trimmed hat, cream deel robe with a dark fur collar.",
 "borte": "The young woman is the same woman as in the reference picture: same calm round face, long black braids, deep red deel robe with blue trim.",
 "hoelun": "The mother is the same woman as in the reference picture: same strong lined face, hair bound under a plain felt cap, grey-green deel robe.",
 "jamukha": "The rival chief is the same man as in the reference picture: same lean sharp face, short black beard, black fur hat, dark brown deel robe with a silver belt.",
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
    setting = LOOK[look][1]
    if "no people" in subj: setting = setting.split(MON)[0].split(", people in long robes")[0].split(", any people")[0]
    refs = refs.split(",") if refs else []
    for k in refs: assert k in REF, (n, k)
    r_ = {"n": n, "clip": clip, "q": q, "k": per[(clip, q)] - 1, "name": name, "look": look,
          "file": f"EP15_{n:03d}_{clip}q{q:02d}_{name}.jpg",
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
md = [f"# EP15 Genghis Khan: shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: every picture is an illustration. No portrait of Genghis Khan was made in his lifetime, so his face in these pictures is invented (the film says so in its last chapter); it is kept alike with reference pictures (`temujin_boy`, `temujin`, `khan`). Börte, Hö'elün and Jamukha also have invented faces with reference pictures. "
      "Other real people (Yesügei, Toghrul, Jebe, Subutai, the Shah, the governor of Otrar, Jalal al-Din, Kublai) are shown from behind, far away or without a clear face. "
      "No blood, no bodies, nobody shown being hurt or killed: wars are shown as riders, dust, smoke far away and empty streets. Clergy of any faith are shown from behind and with respect. "
      "No readable writing and no maps that claim to be accurate. Present-day people from behind or as hands only.\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
