import json,os,sys,subprocess
out={}
if os.path.exists('kup.json'): out=json.load(open('kup.json'))
for p in sys.argv[1:]:
    n=os.path.basename(p)
    if n in out: continue
    r=subprocess.run(['curl','-sS','-X','POST','https://kieai.redpandaai.co/api/file-stream-upload','-H','Authorization: Bearer '+os.environ['KIE_API_KEY'],'-F',f'file=@{p}','-F','uploadPath=fadilal','-F',f'fileName={n}'],capture_output=True,text=True)
    d=json.loads(r.stdout)
    if d.get('code')!=200: print('FAIL',n,d.get('msg')); continue
    out[n]=d['data']['downloadUrl']; print('ok',n)
    json.dump(out,open('kup.json','w'),indent=1)
