#!/usr/bin/env python3
"""Verify the rendered Old Valyria style sampler (720 s, 21600 frames).

Checks container/stream facts, frame count, duration, audio loudness/peak, a full
decode pass, and samples frames at chapter boundaries to confirm each chapter starts
on its own treatment. Writes production/EXPORT_QA.json. Usage:

    .venv/bin/python scripts/episode-audit/verify_valyria_sampler.py <video.mp4> [out.json]
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FFMPEG = ROOT / '.cache/bin/ffmpeg'
FFPROBE = ROOT / '.cache/bin/ffprobe'
SAMPLER = ROOT / 'projects/valyria_style_sampler'
EXPECTED_FRAMES = 21600
EXPECTED_SECONDS = 720.0
CHAPTERS = [0, 90, 180, 270, 360, 450, 540, 630]


def probe(path: Path) -> dict:
    out = subprocess.run(
        [str(FFPROBE), '-v', 'error', '-count_frames', '-show_streams', '-show_format',
         '-of', 'json', str(path)], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def run(cmd: list[str]) -> str:
    return subprocess.run(cmd, capture_output=True, text=True).stderr


def main() -> int:
    video = Path(sys.argv[1] if len(sys.argv) > 1 else
                 ROOT / 'renders/OLD_VALYRIA_STYLE_SAMPLER_12MIN_v01.mp4')
    video = video if video.is_absolute() else (ROOT / video)
    video = video.resolve()
    info = probe(video)
    video_stream = next(s for s in info['streams'] if s['codec_type'] == 'video')
    audio_stream = next((s for s in info['streams'] if s['codec_type'] == 'audio'), None)
    frames = int(video_stream.get('nb_read_frames') or 0)
    duration = float(info['format']['duration'])

    decode = run([str(FFMPEG), '-hide_banner', '-nostdin', '-v', 'error', '-i', str(video),
                  '-f', 'null', '-'])
    decode_errors = [l for l in decode.splitlines() if l.strip()][:10]

    loud = run([str(FFMPEG), '-hide_banner', '-nostdin', '-i', str(video),
                '-af', 'loudnorm=I=-16:TP=-1.5:print_format=json', '-f', 'null', '-'])
    measurement = {}
    if '{' in loud:
        try:
            measurement = json.loads(loud[loud.rindex('{'):loud.rindex('}') + 1])
        except ValueError:
            measurement = {}

    # Chapter-boundary stills (2 s into each chapter) to confirm treatment identity.
    stills_dir = ROOT / '.cache/valyria-sampler-final-stills'
    stills_dir.mkdir(parents=True, exist_ok=True)
    stills = []
    for i, start in enumerate(CHAPTERS, 1):
        target = stills_dir / f'chapter{i:02d}-at-{start + 2}s.png'
        subprocess.run([str(FFMPEG), '-hide_banner', '-nostdin', '-v', 'error', '-y',
                        '-ss', str(start + 2), '-i', str(video), '-frames:v', '1',
                        str(target)], check=True)
        stills.append(str(target.relative_to(ROOT)))

    report = {
        'video': str(video.relative_to(ROOT)),
        'bytes': video.stat().st_size,
        'sha256': subprocess.run(['sha256sum', str(video)], capture_output=True,
                                 text=True).stdout.split()[0],
        'duration_seconds': round(duration, 3),
        'frames': frames,
        'expected_frames': EXPECTED_FRAMES,
        'fps': video_stream.get('r_frame_rate'),
        'resolution': f"{video_stream.get('width')}x{video_stream.get('height')}",
        'video_codec': video_stream.get('codec_name'),
        'pix_fmt': video_stream.get('pix_fmt'),
        'audio_codec': (audio_stream or {}).get('codec_name'),
        'audio_rate': (audio_stream or {}).get('sample_rate'),
        'audio_channels': (audio_stream or {}).get('channels'),
        'decode_errors': decode_errors,
        'loudness': {k: measurement.get(k) for k in
                     ('input_i', 'input_tp', 'input_lra', 'input_thresh')},
        'chapter_stills': stills,
        'checks': {
            'frame_count': frames == EXPECTED_FRAMES,
            'duration': abs(duration - EXPECTED_SECONDS) < 0.5,
            'resolution': f"{video_stream.get('width')}x{video_stream.get('height')}" == '1920x1080',
            'has_audio': audio_stream is not None,
            'decode_clean': not decode_errors,
        },
        'status': 'PASS' if all([
            frames == EXPECTED_FRAMES,
            abs(duration - EXPECTED_SECONDS) < 0.5,
            audio_stream is not None,
            not decode_errors,
        ]) else 'REVIEW',
        'subjective_review': 'PENDING — technical checks are not viewing/listening approval',
    }
    out_name = sys.argv[2] if len(sys.argv) > 2 else 'EXPORT_QA.json'
    out = SAMPLER / 'production' / out_name
    out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('status', 'frames', 'duration_seconds', 'bytes',
                                             'loudness', 'checks')}, indent=2))
    return 0 if report['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
