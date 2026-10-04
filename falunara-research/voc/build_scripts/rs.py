import sys,time,subprocess,urllib.parse,xml.etree.ElementTree as ET,re,html,json
NS={'a':'http://www.w3.org/2005/Atom'}
def get(url):
    for i in range(3):
        r=subprocess.run(['curl','-sS','-A','Mozilla/5.0 (X11; Linux x86_64) research','-w','\n%{http_code}',url],capture_output=True,text=True)
        body,code=r.stdout.rsplit('\n',1)
        if code=='200': return body
        print('HTTP',code,url,file=sys.stderr); time.sleep(25)
    return None
def strip(s): return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',s or ''))).strip()
def parse(x):
    out=[]
    try: root=ET.fromstring(x)
    except Exception as e: return out
    for e in root.findall('a:entry',NS):
        t=e.find('a:title',NS); l=e.find('a:link',NS); c=e.find('a:content',NS)
        out.append({'title':t.text if t is not None else '','url':l.get('href') if l is not None else '','text':strip(c.text if c is not None else '')})
    return out
mode=sys.argv[1]
items=json.loads(sys.argv[2])
res={}
for it in items:
    if mode=='search':
        sub,q=it
        url=f"https://www.reddit.com/r/{sub}/search.rss?q={urllib.parse.quote(q)}&restrict_sr=1&sort=relevance&t=all&limit=25"
    else:
        url=it.rstrip('/')+'/.rss?limit=100'
    x=get(url); res[str(it)]=parse(x) if x else []
    time.sleep(12)
json.dump(res,open(sys.argv[3],'w'),indent=1)
for k,v in res.items():
    print('==',k,len(v))
    for e in v[:25]: print(' -',e['title'][:100],'|',e['url'])
