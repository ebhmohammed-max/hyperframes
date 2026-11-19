"""Art direction for Episode 02's 70 scene masters.

One entry per 30-second block. Each line describes what the narrator is actually
saying in that block, so the picture and the voice are telling the same story.
Episode 01's plates were Valyrian coast - cool sea, sunset, dragon silhouettes.
Episode 02 is a different country: ochre brick, desert light, bronze harpies.

Style anchor is repeated in every prompt because it is what keeps 70 separately
generated images looking like one film.
"""

STYLE = (
    "Photoreal cinematic still, 16:9 widescreen, shot on 35mm anamorphic, "
    "shallow depth of field, fine film grain, natural light only, no text, "
    "no watermark, no logos, no captions."
)

# Palette the whole episode lives in.
GHIS = "warm ochre and terracotta brick, dusty gold light, deep blue-violet shadows"
VALYRIA = "black volcanic rock, cold grey-blue haze, ember orange glow"

SCENES = {
1: ("A worn gold coin half-buried in grey volcanic ash inside a ruined brick room, "
    "a wood-handled shovel leaning against the wall, one face of the coin showing a "
    "woman with bird's wings raising a thunderbolt.", GHIS),
2: ("Close macro of a thumb turning a gold coin in a palm, the harpy and thunderbolt "
    "almost worn smooth, grey ash dust on the fingers, dark background.",
    "gold, ash grey, near-dark"),
3: ("A vast desert battlefield at dusk seen from high above, an abandoned legion "
    "formation of bronze spear points in the dust, no bodies, long shadows.",
    GHIS + ", dying light"),
4: ("A slow wide river crossing a flat plain of cracked clay, endless brick drying "
    "racks along the bank, low sun, dust haze on the horizon.", GHIS),
5: ("A colossal stepped brick pyramid rising over a desert city, a bronze harpy statue "
    "with spread wings and raised thunderbolt on its summit catching the last light, "
    "roofs of the lower city beyond, seen from a day's sail away.", GHIS),
6: ("A crowded slave market in the shadow of brick walls: a line of bound men, a "
    "clerk with a wax tablet, coins changing hands, faces in shadow, dusty air.",
    GHIS + ", harsh noon"),
7: ("Ten thousand legionaries in perfect lockstep on a dry desert road seen from the "
    "side, bronze-tipped spears a moving hedge, dust rising in a long plume.",
    GHIS + ", flat white light"),
8: ("A cold green volcanic peninsula across grey water, black cliffs, goats on a "
    "terraced slope, a few low stone houses, smoke from distant mountains.",
    VALYRIA + ", overcast"),
9: ("An abandoned shield wall: overlapping bronze-faced shields standing in a neat "
    "line on an empty shore, intact and undamaged, scorched ground beyond them, "
    "no soldiers.", GHIS + ", dusk"),
10: ("Ghiscari generals in a lamplit brick council hall around a table of clay models "
     "of towers and ships, one pointing, faces sceptical.", GHIS + ", lamplight"),
11: ("Two war fleets in a narrow strait at dusk, hundreds of oars, a harbour with a "
     "stone mole and a lighthouse, tension in the still water.", "grey-green sea, amber sky"),
12: ("A Ghiscari officer walking his line at night, torchlight on bronze helmets, men "
     "coughing and dicing, and above the cloud a vast slow shadow passing over the "
     "moonlit ground.", "night, torch amber, cold blue moon"),
13: ("Legionaries holding formation on an open shore while enormous wing-shadows sweep "
     "across them, spears still upright, faces upturned, no enemy visible on the ground.",
     "grey smoke, orange firelight from above"),
14: ("A single bronze-faced shield lying flat in the sand, its owner's formation gone, "
     "footprints leading away in perfect order.", GHIS + ", ash haze"),
15: ("Ghiscari engineers on a brick wall rampart adjusting a great torsion engine aimed "
     "at empty sky, ropes and counterweights, one man sighting along the arm.",
     GHIS + ", cold morning"),
16: ("A treaty signing in a shade-dappled brick hall, a scroll of twelve clauses, two "
     "seals, hands not quite touching, guards behind.", GHIS + ", interior shade"),
17: ("An ashamed Ghiscari officer alone at a table with a cup and a map, dawn light, "
     "the city wall outside the window unchanged.", "grey-blue interior, thin light"),
18: ("Valyrian dragonlords on a black volcanic terrace above the sea, a dragon's wing "
     "folded in frame, silver hair, looking down at a harbour far below.",
     VALYRIA + ", cold dawn"),
19: ("A pay chest on an ox cart on a desert road, coins spilled in the dust, a soldier "
     "crouching to pick one up, a broken wheel beside them.", GHIS + ", hard sun"),
20: ("A worn gold coin held to the light, the word for tribute visible at its worn "
     "edge, a child's fingers holding it, market stall blurred behind.",
     "gold, ochre, warm shallow focus"),
21: ("A parchment engineering drawing of a thickened siege tower with an opening roof "
     "pinned to a brick wall, lamp beside it, drafting tools, no signature.", GHIS + ", lamplight"),
22: ("A dragon on a rocky headland unable to go further, sea beyond, a Valyrian ship "
     "waiting offshore, the animal's enormous patience and irritation.",
     VALYRIA + ", grey sea, cold light"),
23: ("A warehouse interior at night: lamplit shelves of jars and grain sacks, a harbour "
     "master's ledger open, a clerk counting with a stylus, long shadows.",
     "lamp amber, deep brown shadow"),
24: ("A Valyrian tax official on a rainy quay with a horse, a purse and a bad expression, "
     "dragon circling far above, burnt rooflines in the background.", "rain, grey slate, cold"),
25: ("A treaty scroll unrolled to forty numbered clauses, a seal at the bottom, a hand "
     "resting over the place where a forbidden word is written.", GHIS + ", candlelight"),
26: ("A clay jar in a cavity under a floor of a humble brick house, lid off, eleven gold "
     "coins and a plain woman's ring inside, the floorboards above pushed aside.",
     "dark earth, one candle"),
27: ("Aerial of a desert city with its walls still standing, siege camps and burned "
     "districts outside, harpy statues intact on the gate towers.", GHIS + ", dust haze"),
28: ("A Valyrian house courtyard: rival dragonlord families in robes, dragons chained at "
     "the walls, a heated argument in progress, wealth everywhere.", VALYRIA + ", braziers"),
29: ("A street in an old coastal city being swept by two men, one bent toward a Ghiscari "
     "banner and one toward a Valyrian one, both flags hanging over the same square.",
     "grey-blue, overcast, weary"),
30: ("An empty harbour at dawn with no tribute ships, water flat, a single official "
     "standing on the mole watching for sails that are not coming.", "grey water, pale sky"),
31: ("An ordinary Ghiscari household over four years: a boy at an anvil, a bride, a roof "
     "being patched, a limping veteran at the door, the same room four times.",
     GHIS + ", domestic amber"),
32: ("A cramped Valyrian governor's office in a hot foreign city: bad water jug, grain "
     "ledgers stacked, an exhausted man writing, no grandeur at all.",
     "hot ochre, harsh window light"),
33: ("A line drawn in the sand before a desert city, a single bronze spear planted at "
     "the boundary, the city ghostly in the dust haze beyond.", GHIS + ", bleached light"),
34: ("A busy market with fresh produce and full stalls, harpy-stamped coins on a counter, "
     "hand weighing one in a scale, no soldiers, ordinary prosperity.", GHIS + ", warm afternoon"),
35: ("Ghiscari children in a schoolroom being taught from a wall painting of a legion "
     "formation, a master with a pointer, the lesson about the plain.", GHIS + ", dusty air"),
36: ("An idle Valyrian watchtower: a guard asleep at his post, dice on the step, no enemy "
     "in any direction, the horizon empty.", "grey-blue, long afternoon"),
37: ("A shipyard at the edge of the known world: half-built hulls of a heavy sea-going "
     "design, shipwrights at work, unfamiliar tools, grey northern light.",
     "cold grey, wet wood, overcast"),
38: ("An ordinary village scene: bread on a sill, two women arguing over a boundary "
     "stone, children throwing stones at a tethered goat, a cow, nobody important.",
     "soft ochre daylight"),
39: ("A counting house interior with maps on the walls, a clerk still reading yesterday's "
     "report, while through the window the first smoke rises on the horizon.", "lamplight, then grey"),
40: ("The buried jar still closed in complete darkness under the floor, ash beginning to "
     "sift down through the boards onto its lid.", "black, one grey shaft of light"),
41: ("Four captured Ghiscari war banners hung in a row on a brick wall, four, all intact, "
     "none of them burned.", "faded crimson and ochre"),
42: ("A Valyrian council of rival houses deadlocked, hands raised against each other, a "
     "map of a city between them nobody can agree to finish.", VALYRIA + ", torchlight"),
43: ("A Ghiscari negotiator at a Valyrian table being served a fine meal, escorted and "
     "watched, his scroll unopened beside his plate.", VALYRIA + ", warm interior, cold courtesy"),
44: ("A scroll of refusals: a hand writing a firm line, the word for ships struck out, "
     "the word for walls struck out, wax seal ready.", "candlelight, parchment"),
45: ("The Ghiscari fleet leaving harbour for the last time, every ship they have, "
     "banners up, no return formation, seen from the walls above.", GHIS + ", low sun"),
46: ("A city seen from far out at sea, burning across its whole width, one solid column "
     "of smoke, the shore black.", "orange fire, black smoke, grey sea"),
47: ("A collapsed brick house interior seen from above through the fallen roof, the floor "
     "broken, the jar below still sealed in the dark under it.", "grey ash, deep shadow"),
48: ("Long columns of captives on a desert road, watched by Valyrian riders, dust, the "
     "road going on past the horizon.", GHIS + ", harsh flat light"),
49: ("A ruined brick pyramid with salt crusted into the ground around its base, the "
     "plain white, a passing ship in the distance for scale.", "white salt, pale dust"),
50: ("Survivors walking down a coast road away from a ruin, carrying bundles and children, "
     "unbroken, not desperate, purposeful.", GHIS + ", early morning"),
51: ("A small side-street temple in a lesser city with a bronze harpy above the door, "
     "markets going on around it, coin weighed in a hand in the foreground.",
     GHIS + ", ordinary afternoon"),
52: ("A Valyrian dragonlord at a window above the sea, confident, wine in hand, the water "
     "outside entirely calm.", VALYRIA + ", golden hour"),
53: ("A golden age coastline: busy harbours, fishing boats, full granaries, a dragon a "
     "speck in the sky, everything peaceful and slightly too quiet.", "warm gold, blue sea"),
54: ("A harpy-stamped coin beside a modern market scale in three different cities, the "
     "coin identical in all three, the cities unrecognisable.", "mixed warm light"),
55: ("A coin passing from one hand to another in a dark market, neither face visible, "
     "only the exchange.", "dark, single warm light"),
56: ("A modern excavation trench dug down through ash layers to a brick floor, a jar "
     "exposed, a shovel, careful brushes, daylight above.", "grey ash, clean daylight"),
57: ("Extreme close-up of the harpy face of the coin, wings, raised fist, thunderbolt, "
     "worn nearly smooth, held between two fingers against black.", "gold on black"),
58: ("A Valyrian dragonlord in full confidence standing on a captured wall, the conquered "
     "city below, his posture exactly that of the men he defeated.", VALYRIA + ", cold light"),
59: ("A coin on a merchant's scale beside grain weights, a hand adding weights, the coin "
     "just a lump of metal, no reverence.", "brown and gold, market light"),
60: ("Many hands over time passing the same small coin, a composite: soldier, fishwife, "
     "child, sailor, all in different light, the coin always the same.", "warm varied light"),
61: ("A wide slow river at dawn, willows on the bank, flat-bottomed boats, distant city "
     "of many towers, entirely different country.", "green-grey water, dawn gold"),
62: ("A Valyrian dragonlord in armour that has never been damaged, standing very still, "
     "the confidence of someone who has never lost.", VALYRIA + ", cold clear light"),
63: ("A fleet seen from directly above, a dragon's shadow crossing it, no enemy anywhere, "
     "the sea empty for a thousand miles.", "blue-green, high sun"),
64: ("The Fourteen Flames: a black volcanic range with smoke and a faint red glow in the "
     "fissures, no people, no city, simply enormous and indifferent.", VALYRIA + ", storm light"),
65: ("A proud Valyrian hall in its full confidence, gold on everything, a harpy statue "
     "gilded, and through the high window the smoking mountain visible behind.", VALYRIA + ", golden"),
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
