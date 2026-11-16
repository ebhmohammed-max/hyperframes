#!/usr/bin/env bash
# After the corrected master render completes: verify it, build the delivery encodes,
# verify those, then print the final numbers for the Drive upload.
set -euo pipefail
cd /home/user/hyperframes
MASTER="renders/OLD_VALYRIA_STYLE_SAMPLER_12MIN_v04_master.mp4"
.venv/bin/python scripts/episode-audit/verify_valyria_sampler.py "$MASTER" EXPORT_QA_master.json
scripts/episode-audit/encode_valyria_sampler.sh "$MASTER" .cache/sampler-encode-final
.venv/bin/python scripts/episode-audit/verify_valyria_sampler.py renders/OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_1080p.mp4 EXPORT_QA_delivery.json
ls -l "$MASTER" renders/OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_1080p.mp4 renders/OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_720p.mp4
