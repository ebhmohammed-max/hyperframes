# The voice engine cannot be punctuated into a slower read

I auditioned a second narrator and tested the last remaining lever. Both failed, and the failure is mechanical rather than a matter of taste.

## What I measured

Three narrators, same script, same detector, same method:

| Voice                      | Articulation  | Pause share | Block 01 duration                  |
| -------------------------- | ------------- | ----------- | ---------------------------------- |
| **Episode 01 (raw takes)** | **165.3 wpm** | **15.6 %**  | 23.22 s _(then conformed to 30 s)_ |
| voice-02                   | 197.2 wpm     | ~15 %       | 21.24 s                            |
| voice-03                   | 212.6 wpm     | 16.9 %      | 20.30 s                            |

The reference is now like-for-like: Episode 01's _raw takes_, measured the same way as the new ones. 165.3 wpm, 15.6 % pause share, 28.72 s mean block.

## The experiment that settles it

voice-03 already has the correct pause share — 16.9 % against Episode 01's 15.6 %. So the only lever left was _more_ pausing. I rewrote block 01 with a deliberate break at every clause boundary, nine hard breaks in 64 words, and rendered it again.

**It came back shorter: 20.30 s, and faster: 226 wpm.**

The engine treats punctuation as phrasing, not as time. Adding breaks does not buy silence — it produces a more clipped read. That closes the question. There is no text-side intervention that turns a 212 wpm narrator into a 165 wpm one.

## Why not stretch it

`audio/pilot/A3_TEMPO_LADDER.mp3` — block 01 at tempo 1.00, 0.84, 0.76 and 0.71, back to back, 104 s.

- **0.84** → 25.2 s, 16 % slow. Sounds plausible.
- **0.76** → 27.9 s, 24 % slow. Audibly artificial.
- **0.71** → 29.9 s, 29 % slow. A stretched recording, not a performance.

The only setting that fills the slot is the one that ruins it. And it has to run on all 70 blocks, so there is no hiding it.

## What this means for the channel

Every narrator this engine offers is **1.2× to 1.3× faster than the one that narrated Episode 01**, and the engine ignores pause instructions. Episode 01 could not have been produced this way — its raw takes land at 28.72 s mean _before_ any conform, which means that narrator was simply slower by nature.

So the decision is not "which voice" any more. It is one of these:

**A. Find the Episode 01 voice.** If that film was narrated on a different service, account, or voice model, that is where Ep02 should go. Nothing else will match it. If you know what produced it, tell me and I will use it.

**B. Accept a faster narrator and re-cut to 78 words a block.** Different film at a different tempo. It would sound like its own thing, not a sequel to Ep01. It is consistent and it is achievable on this engine.

**C. Stretch to fit.** Works mathematically, fails audibly. I would not ship it, and I am not going to quietly do it and hope.

**My recommendation is A**, and if A is impossible, B with the understanding that the two films will not sound alike.

## What is banked either way

- Script: 70 blocks, 4,672 words, 7 chapters, zero duplicates — unchanged and reusable under any voice.
- Reference measurement: **165.3 wpm, 15.6 % pause share.** The acceptance test for every narrator from now on.
- `metronome_ep002.py` — measures any take against that reference, fits a bounded correction, and refuses what it cannot make fit.
- Known limit: **this engine is non-deterministic** (identical text, 21.79 / 22.94 / 22.73 s) **and ignores punctuation as a timing control.** Both are now documented facts rather than suspicions.

## Listen

1. `audio/pilot/A3_TEMPO_LADDER.mp3` — the tempo experiment, 104 s. Judge whether 0.84 is acceptable, because that is the only viable stretch.
2. `audio/pilot/AUDITION_v03_B001.mp3` — voice-03 at natural pace, 21 s.
3. `audio/pilot/EP002_VOICE_COMPARISON.mp3` — voice-02 natural versus slowed, 78 s.

If voice-03 at 0.84 (25.2 s, 16 % slow) is something you would accept, say so and I will build all 70 that way and stop asking. If it is not, then this needs the Episode 01 narrator or a decision to let Ep02 run faster and be a different film.
