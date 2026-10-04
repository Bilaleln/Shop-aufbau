import json,re,sys
kw=r"sleeve|tank|shorts|swim|bikini|summer|winter|mirror|photo|picture|husband|partner|touch|wedding|dress|embarrass|ashamed|shame|sad|depress|hate|cry|horrif|shock|overnight|suddenly|old lady|grandma|my mother|mom|confiden|feel like|myself|sexy|feminin|accept|grace|give up|resign|frustrat|angry|devastat|smooth|soft|glow|ritual|self.care|oil|hide|cover|cardigan|knees|chest|décolleté|decollete|elbow|lizard|alligator|crocodile|tissue|paper|crinkl|happy|love it|holy grail|compliment|scaly|itch"
for f in sys.argv[1:]:
  d=json.load(open(f))
  for k,v in d.items():
    print('\n#####',k,len(v))
    for e in v:
      t=e['text'].replace('submitted by','|')
      sents=re.split(r'(?<=[.!?])\s+',t)
      hits=[s for s in sents if re.search(kw,s,re.I) and len(s)<400]
      if hits: print('*',e['url'].split('/comments/')[1][:60],'::',' // '.join(hits)[:900])
