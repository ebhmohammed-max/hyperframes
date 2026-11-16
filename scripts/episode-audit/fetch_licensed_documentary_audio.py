import subprocess,json,pathlib,hashlib,concurrent.futures,urllib.parse
D=pathlib.Path('projects/ancient_world_of_ice_and_fire/episodes/ep001_rise_of_old_valyria/documentary_film')
out=D/'assets/audio/licensed';out.mkdir(parents=True,exist_ok=True)
p=D/'production/audio_licenses';p.mkdir(parents=True,exist_ok=True)
sha='cf011c7016595833b550a88ff127f089188b25f8';ks='b7729283e47d38f203d85560cfda5b2c1fd6fc7e'
items=[]
for path,name,isrc in [('Epic/Ancient Rite.mp3','ancient-rite.mp3','USUAN1900048'),('Epic/Night Vigil.mp3','night-vigil.mp3','USUAN1900047'),('Miscellaneous/Mana Two - Part 1.mp3','mana-two-part-1.mp3','USUAN1900036'),('Miscellaneous/Ancient Winds [1⧸6].mp3','ancient-winds-part-1.mp3','USUAN1900043')]:
 items.append(dict(repository='0lhi/FreePD',revision=sha,path=path,file=name,license='CC-BY-4.0',author='Kevin MacLeod',primary_source='https://incompetech.com/music/royalty-free/index.html?isrc='+isrc))
for name in ['bookOpen','bookFlip1','cloth1','footstep00','footstep01','footstep02','footstep03','metalLatch','handleCoins','creak1']:
 items.append(dict(repository='ismetcabbar9-oss/kenney-audio-assets',revision=ks,path='Audio (295 files)/RPG sounds (50 sounds)/'+name+'.ogg',file=name+'.ogg',license='CC0-1.0',author='Kenney',primary_source='https://kenney.nl/assets/rpg-audio'))
def dl(a):
 target=out/a['file']; endpoint='repos/'+a['repository']+'/contents/'+urllib.parse.quote(a['path'],safe='/')+'?ref='+a['revision']
 with target.open('wb') as f: subprocess.run(['gh','api',endpoint,'-H','Accept: application/vnd.github.raw+json'],stdout=f,check=True)
 a['sha256']=hashlib.sha256(target.read_bytes()).hexdigest();a['bytes']=target.stat().st_size;a['local_path']=str(target.relative_to(D));a['mirror_source']='https://github.com/'+a['repository']+'/blob/'+a['revision']+'/'+urllib.parse.quote(a['path'],safe='/')
 print(a['file'],a['bytes'],flush=True)
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(dl,items))
for repo,rev,file in [('0lhi/FreePD',sha,'LICENSE'),('ismetcabbar9-oss/kenney-audio-assets',ks,'LICENSE.md'),('ismetcabbar9-oss/kenney-audio-assets',ks,'README.md')]:
 with (p/(repo.split('/')[0]+'-'+file)).open('wb') as f:subprocess.run(['gh','api',f'repos/{repo}/contents/{file}?ref={rev}','-H','Accept: application/vnd.github.raw+json'],stdout=f,check=True)
(p/'ASSET_REGISTER.json').write_text(json.dumps(dict(retrieved_utc='2026-11-15',assets=items,notes=['Music conservatively credited under composer-confirmed CC BY 4.0, not solely mirror CC0 declaration.','Ancient Winds part 1 is an excerpt of the longer composition.','Commercial synchronized video use allowed by listed licenses; no guarantee against erroneous Content ID claims.']),indent=2)+'\n')
