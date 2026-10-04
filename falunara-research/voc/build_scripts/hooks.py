import sys,re,collections
sys.path.insert(0,'/tmp/claude-0/-home-user-Shop-aufbau/5b2336da-6c1e-5391-be3e-77204cb3c276/scratchpad')
from pat import R,CAT
def first(x):
    b=(x.get('eff_body') or '').strip()
    l=b.split('\n')[0].strip()
    return l
def norm(s): return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()[:80]
def cc(x):
    try: return int(x['collation_count'])
    except: return 1
for key,fn in (('HOOK',first),('TITLE',lambda x:(x.get('eff_title') or '').strip())):
    g=collections.defaultdict(list)
    for x in R:
        if x['B'] not in CAT: continue
        h=fn(x)
        if len(h)<4: continue
        g[norm(h)].append(x)
    rows=[]
    for k,L in g.items():
        brands=set(z['B'] for z in L); pages=set(z['page_name'].strip() for z in L)
        mx=max(L,key=lambda z:z['D'])
        rows.append((len(L),mx['D'],k,L,brands,pages,mx))
    print('#####',key)
    for n,d,k,L,brands,pages,mx in sorted(rows,key=lambda r:(-(r[0]>=3 or r[1]>=60), -r[0]))[:70]:
        if n<3 and d<90: continue
        print(f"{n} IDs | {'/'.join(brands)} | pages {len(pages)}: {';'.join(sorted(pages))[:80]} | earliest {min(z['start_date'] for z in L)} | max {d}d ({mx['ad_archive_id']}, start {mx['start_date']}, active {mx['ACT']}) | live {sum(z['ACT'] for z in L)} | collation sum {sum(cc(z) for z in L)} | max coll {max(cc(z) for z in L)}")
        print('    >>',fn(mx)[:260])
