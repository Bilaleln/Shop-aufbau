import subprocess,sys,json
def build(out,clips,w=1080,h=1920,xf=0.4):
    ins=[];f=[]
    for i,(c,ss,dur) in enumerate(clips):
        ins+=['-ss',str(ss),'-t',str(dur),'-i',f'gen/{c}.mp4']
        f.append(f'[{i}:v]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps=24,format=yuv420p,setsar=1[s{i}]')
    prev='s0';t=clips[0][2]
    for i in range(1,len(clips)):
        off=t-xf; f.append(f'[{prev}][s{i}]xfade=transition=fade:duration={xf}:offset={off:.3f}[x{i}]'); prev=f'x{i}'; t=off+clips[i][2]
    f.append(f'[{prev}]fade=t=in:st=0:d=0.3,fade=t=out:st={t-0.5:.3f}:d=0.5[v]')
    cmd=['ffmpeg','-v','error','-y']+ins+['-filter_complex',';'.join(f),'-map','[v]','-an','-pix_fmt','yuv420p','-c:v','libx264','-preset','slow','-crf','22','-profile:v','high','-movflags','+faststart',out]
    subprocess.run(cmd,check=True); print(out,round(t,2),'s')
V1=[('v1_c1',0,2.4),('v1_c2',0,4),('v1_c3',0,3.5),('v1_c4',0,3),('v1_c5',0,3),('v1_c6',0,4),('v1_c7',0,3)]
build('final/fadilal-product-demo.mp4',V1)
build('final/fadilal-product-demo-4x5.mp4',V1,1080,1350)
build('final/fadilal-evening-ritual.mp4',[('v2_c1',0,5),('v2_c2',0,4),('v2_c3',0,5)],xf=0.6)
build('final/fadilal-ugc-demo.mp4',[('v3_c1',0,5),('v3_c2',0,5)],xf=0.3)
