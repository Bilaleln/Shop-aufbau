"""Select ads for the swipe ledger from raw/_master_meta.jsonl -> raw/_ledger_selection.jsonl"""
import json, re, collections, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
rows = [json.loads(l) for l in open(D + "/raw/_master_meta.jsonl")]
def norm(t): return re.sub(r'[^a-z0-9 ]', '', (t or '').lower().replace('’', "'"))[:45]
EVO0 = ('evorabody.com', 'skinglowmagazine.com')
def bnorm(b): return re.sub(r'[^a-z ]', '', (b or '').lower())[:50]
for r in rows:
    # Evora ecosystem: concept = headline; competitors: concept = opening of primary text (titles vary across reused copy)
    r["concept_key"] = (norm(r["eff_title"]) if r['domain'] in EVO0 else bnorm(r["eff_body"])) or norm(r["eff_title"]) or bnorm(r["eff_body"])
EVO = ('evorabody.com', 'skinglowmagazine.com')
sel = {}
ev = [r for r in rows if r['domain'] in EVO]
# 1) one per concept x page (longest running first)
g = collections.defaultdict(list)
for r in ev: g[(r['concept_key'], r['page_name'])].append(r)
for k, v in g.items():
    v.sort(key=lambda r: (-(r['days_running'] or 0), -(r['collation_count'] or 1)))
    sel[v[0]['ad_archive_id']] = v[0]
# 2) top-volume Evora concepts: add the 3 longest-running and 3 highest-variant extra ads
cc = collections.Counter(r['concept_key'] for r in ev)
for ck, n in cc.most_common(3):
    v = [r for r in ev if r['concept_key'] == ck]
    for r in sorted(v, key=lambda r: -(r['days_running'] or 0))[:3] + sorted(v, key=lambda r: -(r['collation_count'] or 1))[:3]:
        sel[r['ad_archive_id']] = r
# 3) competitors: one per concept x page for chosen brands, cap per brand
CAP = {'Goda': 12, 'NØRD BODY': 6, 'VitaeCharm': 5, 'Besque': 7, 'DRMTLGY': 3, 'Feline Skinscience': 2, 'Miami MD': 4,
       'OSEA': 3, 'Saeskyn': 3, 'TurmSkin': 1, 'Frøya Organics': 4, 'emilycarterblog.com': 1, 'theskinmag.com': 2,
       'Beekman 1802': 1, 'Beauty From Bees': 1, 'Remedy Skin': 1, 'tryorgatics.com': 1}
for b, cap in CAP.items():
    v = [r for r in rows if r['brand'] == b and r['domain'] not in EVO]
    if b == 'Goda': v = [r for r in v if 'silk-body-oil' in r['eff_link'] or 'bodyoil' in r['eff_link'] or 'crepey' in r['eff_link']]
    if b == 'Feline Skinscience': v = [r for r in v if 'crep' in (r['eff_title'] or '').lower() + (r['eff_body'] or '').lower()]
    if b == 'Saeskyn': v = [r for r in v if any(w in (r['eff_body'] or '').lower() for w in ('crepey', 'neck', 'firm'))]
    gg = collections.defaultdict(list)
    for r in v: gg[(r['concept_key'], r['page_name'])].append(r)
    picks = [sorted(x, key=lambda r: (-(r['days_running'] or 0)))[0] for x in gg.values()]
    picks.sort(key=lambda r: (-len(gg[(r['concept_key'], r['page_name'])]), -(r['days_running'] or 0)))
    for r in picks[:cap]: sel[r['ad_archive_id']] = r
# seeding text ads (no landing)
for r in rows:
    if r['page_name'] == 'Joanna Woodley':
        sel[r['ad_archive_id']] = r; break
out = list(sel.values())
# concept-level stats for variant_count context
cstat = collections.defaultdict(lambda: {"ids": 0, "pages": set(), "col": 0})
for r in rows:
    c = cstat[(r['brand'], r['concept_key'])]; c["ids"] += 1; c["pages"].add(r['page_name']); c["col"] += (r['collation_count'] or 1)
for r in out:
    c = cstat[(r['brand'], r['concept_key'])]
    r["concept_ids_in_sample"] = c["ids"]; r["concept_pages_in_sample"] = sorted(c["pages"]); r["concept_collation_sum"] = c["col"]
with open(D + "/raw/_ledger_selection.jsonl", "w") as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(out), collections.Counter(r['brand'] for r in out))
