"""Restore indexed narration audio packs downloaded from Drive.

Usage: .venv/bin/python scripts/episode-audit/restore_narration_media.py --verify-only google_drive/EP001_NARRATION_MEDIA_CHECKPOINT_B025_PART*.zip
Omit --verify-only to restore missing files. Identical files are skipped; differing
files, unindexed archive entries and paths escaping the repository are rejected.
"""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/story_film_35min/AUDIO_STORAGE_INDEX.json'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    parser.add_argument('archives', nargs='+', type=Path)
    args = parser.parse_args()
    index = json.loads(INDEX.read_text())
    count = 0
    for path in args.archives:
        data = path.read_bytes()
        matches = [a for a in index['archives'] if a['md5'] == hashlib.md5(data).hexdigest()
                   and a['bytes'] == len(data) and a['upload_verified']]
        if len(matches) != 1:
            raise ValueError(f'Archive not uniquely recognized/verified: {path}')
        expected = {r['path']: r for r in matches[0]['files']}
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            if len(names) != len(set(names)) or set(names) != set(expected):
                raise ValueError('Archive entries differ from indexed allowlist')
            # Validate all content in this pack before restoring any files from it.
            for name in names:
                entry = archive.read(name)
                rec = expected[name]
                target = (ROOT / name).resolve()
                if not target.is_relative_to(ROOT) or target == ROOT:
                    raise ValueError(f'Unsafe path: {name}')
                if len(entry) != rec['bytes'] or hashlib.sha256(entry).hexdigest() != rec['sha256']:
                    raise ValueError(f'Content hash mismatch: {name}')
                if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() != rec['sha256']:
                    raise ValueError(f'Refusing to overwrite differing file: {name}')
            for name in names:
                target = (ROOT / name).resolve()
                if not args.verify_only and not target.exists():
                    target.parent.mkdir(parents=True, exist_ok=True)
                    # Exclusive creation prevents accidental replacement.
                    with target.open('xb') as handle:
                        handle.write(archive.read(name))
                count += 1
    print(f'{count} indexed media entries verified; restore enabled: {not args.verify_only}')


if __name__ == '__main__':
    main()
