import json,sys,urllib.parse
sys.argv=['x','','[]']
exec(open('scan.py').read().split('subs=sys.argv')[0])
plan=json.load(open('plan.json'))
with open(OUT,'a') as f:
  for s,feed,qs in plan:
    if feed:
        code,body=fetch(f'https://www.reddit.com/r/{s}/.rss?limit=25'); label,items=parse(body)
        f.write(json.dumps({'sub':s,'kind':'feed','code':code,'label':label,'items':items})+'\n'); f.flush()
        if not items: continue
    for q in qs:
        code,body=fetch(f'https://www.reddit.com/r/{s}/search.rss?q={urllib.parse.quote(q)}&restrict_sr=1&sort=relevance&t=all&limit=25'); label,items=parse(body)
        f.write(json.dumps({'sub':s,'kind':'search','q':q,'code':code,'items':items})+'\n'); f.flush()
