exec(open('build.py').read().split('# ====================== XLSX')[0])
from norm import split as tsplit

P = {p['key']: p for p in PAT}
def S(key): return rec(P[key]['rows'])
def R(f): return rec(sel(f))
def esc(s): return s.replace('|', '\\|').replace('\n', '<br>')
def qq(i): return esc(q(i))
def link(i): return f"[{i}]({url(i)})"
def qs(ids): return '<br>'.join(f"{esc(q(i))} – {link(i)}" for i in ids)

raw_tags = Counter(t for r in D for t in tsplit(r['Recurrence/pattern tag']))
norm_tags = Counter(t for r in D for t in r['tags'])
ages = [int(r['Stated age']) for r in D if r['Stated age'].isdigit()]
flags = Counter(f for r in D for f in r['flags'])
seed_n = flags['possible_seeding']

L = []
A = L.append
A('# VOC PROMPT 3 – Deep Reddit/Forum VOC Research: Synthese')
A('')
A('**Projekt:** FALUNARA Botanical Body Oil · **Zielgruppe:** U.S.-Frauen 40–65+ (Kern 48–58) mit trockener, crepey wirkender reifer Körperhaut · **Menopause:** nur Kontext · **FALUNARA-Inhaltsstoffe:** unbekannt – es werden keine Inhaltsstoffe, Wirkungen oder Claims abgeleitet · **Keine Ad-Copy.**')
A('')
A('Begleitdatei: `falunara-research/VOC_Master.xlsx` (Tabs 00_README – 09_Patterns). Alle Zitate in diesem Dokument sind verbatim aus `voc/VOC3_raw_merged.csv` übernommen (programmatisch eingefügt und gegengeprüft), jeweils mit VOC-ID und Quell-URL. Zitate bleiben englisch, Analyse auf Deutsch.')
A('')
A('---')
A('')
A('## 1. Methodik & Corpus-Abdeckung')
A('')
A('**Input (nur VOC-Workstream):** `VOC3_raw_merged.csv` (Batches A/B/C), `voc3_batches/batch_{A,B,C}_notes.md`, `VOC2_URL_Corpus.csv/.md`, `VOC3_extraction_spec.md`. Keine neuen Abrufe; `research_notes/`, `reports/`, `ad_intelligence/` wurden nicht gelesen.')
A('')
A(f'- **{len(D):,} VOC-Zeilen**'.replace(',', '.') + f' (Batch A {sum(r["VOC ID"][0]=="A" for r in D)}, B {sum(r["VOC ID"][0]=="B" for r in D)}, C {sum(r["VOC ID"][0]=="C" for r in D)}) aus **{len({r["Corpus ID"] for r in D})} Threads** in **{len({r["Community"] for r in D})} Communities**; alle 90 Corpus-Threads (C001–C090) liefern Zeilen.')
A(f'- **Quote-Verifikation:** In der Extraktion wurde jedes Zitat skriptbasiert gegen den gecachten Thread-Text geprüft (A 850/850, B 892/892, C 672/672). Gedroppt: 1 Titel-only-Zitat (C008), 2 Seeding-/Bot-Kommentare (B), 1 Bot-Zeile (C).')
A(f'- **Evidenzstärke:** high {sum(r["Evidence strength"]=="high" for r in D)} · medium {sum(r["Evidence strength"]=="medium" for r in D)} · low {sum(r["Evidence strength"]=="low" for r in D)}.')
A(f'- **Alter:** in {len(ages)} Zeilen explizit angegeben (Spanne {min(ages)}–{max(ages)}); davon {sum(40<=a<=65 for a in ages)} im Zielkorridor 40–65 und {sum(48<=a<=58 for a in ages)} im Kern 48–58. Bekannter Corpus-Fehler: C034-OP ist **nicht** 55 (die „55“ stammt von einer anderen Posterin) – OP-Zeilen ohne Alter.')
A('')
A('**Zeilen nach Community**')
A('')
A('| Community | Zeilen | Threads |')
A('|---|---|---|')
for c, n in Counter(r['Community'] for r in D).most_common():
    A(f'| {c} | {n} | {len({r["Corpus ID"] for r in D if r["Community"]==c})} |')
