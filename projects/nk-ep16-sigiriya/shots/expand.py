#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
ROCK = "Sigiriya in central Sri Lanka: one huge flat-topped rock of dark orange-streaked stone rising sheer about 180 metres out of a green jungle plain"
LOOK = {
 "A": ("Anuradhapura court, 5th century", "Sri Lanka in the 5th century, the royal city of Anuradhapura, halls of plain stone pillars with timber beams and red tiled roofs, white dome-shaped stupas far away, warm dusty light, small clay or bronze oil lamps only, no glass", ", men bare-chested in white or coloured waist cloths with gold necklaces and armlets, long hair tied in a topknot, no turbans, no stitched coats"),
 "K": ("Sigiriya in Kashyapa's time, about 480 CE", ROCK + ", as it was about the year 480, white lime plaster and red tiled roofs on brick terraces, nothing modern", ", people of 5th century Sri Lanka, bare-chested men in waist cloths, hair in topknots, faces small or turned away"),
 "B": ("the battle of 495, shown without harm", "A wide open plain in northern Sri Lanka in the year 495, dry grass, reeds and scattered trees, dust in the air, soldiers bare-chested in waist cloths with spears and round shields, war elephants, nobody shown being hurt, no blood, no bodies", ""),
 "M": ("monks, always from behind", "Sri Lanka, old stone and brick, soft early light, a calm and respectful mood", ", the monks are Buddhist monks with shaven heads in plain saffron robes, always seen from behind or far away, no faces visible"),
 "P": ("the rock paintings", "Painted in the manner of 5th century Sri Lankan rock painting on old lime plaster: warm reds, ochre yellow and soft green, fine dark outlines, each woman shown from the waist up above a band of cloud, wearing a fitted blouse, a tall jewelled headdress, necklaces and bangles, fully and modestly clothed, the rough rock visible around the plaster", ""),
 "N": ("legend, not record", ROCK + ", shown as in a legend: glowing gold light, heavy clouds, a dreamlike mood, clearly a vision and not a record, any figures tiny and far away", ""),
 "T": ("Sigiriya today", ROCK + ", as it is today, old weathered brick ruins, clipped grass and tall trees, soft daylight, no signboards, no wires, no cars", ", any people seen from behind in plain present-day clothes"),
 "V": ("19th and 20th century, old photograph look", "Sri Lanka, with the look of an old photograph of that time, faded and slightly warm, real people and real places, any people seen from behind", ""),
 "X": ("symbolic still life", "A dim stone room in old Sri Lanka, a single shaft of light on dark stone and old wood, only a small clay oil lamp if any lamp, no glass, no bookshelves, no people", ""),
 "O": ("setting given in the subject", "", ""),
}
REF = {
 "kashyapa": "The king is the same man as in the reference picture: same lean dark-brown face with sharp watchful eyes, short black beard and moustache, long black hair in a topknot, tall gold crown, bare chest with heavy gold necklaces and armlets, deep red silk waist cloth.",
 "dhatusena": "The old king is the same man as in the reference picture: same lined dark-brown face, white beard, white hair in a topknot with a low gold diadem, bare chest with heavy gold necklaces, a dark shawl over one shoulder, white waist cloth with a gold border.",
 "moggallana": "The prince is the same man as in the reference picture: same open dark-brown face, long black hair in a topknot, thin gold circlet, bare chest with a single gold chain, deep blue waist cloth.",
 "migara": "The army commander is the same man as in the reference picture: same heavy square dark-brown face, thick black moustache and no beard, hair tied back, crossed leather chest straps with bronze discs, a sword at his hip, dark green waist cloth.",
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
          "file": f"EP16_{n:03d}_{clip}q{q:02d}_{name}.jpg",
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
md = [f"# EP16 Sigiriya: shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: every picture is an illustration, not a photograph of Sigiriya. No likeness of Kashyapa, Dhatusena, Moggallana or Migara has come down to us, so their faces are invented (the film says so in its last chapter) and kept alike with reference pictures. "
      "No blood, no bodies, nobody shown being hurt or killed: the old king's death is a newly bricked wall, the battle is dust and far figures, Kashyapa's death is a dagger and a crown in the grass. "
      "The painted women are drawn in the manner of the rock paintings but clothed in a blouse, which the originals are not; no surviving painting is copied. Buddhist monks are shown from behind and with respect; no Buddha image is shown. "
      "The legend pictures (look N) carry the tag for belief or claim on screen. Later scholars and officers (Forbes, Bell, Paranavitana, Raja de Silva, the 1967 conservator) from behind only. No readable writing; the scratched verses are always out of focus. Present-day people from behind or as hands only.\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
