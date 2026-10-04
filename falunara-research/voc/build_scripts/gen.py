import csv, re, html, json, os
import xml.etree.ElementTree as ET
NS={'a':'http://www.w3.org/2005/Atom'}
S='/tmp/claude-0/-home-user-Shop-aufbau/5b2336da-6c1e-5391-be3e-77204cb3c276/scratchpad'
C='/home/user/Shop-aufbau/falunara-research/voc/thread_cache'
CAT={'PROB':'Problem description','EMO':'Emotional impact','OUT':'Desired outcomes','SOL':'Attempted solutions / product experiences','OBJ':'Objections / side effects / skepticism','ROUT':'Routines / application habits','CRIT':'Purchase criteria (texture, absorption, scent, price)','AGE':'Age / menopause context'}
ORDER=['40PlusSkinCare','45PlusSkincare','30PlusSkinCare','Menopause','Perimenopause','SkincareAddiction','SkincareAddicts','Skincare_Addiction','beauty','AskWomenOver40','AskWomenOver30','Sephora','Ulta','TwoXChromosomes','tretinoin','AskOldPeople','xxfitness','AskDocs','Inspire']
def meta(id):
    r=ET.parse(f'{C}/{id}.xml').getroot()
    sub=r.find('a:category',NS).get('term')
    ft=r.find('a:title',NS).text
    suf=' : '+sub
    title=ft[:-len(suf)] if ft.endswith(suf) else ft
    es=r.findall('a:entry',NS)
    op=es[0]
    url=op.find('a:link',NS).get('href')
    pub=op.find('a:published',NS); pub=(pub if pub is not None else op.find('a:updated',NS)).text[:10]
    return dict(sub=sub,title=title,url=url,date=pub,ncom=len(es)-1)
rows=[]; excl=[]
for line in open(S+'/decisions.tsv',encoding='utf-8'):
    p=line.rstrip('\n').split('\t')
    if len(p)<7: p+=['']*(7-len(p))
    id,dec,score,topic,why,cats,notes=p[:7]
    if id.startswith('inspire_'):
        m=json.load(open(S+'/inspire_meta.json'))[id]
    else:
        m=meta(id)
    d=dict(id=id,dec=dec,score=int(score),topic=topic,why=why,cats=cats,notes=notes,**m)
    (rows if dec=='I' else excl).append(d)
rows.sort(key=lambda d:(ORDER.index(d['sub']) if d['sub'] in ORDER else 99,-d['score'],d['date']))
out=[]
for n,d in enumerate(rows,1):
    platform='Inspire.com' if d['sub']=='Inspire' else 'Reddit'
    comm=d.get('community') or ('r/'+d['sub'])
    cats='; '.join(CAT[c] for c in d['cats'].split(';') if c)
    notes=(d['notes']+'; ' if d['notes'] else '')+f"Comments/replies retrieved: {d['ncom']}"
    out.append(dict(ID=f'C{n:03d}',Platform=platform,Community=comm,**{'Thread title':d['title'],'URL':d['url'],'Date if available':d['date'],'Topic':d['topic'],'Why relevant':d['why'],'Expected VOC categories':cats,'Quality score':d['score'],'Notes':notes},_id=d['id']))
json.dump(dict(rows=out,excl=excl),open(S+'/gen_out.json','w'),ensure_ascii=False,indent=0)
F=['ID','Platform','Community','Thread title','URL','Date if available','Topic','Why relevant','Expected VOC categories','Quality score','Notes']
with open('/home/user/Shop-aufbau/falunara-research/voc/VOC2_URL_Corpus.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=F,extrasaction='ignore'); w.writeheader(); [w.writerow(r) for r in out]
print(len(out),'included',len(excl),'excluded')
from collections import Counter
print(Counter(r['Community'] for r in out)); print(Counter(r['Quality score'] for r in out))