A('')
A('**Zeilen nach Kategorie** (18 Spec-Kategorien)')
A('')
A('| Kategorie | Zeilen |')
A('|---|---|')
for c, n in Counter(r['Category'] for r in D).most_common():
    A(f'| {c} | {n} |')
A('')
A('**Zeilen nach Körperzone** (Spalte „Body area“)')
A('')
A(' · '.join(f'{b} {n}' for b, n in Counter(r['Body area'] for r in D).most_common()))
A('')
A('**Flags**')
A('')
A('| Flag | Zeilen | Umgang in der Synthese |')
A('|---|---|---|')
A(f'| possible_seeding | {flags["possible_seeding"]} | aus **allen** Zählungen in Tabs 03–09 und in diesem Report **ausgeschlossen** (bleiben in 02_Raw_VOC sichtbar) |')
A(f'| hrt_medical_context | {flags["hrt_medical_context"]} | mitgezählt, je Item separat ausgewiesen; nur Kontext, keine Claims |')
A(f'| non_us_signal | {flags["non_us_signal"]} | mitgezählt; Sensitivität „ohne non_US/U40“ je Item ausgewiesen |')
A(f'| under_40_signal | {flags["under_40_signal"]} | mitgezählt; Sensitivität je Item ausgewiesen |')
A(f'| face_only_transferable | {flags["face_only_transferable"]} | mitgezählt, wo inhaltlich übertragbar |')
A(f'| possible_male_poster | {flags["possible_male_poster"]} | mitgezählt (vernachlässigbar) |')
A('')
A(f'**Basis nach Seeding-Ausschluss:** {len(CORE)} Zeilen / {len({r["Corpus ID"] for r in CORE})} Threads. Ohne non_US- und U40-Zeilen zusätzlich: {len([r for r in CORE if not ({"non_us_signal","under_40_signal"} & set(r["flags"]))])} Zeilen. Die Sensitivitätsprüfung zeigt: Kein Top-Muster verliert durch Ausschluss von non_US/U40 seinen Rekurrenz-Status (Details: Spalte „Sensitivity“ im XLSX und §8).')
A('')
A('### 1.1 Tag-Normalisierung')
A('')
A(f'Die drei Batches nutzten die Spec-Startliste plus eigene `new_`-Tags. Vor der Synthese: **{len(raw_tags)} Roh-Tags → {len(norm_tags)} normalisierte Tags**. Synonyme wurden zusammengeführt; nicht gemappte `new_`-Tags verlieren nur das Präfix. Vollständige Liste auch in 00_README.')
A('')
A('| Normalisierter Tag | Zusammengeführte Roh-Tags |')
A('|---|---|')
inv = defaultdict(list)
for k, v in MAP.items(): inv[v].append(k)
for v in sorted(inv): A(f'| `{v}` | {", ".join("`"+k+"`" for k in sorted(inv[v]))} |')
A('')
A('### 1.2 Zählregeln & Labels')
A('')
A('- **Recurrence** = „N rows / M threads / K communities“, mit Python über alle einem Item zugeordneten Zeilen berechnet (ohne possible_seeding). Zuordnung über normalisierte Tags, teils kombiniert mit Kategorie- und Regex-Filtern auf dem Zitattext; die vollständige ID-Liste je Item steht im XLSX (Spalte „All supporting VOC IDs“). Eine Zeile kann mehreren Items angehören.')
A('- **Rekurrenz-Label** (Basis = distinkte Threads): *stark wiederkehrend* ≥ 20 · *wiederkehrend* 8–19 · *begrenzt wiederkehrend* 3–7 · *isoliert* ≤ 2.')
A('- **Konfidenz:** *hoch* = ≥ 15 Threads und ≥ 4 Communities; *mittel* = ≥ 6 Threads und ≥ 2 Communities; sonst *niedrig*. Konfidenz = Robustheit im Corpus, **keine** Aussage über Häufigkeit in der U.S.-Population.')
A('- Zeilen ≠ Personen: Eine Posterin kann mehrere Zeilen liefern; Threads sind daher die robustere Rekurrenz-Basis.')
A('')
A('---')
A('')
# ================= 2. Deep findings
A('## 2. Deep VOC findings')
A('')
amf = sel(AND(T('amlactin_lactic'), T('fragrance_sensitivity')))
F_ = [
 ('Der Körper ist die „vergessene Zone“ – und der Schock kommt plötzlich.',
  f'Plötzlicher Beginn ist eines der stärksten Narrative ({S("P08")}). Typisch: Gesicht seit Jahren gepflegt, Körper nicht ({S("P18")}). Der Wendepunkt wird als Moment erzählt („overnight“, „woke up“), oft mit konkretem Alter (40–65).',
  ['A0001', 'A0099', 'B0020', 'B0390', 'C0422']),
 ('Crepey ist primär ein Arm- und Bein-Problem, sekundär Hände, Hals, Knie.',
  f'Tags: crepey_arms {R(T("crepey_arms"))}; crepey_legs {R(T("crepey_legs"))}; crepey_hands {R(T("crepey_hands"))}; crepey_knees {R(T("crepey_knees"))}; crepey_chest {R(T("crepey_chest"))}. Der Begriff „crep…“ selbst erscheint in {R(RX("crep"))}.',
  ['B0092', 'A0613', 'A0130', 'A0632', 'C0377']),
 ('Haut wird zum Identitätsmarker: „old lady“, Großmutter, Reptil.',
  f'{S("P09")}. Die Haut der Mutter/Großmutter dient als Spiegel; Reptil-Metaphern (lizard, snake, alligator, crocodile, dragon scales) erscheinen in {R(RX("lizard|reptil|snake|alligator|crocodile|dragon|dinosaur|scales|scaly"))}.',
  ['B0865', 'B0829', 'A0716', 'A0651', 'C0346']),
 ('Sichtbarkeit steuert Verhalten: Ärmel, Shorts, Sommer.',
  f'{S("P10")}. Vermeidung ist konkret (lange Ärmel trotz Hitze, keine Röcke über dem Knie). Erfolg wird umgekehrt als „wieder ärmellos“ erzählt.',
  ['A0080', 'C0636', 'B0223', 'B0804']),
 ('Die zentrale Funktionsklage: Lotion hält nicht.',
  f'{S("P02")} (lotion_temporary + consistency_effort). Nachcremen mehrmals täglich, Lotion „überall im Haus“, Gefühl dass alte Routine „nicht mehr reicht“.',
  ['C0194', 'B0088', 'C0092', 'C0349']),
 ('Öl ist präsent – aber ambivalent und erklärungsbedürftig.',
  f'Öl auf feuchter Haut ist nahezu Konsens ({S("P01")}). Gleichzeitig dominieren Einwände zu Fett/Flecken/Wartezeit und Klebrigkeit ({S("P03")}) sowie Verwirrung über Öl vs. Lotion und Reihenfolge ({S("P04")}). Das Laienmodell „Öl versiegelt nur, hydratisiert nicht“ ist verbreitet.',
  ['A0672', 'C0474', 'C0240', 'B0087', 'C0505', 'C0503']),
 ('AmLactin ist der Benchmark – Geruch ist seine Achillesferse.',
  f'amlactin_lactic: {S("P06")}. Davon mit Geruchseinwand (amlactin_lactic ∩ fragrance_sensitivity): {rec(amf)}. Metaphern: „pee“, „cat pee“, „sour milk“, „maple syrup“.',
  ['A0017', 'A0187', 'A0299', 'A0302', 'B0023']),
 ('Duft polarisiert innerhalb derselben Zielgruppe.',
  f'fragrance_sensitivity {R(T("fragrance_sensitivity"))} vs. scent_love {R(T("scent_love"))}. Ein Teil berichtet neue Duftunverträglichkeit (Peri-Kontext), ein anderer lehnt Unparfümiertes als „fake plastic smell“ ab.',
  ['C0363', 'C0364', 'C0291', 'C0497']),
 ('Preis & Misstrauen bilden einen gemeinsamen Filter.',
  f'Preis-Wert: {S("P11")}; Marketing-Misstrauen/Transparenz: {S("P12")}. Drogerie-/Costco-Preise sind Anker; Prestige-Käufe werden als Lehrgeld erzählt; fehlende Prozentangaben und Vorher/Nachher-Winkel werden aktiv kritisiert.',
  ['A0124', 'C0463', 'C0641', 'A0185', 'C0533']),
 ('Topischer Fatalismus vs. Erfolgsberichte.',
  f'{S("P13")}. Ein starker Teil glaubt, nur Prozeduren, Krafttraining oder Hormone helfen – zugleich gibt es zahlreiche Erfolgsberichte mit einfachen Topika (Kategorie „Successful attempts“: {R(C(SUCC))}).',
  ['B0086', 'A0576', 'B0216', 'B0851']),
 ('Ziele sind taktil und bescheiden.',
  f'Taktile Ziele dominieren ({R(T("soft_smooth_desire"))}) vor Glow ({R(T("glow_desire"))}). Häufig ist das Ziel nicht „jung“, sondern „nicht älter als ich bin“ / „verlangsamen“.',
  ['A0017', 'B0252', 'C0353', 'C0460']),
 ('Routine-Müdigkeit ist real – Ritual-Genuss auch.',
  f'routine_fatigue {R(T("routine_fatigue"))}; self_care_ritual {R(T("self_care_ritual"))}. Die Körperroutine konkurriert mit Zeit, Wärme (Arizona), Ungeduld nach der Dusche.',
  ['A0673', 'A0749', 'B0563', 'A0163']),
 ('Menopause/HRT ist allgegenwärtiger Kontext – nicht Produktthema.',
  f'Pattern P19: {S("P19")}. Juckreiz/Schuppen konzentrieren sich in r/Menopause ({sum(r["Community"]=="r/Menopause" for r in P["P22"]["rows"])} von {len(P["P22"]["rows"])} itch_flake-Zeilen). HRT hilft laut Posterinnen nicht zuverlässig der Haut.',
  ['A0167', 'B0562', 'A0224', 'B0722']),
]
for i, (h, body, ids) in enumerate(F_, 1):
    A(f'**F{i}. {h}** {body}')
    A('')
    for x in ids: A(f'- {q(x)} – {link(x)}')
    A('')
