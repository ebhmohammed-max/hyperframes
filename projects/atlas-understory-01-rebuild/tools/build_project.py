#!/usr/bin/env python3
"""Generate the HyperFrames rebuild from data/command.json + actual-audio caption timings.
Implements HF-DIRECTOR-1.0: 53 graphic units, exact display copy, clean master (no burned captions)."""
import json, math, pathlib, re, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
FPS = 24
DUR_F = 15745

cmd = json.loads((ROOT / 'data' / 'command.json').read_text())
oldcaps = json.loads((ROOT.parent / 'atlas-understory-01' / 'data' / 'captions.json').read_text())
VO = {v['id']: v for v in cmd['vo']}
UNITS = {u['id']: u for u in cmd['units']}
SHOTS = {s['id']: s for s in cmd['shots']}
BOUNDS = {b['frame']: b for b in cmd['boundaries']}

OVERRIDE_SUPPORT = {'C01-S016', 'C03-S014', 'C04-S004'}  # diagram-dominant support intervals (sec.11)

# ---------- actual speech spans from verified caption cues ----------
from collections import defaultdict
byseg = defaultdict(list)
for c in oldcaps['cues']:
    byseg[c['segment']].append(c)
ACT = {}
for vid, cs in byseg.items():
    ACT[vid] = (cs[0]['start_s'] * FPS, cs[-1]['out_s'] * FPS)

def amap(vid, draft_f):
    """Affine map draft frame -> actual frame using the segment's measured speech span."""
    v = VO[vid]
    a0, a1 = ACT[vid]
    d0, d1 = v['start_f'], v['end_f']
    return a0 + (draft_f - d0) * (a1 - a0) / (d1 - d0)

timing = []
for v in cmd['vo']:
    a0, a1 = ACT[v['id']]
    timing.append({'vo': v['id'], 'draft_start_f': v['start_f'], 'draft_end_f': v['end_f'],
                   'draft_speech_end_f': v['speech_end_f'],
                   'actual_start_f': round(a0), 'actual_end_f': round(a1),
                   'start_delta_f': round(a0 - v['start_f']), 'end_delta_f': round(a1 - v['speech_end_f'])})
(ROOT / 'data' / 'timing_actual.json').write_text(json.dumps(timing, indent=1))

# ---------- text cleanup (spacing-only, logged) ----------
fixes = []
def clean(t, ctx):
    out = t.replace(',not', ', not').replace('Roundhole', 'Round hole').replace('alternative:merchant', 'alternative: merchant')
    out = re.sub(r'  +', ' ', out)
    if out != t: fixes.append({'context': ctx, 'from': t, 'to': out})
    return out

SRC_LABEL = {
    'S01': 'IEASM report · 7 Oct 2026', 'S03': 'IEASM project methods',
    'S05': 'Live Science via UA.News · 9 Oct 2026', 'S06': 'British Museum catalog',
    'S07': 'The Met · engraved-gems essay', 'S08': 'The Met · object 1978.93.29',
    'S09': 'UNESCO · 2001 Convention principles', 'S10': 'Natural Earth (public domain)',
    'S11': 'city coordinates (approximate)', 'S14': 'Bridport Museum',
}
def src_label(codes):
    parts = []
    for c in codes.replace(';', ' ').replace(',', ' ').split():
        if c in SRC_LABEL and SRC_LABEL[c] not in parts: parts.append(SRC_LABEL[c])
    return ' · '.join(parts)

def lab(t):
    """Split 'Label: rest' into (label, rest)."""
    m = re.match(r'^([A-Z][A-Za-z /]{2,28}):\s*(.+)$', t)
    return (m.group(1), m.group(2)) if m else (None, t)

def esc(s): return html.escape(s, quote=True)

