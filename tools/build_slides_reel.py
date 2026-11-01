# Turn 4:5 carousel slides into a vertical reel (each slide ~2.6s on blurred bg). Carousels get ~0 reach at 0 followers.
import pathlib,subprocess,sys
R=pathlib.Path(__file__).resolve().parent.parent
src=sorted((R/'assets/carousel-onsen').glob('onsen-*.jpg')); out=R/'reels/2026-11-02-onsen-steps-reel.mp4'
D=2.6; inputs=[]; parts=[]
for i,p in enumerate(src):
    inputs+=['-loop','1','-t',str(D),'-i',str(p)]
    parts.append(f"[{i}]split[a{i}][b{i}];[a{i}]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3,eq=brightness=-0.15[bg{i}];"
                 f"[b{i}]scale=1080:1350,zoompan=z='1+0.03*on/{int(D*30)}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={int(D*30)}:s=1080x1350:fps=30[fg{i}];"
                 f"[bg{i}]fps=30[bgf{i}];[bgf{i}][fg{i}]overlay=0:285:shortest=1,format=yuv420p,setsar=1[v{i}]")
n=len(src)
fc=';'.join(parts)+';'+''.join(f'[v{i}]' for i in range(n))+f'concat=n={n}:v=1:a=0[v]'
subprocess.run(['ffmpeg','-y',*inputs,'-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-filter_complex',fc,'-map','[v]','-map',f'{n}:a',
  '-t',str(D*n),'-c:v','libx264','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-movflags','+faststart',str(out)],check=True,capture_output=True)
print('ok',out.name,D*n)
