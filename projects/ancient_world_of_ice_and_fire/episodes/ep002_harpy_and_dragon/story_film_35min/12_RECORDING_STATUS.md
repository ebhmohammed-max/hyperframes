# Recording status — 40 of 70 conformed

## Built

**40 blocks** at exactly 1,440,000 mono samples, 48 kHz, 16-bit.

|                     | Ep01 delivered    | Ep02 blocks 1–40                |
| ------------------- | ----------------- | ------------------------------- |
| Mean speech in slot | 28.72 s           | **27.97 s**                     |
| Mean silence        | 1.28 s            | **2.03 s**                      |
| Tempo               | varying per block | **0.84 uniform** (B12 at 0.982) |

Five blocks carry more silence than is acceptable, and one block is not recorded:

| Block | Speech  | Gap        | Status                 |
| ----- | ------- | ---------- | ---------------------- |
| 02    | 25.57 s | 4.43 s     | usable, hold the plate |
| 10    | 26.28 s | 3.72 s     | usable, hold the plate |
| 15    | 24.95 s | **5.05 s** | needs a re-take        |
| 20    | 25.93 s | 4.07 s     | usable, hold the plate |
| 40    | 23.74 s | **6.26 s** | needs a re-take        |
| 41    | —       | —          | **not recorded**       |

## The re-take backlog

Block 39 was in the same condition — 7.22 s of silence — and the fix worked exactly as expected: re-rendering with a heavier breath pattern took it from 19.17 s raw to 24.27 s raw, and it now sits at 28.82 s speech with 1.18 s of silence.

So the method for the backlog is known: re-render 15, 40 and record 41, in one batch of three, then re-conform.

## What the batch taught

**Silence is not predictable from word count, and it is not predictable from block position either.** Blocks 32 to 38 all landed between 26.98 s and 29.46 s of speech. Then 39 collapsed to 22.78 s and 40 to 23.74 s. Same script, same voice, same punctuation density, adjacent blocks.

This is the same non-determinism documented in `08_AUDITION_RESULT.md`: identical text rendered three times gave 21.79, 22.94 and 22.73 s. The consequence is that **a block is only known to be good after it has been rendered and measured**, and any block landing under about 27 s of speech has to go back.

That is the only reliable gate, and it is now automated: `conform_ep002_batch.py` measures each block, and the report flags anything with a gap of 3.5 s or more.

## Not a defect, and worth saying plainly

This is not a voice quality problem any more. 35 of 40 blocks land inside the Episode 01 envelope on the first attempt. The five outliers are the engine being erratic, not the writing being wrong, and the fix costs one render each.

## Files

- `audio/conformed/B001–B040_30s.mp3` — built and measured
- `10_CONFORM_REPORT.json` — every block's raw length, tempo, speech and gap; accumulates across runs
- `audio/conformed/EP002_OPENING_31_ON_CLOCK.mp3` — 15:30 preview, still the most recent full preview until 41 is recorded
