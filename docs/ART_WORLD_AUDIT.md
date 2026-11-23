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

## Round five: the first complete full-size sweep

The fourth render was assembled, seam-audited clean, loudness-measured and
delivered. Then, instead of spot-reading the scenes that had been replaced, all
seventy frames were extracted **from the delivered master at full 1920×1080**
(t = (N−1)·30 + 15 s) and read as eighteen 2×2 sheets of 800×450 tiles, with
every suspect immediately re-read at full frame. Four defects survived into
that cut:

| Scene | What was there | Class |
|---|---|---|
| 023 | a large, sharply lit, **fully legible face** at the ledger desk | close legible face |
| 032 | a **full profile portrait** of the governor, beard and all | close legible face |
| 063 | an **aircraft-carrier battle group** at flank speed under the dragon's shadow | 20th-century kit |
| 066 | a **face-on coin** with an encircling legend and a portrait bust | coin design |

All four were in scenes that had never appeared on a defect list, in any round.

**023 and 032 are the same failure as 024, and they are the more serious
finding.** `STYLE` said every face must be "an unfamiliar invented person". Both
faces were unfamiliar and invented — as identity, the rule was satisfied. What
made them wrong was **where the face sat and how it was lit**: 023 put a clerk's
face at a third of frame height under a lamp, 032 a man's profile in window
light. The style constant governed identity and never governed composition, so
nothing in the prompt stack forbade a portrait. It does now:

> **NO LEGIBLE FACE AT CLOSE RANGE** — no face may fill or dominate the frame
> and no face may be lit sharply enough to read as a portrait; anyone near the
> camera is turned away, seen from behind, hooded or shadowed, bent to their
> work, or cropped at the shoulders.

This is a change to `STYLE`, so it is inherited by every prompt in the film and
by every scene rewritten from here on. The `BAN` short form carries it too. The
lesson of round four was *generalise the rule across all seventy scenes*; the
lesson of round five is *write the rule at the level of the prompt stack, not
the scene*.

**063 is the noun trap again, in a new noun class.** "A fleet seen from directly
above" pulls the only fleet the model has ever seen from directly above: a
carrier group. The direction now names wooden oared galleys, square sails and
oar wash, and forbids metal hulls, turrets, stacks and modern hull wakes
outright. As with 007's army and 051's eagle, the fix is to remove the noun
class, not to add more negatives to a scene that lacks a period anchor.

**066 is the coin rule, for the seventh time.** Every coin held up to camera has
come back struck face-on (001, 002, 020, 057, 060, 066, 070). The only fixes
that have ever held are compositional: edge-on, face-down, inside a closed
hand, or lost in shadow. 066 now stands on the edge of the fingers, almost
edge-on, with an empty struck field.

### What this round changes about the audit method

Spot-reading replaced scenes is not an audit. Three rounds of audits that read
only the scenes someone had touched missed four defects that a single complete
pass over all seventy frames found in under an hour. **The gate for release is
one full-size read of every frame of the delivered cut** — this is now the last
step before delivery, not an optional extra, and it must happen on the master
rather than on the masters, because the master is what ships.

### Release gate: the sweep that gated this render

The fifth render (the one now delivered) was gated by a complete full-size read
of all seventy frames **taken from the assembled master**, before delivery, not
after. Result: **70/70 pass, four defects fixed, none remaining.**

| Sheet | Frames | Verdict |
|---|---|---|
| 1 | 001–004 | pass — coin edge-on, map insert intended |
| 2 | 005–008 | pass — harpy emblem intended; 007 bareheaded |
| 3 | 009–012 | pass |
| 4 | 013–016 | pass |
| 5 | 017–020 | pass — 020 coin worn blank |
| 6 | 021–024 | pass — **023 fixed**, 024 still correct |
| 7 | 025–028 | pass — 027 harpies intended (direction names them) |
| 8 | 029–032 | pass — **032 fixed** |
| 9 | 033–036 | pass |
| 10 | 037–040 | pass |
| 11 | 041–044 | pass — 042 still all backs |
| 12 | 045–048 | pass |
| 13 | 049–052 | pass |
| 14 | 053–056 | pass |
| 15 | 057–060 | pass — 058 cap is unmarked, not military |
| 16 | 061–064 | pass — **063 fixed** (wooden galleys) |
| 17 | 065–068 | pass — **066 fixed** (edge-on coin) |
| 18 | 069–070 | pass — 070 museum case intended |

Measured on this master: 2100.118667 s, 63,540 frames, h264 1080p30 + aac
48 kHz stereo, 773,212,635 B. Seam audit EXIT 0, worst corner jump 13.3 (limit
25), zero cadence gaps. Loudness −16.81 LUFS, −1.27 dBTP, LRA 4.90.

### Drive delivery state (fifth render)

The master exceeds Arena's 100 MB upload cap, so it is delivered as 17
lossless stream-copy parts (`-c copy`, not a re-encode), 120 s segments,
largest 62.3 MB, total 737.4 MB. Parts sum to 2100.31 s against the master's
2100.12 s — boundary rounding only, no content difference.

