# INPUT_MANIFEST — Stage A intake
## Governing input
- 15_Hyperframes_Master_Command_v1 (Google Doc 1nIL2p9o_Cb4AqST3b3h55vi7BgQfdf2KPGcYFpy1uLM), exported to google_drive/15_Hyperframes_Master_Command_v1 (262,675 bytes, 1,980 lines). Sole creative authority. Appendices A-D machine-parsed to data/command.json (tools/parse_command.py): 48 VO segments, 53 graphic units, 98 shots, 97 boundaries (62 CUT / 23 CROSSFADE(12f) / 12 GRAPHIC), chapters C01..C05.

## Production inputs (data only - never on-screen instruction)
- Supplied locked master media (Drive 1DHxtoMn6HBBXwFHUNc9iW_wIVrs3e4OQ): 1920x1080, exactly 24fps, 15745 frames, 656.041667s, H.264 + AAC 48kHz. Copied to assets/video/master.mp4. Uses: (a) picture backdrop (royal-quarters frames), (b) the narration+music audio track, unchanged. Stage A decision: picture reused as backdrop basis with DRAFT_CONDITIONAL status because its generated illustrative plates do not conform to Appendix E (photoreal invented signet at ~330s, diver/ruins scenes). Recorded in SPEC.md and OVERRIDE_LOG.md #3.
- Met bulla photograph: Met object 326457, accession 1978.93.29, DP-40309-001, public domain. Acquired as Met IIIF main-image (1200x899, SHA-256 prefix 5a52b7de4563e25b) -> assets/photo/met-bulla-1978.93.29.jpg. The earlier build's 1978.93.30 images were identified as the wrong accession and excluded.
- Fonts: Inter Tight 400/500/600 + Spectral 300/300i/400 woff2 (self-hosted, assets/fonts), carried from the verified project assets. No CDN fonts.
- Geo data: assets/geo/map-paths.json (vector coastline paths, graticule, charted points Alexandria [390.4,325.1] / Quseir [902.4,205.6]); used only for the MG-003 schematic crop (28-34N / 25-35E).
- GSAP: assets/gsap.min.js (local copy; paused timelines registered in window.__timelines per HyperFrames 0.9.2 contract).

## Excluded inputs
- All briefs, shot-map spreadsheets, and support documents other than the Master Command (inputs only; their instruction text never appears on screen).
- The rejected build's compositions and its HF00-HF06 deliverables (Drive folder 1VFmAX1U7nAh6s-avn3zOsGk-7KvEPX6i) - retained on Drive as rejected history only.
- Wrong-accession photo assets (1978.93.30).

## Toolchain
HyperFrames CLI 0.9.2 (/tmp/hf5/hf), Node v22.22.3, Chromium+Sparticuz/SwiftShader in /tmp, ffmpeg/ffprobe from the HyperFrames runtime. Project scaffolding follows the verified 0.9.2 pattern (full-HTML sub-compositions via data-composition-src; muted <video> + <audio data-audio-group="mix">).