def row_html(seg):
    label, rest = lab(seg)
    rest = esc(rest)
    rest = rest.replace('Possibly', '<em class="q">Possibly</em>').replace('possibly', '<em class="q">possibly</em>')
    if '≠' in rest: rest = rest.replace('≠', '<span class="neq">≠</span>')
    if '→' in rest: rest = rest.replace('→', '<svg class="arrsvg" width="36" height="16" viewBox="0 0 36 16" style="vertical-align:-2px"><path d="M2 8 H28 M22 2 L29 8 L22 14" stroke="#397B83" stroke-width="2.4" fill="none"/></svg>')
    if label: return f'<div class="row"><span class="rlab">{esc(label)}</span><span class="rtext">{rest}</span></div>'
    return f'<div class="row"><span class="rtext">{rest}</span></div>'

# ---------- per-unit interval computation ----------
def unit_intervals(u):
    """Return (host_start_f, host_end_f, panel_intervals, chip_intervals) in actual frames."""
    vid = u['vo']
    if u['id'] == 'MG-046':
        return 0, round(amap(vid, SHOTS['C01-S001']['end_f'])), [(0, round(amap(vid, SHOTS['C01-S001']['end_f'])))], []
    if u['id'] in ('MG-047', 'MG-048', 'MG-049', 'MG-050'):
        a0 = round(amap(vid, VO[vid]['start_f']))
        return a0, a0 + 48, [(a0, a0 + 48)], []
    hs = round(amap(vid, VO[vid]['start_f'])); he = round(amap(vid, VO[vid]['end_f']))
    panels, chips = [], []
    for sid in u['shots']:
        s = SHOTS[sid]
        a, b = round(amap(vid, s['start_f'])), round(amap(vid, s['end_f']))
        is_panel = (s['graphic'] == u['id'] and 'PLATE' not in s['dominance']) or sid in OVERRIDE_SUPPORT
        if 'compact qualifier' in s.get('graphic_note', ''):
            chips.append((a, b, clean(u['copy'][0], u['id'])))
        elif is_panel:
            panels.append((a, b))
        elif 'PLATE' in s['dominance']:
            chips.append((a, b, clean(s['disclosure'].split('|')[0], u['id'] + ' chip')))
    return hs, he, panels, chips

