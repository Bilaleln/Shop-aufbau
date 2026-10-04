import json,re,collections,sys
R=[json.loads(l) for l in open('/home/user/Shop-aufbau/falunara-research/ad_intelligence/raw/_master_meta.jsonl')]
def brand(x):
    b=x.get('brand') or ''; p=x['page_name'].strip(); d=x.get('domain') or ''
    if not b:
        if p.startswith('Over 40'): return 'Goda'
        if p=='Evora Body': return 'Evora'
        if p in ('Joanna Woodley','Fiona Hughes','Claudia Neumann','Margaret Amer','Monica Ravichandran'): return 'UnknownSeeding'
        return 'other:'+p
    if b.startswith('Evora'): return 'Evora'
    if b=='instagram.com': return 'Evora' if p=='Daily Discounts' else p
    if b=='theskincareinsider.com': return 'Miami MD'
    if 'feline' in b: return 'Feline Skinscience'
    if 'emilycarter' in b: return 'EmilyCarter/Cellu'
    if b=='norseorganics.co': return 'Frøya Organics'
    if 'shopeverly' in b: return 'shopeverly'
    return b
for x in R:
    x['B']=brand(x)
    if x['B']=='Goda' and re.search(r'goda-for-h|/perfume|/him',x.get('eff_link') or ''): x['B']='Goda-Perfume'
    if x['B'] in ('Miami MD','Feline Skinscience'): x['B']='MiamiMD+Feline'
    try: x['D']=int(x['days_running'])
    except: x['D']=0
    x['ACT']=str(x['is_active'])=='True' or str(x.get('end_date',''))>='2026-10-02'
    x['T']=' '.join([x.get('eff_title') or '',x.get('eff_body') or '',x.get('link_description') or '']).replace('’',"'")
CAT={'Evora','Goda','NØRD BODY','Besque','VitaeCharm','DRMTLGY','MiamiMD+Feline','OSEA','Frøya Organics','Saeskyn','TurmSkin','Remedy Skin','Beekman 1802','Beauty From Bees','EmilyCarter/Cellu','theskinmag.com','tryorgatics.com','Nécessaire','UnknownSeeding','Vitality Extracts'}
P=dict(
crepey=r'crep(e|ey|iness|ey)|creepy',
water_evap=r'(\d+\s*(%|percent|to \d+ percent)\s*water|mostly water|evaporat|sits? on (top|the surface)|sitting on top)',
deep_lipid=r'lipid barrier|absorbs? deep|penetrat|reach(es)? (deeper|where)|deeper layer|sinks? (right )?in|melts? (into|through|in)',
stopped_making=r'stopped (making|producing)|no longer (makes|produces)|(skin|body) (makes|produces) less',
hide_sleeveless=r'sleeveless|long sleeves|short sleeves|wearing shorts|in shorts|cardigan|cover(ing)? (up|my arms)|swimsuit|bathing suit|hid(e|ing) (my|your) (arms|legs)|tank top',
menopause=r'menopaus',
glp1=r'glp-?1|ozempic|wegovy|mounjaro|zepbound|weight loss|lost (the )?weight|losing weight|lost \d+ (lbs|pounds)',
guarantee=r'money[- ]back|risk[- ]free|guarantee',
pct_off=r'\d+\s?%\s?off|\d+% de descuento',
bogo=r'buy \d+,? get \d+|bogo|buy one get',
scarcity=r'sold out|selling out|almost gone|only \d+ left|stock|ends (tonight|midnight|today)|until midnight|last chance|restock',
deadline=r'midnight|ends today|ends tonight|last chance|limited time|today only',
free_gift=r'free gift',
subscription=r'subscri|auto-?ship',
confession=r'get fired|lose this job|not proud|i stole|nobody (wants|warns)|i need to tell you|i\'m not supposed',
rewind=r'let me (rewind|back up|tell you the story|explain)',
insider=r'\b(nanny|butler|chauffeur|caregiver|tour guide|giving tours|spa owner|own a day spa|massage therapist|cabin attendant|vacation rental|delivery driver|flight attendant|esthetician|aesthetician|formulator)\b',
luxury=r'ritz|aman |yacht|first class|biltmore|hamptons|cruise|five-star|5-star|7-star|billionaire|wealthiest|richest|private island|\$\d,\d{3} a night',
derm=r'dermatolog|\bderm\b|harvard',
clinical_stat=r'\d+(\.\d+)?\s?%\s?(of (women|users|participants)|saw|said|reported|experienced|reduction|agreed|noticed|improvement)',
self_age=r"\b(i'm|i am|at|turned) (4[5-9]|5\d|6\d|7\d)\b",
over_age=r'over (40|45|50|55|60)|in (their|your|my) (40s|50s|60s)|after (40|50|60)|women (40|50)\+|50\+',
husband=r'husband',
family_compare=r'my (mother|mom|daughter|sister|grandma|grandmother)|mom\'s|her mom',
myth_wrong=r'doing it all wrong|myth|lotion lie|the real reason|nothing to do with|scam|don\'t actually work|isn\'t working|aren\'t working|never worked|doesn\'t work|don\'t work',
comparison=r'top 5|top five|ranked|#1 (body|choice)|tested \d|side by side|side-by-side|comparison|i tested',
time_box=r'\b\d+\s?(days|weeks|week)\b|two minutes|2 minutes|two pumps|30 days|overnight',
cold_pressed=r'cold[- ]pressed',
peptide=r'peptide',
retinol=r'retin',
collagen=r'collagen',
nongreasy=r'non[- ]greasy|not greasy|no greasy|without the grease|absorbs (fast|quickly|in seconds|instantly)|never greasy',
natural=r'botanical|100% natural|all[- ]natural|plant[- ]based|clean',
quote_open=r'^\s*["“]',
question_open=r'^\s*[^.!\n]{5,140}\?',
bruise=r'bruis',
)
def run(names=None,show=False):
    out={}
    for k,pat in P.items():
        if names and k not in names: continue
        rx=re.compile(pat,re.I|re.M)
        hits=[x for x in R if x['B'] in CAT and (rx.search(x['T'] if k not in('quote_open','question_open') else (x.get('eff_body') or '')))]
        byb=collections.defaultdict(list)
        for x in hits: byb[x['B']].append(x)
        s=[]
        for b,L in sorted(byb.items(),key=lambda z:-len(z[1])):
            mx=max(L,key=lambda z:z['D'])
            s.append(f"{b}:{len(L)}(pg{len(set(z['page_name'] for z in L))},max{mx['D']}d id{mx['ad_archive_id']},≥60d:{sum(z['D']>=60 for z in L)},≥90d:{sum(z['D']>=90 for z in L)},live:{sum(z['ACT'] for z in L)})")
        print(f"== {k}: {len(hits)} ads / {len(byb)} brands; brands w/≥60d: {sum(any(z['D']>=60 for z in L) for L in byb.values())}; w/≥90d: {sum(any(z['D']>=90 for z in L) for L in byb.values())}")
        print('   '+' | '.join(s))
if __name__=='__main__': run()
