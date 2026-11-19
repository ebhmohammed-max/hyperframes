# Pacing diagnosis — why the voice does not fill the slot

**Listen:** `audio/pilot/EP002_OPENING_11_BLOCKS_ON_CLOCK.mp3` — 5 min 30 s, the opening eleven blocks laid on the film clock with nothing hidden.

You will hear the problem in the first thirty seconds. Block 01 fills its slot. Block 02 stops talking at 21.5 seconds and the remaining 8.5 seconds are silent.

## The numbers

| Block | Words | Speech  | Dead air in a 30 s slot |
| ----- | ----- | ------- | ----------------------- |
| 01    | 64    | 26.61 s | 3.39 s                  |
| 02    | 62    | 21.49 s | **8.51 s**              |
| 03    | 68    | 24.69 s | 5.31 s                  |
| 04    | 62    | 23.45 s | 6.55 s                  |
| 05    | 64    | 22.38 s | 7.62 s                  |
| 06    | 63    | 22.48 s | 7.52 s                  |
| 07    | 66    | 24.65 s | 5.35 s                  |
| 08    | 66    | 23.37 s | 6.63 s                  |
| 09    | 66    | 24.52 s | 5.48 s                  |
| 10    | 62    | 22.09 s | 7.91 s                  |
| 11    | 68    | 24.52 s | 5.48 s                  |

**Speech fills 78.9 % of the clock. Mean dead air 6.34 s per block.** Across the whole film that is roughly 7.5 minutes of a narrator saying nothing.

## What the Episode 01 film actually did

Measured from the nine conformed blocks still on disk (`audio/review/B002–B010_30sec_v01.wav`):

- 67–71 words per block, not 62–66
- speech fills **26.9–29.4 s** of each slot
- silence **0.6–3.1 s**, mean ~1.2 s
- effective **134.4 wpm** across the 270-second wall

So the delivered film is _denser_ than I had been planning. The 145.7 wpm figure I was working from is the raw take, before the conform step adds breath and lands it in the slot. Episode 01 was made by generating, measuring, and **regenerating** until each block sat at 28–29.5 s. It was never one pass.

## Why punctuation cannot fix this one

Voice-02 articulates at about **165 wpm** raw. That is roughly 23 % faster than the narrator in the finished Episode 01 film. To fill 28.5 s of a 30 s slot at that rate you need **~64 words spoken slowly, or ~76 words at natural pace**.

The current blocks are 62–68 words and mostly read them at full speed. Converting every comma to a beat recovers about 3.5 s — it closes a 5-second gap, not a 6.5-second one. And on 24 of the 70 blocks there are not enough commas to convert at all (blocks 10, 15, 33, 35, 41, 49 have one or none).

A text-duration model fitted to the fifteen measured blocks reached R² = 0.33. **You cannot predict the length of a take from its word count.** The take has to be rendered and measured. That is how Episode 01 was built and it is how this must be built.

## The two honest options

**Option A — re-cut the script to Episode 01's density.**
Raise every block to 68–74 words and accept that the voice's natural pace fills the slot. Cost: rewriting most of 70 blocks, which puts the story back through the surgery that has duplicated blocks five times. It also makes the film denser and faster than the version you have been reading.

**Option B — re-record against the metronome, block by block.**
Keep the script exactly as written. For each block, render, measure, and regenerate with a heavier breath pattern until it lands between 28 and 29.5 s. This is what produced Episode 01 and it is proven. Cost: roughly two to four render attempts per block instead of one, so about 150–250 synthesis calls for the film, and it cannot be rushed into batches of ten.

Option B is the one I would defend. It preserves the writing, it reproduces the pacing you already approved on Episode 01, and it is measurable at every step.

## The third thing, which is not a pacing issue

Block 01 of this preview is the block whose voice you were asked to approve. Blocks 02–11 are the same narrator. **I still cannot confirm this is the Episode 01 narrator**, because Ep01's voice ID did not survive into this session and the 97 raw takes on disk carry no speaker fingerprint I can compare against. If the two films are meant to sound like one channel, that has to be settled before 70 blocks are recorded, not after.

## Also fixed this turn

The script source was hiding two defects that would have gone out on the recording:

- The block parser was swallowing the `## Chapter II` heading into the end of block 10. Any narration generated from the derived JSON would have spoken the words _"Chapter II, the wrong tool for the sky"_ out loud.
- Five of the seven chapter headings had been lost from the source entirely — only I and II existed. Chapters III–VII are now restored at their correct boundaries (blocks 21, 31, 42, 52, 62).

All derived artefacts now build through one parser, `scripts/episode-audit/ep002_blocks.py`, which refuses to emit a block containing a heading. Script is 70 blocks, 4,672 words, 7 chapters, zero duplicate pairs.
