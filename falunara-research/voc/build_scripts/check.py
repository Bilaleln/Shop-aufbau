from items import *
for grp in [DESIRES,PROBLEMS,OBJECTIONS,FAILED,TRIGGERS,PATTERNS]:
    for it in grp:
        rows=sel(it['f']); ex=examples(it,rows)
        print(f"{rec(rows):45s} {label(rows):22s} {conf(rows):7s} {it['name'][:70]}")
        for c in it.get('counter',[]): assert c in BYID,c
    print()
for a,b,c,_ in CONTRA:
    for i in b+c: assert i in BYID, i
for i in CURATED: assert i in BYID,i
print(len(CURATED)); print('\n'.join(WARN))
