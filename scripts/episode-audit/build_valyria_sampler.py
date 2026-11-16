#!/usr/bin/env python3
"""Build a separate 12-minute Old Valyria documentary-language sampler.
Reuses selected voice-01 narration excerpts, not the rejected condensed film.
Does not modify the 35-minute film, narration, ledger or original assets.
"""
import hashlib
import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EP = ROOT/'projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria'
SOURCE = EP/'documentary_film'
P = ROOT/'projects/valyria_style_sampler'
CH = [
 ('Cinematic history','From pasture to power',0,[1,8,23,30,151,226],'#c5a56a','Wide establishing images · restrained camera · question-led opening','Original illustrated reconstruction. Not recovered footage.'),
 ('Archival essay','Reading the uncertain past',60,[31,38,46,53,60,76],'#b79769','Reading cards · chronology · quotation vs interpretation','Designed reading cards, not scans or facsimiles of published pages.'),
 ('Investigative history','Where did dragons begin?',780,[391,398,405,406,413,420],'#d2a26f','Competing claims · evidence labels · unresolved questions','Traditions are presented as traditions, not verified origins.'),
 ('Geographic explainer','The peninsula beneath fire',300,[151,158,165,166,173,180],'#6bc9bb','Schematic map · progressive route · geographic callouts','Not an authoritative map. No exact distance or peak count implied.'),
 ('Natural-history explainer','An animal, not an emblem',660,[331,335,338,345,346,353],'#7ebdc8','Anatomy labels · conceptual diagram · image-detail cutaways','Simplified fictional anatomy. Illustrated details are not scientific evidence.'),
 ('Political history','Power without one throne',1350,[676,683,690,691,698,705],'#b3a0d4','Conceptual network · hierarchy · institutional comparison','Nodes are illustrative, not a complete genealogy or influence ranking.'),
 ('Human-cost documentary','The price beneath the stone',1740,[871,878,885,886,893,900],'#bdafa1','Longer holds · quiet transitions · narration-first sound','Unnamed people are AI reconstructions. Sound effects are designed.'),
 ('Reflective essay','Who paid for their power?',2040,[1021,1028,1035,1036,1043,1050],'#d0b177','Juxtaposition · recurring motif · editorial typography','An illustrated fan-documentary demonstration, not a new lore source.'),
]
INTRO = [
 'Old Valyria. One story, eight documentary languages. First, cinematic history: a question, a landscape, and an unfolding transformation. These are illustrated reconstructions, not recovered footage. Watch the images establish scale before the argument begins.',
 'The archival essay makes uncertainty visible. Our narration now becomes a reading guide, framed by chronology and source notes. These are designed reading cards, not scans of ancient documents. A beautiful page must never be mistaken for new evidence.',
 'Investigative history separates a tradition from a conclusion. Where did dragons come from? This treatment places competing accounts beside one another, leaving unresolved questions open. The graphics organize the claims; they do not prove them.',
 'A geographic explainer connects pasture, coast and volcanic mountains. This is a schematic peninsula, not an authoritative map. Watch the labels and routes reveal relationships without pretending to establish exact locations or distances.',
 'A natural-history treatment looks at the dragon as an animal rather than a banner. Labels isolate wings, hind legs and the body. The drawing is a simplified fictional anatomy study, not a scientific model or proof of every illustrated detail.',
 'Political history asks how power is distributed. The Freehold becomes a network of competing dragonlord houses rather than a single throne. These nodes represent a concept, not a complete family tree, census or measured ranking of influence.',
 'The human-cost documentary slows the camera and refuses spectacle. The mines move from background detail to the center of the story. These people are unnamed reconstructions. Sound is designed for the film, not presented as an authentic recording.',
 'The reflective essay brings the argument together: pasture, power, stone and servitude. Typography and juxtaposition can guide attention without inventing testimony. Compare this ending with the cinematic opening, then choose the combination that best serves your film.'
]

def esc(s): return html.escape(str(s))
def clip(cid,start,duration,content,css='panel',track=1):
 return f'<div id="{cid}" class="clip {css}" data-start="{start}" data-duration="{duration}" data-track-index="{track}" data-track-kind="graphics" data-hold="true">{content}</div>'
