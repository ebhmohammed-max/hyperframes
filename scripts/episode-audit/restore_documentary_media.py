"""Verify/restore indexed documentary ZIPs without overwriting differing files."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
F = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/documentary_film'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-only', action='store_true')
    parser.add_argument('archives', nargs='+', type=Path)
    args = parser.parse_args()
    index = json.loads((F / 'production/MEDIA_STORAGE_INDEX.json').read_text())
    verified = 0
    for path in args.archives:
        raw = path.read_bytes()
        checksum = hashlib.md5(raw).hexdigest()
        matches = [row for row in index['archives'] if row['md5'] == checksum]
        assert len(matches) == 1, f'Unknown archive: {path}'
        row = matches[0]
        assert row['upload_verified'] and len(raw) == row['bytes']
        allowed = {item['path']: item for item in row['files']}
        with zipfile.ZipFile(path) as archive:
            names = archive.namelist()
            assert len(names) == len(set(names)) and set(names) == set(allowed)
            for name in names:
                relative = Path(name)
                assert not relative.is_absolute() and '..' not in relative.parts
                destination = (ROOT / relative).resolve()
                assert destination.is_relative_to(F.resolve())
                data = archive.read(name)
                item = allowed[name]
                assert len(data) == item['bytes']
                assert hashlib.sha256(data).hexdigest() == item['sha256']
                if destination.exists():
                    assert hashlib.sha256(destination.read_bytes()).hexdigest() == item['sha256'], destination
                elif not args.verify_only:
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(data)
                verified += 1
    print(f'{verified}indexed media entries verified; restore enabled:{not args.verify_only}')


if __name__ == '__main__':
    main()