# ---------- HTML templates ----------
FONT_CSS = """
@font-face{font-family:"Spectral";src:url("../assets/fonts/spectral-300.woff2") format("woff2");font-weight:300}
@font-face{font-family:"Spectral";src:url("../assets/fonts/spectral-400.woff2") format("woff2");font-weight:400}
@font-face{font-family:"Spectral";src:url("../assets/fonts/spectral-300i.woff2") format("woff2");font-weight:300;font-style:italic}
@font-face{font-family:"Inter Tight";src:url("../assets/fonts/inter-tight-400.woff2") format("woff2");font-weight:400}
@font-face{font-family:"Inter Tight";src:url("../assets/fonts/inter-tight-500.woff2") format("woff2");font-weight:500}
@font-face{font-family:"Inter Tight";src:url("../assets/fonts/inter-tight-600.woff2") format("woff2");font-weight:600}
:root{--navy:#0B1822;--slate:#253642;--teal:#397B83;--ivory:#F2EEE4;--bronze:#A98255;--amber:#CBA66D;--bone:#C9BFA9;
--f-d:"Spectral",Georgia,serif;--f-t:"Inter Tight",Helvetica,Arial,sans-serif}
*{box-sizing:border-box}html,body{margin:0;padding:0;background:transparent;overflow:hidden}
#root{position:relative;width:1920px;height:1080px;overflow:hidden;background:transparent}
.clip{position:absolute}
.panel{left:192px;top:228px;width:1184px;z-index:5}
.panel.wide{width:1536px}
.panel-in{background:rgba(11,24,34,.90);border:1px solid rgba(169,130,85,.55);padding:34px 44px 30px;box-shadow:0 18px 50px rgba(0,0,0,.45)}
.p-name{font-family:var(--f-d);font-weight:400;font-size:41px;line-height:1.1;color:var(--ivory);margin:0}
.p-rule{height:2px;background:var(--teal);margin:16px 0 8px;transform-origin:left center}
.row{display:flex;gap:16px;align-items:baseline;padding:11px 0;border-bottom:1px solid rgba(242,238,228,.10)}
.row:last-child{border-bottom:none}
.rlab{font-family:var(--f-t);font-weight:600;font-size:28px;letter-spacing:.06em;text-transform:uppercase;color:var(--bronze);white-space:nowrap;padding-top:4px}
.rtext{font-family:var(--f-t);font-weight:400;font-size:39px;line-height:1.22;color:var(--ivory)}
.rtext .q{color:var(--amber);font-style:normal;font-weight:500}
.rtext .neq{color:var(--amber);font-weight:600;padding:0 6px}
.rtext .arr{color:var(--teal);font-weight:600;padding:0 8px}
.chips{display:flex;gap:18px;flex-wrap:wrap;padding-top:8px}
.chipbox{border:1px solid rgba(169,130,85,.6);padding:16px 26px;font-family:var(--f-t);font-size:34px;color:var(--ivory);background:rgba(37,54,66,.65)}
.strip{left:192px;top:694px;width:1184px;z-index:5}
.strip.wide{width:1536px}
.strip-in{display:flex;justify-content:space-between;gap:40px;background:rgba(11,24,34,.93);border-top:1px solid rgba(169,130,85,.45);padding:13px 20px}
.disc{font-family:var(--f-d);font-style:italic;font-weight:300;font-size:28px;color:var(--bone)}
.srcl{font-family:var(--f-t);font-size:28px;color:var(--ivory);white-space:nowrap}
.srcl b{color:var(--amber);font-weight:600;letter-spacing:.05em;text-transform:uppercase;font-size:27px;margin-right:10px}
.dchip{left:192px;top:700px;z-index:5}
.dchip-in{background:rgba(11,24,34,.85);border-left:3px solid var(--teal);padding:10px 18px;font-family:var(--f-d);font-style:italic;font-weight:300;font-size:28px;color:var(--bone)}
.photowrap{display:flex;gap:34px}
.photo{flex:none;width:470px}
.photo img{width:470px;height:318px;object-fit:contain;background:#E8E6E1;display:block}
.photocap{font-family:var(--f-t);font-size:20px;color:var(--bone);margin-top:10px;line-height:1.35;white-space:nowrap}
.photorows{flex:1}
.headwrap{left:192px;top:118px;width:1536px;z-index:8}
.ch-kicker{font-family:var(--f-t);font-weight:600;font-size:28px;letter-spacing:.22em;text-transform:uppercase;color:var(--amber)}
.ch-title{font-family:var(--f-d);font-weight:400;font-size:66px;line-height:1.08;color:var(--ivory);margin-top:10px}
.ch-rule{height:2px;width:520px;background:var(--teal);margin-top:18px;transform-origin:left center}
.titlewrap{left:192px;top:150px;width:1536px;z-index:8}
.t-big{font-family:var(--f-d);font-weight:400;font-size:86px;line-height:1.05;color:var(--ivory)}
.t-sub{font-family:var(--f-t);font-weight:400;font-size:44px;color:var(--bone);margin-top:14px}
.t-src{font-family:var(--f-t);font-size:28px;color:var(--amber);margin-top:26px;letter-spacing:.04em}
svg text{font-family:var(--f-t)}
"""