def plate(idx,cls=''):
 return f'<img class="photo {cls}" src="assets/images/{idx:04}.jpg" alt="AI-illustrated Valyria reconstruction">'
def lockup(k,t,desc=''):
 return f'<div class="lock"><p class="eyebrow">{esc(k)}</p><h1>{esc(t)}</h1><p class="deck">{esc(desc)}</p></div>'
def card(k,t,desc=''):
 return f'<div class="reading"><p class="eyebrow">{esc(k)}</p><h2>{esc(t)}</h2><p>{esc(desc)}</p></div>'

def map_svg():
 return '''<svg class="diagram" viewBox="0 0 1200 650"><defs><pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M60 0H0V60" fill="none" stroke="#233e40" stroke-width="1"/></pattern></defs><rect width="1200" height="650" fill="url(#grid)"/><path d="M70 40 L970 45 1090 160 890 230 820 330 760 480 660 580 550 530 520 410 410 330 300 240 140 200Z" fill="#243e3a" stroke="#9bba9d" stroke-width="3"/><path class="route" d="M400 190Q600 260 625 455" fill="none" stroke="#d9c595" stroke-width="7" stroke-dasharray="700"/><g fill="#c99c71"><path d="M480 245l45-85 45 85Z"/><path d="M600 270l55-105 55 105Z"/><path d="M720 245l45-85 45 85Z"/></g><g fill="#e5e4d3" font-size="30" font-family="Arial"><text x="510" y="125">VOLCANIC HEIGHTS</text><text x="260" y="335">PASTURE</text><text x="700" y="530">SOUTHERN SEAS</text><text x="55" y="610" font-size="28">SCHEMATIC — not cartography / no exact scale</text></g><circle class="map-dot" cx="625" cy="455" r="12" fill="#fff0c0"/></svg>'''

def anatomy_svg():
 return '''<svg class="diagram" viewBox="0 0 1200 650"><g fill="#38515a" stroke="#b9d5d9" stroke-width="3"><path d="M590 350C500 320 430 180 260 110L320 220 160 220 350 300 240 330 530 390Z"/><path d="M620 350C730 300 820 180 1010 100L950 235 1120 210 940 310 1050 340 680 395Z"/><ellipse cx="606" cy="375" rx="100" ry="51"/><path d="M540 370Q405 400 340 460Q450 445 565 413Z"/><path d="M667 350Q700 260 770 265L810 290 760 315 705 395Z"/><path d="M580 405l-15 80 60-5-25-18 20-54Z"/><path d="M640 410l20 75 58-10-35-18-4-64Z"/></g><g fill="none" stroke="#d4b788" stroke-width="2"><path d="M340 200L220 65H80"/><path d="M680 470L790 550H1050"/><path d="M605 350V105H710"/></g><g fill="#e3e9e9" font-family="Arial" font-size="30"><text x="70" y="50">WING FORELIMBS</text><text x="800" y="590">TWO HIND LEGS</text><text x="720" y="115">BODY</text><text x="60" y="625" font-size="28">CONCEPTUAL SILHOUETTE — not a biological simulation</text></g></svg>'''

def network_svg():
 pts=[(240,150),(600,100),(960,150),(1040,440),(600,520),(160,440)]
 lines=''.join(f'<line x1="{x}" y1="{y}" x2="{xx}" y2="{yy}"/>' for i,(x,y) in enumerate(pts) for xx,yy in pts[i+1:])
 nodes=''.join(f'<g class="house"><circle cx="{x}" cy="{y}" r="62"/><text x="{x}" y="{y+9}" text-anchor="middle">HOUSE</text></g>' for x,y in pts)
 return f'<svg class="diagram" viewBox="0 0 1200 650"><g stroke="#746382" stroke-width="2">{lines}</g><g fill="#292332" stroke="#bba6d9" stroke-width="3">{nodes}</g><text x="600" y="325" text-anchor="middle" fill="#f0e7d8" font-family="Georgia" font-size="46">NO SINGLE THRONE</text><text x="600" y="635" text-anchor="middle" fill="#b7abbe" font-family="Arial" font-size="28">Conceptual network — not all forty families or a measured graph</text></svg>'


