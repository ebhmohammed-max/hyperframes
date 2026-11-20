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
5: ("A colossal stepped brick pyramid rising over a desert city, a bronze harpy statue "
    "with spread wings and raised thunderbolt on its summit catching the last light, "
    "roofs of the lower city beyond, seen from a day's sail away.", GHIS),
6: ('A Ghiscari slave market seen from above and behind the buyers: a crowd of men with shaved heads in ochre tunics standing in loose lines in a walled dust yard, buyers in robes with their backs to the camera, one hand pressing a bone stylus into a wet clay tablet, bronze coins on a low table, harsh noon, no face legible, no turbans, no draped headcloths.',
    GHIS),
7: ('Ghiscari heavy infantry in perfect lockstep on a dry desert road seen from the side: tall crested bronze helmets, scale and leather armour, long iron spears and wicker shields, dust rising in a long plume, ochre hills beyond, unfamiliar soldiers of no earthly nation.',
    GHIS),
8: ('A dry volcanic peninsula across calm green sea: black basalt cliffs, terraced slopes of scorched grass and olive-like scrub, goats, a cluster of flat-roofed brick houses, thin smoke rising from the far mountains, warm haze.',
    VALYRIA),
9: ('An abandoned shield wall on an empty shore: large oval wicker-and-hide shields, painted in ochre and black, standing overlapping in a neat line, intact and undamaged, scorched ground beyond them, no soldiers.',
    GHIS),
10: ('Ghiscari generals around a table of clay models of towers, walls and ships, seen from over the shoulder of one man in a dark cloak, the others leaning in as backs and hooded heads, no face legible, a hand with a bronze stylus pointing, braziers burning in a carved cedar hall of ochre brick, lamplight, no glass.',
    GHIS),
11: ("Two war fleets in a narrow strait at dusk, hundreds of oars, a harbour with a "
     "stone mole and a lighthouse, tension in the still water.", "grey-green sea, amber sky"),
12: ("A Ghiscari officer's back as he walks his line at night, torchlight along a rank of plain iron helmets and scaled armour, men sitting on the ground coughing and casting knucklebones, all heads turned away or down, and high above the cloud a vast slow wing-shadow crossing the moonlit ground, no horns, no ornament.",
    GHIS),
13: ('Ghiscari infantry holding formation on an open shore while enormous wing-shadows sweep across them, iron spears still upright, oval wicker shields raised, faces upturned and unfamiliar, no enemy visible on the ground, smoke and firelight falling from above.',
    'grey smoke, orange firelight from above'),
14: ("A single large oval wicker-and-hide shield lying flat in the sand, painted ochre and black, its owner's formation gone, footprints leading away in perfect order, ash haze in the air.",
    GHIS),
15: ('Ghiscari engineers on a mud-brick rampart straining at a great wooden torsion engine of twisted sinew and rope, no metal gearing, aimed at empty sky, counterweights and a sighting arm, one man looking along it, cold morning.',
    GHIS),
16: ('A treaty being sealed in a high cool hall of ochre brick and carved cedar: two seated envoys in heavy robes seen from behind and in profile, their faces hidden in shadow, a clay tablet of clauses between them, two seal stones, hands not quite touching, plain spearmen standing back in the half-light, shafts of dusty light, no paper, no lettering.',
    GHIS),
17: ('The abandoned desk of a Ghiscari officer at dawn: a low table with a clay cup, a scratched map on hide weighed down with a stone, and a sheathed bronze sword on the bench, the seat empty and pushed back, thin grey-blue light from a high narrow slot in the mud-brick wall, no window view, no castle, nobody present.',
    GHIS),
18: ("Valyrian dragonlords on a black volcanic terrace above the sea, a dragon's wing "
     "folded in frame, silver hair, looking down at a harbour far below.",
     VALYRIA + ", cold dawn"),
19: ('A pay chest of split cedar spilled on a desert road, bronze coins scattered in the dust, a broken wooden cart wheel beside it, and a Ghiscari soldier crouching to pick one up, seen from behind and from the side so his face is hidden, scale armour and a plain iron helmet with no crest, hard sun.',
    GHIS),
20: ("A worn gold coin held up to the light, the winged-woman figure at its centre almost smooth, a child's fingers holding it, an ochre-brick market blurred behind, warm shallow focus, no lettering.",
    'gold, ochre, warm shallow focus'),
