import re,html,sys
s=open(sys.argv[1],encoding='utf8',errors='ignore').read()
s=re.sub(r'(?s)<(script|style|svg|noscript)[^>]*>.*?</\1>',' ',s)
t=html.unescape(re.sub(r'<[^>]+>','\n',s))
out=[];prev=None
for l in t.split('\n'):
  l=l.strip()
  if l and l!=prev and len(l)>2: out.append(l)
  prev=l
txt='\n'.join(out)
kw=sys.argv[2:] 
print(txt[:int(kw[0])] if kw else txt[:5000])
