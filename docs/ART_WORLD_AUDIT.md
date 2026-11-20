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

## Status

Regenerated and verified: **007, 009, 013, 015, 024, 033, 037** — seven good.

Directions rewritten, image not yet regenerated: **001, 004, 006, 010, 012, 014,
016, 017, 019, 020, 021, 025, 029, 031, 035, 036, 038, 039, 041, 042, 043, 048,
052, 053, 054, 058, 061, 062, 065.**

The image tool caps at ten per turn, so this proceeds ten at a time. Nothing
renders until the set is clean.

## The rule that follows

**A contact sheet at thumbnail size cannot audit a world.** Every plate is read
at full size before it enters a render, and the question asked of it is not "is
this plausible ancient?" but "is this *this* world, and could this object exist
in it?"