# ---------- special bodies ----------
def map_body(u):
    geo = json.loads((ROOT / 'assets' / 'geo' / 'map-paths.json').read_text())
    paths = ''.join(f'<path d="{p}"/>' for p in geo['paths'])
    ax, ay = geo['points']['alexandria']
    vb = '287 266 210 118'  # computed crop: lon 25-35E, lat 28-34N (Natural Earth projection px)
    return f'''<div class="photowrap"><div style="flex:none">
<svg width="640" height="360" viewBox="{vb}" preserveAspectRatio="xMidYMid slice" style="background:#10222E;display:block">
<g fill="#2C4553" stroke="#7FA3B0" stroke-width="0.7">{paths}</g>
<circle cx="{ax}" cy="{ay}" r="3.2" fill="#CBA66D"/><circle cx="{ax}" cy="{ay}" r="7" fill="none" stroke="#CBA66D" stroke-width="1.2"/>
<text x="{ax+11}" y="{ay-8}" font-size="10.5" fill="#F2EEE4" font-weight="600">Alexandria</text>
<text x="{ax+11}" y="{ay+6}" font-size="7.5" fill="#C9BFA9">approximate city location</text>
<text x="296" y="290" font-size="10" fill="#9FC3CE" font-style="italic">Mediterranean Sea</text>
<text x="330" y="368" font-size="10" fill="#C9BFA9" letter-spacing="2">EGYPT</text>
</svg></div><div class="photorows">
<div class="row"><span class="rtext">Egypt</span></div>
<div class="row"><span class="rtext">Alexandria — approximate city location</span></div>
<div class="row"><span class="rtext">Antirhodos: reported site; no exact findspot pin</span></div>
</div></div>'''

def vx1_body(u):
    return '''<svg width="1096" height="208" viewBox="0 0 1096 300">
<g id="vx1-a"><circle cx="150" cy="130" r="86" fill="none" stroke="#A98255" stroke-width="10"/>
<circle cx="150" cy="130" r="60" fill="#253642" stroke="#397B83" stroke-width="2"/>
<path d="M150 92 L162 118 L190 120 L168 137 L176 165 L150 150 L124 165 L132 137 L110 120 L138 118 Z" fill="#CBA66D"/>
<text x="150" y="248" text-anchor="middle" font-size="24" fill="#C9BFA9">Seal face — generic symbol</text></g>
<path id="vx1-arrow" d="M268 130 L470 130" stroke="#397B83" stroke-width="5" fill="none"/>
<path d="M470 130 L442 116 L442 144 Z" fill="#397B83"/>
<g id="vx1-b"><path d="M520 62 Q640 34 760 62 Q792 130 760 198 Q640 226 520 198 Q488 130 520 62Z" fill="#3A2E22" stroke="#A98255" stroke-width="2"/>
<path d="M640 100 L649 118 L669 120 L653 132 L659 152 L640 141 L621 152 L627 132 L611 120 L631 118Z" fill="none" stroke="#E8D9B8" stroke-width="3"/>
<text x="640" y="248" text-anchor="middle" font-size="24" fill="#C9BFA9">Impression in soft material</text></g>
<g id="vx1-c" opacity="0"><path d="M836 76 Q916 56 996 76 Q1018 130 996 184 Q916 204 836 184 Q814 130 836 76Z" fill="#3A2E22" stroke="#A98255" stroke-width="2"/>
<path d="M916 106 L923 119 L938 121 L926 130 L930 146 L916 138 L902 146 L906 130 L894 121 L909 119Z" fill="none" stroke="#E8D9B8" stroke-width="3"/>
<text x="916" y="248" text-anchor="middle" font-size="24" fill="#C9BFA9">The mark travels</text></g></svg>
<div class="row"><span class="rtext">Design <svg class="arrsvg" width="36" height="16" viewBox="0 0 36 16" style="vertical-align:-2px"><path d="M2 8 H28 M22 2 L29 8 L22 14" stroke="#397B83" stroke-width="2.4" fill="none"/></svg> identifying impression</span></div>
<div class="row"><span class="rtext">Schematic, not this ring’s actual impression</span></div>'''

def vx2_body(u):
    return '''<div style="display:flex;gap:26px">
<div style="flex:1;border:1px solid rgba(169,130,85,.55);padding:22px 26px;background:rgba(37,54,66,.5)">
<div class="rlab">Team interpretation</div>
<div style="font-family:var(--f-t);font-size:36px;line-height:1.25;color:var(--ivory);margin-top:10px">lighthouse-related administration</div>
<div style="font-family:var(--f-t);font-size:22px;color:var(--bone);margin-top:12px">Excavation team · IEASM report</div></div>
<div style="flex:1;border:1px solid rgba(169,130,85,.55);padding:22px 26px;background:rgba(37,54,66,.5)">
<div class="rlab">Reported alternative</div>
<div style="font-family:var(--f-t);font-size:36px;line-height:1.25;color:var(--ivory);margin-top:10px">merchant / city symbol</div>
<div style="font-family:var(--f-t);font-size:22px;color:var(--bone);margin-top:12px">Margaret Miles · reported by Live Science; relayed by UA.News</div></div></div>
<div class="row" style="margin-top:14px"><span class="rtext">Neither identifies a specific user</span></div>'''

