import builtins
exec(open('build.py').read().split('# ====================== XLSX')[0])
for it in PH: print(f"{rec(it['rows']):42s} {it['name'][:50]:50s} {it['exids']}")
for t,rs in ISO: print('ISO',t,rec(rs))
for grp in (DS,PS,OS,FS,TS):
    for it in grp: print(it['exids'], it['name'][:50])
