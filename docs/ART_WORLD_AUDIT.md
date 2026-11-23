# Art world audit — Episode 02

The user looked at the finished stills and said they were **not the world of the
book or of George R. R. Martin**: modern-day objects and modern-day-looking
imagery, wrong for a fantasy saga, plus faces that read as real actors.

They were right. This is the audit, the cause, and the rule that prevents it.

## The cause was in our own text, not only in the model

Three scene directions literally asked for the wrong thing:

| Scene | Direction said | Produced |
|---|---|---|
| 054 | "beside a **modern** market scale" | modern digital scales |
| 056 | "a **modern** excavation trench" | modern excavation (intentional, see below) |
| 007 | "**legionaries**" | Roman legionaries |

And the style anchor named no world at all. It said "photoreal cinematic still,
natural light only, no text". Given an unanchored ancient setting, the model
pulls the nearest stock photograph: **Rome, Greece, medieval Europe, a
Mediterranean souk, or a Victorian interior.** That is what happened, across
most of the film.

## What was wrong, scene by scene

Forty of seventy were wrong-world. Thirty were usable.

| Failure | Scenes |
|---|---|
| Roman legionaries, lorica segmentata, galea | 007, 012, 013, 019, 033 |
| Greek aspis or hoplite round shields | 009, 013, 014 |
| Medieval Europe: trebuchet, gothic arches, keeps | 015, 016, 036, 039, 065 |
| Nineteenth century: glass lamp chimneys, scholars' desks | 010, 020, 031, 035, 037, 038, 043 |
| Modern: digital scales, Erlenmeyer flask, cargo pallets, knit beanie, naval cap | 001, 004, 006, 017, 024, 054, 056 |
| Wrong culture: minarets, Venetian harbour, Hanseatic quay, Gothic schoolroom | 024, 033, 053, 061 |
| Readable or gibberish lettering | 021, 025, 029, 041 |
| Actor-like faces | 042, 052, 058, 062 |
| Fantasy-game armour, no anchor in any real smithing | 062, 065 |

## Two modern images are correct and stay

- **056** — the archaeologist opening the ground. The narration says a man with
  a shovel found the jar in the last hundred years. Modern is the point.
- **070** — the museum case with its unread card. The film's last image, and
  the card it describes.

These are framing devices outside the ancient story, not errors inside it.

## The fix, and why it is in the file and not in a conversation

Prompts are no longer written by hand. `scripts/episode-audit/ep002_prompts.py`
emits the exact prompt for any scene from
`scripts/episode-audit/ep002_scene_directions.py`. The style anchor now names
the world and bans the specific pulls:

- **no real-world empires** — no Roman legionaries, lorica segmentata, galea,
  scutum, no Greek aspis, hoplite, Corinthian helmet, no Greek or Roman temples
- **no medieval Europe** — no crenellated keeps, gothic arches, stained glass,
  trebuchets, timber framing, thatch, knights, heraldry
- **no modernity** — no electric light, glass lamp chimneys, printed paper,
  books, newspapers, watches, plastics, scaffolding, pallets, engines, lab glass
- **no real ethnicity or place** — not Mesopotamian, Egyptian, Middle Eastern,
  Islamic, Ottoman, Chinese, Japanese, Nordic, Icelandic, European
- **no recognisable people** — every face an unfamiliar invented person, never
  a real actor or celebrity likeness

## Faces, specifically

The user asked for no celebrity or actor faces. The lever that works is
composition, not negatives: **keep faces out of frame.** Backs, profiles in
shadow, silhouettes, hands, over-the-shoulder. A face turned away cannot look
like anyone, and the shots become more cinematic for it.

Scene 042 and 052 are the highest risk — a Valyrian council and a dragonlord at
a window. Both should be composed so no face is legible.

## Status — 70 of 70 verified

This document previously claimed "all 70 pass". That claim was false twice, and
both times it was written from thumbnails and from my own notes rather than
from the files. It is recorded here rather than quietly deleted, because the
failure mode is the finding.