A('---')
A('')

def bank(title, items, extra_col=None, extra_key=None, intro=''):
    A(f'## {title}')
    A('')
    if intro: A(intro); A('')
    hdr = '| # | Item | Verbatim (VOC ID → URL) | Recurrence | Label | Konfidenz |' + (f' {extra_col} |' if extra_col else '')
    A(hdr); A('|' + '---|' * (hdr.count('|') - 1))
    for n, it in enumerate(items, 1):
        line = f"| {n} | {esc(it['name'])} | {qs(it['exids'])} | {rec(it['rows'])} | {label(it['rows'])} | {conf(it['rows'])} |"
        if extra_col: line += f" {esc(it[extra_key])} |"
        A(line)
    A('')

# ================= 3. Phrase bank
A('## 3. Phrase bank')
A('')
A('Teil A zählt Begriffs-/Metaphernfamilien per Regex im **Zitattext** (messbar). Teil B: eine Auswahl prägnanter Einzelphrasen; alle 1-zu-1-Phrasen der Kategorie „Exact phrases / metaphors / repeated wording“ stehen im XLSX-Tab 08_Phrase_Bank.')
A('')
A('**Teil A – Begriffsfamilien**')
A('')
A('| Phrase/Metapher | Kategorie | Recurrence | Beispiele (VOC ID → URL) |')
A('|---|---|---|---|')
for it in sorted(PH, key=lambda x: -len(x['rows'])):
    A(f"| {esc(it['name'])} | {it['cat']} | {rec(it['rows'])} | {qs(it['exids'][:2])} |")
