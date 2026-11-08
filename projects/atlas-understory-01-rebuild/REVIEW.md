# REVIEW — Stage E notes for the human reviewer
## What this build is
A complete rebuild of Atlas Understory Video 01 ("The Lighthouse Ring Found in Alexandria's Sunken Palace") governed solely by 15_Hyperframes_Master_Command_v1. The previous build was rejected because production/instruction material had been treated as on-screen content; none of that material appears in this film. On screen: the story's reported facts, quoted source wording, measurements, source attributions, explicit inference labels, and IMAGE NOT VERIFIED disclosures where no verified image exists.

## How it was made (HyperFrames workflow)
1. Stage A: command document parsed (tools/parse_command.py -> data/command.json: 48 VO / 53 units / 98 shots). Master media probed; picture-basis decision recorded (INPUT_MANIFEST.md). Met 1978.93.29 plate acquired via Met IIIF.
2. Timing: actual narration alignment proven verbatim (TIMING_LOCK_REPORT.md); graphic windows re-timed by per-segment affine map; total 15,745 frames unchanged.
3. Stage B: 53 generated sub-compositions (tools/build_project.py) + root index.html; caption phrase-group proof rendered; determinism snapshot test passed.
4. Stage C/D: hf lint 0/0; hf check ok=true; 17 timestamp snapshot reviews; three defect fixes (arrow glyph, map crop, photo caption) regenerated and re-verified.
5. Stage F draft delivery: full render at 24fps/1 worker/950k -> renders/Atlas_Understory_01_The_Lighthouse_Ring_DRAFT_CONDITIONAL_1080p.mp4 (15,745 frames, -16.03 LUFS/TP -1.88, 94,182,339 bytes); SRT+VTT sidecars.
6. Verification pass (after full manual read of Appendix C S015-S098, H, I): shot-level panel/chip rhythm confirmed against Appendix C (panel on graphic shot, disclosure chip on plate shot; MG-037 panel-gap-panel; VX support-plate continuation) and snapshot-verified at 10.5/523/529/645s; panel-free share measured 46.80% vs Q05's 46.8720% plan. One fix: MG-045 closing qualifier now persists to the final frame instead of ending with narration. Film re-rendered with identical settings; QC_REPORT.md carries the details.

## Decision recorded (user, 2026-11-08)
Picture basis: KEEP the current muted supplied-master backdrop as delivered. No solid-background fallback rebuild and no Appendix E plate commission. The film rests as DRAFT_CONDITIONAL; remaining release gates are the human holds Q14 (historical/source independence), Q15 (oral-read signoff), Q16 (workprint/release status).

## What a reviewer should check first
- The picture basis: backdrop plates are the supplied master's generated illustrations, not the Appendix E plates. The film is labelled DRAFT_CONDITIONAL for exactly this reason; plate approval or replacement is the main open creative decision (decided 2026-11-08: keep).
- Chapter-heading placement at actual narration chapter starts (116.79 / 242.16 / 332.24 / 424.17 s).
- The "S01" prefix omission and five spacing-only copy fixes (OVERRIDE_LOG.md) — accept or ask for reverts; all are one-line generator changes.
- Whether the 28px label sizes (command spec 26-30px) read well on your display; the hf craft heuristic prefers larger, we kept the spec.

## Holds that keep this a draft (Appendix I)
Q14 historical/source independence, Q15 oral-read signoff, Q16 workprint/release status: HOLD. Q07 human visual verification of the Met plate vs DP-40309-001 also still owed. Nothing in this project is an approved final or public master.

## Release paperwork prepared for the human gates
- ORAL_READ_PACKET.md — Q15: all 48 narration segments at actual timestamps with pronunciation watch-items and a sign-off block (two confirm-first names: Antirhodos, Franck Goddio).
- SOURCE_INDEPENDENCE_NOTE.md — Q14: claim-by-claim independence summary from Appendix F, with the editor's three-way decision (accept / require corroboration / require text change).
- RELEASE_CHECKLIST.md — Q01–Q17 status, evidence pointers, remaining human actions, and the release procedure once Q14+Q15 clear.

## Rebuild / re-render
- Regenerate compositions: `python3 tools/build_project.py` (asserts caption text 48/48 while running tools/make_captions.py separately).
- Re-render: source the runtime env, then `hf render -o renders/<name>.mp4 -f 24 -w 1 --video-bitrate 950k` from this directory (delete renders/work-* first if a stale work dir exists).