def vx3_body(u):
    return '''<div class="row"><span class="rtext">Context/use interpretation <span class="neq">≠</span> exact manufacture year</span></div>
<div style="margin-top:10px">
<div style="display:flex;gap:18px;align-items:baseline;padding:13px 0;border-bottom:1px solid rgba(242,238,228,.12)">
<span class="rlab" style="min-width:280px">Associated ceramics</span><span class="rtext">second century AD</span></div>
<div style="display:flex;gap:18px;align-items:baseline;padding:13px 0">
<span class="rlab" style="min-width:280px">Ring manufacture</span><span class="rtext">not fixed here — could be earlier</span></div>
<div style="font-family:var(--f-d);font-style:italic;font-size:25px;color:var(--amber);margin-top:6px">Reported association — connects context, not dates of manufacture</div></div>'''

def photo_body(u):
    rows = ''.join(row_html(clean(s, u['id'])) for s in u['copy'])
    return f'''<div class="photowrap"><div class="photo">
<img class="photoimg" src="../assets/photo/met-bulla-1978.93.29.jpg" alt="Met bulla 1978.93.29"/>
<div class="photocap">The Met · 1978.93.29 · Public Domain</div></div>
<div class="photorows">{rows}</div></div>'''

def unit_body(u):
    if u['id'] == 'MG-003': return map_body(u)
    if u['id'] == 'VX-001': return vx1_body(u)
    if u['id'] == 'VX-002': return vx2_body(u)
    if u['id'] == 'VX-003': return vx3_body(u)
    if u['id'] in ('MG-011', 'MG-012', 'MG-013'): return photo_body(u)
    segs = [clean(s, u['id']) for s in u['copy']]
    if len(segs) >= 3 and all(len(s) <= 26 for s in segs):
        return '<div class="chips">' + ''.join(f'<div class="chipbox">{esc(s)}</div>' for s in segs) + '</div>'
    return ''.join(row_html(s) for s in segs)

# ---------- composition writers ----------
def boundary_cat_at(draft_f):
    b = BOUNDS.get(draft_f)
    return b['category'] if b else 'CUT'

