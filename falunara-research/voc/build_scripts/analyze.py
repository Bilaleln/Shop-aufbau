import re, sys, html, glob, json, os
import xml.etree.ElementTree as ET
NS={'a':'http://www.w3.org/2005/Atom'}
C='/home/user/Shop-aufbau/falunara-research/voc/thread_cache'
def clean(s):
    s=html.unescape(s or '')
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
    s=re.sub(r'\s+',' ',s).strip()
    s=s.replace('submitted by /u/','[by] ')
    return s
BODY=re.compile(r"\b(body|arms?|legs?|shins?|knees?|elbows?|hands?|thighs?|chest|d[eé]collet|neck|feet|back|stomach|belly|butt|forearms?|calves|all over|shower)\b",re.I)
FP=re.compile(r"\b(I|I'm|I've|my|me|mine)\b")
AGE=re.compile(r"\b(?:I'?m|I am|age[d]?|turned|turning|at)\s+(\d{2})\b|\b(\d{2})\s?(?:F|f|yo|y/o|yrs?|years? old)\b|\b(?:in my|my)\s+(?:early |mid |late |mid-)?(\d0)s\b")
UK=re.compile(r"\b(Boots|Superdrug|Tesco|Sainsbury|NHS|£|Mumsnet|Holland & Barrett|Aldi UK)\b")
US=re.compile(r"\b(Target|Walmart|CVS|Walgreens|Costco|Ulta|TJ ?Maxx|Marshalls|Trader Joe|\$\d)")
def an(id):
    t=ET.parse(f'{C}/{id}.xml').getroot()
    title=t.find('a:title',NS).text or ''
    title=re.sub(r' : [^:]+$','',title)
    es=t.findall('a:entry',NS)
    out=[]
    for e in es:
        a=e.find('a:author/a:name',NS); a=a.text if a is not None else ''
        c=clean(e.find('a:content',NS).text if e.find('a:content',NS) is not None else '')
        u=e.find('a:updated',NS); u=u.text[:10] if u is not None else ''
        out.append((a,u,c))
    return title,out
if __name__=='__main__':
    ids=sys.argv[1:]
    for id in ids:
        if not os.path.exists(f'{C}/{id}.xml'): print(id,'NOCACHE'); continue
        title,es=an(id)
        if not es: print(id,'EMPTY',title); continue
        op=es[0]; comments=es[1:]
        txt=' '.join(c for _,_,c in es)
        ages=sorted(set(x for m in AGE.findall(txt) for x in m if x and 18<=int(x)<=85))
        fp=len(FP.findall(txt)); body=len(BODY.findall(txt))
        clen=sum(len(c) for _,_,c in comments)
        print(f"=== {id} | {title} | OP {op[0]} {op[1]} | comments={len(comments)} chars={clen} fp={fp} body={body} ages={ages} UK={UK.findall(txt)[:3]} US={US.findall(txt)[:3]}")
        print('OP:',op[2][:700])
        for a,u,c in comments[:int(os.environ.get('NC','4'))]:
            print('  -',c[:220])
