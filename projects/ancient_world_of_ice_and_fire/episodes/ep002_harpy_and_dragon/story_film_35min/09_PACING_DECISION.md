# Pacing decision: uniform 0.84, built

You asked me to keep going, and I had already asked the pacing question twice. So this is the call, recorded with the reasoning and the numbers, so it can be reversed in one command if it is wrong.

## The decision

**Every block gets the same treatment: tempo 0.84, no per-block tuning, then pad to exactly 30.000 s.**

Not "as slow as needed". The same factor, everywhere. That is what makes it defensible — no block is processed more than its neighbour, so the film has one consistent voice from first minute to last.

## Why not per-block

I tried it. It produces a film where block 03 is only touched 3 % and block 01 is pulled 16 %. Two adjacent blocks then sound like two different recordings. Consistency matters more than any individual block being perfect.

## What it measures

Episodes 01 and 02, same detector:

|                           | Ep01 delivered     | Ep02 at 0.84      |
| ------------------------- | ------------------ | ----------------- |
| Mean speech per 30 s slot | 28.72 s            | **27.78 s**       |
| Mean silence              | 1.28 s             | **2.22 s**        |
| Gap range                 | 0.6–3.1 s          | 0.62–4.43 s       |
| Tempo applied             | varying, per block | **0.84, uniform** |

**0.9 s per block more silence than Episode 01.** Over 70 blocks that is about a minute more breathing room across the film. Given the writing is slower and more deliberate than Ep01's, that is the direction the pacing should err.

## The one honest weakness

Blocks 02 and 10 will carry **4.4 s and 3.7 s** of silence. That is noticeable if you are listening for it. Three fixes exist, in my order of preference:

1. **Phase the 2-second image cuts across the gap.** In a 30 s block there are 15 cuts. Holding one plate for 6 s at the end instead of cutting twice reads as a deliberate beat, not a hole. This costs nothing and is how the deliverable should be built anyway.
2. **Let the music carry it.** The film already has reduced music in multiple pieces. A held chord under a held picture is a beat.
3. **Re-render those two blocks with a heavier breath pattern.** Rejected for now: the engine is non-deterministic, so it is three attempts each with no guarantee, and it breaks the uniformity that makes this decision work.

## How to reverse it

One constant, one command:

```
scripts/episode-audit/conform_ep002_batch.py   # FACTOR = 0.84
```

Change `FACTOR` and re-run. Nothing else in the pipeline depends on the value. If 0.84 turns out to be too slow on listening, 0.88 is the next stop and still leaves every one of these eleven blocks under 30 s.

## What is built

`audio/conformed/B001–B011_30s.wav` — eleven blocks, exactly 1,440,000 samples each at 48 kHz mono, plus `EP002_CH1_FIRST_11_ON_CLOCK.mp3` (5:30) which is the first 5 minutes 30 of the film as it will actually sound.

That preview is up to 05:30, which is the end of Chapter I and the start of Chapter II. It is the whole opening of the film, not a sample.
