# Retention and on-screen graphics — The Long Night

Standing rules for every episode. Written because the published data says one
specific thing: people who get past the first minute finish the film. The
opening is the only part losing them.

## What the data actually says

| | |
|---|---|
| Drop in the first minute | 30–45 % |
| Retention after the first minute | near complete to the end |
| Conclusion | the body works; the opening does not |

This matters because it rules out the usual instincts. The film is not too
long, the middle is not sagging, and the narration is not losing people. Only
the first sixty seconds are losing them. Fix that and stop touching the rest.

## The diagnosis

Between 0:00 and 1:00 the film shows **thirty different images** and **four
text cards**. The cutting rate is one image every two seconds.

A strong hook is the opposite: **one thing, held, escalating.** When the eye is
given thirty pictures in a minute it has nothing to land on, so nothing
imprints. The single most valuable object in the episode — the coin — is on
screen for two seconds at 0:00 and then replaced by a battlefield at 0:04.

That is the fault. Not a shortage of graphics: a shortage of **focus**.

## The rules

### 1. The hook is a held object, not a montage
The first thirty seconds keep the audience on **one** image, slowly moving,
while the narration plants the question. One cut is allowed, at the punchline.
No churn.

### 2. One question, stated plainly, and deferred
Within the first twenty seconds the film says out loud what it is asking. It is
answered once, near the end. Stated early, deferred long.

### 3. The strongest visual asset appears first, not fourth
Whatever the episode's central object is — a coin, a map, a body, a door —
it opens the film and it closes it.

### 4. Escalate before explaining
Facts arrive after stakes. The five defeats are announced before the geography
is explained, because a viewer will wait for a story and will not wait for a
lesson.

## Graphics: when to add, when to refuse

The instruction was "add these if needed, not necessarily all of them." That is
the correct instinct and it has a test:

> **A graphic earns its place only if it makes something the narration already
> says easier to keep in the head.**

Decoration fails this test. A map that shows a strait the audience cannot
otherwise picture passes it. An animated bar chart over a line of narration
that is not about numbers fails it.

### Maps — use when the story is spatial
The five Ghiscari wars are a story about **distance across water**: two
continents, one strait, ships vs dragons that cannot swim. That is
unphotographable and must be mapped.

**Rule: the map is one image, animated by camera and by labels.** Never
generate a map with text baked in. Text in generated images is garbage or
wrong — see `DEFECTS.md` scene 044. All labels are HTML.

Map discipline:
- Enter only while the narration is talking about place.
- Move, do not cut. One continuous camera push.
- Declare the scale and the century once.
- Never more than three labels on screen at once.
- Leave before it becomes wallpaper.

### Motion graphics — use for quantity and sequence
Where the narration counts, rank, or sequences, show it. "Four times nothing"
is a countdown; a viewer who sees `FOUR` — `THREE` — `TWO` — `ONE` in the same
type as the chapter cards is being given the structure for free.

**Rule: motion graphics carry no new facts.** They restate a number, a name or
a sequence that the voice has already said. If a graphic introduces information
the narration has not given, it competes with the narration and loses.

### Mockups — use for objects that need examining
A coin at 1376×768 cannot be read. When the film needs the audience to examine
something — the harpy's face, a clause on a treaty, the wear on an edge —
present it as a specimen: isolated on black, lit, with a small mono caption.
This is a camera move plus a caption, not a new render.

### Chapter backgrounds — always
Every chapter card gets the image that belongs to that chapter, held behind the
existing card, slowly pushing. The card design, type, colour and its sound
effect are **frozen**. Only the plate underneath is added.

The background must be the chapter's *own* subject, not a generic texture:
the coin for Chapter I, the sea-wall for Chapter IV, the ash plain for VII.

## What is frozen

Not negotiable, on any episode:

- Narration text, voice, pronunciation, timing
- Chapter card design, typography, colour, and its sound effect
- Title card design
- Plate motion language: push / pull / pan, 1.055→1.000 and the rest
- Palette, grain, grade, vignette
- Music beds and their levels

Everything added by this document is a **layer on top**. If an addition would
require changing any of the above, the addition is wrong.
