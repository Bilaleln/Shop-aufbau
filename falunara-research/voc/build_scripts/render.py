# -*- coding: utf-8 -*-
import sys, csv, re, collections
sys.path.insert(0, '/tmp/claude-0/-home-user-Shop-aufbau/5b2336da-6c1e-5391-be3e-77204cb3c276/scratchpad')
from items import ITEMS, CONTROL, CHALLENGER
from pat2 import R
OUT = '/home/user/Shop-aufbau/falunara-research/ad_intelligence/'
SCR = '/tmp/claude-0/-home-user-Shop-aufbau/5b2336da-6c1e-5391-be3e-77204cb3c276/scratchpad/'
idx = {x['ad_archive_id']: x for x in R}
LEDGER = set(r['ad_id'] for r in csv.DictReader(open(OUT + 'swipe_ledger.csv')))
URL = 'https://www.facebook.com/ads/library/?id='
ALL = ITEMS + CONTROL + CHALLENGER
COLS = ['Item', 'Type', 'Description', 'Supporting ads/sources', 'Evidence signals', 'Counter-evidence', 'Confidence', 'Control/Challenger implication']

def conf(it): return f"{it['status']} · {it['conf']}"

# ---------- CSV ----------
with open(OUT + 'synthesis_table.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(COLS)
    for it in ALL:
        ads = '; '.join(URL + a + (' (Ledger)' if a in LEDGER else '') for a in it['ads'])
        sup = ads + (('; ' + '; '.join(it['src'])) if it['src'] else '')
        w.writerow([it['item'], it['cat'], it['desc'], sup, it['sig'], it['counter'], conf(it), it['impl']])

# ---------- MD table ----------
def esc(s): return s.replace('|', '\\|').replace('\n', ' ')
rows = ['| ' + ' | '.join(COLS) + ' |', '|' + '---|' * len(COLS)]
for it in ALL:
    ads = ', '.join(f"[{a}]({URL}{a}){'†' if a in LEDGER else ''}" for a in it['ads'])
    sup = ads + (('<br>' + '<br>'.join(esc(s) for s in it['src'])) if it['src'] else '')
    rows.append('| ' + ' | '.join([f"**{esc(it['item'])}**", esc(it['cat']), esc(it['desc']), sup, esc(it['sig']),
                                    esc(it['counter']), f"**{esc(conf(it))}**", esc(it['impl'])]) + ' |')
open(SCR + 'table.md', 'w').write('\n'.join(rows) + '\n')

# ---------- per-category lists ----------
cats = collections.OrderedDict()
for it in ITEMS:
    key = it['cat'].split(' / ')[0]
    cats.setdefault(key, []).append(it)
WHY = {
 'D7':'V2 verfehlt (nur VitaeCharm ≥60 Tage)', 'D8':'V4 verfehlt (Kundenglaube „nur Eingriffe helfen“)',
 'A8':'V1 verfehlt (faktisch nur Evora)', 'A9':'V4 verfehlt (Partner-/Sinnlichkeitsmotiv kundenseitig nicht belegt)',
 'A10':'V2 verfehlt (keine Body-Variante ≥60 Tage)', 'M2':'V4 verfehlt (Experten und informierte Kundinnen: Öl versiegelt)',
 'M5':'V1 verfehlt (nur Evora)', 'M6':'V1 verfehlt (je ein Advertiser pro Mechanismus)',
 'H6':'V1/V2 verfehlt (faktisch nur Evora, max. 75 Tage)', 'H7':'V1 verfehlt (51 von 55 Treffern Evora)',
 'H8':'V1 verfehlt (ein unbekannter Cluster); Authentizitätsrisiko', 'S3':'V1 verfehlt (nur Evora)',
 'S4':'V2 verfehlt (nur Evora ≥60 Tage)', 'S5':'V2 nicht messbar (Laufzeit verlinkender Anzeigen je Lander unbekannt)',
 'C4':'V1/V2 verfehlt (nur Evora, max. 42 Tage)', 'C5':'V1–V3 nicht messbar (nur 40 gesichtete Thumbnails)',
 'C6':'V3 verfehlt (7 Anzeigen)', 'O5':'V4 verfehlt (Abo-/Billing-Beschwerden dominieren Negativbewertungen)',
 'O8':'V1 verfehlt (Free gifts nur VitaeCharm; XL nur Besque/OSEA)'}
lines = []
for c, L in cats.items():
    v = [i for i in L if i['status'] == 'Validated']; k = [i for i in L if i['status'] == 'Candidate']
    lines.append(f"### {c}\n")
    lines.append('**Validated:** ' + ('; '.join(f"{i['item'].split(' · ')[0]} {i['item'].split(' · ',1)[1]} ({i['conf']})" for i in v) if v else '–') + '\n')
    lines.append('**Candidate:** ' + ('; '.join(f"{i['item'].split(' · ')[0]} {i['item'].split(' · ',1)[1]} – *{WHY[i['item'].split(' · ')[0]]}*" for i in k) if k else '–') + '\n')
open(SCR + 'cats.md', 'w').write('\n'.join(lines))

# ---------- Swipe file ----------
def norm(s): return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()[:80]
fl = lambda x: (x.get('eff_body') or '').strip().split('\n')[0].strip()
H = collections.defaultdict(list); T = collections.defaultdict(list)
for x in R:
    if x['B'] in ('Goda-Perfume',): continue
    H[norm(fl(x))].append(x)
    if (x.get('eff_title') or '').strip(): T[norm(x['eff_title'])].append(x)

def status(x):
    return 'live (Auslieferung bis 2026-10-03)' if x['end_date'] >= '2026-10-02' else f"gestoppt / nicht mehr ausgeliefert (letztes Datum {x['end_date']})"
def coll(x):
    c = x.get('collation_count')
    return 'k. A.' if c in (None, 'None', '') else str(c)
def rep(group):
    pages = sorted(set(z['page_name'].strip() for z in group))
    return f"{len(group)} IDs im Sample auf {len(pages)} Seite(n) ({', '.join(pages)}); frühester Start {min(z['start_date'] for z in group)}; davon live {sum(z['end_date']>='2026-10-02' for z in group)}"
def adv(x):
    b = {'MiamiMD+Feline': 'Miami MD / Feline Skinscience (Cluster)', 'UnknownSeeding': 'unbekannt (Seeding-Seite)'}.get(x['B'], x['B'])
    return f"{b} – Seite „{x['page_name'].strip()}“"
def meta(x, group, label):
    return (f"- Ad: [{x['ad_archive_id']}]({URL}{x['ad_archive_id']}){' (Ledger)' if x['ad_archive_id'] in LEDGER else ''} · Advertiser: {adv(x)} · Format: {x['display_format']}\n"
            f"- Start: {x['start_date']} · Days running: {x['D']} · Status: {status(x)} · Varianten (Meta „ads use this creative“): {coll(x)}\n"
            f"- Replikation ({label}): {rep(group)}\n")

HOOKS = [  # (id, validated-item reference)
 ('4109833019265205', 'H2, S1, CT3'), ('1637558804018844', 'H1, D1, CT2'), ('1611807499919232', 'H1, CT2'),
 ('1811884486444866', 'H1, D1'), ('1564770261945264', 'H1, A1, A4'), ('2202226780628780', 'H3, A1, A5, H5'),
 ('1570129684499222', 'H3, M1, S2'), ('2116539015744078', 'S1 (geteilter Opener Miami MD/Feline)'),
 ('4092537667704644', 'H2, H4, A2'), ('965929252430847', 'A2, B2'), ('1183652923933432', 'H3, D6, D5'),
 ('1175006387786014', 'H2, B1'), ('1070866808556946', 'D4, D1'), ('980035185081066', 'A4, A6, D2'),
 ('2310106993153092', 'D7 / CH1 (Kandidat)'), ('880796694467063', 'CH7 (Kandidat), B2'),
 ('4479159772361966', 'H2, C6 (angrenzend: Gesicht)'), ('1706678643610029', 'A1 (angrenzend: Gesicht)'),
 ('2515907112242718', 'O4 (Evora-Control)'), ('1361129475914444', 'O1, O2 (Evora-Control)'),
 ('1021976634228403', 'H6, S3 (Evora-Control, Kandidat)'), ('2329433507867811', 'A3, S3 (Evora-Control)'),
 ('1741250287018176', 'A9 (Kandidat, Evora)'), ('1908949839699218', 'H8 (Kandidat, Seeding)'),
 ('971890085912295', 'A10 / CH4 (Kandidat)'),
]
HEADS = ['1637558804018844', '980035185081066', '854380807531360', '1076748835007888', '1361129475914444',
         '986622734003880', '4109833019265205', '2202226780628780', '4092537667704644', '1021976634228403',
         '1564770261945264', '1048726737582951', '1570129684499222', '965929252430847', '1070866808556946',
         '2329433507867811', '1467338712082607', '1994209947876803', '1998108007419317', '2032403464184564',
         '971890085912295', '1592473439201348']
OPEN = [('4109833019265205', 7), ('1570129684499222', 6), ('1811884486444866', 4), ('2116539015744078', 5),
        ('965929252430847', 6), ('1183652923933432', 5), ('1048726737582951', 5), ('1021976634228403', 4),
        ('2329433507867811', 3), ('1741250287018176', 5), ('1540482734095150', 4), ('882082784513664', 5)]

out = []
out.append("# Swipe File – Wettbewerber-Hooks, Headlines und Story-Openings (verbatim)\n")
out.append("*FALUNARA Botanical Body Oil · U.S. · Stand 2026-10-03 · Quelle: öffentliche Meta Ad Library (US, ausgeloggt), deduplizierter Master `raw/_master_meta.jsonl` (849 IDs).* \n")
out.append("**Zweck und Grenzen.** Dies ist ein Forschungsarchiv fremder Werbetexte zur Analyse. Alle Texte stehen **unverändert** in Code-Blöcken (Groß-/Kleinschreibung, Emojis, Tippfehler und Zeichensetzung wie im Original). `[…]` außerhalb der Blöcke markiert nur, dass ein Opening nach N Absätzen abgeschnitten wurde; innerhalb der Blöcke ist nichts umformuliert, gekürzt oder ergänzt (einzige Ausnahme bei Openings: Leerzeilen und das Füllzeichen „⠀“ zwischen Absätzen wurden entfernt). Es ist **kein** Copy-Vorschlag für FALUNARA; Texte von Wettbewerbern dürfen nicht übernommen werden (insbesondere nicht von Evora, dem direkten Format- und Preis-Twin). Behauptungen in den Texten sind Aussagen der Advertiser und nicht geprüft.\n")
out.append("**Felder.** *Days running* = end_date − start_date (bei live-Anzeigen eine Untergrenze). *Varianten* = Metas „N ads use this creative and text“ (`collation_count`; k. A. = nicht angezeigt). *Replikation* = Anzahl der Ad-IDs im Sample mit identischer Erstzeile (Hooks/Openings) bzw. identischer Headline (Headlines), Persona-Seiten einzeln aufgeführt (sie sind **keine** unabhängigen Advertiser). Auswahl nach Evidenzstärke (Laufzeit ≥60 Tage und/oder Replikation ≥10 IDs bzw. ≥2 Seiten) gemäß Advertising_Intelligence_Synthesis.md; schwächere Einträge sind als Kandidat/Evora-spezifisch markiert. Keine Spend-, Reichweiten- oder ROAS-Daten; Survivorship Bias (Inaktiv-Ansicht lieferte 0 Anzeigen).\n")
out.append("\n## 1. Hooks (erste Zeile des Primärtexts)\n")
for n, (a, ref) in enumerate(HOOKS, 1):
    x = idx[a]; g = H[norm(fl(x))]
    out.append(f"### HOOK-{n:02d} · {adv(x)} · Bezug: {ref}\n")
    out.append(meta(x, g, 'identische Erstzeile'))
    out.append("```text\n" + fl(x) + "\n```\n")
out.append("\n## 2. Headlines (Anzeigentitel)\n")
for n, a in enumerate(HEADS, 1):
    x = idx[a]; g = T[norm(x['eff_title'])]
    out.append(f"### HEAD-{n:02d} · {adv(x)}\n")
    out.append(meta(x, g, 'identische Headline'))
    out.append("```text\n" + x['eff_title'].strip() + "\n```\n")
out.append("\n## 3. Story-Openings (erste Absätze des Primärtexts)\n")
for n, (a, k) in enumerate(OPEN, 1):
    x = idx[a]; g = H[norm(fl(x))]
    paras = [p for p in (x.get('eff_body') or '').strip().split('\n') if p.strip() and p.strip() != '⠀']
    cut = len(paras) > k
    out.append(f"### OPEN-{n:02d} · {adv(x)} · Headline: „{(x.get('eff_title') or '').strip()}“\n")
    out.append(meta(x, g, 'identische Erstzeile'))
    out.append(f"- Umfang: erste {min(k,len(paras))} von {len(paras)} Absätzen; Gesamtlänge Primärtext {len(x.get('eff_body') or '')} Zeichen" + (" · [… danach abgeschnitten]" if cut else '') + "\n")
    out.append("```text\n" + '\n'.join(paras[:k]) + "\n```\n")
open(OUT + 'Swipe_File.md', 'w', encoding='utf-8').write('\n'.join(out))
print('ok', len(ALL), 'rows')