A('')
A('**Teil B – prägnante Einzelphrasen** (isoliert oder selten, aber sprachlich besonders aussagekräftig)')
A('')
for x in ['A0670', 'A0671', 'B0727', 'B0188', 'C0377', 'C0196', 'C0284', 'A0651', 'B0181', 'C0105', 'B0227', 'B0815', 'A0792', 'C0204', 'B0612', 'A0746', 'B0237', 'C0042', 'C0181', 'B0087', 'A0806', 'C0460', 'C0353']:
    A(f'- {q(x)} – {link(x)}')
A('')
A('---')
A('')
bank('4. Objection bank', OS, 'Forschungs-Implikation', 'impl')
A('---'); A('')
bank('5. Desire bank', DS, 'direkt/abgeleitet', 'kind')
A('---'); A('')
bank('6. Failed-solution bank', FS, 'Beschwerde/Ergebnis', 'out')
A('---'); A('')
bank('7. Trigger/situation bank', TS)
A('---'); A('')
# ================= 8. Pattern synthesis
A('## 8. Pattern synthesis – wiederkehrend vs. isoliert')
A('')
A('Rekurrenz ist hier **messbar**: Zeilen, distinkte Threads und Communities aus der CSV (ohne possible_seeding). Die Spalte „ohne non_US/U40“ zeigt die Robustheit gegenüber Nicht-U.S.- und Unter-40-Signalen; „HRT“ = Zeilen mit hrt_medical_context.')
A('')
A('### 8.1 Wiederkehrende Muster')
A('')
A('| ID | Muster | Recurrence | ohne non_US/U40 | HRT-Zeilen | Konfidenz | Kernbelege | Gegenevidenz |')
A('|---|---|---|---|---|---|---|---|')
for p in PAT:
    rows = p['rows']
    strict = [r for r in rows if not ({'non_us_signal', 'under_40_signal'} & set(r['flags']))]
    n2, m2, k2 = nmk(strict)
    hrt = sum('hrt_medical_context' in r['flags'] for r in rows)
    ce = '<br>'.join(f"{esc(q(i))} – {link(i)}" for i in p['counter']) + ('<br>' if p['counter'] else '') + esc(p['cnote'])
    A(f"| {p['key']} | {esc(p['name'])} | {rec(rows)} | {n2} rows / {m2} threads | {hrt} | {conf(rows)} | {qs(p['exids'][:2])} | {ce} |")
