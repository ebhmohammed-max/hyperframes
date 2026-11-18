#!/usr/bin/env python3
"""shots/shots.txt -> shots/prompts.json, SHOTLIST.md. Checks the image count per line against shots/counts.json.
Row format:  clip|line|name|look[@ref,ref]|subject     (refs = keys in shots/CAST.md; their pictures are passed as reference images)"""
import json, collections
RAJ = ", people in late 16th-century Rajput dress, men in long jama tunics with sashes and turbans, women in ghagra skirts, short blouses and long veils, modest, faces small or turned away"
LOOK = {
 "B": ("Bhangarh today, daylight", "Present day, the ruins of a 16th-century Rajput town in a valley below steep scrub-covered Aravalli hills in Rajasthan, low roofless walls of grey-brown rubble stone, trimmed grass and old banyan trees, soft morning light, no signboards, no wires, no poles, any people small and seen from behind"),
 "N": ("Bhangarh after dark", "The ruins of a 16th-century Rajput town below scrub-covered Aravalli hills in Rajasthan at dusk or by moonlight, roofless rubble-stone walls, old banyan trees, deep blue shadows, no electric lights, no ghosts or apparitions, any people seen from behind"),
 "P": ("the town in its living days", "A Rajput town in Rajasthan in the late 16th and 17th centuries in its living days, sandstone and rubble-stone buildings with flat roofs and carved balconies, steep scrub-covered hills behind, warm daylight" + RAJ),
 "S": ("the legends (storybook mood)", "A Rajasthani folk tale, storybook mood with lamp glow, long shadows and a touch of mist, an old Rajput town below scrub-covered hills" + RAJ),
 "M": ("records", "An old Rajasthani record room, warm oil-lamp light, cloth-wrapped bundles and long narrow ledgers of handmade paper carrying only faint illegible marks"),
 "F": ("the famine of 1783", "North India in a great drought of the 1780s, cracked dry earth, bare trees, a pale dusty sky, nobody shown suffering, no bodies, any people only from behind or far away in plain cotton dhotis, turbans and veils"),
 "W": ("wildlife of the Aravallis", "Dry rocky forest and old stone ruins of the Aravalli hills in Rajasthan at dusk or by moonlight, the mood of a natural wildlife photograph"),
 "T": ("visitors and guards today", "Present day Rajasthan, at the ruins of an old Rajput town below scrub-covered hills, any people seen from behind or as hands only, ordinary present-day Indian clothes, no readable writing, no logos"),
 "X": ("symbolic still life", "Dark room, a single shaft of light on dark stone"),
 "O": ("setting given in the subject", ""),
}
REF = {
 "ratnavati": "The princess is the same young woman as in the reference picture: same face, deep red and gold ghagra skirt and long veil, gold forehead ornament.",
 "singhia": "The sorcerer is the same man as in the reference picture: same gaunt face, matted black hair and long black beard, black and dark red robes, bead necklaces.",
 "board": "The notice board is the same as in the reference picture: a dark blue metal board with a small white emblem and rows of small white lettering that stays soft and unreadable, fixed to an old rubble-stone wall.",
 "gate": "The gateway is the same as in the reference picture: same stone, same arch, same shape.",
 "bazaar": "The street is the same as in the reference picture: a straight paved lane between two rows of roofless stone shop cells.",
 "palace": "The palace ruin is the same as in the reference picture: same stone, same shape, standing against the same scrub-covered hillside.",
 "temple": "The temple is the same as in the reference picture: same honey-coloured sandstone, same curved spire and pillared porch on a high plinth.",
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
    if "no people" in subj: setting = setting.split(RAJ)[0].split(", any people")[0].split(", nobody shown")[0]
    refs = refs.split(",") if refs else []
    for k in refs: assert k in REF, (n, k)
    r_ = {"n": n, "clip": clip, "q": q, "k": per[(clip, q)] - 1, "name": name, "look": look,
          "file": f"EP14_{n:03d}_{clip}q{q:02d}_{name}.jpg",
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
md = [f"# EP14 Bhangarh: shot list\n\n{len(rows)} images. File names carry the running number, narration clip and line.\n",
      "Rules: every picture is an illustration, not a photograph of the site. The views of the ruins follow the real layout (gateway, bazaar street, temples, palace on the slope) loosely, with reference pictures (`gate`, `bazaar`, `palace`, `temple`, `board`) to keep them alike. "
      "The legend figures Ratnavati and Singhia have invented faces, kept alike with reference pictures. Guru Balu Nath is honoured at a shrine on the site to this day, so he is never shown by face: from behind, far away or as hands. Real rulers (Bhagwant Das, Man Singh, Madho Singh, Akbar, Chhatr Singh, Ajab Singh, Jai Singh) are never shown by face: from behind, far away or as hands. "
      "No ghost or apparition is ever shown. No blood, no bodies, nobody shown starving. Present-day people from behind or as hands only. No readable writing: the notice board's lettering stays unreadable (its real wording is in FACT_SHEET.md and goes on screen in the edit).\n",
      "Looks: " + "; ".join(f"**{k}** {v[0]}" for k, v in LOOK.items()) + ".\n"]
cur = None
for r_ in rows:
    if r_["clip"] != cur: cur = r_["clip"]; md.append(f"\n## {cur}\n")
    md.append(f"**{r_['n']:03d}** `{r_['file']}` [{r_['look']}]{' refs: ' + ', '.join(r_['refs']) if r_.get('refs') else ''} ({r_['clip']} q{r_['q']:02d}: “{cap[(r_['clip'], r_['q'])]}”)  \n{r_['prompt']}\n")
open("SHOTLIST.md", "w", encoding="utf8").write("\n".join(md))
print(len(rows), "images;", bad, "count mismatches;", dict(collections.Counter(r_["clip"] for r_ in rows)))
