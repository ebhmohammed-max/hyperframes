# QC_REPORT — Atlas Understory Video 01 (Rebuild), DRAFT_CONDITIONAL
Output: renders/Atlas_Understory_01_The_Lighthouse_Ring_DRAFT_CONDITIONAL_1080p.mp4
Rendered: HyperFrames 0.9.2 CLI (`hf render -f 24 -w 1 --video-bitrate 950k`), exit 0.

## Container / stream probe (ffprobe, counted)
- Video: H.264, 1920x1080, r_frame_rate 24/1, nb_read_frames = 15745 (exact), duration 656.041667s.
- Audio: AAC 48 kHz stereo, duration 656.041s.
- File size: 94,182,339 bytes (under the 100 MB handling limit; video bitrate capped at 950k by design decision, logged in OVERRIDE_LOG context).

## Audio (ffmpeg loudnorm analysis on the rendered file)
- Integrated -16.03 LUFS, true peak -1.88 dB, LRA 3.50 — matches the supplied master track (audio passed through unchanged). Narration span 1.21-639.92s; music tail to ~653.1s; closing frames quiet.

## gates
- `hf lint`: ok=true, 0 errors, 0 warnings, 54 files.
- `hf check --json`: overall ok=true; lint/runtime/layout/motion/contrast/audio 0 errors; 48 craft text_below_floor warnings on 28px spec-sized labels (rationale in OVERRIDE_LOG.md #7).
- Determinism: repeated cold snapshot at 340.0s -> identical MD5 (09fad1051cba99cfbeb68a3798a7bbaa).

## Visual spot checks (snapshots + frames extracted from the rendered MP4)
Verified at 2.0 / 5.2 / 10.5 / 30 / 95 / 102 / 117.5 / 146 / 150 / 160 / 213 / 340 / 410 / 500 / 632 / 646 / 655.5 s:
- Title + first evidence panel hierarchy; chapter headings (MG-047 etc.) integrated with staggered chips.
- VX-001 three states incl. inline SVG arrow (no tofu; U+2192 avoided); VX-002 branches; VX-003 lanes; "≠" glyph renders in Inter Tight.
- MG-003 schematic map: coastline crop 28-34N/25-35E, Alexandria marker only, no findspot pin.
- MG-011/012/013 photo panels: Met 1978.93.29 plate, caption one line "The Met · 1978.93.29 · Public Domain".
- MG-016, MG-045 ending panel; quiet closing frames (646/655.5s) carry no graphics, no credits/end card.
- Caption proof render (proof/caption-proof.html -> renders/caption-proof.mp4, 13.458s): VO-C01-B01 phrase groups show one at a time inside the caption zone; sidecar SRT is the release caption format (see below).

## Captions
- tools/make_captions.py: 161 cues, span 1.208-639.917s, max 18.1 CPS, max line 42 chars, max 2 lines/cue; concatenated cue text reproduces Appendix A 48/48 segments verbatim (asserted in the generator).
- HF03_Atlas_Understory_01_captions.srt + .vtt (WebVTT converted from the same SRT).

## Q07 plate inspection (agent visual pass, 2026-11-08)
- Acquired file assets/photo/met-bulla-1978.93.29.jpg (1200x899, Met IIIF main-image for object 326457) visually inspected at full size: irregular brown un-baked clay sealing on the Met's light background, faint weathered curvilinear seal impressions across the upper surface, no figure legible enough to identify at this resolution. Consistent with the Met record (Bulla, Parthian, 2nd c. BC-1st c. AD, Shahr-i Qumis).
- Film behaviour: MG-011/012/013 show the photo flat and unannotated (no arrows, markers, or motif claims drawn on it); all interpretation is in adjacent text rows with "Possibly" qualifiers; credit shown as "The Met · 1978.93.29 · Public Domain" (full credit line preserved in INPUT_MANIFEST.md). Nothing was annotated from the image itself.
- Still owed for Q07 closure: human side-by-side against the DP-40309-001 original file. The acquired IIIF derivative is displayed at 470x318px (downscaled, never upscaled), so resolution is not a legibility risk at 1080p.

## Known accepted imperfections
- Long source-strip disclosure text can wrap to two lines inside the strip (seen at 632s); strip height absorbs it, no overlap with panels.
- The backdrop picture is the supplied master picture with non-Appendix-E generated plates; disclosure chips keep the film honest ("IMAGE NOT VERIFIED" where no verified image exists), and release stays DRAFT_CONDITIONAL.

## Shot-rhythm conformance (Appendix C, verified after full manual read of S015-S098)
- Every base unit follows its Appendix C shot pattern: dominant panel on the graphic shot, disclosure-only chip on the following BACKGROUND PLATE shot ("keep illustration disclosure visible"), panel hard-clear or 0.45s fade per the Appendix D boundary class out of the graphic shot. VX-001/002/003 continue over their SUPPORT PLATE shots (OVERRIDE_SUPPORT) with a second state.
- Snapshot-verified in the assembled film: 10.5s (MG-001 plate interval, chip only), 523s (MG-037 plate gap), 529s (MG-037 panel returns for C05-S003), 645s (MG-045 compact closing qualifier persisting over the final plate past narration end).
- Q05 dominance proxy under the backdrop basis: panel-free frames = 46.80% of 15,745 (plan target for plate share: 46.8720%). The residual delta is the affine audio re-time, not a layout change.
- One functional fix in this pass: the MG-045 compact qualifier previously ended with narration (639.92s); it now persists through C05-S020 to frame 15745 per Appendix B MG-045 ("carry a compact identity-unestablished qualifier into the final plate").
- Boundary census (62 CUT / 23 CROSSFADE / 12 GRAPHIC) governs plate edits in the Appendix E system; under the recorded picture-basis decision the picture is the supplied master's own edit, and boundary classes drive only panel exit behaviour. This remains part of the DRAFT_CONDITIONAL picture deviation.

## Appendix I gate mapping for this build
Q01-Q06/Q17: plan-checked (unchanged). Q07 (media existence): partially evidenced — Met plate acquired and identity-verified via Met API/IIIF; human visual check against DP-40309-001 still owed. Q08 (installed syntax): executed — lint/check clean on HF 0.9.2. Q09 (determinism): executed — identical hashes. Q10-Q13: executed for this draft (caption alignment proven 48/48 verbatim; audio measured; legibility spot-checked at 1080p; encoded output probed). Q14/Q15/Q16: HOLD (historical/source independence, oral-read signoff, release status) — output remains DRAFT_CONDITIONAL, not an approved/public master.
