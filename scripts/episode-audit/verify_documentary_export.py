#!/usr/bin/env python3
"""Verify a completed 35-minute export, optionally waiting for its renderer PID.

Wait uses a Linux pidfd (no polling). Technical results are not subjective
listening, lore validation, complete semantic review or legal clearance.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import select
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/documentary_film'


def inspect_export(path, ffmpeg, ffprobe):
    raw = subprocess.run([ffprobe, '-v', 'error', '-count_frames', '-show_streams',
                          '-show_format', '-of', 'json', str(path)],
                         check=True, capture_output=True, text=True)
    metadata = json.loads(raw.stdout)
    videos = [s for s in metadata['streams'] if s['codec_type'] == 'video']
    audios = [s for s in metadata['streams'] if s['codec_type'] == 'audio']
    checks = {'one_video_stream': len(videos) == 1, 'one_audio_stream': len(audios) == 1}
    if len(videos) == 1:
        v = videos[0]
        checks.update(full_hd=(v['width'], v['height']) == (1920, 1080),
                      frames_63000=int(v.get('nb_read_frames', 0)) == 63000,
                      fps_30=v['avg_frame_rate'] == '30/1')
    checks['duration_2100_seconds'] = abs(float(metadata['format']['duration']) - 2100) < 0.1
    decode = subprocess.run([ffmpeg, '-v', 'error', '-xerror', '-i', str(path), '-f', 'null', '-'],
                            capture_output=True, text=True)
    checks['full_decode'] = decode.returncode == 0 and not decode.stderr.strip()
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            digest.update(chunk)
    return {'file': str(path.relative_to(ROOT)), 'bytes': path.stat().st_size,
            'sha256': digest.hexdigest(), 'checks': checks, 'technical_pass': all(checks.values()),
            'metadata': metadata, 'decode_errors': decode.stderr[-5000:],
            'subjective_listening_approval': 'PENDING',
            'complete_word_image_alignment': 'PENDING',
            'publication_rights_clearance': 'NOT_ESTABLISHED_BY_TECHNICAL_QA'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--wait-pid', type=int)
    parser.add_argument('--file', type=Path, default=ROOT / 'renders/EP001_RISE_OF_OLD_VALYRIA_35MIN_REVIEW_MASTER_v01.mp4')
    args = parser.parse_args()
    if args.wait_pid:
        try:
            pidfd = os.pidfd_open(args.wait_pid)
        except ProcessLookupError:
            pass  # It already exited; inspect the expected output, not a new job.
        else:
            print(f'Waiting for renderer PID {args.wait_pid} to exit.', flush=True)
            try:
                select.select([pidfd], [], [])
            finally:
                os.close(pidfd)
    path = args.file.resolve()
    if not path.is_file():
        report = {'technical_pass': False, 'error': 'Expected completed output is missing. Renderer may have failed.', 'file': str(path)}
    else:
        try:
            report = inspect_export(path, os.environ.get('FFMPEG', 'ffmpeg'), os.environ.get('FFPROBE', 'ffprobe'))
        except (subprocess.CalledProcessError, ValueError, KeyError) as exc:
            report = {'technical_pass': False, 'error': str(exc), 'file': str(path)}
    (D / 'production/FULL_EXPORT_QC.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2), flush=True)
    return 0 if report['technical_pass'] else 1


if __name__ == '__main__':
    sys.exit(main())