**What actually happened.** A fifth sweep rendered all 70 masters into five
640 px contact sheets covering every scene. Those sheets passed. Reading the
high-risk frames again at 900–1400 px failed three of them anyway:

| Scene | What the thumbnail hid | What full size showed |
|---|---|---|
| 042 | a council of robed figures | dragon skull on the wall, painted campaign table, silver-haired figures — the show's own war chamber |
| 058 | a cloaked figure from behind | silver hair over a black cloak — the show's lead, regardless of the camera |
| 070 | a coin in a case | a Roman denarius, laureate emperor in profile |

All three were rewritten, regenerated and re-verified, and all three are clean.

**070 took three attempts, and the two failures are the most useful thing in
this document.** Attempt one, a harpy on a flat-on coin face, came back as a
Roman denarius with a laureate emperor. Attempt two, with the heraldry spelled
out in the negative list, came back as an **Athena tetradrachm** — a helmeted
classical profile with a crest. Told exactly what not to draw, the model drew
the next classical coin along. Only the third attempt worked, and it worked
because the composition changed: a macro from directly above, the coin cropped
to a bare arc, raking light so the relief is texture, and no person in the
glass at all.

The generalisation is uncomfortable and worth keeping: **for an object with a
strong canonical form, no phrasing of the negative will save you.** A coin seen
face-on is a portrait die; to not have a portrait, you have to not see the
face. It is the same lesson as 005's pyramid and 042's war chamber, and it took
a third failure to make it stick.

**Replaced across the repair rounds (29 masters; 070 is in the list and is
now the face-free macro, not the denarius):**

    005 007 009 010 012 015 016 018 019 023 024 028 029 033 034 035
    042 043 044 045 049 050 052 055 056 058 065 069 070

Verified clean at full size, all 70: the 29 replacements above, plus 041, plus
every scene in 001–004, 006, 008, 011, 013, 014, 017, 020–022, 025–027,
030–032, 036–040, 046–048, 051, 053, 054, 057, 059–064, 066–068.

**One correction to an earlier note in this file:** scene 049 is *not* a
pyramid. "Pyramid", as a noun, produced Egypt or Mesoamerica three separate
times (005, 049, 069). The replacement is a sheer square brick tower, face
unstepped, summit flat. Nothing in the film is stepped.

### Two judgement calls, recorded rather than buried

**025 carries an invented script and is correct.** It shows a treaty roll with
rows of cut marks and stamped seals. The earlier ban on lettering came from
scene 044, where *legible English* was burned into the frame by accident. Here
the marks are a non-Latin invented script and the narration for this block is
a treaty of forty clauses with a forbidden word — a written treaty is what
the shot is of. Banning text outright would have banned the subject.

**039 has a rectangular window with sky in it.** Soft pass. It is a stone
slot, not a castle, nothing in the view leaks a second world, and the clerk is
seen from behind. It is noted because 017 failed in exactly this position.

## What the third pass taught

Two failure modes recur and neither is about style words.

**A window with a view is a world leak.** Scene 017 put a crenellated
medieval castle outside a Ghiscari window. The fix is to take the window
out, not to ask for a different castle.

**An instruction not to write becomes an instruction to write.** Told "no
lettering", scene 025 produced rows of invented glyphs that still read as
text across the frame, and scene 021 produced cut tally marks, which read
as a counting system and work. The difference is texture versus text: many
small marks pass, a row of distinct signs does not.

## What the second pass taught

The negative list alone does not stop a wrong face. Scenes 043, 010 and 012
were regenerated with the full world anchor and still came back with legible,
actor-like faces, and 012 additionally grew horned fantasy-game helmets.

The lever that works is **camera**, not prose. Every scene with people is now
written as one of: from behind, over the shoulder, in silhouette, heads
turned away or down, or faces hidden in shadow. 019 and 052 are the proof —
both full of people, neither with a face you could mistake for someone.

## What the full-size pass taught

Three more failures, all of a kind that no contact sheet can catch.

**Face-away is not enough.** Scene 058 was a cloaked figure seen from behind,
which satisfied the camera rule and still failed: silver hair over a black
cloak reads as the show's lead from any angle. Change the hair and the
garment, not the camera. It is now a shaved head with a bronze circlet.

