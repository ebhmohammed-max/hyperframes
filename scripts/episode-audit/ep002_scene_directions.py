"""Art direction for Episode 02's 70 scene masters.

One entry per 30-second block. Each line describes what the narrator is actually
saying in that block, so the picture and the voice are telling the same story.
Episode 01's plates were Valyrian coast - cool sea, sunset, dragon silhouettes.
Episode 02 is a different country: ochre brick, desert light, bronze harpies.

Style anchor is repeated in every prompt because it is what keeps 70 separately
generated images looking like one film.
"""

STYLE = (
    "Photoreal cinematic still from a fantasy saga set in an invented ancient "
    "world, 16:9 widescreen, shot on 35mm anamorphic, shallow depth of field, "
    "fine film grain, natural light only, no text, no watermark, no logos, "
    "no captions. NO REAL-WORLD EMPIRES: no Roman legionaries, no lorica "
    "segmentata, no galea helmets, no scutum or rectangular tower shields, no "
    "Greek aspis or hoplite round shields, no Corinthian helmets, no Greek or "
    "Roman statues or temples. NO MEDIEVAL EUROPE: no castles with crenellated "
    "keeps, no gothic pointed arches, no stained glass, no trebuchets, no "
    "timber-framed or thatched cottages, no knights, no heraldic surcoats. "
    "NO MODERNITY: no electric light, no glass lamp chimneys, no printed paper "
    "or books, no newspapers, no wristwatches, no plastics, no metal "
    "scaffolding, no cargo pallets, no engines, no digital or laboratory "
    "instruments, no machine-cut milled wood. NO REAL ETHNICITY OR PLACE: not "
    "Mesopotamian, not Egyptian, not Middle Eastern or Islamic, not Ottoman, "
    "not minarets, not Chinese or Japanese, not Nordic or Icelandic, not "
    "European. NO RECOGNISABLE PEOPLE: every face must be an unfamiliar "
    "invented person, never a real actor, never a celebrity likeness, never a "
    "portrait of a known performer. No invented lettering of any kind."
)

# Folded into every prompt. These are the specific pulls the model makes when
# only given a vague ancient setting: it reaches for Rome, for Greece, for
# medieval Europe, for a Mediterranean souk, or for a Victorian interior.
BAN = (
    "Fantasy antiquity only. Not Rome, not Greece, not medieval Europe, "
    "not the modern world. Every face unfamiliar and invented."
)

# Palette the whole episode lives in.
GHIS = "warm ochre and terracotta brick, dusty gold light, deep blue-violet shadows"
VALYRIA = "black volcanic rock, cold grey-blue haze, ember orange glow"

