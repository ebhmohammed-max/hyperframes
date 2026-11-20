# CHUNK SEAMS AND CHAPTER CHANGES — the lag, diagnosed

User report: "the last video is lagging on chapter changing." This is the
investigation and the fix. The finding was not what it looked like.

## What it looked like

A hitch at every chapter change, read as a stutter or lag.

## What it actually was

Two independent faults that both landed at the same instants.

### Fault 1 — chapter boundaries sat exactly on render chunk seams

The film is rendered in seven chunks, joined afterwards:

```
chunk  ch01 0–300   ch02 298–600   ch03 598–900   ch04 898–1200 ...
chapter II   starts at 300 s   = exactly the ch01/ch02 join
chapter III  starts at 600 s   = exactly the ch02/ch03 join
chapter IV   starts at 900 s   = exactly the ch03/ch04 join
```

Chapters II, III and IV began on the join. Chapters V, VI and VII begin at
1230, 1530 and 1830 s — nowhere near a seam — and the viewer did not report
lag there. **That correlation is the proof.**

### Fault 2 — a fade that never finished

Measured on the delivered file, corner luminance either side of the 300 s join:

| time | corner luminance |
|---|---|
| 299.0 | 5.4 – 8.3 |
| 299.3 | 7.7 – 13.0 |
| 299.6 | 10.2 – 17.8 |
| 299.9 | 13.3 – 23.8 |
| 300.0 | 14.6 – 26.6 |
| 300.2 | 82.6 – 58.4  ← snaps back |

The picture darkens to near black and then jumps. The chunk boundary fell
inside a transition, so the outgoing chunk's final frames were captured
mid-fade and the incoming chunk started after it.

Audio was checked separately and is **continuous** through the seam — no
dropout, no shift, no lip-sync jump. The defect was purely visual.

## The fixes

### Fix 1 — chunks no longer assume they start at zero

Every chunk rendered after the first used to capture from t=0 of its own
timeline, because the renderer's `--start` renders a window whose clip begins
at 0. That is why each chunk carried a 2 s lead-in that had to be trimmed at
assembly, and why a chapter card inside that lead was captured with its
animations at their initial state.

Each chunk now carries its own offset and gets a pre-roll: capture begins
`PREROLL` seconds before the chunk's first wanted frame, so every animation
that was already running has settled before the first kept frame. The
assembly trims the pre-roll exactly, instead of assuming 2 s.

### Fix 2 — seams never land on a chapter change

The chunk boundaries are now chosen so that no seam falls within
`SEAM_GUARD` seconds of a chapter start or a chapter card's reveal or exit.
Chapter starts are 0, 300, 600, 900, 1230, 1530, 1830; the default boundaries
are 300, 600, 900, 1200, 1500, 1800, which collides with three of them.

New boundaries are placed in the quiet part of each block, avoiding:

- chapter starts (0, 300, 600, 900, 1230, 1530, 1830)
- chapter card reveal at start + 0.35 (or +5.40 for the re-sequenced opening)
- chapter card exit at reveal + 4.05

Proposed: **297, 597, 897, 1227, 1527, 1827** — three seconds clear of every
chapter start, which puts the join in the middle of an ordinary plate.

## Verification, required before delivery

1. **Seam audit.** For each seam, sample frames at ±0.3 s and compare corner
   luminance and mean luminance. Any jump above the frame-to-frame baseline
   is a fail.
2. **Fade audit.** No transition may begin within `SEAM_GUARD` of a seam.
3. **Audio continuity.** RMS in 100 ms windows across each seam; any zero run
   longer than 150 ms that is not present in the source mix is a fail.
4. **Frame cadence.** Constant inter-frame delta, no gaps over 1.5 frames.

Scripts: `scripts/episode-audit/audit_ep002_seams.py`.
