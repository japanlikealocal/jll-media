import subprocess
from playwright.sync_api import sync_playwright
CSS=open('/home/claude/reel2/make.py').read().split('CSS = """')[1].split('"""')[0]
BR='<div class="brand"><div class="jp">JP</div>Japan Like a Local</div>'
reels={
 "taxis":{"tag":"TAXIS","h1":"Taking a taxi in Japan?","sub":"3 things to know 👇","items":[
   ("Automatic door","The driver often opens and closes the rear left door. If it opens automatically, don&rsquo;t open or close it yourself."),
   ("Show your destination","Show the address or place name in Japanese to help the driver understand where you want to go."),
   ("Payment","Many taxis accept credit cards or transit IC cards, but not all. Check before you get in.")],
   "end":"Rules vary by area and company.","D":[3.0,5.5,5.5,5.0,4.0]},
 "konbini":{"tag":"CONVENIENCE STORES","h1":"First time at a Japanese konbini?","sub":"3 things to know 👇","items":[
   ("Hot food at the counter","Fried chicken and other hot snacks are often sold near the register."),
   ("\"Warm it up?\"","Staff may ask if you want food heated. You can nod to say yes."),
   ("ATMs inside","Many stores have ATMs. Check if your card is accepted.")],
   "end":"Services vary by store.","D":[3.0,4.5,4.5,4.5,4.0]},
 "shrines":{"tag":"SHRINES &amp; TEMPLES","h1":"Visiting a shrine or temple?","sub":"3 things to know 👇","items":[
   ("Purification fountain","If available, follow the posted instructions for rinsing your hands and mouth. Don&rsquo;t touch the ladle to your mouth."),
   ("Photos","Some areas don&rsquo;t allow photos. Check the signs before taking pictures."),
   ("Shoes","You may be asked to remove your shoes before entering some halls or buildings.")],
   "end":"Customs vary by place.","D":[3.0,6.0,4.5,4.5,4.0]},
}
with sync_playwright() as p:
  b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
  for k,r in reels.items():
    slides=[f'<div class="safe"><div class="tag">{r["tag"]}</div><h1>{r["h1"]}</h1><div class="sub">{r["sub"]}</div></div>']
    for i,(t,dd) in enumerate(r["items"],1):
      slides.append(f'<div class="safe"><div class="num">{i}</div><div class="t">{t}</div><div class="d">{dd}</div></div>')
    slides.append(f'<div class="safe"><div class="tag">BEFORE YOU GO</div><h1 style="font-size:96px">{r["end"]}</h1><div class="cta">Save this for your trip!<br>Free 1-page<br>Japan Quick Start:<br>link in bio</div></div>')
    for n,s in enumerate(slides):
      pg.set_content(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="top"></div>{BR}{s}</body></html>')
      pg.screenshot(path=f'{k}_s{n}.png')
    with open(f'{k}_list.txt','w') as f:
      for i,x in enumerate(r["D"]): f.write(f"file '{k}_s{i}.png'\nduration {x}\n")
      f.write(f"file '{k}_s4.png'\n")
  b.close()
for k,r in reels.items():
  subprocess.run(['ffmpeg','-y','-f','concat','-safe','0','-i',f'{k}_list.txt','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-t',str(sum(r["D"])),'-vf','fps=30,format=yuv420p','-c:v','libx264','-profile:v','high','-crf','20','-g','60','-c:a','aac','-b:a','128k','-use_editlist','0','-movflags','+faststart',f'{k}-reel-v2.mp4'],check=True,capture_output=True)
  subprocess.run(['ffmpeg','-v','error','-y']+sum([['-i',f'{k}_s{i}.png'] for i in range(5)],[])+['-filter_complex',''.join(f'[{i}]scale=432:-1[a{i}];' for i in range(5))+''.join(f'[a{i}]' for i in range(5))+'hstack=5','-frames:v','1',f'{k}-reel-v2-all-slides.png'],check=True)
