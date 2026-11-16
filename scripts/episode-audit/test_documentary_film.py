"""Structural/media tests, explicitly not visual or listening approval."""
import hashlib
import json
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria'
F = EP / 'documentary_film'


class Tags(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class DocumentaryTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((F / 'production/FILM_MANIFEST.json').read_text())

    def test_preserved_clock_and_identity(self):
        shots = self.manifest['shots']
        self.assertEqual(len(shots), 1050)
        self.assertEqual(len({s['scene_id'] for s in shots}), 1050)
        self.assertEqual(self.manifest['frame_count'], 63000)
        for i, shot in enumerate(shots):
            self.assertEqual((shot['index'], shot['start'], shot['duration']), (i + 1, i * 2, 2))
            self.assertEqual(shot['block'], f'B{i // 15 + 1:03d}')
            self.assertFalse(shot['final_approved'])

    def test_authored_html_windows(self):
        tags = Tags((F / 'index.html').read_text()).tags
        hosts = [a for _, a in tags if 'data-composition-src' in a]
        self.assertEqual(len(hosts), 70)
        self.assertTrue(any(a.get('data-duration') == '2100' for _, a in tags))
        for i, host in enumerate(hosts):
            self.assertEqual(float(host['data-start']), i * 30)
            self.assertEqual(float(host['data-duration']), 30)
            source = Tags((F / host['data-composition-src']).read_text()).tags
            plates = [a for _, a in source if 'plate' in a.get('class', '').split()]
            self.assertEqual(len(plates), 15)
            for j, plate in enumerate(plates):
                self.assertEqual(float(plate['data-start']), j * 2)
                self.assertEqual(float(plate['data-duration']), 2)

    def test_proxy_integrity_and_narration(self):
        self.assertEqual(self.manifest['missing_candidates'], 0)
        for shot in self.manifest['shots']:
            self.assertIsNotNone(shot['proxy'])
            self.assertEqual(hashlib.sha256((F / shot['proxy']).read_bytes()).hexdigest(), shot['proxy_sha256'])
        narration = json.loads((EP / 'story_film_35min/47_COMPLETE_35MIN_AUDIO_MANIFEST.json').read_text())
        self.assertEqual(hashlib.sha256((F / 'assets/audio/narration.mp3').read_bytes()).hexdigest(), narration['preview_mp3']['sha256'])

    def test_editorial_corrections_preserve_original_provenance(self):
        overrides = json.loads((F / 'production/EDITORIAL_OVERRIDES.json').read_text())
        for key, entry in overrides.items():
            shot = self.manifest['shots'][int(key) - 1]
            origin = shot['source_origin']
            self.assertEqual(origin['type'], 'ai_generated_editorial_correction')
            self.assertEqual(origin['replaces_candidate'], shot['source_candidate'])
            self.assertEqual(hashlib.sha256((F / entry['asset']).read_bytes()).hexdigest(), shot['source_sha256'])
            self.assertFalse(shot['final_approved'])

    def test_single_soundtrack_and_license_integrity(self):
        tags = Tags((F / 'index.html').read_text()).tags
        audio = [a for tag, a in tags if tag == 'audio']
        self.assertEqual(len(audio), 1, 'Do not double narration or legacy whooshes')
        self.assertEqual(audio[0]['src'], 'assets/audio/final-mix.mp3')
        report = json.loads((F / 'production/SOUND_MIX_REPORT.json').read_text())
        self.assertEqual(hashlib.sha256((F / audio[0]['src']).read_bytes()).hexdigest(), report['output_sha256'])
        register = json.loads((F / 'production/audio_licenses/ASSET_REGISTER.json').read_text())
        for asset in register['assets']:
            self.assertIn(asset['license'], ['CC-BY-4.0', 'CC0-1.0'])
            self.assertEqual(hashlib.sha256((F / asset['local_path']).read_bytes()).hexdigest(), asset['sha256'])
        self.assertIn('creativecommons.org/licenses/by/4.0/', (F / 'compositions/b069.html').read_text())

    def test_protected_baseline_and_holds(self):
        validation = json.loads((EP / 'story_film_35min/06_VALIDATION_REPORT.json').read_text())
        for path, checksum in validation['baseline_hashes_after'].items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), checksum)
        self.assertEqual(self.manifest['final_approved_images'], 0)
        self.assertEqual(self.manifest['narration_word_alignment'], 'BLOCK_WINDOWS_ONLY_NOT_WORD_LEVEL')


if __name__ == '__main__':
    unittest.main()
