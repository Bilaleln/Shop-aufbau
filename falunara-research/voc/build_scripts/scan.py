import subprocess, time, json, re, sys, urllib.parse, xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) research'
NS={'a':'http://www.w3.org/2005/Atom'}
OUT='/tmp/claude-0/-home-user-Shop-aufbau/5b2336da-6c1e-5391-be3e-77204cb3c276/scratchpad/results.jsonl'
def fetch(url):
    for attempt in range(12):
        time.sleep(8)
        r=subprocess.run(['curl','-sS','-L','-A',UA,'-w','\n%{http_code}',url],capture_output=True,text=True)
        body,_,code=r.stdout.rpartition('\n')
        if code=='429' or (code=='200' and not body.strip()):
            time.sleep(45); continue
        return code,body
    return 'fail',''
def parse(body):
    try: root=ET.fromstring(body)
    except Exception: return None,[]
    cat=root.find('a:category',NS)
    label=cat.get('label') if cat is not None else None
    items=[]
    for e in root.findall('a:entry',NS):
        t=e.findtext('a:title',default='',namespaces=NS)
        l=e.find('a:link',NS); u=l.get('href') if l is not None else ''
        d=e.findtext('a:updated',default='',namespaces=NS) or e.findtext('a:published',default='',namespaces=NS)
        items.append({'title':t,'url':u,'date':d[:10]})
    return label,items
subs=sys.argv[1].split(',')
queries=json.loads(sys.argv[2])
with open(OUT,'a') as f:
    for s in subs:
        code,body=fetch(f'https://www.reddit.com/r/{s}/.rss?limit=25')
        label,items=parse(body)
        f.write(json.dumps({'sub':s,'kind':'feed','code':code,'label':label,'items':items})+'\n'); f.flush()
        if not items: continue
        for q in queries:
            url=f'https://www.reddit.com/r/{s}/search.rss?q={urllib.parse.quote(q)}&restrict_sr=1&sort=relevance&t=all&limit=25'
            code,body=fetch(url)
            label,items=parse(body)
            f.write(json.dumps({'sub':s,'kind':'search','q':q,'code':code,'items':items})+'\n'); f.flush()
