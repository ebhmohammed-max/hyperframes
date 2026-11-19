# Correction, and the first 21 blocks built

## What I got wrong

In `09_PACING_DECISION.md` I wrote that 0.84 "speeds up" the audio. That was wrong, and I then acted on it wrongly, and it is worth writing down plainly so it does not survive as a fact in this project.

**`atempo` divides duration by the factor.** A factor below 1 makes the audio _longer_:

- `atempo=0.84` turns 23.20 s into 27.57 s — it **slows the narration down**
- `atempo=1.16` would turn it into 20 s — it speeds it up

The takes average **23.5 s** against a **30 s** slot, so they need to be _stretched_, and 0.84 is correct. It has been correct all along. What was wrong was my sentence describing it as a speed-up, and a brief moment in this session where I "fixed" the factor to 1.16 on the strength of that sentence. The 1.16 attempt was reverted within two commands and never produced a shipped file.

The practical effect of 0.84: **narration slows by 16 %, and every block fills its slot.**

## The one place uniform could not hold

Uniform 0.84 fails wherever a raw take is already longer than `0.84 × 29.5 = 24.8 s`, because stretching it further would overrun the slot. Exactly one block is in that position:

| Block | Raw     | Factor used | Speech  | Note                                  |
| ----- | ------- | ----------- | ------- | ------------------------------------- |
| 12    | 28.97 s | **0.982**   | 29.43 s | already long; gets only 1.8 % stretch |

That is a clamp forced by geometry, not per-block tuning. A take that is already nearly a full slot does not need help.

## State of the film

**21 of 70 blocks conformed and measured.** Each is exactly 1,440,000 mono samples at 48 kHz.

|                     | Ep01 delivered    | Ep02, blocks 1–21                     |
| ------------------- | ----------------- | ------------------------------------- |
| Mean speech in slot | 28.72 s           | **27.79 s**                           |
| Mean silence        | 1.28 s            | **2.22 s**                            |
| Tempo               | varying per block | **0.84 Uniform** (one block at 0.982) |

**Four blocks carry 3.5 s or more of silence: 02 (4.43 s), 10 (3.72 s), 15 (5.05 s), 20 (4.07 s).** The rest are between 0.56 s and 3.36 s, which is a normal documentary breath.

These four are not a defect to fix by re-rendering. In a 30-second block there are fifteen 2-second image cuts, and holding a plate for five seconds at the end of a block reads as a deliberate beat. That is an assembly decision, and it is recorded here so it does not get lost.

## Listen

`audio/conformed/EP002_OPENING_21_ON_CLOCK.mp3` — **10 min 30 s**, blocks 1 to 21 laid end to end on the film clock. That is Chapter I complete and Chapter II well under way, with every gap exactly as it will be heard in the finished film.

If this is right, blocks 22 to 70 follow in batches of ten and the film goes to image assembly.
