# RELEASE_CHECKLIST — Appendix I gates, evidence, and the exact remaining actions
Film: Atlas_Understory_01_The_Lighthouse_Ring_DRAFT_CONDITIONAL_1080p.mp4 (Drive 1noVJNGfCKQ8oCyaS-JVmBeP8yWezRWFb). Status today: DRAFT_CONDITIONAL workprint. Nothing may be labelled APPROVED/FINAL/PUBLIC MASTER until Q14–Q16 clear.

| Gate | Target | Status | Evidence | Remaining human action |
|---|---|---|---|---|
| Q01 Source identity | 1,427 words / 48 VO / 98 shots / 5 chapters | PLAN CHECKED (1,426 by whitespace count; delta logged, OVERRIDE_LOG #1) | data/command.json; SPEC.md | None |
| Q02 Frame coverage | Frames 0–15745, 98 adjacent intervals | PLAN CHECKED + render counted 15,745 | QC_REPORT.md (ffprobe census) | None |
| Q03 Graphics inventory | 48 base + 5 headings = 53 units | EXECUTED | 53 compositions; hf lint 0/0 | None |
| Q04 Image inventory | 31 baseline asset rows | DEVIATES BY DECISION (picture basis kept 2026-11-08; only sourced photo = Met bulla) | INPUT_MANIFEST.md; SPEC.md | None unless basis is reopened |
| Q05 Dominant share | Plate 46.8720% | MEASURED 46.80% panel-free under backdrop basis | QC_REPORT.md shot-rhythm section | None |
| Q06 Boundaries | 62 CUT / 23 CROSSFADE / 12 GRAPHIC | Plan-checked; classes drive panel exits only under backdrop basis | QC_REPORT.md | None |
| Q07 Media existence/approvals | Actual paths, licences, approvals | PARTIAL: Met plate acquired via Met IIIF, identity via API record S12 | INPUT_MANIFEST.md | Human visual check of the plate against DP-40309-001 original |
| Q08 Installed syntax | Verified version/flags | EXECUTED (HyperFrames 0.9.2) | RUNTIME_CAPABILITY_REPORT.md | None |
| Q09 Determinism | Cold/repeat same-time parity | EXECUTED (identical MD5 at 340.0s, twice, incl. after final patch) | QC_REPORT.md | None |
| Q10 Captions | Real VO alignment, one group, hard kills | EXECUTED (48/48 verbatim; 161 cues; SRT+VTT) | TIMING_LOCK_REPORT.md; caption proof render | None |
| Q11 Audio mix | Measured LUFS/TP, speech-first | EXECUTED (−16.03 LUFS, TP −1.88, supplied track unchanged) | QC_REPORT.md | Listening approval folds into Q15 |
| Q12 Legibility | 1080p checks, no collisions | EXECUTED (17 snapshot points + encoded-frame grabs) | QC_REPORT.md | Optional small-screen pass by reviewer |
| Q13 Encoded output | Codec/duration/critical windows | EXECUTED (H.264 1920×1080 24fps, 656.041667s) | QC_REPORT.md | None |
| Q14 Historical/source independence | No conflation of relayed announcement with field check | **HOLD — HUMAN EDITORIAL** | SOURCE_INDEPENDENCE_NOTE.md | Editor decision (a)/(b)/(c) in the note |
| Q15 Oral-read signoff | Approved narration/pronunciation review | **HOLD — HUMAN EDITORIAL** | ORAL_READ_PACKET.md (48 timed segments, priority pronunciations) | One full listen; sign the packet (Antirhodos + Franck Goddio are confirm-first items) |
| Q16 Workprint/release status | Conditional until factual/rights/VO checks clear | **HOLD — RELEASE** | This checklist | Release decision after Q14+Q15 |
| Q17 No unauthorized activity | No generation/purchase/publish/sharing changes | PLAN SCOPE CHECKED (none performed) | — | None |

## Release procedure (only after Q14 and Q15 clear)
1. Record both decisions in this file and QC_REPORT.md; update Q16 to CLEARED with date/name.
2. Rename deliverables without DRAFT_CONDITIONAL; re-export captions under final names; upload as the release set (keep the draft set in Drive history).
3. Re-run hf lint/check + spot snapshots on the final file (no picture change expected; this is a labelling operation unless Q14 chose option (c), which requires a command-level revision and re-render).
Release approved by: ______________  Date: __________