21: ('A plan scratched onto a slab of smoothed hide and set in a clay frame: a thickened siege tower with an opening roof and timber dimensions marked with cut notches and tally strokes, no letters, a bronze awl and a clay lamp beside it, pinned to a brick wall.',
    GHIS),
22: ("A dragon on a rocky headland unable to go further, sea beyond, a Valyrian ship "
     "waiting offshore, the animal's enormous patience and irritation.",
     VALYRIA + ", grey sea, cold light"),
23: ("A warehouse interior at night: lamplit shelves of jars and grain sacks, a harbour "
     "master's ledger open, a clerk counting with a stylus, long shadows.",
     "lamp amber, deep brown shadow"),
24: ('A Valyrian tax official in a hooded oiled-wool cloak standing on a wet grey quay with a short desert horse, a purse at his belt and a bad expression, a dragon a distant black speck in the overcast, burnt brick rooflines behind, flat-roofed warehouses, no gables, no timber framing.',
    'rain, grey slate, cold'),
25: ('A treaty written on a long roll of cured hide laid open on a low table, rows of tally notches and stamped clay seal impressions down its length, a hand resting over the place where a clause has been cut away, a clay oil lamp burning, no letters, no words, no letterforms of any alphabet, no parchment paper.',
    GHIS),
26: ("A clay jar in a cavity under a floor of a humble brick house, lid off, eleven gold "
     "coins and a plain woman's ring inside, the floorboards above pushed aside.",
     "dark earth, one candle"),
27: ("Aerial of a desert city with its walls still standing, siege camps and burned "
     "districts outside, harpy statues intact on the gate towers.", GHIS + ", dust haze"),
28: ("A Valyrian house courtyard: rival dragonlord families in robes, dragons chained at "
     "the walls, a heated argument in progress, wealth everywhere.", VALYRIA + ", braziers"),
29: ('A street in an old coastal city being swept by two men with stiff palm brooms, one bent toward a Ghiscari harpy banner and one toward a Valyrian three-headed banner, both flags hanging over the same ochre-brick square, flat roofs, no cobbles, no gables.',
    'grey-blue, overcast, weary'),
30: ("An empty harbour at dawn with no tribute ships, water flat, a single official "
     "standing on the mole watching for sails that are not coming.", "grey water, pale sky"),
31: ("The same ordinary Ghiscari room across four years, four narrow panels: a boy's hands at a small bronze furnace, a bride's hands on a loom with her face turned down, two men's hands patching a flat mud roof seen from below, and a limping veteran's stick and sandalled feet at the threshold, faces out of frame throughout, clay pots and a loom, ochre brick, no glass.",
    GHIS),
32: ("A cramped Valyrian governor's office in a hot Ghiscari city: a cracked clay water jug, stacked clay tablets of grain tallies, an exhausted man in a plain linen tunic writing with a reed stylus, no grandeur at all, no paper, no glass windows.",
    'hot ochre, harsh window light'),
33: ('A line drawn in the dust before a desert city, a single iron spear planted at the boundary with an ochre rag tied to it, the city low and ochre behind a haze of dust, flat roofs and a stepped pyramid, no domes, no minarets, bleached light.',
    GHIS),
34: ("A busy market with fresh produce and full stalls, harpy-stamped coins on a counter, "
     "hand weighing one in a scale, no soldiers, ordinary prosperity.", GHIS + ", warm afternoon"),
