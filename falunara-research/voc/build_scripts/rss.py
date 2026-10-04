import sys,subprocess,time,re,html
import xml.etree.ElementTree as ET
ns={'a':'http://www.w3.org/2005/Atom'}
def fetch(url):
    for i in range(3):
        r=subprocess.run(['curl','-s','-w','\n%{http_code}','-A','Mozilla/5.0 (X11; Linux x86_64) research',url],capture_output=True,text=True)
        body,code=r.stdout.rsplit('\n',1)
        if code=='200': return body
        print('HTTP',code,file=sys.stderr); time.sleep(25)
    return None
def clean(s):
    s=html.unescape(re.sub('<[^>]+>',' ',s or ''));return re.sub(r'\s+',' ',s).strip()
mode=sys.argv[1]
for url in sys.argv[2:]:
    b=fetch(url)
    if not b: print('FAIL',url);continue
    root=ET.fromstring(b)
    for e in root.findall('a:entry',ns):
        t=e.findtext('a:title',default='',namespaces=ns)
        l=e.find('a:link',ns).get('href')
        c=clean(e.findtext('a:content',default='',namespaces=ns))
        n=400 if mode=='s' else 1200
        print('##',t,'|',l); print(c[:n]); print()
    time.sleep(7)
