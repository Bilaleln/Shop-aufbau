"""Merge all Meta raw scrapes (raw/*.jsonl + scrapers/samples/meta*.jsonl) into raw/_master_meta.jsonl, deduped by ad id.
Adds: brand (from landing domain), eff_title/eff_body (DCO card fallback), days_running (end_date - start_date, end=observed),
sources (list of scrape files that surfaced the ad)."""
import json, glob, os, re, datetime
from urllib.parse import urlparse
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BR = {"evorabody.com": "Evora Body", "skinglowmagazine.com": "Evora Body (via skinglowmagazine listicle)",
      "goda.co": "Goda", "godaperfume.com": "Goda", "drmtlgy.com": "DRMTLGY", "saeskyn.com": "Saeskyn",
      "try-turmskin.com": "TurmSkin", "turmskin.com": "TurmSkin", "besque.co": "Besque", "nordbody.com": "NØRD BODY",
      "vitaecharm.com": "VitaeCharm", "trymiamimd.com": "Miami MD", "felineskinscience.com": "Feline Skinscience",
      "froyaorganics.com": "Frøya Organics", "beekman1802.com": "Beekman 1802", "oseamalibu.com": "OSEA",
      "crepeerase.com": "Crepe Erase", "thebodyfirm.com": "Crepe Erase", "necessaire.com": "Nécessaire",
      "goldbond.com": "Gold Bond", "soldejaneiro.com": "Sol de Janeiro", "beautyfrombees.ca": "Beauty From Bees",
      "vitalityextracts.com": "Vitality Extracts", "meditherapy.co": "Meditherapy", "remedyskin.com": "Remedy Skin"}
def dom(u):
    try: h = urlparse(u).netloc.lower()
    except Exception: return ""
    h = h[4:] if h.startswith("www.") else h
    for k in BR:
        if h == k or h.endswith("." + k): return k
    return h
def d(s): return datetime.date.fromisoformat(s) if s else None
files = sorted(glob.glob(D + "/raw/*.jsonl")) + sorted(glob.glob(D + "/scrapers/samples/meta*.jsonl"))
M = {}
for f in files:
    if os.path.basename(f).startswith(("_", "google_")): continue
    for l in open(f):
        r = json.loads(l); i = r.get("ad_archive_id")
        if not i: continue
        src = os.path.basename(f)
        if i in M:
            M[i]["sources"].append(src)
            if r.get("cards") and not M[i].get("cards"): M[i].update({k: v for k, v in r.items() if k != "sources"})
            continue
        r["sources"] = [src]; M[i] = r
out = []
for i, r in M.items():
    c0 = (r.get("cards") or [{}])[0] if r.get("cards") else {}
    t = r.get("title") or ""; b = r.get("body") or ""
    if "{{" in t or not t: t = c0.get("title") or t
    if "{{" in b or not b: b = c0.get("body") or b
    lu = r.get("link_url") or c0.get("link_url") or ""
    if "{{" in lu and c0.get("link_url"): lu = c0["link_url"]
    r["eff_title"], r["eff_body"], r["eff_link"] = t, b, lu
    r["domain"] = dom(lu) or dom("https://" + (r.get("caption") or ""))
    r["brand"] = BR.get(r["domain"], r["domain"])
    s, e = d(r.get("start_date")), d(r.get("end_date"))
    r["days_running"] = (e - s).days if s and e else None
    r["days_since_start_asof_2026-10-03"] = (datetime.date(2026, 10, 3) - s).days if s else None
    out.append(r)
with open(D + "/raw/_master_meta.jsonl", "w") as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(out), "unique ads")
