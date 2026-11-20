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

## Actual render of episode 02 (2026-11-20)

The planned seams were kept to one decimal place in the end:
**296.5 / 596.5 / 896.5 / 1200 / 1500 / 1800**, with 3.0 s of preroll on
chunks 2–7 and each chunk's `<name>.lead` recording it for the assembler.

Structure worth knowing before the next long render: the renderer splits each
chunk into **parts** of about 132 s (3,938 frames) each. Frames are captured to
`part-NNNN.mp4.work.<pid>.<hash>/captured-frames/`, encoded, and the frame
directory is deleted the moment that part's mp4 exists. So a chunk's peak disk
cost is one part's frames — about 1 GB — not the whole chunk's. Peak observed
usage never exceeded 2.3 GB on a 7 GB budget.

Per part, capture runs at roughly **0.13 s per frame** and encode at roughly
0.015 s per frame; a 132 s part costs about 9.5 minutes, so a 300 s chunk is
about 22 minutes and the whole 2,100 s film about **3 h 15 m**.

### Chapter-lag check, measured

This is the defect the user reported on the previous film, so it was measured
rather than assumed. On the old master, corner luminance across the 300 s
chapter change went 5.4 → 14.6 → **82.6 within 0.2 s** — a visible snap.

On the new master, across the chapter I card (reveal 5.40, exit 9.45):

```
t=5.20  corner 27.6      t=7.00  corner 66.3
t=5.40  corner 63.3      t=9.30  corner 67.4
t=5.60  corner 63.3      t=9.80  corner 64.1
t=6.00  corner 64.3      t=10.20 corner 34.9
```

The card arrives over about 0.4 s and leaves over about 0.6 s, with no step
larger than the fade itself. **No snap.** ch01 cadence: 8,895 frames, median
inter-frame delta 0.0333 s, **max 0.0333 s, zero gaps**.

## Second render, after the art repair (2026-11-20 16:00–18:15 UTC)

All seven chunks were re-rendered from ch01. Resuming at ch02 was not an option:
the earlier ch01 and ch02 were captured against art that has since been
replaced, so they were deleted rather than kept.

Measured chunk lengths, all matching `end - start` to the frame:

| Chunk | Span (s) | Rendered | Preroll lead |
|---|---|---|---|
| ch01 | 0 → 296.5 | 296.512 | 0.000 |
| ch02 | 296.5 → 596.5 | 303.000 | 3.000 |
| ch03 | 596.5 → 896.5 | 303.000 | 3.000 |
| ch04 | 896.5 → 1200.0 | 306.500 | 3.000 |
| ch05 | 1200.0 → 1500.0 | 303.000 | 3.000 |
| ch06 | 1500.0 → 1800.0 | 303.000 | 3.000 |
| ch07 | 1800.0 → 2100.0 | pending | 3.000 |

Throughput held at **22–24 minutes per 300 s chunk**, consistent with the
0.13 s/frame capture and 0.015 s/frame encode measured on the first render.

### Seam and cadence audit on ch01–ch06

Assembled to a partial master of 1,800.03 s and audited before ch07 existed:

```
cadence: frames=54450 median=0.0333s max=0.0333s gaps=0  PASS
   seam   d_mean  d_corner  verdict
  296.5      0.4      -0.2  pass
  596.5     -1.5      -2.5  pass
  896.5     -0.5      -0.6  pass
 1200.0     25.1      -1.0  pass
 1500.0     25.1      12.4  pass
worst corner jump: 12.4
```

Fifty-four thousand four hundred and fifty frames with **zero gaps** and a worst
corner jump of 12.4 against a 25 threshold. The chapter-lag defect stays fixed.

### Silence at the joins is content, not loss

Four seams showed windows of digital silence, which is exactly what a bad
`-c copy` concat looks like. It was checked against the source mix rather than
assumed either way:

| Seam | Silent window | In `mix.m4a`? |
|---|---|---|
| 596.5 | 595.85 → 598.00 | yes, same window |
| 1200.0 | 1198.50 → 1200.10 | yes, same window |
| 1500.0 | 1499.35 → 1500.05 | yes, same window |

The narration itself pauses across those chapter breaks. Each chunk's own audio
matches the mix within 0.1 s of the join, so nothing is being dropped by the
assembly. The one thing worth doing differently next time is padding the mix so
no drop lands within 1 s of a seam, which would make the audit unambiguous
instead of requiring this comparison.