A('')
A('**Lesehilfe:** P02, P03, P04, P05 und P11 sind die für ein Körperöl operativ relevantesten Muster (Anwendung, Textur, Erklärungsbedarf, Duft, Preis). P08–P10 beschreiben den emotionalen/situativen Kontext. P19 ist Kontext, kein Produktthema.')
A('')
A('### 8.2 Isolierte Aussagen (≤ 2 Threads)')
A('')
A('Diese Tags kommen nur in 1–2 Threads vor. Sie werden **nicht** als Muster interpretiert, aber als Hypothesen-Material dokumentiert.')
A('')
A('| Tag | Recurrence | Beleg |')
A('|---|---|---|')
for t, rs in ISO:
    A(f"| `{t}` | {rec(rs)} | {qs([rs[0]['VOC ID']])} |")
A('')
A('Weitere, in Tags nicht erfasste Einzelstimmen mit Hypothesenwert: ' + '; '.join(f'{q(i)} ({link(i)})' for i in ['C0167', 'C0577', 'C0410', 'B0319']) + '.')
A('')
A('---')
A('')
# ================= 9. Contradictions
A('## 9. Contradictions')
A('')
A('| Spannungsfeld | Position A (verbatim) | Position B (verbatim) | Einordnung |')
A('|---|---|---|---|')
for t, a, b, note in CONTRA:
    A(f'| {esc(t)} | {qs(a)} | {qs(b)} | {esc(note)} |')
