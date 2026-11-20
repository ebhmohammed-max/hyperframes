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

## Status — 69 of 70 verified, one open

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

All three were rewritten, regenerated and re-verified. 042 and 058 are clean.
**070 is the one open defect**: its direction now specifies a harpy with raised
fist and thunderbolt on the coin and a blank ivory label, but the image has not
yet been regenerated, so the file on disk is still the denarius. It must not
enter a render until it is replaced.

**Replaced across the two repair rounds (29 masters):**

    005 007 009 010 012 015 016 018 019 023 024 028 029 033 034 035
    042 043 044 045 049 050 052 055 056 058 065 069 070

Verified clean at full size: 005 007 009 010 012 015 016 018 019 023 024 029
033 034 035 041 042 043 044 045 049 050 052 055 056 058 065 069, plus every
scene in 001–004, 006, 008, 011, 013, 014, 017, 020–022, 025–027, 030–032,
036–040, 046–048, 051, 053, 054, 057, 059–064, 066–068.

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

## The rule that follows

**A contact sheet at thumbnail size cannot audit a world.** Every plate is read
at full size before it enters a render, and the question asked of it is not "is
this plausible ancient?" but "is this *this* world, and could this object exist
in it?"