def write_unit_comp(u):
    uid = u['id']
    hs, he, panels, chips = unit_intervals(u)
    dur_s = (he - hs) / FPS
    gvid = VO[u['vo']]
    sections, tl = [], []
    first_panel = panels[0] if panels else (hs, he)
    for k, (a, b) in enumerate(panels):
        ls, ld = (a - hs) / FPS, (b - a) / FPS
        gshot = next(SHOTS[s] for s in u['shots'] if SHOTS[s]['graphic'] == uid or s in OVERRIDE_SUPPORT)
        body = unit_body(u)
        strip = (f'<div class="strip-in"><span class="disc">{esc(clean(gshot["disclosure"].split("|")[0], uid))}</span>'
                 f'<span class="srcl"><b>Source</b>{esc(src_label(u["sources"]))}</span></div>')
        tops = {'MG-001': 342, 'MG-009': 306, 'MG-020': 306, 'MG-029': 306, 'MG-037': 306, 'VX-001': 196, 'MG-003': 180}
        style = f' style="top:{tops[uid]}px"' if uid in tops else ''
        sections.append(f'<section class="clip panel{" wide" if uid in ("MG-003", "VX-001", "VX-002") else ""}"{style} id="{uid.lower()}-panel{k}" '
                        f'data-start="{ls:.3f}" data-duration="{ld:.3f}" data-track-index="2">'
                        f'<div class="panel-in"><h2 class="p-name">{esc(clean(u["name"], uid))}</h2><div class="p-rule"></div>{body}</div></section>')
        sections.append(f'<section class="clip strip{" wide" if uid in ("MG-003", "VX-001", "VX-002") else ""}" id="{uid.lower()}-strip{k}" '
                        f'data-start="{ls:.3f}" data-duration="{ld:.3f}" data-track-index="3"><div class="strip-inwrap">{strip}</div></section>')
        tl.append(f'tl.fromTo("#{uid.lower()}-panel{k} .panel-in",{{opacity:0,y:18}},{{opacity:1,y:0,duration:0.35,ease:"power2.out"}},{ls:.3f});')
        tl.append(f'tl.fromTo("#{uid.lower()}-panel{k} .p-rule",{{scaleX:0}},{{scaleX:1,duration:0.5,ease:"power2.out"}},{ls + 0.1:.3f});')
        tl.append(f'tl.fromTo("#{uid.lower()}-panel{k} .row, #{uid.lower()}-panel{k} .chipbox",{{opacity:0,y:12}},{{opacity:1,y:0,duration:0.4,stagger:0.55,ease:"power2.out"}},{ls + 0.25:.3f});')
        tl.append(f'tl.fromTo("#{uid.lower()}-strip{k} .strip-inwrap",{{opacity:0}},{{opacity:1,duration:0.35}},{ls + 0.15:.3f});')
        cat = boundary_cat_at(next(SHOTS[s]['end_f'] for s in u['shots'] if (SHOTS[s]['graphic'] == uid and 'PLATE' not in SHOTS[s]['dominance']) or s in OVERRIDE_SUPPORT))
        end_local = ls + ld
        if cat in ('CROSSFADE', 'GRAPHIC') and end_local < dur_s - 0.05:
            tl.append(f'tl.to("#{uid.lower()}-panel{k} .panel-in",{{opacity:0,duration:0.45,ease:"power1.in"}},{end_local - 0.45:.3f});')
            tl.append(f'tl.to("#{uid.lower()}-strip{k} .strip-inwrap",{{opacity:0,duration:0.4}},{end_local - 0.4:.3f});')
    for k, (a, b, txt) in enumerate(chips):
        ls, ld = (a - hs) / FPS, (b - a) / FPS
        sections.append(f'<section class="clip dchip" id="{uid.lower()}-chip{k}" data-start="{ls:.3f}" data-duration="{ld:.3f}" data-track-index="2">'
                        f'<div class="dchip-in">{esc(txt)}</div></section>')
        tl.append(f'tl.fromTo("#{uid.lower()}-chip{k} .dchip-in",{{opacity:0}},{{opacity:1,duration:0.4}},{ls:.3f});')
    if uid == 'VX-001' and panels:
        ls = (panels[0][0] - hs) / FPS
        tl.append(f'tl.fromTo("#vx1-c",{{opacity:0}},{{opacity:1,duration:0.8}},{ls + 6.5:.3f});')
    tl.append(f'tl.to({{}},{{duration:0.001}},{max(dur_s - 0.002, 0):.3f});')
    comp = f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}</style>
