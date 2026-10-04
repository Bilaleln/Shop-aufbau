import re,sys
from norm import *
d=load()
for pat in sys.argv[1:]:
    rx=re.compile(pat,re.I)
    m=[r for r in d if rx.search(r['Exact short quote'])]
    print(f"\n### {pat}: {len(m)} rows / {len({r['Corpus ID'] for r in m})} thr / {len({r['Community'] for r in m})} comm")
    for r in m[:int(__import__('os').environ.get('N','8'))]: print(' ',r['VOC ID'],r['Evidence strength'][0],r['Flags'][:12],'|',r['Exact short quote'][:150])
