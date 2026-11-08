# SPEC — Atlas Understory Video 01 (Rebuild)
Governing document: 15_Hyperframes_Master_Command_v1 (Google Drive 1nIL2p9o_Cb4AqST3b3h55vi7BgQfdf2KPGcYFpy1uLM), HF-DIRECTOR-1.0.
Release status of every output of this project: DRAFT_CONDITIONAL (Appendix I holds remain open).

## Identity
- Episode: The Lighthouse Ring Found in Alexandria's Sunken Palace
- Series: Atlas Understory
- Canvas: 1920x1080, exactly 24 fps, exact frame count 15745 (00:10:56:01 draft end = frame start 15745, exclusive EOF).
- Word count claim: 1,427 (command count) / 1,426 (whitespace tokenisation of the Appendix A text as exported) - the 1-word delta is logged in OVERRIDE_LOG.md; nothing was rewritten to force the number.
- Structure: 48 VO segments, 5 chapters, 98 shot intervals, 97 boundaries (62 CUT / 23 CROSSFADE(12f) / 12 GRAPHIC).
- Inventory: 53 graphic units = MG-001..MG-045 + VX-001..VX-003 (extended) + MG-046..MG-050. MG-046 title integrated inside C01-S001 (no pre-roll). Chapter headings integrated only. MG-045 is the ending; no added runtime, credits, or end card.

## Approved script basis
Appendix A verbatim VO text (data/command.json: vo[], 48 segments, chapter + paragraph breaks). On-screen text = only the film's editorial content: story facts, quoted source wording, measurements, source attribution, explicit inference labels, and (where no verified image exists) an IMAGE NOT VERIFIED disclosure. No command/instruction text, edition labels, or mastering metadata appears on screen.

## Timing model (authoritative for this build)
The draft timecodes in the command are design timecodes. Actual narration timing was proven from the audio embedded in the supplied master media and is recorded in TIMING_LOCK_REPORT.md. Graphic unit windows follow the actual narration: each unit's draft window was mapped through the actual start times of its narration segment (per-segment affine map). Chapter headings sit at actual chapter starts. SRT/VTT sidecars are generated from the actual alignment (data/captions.json -> tools/make_captions.py), 161 cues, <=42 chars/line, <=2 lines, <=21 CPS.

## Design direction (sections 06/12/13)
Quiet museum-grade evidence atelier. Backdrop: supplied picture (royal-quarters frames only) dimmed and desaturated under panels; dark navy panels rgba(11,24,34,.90-.93), ivory text #F2EBDD, slate #92A0AC, amber #C49643 labels, teal #5E8B8F accents. Fonts: Inter Tight (UI/labels/body) + Spectral (pull-quotes) - self-hosted woff2 in assets/fonts. Photo plate: one approved Met bulla frame, 4%-padded frame, caption + separate credit line. Map (MG-003): schematic vector coastline crop, marker for Alexandria only, "Solid marker: charted point / Unmarked coast: no charted findspot pin" legend. Complex graphics VX-001/002/003: neutral flat line/dot construction, grey/tan/teal, never pie/score/needle/gauge and never desirability-weighted. Left rail at x=96; safe box x 96..1340 (photo 1520x842); max panel 1240x760.

## Approved / held media
- Picture basis: supplied locked-master picture reused as backdrop (Stage A decision recorded in INPUT_MANIFEST.md); its generated illustrative plates are NOT the Appendix E plates. DECISION (user, 2026-11-08): keep this basis as delivered - no solid-background rebuild, no Appendix E plate commission at this time. Release remains DRAFT_CONDITIONAL pending Appendix I Q14/Q15/Q16.
- Audio: supplied locked-master audio track used unchanged (encoded under HyperFrames audio policy); integrated loudness -16.0 LUFS, TP -1.9 dB (Stage A measurement).
- On-screen photograph: Met 1978.93.29 (object 326457, DP-40309-001, public domain, IIIF main-image 1200x899). Accession 1978.93.30 images from the earlier rejected build were removed and are not used.
- All other "objects" are textual/graphic reconstructions; nothing photoreal is presented as evidence.

## Deliverables
renders/Atlas_Understory_01_The_Lighthouse_Ring_DRAFT_CONDITIONAL_1080p.mp4 (bitrate-limited for <=100MB handling), HF03_Atlas_Understory_01_captions.srt + .vtt equivalents via ffprobe-validated SRT, proof/caption-proof.html, QC_REPORT.md, REVIEW.md, OVERRIDE_LOG.md, INPUT_MANIFEST.md, RUNTIME_CAPABILITY_REPORT.md, TIMING_LOCK_REPORT.md.

## Unresolved holds (Appendix I)
Q07-Q13 execution evidence partially gathered by this build (see QC_REPORT.md); Q14 historical/source independence, Q15 oral-read signoff, Q16 workprint/release status remain HOLD. No output of this project may be labelled APPROVED, FINAL, or PUBLIC MASTER.