SCENES = {
1: ("A worn gold coin half-buried in grey volcanic ash inside a collapsed room of mud brick, the coin's face a winged woman with a raised fist and a thunderbolt, a broken clay water jar and a splintered wooden beam beside it, no tools, nobody present, daylight falling through the broken roof.",
    GHIS),
2: ("Close macro of a thumb turning a gold coin in a palm, the harpy and thunderbolt "
    "almost worn smooth, grey ash dust on the fingers, dark background.",
    "gold, ash grey, near-dark"),
3: ('A vast desert battlefield at dusk seen from high above, thousands of long iron spear shafts still planted upright in the dust where a Ghiscari phalanx stood, lockstep ranks with gaps in them, no bodies, long shadows, nobody left.',
    GHIS),
4: ('A slow wide river crossing a flat plain of cracked clay, long low brick drying sheds and stacked clay tiles along the bank, coated in dust, a single flat-bottomed reed boat, low sun, haze on the horizon, no machinery.',
    GHIS),
5: ("A colossal bronze harpy statue with spread wings and a raised thunderbolt standing on the flat-topped summit of a massive square brick tower above a desert city, seen from a day's sail away across still grey water, the tower sheer and unstepped with no staircases and no sloping faces and no tiered terraces, roofs of the lower city huddled below, no pyramid, no ziggurat, no stepped pyramid, no monument of stacked platforms.",
    GHIS),
6: ('A Ghiscari slave market seen from above and behind the buyers: a crowd of men with shaved heads in ochre tunics standing in loose lines in a walled dust yard, buyers in robes with their backs to the camera, one hand pressing a bone stylus into a wet clay tablet, bronze coins on a low table, harsh noon, no face legible, no turbans, no draped headcloths.',
    GHIS),
7: ('Ghiscari infantry in a shuffling column on a dry desert road, seen from behind and low: bare shaved heads and hoods under plain hemispherical iron caps with no crest and no brim, stiffened hide coats over undyed tunics, tall wicker shields on their backs, dust rising in a long plume, ochre hills beyond, no metal-plated armour, no horsehair, no helmets of riveted plate, unfamiliar soldiers of no earthly nation.',
    GHIS),
8: ('A dry volcanic peninsula across calm green sea: black basalt cliffs, terraced slopes of scorched grass and olive-like scrub, goats, a cluster of flat-roofed brick houses, thin smoke rising from the far mountains, warm haze.',
    VALYRIA),
9: ('An abandoned shield wall on an empty shore: tall hide-and-reed shields, plain weathered hide with faded red-dyed geometric borders and no spiral pattern, standing overlapping in a leaning line, a few fallen, scorched ground beyond them, no soldiers, wind-blown ash.',
    GHIS),
10: ('Ghiscari generals around a table of clay models of towers, walls and ships, seen from over the shoulder of one man in a dark cloak, the others leaning in as backs and hooded heads, no face legible, a hand with a bronze stylus pointing, braziers burning in a carved cedar hall of ochre brick, the walls plain plaster with no carving and no script and no hieroglyphs, warm firelight, no glass.',
    GHIS),
11: ("Two war fleets in a narrow strait at dusk, hundreds of oars, a harbour with a "
     "stone mole and a lighthouse, tension in the still water.", "grey-green sea, amber sky"),
12: ("A Ghiscari officer's back as he walks his line at night, torchlight along a rank of plain bowl-shaped caps with no crest and no plume and no neck guard, men in quilted hemp jackets sitting on the ground coughing and casting knucklebones, all heads turned away or down, and high above the cloud a vast slow wing-shadow crossing the moonlit ground, no horns, no ornament, no segmented metal armour.",
    GHIS),
13: ('Ghiscari infantry holding formation on an open shore while enormous wing-shadows sweep across them, iron spears still upright, oval wicker shields raised, faces upturned and unfamiliar, no enemy visible on the ground, smoke and firelight falling from above.',
    'grey smoke, orange firelight from above'),
14: ("A single large oval wicker-and-hide shield lying flat in the sand, painted ochre and black, its owner's formation gone, footprints leading away in perfect order, ash haze in the air.",
    GHIS),
15: ('Ghiscari engineers working a massive torsion catapult of braided sinew and timber on a mud-brick tower, its throwing arm hauled back by a windlass, seen from the side at a distance, men hauling on ropes, dust below, ochre city wall beyond, no wheeled field gun, no bolt-thrower, no ballista, no artillery carriage, no iron frame.',
    GHIS),
16: ('A treaty being sealed in a high cool hall of ochre brick and carved cedar: two seated envoys in heavy robes seen from behind and in profile, their faces hidden in shadow, a clay tablet of clauses between them, two seal stones, hands not quite touching, two spearmen standing back in the half-light in plain unadorned tunics with no armour and no shields, bare plaster walls with no carving and no bas-relief and no painted frieze on them.',
    GHIS),
17: ('The abandoned desk of a Ghiscari officer at dawn: a low table with a clay cup, a scratched map on hide weighed down with a stone, and a sheathed bronze sword on the bench, the seat empty and pushed back, thin grey-blue light from a high narrow slot in the mud-brick wall, no window view, no castle, nobody present.',
    GHIS),
18: ("A dragon's enormous folded wing and shoulder filling one side of the frame at the edge of a high black cliff, and down beyond it a harbour city at dusk with tiny boats and lamps, no people anywhere in the frame, no riders, no figures standing on the cliff, only the animal's hide and the drop and the lights far below, cold blue dusk.",
    VALYRIA),
19: ('A pay chest of split cedar spilled on a desert road, small bronze coins scattered in the dust, a broken wooden cart wheel beside it, and a Ghiscari soldier crouching to pick one up, seen from behind and from the side so his face is hidden, a soft quilted hemp jacket and a rounded leather cap, sandals and bare legs, a short plain blade at his belt, no metal scales, no cheek guards, no banded helmet, hard sun.',
    GHIS),
20: ("A worn gold coin held up to the light, the winged-woman figure at its centre almost smooth, a child's fingers holding it, an ochre-brick market blurred behind, warm shallow focus, no lettering.",
    'gold, ochre, warm shallow focus'),
21: ('A plan scratched onto a slab of smoothed hide and set in a clay frame: a thickened siege tower with an opening roof and timber dimensions marked with cut notches and tally strokes, no letters, a bronze awl and a clay lamp beside it, pinned to a brick wall.',
    GHIS),
22: ("A dragon on a rocky headland unable to go further, sea beyond, a Valyrian ship "
     "waiting offshore, the animal's enormous patience and irritation.",
     VALYRIA + ", grey sea, cold light"),
23: ('A warehouse interior at night lit by three small clay oil lamps with open pinched spouts and no glass: shelves of stacked unglazed jars and tied grain sacks, a bonded clerk tallying on a wax tablet with a reed stylus, a few tally notches cut into a wooden stick, packed earth floor, low timber ceiling, long shadows, no glass lamp chimneys, no printed book, no paper leaves, no metal pen.',
    "warm lamplight"),
24: ('A Valyrian tax official in a hooded oiled-wool cloak standing on a wet grey quay with a short desert horse, a purse at his belt, a dragon a distant black speck in the overcast, burnt brick rooflines behind, flat-roofed brick warehouses with parapets, no gables, no timber framing, no stepped roofs, no brick-arched windows, no northern European harbour.',
    "grey light"),
25: ('A treaty written on a long roll of cured hide laid open on a low table, rows of tally notches and stamped clay seal impressions down its length, a hand resting over the place where a clause has been cut away, a clay oil lamp burning, no letters, no words, no letterforms of any alphabet, no parchment paper.',
    GHIS),
26: ("A clay jar in a cavity under a floor of a humble brick house, lid off, eleven gold "
     "coins and a plain woman's ring inside, the floorboards above pushed aside.",
     "dark earth, one candle"),
27: ("Aerial of a desert city with its walls still standing, siege camps and burned "
     "districts outside, harpy statues intact on the gate towers.", GHIS + ", dust haze"),
28: ("A torch-lit night street of ochre brick in a Ghiscari city, seen low and level: empty, no crowd, no assembly, a worn sandstone doorway with a bronze harpy's head knocked from its bracket lying in the dust, one dog asleep on the step, distant temple fires beyond the rooftops, no people in robes, no banners, no throne, no gathering of nobles.",
    GHIS),
29: ('Ghiscari street-sweepers in undyed tunics brushing dust from brick paving between flat-roofed houses, and hanging from a wall bracket a single faded ochre cloth with a plain sewn harpy outline and no heraldry and no three-headed beast, a broom leaned against the wall, overcast morning light.',
    GHIS),
30: ("An empty harbour at dawn with no tribute ships, water flat, a single official "
     "standing on the mole watching for sails that are not coming.", "grey water, pale sky"),
31: ("The same ordinary Ghiscari room across four years, four narrow panels: a boy's hands at a small bronze furnace, a bride's hands on a loom with her face turned down, two men's hands patching a flat mud roof seen from below, and a limping veteran's stick and sandalled feet at the threshold, faces out of frame throughout, clay pots and a loom, ochre brick, no glass.",
    GHIS),
32: ("A cramped Valyrian governor's office in a hot Ghiscari city: a cracked clay water jug, stacked clay tablets of grain tallies, an exhausted man in a plain linen tunic writing with a reed stylus, no grandeur at all, no paper, no glass windows.",
    'hot ochre, harsh window light'),
33: ('A line drawn in the dust before a desert city, a single iron spear planted at the boundary with an ochre rag tied to it, the city low and ochre behind a haze of dust, flat roofs and squat square brick towers with battered outer walls, no ziggurat, no stepped pyramid, no tiered terraces, no domes, no minarets, bleached light.',
    GHIS),
34: ('A market of dried goods and clay: stalls of stacked clay amphorae, bowls of dates and figs and coarse salt, hanging bundles of dried fish, harpy-stamped bronze coins on a counter, a hand weighing one in a small balance scale, no tomatoes, no peppers, no potatoes, no maize, no green vegetables, ordinary ancient prosperity.',
    GHIS),
35: ('Ghiscari children seated on a clay bench in a mud-brick room being taught to count from a wall of tally marks scratched into plaster, an old master with a wooden pointer, clay counting tablets on their knees, rows of counters in a shallow tray, dusty air through a narrow unglazed opening, no painted warriors, no frieze of soldiers, no shields on the wall.',
    GHIS),
36: ('An idle Ghiscari watchtower of mud brick with a flat timber platform: a guard asleep sitting up at his post, knucklebones on the step, no enemy in any direction, the desert horizon empty, late afternoon.',
    'grey-blue, long afternoon'),
37: ('A shipyard at the edge of a dry coast: half-built hulls of a heavy sea-going design in oak and cedar, shipwrights using unfamiliar bronze adzes and twisted cord, no metal scaffolding, dust and sawdust, hard afternoon light, flat-roofed sheds.',
    'cold grey, wet wood, overcast'),
38: ('An ordinary Ghiscari village: flat bread on a mud sill, two women arguing over a boundary stone, children throwing stones at a tethered goat, a humped ox, flat mud-brick roofs, no thatch, no churchyard, nobody important.',
    'soft ochre daylight'),
39: ("A counting house interior of ochre brick with hide maps on the wall, a clerk still reading yesterday's clay tally, while through the narrow window the first smoke rises on the horizon, clay lamps, no paper, no globes.",
    'lamplight, then grey'),
40: ("The buried jar still closed in complete darkness under the floor, ash beginning to "
     "sift down through the boards onto its lid.", "black, one grey shaft of light"),
41: ('Four captured Ghiscari war banners of ochre cloth hung in a row on a brick wall, each bearing a painted harpy with spread wings, four, all intact, none of them burned, faded crimson and ochre.',
    'faded crimson and ochre'),
42: ('A Ghiscari council of war in a bare brick vault seen from behind at a low angle: six seated men in plain undyed robes with cropped dark hair, none of them seen from the front, a rough slab table between them carrying small clay blocks arranged as walls and streets, iron sconces on cracked plaster, no silver hair, no hooded cloaks in black, no dragon skull, no carved ornamental wall, no throne, no painted map, no gilded hall.',
    "warm firelight"),
43: ("Two men seated opposite each other at a rough plank table in a dim brick room, seen from behind one man's shoulder so neither face is legible, a clay dish of olives and flatbread between them, a small clay lamp with an open spout, a rolled hide document, no glass cups, no goblets, no bottles, no window glass, firelight only.",
    "warm firelight"),
44: ('A hand pressing a carved stone seal into a wet clay bulla on a folded hide document, a reed stylus and a small clay dish of pigment beside it, ochre brick and lamplight, no wax, no sealing wax, no quill, no feather pen, no string-tied scroll, no parchment roll.',
    "warm lamplight"),
45: ('A forest of masts in a harbour basin at sunset seen from the top of the mole, hundreds of lashed-reed and timber hulls packed side by side, crews furling sail, the ochre city rising behind, no banners, no heraldry, no pennants, no flags of any kind.',
    "green-grey sea, amber sky"),
46: ("A city seen from far out at sea, burning across its whole width, one solid column "
     "of smoke, the shore black.", "orange fire, black smoke, grey sea"),
47: ("A collapsed brick house interior seen from above through the fallen roof, the floor "
     "broken, the jar below still sealed in the dark under it.", "grey ash, deep shadow"),
48: ('A long column of Ghiscari captives on a desert road seen from behind and above: barefoot figures in ochre tunics with bundles on their heads, a dust plume, and further back a line of Valyrian riders on short desert horses, dark cloaks and pale silver hair, the road going on past the horizon, no faces legible.',
    VALYRIA),
49: ('A single vast square brick tower standing on an ash plain beside a grey sea, its face sheer and unstepped and its summit flat, the whole lower half sheared away and slumped into a long scree of brick, seen from a low angle, no pyramid, no ziggurat, no staircase up the face, no tiered terraces, no polished casing.',
    "ash grey, cold light"),
50: ("A long refugee column walking a dusty road away from the camera in the last light, bundles and waterskins on their backs and a hand cart and a goat, plain cloaks and hoods of undyed wool, one child holding an adult's hand, the sea and a broken ochre city behind, seen from behind at a distance so no face is legible, no plastic bags, no nylon backpacks, no modern clothing, no vehicles.",
    "dusk, sea haze"),
51: ("A small side-street temple in a lesser city with a bronze harpy above the door, "
     "markets going on around it, coin weighed in a hand in the foreground.",
     GHIS + ", ordinary afternoon"),
52: ('A tall figure in a long black cloak seen from behind at a tall unglazed stone window above a calm black sea, one hand resting on the sill holding a bronze wine cup, pale silver-grey hair, head turned to the water, the face not visible at all and no profile and no chin in frame, black stone sill, golden hour on the horizon, the sea entirely still.',
    VALYRIA),
53: ('A golden age Ghiscari coastline: busy harbours of flat-roofed ochre warehouses, fishing boats, full granaries, a dragon a distant speck in the sky, everything peaceful and slightly too quiet, no domes, no church towers.',
    'warm gold, blue sea'),
54: ("A harpy-stamped gold coin lying flat on a scarred wooden market counter in close focus, a second and third identical coin further along the same counter as it recedes into the blurred distance, a shallow pan of grain beside them, a merchant's hands resting at the edge of frame, no faces, awnings above, everything resting solidly on the wood, no free-floating objects.",
    'mixed warm light'),
55: ('A hand passing a small gold coin to another hand across a market stall in low evening light, both forearms in coarse wool and a bronze wrist-ring, a small clay oil lamp with an open pinched spout burning on the boards between them, blurred stalls behind, no glass lamp, no glass chimney, no lantern glass, no metal shade.',
    "warm lamplight, dusk"),
56: ('Men at the bottom of a hand-dug excavation pit cut down through grey ash to a burnt brick floor, a wide-mouthed clay jar lying on its side in the earth, long-handled spades and a pick still in the soil and a hand brush, sides of the pit heaped ash and loose rubble, hazy daylight from above, the workers small and faceless in silhouette, the pit walls and ash bed filling most of the frame.',
    "ash grey"),
57: ("Extreme close-up of the harpy face of the coin, wings, raised fist, thunderbolt, "
     "worn nearly smooth, held between two fingers against black.", "gold on black"),
58: ("A dragonlord standing at a cracked parapet above a conquered city at dusk, seen from behind and from a distance so the figure is small: shaved head with a plain bronze circlet, coarse dark breeches and a lye-stained workman's coat, one hand flat on the brick, smoke rising from the roofs below, no silver hair, no platinum hair, no long white hair, no black cloak.",
    VALYRIA + ", dusty gold"),
59: ("A coin on a merchant's scale beside grain weights, a hand adding weights, the coin "
     "just a lump of metal, no reverence.", "brown and gold, market light"),
60: ("Many hands over time passing the same small coin, a composite: soldier, fishwife, "
     "child, sailor, all in different light, the coin always the same.", "warm varied light"),
61: ('A wide slow river at dawn, willows on the muddy bank and flat-bottomed boats of lashed reed and timber pulled up on it, and far across the water a low foreign city of flat-topped brick towers and long walls rising out of the river mist, no domes, no minarets, no spires, no battlements, an entirely different country, green-grey water, dawn gold.',
    'green-grey water, dawn gold'),
62: ('A Valyrian dragonlord standing very still on black basalt at the rim of a lava field, seen small in the frame from a distance and slightly behind, a black-cloaked figure with silver hair against the ember glow, close-fitting dark scale armour with no ornament and no helmet, the calm of someone who has never lost, no face visible at this distance, ash and smoke drifting.',
    VALYRIA),
63: ("A fleet seen from directly above, a dragon's shadow crossing it, no enemy anywhere, "
     "the sea empty for a thousand miles.", "blue-green, high sun"),
64: ("The Fourteen Flames: a black volcanic range with smoke and a faint red glow in the "
     "fissures, no people, no city, simply enormous and indifferent.", VALYRIA + ", storm light"),
65: ('A wild dragon crouched in sleep on a vast fused black-stone terrace high on the smoking mountain, seen from behind and to one side at a distance, its wings folded and its eye shut, a low sheer wall of unbroken black stone behind it and the lava glow far below, a few robed figures standing small and far off at the terrace edge with their backs turned, no building interior, no hall, no ceiling, no roof, no walls of masonry, no columns, no arches, no windows, no doorway, moonlight and ember light only.',
    VALYRIA + ", ember and moon"),
66: ("Split impression: a battle plain empty of anyone, and in the foreground a single coin "
     "in a stranger's palm, the two scales of history.", "grey and gold"),
67: ("A coastline where a peninsula used to be, broken islands in grey water, the sea "
     "covering the shape of a country.", "grey sea, cold haze"),
68: ("A pair of hands apart from each other, one holding a sword, one holding nothing, "
     "unable to be joined, dark background.", "dark, single light"),
69: ('The ash plain of the ruined city at dusk, a bronze harpy statue with spread wings alone on a broken square brick plinth in the middle distance, cracked brick rubble and broken walls around it to the horizon, no staircase on the plinth and no tiered platforms and no pyramid and no stepped pyramid, no classical columns, no temple colonnade, last light on the bronze.',
    GHIS + ", last light"),
70: ("The coin in a museum case on dark velvet with a small blank ivory label beneath it and nothing written on it, a visitor's blurred reflection faintly visible in the glass, the coin's face showing a winged woman with a raised fist and a thunderbolt, no laurel wreath, no emperor's profile, no classical portrait bust, no Latin letters.",
    "dark, museum spot"),
}