35: ('Ghiscari children seated on a clay bench in a mud-brick room being taught from a wall painting of a phalanx formation, an old master with a wooden pointer, clay tablets on their knees, dusty air through a narrow window.',
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
42: ('A Valyrian council of rival dragonlord houses deadlocked: men and women in black robes with ember-coloured embroidery, silver hair, hands raised against each other, a carved stone map of a city between them nobody can agree to finish, firelight, black stone hall, faces unfamiliar and invented.',
    VALYRIA),
43: ("A Valyrian table set for a Ghiscari negotiator, seen from behind and above the visitor's shoulder: a bronze plate of fine food, an unopened hide scroll, a cup, and across the table two dragonlords in silhouette against a fire pit, their faces entirely in shadow, black stone and ember light, cold courtesy.",
    VALYRIA),
44: ('A hand striking out a line of tally notches on a cured hide scroll with a bronze awl, a second line cut away, a lump of wax ready for sealing, candlelight, no lettering of any kind, no paper.',
    'candlelight, parchment'),
45: ("The Ghiscari fleet leaving harbour for the last time, every ship they have, "
     "banners up, no return formation, seen from the walls above.", GHIS + ", low sun"),
46: ("A city seen from far out at sea, burning across its whole width, one solid column "
     "of smoke, the shore black.", "orange fire, black smoke, grey sea"),
47: ("A collapsed brick house interior seen from above through the fallen roof, the floor "
     "broken, the jar below still sealed in the dark under it.", "grey ash, deep shadow"),
48: ('A long column of Ghiscari captives on a desert road seen from behind and above: barefoot figures in ochre tunics with bundles on their heads, a dust plume, and further back a line of Valyrian riders on short desert horses, dark cloaks and pale silver hair, the road going on past the horizon, no faces legible.',
    VALYRIA),
49: ("A ruined brick pyramid with salt crusted into the ground around its base, the "
     "plain white, a passing ship in the distance for scale.", "white salt, pale dust"),
50: ("Survivors walking down a coast road away from a ruin, carrying bundles and children, "
     "unbroken, not desperate, purposeful.", GHIS + ", early morning"),
51: ("A small side-street temple in a lesser city with a bronze harpy above the door, "
     "markets going on around it, coin weighed in a hand in the foreground.",
     GHIS + ", ordinary afternoon"),
52: ('A Valyrian dragonlord seen from behind at a tall unglazed window above a calm black sea, one hand resting on the sill with a bronze wine cup, silver hair and a long black cloak, face turned to the water and not visible, black stone sill, golden hour on the horizon, the sea entirely still.',
    VALYRIA),
53: ('A golden age Ghiscari coastline: busy harbours of flat-roofed ochre warehouses, fishing boats, full granaries, a dragon a distant speck in the sky, everything peaceful and slightly too quiet, no domes, no church towers.',
    'warm gold, blue sea'),
54: ("A harpy-stamped gold coin lying flat on a scarred wooden market counter in close focus, a second and third identical coin further along the same counter as it recedes into the blurred distance, a shallow pan of grain beside them, a merchant's hands resting at the edge of frame, no faces, awnings above, everything resting solidly on the wood, no free-floating objects.",
    'mixed warm light'),
55: ("A coin passing from one hand to another in a dark market, neither face visible, "
     "only the exchange.", "dark, single warm light"),
56: ("A modern excavation trench dug down through ash layers to a brick floor, a jar "
     "exposed, a shovel, careful brushes, daylight above.", "grey ash, clean daylight"),
57: ("Extreme close-up of the harpy face of the coin, wings, raised fist, thunderbolt, "
     "worn nearly smooth, held between two fingers against black.", "gold on black"),
58: ('A Valyrian dragonlord seen from behind standing on a captured mud-brick wall, black cloak and silver hair, one hand resting on the parapet, the conquered ochre city spread below under flat roofs and thin smoke, his posture exactly that of the men he defeated, face not visible, cold light.',
    VALYRIA),
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
65: ('A proud Valyrian hall in its full confidence, seen down its length: black stone columns and a shallow domed ceiling, gold on everything, a bronze harpy statue with spread wings at the far end, and beyond the unglazed opening the smoking mountain, a few robed figures at a distance, no gothic arches, no stained glass, no lettering.',
    VALYRIA),
66: ("Split impression: a battle plain empty of anyone, and in the foreground a single coin "
     "in a stranger's palm, the two scales of history.", "grey and gold"),
67: ("A coastline where a peninsula used to be, broken islands in grey water, the sea "
     "covering the shape of a country.", "grey sea, cold haze"),
68: ("A pair of hands apart from each other, one holding a sword, one holding nothing, "
     "unable to be joined, dark background.", "dark, single light"),
69: ("The ash plain of the ruined city at dusk with the harpy statue still standing on "
     "its broken pyramid, alone.", GHIS + ", last light"),
70: ("The coin in a museum case on dark velvet with a small printed card beneath it, a "
     "visitor's reflection faintly visible in the glass.", "dark, museum spot"),
}

ORDER = [1]