**A camel is a horse by a committee.** Naming a culture's *architecture* is
not enough when the composition is a symbol. Any scene that asked for a
"pyramid" got Egypt or Mesoamerica; any scene that asked for dragon heraldry
got the show's own three-headed sigil and its cast. Emblems have to be
replaced with something the film invented — a plain harpy with a raised fist
and a spear — and not merely forbidden.

**A ban cannot fix a composition that demands the banned thing.** Scene 065
kept returning gothic arches because it was written as an interior with a
vault overhead; the fix was an exterior, roofless terrace. Scene 042 kept
returning the show's war chamber because it was written as a council at a
painted table; the fix was a bare brick vault and a plain clay floor.

The floor for this film is: **read every high-risk frame at 900 px or more,
and treat an emblem, a distinctive hairstyle or a costume silhouette as
high-risk regardless of the camera.**


## The delivered-frame sweep, and why the master audit was still not enough

Even with all seventy masters verified, reading frames out of the **finished
film** found five more violations. Four of them were in scenes this document
had already certified. That is the important part: the master sweep was run on
masters, and three of these passed it because the motif *matched the intent*.

| Scene | What the master audit saw | What the film showed |
|---|---|---|
| 001 | a gold disc in ash | a winged Nike, face-up — Greek coinage |
| 002 | "the harpy coin" | a winged Nike with **ΝΙΚΗ** cut in the field — Greek lettering |
| 057 | "the harpy face of the coin" | a gold stater, Nike in a chiton with a monogram |
| 012 | bowl caps and quilted hemp jackets | steel helmets and quilted field jackets — a 20th-century army |
| map | not a master at all | a Mesoamerican stepped pyramid drawn into the map base |

**The coin motif was wrong in every face-on instance.** All four coins — 001,
002, 057, 070 — have now been re-composed so the struck design never resolves:
turned edge-on, sunk in ash, hidden in a closed hand, or shot from directly
above in raking light. None of them shows a readable figure, and the word ΝΙΚΗ
is gone from the film.

**012 is the one I got wrong by my own wording.** The direction said "quilted
hemp jackets" and "bowl-shaped caps"; the model read that as quilted field
jackets and steel helmets, and produced an army from about 1916. No negative
would have fixed a description that specific — the nouns had to change. It is
now bare heads, coarse wool shawls, homespun tunics and bare feet.

**The map was never in the master set.** It is a separate asset in
`documentary_v2/assets/maps/`, and it carried a full stepped pyramid with a
central double staircase in the Ghis region. Nothing in the master audit could
have seen it, which is why the film itself has to be read and not just its
inputs.

### What follows from this

The audit rule changes from "read every master at full size" to **"read frames
out of the delivered cut, at full size, on scenes whose subject has a canonical
form."** Coins, pyramids, armies, emblems and costumes all have strong
canonical forms, and in each case the model reaches for the canonical version
unless the composition prevents it. A master can be reviewed by someone who
knows what the scene is *supposed* to be, and that reviewer will see the
intended thing. The film cannot lie that way.

## The rule that follows

**A contact sheet at thumbnail size cannot audit a world.** Every plate is read
at full size before it enters a render, and the question asked of it is not "is
this plausible ancient?" but "is this *this* world, and could this object exist
in it?"

## The full repair list, round three

Frames read out of the delivered cut found sixteen violations. Fourteen were
scenes this document had already certified. Listed together because the
number is the point:

| # | Defect found in the cut | Root cause in our own text |
|---|---|---|
| 001 | winged Nike on a coin, face-up | "the coin's face a winged woman" |
| 002 | winged Nike with **ΝΙΚΗ** in the field | "the harpy coin", face-on |
| 007 | Brodie helmets, khaki tunics, webbing | "infantry column", "iron caps" |
| 012 | steel helmets, quilted field jackets | "quilted hemp jackets" |
| 013 | conical steel helmets, mail, legible faces | "infantry", "iron spears" |
| 015 | Brodie helmets on the catapult crew | crew described as "men", engine only |
| 019 | the same soldier again, quilted jacket and cap | "quilted hemp jacket and rounded leather cap" |
| 020 | face-on winged Nike | "the winged-woman figure at its centre" |
| 041 | heraldic double-headed eagle banners | "banners, each bearing a painted harpy" |
| 048 | pale silver hair on the riders | "dark cloaks and pale silver hair" |
| 051 | legionary aquila, struck coin, legible faces | "temple with a bronze harpy above the door" |
| 052 | the lead at a window: silver hair, black cloak | "long black cloak… pale silver-grey hair" |
| 054 | Roman eagles struck on the coins | "harpy-stamped gold coin lying flat" |
| 057 | Greek gold stater, Nike and monogram | "extreme close-up of the harpy face of the coin" |
| 060 | laurel-wreathed profile head | "the same small coin", passed hand to hand |
| 062 | silver hair, black cloak, at the lava field | "black-cloaked figure with silver hair" |
| map | stepped Mesoamerican pyramid | not a master — a separate map asset |

**Three patterns, and every one of them was self-inflicted.**

1. **The coin cannot be shown face-on.** Seven scenes put a coin face toward
   the lens and six produced classical coinage. A flat disc with a figure on it
   is a portrait die; the only reliable fix is to turn it, bury it, or lose it
   in a closed hand. All of them are now edge-on, face-down, or blank.

2. **Military vocabulary summons a real army.** "Quilted hemp jacket",
   "hemispherical iron caps", "infantry", "iron spears" — each returned a
   recognisable twentieth-century soldier. Negatives do not help, because the
   positive noun is the instruction. Every such description is gone; the
   characters are now bareheaded, barefoot and in undyed cloth.

3. **The lead's silhouette is a costume, not a face.** Silver hair over a black
   cloak reads as one specific character from any camera angle, including from
   behind. 048, 052, 058 and 062 all had it; all four now have shaved heads,
   bronze circlets and wool wraps.

**What the ban now carries**, inherited by every prompt:
no coin design; no military uniforms of any era; no steel or iron helmets;
no eagles, aquila, heraldry, banners or sigils.

**The rule this round proved:** a text audit of the *directions* is as
necessary as a visual audit of the images. All sixteen defects were visible in
the scene descriptions before a single image was generated. Reading the
directions for positive-language traps — and reading the delivered cut for
what actually landed — are two separate gates, and both have to happen.

## Round four: the two that passed twice

The third render was assembled and audited clean on cadence, seams and audio,
and nineteen replaced scenes were read out of it at full frame. Then a dense
one-frame-per-scene sweep of all seventy found two more, and both had already
survived two earlier audits of mine:

| Scene | What was there | Why the earlier audits missed it |
|---|---|---|
| 024 | a large, sharply lit, **fully legible face**, leather cloak, and a gabled timbered house its direction banned | it was never on a defect list, so the "keep faces out of frame" rule was never applied to it |
| 042 | **four clear three-quarter faces** around a table | it had been re-reviewed for the dragon skull and the silver hair, and those were gone, so it was closed |

**042 was structurally impossible to pass.** Six men seated around a table means
at least three must face the camera. The direction asked for "none of them seen
from the front", which that layout cannot deliver — the instruction was
unachievable in the composition chosen. Reframed from behind, so only backs show.

**024 is the more instructive failure.** Every other scene in the film keeps
faces turned away, because that rule was applied scene by scene as each was
rewritten. 024 was never rewritten, so it never received the rule, and it
carried the largest and clearest face in the film the whole way through. A
per-scene fix does not generalise; it only protects the scenes you happened to
touch.

Both were regenerated, verified at full size, and confirmed in the assembled
cut. Neither chunk needed a full re-render of the film: ch03 and ch05 were
rebuilt and the master re-assembled.

### The gate that now exists

`audit_ep002_stale.py` catches the mechanical half of this — it names any chunk
built on art that changed after capture, so a stale frame cannot reach an
assembly unnoticed again. It cannot catch a wrong image that was faithfully
rendered; only reading the cut does that.