def main():
 for folder in ['assets/audio','assets/images','assets/vendor','compositions','production','renders']:(P/folder).mkdir(parents=True,exist_ok=True)
 shutil.copyfile(SOURCE/'assets/vendor/gsap.min.js',P/'assets/vendor/gsap.min.js')
 manifest=json.loads((SOURCE/'production/FILM_MANIFEST.json').read_text())
 narration=json.loads((EP/'story_film_35min/narration_blocks_v02.json').read_text())
 used=sorted({v for ch in CH for v in ch[3]})
 for idx in used:shutil.copyfile(SOURCE/f'assets/images/{idx:04}.jpg',P/f'assets/images/{idx:04}.jpg')
 shutil.copytree(SOURCE/'production/audio_licenses',P/'production/audio_licenses',dirs_exist_ok=True)
 hosts=[];chapters=[]
 for c,(style,title,source_start,images,accent,tools,caveat) in enumerate(CH,1):
  cid=f'chapter{c:02}'; tags=[]; anim=[]
  tags.append(clip(f'{cid}-intro',0,22,plate(images[0])+lockup(f'{c:02} / DOCUMENTARY LANGUAGE',style,title),'intro'))
  anim += [f'tl.fromTo("#{cid}-intro .photo",{{scale:1}},{{scale:1.055,duration:21.9,ease:"none"}},0);',f'tl.fromTo("#{cid}-intro .lock",{{opacity:0,y:28}},{{opacity:1,y:0,duration:1.2}},0.8);']
  for j in range(6):
   start=22+j*10;sub=f'{cid}-p{j}';img=plate(images[j]);content=img;cls='panel'
   if c==2:
    excerpts=[('THE RECORD','Dates remain uncertain','The chronology is distant; the narration distinguishes later traditions from eyewitness knowledge.'),('THE NARRATION','Later histories place Valyria’s rise roughly five thousand years before the Conquest','Excerpt from the project narration. Not a quotation copied from a published book.'),('THE LIMIT','Distance has blurred the chronology','Designed reading treatment / not an authentic manuscript.'),('RIVER TRADITIONS','Along the Rhoyne','A later remembered account enters the story as a tradition.'),('THE IMAGE','An imagined frozen river','Illustration helps the viewer follow the account; it does not establish an event.'),('THE METHOD','Keep the source visible','Published book/page verification remains a separate research step.')]
    content=f'<div class="archive-photo">{img}</div>'+card(*excerpts[j]);cls+=' archival'
   elif c==3:
    labels=[('VALYRIAN TRADITION','The Fourteen Flames','An origin associated with the volcanic peninsula.'),('OPEN QUESTION','One place, or a wider history?','A tradition does not prove dragons existed nowhere else.'),('COMPARE','Claim / account / uncertainty','The narration keeps these categories distinct.'),('QARTHENE TALE','Two moons','A mythic explanation, presented as a tale.'),('THE LEGEND','A moon cracked like an egg','Do not animate a legend as if it were an astronomical finding.'),('UNRESOLVED','The origin remains disputed','A question may be the honest end of an investigation.')]
    content=f'<div class="evidence-photo">{img}</div>'+card(*labels[j]);cls+=' investigative'
   elif c==4:
    content=map_svg()+f'<div class="map-inset">{img}</div><div class="diagram-title">{esc(["A living peninsula","Coast and pasture","Mountains above settlement","The Fourteen Flames","A volcanic landscape","Not a barren wasteland"][j])}</div>';cls+=' technical'
    anim.append(f'tl.fromTo("#{sub} .route",{{strokeDashoffset:700}},{{strokeDashoffset:0,duration:5,ease:"none"}},{start});')
   elif c==5:
    if j%2==0:content=anatomy_svg()+f'<div class="diagram-title">{esc(["Look at the animal","", "Two wing forelimbs", "", "An illustrated anatomy", ""][j])}</div>'
    else:content=img+f'<div class="detail-tag">{esc(["","Scales and folded wing","","Jaws and nostrils","","Illustrative fire detail — not biology"][j])}</div>'
    cls+=' anatomy'
   elif c==6:
    if j in [0,2,4]:content=network_svg()+f'<div class="diagram-title">{esc(["The Freehold","","Competing dragonlord houses","","Power checks power",""][j])}</div>'
    else:content=img+f'<div class="detail-tag">{esc(["","A political community","","Dragons change the calculation","","Competition is not equality"][j])}</div>'
    cls+=' politics'
    if j in [0,2,4]:anim.append(f'tl.fromTo("#{sub} .house",{{opacity:0}},{{opacity:1,stagger:0.3,duration:0.8}},{start+0.5});')
   elif c==7:
    content=img+f'<div class="human-note">{esc(["Captivity is not background","Heat, dust and danger","A reconstruction, not identified people","The system at human scale","No invented last words","Whose achievement? Whose suffering?"][j])}</div>';cls+=' human'
   elif c==8:
    words=['PASTURE','BLOOD','STONE','SERVITUDE','HARPY / DRAGON','WHO PAID?'];content=img+f'<div class="essay-word">{esc(words[j])}</div>';cls+=' essay'
   else:
    content+=f'<div class="cinema-note">{esc(["Before the throne","A smoking peninsula","Shepherds before dragonlords","From discovery to possession","Power changes the landscape","Who paid for their world?"][j])}</div>'
   tags.append(clip(sub,start,10,content,cls))
   if c in [1,7,8] or (c==5 and j%2):anim.append(f'tl.fromTo("#{sub} .photo",{{scale:1,x:0}},{{scale:{1.018 if c==7 else 1.045},x:{0 if c==7 else (-12 if j%2 else 12)},duration:9.99,ease:"none"}},{start});')
  ending=card('WHAT THIS TREATMENT ADDS',tools,caveat)
  if c==8:ending='<div class="closing"><h2>Choose the language.<br>Then build the film.</h2><p>Cinematic · archival · investigative · geographic · natural history · political · human cost · reflective essay</p><p class="credits">Music: Kevin MacLeod / CC BY 4.0<br>creativecommons.org/licenses/by/4.0/<br>SFX: Kenney RPG Audio / CC0<br>AI illustrations and synthetic narration · unofficial fan documentary</p></div>'
  tags.append(clip(f'{cid}-outro',82,8,ending,'outro'))
  tags.append(clip(f'{cid}-label',0,90,f'<span>{c:02} / {esc(style.upper())}</span><span>OLD VALYRIA • STYLE SAMPLER</span>','topline',5))
  tags.append(clip(f'{cid}-disclosure',0,82,esc(caveat),'disclosure',4))
  css='''*{box-sizing:border-box}#root{position:absolute;inset:0;background:#101211;color:#f1e9dc;font-family:Arial,sans-serif;overflow:hidden}.intro,.panel,.outro{position:absolute;inset:0;overflow:hidden;background:#101211}.photo{position:absolute;inset:0;width:100%;height:100%;object-fit:contain}.intro .photo{opacity:.46}.lock{position:absolute;left:192px;right:192px;bottom:230px;max-width:1500px}.eyebrow{font-size:28px;letter-spacing:4px;color:var(--accent);text-transform:uppercase;margin:0 0 20px}h1{font:76px/1.1 Georgia,serif;font-weight:400;margin:0}h2{font:48px/1.25 Georgia,serif;margin:0 0 24px}.deck{font-size:35px;color:#ded3bf;margin:25px 0 0}.topline{position:absolute;left:0;right:0;top:0;display:flex;justify-content:space-between;padding:38px 96px 26px;font-size:28px;letter-spacing:2px;color:#f0e2c4;z-index:9;background:linear-gradient(180deg,rgba(8,10,9,.88) 0%,rgba(8,10,9,.72) 55%,rgba(8,10,9,0) 100%);text-shadow:0 1px 3px rgba(0,0,0,.9)}.disclosure{position:absolute;bottom:38px;left:120px;right:120px;text-align:center;font-size:28px;line-height:1.25;color:#c9c5bb;background:#101211;z-index:8;padding:8px}.cinema-note,.detail-tag,.human-note{position:absolute;left:192px;bottom:155px;max-width:1450px;background:rgba(12,14,13,.92);padding:20px 30px;font:40px/1.2 Georgia,serif;border-left:3px solid var(--accent)}.reading{position:absolute;left:192px;right:192px;top:240px;padding:42px 50px;background:#e5dbc6;color:#28251f;max-width:1500px;border-left:5px solid var(--accent)}.reading p:not(.eyebrow){font-size:30px;line-height:1.5;margin-bottom:0}.reading .eyebrow{color:#735d39}.archive-photo{position:absolute;right:120px;top:130px;width:560px;height:760px;opacity:.75}.archival .reading{left:155px;right:auto;top:245px;width:1100px;background:#e5dbc6}.evidence-photo{position:absolute;inset:130px 110px 150px 830px;opacity:.65}.investigative .reading{left:140px;right:auto;width:1030px;top:260px;background:#191c20;color:#efebe2;border:2px solid #806e4a}.investigative .reading .eyebrow{color:#d4b57b}.technical{background:#0e2226}.diagram{position:absolute;left:170px;top:220px;width:1580px;height:650px}.diagram-title{position:absolute;left:192px;top:135px;font:44px Georgia,serif;color:#e9e2d4}.map-inset{position:absolute;width:380px;height:215px;right:170px;bottom:130px;border:2px solid #9bba9d}.anatomy{background:#14252c}.politics{background:#201c27}.politics text{fill:#eee5d8;stroke:none;font:30px Arial}.human{background:#100f0e}.human .photo{object-fit:contain}.human-note{font-size:34px;border:0;background:#161410}.essay-word{position:absolute;left:160px;bottom:190px;font:bold 112px/1 Arial,sans-serif;color:#f4e7cb;text-shadow:0 4px 20px #000}.essay .photo{opacity:.63}.outro .reading{top:200px;background:#171b1b;color:#efebe1}.outro .reading .eyebrow{color:var(--accent)}.closing{position:absolute;left:192px;top:150px;right:192px}.closing h2{font-size:56px}.closing p{font-size:30px;max-width:1450px;line-height:1.5}.closing .credits{font-size:28px;color:#c5b99f}'''
  doc=f'<template><style>{css}</style><div id="root" data-composition-id="{cid}" data-duration="90" data-width="1920" data-height="1080" style="--accent:{accent}">'+''.join(tags)+f'</div><script>(function(){{const tl=gsap.timeline({{paused:true}});'+''.join(anim)+f'window.__timelines=window.__timelines||{{}};window.__timelines["{cid}"]=tl;}})();</script></template>'
  (P/f'compositions/{cid}.html').write_text(doc)
  hosts.append(f'<div id="{cid}" class="clip" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" data-start="{(c-1)*90}" data-duration="90" data-width="1920" data-height="1080" data-track-index="1" data-track-kind="graphics"></div>')
  chapters.append({'number':c,'start':(c-1)*90,'duration':90,'style':style,'title':title,'source_narration_start':source_start,'source_narration_duration':60,'source_narration_placement':22,'intro_text':INTRO[c-1],'intro_asset':f'assets/audio/intro-{c:02}.mp3','images':images,'techniques':tools,'caveat':caveat,'source_narration_blocks':narration[source_start//30:source_start//30+2]})
 (P/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Old Valyria — Eight Documentary Languages</title><script src="assets/vendor/gsap.min.js"></script><style>html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#101211}#sampler{position:relative;width:1920px;height:1080px}#sampler>.clip:not(audio){position:absolute;inset:0}</style></head><body><div id="sampler" data-composition-id="sampler" data-width="1920" data-height="1080" data-fps="30" data-start="0" data-duration="720">'+''.join(hosts)+'<audio id="soundtrack" class="clip" src="assets/audio/soundtrack.m4a" data-start="0" data-duration="720" data-volume="1" data-track-index="0"></audio></div><script>window.__timelines=window.__timelines||{};window.__timelines.sampler=gsap.timeline({paused:true});</script></body></html>')
 (P/'hyperframes.json').write_text(json.dumps({'name':'old-valyria-style-sampler','skill':'hyperframes'},indent=2)+'\n')
 assets=[{'image':i,'source':manifest['shots'][i-1]['proxy'],'sha256':hashlib.sha256((P/f'assets/images/{i:04}.jpg').read_bytes()).hexdigest(),'prior_status':'UNAPPROVED_CANDIDATE_NOT_PUBLICATION_CLEARANCE'} for i in used]
 (P/'production/SAMPLER_MANIFEST.json').write_text(json.dumps({'duration':720,'fps':30,'chapters':chapters,'images':assets,'voice':'voice-01','status':'ASSEMBLY_NOT_FINAL_EXPORT','source_film_unchanged':True,'scope':'Representative styles, not every possible documentary mode. No real interviews, historical documents, external lore verification or scientific simulation claimed.'},indent=2)+'\n')
 (P/'production/DRIVE_STORAGE.json').write_text(json.dumps({'studio_folder_id':'1LqivhzEJWhvtnYrZ_pCfU-W1lv_kcWFS','studio_folder_url':'https://drive.google.com/drive/folders/1LqivhzEJWhvtnYrZ_pCfU-W1lv_kcWFS','sampler_folder_id':'17MM15rQBT-3nm7QJDxnUwtuXSIXN3yu6','sampler_folder_url':'https://drive.google.com/drive/folders/17MM15rQBT-3nm7QJDxnUwtuXSIXN3yu6','video_uploaded':False},indent=2)+'\n')
 (P/'production/REPO_COMPONENTS.md').write_text('# Repository design primitives\n\nReviewed and adapted titlecard-calm (fixed entrance/hold/outro), caption-editorial-emphasis (selective emphasis), beat-timeline (deterministic progressive reveals), and animated-bar-chart (labels remain attached to concepts). Source files remain in registry/components. This sampler uses custom Valyria-specific diagrams; no numeric data chart is fabricated to fill a technique slot. Maps are explicitly schematic; house nodes are conceptual. No online font or runtime CDN dependencies.\n')
 (P/'.gitignore').write_text('renders/\nassets/audio/\n')
 (P/'SPEC.md').write_text('# Old Valyria — Eight Documentary Languages\n\n720seconds,1920×1080,30fps; eight90second chapters. Each chapter:22second technique introduction,60seconds of the selected full-film narration,8second summary. Same selected voice-01. Short intro starts at1second. Four primary-verified Kevin MacLeod tracks and CC0 Kenney effects reused with credits. No original film edits. Full-film render paused after four completed100second segments; resuming requires same original command and --resume.\n\nPalette, typography, framing and diagram structure change by treatment. Labels identify the treatment and the limits of reconstruction. No fabricated interview, expert witness, manuscript, quotation from an unconsulted book, numeric dataset or geographic accuracy. Full lore/image/listening/publication approval is not implied. Captions on screen identify techniques, not word-aligned subtitles.\n\n## Delivery\n\n| Item | Location |\n|---|---|\n| Master render (full quality) | `renders/OLD_VALYRIA_STYLE_SAMPLER_12MIN_v01.mp4` |\n| Delivery encode,1080p (<100MB) | `renders/OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_1080p.mp4` |\n| Delivery encode,720p fallback | `renders/OLD_VALYRIA_STYLE_SAMPLER_12MIN_FINAL_720p.mp4` |\n| Editable project archive | `renders/OLD_VALYRIA_STYLE_SAMPLER_SOURCE_v01.zip` |\n| Viewer documents | `renders/sampler_drive_upload/` |\n| Export QA | `production/EXPORT_QA.json` |\n| Browser/craft checks | `production/BROWSER_CHECK.json` |\n| Sound measurements | `production/SOUND_MIX.json` |\n\nScripts: `scripts/episode-audit/build_valyria_sampler.py` (visuals/manifest),\n`mix_valyria_sampler.py` (soundtrack), `verify_valyria_sampler.py` (export QA),\n`encode_valyria_sampler.sh` (delivery encodes).\n\nThe35-minute full film is untouched: it remains paused with four completed100second\nsegments and the same original render command.\n')
 print(json.dumps({'project':str(P),'duration':720,'chapters':8,'images':len(used)},indent=2))

if __name__=='__main__':main()