<script src="../assets/gsap.min.js"></script></head><body>
<div class="stage" id="root" data-composition-id="unit-{uid.lower()}" data-width="1920" data-height="1080" data-duration="{dur_s:.3f}" data-fps="24">
{chr(10).join(sections)}
</div>
<script>window.__timelines=window.__timelines||{{}};var tl=gsap.timeline({{paused:true}});
{chr(10).join(tl)}
window.__timelines["unit-{uid.lower()}"]=tl;</script></body></html>'''
    (ROOT / 'compositions' / f'unit-{uid}.html').write_text(comp)
    return hs, he

def write_heading_comp(u):
    uid = u['id']
    hs, he, _, _ = unit_intervals(u)
    dur_s = (he - hs) / FPS
    title = clean(u['copy'][0], uid)
    chno = {'MG-047': 'Chapter Two', 'MG-048': 'Chapter Three', 'MG-049': 'Chapter Four', 'MG-050': 'Chapter Five'}[uid]
    comp = f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}</style>
<script src="../assets/gsap.min.js"></script></head><body>
<div class="stage" id="root" data-composition-id="unit-{uid.lower()}" data-width="1920" data-height="1080" data-duration="{dur_s:.3f}" data-fps="24">
<section class="clip headwrap" id="{uid.lower()}-head" data-start="0" data-duration="{dur_s:.3f}" data-track-index="2">
<div class="head-in"><div class="ch-kicker">{chno}</div><div class="ch-title">{esc(title)}</div><div class="ch-rule"></div></div>
</section></div>
<script>window.__timelines=window.__timelines||{{}};var tl=gsap.timeline({{paused:true}});
tl.fromTo(".head-in",{{opacity:0,y:14}},{{opacity:1,y:0,duration:0.3,ease:"power2.out"}},0);
tl.fromTo(".ch-rule",{{scaleX:0}},{{scaleX:1,duration:0.45,ease:"power2.out"}},0.08);
tl.to(".head-in",{{opacity:0,duration:0.3,ease:"power1.in"}},{dur_s - 0.32:.3f});
window.__timelines["unit-{uid.lower()}"]=tl;</script></body></html>'''
    (ROOT / 'compositions' / f'unit-{uid}.html').write_text(comp)
    return hs, he

def write_title_comp(u):
    uid = 'MG-046'
    hs, he, _, _ = unit_intervals(u)
    dur_s = (he - hs) / FPS
    comp = f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}</style>
<script src="../assets/gsap.min.js"></script></head><body>
<div class="stage" id="root" data-composition-id="unit-mg-046" data-width="1920" data-height="1080" data-duration="{dur_s:.3f}" data-fps="24">
<section class="clip titlewrap" id="mg-046-title" data-start="0" data-duration="{dur_s:.3f}" data-track-index="2">
<div class="title-in"><div class="t-big">The Lighthouse Ring</div><div class="t-sub">Alexandria’s submerged palace</div>
<div class="t-src">IEASM report · 7 Oct 2026</div></div>
</section></div>
<script>window.__timelines=window.__timelines||{{}};var tl=gsap.timeline({{paused:true}});
tl.fromTo(".title-in",{{opacity:0,y:16}},{{opacity:1,y:0,duration:0.4,ease:"power2.out"}},0);
tl.to(".title-in",{{opacity:0,duration:0.5,ease:"power1.in"}},{max(dur_s - 0.9, 3.5):.3f});
window.__timelines["unit-mg-046"]=tl;</script></body></html>'''
    (ROOT / 'compositions' / 'unit-MG-046.html').write_text(comp)
    return hs, he

def write_root(windows):
    chain = sorted((windows[u['id']][0], u['id']) for u in cmd['units'] if u['id'] not in ('MG-046','MG-047','MG-048','MG-049','MG-050'))
    nxt = {chain[i][1]: chain[i+1][0] for i in range(len(chain)-1)}
    mounts = []
    for u in cmd['units']:
        uid = u['id']
        hs, he = windows[uid]
        if uid in nxt: he = min(he, nxt[uid] - 1)
        z = 20 if uid.startswith('MG-04') and uid != 'MG-045' else 10
        mounts.append(f'<div class="clip mount" id="m-{uid.lower()}" style="z-index:{z}" data-track-kind="graphics" '
                      f'data-composition-src="compositions/unit-{uid}.html" data-composition-id="unit-{uid.lower()}" '
                      f'data-start="{hs / FPS:.3f}" data-duration="{(he - hs) / FPS:.3f}" data-track-index="10"></div>')
    root_css = FONT_CSS.replace('../assets/', 'assets/')
    doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>{root_css}
video{{position:absolute;inset:0;width:1920px;height:1080px;object-fit:cover;z-index:1}}
.mount{{inset:0}}</style>
<script src="assets/gsap.min.js"></script></head><body>
<div class="stage" id="root" data-composition-id="atlas-understory-01-rebuild" data-width="1920" data-height="1080" data-duration="656.041667" data-fps="24">
<video class="clip" id="master-video" data-start="0" data-duration="656.041667" data-track-index="1" src="assets/video/master.mp4" muted playsinline data-media-start="0"></video>
<audio class="clip" id="master-audio" data-start="0" data-duration="656.041667" data-track-index="0" src="assets/video/master.mp4" data-audio-group="mix" preload="auto"></audio>
{chr(10).join(mounts)}
</div>
<script>window.__timelines=window.__timelines||{{}};window.__timelines["atlas-understory-01-rebuild"]=gsap.timeline({{paused:true}});</script></body></html>'''
    (ROOT / 'index.html').write_text(doc)

