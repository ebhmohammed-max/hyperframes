# NK style samples — EP06 cold open (Nagapattinam, 1856)

Nine sample video styles cut from the EP06 Act 1 plates, built with the
[hyperframes](https://github.com/ebhmohammed-max/hyperframes) repo (CLI 0.8.223, HTML + GSAP
compositions rendered frame by frame to H.264 / AAC, 30 fps).

All of them use the same raw material so the styles can be compared like for like:

- **Pictures:** the EP06 Act 1 plates (`EP06_ACT1_PLATES_v4.zip`), upscaled to 2304×1286.
- **Voice:** the existing EP06 Act 1 narration (`EP06_ACT1_NARRATION_voice19.mp3`), first 52 s.
  No new speech was generated.
- **Words on screen:** the narration text, timed to the voice; card wording from `EP06_CARDS_v1.zip`.
- **Sound effects:** the hyperframes SFX set (Pixabay Content License).
- **No music.** There was no music source available in the build environment, so every sample is
  voice + effects only (08 is effects only).

## The videos (`videos/`)

| # | File | Style | Length | Frame | What is in it |
|---|------|-------|--------|-------|---------------|
| 01 | `NK_style_01_classic_documentary.mp4` | Classic documentary | 52.0 s | 1920×1080 | Slow Ken Burns moves, 0.8 s dissolves, hard cuts on the dig, lower-left place/year title, serif subtitles, vignette, fade out |
| 02 | `NK_style_02_cinematic_trailer.mp4` | Cinematic trailer | 52.0 s | 1920×1080 (2.39:1 bars) | Letterbox, bigger camera moves, dips to black, flash cuts, light leaks, camera jolt on the tool strike, full-screen word supers ("உலோகம்."), film grain, riser / impacts / whooshes |
| 03 | `NK_style_03_ola_manuscript.mp4` | OLA manuscript (NK Direction A) | 21.6 s | 1920×1080 | Palm-leaf page, double rule with vermilion corner ticks, running head, framed plate with wipes and dissolves, cream caption plate with the spoken word in vermilion |
| 04 | `NK_style_04_vertical_short.mp4` | Vertical short (Shorts / Reels) | 31.6 s | 1080×1920 | Hook line on the first frame, re-framed vertical crops that pan, flash cuts, jolt on the strike, word-by-word captions with the spoken word boxed, progress bar, effects on the cuts |
| 05 | `NK_style_05_vintage_film.mp4` | Vintage film | 21.6 s | 1920×1080 (4:3 gate) | Sepia orthochromatic grade, rounded gate, gate weave, flicker, scratches, dust, heavy grain, intertitle card, iris out |
| 06 | `NK_style_06_archive_board.mp4` | Archive board / case file | 31.6 s | 1920×1080 | Plates as pinned photo prints with typed labels, one camera travelling print to print, prints dropping in, red thread, ring on the strike, rubber stamp, label-strip captions |
| 07 | `NK_style_07_kinetic_type.mp4` | Kinetic typography | 21.6 s | 1920×1080 | The narration as large type, each word hitting on the frame it is spoken, plates as a dark blurred wash, sentence counter, progress rule |
| 08 | `NK_style_08_title_sequence.mp4` | Title sequence / teaser | 15.5 s | 1920×1080 | Question card, riser, all 17 plates in an accelerating cut (whips, zoom-throughs, hard cuts on impacts), flash, episode title card. No narration |
| 09 | `NK_style_09_split_triptych.mp4` | Split-screen triptych | 31.6 s | 1920×1080 | Three tall panels holding the last three shots; the newest rises in lit, the others fall to a dim duotone; marker over the live panel; captions underneath |

Sound on every file was levelled after the render to about −14 LUFS integrated, peak below −1.5 dB.

## Rebuilding (`source/NK_style_samples_source.zip`)

```
build.mjs            node build.mjs [01 02 …]  → regenerates styles/<slug>/
gen/lib.mjs          narration timing table, shot list, scene / index writers, transitions, SFX placement
gen/caps.mjs         caption builders (per sentence, per word) and film grain
gen/s01.mjs … s09    one generator per style
scripts/             prepare_assets.py (plates + narration cuts), make_textures.py (paper, board,
                     grain, sepia plates), finish.py (loudness pass)
shared/              plates, sepia plates, textures, fonts (OFL / Apache), audio, sfx, gsap
styles/<slug>/       the generated hyperframes projects (index.html + compositions/)
```

Inside a style folder `assets` is a link to `../../shared` (in the zip it is stored as a link; on
Windows copy `shared` into the style folder as `assets`). Then, with hyperframes installed:

```
cd styles/02-cinematic-trailer
npx hyperframes lint
npx hyperframes check
npx hyperframes render --quality looks --output out.mp4
```

Each style passed `hyperframes lint` (0 errors) and `hyperframes check` before rendering.

## Notes and limits

- These are style samples on one 52 s passage, not a finished episode. The longest runs 52 s.
- 30 fps (hyperframes default). The NK command document says 25 fps; add `--fps 25` to change it.
- One narrator (the existing EP06 voice), not the three-voice cast described in the command document.
- Tamil is set in Noto Serif Tamil, Anek Tamil, Hind Madurai, Tiro Tamil and Kavivanar; none of it is
  letter-spaced.
- Style 03 follows the NK "Direction A — OLA" palette and rules; the other styles deliberately do not,
  so that there is something to compare against.
