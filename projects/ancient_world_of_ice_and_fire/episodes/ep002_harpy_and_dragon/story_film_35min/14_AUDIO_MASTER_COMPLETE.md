# Episode 02 narration master — complete

## Built

**70 of 70 blocks.** Every block exactly 1,440,000 mono samples at 48 kHz, 16-bit PCM.

**Master: `EP002_NARRATION_MASTER_35MIN.wav` — 2,100.000000 seconds exactly, 100,800,000 frames.**
MP3 delivery copy: 49 MB, 2,100.024 s container duration (codec delay only; the WAV is the timing authority).

**Uploaded to Drive:** `EP002_NARRATION_MASTER_35MIN.mp3`
https://drive.google.com/file/d/1DXPGFHLYMu8hKzuq_MN5CxIaz5x2Npaw/view

## The numbers against Episode 01

|                       | Ep01 delivered | Ep02                     |
| --------------------- | -------------- | ------------------------ |
| Blocks                | 70             | **70**                   |
| Speech in the film    | —              | **1,968.4 s = 32.8 min** |
| Mean speech per slot  | 28.72 s        | **28.12 s**              |
| Mean silence per slot | 1.28 s         | **1.88 s**               |
| Total film duration   | 2,100 s        | **2,100 s**              |

Silence segments longer than 2 seconds across the whole film: **35** — roughly one per two blocks, which is the breathing pattern a 35-minute voice-only documentary should have.

## How it was built

Every block rendered separately, decoded to PCM, slowed by a **uniform factor of 0.84** (`atempo`, pitch-preserving), then padded with digital silence to exactly 30.000 s. Uniform because per-block tuning leaves adjacent blocks sounding like different recordings; the one exception is block 12, whose take was already 28.97 s and could only take 0.982.

## What went wrong along the way, and what fixed it

The speech engine is **non-deterministic and drifts**. Seven batches, same script, same voice:

| Batch     | Mean raw    | Articulation  |
| --------- | ----------- | ------------- |
| 1–11      | 23.38 s     | 166.0 wpm     |
| 22–31     | 24.26 s     | 166.7 wpm     |
| 42–48     | 24.54 s     | 165.9 wpm     |
| **59–68** | **22.05 s** | **179.8 wpm** |

The last batch came back 2 seconds shorter and 11 wpm faster than the ones before it. That drift, not the writing, is what caused every pacing problem in this episode.

The repair is a re-take, and it works reliably: **all eight re-takes came back longer.** Block 68 went from a 6.08 s hole to 2.91 s, block 64 to 0.55 s, block 10 from 3.65 s to 1.12 s.

## The eight blocks that still carry a long hold

| Block | Gap    | Decision                     |
| ----- | ------ | ---------------------------- |
| 49    | 4.39 s | hold the plate               |
| 02    | 4.26 s | hold the plate               |
| 59    | 4.17 s | hold the plate               |
| 15    | 4.08 s | hold the plate               |
| 20    | 4.07 s | hold the plate               |
| 62    | 3.72 s | deliberate — closing chapter |
| 61    | 3.61 s | deliberate — closing chapter |
| 40    | 3.56 s | hold the plate               |

All eight sit between 3.5 and 4.4 s. In a 30-second block there are fifteen 2-second image slots; holding one plate across a 4-second gap instead of cutting twice reads as a deliberate beat. This is an assembly instruction, recorded here so it is not lost.

## Reproduce

```
scripts/episode-audit/build_ep002_script.py     # 70 blocks, 7 chapters, from one parser
scripts/episode-audit/conform_ep002_batch.py 1 2 3 ... 70   # uniform 0.84, pad to 30.000 s
```

Then concatenate the 70 WAVs in order. Every step is measured and reported; `10_CONFORM_REPORT.json` holds each block's raw length, factor, speech and gap.

## Disk

Local WAV masters and the 70 per-block WAVs were deleted after upload — they are reproducible from the MP3 takes in one command. `renders/segments_v2` (824 MB of Episode 01 chapter renders already concatenated into the delivered master) and three superseded sampler/part-one exports were also removed. Free space went from 263 MB to **1.8 GB**, which is what the image assembly will need.
