from norm import *
from collections import Counter,defaultdict
d=load()
by=defaultdict(list)
for r in d:
    for t in r['tags']: by[t].append(r)
rank={'high':0,'medium':1,'low':2}
out=open('cands.txt','w')
for t,rows in sorted(by.items(),key=lambda x:-len(x[1])):
    if len(rows)<6: continue
    th=len({r['Corpus ID'] for r in rows}); cm=len({r['Community'] for r in rows})
    out.write(f"\n## {t}: {len(rows)} rows / {th} thr / {cm} comm | cats {Counter(r['Category'] for r in rows).most_common(4)}\n")
    seen=Counter(); k=0
    for r in sorted(rows,key=lambda r:(rank[r['Evidence strength']],len(r['flags']))):
        if 'possible_seeding' in r['flags'] or seen[r['Corpus ID']]>=1: continue
        seen[r['Corpus ID']]+=1; k+=1
        out.write(f"{r['VOC ID']} [{r['Evidence strength'][0]}{','.join(f[:3] for f in r['flags'])}|{r['Stated age']}|{r['Category'][:12]}] {r['Exact short quote'][:160]}\n")
        if k>=14: break
