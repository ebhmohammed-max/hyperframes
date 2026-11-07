# TIMING_LOCK_REPORT — how actual narration timing was established
## Claim
The draft MM:SS:FF timecodes in the Master Command are design-time estimates. This build's graphic windows and captions follow the ACTUAL narration timing of the supplied master audio.

## Evidence chain
1. Source audio: the AAC track of the supplied locked master (1920x1080, 24fps, 15745 frames, 656.041667s).
2. Prior alignment work (preserved from the rejected build's data, reused here only as timing data): 161 phrase-group cues spanning 1.208s -> 639.917s.
3. Verbatim verification performed in this rebuild: concatenating the cue texts reproduces Appendix A exactly for all 48/48 VO segments (tools/make_captions.py asserts this on every run; FAIL = build stops). This proves the cues are aligned to THIS audio, not another take.
4. Independent corroboration: 50ms RMS blocking on the master audio shows speech energy ending at 639.90s (music tail continues to ~653.1s), matching the last cue end 639.917s within one frame. Integrated audio: -16.02 LUFS, TP -1.89 dB, LRA 3.5.
5. Drift profile: actual narration begins 1.208s (draft 0.000s) and ends 16.17s earlier than the draft end (639.92 vs 656.04) - the draft schedule is uniformly slow-aspirational; a per-segment affine map (draft->actual per VO segment, linear within segment) re-times every graphic unit. Method: tools/build_project.py (seg_map). Total runtime and frame count unchanged.

## What was NOT used
- No ASR/Whisper (huggingface unreachable from this environment; also unnecessary given the verbatim text-match proof).
- Speech-boundary detectors (silencedetect/RMS edges) cannot resolve the 48 segment boundaries because the music bed fills pauses; they were used only to corroborate narration end. Boundary precision rests on the verbatim cue match (item 3).

## Segment windows used (actual seconds, from data/command.json via generator)
MG-001 1.21-13.62; MG-002 13.62-23.17; MG-003 23.17-33.00; MG-004 33.00-44.00; MG-005 44.00-53.00; MG-006 53.00-65.00; VX-001 65.00-95.00 (extended); MG-007 95.00-102.00; MG-008 102.00-115.00; MG-009 116.79-136.00; MG-010 136.00-143.00; MG-011 143.00-150.00; MG-012 150.00-158.00; MG-013 158.00-167.00; MG-014 167.00-176.00; MG-015 176.00-188.00; MG-016 188.00-204.00; MG-017 204.00-218.00; MG-018 218.00-229.00; MG-019 229.00-240.00; MG-020 242.16-252.00; MG-021 252.00-262.00; MG-022 262.00-273.00; MG-023 273.00-282.00; MG-024 282.00-289.00; MG-025 289.00-299.00; MG-026 299.00-310.00; MG-027 310.00-322.00; MG-028 322.00-331.00; MG-029 332.24-340.00; MG-030 340.00-352.00; MG-031 352.00-360.00; VX-002 360.00-366.00 (extended); MG-032 366.00-378.00; MG-033 378.00-387.00; MG-034 387.00-398.00; MG-035 398.00-412.00; MG-036 412.00-422.00; MG-037 424.17-433.00; MG-038 433.00-448.00; MG-039 448.00-462.00; MG-040 462.00-474.00; MG-041 474.00-486.00; MG-042 486.00-500.00; MG-043 500.00-518.00; MG-044 518.00-537.00; VX-003 537.00-561.00 (extended); MG-045 627.46-639.92.
(Chapter-heading units MG-047..MG-050 at 116.79/242.16/332.24/424.17s; MG-046 title 0-7.42s.)

## Verdict
Timing is locked to the actual narration by verbatim text proof. Status: LOCKED (audio), with Appendix I narration-performance acceptability (Q15) still HOLD for human signoff.
