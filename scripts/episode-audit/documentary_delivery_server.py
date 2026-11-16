#!/usr/bin/env python3
"""Read-only render progress and QA-gated, full-quality master download.
No authentication tokens, arbitrary paths, file writes or public sharing changes.
"""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import mimetypes
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
D = ROOT / 'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/documentary_film'
MASTER = ROOT / 'renders/EP001_RISE_OF_OLD_VALYRIA_35MIN_REVIEW_MASTER_v01.mp4'
LOG = ROOT / '.cache/film-full-render.log'
PAGE = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Rise of Old Valyria — export</title>
<style>*{box-sizing:border-box}body{margin:0;background:#10100f;color:#ede5d7;font:17px/1.6 system-ui,sans-serif}main{max-width:880px;margin:10vh auto;padding:36px}small{letter-spacing:.18em;color:#c6aa77;text-transform:uppercase}h1{font:clamp(38px,7vw,70px)/1.1 Georgia,serif;font-weight:400;margin:25px 0}p{color:#bcb7ac}.bar{background:#30302a;height:5px;margin:34px 0 14px}.bar>div{height:100%;background:#c6aa77;transition:width 1s}#count{font-variant-numeric:tabular-nums}section{padding:24px 0;border-top:1px solid #34332d;margin-top:32px}a{display:inline-block;padding:12px 20px;background:#c6aa77;color:#10100f;text-decoration:none;margin:8px 12px 8px 0}a.secondary{background:none;border:1px solid #766448;color:#d5bd91}#state{color:#e8d5af}.note{font-size:14px;color:#aaa496}video{max-width:100%;margin-top:20px}</style>
<main><small>Ancient World of Ice and Fire / Episode 01</small><h1>Rise of Old Valyria</h1><p>35-minute review master · 1920 × 1080 · 30 fps<br>1,050 ordered image slots · selected narration voice-01</p><div class="bar"><div id="bar" style="width:0"></div></div><div id="count">Connecting to render status…</div><p id="state" role="status"></p><div id="ready" hidden><a href="/master.mp4?download=1">Download full-quality master</a><a class="secondary" href="/master.mp4" target="_blank" rel="noopener">Play master</a></div><section><small>Soundtrack</small><p>Licensed music and CC0 sound effects are mixed with narration. Music and SFX credits appear in the film.</p><a class="secondary" href="/credits.txt">Publication audio credits</a><p class="note">The export is not complete until all 63,000 frames are rendered, audio is muxed, and full-file checks pass. Progress below is captured-frame progress, not the renderer's weighted stage percentage.</p></section><p class="note">A successful technical check does not certify subjective listening approval, every word-to-image match, lore accuracy, or all publication rights. Drive delivery is pending: a resumable session was created, but direct PUT failed TLS from this sandbox. This page offers the unchanged master, not a compressed substitute.</p></main>
<script>async function update(){try{const r=await fetch('/status',{cache:'no-store'});const s=await r.json();document.getElementById('bar').style.width=(s.frames/63000*100)+'%';document.getElementById('count').textContent=s.frames.toLocaleString()+' / 63,000 frames captured ('+(s.frames/63000*100).toFixed(1)+'%)';document.getElementById('state').textContent=s.message;document.getElementById('ready').hidden=!s.ready;}catch(e){document.getElementById('state').textContent='Status connection interrupted. Retrying…';}}update();setInterval(update,10000);</script></html>'''


def status():
    tail = ''
    if LOG.exists():
        with LOG.open('rb') as stream:
            stream.seek(max(0, LOG.stat().st_size - 150000))
            tail = stream.read().decode('utf-8', errors='replace')
    frames = re.findall(r'"done":(\d+),"total":63000', tail)
    count = int(frames[-1]) if frames else 0
    qc_path = D / 'production/FULL_EXPORT_QC.json'
    qc = json.loads(qc_path.read_text()) if qc_path.exists() else {}
    ready = bool(qc.get('technical_pass') and MASTER.is_file() and MASTER.stat().st_size == qc.get('bytes'))
    if ready:
        count = 63000
        message = 'Full export complete. Technical file checks passed; review approval remains pending.'
    elif qc and not qc.get('technical_pass'):
        message = 'Export verification failed. The master is not available as a completed deliverable.'
    elif count >= 63000:
        message = 'Capture complete. Encoding, audio mux and full-file verification are still pending.'
    else:
        checkpoint_path = D / 'production/CHECKPOINT.json'
        checkpoint = json.loads(checkpoint_path.read_text()) if checkpoint_path.exists() else {}
        if checkpoint.get('status') == 'PAUSED_FOR_STYLE_SAMPLER':
            message = 'Full film paused to prioritize the requested Old Valyria style sampler. Completed render segments are preserved.'
        else:
            message = 'Full-length render in progress. Download will unlock only after export verification.'
    return {'frames': count, 'ready': ready, 'message': message}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        route = self.path.split('?')[0]
        if route == '/':
            self.send_bytes(PAGE.encode(), 'text/html; charset=utf-8')
        elif route == '/status':
            self.send_bytes(json.dumps(status()).encode(), 'application/json')
        elif route == '/credits.txt':
            self.send_bytes((D / 'production/audio_licenses/YOUTUBE_AUDIO_CREDITS.txt').read_bytes(), 'text/plain; charset=utf-8')
        elif route == '/master.mp4' and status()['ready']:
            self.send_response(200)
            self.send_header('Content-Type', 'video/mp4')
            self.send_header('Content-Length', str(MASTER.stat().st_size))
            if 'download=1' in self.path:
                self.send_header('Content-Disposition', f'attachment; filename="{MASTER.name}"')
            self.end_headers()
            try:
                with MASTER.open('rb') as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b''):
                        self.wfile.write(chunk)
            except (BrokenPipeError, ConnectionResetError):
                pass
        else:
            self.send_error(404)

    def send_bytes(self, data, content_type):
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)


if __name__ == '__main__':
    print('Documentary progress and QA-gated download on port 3004', flush=True)
    ThreadingHTTPServer(('0.0.0.0', 3004), Handler).serve_forever()
