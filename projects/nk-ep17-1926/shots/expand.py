#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
MAD = "Madras in South India in 1926, under British rule: low houses with clay-tiled roofs and raised front verandas with wooden pillars, lime-washed walls, coconut and palmyra palms, neem and banyan trees, bullock carts, no motor traffic unless named, no plastic, no concrete towers, no modern signboards"
PPL = ", Tamil people of the 1920s: men in white veshtis with shirts or bare-chested, some in turbans or coats, women in cotton saris worn in the old Tamil style with hair in a bun, children barefoot"
LOOK = {
 "H": ("inside the house", "Inside a modest Tamil house in Madras in 1926: lime-washed walls, a red oxide floor, wooden pillars and rafters under a clay-tiled roof, brass and clay vessels, reed mats, light only from a kerosene lamp, an oil lamp or a small window, no electric fittings, no plastic, no steel furniture", PPL),
 "S": ("street and town, 1926", MAD + ", warm dusty daylight unless another time is named", PPL),
 "W": ("work, 1926", MAD + ", a place of work, iron and brick, dusty light", PPL),
 "C": ("children and school, 1926", MAD + ", soft morning light", ", Tamil children of the 1920s, boys in shorts or small veshtis with bare chests, girls in long skirts and blouses with oiled plaits, barefoot"),
 "E": ("cinema, stage and wireless, 1926", "Madras in South India in 1926, an evening entertainment of that time, dark hall or night air, warm bulbs, footlights or lantern light, smoke in the beam, nothing modern", PPL),
 "N": ("night in the house", "Inside a modest Tamil house in Madras in 1926 at night: lime-washed walls, reed mats, one kerosene chimney lamp, deep soft shadows, a quiet and tender mood, nothing frightening", PPL),
 "T": ("present day", "South India in the present day, clean natural light, ordinary modern life, no brand names, no logos, any screen shows only a soft blur of light", ", any people seen from behind or as hands only"),
 "X": ("still life", "A still life on old dark wood or stone in South India in the 1920s, a single shaft of warm light, deep shadows, no people", ""),
 "O": ("setting given in the subject", "", ""),
}
REF = {
 "father": "The father is the same man as in the reference picture: about thirty-five, lean dark-brown face, neat black moustache, oiled hair combed back, white cotton shirt, white veshti, a plain black coat.",
 "mother": "The mother is the same woman as in the reference picture: about twenty-eight, dark-brown oval face, hair in a low bun with a short strand of jasmine, a red dot on her forehead, a small nose stud, a dark maroon cotton sari with a mustard border worn in the old Tamil style, glass bangles.",
 "girl": "The girl is the same child as in the reference picture: about eleven, thin, large dark eyes, two short oiled plaits tied with ribbon, a faded green long skirt and blouse, small ear studs, barefoot.",
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
          "file": f"EP17_{n:03d}_{clip}q{q:02d}_{name}.jpg",
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
md = [f"# EP17 1926, an ordinary day: shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: every picture is an illustration of how a day in Madras in 1926 may have looked, not a photograph. The family (father, mother, girl, a younger boy, a grandmother) is invented and the film says so in its last chapter; three of them are kept alike with reference pictures. "
      "No blood, no bodies, nobody shown being hurt. Illness and the death of infants are shown only through a hand on a forehead, an empty cloth cradle and unlit lamps; no sick or dead child is shown. Child marriage is shown only as a still life (a slate beside a folded silk sari) and a wedding house seen from far. "
      "Real people (Dr Muthulakshmi Reddy, J. L. Baird) are seen only from behind; the king's head on the coins is worn smooth. No readable writing: newspapers, tickets, postcards, telegrams and film title cards are set in the edit as mock-ups, and maps are drawn in the edit from real coastline data. Present-day people from behind or as hands only. "
      "Lines that carry a full-screen graphic have no picture.\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