A('')
A('Zentrale Widerspruchs-Logik: Die Zielgruppe ist **nicht homogen** in Textur- (leicht vs. reichhaltig) und Duftpräferenz (duftfrei vs. Duftgenuss) sowie im Wirkglauben (Topika sinnlos vs. Topika haben geholfen). Diese Achsen sollten in späteren Prompts als Segmentierungsvariablen geprüft werden – nicht als Mehrheitsmeinung aufgelöst.')
A('')
A('---')
A('')
# ================= 10. Evidence table
A('## 10. Source-complete evidence table')
A('')
A(f'**Vollständige Evidenz:** alle {len(D)} Zeilen in `VOC_Master.xlsx` → Tab **02_Raw_VOC** (VOC ID, Kategorie, Zitat verbatim, Paraphrase DE, Source URL, Thread URL, Corpus ID, Community, Kontext, Original- und normalisierte Tags, Evidenzstärke, Implikation, Alter, Körperzone, Flags). Thread-Metadaten in Tab 01_Source_Corpus.')
A('')
A(f'**Kuratierte Tabelle der {len(CURATED)} wichtigsten Einträge** (Auswahl nach Rekurrenz-Relevanz, Evidenzstärke, Zielalter und Abdeckung aller Banks):')
A('')
A('| # | VOC ID | Kategorie | Zitat (verbatim) | Community | Alter | Evidenz | Flags | URL |')
A('|---|---|---|---|---|---|---|---|---|')
for n, i in enumerate(CURATED, 1):
    r = BYID[i]
    A(f"| {n} | {i} | {r['Category']} | {esc(r['Exact short quote'])} | {r['Community']} | {r['Stated age'] or '–'} | {r['Evidence strength']} | {r['Flags'] or '–'} | [Link]({r['Source URL']}) |")
A('')
A('---')
A('')
# ================= 11. Limitations
A('## 11. Limitations')
A('')
for s in [
 'Plattform-Bias: 88 von 90 Threads sind Reddit, 2 Inspire.com. Facebook-Gruppen, TikTok/YouTube-Kommentare und Retailer-Reviews fehlen (VOC2-Scope). Reddit-Nutzerinnen sind vermutlich recherche-affiner und skeptischer als der Durchschnitt.',
 'U.S.-Herkunft ist nicht verifizierbar; non_us_signal markiert nur explizite Hinweise. Fehlende Flags bedeuten nicht gesicherte U.S.-Herkunft.',
 f'Alter ist nur in {len(ages)} Zeilen angegeben; r/30PlusSkinCare, r/SkincareAddiction, r/beauty und r/Ulta liegen tendenziell jünger. under_40_signal erfasst nur explizite Angaben.',
 'Kommentar-Tiefe: Der Cache enthält max. ~100 Einträge pro Thread; tiefere Antworten großer Threads fehlen.',
 'Zählungen sind Erwähnungen im Corpus (Zeilen/Threads), keine Prävalenz- oder Marktanteilsschätzungen. Threads wurden für Relevanz ausgewählt (Selektionsbias zugunsten von Problem-Threads).',
 'Kodierung: drei Extraktions-Batches mit leicht unterschiedlichem Tagging-Stil; nach Normalisierung bleiben Unschärfen (z. B. Zitat über „pee“-Geruch einmal als scent_love getaggt). Items kombinieren daher Tags mit Kategorie-/Regex-Filtern; volle ID-Listen erlauben Audit.',
 'Regex-Zählungen (Phrase bank) können vereinzelt Fehltreffer enthalten (z. B. „thin“ in anderem Sinn); sie sind als Größenordnung zu lesen.',
 'Mehrfachzeilen pro Person/Kommentar möglich (ein Zitat kann zwei Kategorien bedienen) – Threads sind die robustere Basis.',
 f'Seeding: {seed_n} Zeilen als possible_seeding ausgeschlossen; die starke AmLactin-/Gold-Bond-Begeisterung wirkt organisch, ist aber nicht beweisbar frei von verdeckter Werbung (vgl. Skepsis-Zitat A0054).',
 'Menopause-/HRT-Aussagen sind medizinischer Kontext und keine Grundlage für Produkt- oder Wirkclaims; Juckreiz kann symptomatisch statt kosmetisch sein.',
 'FALUNARA-Formel ist unbekannt: Kein Item in diesem Report behauptet oder impliziert, dass FALUNARA ein Problem löst. Implikationen sind Forschungsfragen, keine Werbeaussagen.',
]:
    A(f'- {s}')
A('')
open(OUT_MD, 'w', encoding='utf-8').write('\n'.join(L))
print('written', OUT_MD, len(L), 'lines')