def write_caption_proof():
    cues = [c for c in oldcaps['cues'] if c['segment'] == 'VO-C01-B01']
    t0 = cues[0]['start_s']
    dur = cues[-1]['out_s'] - t0 + 1.0
    groups, tl = [], []
    for i, c in enumerate(cues):
        s, d = c['start_s'] - t0, c['out_s'] - c['start_s']
        txt = '<br/>'.join(esc(l) for l in c['lines'])
        groups.append(f'<section class="clip capgroup" id="cap{i}" data-start="{s:.3f}" data-duration="{d:.3f}" data-track-index="2">'
                      f'<div class="cap-in">{txt}</div></section>')
        tl.append(f'tl.fromTo("#cap{i} .cap-in",{{opacity:0,y:10}},{{opacity:1,y:0,duration:0.25}},{s:.3f});')
    comp = f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}
body{{background:#0B1822}}#root{{background:#0B1822}}
.capgroup{{left:240px;top:806px;width:1440px;text-align:center}}
.cap-in{{display:inline-block;background:rgba(11,24,34,.88);padding:16px 28px;font-family:var(--f-t);font-size:50px;line-height:1.25;color:var(--ivory)}}
.proof-label{{left:192px;top:120px;font-family:var(--f-t);font-size:28px;color:var(--bone)}}</style>
<script src="../assets/gsap.min.js"></script></head><body>
<div class="stage" id="root" data-composition-id="caption-proof" data-width="1920" data-height="1080" data-duration="{dur:.3f}" data-fps="24">
<div class="clip proof-label" data-start="0" data-duration="{dur:.3f}" data-track-index="1">Caption proof — VO-C01-B01 phrase groups (test assembly, not the film)</div>
<div class="clip caphost" data-track-kind="captions" data-start="0" data-duration="{dur:.3f}" data-track-index="2" style="inset:0">
{chr(10).join(groups)}</div></div>
<script>window.__timelines=window.__timelines||{{}};var tl=gsap.timeline({{paused:true}});
{chr(10).join(tl)}
window.__timelines["caption-proof"]=tl;</script></body></html>'''
    (ROOT / 'proof' / 'caption-proof.html').write_text(comp)

def main():
    windows = {}
    for u in cmd['units']:
        uid = u['id']
        if uid == 'MG-046': windows[uid] = write_title_comp(u)
        elif uid in ('MG-047', 'MG-048', 'MG-049', 'MG-050'): windows[uid] = write_heading_comp(u)
        else: windows[uid] = write_unit_comp(u)
    write_root(windows)
    write_caption_proof()
    seen, fl = set(), []
    for f in fixes:
        k = (f['context'], f['from'])
        if k not in seen: seen.add(k); fl.append(f)
    (ROOT / 'data' / 'override_log.json').write_text(json.dumps(fl, indent=1, ensure_ascii=False))
    print(f'units written: {len(windows)}  spacing fixes: {len(fl)}')
    for u in cmd['units']:
        hs, he = windows[u['id']]
        print(f"  {u['id']:7} {hs / FPS:8.2f} .. {he / FPS:8.2f}  ({(he - hs) / FPS:5.1f}s)")

if __name__ == '__main__':
    main()
