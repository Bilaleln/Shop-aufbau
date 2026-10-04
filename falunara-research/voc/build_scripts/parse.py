import re,html,sys,json,os
import xml.etree.ElementTree as ET
base='/home/user/Shop-aufbau/falunara-research/voc/thread_cache/'
mp={}
ids=['10h8dgw','10p4w6s','1bzw7lc','1d2qhua','1ka0x6t','1nt3nlq','1d3lf3m','1jocpbh','1kkbxtg','1l9q1e2','1n0taq6','1kgdnjc','1lwdvsg','1m1b7ig','1ti4ysg','1jsf80m','1nfkepq','m78e8v','14cn06o','1pg9y2o','1dhgg35','1ar1zbc','1qfgegt','1td3ff8','1t5ys67','1r8m0yr','1ukz2dt','m540tj']
for i,t in enumerate(ids): mp['C%03d'%(61+i)]=t+'.xml'
mp['C089']='inspire_itchy-all-over-1.html'
mp['C090']='inspire_skin-sagging-more-than-just-age-no-weight-gain-or-loss.html'
def clean(s):
    s=re.sub(r'<br\s*/?>|</p>|</li>',' \n',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    return s
def norm(s):
    s=html.unescape(s)
    s=s.replace('’',"'").replace('‘',"'").replace('“','"').replace('”','"').replace('—','-').replace('–','-').replace('\xa0',' ')
    return re.sub(r'\s+',' ',s).strip().lower()
def entries(cid):
    f=base+mp[cid]
    raw=open(f,encoding='utf-8').read()
    out=[]
    if f.endswith('.xml'):
        ns={'a':'http://www.w3.org/2005/Atom'}
        root=ET.fromstring(raw)
        for e in root.findall('a:entry',ns):
            a=e.find('a:author/a:name',ns); a=a.text if a is not None else ''
            l=e.find('a:link',ns).get('href')
            c=e.find('a:content',ns); c=c.text or '' if c is not None else ''
            c=re.sub(r'submitted by.*$','',c,flags=re.S) if '[link]' in c else c
            out.append((a,l,clean(c)))
    else:
        out.append(('','',clean(raw)))
    return out
if __name__=='__main__':
    for cid in mp:
        with open('c/%s.txt'%cid,'w') as fo:
            for n,(a,l,c) in enumerate(entries(cid)):
                fo.write('#%d %s %s\n%s\n\n'%(n,a,l,re.sub(r'[ \t]+',' ',re.sub(r'\n\s*\n+','\n',c)).strip()))
