import glob,re,sys,os
import xml.etree.ElementTree as ET
NS={'a':'http://www.w3.org/2005/Atom'}
S='/tmp/claude-0/-home-user-Shop-aufbau/5b2336da-6c1e-5391-be3e-77204cb3c276/scratchpad'
known=set(l.split('\t')[0] for l in open(S+'/candidates.tsv'))
raw=open('/home/user/Shop-aufbau/falunara-research/voc/voc1_raw_search_hits.md').read()
for f in sorted(glob.glob(S+'/search/*.xml')):
    if len(sys.argv)>1 and not any(a in f for a in sys.argv[1:]): continue
    try: r=ET.parse(f).getroot()
    except Exception as e: print('ERR',f); continue
    print('##',os.path.basename(f))
    for e in r.findall('a:entry',NS):
        u=e.find('a:link',NS).get('href'); i=u.split('/comments/')[1].split('/')[0]
        t=e.find('a:title',NS).text; d=e.find('a:updated',NS).text[:10]
        tag='C' if i in known else ('V' if i in raw else 'NEW')
        print(f"{tag}|{d}|{i}|{t[:120]}")