Episode 02 folder `1SltSCtCl6DbqvYOaQi85KEpTdzqyZQqS`.

Uploaded (9 of 17): part00 `1t3nqCcJPG39hxCLsIa4rLcxb0rrp5ck6` ·
part01 `1eW6oo0H7-p6uF2zVnSHiKHIM_5UrtEyH` ·
part02 `1pJbP7utvcUwoucpgKrsWhKbw72PmJ6Ze` ·
part03 `131cnRNZFEX3dX34ce__dNCTqz47UfY_l` ·
part04 `19uq-JJzXzOPfHaR68uHEKFX-VETcbvhR` ·
part05 `1_XRAJmQhYf-Z82Fs1bahyTz6IijeYmgC` ·
part06 `1P7Vt8m6_kxRzbQliSGdhZdAnt4bV92Tn` ·
part07 `1LooMhJI1kk24POsyBhOCr92LU29r_fAu` ·
part08 `10qa7bDCPmBKuILOnRok15E6mBHjgkhFo`

**Still to upload (8 of 17):** part09–part16, plus `README.txt` (the
rejoin instructions, staged at `/tmp/driveparts/README.txt`).

Arena rate-limits uploads per reply; after roughly nine files the remainder
must wait for the next reply. Local parts live in `/tmp/driveparts/`.

**Upload completed.** All 17 parts plus the README are in the Episode 02 folder
`1SltSCtCl6DbqvYOaQi85KEpTdzqyZQqS`, and every part's Drive size matches its
local file byte for byte — 17/17 identical, 773,235,411 B on both sides, which
is 22,776 B of per-part MP4 container headers over the 773,212,635 B master.

| Part | ID | Bytes |
|---|---|---|
| 00 | `1t3nqCcJPG39hxCLsIa4rLcxb0rrp5ck6` | 65,333,789 |
| 01 | `1eW6oo0H7-p6uF2zVnSHiKHIM_5UrtEyH` | 50,091,253 |
| 02 | `1pJbP7utvcUwoucpgKrsWhKbw72PmJ6Ze` | 50,836,889 |
| 03 | `131cnRNZFEX3dX34ce__dNCTqz47UfY_l` | 41,566,680 |
| 04 | `19uq-JJzXzOPfHaR68uHEKFX-VETcbvhR` | 52,841,688 |
| 05 | `1_XRAJmQhYf-Z82Fs1bahyTz6IijeYmgC` | 39,596,886 |
| 06 | `1P7Vt8m6_kxRzbQliSGdhZdAnt4bV92Tn` | 45,829,716 |
| 07 | `1LooMhJI1kk24POsyBhOCr92LU29r_fAu` | 59,519,592 |
| 08 | `10qa7bDCPmBKuILOnRok15E6mBHjgkhFo` | 50,651,558 |
| 09 | `1UlEf0FbjyENyjd3BKXSUSxdSVMglGvNf` | 40,887,417 |
| 10 | `10IOYwmrEVUj83Pml0Nwuh_pAI87tokvh` | 53,168,881 |
| 11 | `1NehJd2CWMU4-gnj_OjIb6BTnBKAx7Shu` | 18,413,171 |
| 12 | `1Hn4-Uj0gk1HgAWTgTl9FaiZ9HvkpW9pz` | 26,683,236 |
| 13 | `1haSgJ7Y_yorGrUuNlz1hCth70b_r_pxm` | 43,941,577 |
| 14 | `1vEXSPQyKEfZ1tcfS-uLqYi3Us7TmLyL2` | 42,922,939 |
| 15 | `1_uRJ22ugPcSN1Bz5eFFCMwgdlF1grQkY` | 54,926,770 |
| 16 | `18rUajyjl_9Z_nrazO5V2gJAFRea7mmSP` | 36,023,369 |
| README | `1Q0X8rJctxogD57Hy30FAlAxp4UG6ocAa` | 907 |

Delivery of the 35-minute documentary is complete: art gated, master verified,
and the film in Drive.

### Masters folder brought current

The Masters folder still held pre-fix art from earlier rounds. A size diff of all
70 Drive masters against the local files found **25 stale**: the 21 from the
handoff list, plus 023, 032, 063, 066 from this round.

All 25 were trashed and re-uploaded at full quality, then verified: **70/70
present, 70/70 byte-identical to local, 13,676,717 B.**

A failed shortcut worth recording. `update_file_content` looks attractive for
replacing a file in place, but the inline base64 payload is truncated by the
tool transport somewhere under 100 KB — a 121 KB value came back as
`Incorrect padding`. The bad payload also overwrote 057 before being detected,
which is why that scene was trashed and re-uploaded too. **Do not route large
binary content through `update_file_content`; use `upload_file` with a
`file_path`.** Trashing the superseded copy and uploading fresh is slower but
it is the only path that verifiably delivers whole files.
