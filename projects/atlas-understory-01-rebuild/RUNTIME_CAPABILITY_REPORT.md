# RUNTIME_CAPABILITY_REPORT — Stage A.3/A.4 evidence
Date: 2026-11-07. Environment: sandbox Linux, Node v22.22.3, HyperFrames CLI 0.9.2 (invoke as /tmp/hf5/hf), Chromium (Sparticuz brotli bundle + SwiftShader libs in /tmp), ffmpeg/ffprobe from HyperFrames runtime (/tmp/hf5).

## Verified version
- `hf --version` -> hyperframes@0.9.2. package.json dependency recorded as hyperframes@0.9.2.

## gates executed on this project
- `hf lint` -> ok=true, 0 errors, 0 warnings, 54 files checked (53 unit sub-compositions + root). Rules exercised: root_composition_missing, composition_file_too_large, gsap_duplicate_target, gsap_overlap_detected, gsap_stagger_children, gsap_target_overlap, var_reference_undefined, composition_self_attribute_selector, root_composition_structure, composition_syntax_attributes, composition_duplicate_ids, etc.
- `hf check --json` (Chromium screenshot + inspect) -> overall ok=true: runtime errors 0, layout errors 0, motion errors 0, contrast errors 0, audio errors 0. Residual: 48 craft text_below_floor warnings on panel meta text (28px, within the command's 26-30px badge spec; heuristic floor differs - rationale logged in OVERRIDE_LOG.md). No text was enlarged to satisfy the heuristic.

## Determinism test (section 16)
Same timestamp (340.0s) snapshot twice from cold seeks -> identical MD5 (09fad1051cba99cfbeb68a3798a7bbaa). Snapshot extraction is deterministic at frame level.

## Audio capability (section 17 acceptance)
- Master audio track probed: AAC 48kHz stereo, -16.02 LUFS integrated, TP -1.89 dB, LRA 3.5 (ffmpeg loudnorm analysis on the supplied master; the same track is encoded unchanged by HyperFrames' audio policy).
- Render audio policy observed: full-resolution AAC passthrough path of HyperFrames 0.9.2; no loudness re-targeting applied by this project.

## Render settings applied
-f 24 (exact), -w 1, --video-bitrate 950k (chosen to keep the 10:56 master under the 100 MB handling limit observed for this workflow), output H.264 + AAC in MP4.

## Unsupported-operation findings
None encountered: sub-composition mounting (data-composition-src), paused GSAP timelines under window.__timelines, muted <video> + separate <audio data-audio-group="mix">, caption phrase groups, and snap-at-time extraction all behave as documented for 0.9.2 in this build.
