import re,csv
md=open('/home/user/Shop-aufbau/falunara-research/voc/VOC3_Deep_Reddit_VOC_Research.md',encoding='utf-8').read()
d={r['VOC ID']:r for r in csv.DictReader(open('/home/user/Shop-aufbau/falunara-research/voc/VOC3_raw_merged.csv',encoding='utf-8'))}
ids=re.findall(r'\u201c \(([ABC]\d{4})\)',md)
def form(i):
    s=d[i]['Exact short quote'].replace('|','\\|').replace('\n','<br>')
    return '\u201e'+s+'\u201c ('+i+')'
bad=[i for i in set(ids) if form(i) not in md]
print(len(ids),len(set(ids)),'bad',bad)
for i in re.findall(r'\| \d+ \| ([ABC]\d{4}) \|',md): assert d[i]['Exact short quote'] in md
# links point to correct url
for i,u in re.findall(r'\[([ABC]\d{4})\]\((\S+?)\)',md): assert d[i]['Source URL']==u,(i)
print('ok')
