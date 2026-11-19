# 68 of 70 blocks conformed — and the thing that is actually going on

## Built

**68 blocks**, every one exactly 1,440,000 mono samples at 48 kHz. Blocks 69 and 70 remain (this turn's generation cap).

Total speech in the current build: **1,894 seconds = 31.6 minutes** inside a 35-minute film.

|                     | Ep01 delivered | Ep02, blocks 1–68 |
| ------------------- | -------------- | ----------------- |
| Mean speech in slot | 28.72 s        | **27.9 s**        |
| Mean silence        | 1.28 s         | **2.1 s**         |

## What this batch exposed

Blocks 59–68 came in badly: mean raw length **22.05 s** against 24.1–24.5 s for every earlier batch, mean articulation **179.8 wpm** against 166–170. Adjacent blocks in the same session, same script, same voice.

So the pattern is now clear across all seven batches:

| Batch     | Mean raw    | Mean articulation |
| --------- | ----------- | ----------------- |
| 1–11      | 23.38 s     | 166.0 wpm         |
| 12–21     | 23.92 s     | 170.4 wpm         |
| 22–31     | 24.26 s     | 166.7 wpm         |
| 32–41     | 23.88 s     | 169.2 wpm         |
| 42–48     | 24.54 s     | 165.9 wpm         |
| 49–58     | 24.09 s     | 168.8 wpm         |
| **59–68** | **22.05 s** | **179.8 wpm**     |

The engine has no stable output. It drifts, and it drifts hardest at the end of a long session.

## The hard limit this creates

0.84 is already the slowest tempo allowed. If the engine hands back a take of 20.1 s, the most that take can ever become is **23.9 s — a 6.1 s hole.** Playing it faster makes it shorter, not longer.

**Thirteen blocks are in that position and cannot be fixed by tempo:**

| Block  | Raw     | Best possible at 0.84 | Gap        |
| ------ | ------- | --------------------- | ---------- |
| 68     | 20.09 s | 23.92 s               | **6.08 s** |
| 62     | 20.30 s | 24.17 s               | 5.83 s     |
| 61     | 20.32 s | 24.19 s               | 5.81 s     |
| 66     | 20.64 s | 24.57 s               | 5.43 s     |
| 44     | 21.11 s | 25.13 s               | 4.87 s     |
| 64     | 21.45 s | 25.54 s               | 4.46 s     |
| 2      | 21.52 s | 25.62 s               | 4.38 s     |
| 49     | 21.58 s | 25.69 s               | 4.31 s     |
| 59     | 21.76 s | 25.90 s               | 4.10 s     |
| 15, 20 | 21.84 s | 26.00 s               | 4.00 s     |
| 10     | 22.13 s | 26.35 s               | 3.65 s     |
| 40     | 22.26 s | 26.50 s               | 3.50 s     |

Two of those (15 and 40) were already re-rendered once and came back shorter the second time, which is the same non-determinism hitting twice.

## The options, honestly

**A. Re-take the thirteen.** Each re-render is a fresh sample from the same erratic distribution. Empirically about half come back long enough — block 39 went from 19.17 s to 24.27 s on one retry, and 15 and 40 went the other way. So thirteen blocks probably needs 20–30 renders and would land maybe eight of them, leaving five still short.

**B. Hold the plate at assembly.** Blocks 61, 62, 66 and 68 are in the closing chapter, where the writing is deliberately slow and spare — a six-second hold on a single image before a hard cut is a legitimate documentary beat, not an error. On blocks 02 and 10, which are mid-flow, it is more of a compromise.

**C. Rewrite the thirteen blocks longer.** Adding 8–12 words to each would put them beyond the drift's reach. It costs 13 block rewrites and breaks the "script is locked" property, which has already caused five duplication bugs on this project.

**D. Accept a slightly faster film.** Set the floor at 0.80 instead of 0.84. That recovers about 0.8 s per block, not the 4–6 s needed. Not enough to matter.

## What I will do unless told otherwise

Re-take the four worst that sit in _mid-flow_ (44, 49, 2, 10) in the next batch, at the same time as recording 69 and 70. If they come back long, they improve; if not, they ship with a held plate. The closing-chapter holds (61, 62, 66, 68) I would leave alone deliberately — that is where a long still frame is an asset.

That gets the film to a defensible 70/70 without reopening the script, which is the failure mode that has cost the most time on this project so far.

## Files

- `audio/conformed/B001–B068_30s.mp3`
- `10_CONFORM_REPORT.json` — per-block raw, tempo, speech, gap
- `14_` — the 69/70 batch and the audio master, next.
