# Creative Research Playbook: FALUNARA Botanical Body Oil (U.S.)

*Workstream 8 „Cross-Workstream Synthesis“ · Stand 2026-10-04 · Zielgruppe: U.S.-Frauen 40–65+, Kern 48–58, trockene bzw. „crepey“ wirkende reife Körperhaut · Produkt: FALUNARA Botanical Body Oil, $49 (Vergleichspreis $79), goldenes Öl in Glasflasche mit weißer Pumpe, Website falurana.com. Markenname „FALUNARA“ und Domain „falurana“ werden bewusst unverändert nebeneinander geführt (siehe §14).*

**Was dieses Dokument ist.** Eine Synthese der vier abgeschlossenen Upstream-Workstreams (Marktbewusstsein, Psychografie/Wünsche, Competitor/Advertising Intelligence, VOC). Es überschreibt keine Upstream-Labels. Wo dieses Playbook zu einer anderen Einschätzung kommt, steht das als „Upstream-Label → Playbook-Einschätzung“ mit Begründung da. **Was es nicht ist:** keine Ad-Copy, keine Headlines, keine Claims für FALUNARA. FALUNARAs Inhaltsstoffe (INCI), Sensorik, Duft, Reviews und klinische Daten sind unbekannt. Nichts hier unterstellt sie.

---

## Datenbasis & Methodik

**Upstream-Quellen (vollständig gelesen) und Kürzel in diesem Dokument**

| Kürzel | Datei | Inhalt |
|---|---|---|
| **[MB]** | `reports/FALUNARA Marktbewusstsein USA.md` | Schwartz-Awareness, Sophistication, Problem-Sprache, Einwände, Segmente |
| **[PW]** | `reports/FALUNARA Psychografie und Wünsche USA.md` | Desire-Inventar D1–D16, Mass Desires, Trigger, Kaufkriterien, Evidence-Table #1–#53 |
| **[CI]** | `ad_intelligence/Competitor_Intelligence_Research.md` | Wettbewerberset, Top-25-Ads, Muster-Zählungen, Landingpages, Visuals |
| **[AIS]** | `ad_intelligence/Advertising_Intelligence_Synthesis.md` + `synthesis_table.csv` (inhaltsgleich, 68 Items) | Items D1–D8, A1–A10, B1–B2, M1–M6, H1–H8, S1–S5, C1–C6, O1–O8, CT1–CT6, CT-E, CH1–CH8 mit V1–V4-Validierung |
| **[SF]** | `ad_intelligence/Swipe_File.md` | HOOK-01–25, HEAD-01–22, OPEN-01–12 (verbatim) |
| **[LED]** | `ad_intelligence/swipe_ledger.csv` | 122 codierte Anzeigen (nur punktuell genutzt) |
| **[VOC1]** | `voc/VOC1_Community_Map.md` | Community-Karte, Zugriffstests |
| **[VOC2]** | `voc/VOC2_URL_Corpus.md` | 90 verifizierte Threads C001–C090 |
| **[VOC3]** | `voc/VOC3_Deep_Reddit_VOC_Research.md` | Findings F1–F13, Phrase Bank, Objection Bank #1–15, Desire Bank #1–16, Failed-Solution Bank #1–15, Trigger Bank #1–15, Patterns P01–P25, Contradictions |
| **[VOCX]** | `VOC_Master.xlsx` (Tabs 00–09; 2.414 Zeilen, 2.378 ohne Seeding) | Rohzeilen mit VOC-IDs (A/B/C####) |

**Zählweise.** VOC-Rekurrenz wird wie in [VOC3 §1.2] als „Zeilen / Threads / Communities“ angegeben (ohne `possible_seeding`). Wo dieses Playbook eigene Nachzählungen in `VOC_Master.xlsx` → `02_Raw_VOC` vorgenommen hat (Regex über das Zitatfeld, Seeding ausgeschlossen), ist das als **[PB-Nachzählung]** markiert. Werbe-Zahlen sind Anzeigen im Scrape-Sample (Untergrenzen), keine Library-Totals [AIS §1.5].

**Label-System in diesem Playbook**

| Label | Bedeutung |
|---|---|
| **VALIDIERT** | Upstream als validiert geführt **und** VOC bestätigt oder verstärkt die Kernprämisse (≥ „wiederkehrend“, ≥ 8 Threads) |
| **VALIDIERT (eingeschränkt)** | Validiert, aber VOC widerspricht einem Teil oder ist nur teilweise deckend |
| **KANDIDAT** | Mindestens eine Evidenzsäule fehlt oder ist widersprüchlich; Zusatz „gestärkt“/„geschwächt“ zeigt die VOC-Richtung |
| **HYPOTHESE** | Playbook-eigene Ableitung, nicht getestet; nur für §15 und als Territoriums-Vorschlag |
| VOC-Verdikt | **bestätigt / verstärkt / abgeschwächt / widerspricht / stumm** (stumm = VOC enthält keine verwertbare Evidenz) |

**Wichtiger Hintergrund zur V4-Neuprüfung.** [AIS] hat ihr Kriterium V4 („kein Kundenwiderspruch“) vor Abschluss der VOC-Arbeit geprüft und sich nur auf [MB] und [PW] gestützt [AIS §1.1, §7 Punkt 8]. Dieses Playbook prüft jedes AIS-Item gegen [VOC3]/[VOCX] erneut (Abschnitte 4–6 und 9–13).

**Tool-Substitutionen und blockierte Quellen**

| Geplant | Tatsächlich | Quelle |
|---|---|---|
| TrendTrack (Spend/Scaling/Transkripte) | **0 Credits → nicht genutzt.** Ersatz: öffentliche **Meta Ad Library** (US, ausgeloggt, ~30 Anzeigen pro Seitenaufruf; 849 eindeutige IDs) + **Google Ads Transparency Center** (Laufzeiten, keine Copy). Keine Spend-, Reichweiten-, CTR- oder ROAS-Daten. | [CI §7], [AIS §1.5], `access_test.md` |
| ChatGPT Deep Research | **Nicht verfügbar.** Ersatz: der Multi-Agent-Deep-Research-Prozess dieser Umgebung (getrennte Workstreams, deren Notizen in `research_notes/` liegen; Synthese durch diesen Agenten) | Aufgabenbriefing |
| Reddit-API / Mitgliederzahlen | Reddit nur über **RSS/Atom** (Feeds, In-Sub-Suche, Thread-RSS max. ~100 Einträge); `about.json` blockiert; starke HTTP-429-Limits (86 × in VOC2) | [VOC1 §1], [VOC2 §7] |
| TikTok | **TikTok Ad Library US nicht verfügbar** (HTTP 421, nur EU/EEA/UK/CH); Creative-Center-Keyword-Suche deaktiviert | [CI §7], `access_test.md` |
| Retail-Reviews | **Amazon 503, Walmart/Sam's Club CAPTCHA, RealSelf 503**; Ulta/Sephora/Target-Texte nicht abrufbar | [MB Contradictions], [PW Unbekannt] |
| Weitere blockierte Quellen | Google Trends (HTTP 429), CNN Underscored (HTTP 451), Allure nicht direkt gelesen, Neutrogena-Body-Oil-Seite 404, Nécessaire/Gold-Bond-Landingpages 404, Miami-MD-Lander (Proxy), r/over50 (403), r/AgingGracefully/r/over40 leer, SkinCareTalk (Paywall), Mayo Clinic Connect/Quora/PurseForum/MetaFilter (403), Sephora Community eingestellt, Mumsnet (UK → ausgeschlossen) | [MB], [CI §7], [VOC1 §2–3] |
| Trustpilot, Blogs, einige Umfragen | Über ein zusammenfassendes Fetch-Tool gelesen → **„Wortlaut vor Verwendung prüfen“** (in diesem Dokument: **[WP]**) | [MB], [PW] |

**Grundsätzliche Grenzen.** Keine Performance-Daten (Laufzeit und Replikation sind Verhaltens-Proxys, keine Erfolgsbelege); Survivorship Bias (Inaktiv-Filter lieferte 0 Anzeigen); Video-Inhalte nicht transkribiert (40 Thumbnails gesichtet); VOC ist zu 88/90 Threads Reddit, U.S.-Herkunft nicht verifizierbar, Alter nur in 438 Zeilen angegeben (175 im Kern 48–58) [VOC3 §1, §11].

---

## 1. Market snapshot

**Kategorie und Größe (Werbesignale).** Aktive U.S.-Meta-Anzeigen je Keyword: „crepey skin“ 14,299; „crepey arms“ 6,036; „crepey body oil“ 4,981 [CI §1.1]. Für Suchvolumen fehlen Daten (Google Trends HTTP 429) [MB Search-Signale]. Die Kategoriebasis der Ad-Synthese umfasst 707 Anzeigen in 20 unabhängigen Advertiser-Clustern; Evora stellt 220 davon [AIS §1.2].

**Wettbewerbsfeld (Auszug, nach Relevanz)** [CI §1.1], [MB Known-solution map]

| Spieler | Preis (laut Quelle) | Rolle für FALUNARA | Werbe-Signal |
|---|---|---|---|
| **Evora Body – Botanical Body Oil™** | $49 (compare $69), 2er $39/Fl., 3er $34/Fl. [CI]; abweichend $54 / $88 / $119 laut Shopify-JSON [PW #39] → siehe §14 | **Direkter Format- und Preis-Twin**: goldenes Öl, Klarglas, weiße Pumpe, „botanical body oil“, gleiche Zielgruppe | 5 Persona-Seiten + Listicle-Seite; 1,161 Library-Anzeigen gemeldet; Volumen-Schwerpunkt September 2026 [CI §1.2] |
| Goda – Silk Body Oil | $59 (compare $98) | Längster Body-Oil-Langläufer | Testimonial-Konzept ~16 Monate, 4 Seiten [CI §3] |
| NØRD BODY – Peptide Body Oil | n. erfasst | Peptid-Öl, „face-grade for body“ | 56 IDs, bis 117 Tage [CI §3] |
| Besque – Magic Body Oil | $120 / $78 Abo | Natürliches Öl 50+ | Persona „40 Plus & Fabulous“ |
| VitaeCharm – Body Oil | $32 / $19 / $15 je Fl. | GLP-1-, Bluterguss-Nischen | 15 IDs „Ditching $400…“ 99 Tage |
| DRMTLGY Retinol Body Lotion | $36 / $27 Auto-Ship | Retinol/Derm-Positionierung | 50 IDs, 185 Tage, Google seit 2023 |
| Miami MD / Feline „Advanced Crepe Fix“ | – | „Harvard dermatologist“, „Fibroblast Failure“ | 11 IDs, 107–147 Tage |
| OSEA Undaria Algae Body Oil | $100 → $84 (Abo $75.60) [CI]; $52 (5 oz) [MB] | Premium-Referenz, auch im VOC genannt | gering |
| Gold Bond Crepe Corrector, AmLactin, Crepe Erase | ca. $10–$50 | Drogerie/Infomercial-Benchmarks im VOC | In Meta-Library kaum sichtbar [CI §1.1] |

**Preisbänder im Kopf der Kundinnen.** Drogerie $10–20, Körper-Retinol < $25, Prestige-Öle ~$50–80, Evora-Einzelflasche $49–54 [MB Known-solution map], [PW Preis-Tradeoff]. VOC-Anker (siehe §8, §14): „Do not spend more than like $20 on a bottle for big brand names.“ (A0593), „Costco has a huge bottle for about $20“ (A0197).

**FALUNARA heute** [MB „Wo FALUNARA heute steht“]: ein Produkt, „FALUNARA Botanical Body Oil $49.00 $79.00 SAVE 38%“; Ritual-/Textur-Copy („Falunara — made for the minute after the shower“, „An oil, not a lotion — no water in the bottle“, „Goes on damp skin and settles in a minute“, „the water is already there and the oil holds it in place“); „30 Day Money Back Guarantee“; **keine** INCI, Reviews, klinischen Daten, Dermatologen-Bezüge, keines der Wörter crepey/firm/collagen/elasticity/mature/age; Text nennt 100 ml und 200 ml, Produkt-JSON zeigt eine Variante.

**Kernbefund Snapshot (VALIDIERT, Quelle [MB] + [AIS] + [VOC3]).** Der Markt ist laut, gesättigt und von einem Twin-Wettbewerber im gleichen Format und Preis besetzt. Die Kundinnen sind erfahren, preisverankert bei Drogerie/Costco und skeptisch.

---

## 2. Awareness and sophistication

**Awareness (Schwartz).** Upstream: Kernmarkt „überwiegend solution-aware bis product-aware“, breite Schicht „most aware, aber enttäuscht“ [MB Executive Summary, Awareness segmentation]. **VOC: bestätigt.** „Alles probiert“ ist stark wiederkehrend (Failed-Solution Bank #15: 55 rows / 37 threads / 9 communities) und Kundinnen nennen konkrete Produkte (AmLactin 147 rows / 44 threads; Gold Bond 84 rows / 31 threads) [VOC3 §6, P06, P07]. Das Wort „crepey“ ist Alltagssprache (169 rows / 51 threads / 10 communities) [VOC3 Phrase Bank A].

**Sophistication.** Upstream: Stufe 4–5 [MB Sophistication]. „Visibly firm“, „elasticity“, „non-greasy“ sind table stakes; Zahlen-Eskalation („82% … in two days“ Gold Bond; „100% agreed“ OSEA; „91% … in 8 weeks“ Crepe Erase); Evora attackiert den alten Mechanismus (Stufe 4); Sol de Janeiro/Besque/FALUNARA spielen Identifikation/Erlebnis (Stufe 5). **VOC: bestätigt und verschärft.** Marketing-Misstrauen 101 rows / 50 threads / 10 communities (P12), z. B. „You are basically paying $12 extra just for the word "firming".“ (C0463) und „they made up a fucking buzzword to fuck with people who never even thought anything about it before“ (C0641). → **Playbook-Einschätzung: VALIDIERT.** Ein schlichter Straffungs-Claim ohne Beleg wäre die schwächste Version eines gesättigten Claims [MB Messaging implications].

**Segmente** ([MB Segmentierung], ergänzt um VOC-Abdeckung)

| Segment [MB] | Stufe | VOC-Abdeckung | Playbook-Einschätzung |
|---|---|---|---|
| „Overnight Dry-Out“ | Problem Aware, eigene Bildsprache | **verstärkt**: Onset-Narrativ 116 rows / 34 threads (P08); Trockenheits-/Reptil-/Wüsten-Metaphern (33 rows / 23 threads; 15 / 13); Juckreiz/Schuppen 76 / 31 (P22) | KANDIDAT (gestärkt) – beste Passung für die Vorteile, die einem Öl geglaubt werden; Größe unbekannt |
| „Crepe Researchers“ | Solution Aware | **bestätigt**: Fragen-Kategorie 105 Zeilen; Transparenzforderung (A0185, A0272) | KANDIDAT – fehlende INCI ist hier Reibung |
| „Tried-Everything Skeptics“ | Product Aware, enttäuscht | **bestätigt**: Failed-Solution #15 (55 / 37); „Save your money. … Nothing works. Just wear long sleeves.“ (B0032) | VALIDIERT (Existenz); Ansprechbarkeit offen |
| „Medical/HRT Route“ | Solution/Product Aware | **relativiert**: HRT-Kontext 149 rows / 44 threads, aber „HRT hilft der Haut nicht zuverlässig“ (A0224, A0166) | Kontext, kein Produktthema [VOC3 F13] |
| „Settled Cheap-Staple Loyalists“ | Most Aware (andere Marke) | **verstärkt**: Preis-Wert 227 rows / 74 threads (P11); Neutrogena Sesame, Costco, Target-„bath oil“ „$3“ (B0541) | VALIDIERT – schwer zu $49 zu bewegen |
| „Acceptors“ | bewusst abgewandt | **bestätigt**: Akzeptanz 84 rows / 33 threads (P14), aber Gegenstimmen („I don’t want to embrace my body’s changes“, C0199) | VALIDIERT (Ton-Bedingung, kein Zielsegment) |
| *neu aus VOC:* „Body-Neglecters“ (Gesicht gepflegt, Körper vergessen) | Problem → Solution Aware | P18: 29 rows / 20 threads / 7 communities; „I’ve realized that I’ve completely neglected my skin below the neck.“ (A0001) | KANDIDAT (VOC-only; keine Werbe- oder [MB]-Spiegelung) |

**Altersbefund.** Evora-Erzählerinnen 56–64 (57 Ads) und Trustpilot-Reviewerinnen 61–69 liegen über FALUNARAs Kern 48–58 [CI §4], [MB]. VOC-Zeilen mit Altersangabe: 390 im Korridor 40–65, 175 im Kern [VOC3 §1]. → Konflikt §14.

---

## 3. Core customer language

*Alle Zitate verbatim aus [VOC3]/[VOCX] bzw. [MB]/[PW]; nicht übersetzt. Verwendung als Sprach-Referenz, nicht als Copy.*

**3.1 Begriffsfamilien mit Rekurrenz** [VOC3 Phrase Bank Teil A]

| Familie | Rekurrenz | Beispiel (VOC-ID) | Lesart |
|---|---|---|---|
| crepey / crepe / crepiness / crepefication | 169 / 51 / 10 | „slow down the crepefication“ (C0460) | Selbstbezeichnung; auch „creepy“ (13 / 7 / 4; „I’m 54 and I’m concerned about creepy skin.“ C0452) |
| on damp/wet skin, out of the shower | 105 / 46 / 10 | „The important part is to do it while you have water on your skin, so before toweling off.“ (C0044) | Anwendungswissen ist Allgemeingut |
| soft (as a baby’s butt/bottom) | 94 / 49 / 8 | „I’m almost 50 and my skin is soft as a baby.“ (A0017) | häufigstes positives Ziel |
| absorbs / sinks in / soaks in | 83 / 38 / 9 | „By the time I dry my hair and do my makeup, it’s pretty well absorbed - so like 30-45 minutes.“ (C0305) | Kaufkriterium |
| greasy / oily / slick | 75 / 42 / 9 | „Using body oil and lotion leaves it too greasy. Just lotion still seems to be not enough.“ (C0240) | Haupteinwand Öl |
| itchy / itching | 49 / 35 / 10 | „Some nights I felt like I was going to claw my skin off.“ (C0250) | Komfort |
| sticky / tacky / gluey | 47 / 31 / 9 | „I just bought this one and oh my gosh it is sticky ALL FREAKING DAY“ (C0304) | v. a. Lotionen/Actives |
| Reptil (lizard, snake, alligator, crocodile, dragon scales) | 33 / 23 / 8 | „My son calls my legs “dragon scales”“ (A0651) | Textur-Metapher |
| glow / glowy / sheen | 30 / 24 / 7 | „it's nice to look at my decolletage in the mirror now and see a hydrated glow!“ (A0482) | sekundär zu taktil |
| overnight / woke up | 29 / 15 / 6 bzw. 14 / 8 / 4 | „in your 40s one day you just wake up to find that your skin has aged a decade overnight“ (A0099) | Onset-Schock |
| lock in / seal (in) | 25 / 20 / 7 | „So the only real moisturizer is water. It's sealing it in that is the issue.“ (C0095) | Laien-Mechanismus |
| old lady / old woman / grandma / granny | 23 / 16 / 5 bzw. 10 / 9 / 5 | „I’m 53 and have granny hands and arms.“ (A0716) | Identität |
| sleeve(s) / sleeveless; shorts / skirts / sundress | 21 / 11 / 6 bzw. 15 / 11 / 3 | „I just want to hide them but short sleeve weather is coming. Help.“ (B0223) | Verhalten |
| smells like … (pee, sour milk) | 21 / 14 / 6 | „I really can’t handle smelling like cat pee.“ (A0299) | AmLactin-Schwäche |
| temporary / bandaid / pick your poison | 11 / 10 / 7 | „Nothing that is permanent. Lotions are just bandaids.“ (B0237) | Grunderwartung |
| hype / buzzword / marketing | 12 / 10 / 7 | „I do not see what the hype is on this stuff aside from its smells wonderful.“ (C0547) | Skepsis |

**3.2 Prägnante Einzelphrasen** (isoliert, hoher Sprachwert) [VOC3 Phrase Bank B]: „body dandruff“ (A0670), „My bra would look like a dandruff commercial.“ (A0671), „desert shins“ (A0806; Thread C029), „I felt like I was turning into a mummy in realtime!“ (C0196), „My hands look human when I look at them with my eyeballs. In photos it’s like they belong to Nosferatu.“ (B0181), „I got bat wings over night.“ (B0815), „spray down the tub/shower with shower cleaner afterwards or else it's a slippery death trap“ (C0042), „my skin just slurps it right up and asks for more“ (C0204).

**3.3 Sprache aus [MB]/[PW], die VOC bestätigt.** „crepe creep“, „crypt keeper“, „crocodile skin“, „turtle skin“ [MB Problem-language map]; „slick pig“ [PW Tradeoff]; „meteor of knowledge“ (Öl in der Dusche) [PW]. VOC bestätigt die Familien (Reptil, old lady, slick/greasy), die Einzelwörter stammen aus [MB]/[PW]-Threads (teils dieselben Threads, z. B. 1lwrmvw, 1fd0h17, otvj5z – siehe Überlappung §16).

**3.4 Marketer-Vokabular ohne Kundenbeleg** (nicht als Kundensprache behandeln): „kninkles“, „turkey skin“ (Körper), „elephant knees“, „chicken skin“ (= Keratosis pilaris) [MB „Was nicht auftaucht“]; „Natural Botox in a bottle“ (Evora-Visual) [CI §4]; „Fibroblast Failure“, „fat cushion layer“, „lotion lie“ [AIS M6], [SF OPEN-06]. „Confident“ kommt in Kundenevidenz kaum vor [PW Schwache Evidenz]; VOC-Treffer für „confident“ ist z. B. „I feel confident wearing my shorts and skirts.“ (B0124) – Einzelstimme.

**3.5 Sprach-Asymmetrie (Interpretation).** Die Kundin spricht zuerst **taktil und praktisch** (soft, absorbs, greasy, sticky, itchy, damp skin), dann **identitär** (old lady, grandma, mother’s arms), erst danach **strukturell** (firm, bounce, collagen: Desire Bank #7 nur 15 rows / 9 threads). Die Werbung spricht umgekehrt zuerst strukturell („visibly firm“, „reaches deeper“) [AIS D2, M2].

---

## 4. Validated / candidate desires

**4.1 Re-Check der AIS-Desires gegen VOC**

| AIS-Item | Upstream-Label | VOC-Befund | VOC-Verdikt | **Playbook-Einschätzung** | Begründung |
|---|---|---|---|---|---|
| **D1** Arme/Beine wieder zeigen | Validated · Hoch | Desire #4: 50 / 22 / 6; P10 Verstecken: 63 / 33 / 8; „It's summer! I wanna wear shorts without being self-conscious about my damn shins!“ (A0782) | bestätigt | **VALIDIERT** | Werbe- (9 Cluster) und Kundenevidenz konvergieren; [PW] Mass Desire #1. *Rangfolge-Konflikt* siehe 4.2 |
| **D2** „Crepey/old lady“-Look loswerden | Validated · Hoch | „crep…“ 169 / 51; Identität P09 98 / 49; **aber** Ziel bescheiden: Desire #5 16 / 12 („I don't mind looking my age, I just don't want to look older than I am!“ C0353) | bestätigt (Problem), abgeschwächt (Anspruch) | **VALIDIERT (eingeschränkt)** | Der Wunsch ist real; die Intensität „goodbye to crepey“ übersteigt die VOC-Erwartung („slow down“) |
| **D3** Weich, nicht schmierig, zieht ein | Validated · Mittel-hoch | Desire #1 taktil 120 / 62 / 8; Desire #2 Einziehen 127 / 49 / 10; P03 Gatekeeper 192 / 59 / 10 | **verstärkt** | **VALIDIERT (hoch)** | Stärkstes Kundensignal im gesamten VOC; Werbung nutzt es nur als Nebenzeile |
| **D4** Sich wieder wie man selbst fühlen | Validated · Mittel | Desire #8 29 / 16 / 6 (abgeleitet); P09 98 / 49 / 9; „I’m 52, but I’m not ready to have an old person’s body. It’s so depressing.“ (B0865) | verstärkt | **VALIDIERT** | Identitätsebene breiter belegt als upstream angenommen |
| **D5** Menopause-bedingte Veränderung | Validated · Mittel | P19 149 / 44 / 8, aber VOC wertet als „Kontext – nicht Produktthema“; HRT hilft Haut nicht zuverlässig (A0224, A0166) | bestätigt (Kontext), stumm (als Kaufmotiv) | **VALIDIERT als Kontext / KANDIDAT als Lead** | Menopause erklärt das „Warum“, ist aber kein eigener Kaufwunsch; Medizin-Nähe |
| **D6** Trockenheit lindern | Validated · Mittel | P02 Lotion hält nicht 162 / 67 / 10; P22 Juckreiz/Schuppen 76 / 31 / 7; Desire #3 Langzeit-Feuchtigkeit 90 / 54 / 10 | **verstärkt** | **VALIDIERT (hoch)** | Trockenheit ist für die Zielgruppe kein Neben-, sondern ein Hauptproblem |
| **D7** Post-GLP-1/Gewichtsverlust | Candidate · Mittel | P20 29 / 17 / 5 (VOC-Konfidenz „hoch“); „I’m over 60 and have lost nearly fifty pounds this year, great for the waistline but not so great for the skin.“ (B0514) | **verstärkt** (vs. [PW]: 4 Stimmen) | **KANDIDAT (gestärkt)** | Kundenseite jetzt wiederkehrend; Werbeseite verfehlt V2 weiterhin. Achtung: VOC2-Filter schloss reine „loose skin“-Threads aus → Untererfassung möglich |
| **D8** Ohne Nadeln/Eingriffe | Candidate · Niedrig-mittel | Prozedur-Frust 24 / 17 / 6 („I can't afford neck tox anymore. It works, but doesn't last.“ A0444); „Skincare only please. I’m not interested in treatments.“ (A0323, isoliert); Fatalismus P13 139 / 54 | gemischt | **KANDIDAT** | Kosten-/Enttäuschungsmotiv gegenüber Prozeduren belegt; „Nadelangst“ selbst nicht belegt |

**4.2 Desire-Rangfolge: zwei Lesarten (Konflikt, nicht aufgelöst)**

- [PW] rankt nach **Verhaltensbindung**: #1 „Bare my arms again“, #2 „not crepey/old“, #3 „soft, comfortable“ [PW Candidate mass desires].
- [VOC3] zählt nach **Thread-Rekurrenz**: taktile Ziele 120 / 62 und Einziehen 127 / 49 liegen deutlich vor Kleidungsfreiheit 50 / 22 [VOC3 Desire Bank].
- **Playbook-Lesart (Interpretation):** Kleidungsfreiheit ist das **emotionale Warum** (verhaltensgebunden, kauf-auslösend im Sommer); Weichheit/Einziehen ist das **funktionale Wie** (Erwartung an jedes Produkt, Abbruchgrund). Beide sind VALIDIERT; keine Rangfolge ohne Testdaten.

**4.3 VOC-Desires ohne AIS-Gegenstück**

| Desire | VOC | Werbe-Spiegelung | Playbook |
|---|---|---|---|
| Lang anhaltend, kein Nachcremen | Desire #3 90 / 54 / 10 | Crepe Erase „72 hours“, Gold Bond „24-hour“ [MB] | KANDIDAT (gestärkt) – nur mit Beleg kommunizierbar |
| Wenige Schritte, einfache Routine | Desire #9 97 / 46 / 8; Routine-Müdigkeit P15 122 / 51 | Evora „Two minutes a day“ (111 Ads, nur Evora) [CI §4] | KANDIDAT |
| Dezenter Duft **oder** duftfrei | Desire #10 75 / 36 / 7 vs. #11 39 / 26 / 10 | kaum (Sol de Janeiro Duft-Positionierung [MB]) | KANDIDAT – Segmentierungsvariable, FALUNARA-Duft unbekannt |
| Echte, nachvollziehbare Wirkung statt Hype | Desire #13 25 / 23 / 8 | Gegenteil der Werbe-Norm | KANDIDAT (gestärkt) |
| Glow | Desire #6 36 / 29 / 7 | Goda „Glowing Silky Smooth“ [SF HEAD-07] | VALIDIERT als Neben-Desire |
| Ritual / Selbstfürsorge | Desire #15 25 / 23 / 8 | FALUNARA-Website, Sol de Janeiro | KANDIDAT – [PW] führte es nur als Interpretation; VOC liefert nun direkte Belege (A0163, C0243) |
| Dickere, robustere Haut | Desire #16 28 / 12 / 5 | VitaeCharm/Besque Blutergüsse (CH7) | KANDIDAT – medizinische Claim-Nähe |
| Bezahlbarkeit | Desire #14 116 / 56 / 9 | Preisanker-Angle A5 | VALIDIERT (als Barriere, siehe §8) |
| Sinnlichkeit / Partnerberührung | [PW] D16 „kaum Evidenz“; VOC „husband“ 6 / 6 [PB-Nachzählung] (z. B. „My skin has never been softer - even my husband noticed.“ C0585) | Evora Ehemann-Pointe (A9) | KANDIDAT (schwach) |

---

## 5. Validated / candidate angles

| AIS-Item | Upstream-Label | VOC-Befund | VOC-Verdikt | **Playbook-Einschätzung** | Begründung |
|---|---|---|---|---|---|
| **A1** Anti-Creme: Lotionen versagen → Öl | Validated · Hoch | **Problemhälfte bestätigt**: P02 162 / 67 („Everything else doesn’t even come close to an hour before I have to put more on.“ C0194). **Lösungshälfte geschwächt**: Community-Benchmarks sind *Lotionen/Cremes* (AmLactin 147 / 44; Gold Bond 84 / 31; CeraVe „My New Fave for Crepey Skin!“ C086); Öl allein „too greasy“ oder „not enough“ (Failed-Solution #7: 44 / 30 / 10) | bestätigt + teilweise widersprochen | **VALIDIERT (eingeschränkt)** | „Lotion hält nicht“ ist Kundenwahrheit; „Cremes versagen grundsätzlich“ widerspricht den VOC-Erfolgsberichten mit Lotionen |
| **A2** Versteckte wahre Ursache / Myth-busting | Validated · Mittel-hoch | Trigger #15 „Derm sagt: das ist Alter“ 13 / 12 („They just said it was age. THIS ISN'T AGE“ C0666) vs. Fatalismus P13 139 / 54 und Buzzword-Skepsis (C0641) | gemischt | **VALIDIERT (eingeschränkt)** | Wunsch nach Erklärung existiert; erfundene Ursachen treffen auf „buzzword“-Misstrauen |
| **A3** Profi-/Insider-Empfehlung | Validated · Mittel-hoch | Esthetician 1 Zeile; Derm 16 / 14 gemischt („I honestly steer clear of those derms, they have an incentive to push expensive treatments.“ A0733); **Peer-Proof** P25 43 / 33 / 7 | abgeschwächt (Profi) / verstärkt (Peer) | **VALIDIERT (eingeschränkt)** | Im VOC kaufen Frauen auf Empfehlung *anderer Frauen*, nicht von Insidern |
| **A4** Dermatologen-/Klinik-Autorität | Validated · Hoch | Derm-Empfehlung wirkt teils („My doctor recommended the Neutrogena Sesame for my dry skin in the winter.“ A0580), teils Misstrauen (A0733, A0095) | gemischt | **VALIDIERT (Werbeverhalten) – für FALUNARA nicht zugänglich** | Ohne benannte, echte Expertise nicht nutzbar; unbenanntes „Dermatologist Approved“ (Evora PDP) ist Compliance-Beobachtung |
| **A5** Preisanker gegen teure Alternativen | Validated · Mittel | „I’ve spent so much money on fancy creams and lotions that buying Gold Bond from Walgreens feels like a real win for the wallet.“ (A0124); Prestige als Lehrgeld (Failed #6: 50 / 36 / 9). **Aber** Referenzpreis für Körperprodukte $10–30 (A0593, B0490) | gemischt | **VALIDIERT (eingeschränkt)** | Die „verschwendetes Geld“-Erzählung trägt; der Anker spricht aber eher **gegen** $49 als dafür |
| **A6** Wirkstoff-Upgrade „face-grade for body“ | Validated · Mittel-hoch | Retinol/AHA-Reizung (Objection #9: 32 / 22 / 10); Transparenz-Forderung (A0185); Gesichtsprodukte auf dem Körper (P18, C0422) | bestätigt (Segment) | **VALIDIERT – nicht anwendbar ohne INCI** | Abhängigkeit: Inhaltsstoffe |
| **A7** Natürlich / botanisch / kaltgepresst | Validated · Mittel-hoch | P24 39 / 23 / 7 (Natürlichkeit + Mineralöl-Angst) vs. „I do better with professionally formulated products.“ (A0412); ätherische Öle als Reizung (C0168) | bestätigt (Hygiene) | **VALIDIERT als table stakes** | Differenziert nicht gegen $3–20-Öle |
| **A8** Luxus-Insider (< $40 aus dem Luxus) | Candidate · Mittel (Evora-Control) | Keine Luxus-Aspiration im VOC; „luxurious“ nur sensorisch (C0535, C0430); „Nothing fancy“ als Lob (B0778, A0807) | **widerspricht** (Motiv) | **KANDIDAT (geschwächt)** | Evora-spezifisch, ohne Kundenmotiv; Nachbau = Evora-Klon |
| **A9** „Andere bemerken es“ / Ehemann | Candidate · Niedrig-mittel | 6 / 6 [PB-Nachzählung]; gemischt (C0585 positiv; „my husband thinks I’m crazy because he doesn’t see it“ A0158) | leicht verstärkt | **KANDIDAT** | Als Nebenmotiv belegbar, Partner-Sinnlichkeit weiterhin nicht |
| **A10** Drittanbieter-Vergleich / Ranking | Candidate · Mittel | Kundinnen vergleichen selbst (C0463 INCI-Vergleich), sind überfordert (C0533), aber erkennen Werbung („Is this an ad?“ C0482; „Did Amlactin hire a social media team or what?“ A0054) | gemischt, Risiko verstärkt | **KANDIDAT (Compliance-kritisch)** | Pseudo-redaktionelle Rankings (skinglowmagazine „Top 5“ mit Evora A+) sind eine **Forschungsbeobachtung mit Täuschungsrisiko** |

**Neue Angle-Kandidaten aus VOC (ohne Werbe-Validierung):** (a) **Anwendungs-Aufklärung** Öl vs. Lotion, Reihenfolge, feuchte Haut (P04 168 / 58 / 10; „Wait, oil goes on top?“ C0503) – KANDIDAT; (b) **„Vergessene Körperzone“** (P18) – KANDIDAT; (c) **Ehrliche Zeitachse** „Gefühl sofort, Optik nach Monaten“ (P21 81 / 45 / 8) – KANDIDAT (siehe CH5).

---

## 6. Validated / candidate mechanisms

**6.1 Re-Check der AIS-Mechanismen**

| AIS-Item | Upstream-Label | VOC-Befund | VOC-Verdikt | **Playbook-Einschätzung** | Begründung |
|---|---|---|---|---|---|
| **M1** Cremes 70–80 % Wasser, verdunsten, bleiben an der Oberfläche | Validated · Hoch | Erlebnis „Lotion hält nicht“ 162 / 67 bestätigt. **Die Erklärung „Wasser ist das Problem“ kollidiert mit dem Laienmodell „Wasser ist der eigentliche Feuchtigkeitsspender“**: „So the only real moisturizer is water. It's sealing it in that is the issue.“ (C0095); „I needed to seal the moisture in my skin vs add moisture externally and have it mostly evaporate.“ (C0122). Wasser-/Verdunstungs-Sprache selbst nur 2 Zeilen [PB-Nachzählung] | bestätigt (Erlebnis) / teilweise widersprochen (Erklärung) | **VALIDIERT als Werbeverhalten; KANDIDAT als kundenkonforme Erklärung** | Die Kundin glaubt nicht, dass Wasser schlecht ist, sondern dass es *versiegelt* werden muss |
| **M2** Öl durchdringt die Lipidbarriere, erreicht tiefere Schicht | Candidate · Mittel (umstritten), V4 verfehlt | Objection #5 „Öl versiegelt nur“ **48 / 31 / 9**, stark wiederkehrend („oil doesn’t actually hydrate the skin, it is just creating a barrier“ C0505). Gegenstimmen: „Some oils have molecular weights small enough to penetrate several layers deep into the stratum corneum, where they replace lost lipids.“ (B0581), „much more absorbent“ (A0404) – Minderheit; „penetrat/deeper“ gesamt nur 6 / 5 [PB-Nachzählung], davon meist auf Peeling bezogen | **widerspricht** (bestätigt den upstream-V4-Befund mit Primär-VOC) | **KANDIDAT (geschwächt) – Claim-Risiko hoch** | Experten nennen Öle okklusiv [MB]; keine Quelle stützt „where crepey skin starts“. „Zieht schnell ein“ (Sensorik) ≠ „dringt tief ein“ (Wirkung) |
| **M3** Feuchte Haut direkt nach der Dusche | Validated · Mittel | **P01 132 / 50 / 10**, nahezu Konsens; „Body oil after shower, but before drying off“ (B0544). Gegenstimmen: Ungeduld (B0563), rutschige Dusche (C0042), Mietwohnung/Rohre (C0179), Pumpe mit öligen Händen (C0488) | **verstärkt** | **VALIDIERT (hoch) – nicht differenzierend** | Experten [MB], Kundinnen [VOC3] und FALUNARA-Website sagen dasselbe; Babyöl/Neutrogena funktionieren identisch [MB Messaging implications] |
| **M4** Peptide/Retinoide bauen Kollagen auf | Validated · Mittel-hoch | Retinol-Fehlschläge 15 / 13; Reizung #9 | bestätigt (Segment) | **VALIDIERT – nicht anwendbar ohne INCI** | Abhängigkeit Inhaltsstoffe/Studien |
| **M5** Lipid-Ersatz „replaces what skin stopped making after 50“ | Candidate · Niedrig-mittel (nur Evora) | Einzelstimme B0581 („replace lost lipids“); AAD „skin loses some ability to hold water“ [MB]; VOC „body cannot retain moisture anymore“ (B0722) | leicht verstärkt (Problem), stumm (Mechanismus) | **KANDIDAT** | Erfahrung „Haut hält Feuchtigkeit nicht mehr“ belegt; Lipid-Ersatz als Wirkmechanismus braucht Formel- und Studienbeleg |
| **M6** Proprietäre Einzel-Ursachen (Fibroblast Failure, Fat cushion, TEWL, PDRN) | Candidate · Niedrig | Buzzword-Misstrauen (C0641, C0463) | widerspricht (Ton) | **KANDIDAT (geschwächt)** | Erfundene Ursachen-Namen treffen auf aktive Skepsis |

**6.2 Mechanismus-Landkarte für ein Öl (Playbook-Synthese)**

| Ebene | Was Kundinnen glauben (VOC) | Was Experten sagen ([MB]) | Was die Werbung sagt ([AIS]) | Glaubwürdigkeit für FALUNARA (Interpretation) |
|---|---|---|---|---|
| Anwendung | Öl auf feuchte Haut (P01) | „immediately after showering“, „on damp skin“ (Garshick, Queller, AAD) | „Two minutes a day after the shower“ (Evora) | **hoch**, aber generisch |
| Wirkprinzip | versiegeln/„lock in“ (Obj. #5, 25 / 20 „lock in/seal“) | okklusiv + emollient | „melts through the barrier“ | Versiegeln **hoch**; Tiefenwirkung **niedrig** |
| Ergebnis-Zeit | Gefühl sofort, Optik Monate (P21) | „temporarily improve the appearance“ (Fenton) | „3–4 weeks“, Week 8–12 (Evora) | Gefühl-Versprechen tragfähig nur mit Sensorik-Test; Optik-Versprechen nur mit Studie |
| Struktur | „nothing is going to tighten it up“ (A0576); Hormone/Training/Prozeduren | Retinoide, Laser, RF; „cannot be completely eliminated“ (nur Suchzusammenfassung) | „visibly restores firmness“ | **nicht belegbar** ohne Daten → Compliance-sensibel |

**6.3 Hinweis zu FALUNARAs eigener Website-Logik.** „the water is already there and the oil holds it in place“ [MB] deckt sich fast wörtlich mit dem VOC-Laienmodell (C0095) und der Expertensicht. „An oil, not a lotion — no water in the bottle“ liegt dagegen nahe an M1/CT1 (Evora-Rahmung „70–80% water“) – Risiko der Verwechselbarkeit mit dem Twin (Interpretation).

---

## 7. Big Ideas

**7.1 Upstream-Big-Ideas, neu bewertet**

| AIS-Item | Upstream-Label | VOC-Verdikt | **Playbook-Einschätzung** | Begründung |
|---|---|---|---|---|
| **B1** „Falsches Format, nicht falsches Produkt“: Cremes erreichen die Stelle nie | Validated · Hoch | Problem bestätigt (P02); „erreichen die Stelle“ widersprochen (Obj. #5); Lotion-Benchmarks erfolgreich (P06, Thread C086) | **VALIDIERT (eingeschränkt)** als Werbe-Control; für FALUNARA durch Evora besetzt und mechanistisch angreifbar |
| **B2** „Nicht das Alter – eine benannte, versteckte Ursache“ | Validated · Mittel | gemischt (C0666 vs. P13, C0641) | **VALIDIERT (eingeschränkt)** als Template; einzelne Ursachen = KANDIDAT (geschwächt) |
| Evora Luxus-Insider („das eine Fläschchen im Milliardärshaus“) | Candidate (Evora-Control, A8/S3) | widerspricht (kein Luxusmotiv; „Nothing fancy“) | **KANDIDAT (geschwächt)** |

**7.2 Big-Idea-Territorien für künftige Tests – nur Territoriumsbeschreibungen, keine Headlines, Status HYPOTHESE**

| # | Territorium (Beschreibung) | Evidenz-Anker | Abgrenzung zu Evora | Status / Abhängigkeit |
|---|---|---|---|---|
| BI-1 | **„Die Minute nach der Dusche“** – der Moment, in dem Wasser noch auf der Haut ist, als eigentlicher Ort der Körperpflege; Öl als Werkzeug dieses Moments | P01 (132 / 50), Trigger #9, Experten [MB], Website „made for the minute after the shower“ | Evora nutzt „after the shower“ nur als Bullet („Two minutes a day…“); Ritual als Lead ist werblich kaum besetzt (CH3) | HYPOTHESE · braucht Sensorik-Daten (Einziehzeit) |
| BI-2 | **„Wasser ist schon da – es fehlt das Festhalten“** – kundenkonforme Erklärung (versiegeln statt „tief eindringen“) | C0095, C0122, Obj. #5, Garshick/Queller [MB] | Gegenmodell zu M2 („melts through the barrier“) | HYPOTHESE · Claim-Prüfung; nicht differenzierend gegen Billig-Öle allein |
| BI-3 | **„Erst das Gefühl, dann – mit Geduld – das Bild“** – ehrliche Zeitachse in einem Markt der „2 days/2 minutes“-Versprechen | P21 (81 / 45), B0851 „a little over three months“, „I don't expect miracles“ [MB], CH5 | Evora „See real results in 3–4 weeks“; Gold Bond „two days“ | HYPOTHESE · Optik-Aussagen erst mit Studie |
| BI-4 | **„Der vergessene Körper“** – Gesicht seit Jahren gepflegt, Körper nie; Wendepunkt-Moment | P18 (29 / 20), F1 (A0001, C0422), Onset P08 | Werblich unbesetzt (keine AIS-Entsprechung) | HYPOTHESE · VOC-only |
| BI-5 | **„Pflege ohne Kampf“** – mildern statt bekämpfen; Akzeptanz und Pflege zugleich | [PW] Mass Desire #5 (Tonbedingung), P14 (84 / 33), „I've decided instead of fighting it, just mitigate it.“ [PW] | Gegenpol zur Fix-/Reverse-Rhetorik | HYPOTHESE · Ton, nicht Claim; Absenz-Signal ≠ Performance |

---

## 8. Objections and belief barriers

**Einwandkette für ein $49-Öl** [PW Konkrete Einwände]: „Kann Öl überhaupt etwas gegen crepey?“ → „$49 statt $10-Mandelöl?“ → „schmiert, färbt, reizt?“ → „Abo-Falle?“. VOC-Prüfung je Glied:

| # | Einwand / Glaubensbarriere | Upstream | VOC (Rekurrenz, Beleg) | VOC-Verdikt | Playbook-Status | Kreative Relevanz (Forschung, keine Copy) |
|---|---|---|---|---|---|---|
| E1 | **Topika wirken nicht / nur Eingriffe, Hormone, Training** | [MB] Einwand 3–4; [PW] hoch (≥6) | Obj. #8 59 / 33 / 7; P13 139 / 54 / 9; „I have been the queen of creams my entire life. But at age 67 there is nothing to stop it. Nothing.“ (B0086) | bestätigt | **VALIDIERT** | Jede Struktur-Aussage trifft auf Gegenwehr |
| E2 | **Nur temporär** | [MB] Einwand 2 | Obj. #14 30 / 24 / 7; „creams like Crepe Erase are very effective. However, the crepey skin returns if you stop using. Pick your poison!“ (A0746) | bestätigt | **VALIDIERT** | Grunderwartung, nicht Ausnahme |
| E3 | **Öl versiegelt nur, hydratisiert nicht** | [MB] „oil only seals“ | Obj. #5 48 / 31 / 9 | bestätigt | **VALIDIERT** | Gegen M2; mit BI-2 vereinbar |
| E4 | **Fettig, färbt ab, Warten vor dem Anziehen** | [MB] Einwand 7; [PW] Tradeoff | Obj. #3 70 / 38 / 9; Gatekeeper P03 192 / 59; „Then I put on the terrycloth robe for a half hour before getting dressed so it can absorb into my skin (and the robe, lols).“ (B0087) | **verstärkt** | **VALIDIERT (hoch)** | Wichtigster Öl-spezifischer Einwand |
| E5 | **Klebrig / filmig** (v. a. Lotionen/Actives) | [PW] | Obj. #4 41 / 29 / 7 | bestätigt | **VALIDIERT** | Abgrenzungsfeld für Öl-Textur (nur testen, nicht behaupten) |
| E6 | **Preis nicht gerechtfertigt / DIY reicht** | [MB] Preisanker; [PW] niedrig-mittel (1–2 Stimmen zu ~$50) | Obj. #6 118 / 56 / 9; P11 227 / 74. Preis-Belege [PB-Nachzählung]: „Do not spend more than like $20 on a bottle for big brand names.“ (A0593); „I don’t think I’d spend more than $20-$30 on a body product“ (B0490); „There was an oil on Facebook they were selling last Christmas for $70.00 for 16oz. Way too expensive“ (B0039); „I thought ok $55 I'll give it a try … I didn't know it was TINY“ (B0097); „Osea is very expensive so this has become my holy grail.“ (B0065). Gegenstimme: „Pricey, but the older I get the pickier I am about what I put on my skin.“ (A0406) | **verstärkt** (vs. [PW] „niedrig-mittel“) | **VALIDIERT (hoch)** | $49 liegt über dem VOC-Referenzband; Menge pro Dollar wird beachtet (B0097) |
| E7 | **Marketing-Misstrauen / Hype / Transparenz** | [PW] „mostly marketing“; [MB] Einwand 6 | Obj. #7 92 / 48 / 10; P12 101 / 50 | **verstärkt** | **VALIDIERT (hoch)** | Fehlende INCI ist für „Crepe Researchers“ ein Ausschlussgrund |
| E8 | **Abo-/Billing-Falle** | [MB] Einwand 5; [PW] hoch (Trustpilot) | **0 relevante Zeilen** (einzige Fundstelle „subscription for HRT“ B0213); Thread-Cache-Grep findet keine Abo-Beschwerde [PB-Nachzählung] | **stumm** | **KANDIDAT** (Evidenz nur Trustpilot [WP] + Aggregatoren) | Siehe §11, §13 CH2, §14 |
| E9 | **Duft: zu stark / reizt** vs. **unparfümiert riecht „plastic“** | [PW] Rang 3 | P05 181 / 59 / 10; Obj. #2 22 / 15 / 8; „the smell of scented lotions have started making me upset“ (C0363) vs. „I don't like the fake plastic smell.“ (C0291) | **verstärkt** | **VALIDIERT (Polarisierung)** | FALUNARA-Duft unbekannt → kritische Abhängigkeit |
| E10 | **Reizung durch Actives** (AHA, Retinol, Gold Bond) | [PW] #40 | Obj. #9 32 / 22 / 10; „DO NOT USE Gold Bond Crepe corrector“-Thread (C026) | bestätigt | **VALIDIERT** (Wettbewerberschwäche) | Nur relevant, wenn FALUNARA-Verträglichkeit belegt ist |
| E11 | **Rutschige Dusche / Dosieren mit öligen Händen** | [PW] Verpackung dünn | Obj. #10 11 / 8 / 5; „it's a little hard to squirt when I'm all slippery and oily in the shower“ (C0488); Pumpe bevorzugt (A0597) | neu | **KANDIDAT** | Glasflasche in der Dusche: **keine** VOC-Evidenz (weder pro noch contra) – Sicherheitsfrage offen |
| E12 | **Zu aufwendig / vergesse es** | [PW] Comfrey-Abbruch | Obj. #13 81 / 43 / 7; „I’m waaaaay to impatient…“ (B0563) | verstärkt | **VALIDIERT** | Adhärenz ist Voraussetzung für jedes Ergebnis |
| E13 | **Inhaltsstoff-Ängste** (Mineralöl, „chemicals“) | – | Obj. #11 23 / 17 / 6 | neu | **KANDIDAT** | Botanische Basis könnte passen – nur mit INCI |
| E14 | **Reformulierung / Fälschung (Amazon)** | [MB] Einwand 6 | Obj. #12 12 / 7 / 5 | bestätigt | **KANDIDAT** | Bezugsquelle/Formelkonstanz |
| E15 | **„Lieber Lotion als Öl“ / schwere Texturen bevorzugt** | [PW] niedrig-mittel | P03-Gegenevidenz „Heavy,heavy moisturizers.“ (A0132); Kontra „I hate the feeling of stuff on my body“ (C0086) | bestätigt (Segment) | **KANDIDAT** | Texturpräferenz ist segmentabhängig [VOC3 §9] |
| E16 | **Anti-Aging-Marketing verkauft Unsicherheit** | [PW] niedrig-mittel, tonprägend | „women ads: you have all these flaws, if you buy these products, maybe you can fix some of them.“ (C0640); „I got bombarded with ads…“ (C0533) | bestätigt | **VALIDIERT (Ton-Barriere)** | Spricht gegen „old lady“-Shaming als Hook |

---

## 9. Proven / recurring hooks and story structures

*„Proven“ heißt hier nur: lang laufend und/oder repliziert im Werbesample. Kein Performance-Beleg. Texte sind Wettbewerber-Copy aus [SF] und dürfen nicht übernommen werden.*

**9.1 Hooks – Re-Check**

| AIS-Item | Upstream | Stärkster Beleg (Ad-ID) | VOC-Verdikt | **Playbook** | Begründung |
|---|---|---|---|---|---|
| **H1** Zonen-/Vermeidungs-Frage | Validated · Hoch | „Ever avoid wearing shorts because of sagging or creepy skin?“ [SF HOOK-02, 1637558804018844, 117 Tage, 30 IDs/2 Seiten] | bestätigt (P10; A0080) | **VALIDIERT** | Spiegelt reales Vermeidungsverhalten; beachte: NØRD nutzt „creepy“ – Kundinnen-Falschschreibung |
| **H2** Zitiertes Ich-Testimonial mit Wendepunkt | Validated · Hoch | „"Dryness, saggy and crepey skin... I struggled with it all for years until I realized I was doing it all wrong. 😨"“ [SF HOOK-01, 4109833019265205, 314 Tage; Konzept 29 IDs/4 Seiten] | bestätigt (Peer-Proof P25) | **VALIDIERT – setzt echte Kundenstimmen voraus** | Evora-Footer: Testimonials teils vergütet [MB]; FTC-relevante Offenlegung = Compliance |
| **H3** Anti-Creme-Opener | Validated · Hoch | „Let's be honest — most body firming lotion and creams don't actually work.“ [SF HOOK-07, 1570129684499222] | teilweise widersprochen (siehe A1) | **VALIDIERT (eingeschränkt)** | |
| **H4** Alter + Zone im ersten Satz | Validated · Mittel-hoch | „At 48, my neck and arms looked like crepe paper…“ [SF HOOK-09] | **verstärkt** – genau so sprechen Posterinnen: „I am 56 and my arms are very crepey.“ (B0092); „I’m 53 and have granny hands and arms.“ (A0716) | **VALIDIERT** | Natürliches Sprachmuster der Zielgruppe |
| **H5** „Women over 50“-Call-out | Validated · Mittel-hoch | „💸 Women Over 50 Are Ditching $400 Worth of Creams For This“ [SF HOOK-06, 99 Tage] | gemischt (Age-gated Subs vs. Akzeptanz/Anti-Label P14) | **VALIDIERT (eingeschränkt)** | Kern 48–58 beginnt unter 50 |
| **H6** Geständnis-/Verbots-Opener | Candidate (Evora) | „I'm probably going to get fired for posting this…“ [SF HOOK-21] | stumm | **KANDIDAT** | |
| **H7** „Weird/odd oil“-Neugier | Candidate (Evora) | „The butler brought me this “weird” oil“ [SF HEAD-17] | stumm | **KANDIDAT** | |
| **H8** Pseudo-organische Frage ohne Link | Candidate, Authentizitätsrisiko | „My body skin looks 10 years older than my face what do you use for crepey arms regular lotion doesnt help anymore“ [SF HOOK-24, 308 Tage] | Zielgruppe erkennt Seeding (A0054; VOC schloss 36 Seeding-Zeilen aus) | **KANDIDAT – Compliance-Beobachtung, nicht als Taktik** | Sprachlich deckungsgleich mit VOC (A0814 „My hands look ten years older than my face.“) |

**9.2 Natürliche VOC-Erzählmuster (Beobachtung, keine Hooks)**: Onset-Moment („woke up“, „overnight“; P08), Mutter-Spiegel (Trigger #5, 27 / 19; „how did my mother's hands get here?“ A0850), Sicht-Moment (Gym, Schaufenster, Foto; Trigger #4 20 / 16), Saison-Moment (Sommer 63 / 33; Winter 51 / 32), Peer-Empfehlung → Kauf (P25). Diese Muster tauchen in der Werbung teils auf (Sommer/Ärmel), teils nicht (Winter, Mutter-Spiegel, Körper-Vernachlässigung) → §13.

**9.3 Story-Strukturen – Re-Check**

| AIS-Item | Upstream | VOC-Verdikt | **Playbook** | Begründung |
|---|---|---|---|---|
| **S1** Testimonial-Transformation: alles probiert → Tipp → Skepsis („greasy?“) → Wochen → ärmellos [SF OPEN-01] | Validated · Hoch | bestätigt: VOC-Erfolgsberichte folgen dem Bogen, inkl. Einschränkung („it hasn't repaired it but doesn't seem to have gotten worse“ [PW]; B0851) | **VALIDIERT** – glaubwürdig nur mit Alter + Zone + Dauer + moderatem Ergebnis + Einschränkung [PW Vertrauen] | |
| **S2** Kurzes DR: Call-out → Reason-why → Bullets → Garantie [SF OPEN-02/03] | Validated · Hoch | stumm (Format) | **VALIDIERT (Format)** | |
| **S3** Luxus-Insider-Long-form [SF OPEN-08/09] | Candidate (Evora) | widerspricht (Motiv) | **KANDIDAT (geschwächt)** | |
| **S4** Lebensereignis (Witwe/World Cup, Hochzeit) [SF OPEN-11] | Candidate | **stumm**: Anlass-/Hochzeits-Suche ergibt keine relevanten Zeilen [PB-Nachzählung]; [PW] nur 1 Fall | **KANDIDAT (geschwächt)** | |
| **S5** Advertorial-Listicle-Lander | Candidate | stumm | **KANDIDAT** | |
| *Ergänzung:* Saisonale Ich-Erzählung Winter („I need to tell you about the lotion lie.“ [SF HOOK-11/OPEN-06], Goda, 150 Tage, gestoppt) | nicht als eigenes Item | **verstärkt** (P23 86 / 48; Winter 32 / 21 [PB-Nachzählung]) | **KANDIDAT** (1 Langläufer) | Werblich selten, kundenseitig breit |

---

## 10. Creative and visual patterns

| AIS-Item / Muster | Upstream | Beobachtung | VOC-Verdikt | **Playbook** | Kommentar |
|---|---|---|---|---|---|
| **C1** Native Persona-Seiten tragen Long-form | Validated · Hoch (Distribution) | Evora 5 Persona-Seiten (Natalie Brooks 576 Library-Ads), Goda „Over 40 & Fabulous“ 314 Tage, Frøya „Anne's Skincare Blog“ 586 Tage [AIS C1] | Risiko verstärkt („Is this an ad?“ C0482; A0054) | **VALIDIERT als Wettbewerberverhalten – Compliance-Beobachtung** | Persona-Seiten, die wie unabhängige Personen/Blogs wirken, sind eine Authentizitäts- und Täuschungsfrage; hier nur dokumentiert |
| **C2** Textlastige Long-form-Bildanzeigen | Validated · Mittel-hoch | 143 Anzeigen / 9 Cluster | stumm | **VALIDIERT (Format)** | |
| **C3** DCO mit fixem Hook | Validated · Mittel | DRMTLGY 53 IDs, 185 Tage | stumm | **VALIDIERT (Format)** | |
| **C4** Story-Video-Shell (AI-Szenen, Green-Screen-Erzählerin) | Candidate (Evora, ≤42 Tage) | 41 IDs, collation 91 | stumm; AARP: 61 % fühlen sich in Medien nicht repräsentiert, 58 % kaufen eher bei Marken mit ähnlichen Models (2018, [WP]) [PW] | **KANDIDAT** | AI-generierte Personen in Testimonial-Nähe = Compliance-Beobachtung |
| **C5** Vorher/Nachher, Arm-neben-Arm | Candidate | Goda „BEFORE GODA / 2 WEEKS ON GODA“; theskinmag „Her arm. My arm.“ | gemischt: „The neck in the after photo is pulled tighter and smoother because the chin is higher. So "results" are false.“ (A0449) vs. „The pics I saw online of before and after were enough for me to give it a shot!“ (A0830) | **KANDIDAT** | Untypische Vorher/Nachher bei Crepe Erase kritisiert [MB, Aggregator] |
| **C6** Klinische Prozent-Karte | Candidate (V3) | „93% saw smoother-looking neck skin after 4 weeks“ [SF HEAD-18] | stumm zu Studien-%, aber Forderung nach **Konzentrations-%** (A0185, A0272) | **KANDIDAT – ohne eigene Studie nicht verfügbar** | |
| Evora-Offer-Visuals | – | „EVORA SENIOR SALE – ENDS MIDNIGHT“, Maskottchen „Almost sold out… Restock in 2 months“, „NATURAL BOTOX IN A BOTTLE?“ [CI §4] | stumm | Beobachtung | „Natural Botox“-Vergleich = Claim-Risiko |
| **Produkt-Hero-Shot Klarglas, goldenes Öl, weiße Pumpe** (Evora) | AIS CH-Beobachtung 8 | Identisch mit FALUNARAs Format [CI §6.8] | VOC: Pumpe bevorzugt (A0597), Glas ohne Evidenz | **VALIDIERT als Verwechslungsrisiko** | Visuelle Differenzierung ist offene Abhängigkeit (Packaging) |
| Macro-Textur auf Haut (VitaeCharm Unterarm), Zonen-Fokus Arm | – | [CI §4] | VOC-Zonen: Arme 39 Threads, **Beine 35**, Hände 19, Knie 13, Brust 11 (P17) | KANDIDAT | Werbung zeigt fast nur Arme (219 Anzeigen) vs. Beine/Knie 59 [AIS D2] |

**Fehlende visuelle Evidenz:** Video-Inhalte nicht transkribiert, nur 40 Thumbnails gesichtet [CI §7]; keine VOC-Bildanalyse. Visuelle Aussagen bleiben daher Kandidaten.

---

## 11. Offer / landing-page patterns

**11.1 Offer-Items – Re-Check**

| AIS-Item | Upstream | VOC-Verdikt | **Playbook** | Begründung / FALUNARA-Status |
|---|---|---|---|---|
| **O1** 60–90-Tage-Garantie als Headline | Validated · Hoch (Prävalenz) | **stumm** (0 Zeilen zu guarantee/refund [PB-Nachzählung]); indirekt: Probier-Wunsch „I would caution anyone not to blind buy a full bottle“ (C0410), „Get the travel size to see if you like it.“ (A0666), „I wish I could smell it before buying!“ (C0577) – 6–7 Zeilen | **VALIDIERT als Kategorie-Standard; Kundenwirkung unbelegt** | FALUNARA „30 Day Money Back Guarantee“ < DTC-Standard 60–90 Tage [MB]; Evora-Garantie schließt Versand aus [CI] |
| **O2** %-Rabatt + Deadline | Validated · Hoch | Rabattjagd belegt („This is a good time to hunt for a discount set“ B0636; Costco-Sale A0019); Deadline/Scarcity stumm | **VALIDIERT (Prävalenz)** | Evora: Preisdiskrepanz „ad said $28 a bottle…“ [MB, WP] |
| **O3** Bundles / BOGO | Validated · Mittel | Größe/Menge zählt („I didn't know it was TINY“ B0097; „big bottle“ A0354, A0786) | bestätigt (Menge pro $) | **VALIDIERT** | FALUNARA: 100/200 ml im Text, 1 Variante im JSON → offen |
| **O4** Knappheit / Live-Bestand („437 Orders in Last Hour — Almost gone“) | Validated · Mittel | stumm; Misstrauen-Kontext | **VALIDIERT (Prävalenz) – Compliance-Beobachtung** | Unverifizierbare Echtzeit-Bestandsangaben sind ein Täuschungsrisiko |
| **O5** Abo vorausgewählt + „BUY ONCE - NO SAVINGS →“ | Candidate (V4: Abo-Beschwerden) | **stumm** – Reddit-VOC enthält keine Abo-Klagen | **KANDIDAT (unverändert), aber Evidenzbasis enger als upstream dargestellt** | Widerspruch beruht allein auf Trustpilot/BBB/Aggregatoren [MB, PW] (WP) – plausibel, aber nicht durch Primär-VOC gedeckt. Negative-Option-/Auto-Renewal-Gestaltung ist in den USA regulatorisch sensibel → rechtlich prüfen (Beobachtung, keine Rechtsauskunft) |
| **O6** Anlass-Sale (Labor Day, BFCM, „SENIOR SALE“) | Validated · Mittel | stumm | **VALIDIERT (Prävalenz)** | |
| **O7** Social-Proof-Zahlen („50,000+“) | Validated · Mittel | Peer-Proof wirkt im VOC über Communities, nicht Kundenzahlen (P25); YouGov 66 % Reviews wichtig [PW, WP] | **VALIDIERT (eingeschränkt)** | FALUNARA hat keine Reviews; Evora-Zahlen widersprüchlich (1113 / 1560 / „50.000+“) [MB] |
| **O8** Gratis-Geschenke / XL | Candidate | Menge zählt (s. O3) | **KANDIDAT** | |

**11.2 Landingpage-Muster** [CI §4], [AIS S5]

- **Evora PDP** (195 von 218 Ads verlinken direkt): $49/$69, 3 Bundle-Stufen, vorausgewähltes Abo, „89% sold“-Balken, 90-Tage-Garantie, Lipidbarrieren-Mechanismusblock, 6 Hero-Ingredients + volle INCI, Wochen-Timeline bis „Week 8-12“ („Sleeveless tops. Bracelets.“), „vs Others“-Tabelle, unbenanntes „Dermatologist Approved“.
- **Sekundär:** 7-Reasons-Listicle, Quiz mit Altersfilter und $105-Rabatt, drittanbieter-artiges „Top 5“-Ranking (skinglowmagazine; Evora A+, Goda C, Besque D+) → **Compliance-Beobachtung** (verdeckte Eigenwerbung).
- **Wettbewerber:** Advertorial-Listicles (NØRD, VitaeCharm, TurmSkin), Ich-Long-form-Lander („Down 38 Pounds…“, „1973 Nobel Prize Discovery“), Affiliate-Prelander/VSL/Quiz (Miami MD). NØRD-Lander: „No subscription · No auto-ship, ever“ [AIS CH2].

**11.3 FALUNARA-Lücken gegenüber Kategorie-Standard und VOC** (Befund, keine Empfehlung)

| Element | Kategorie-Standard | VOC-Relevanz | FALUNARA laut [MB] |
|---|---|---|---|
| INCI / Konzentrationen | Evora volle INCI | P12 Transparenz 101 / 50 | fehlt |
| Reviews / Peer-Proof | Trustpilot/Onsite | P25 43 / 33 | fehlt |
| Garantie | 60–90 Tage | stumm | 30 Tage |
| Probiergröße / Duftinfo | OSEA Travel Size [VOC A0666] | Trial 7 / 7; Duft P05 | unbekannt / 1 Variante |
| Anwendungserklärung | Evora „Two minutes…“ | P04 168 / 58 | vorhanden („Goes on damp skin…“) – Sensorik-Claim muss belegbar sein |
| Kaufbedingungen ohne Abo | Abo-Default bei Evora/Goda/VitaeCharm | VOC stumm, Trustpilot laut | kein Abo erwähnt (Status unklar) |
| Name/Domain-Konsistenz | – | Fälschungsangst Obj. #12 (12 / 7) | „Falunara“ vs. „Falurana“ |

---

## 12. Control territories

*Control = über mehrere unabhängige Advertiser persistent bespielt. Beschreibt Wettbewerberverhalten, ist keine Empfehlung [AIS §4].*

| # | Territorium | Upstream | VOC-Re-Check | **Playbook-Einschätzung** | Folgerung für FALUNARA (Forschungssicht) |
|---|---|---|---|---|---|
| **CT2** | „Arme (und Beine) nicht mehr verstecken“ (D1 + H1) | Validated · Hoch | bestätigt (P10 63 / 33; Desire #4 50 / 22) | **VALIDIERT – stärkste Konvergenz Werbung × VOC** | Pflicht-Desire, allein nicht differenzierend. Sommer-Trigger kollidiert mit Öl-Schmierigkeit [PW] |
| **CT3** | Zitiertes Ich-Testimonial mit Transformationsbogen (H2 + S1 + A3) | Validated · Hoch | bestätigt (Peer-Proof P25), A3-Insider-Teil abgeschwächt | **VALIDIERT – nur mit echten, offengelegten Kundenstimmen** | FALUNARA hat keine Reviews → derzeit nicht bespielbar ohne Fabrikation (ausgeschlossen) |
| **CT5** | Angebots-Stack: Rabatt + Deadline + 60–90-Tage-Garantie (+ Knappheit, Bundles) | Validated · Hoch (Prävalenz) | Rabatt-/Mengen-Sensibilität bestätigt; Garantie/Deadline/Knappheit stumm | **VALIDIERT als Mindeststandard; Wirkung unbelegt** | 30-Tage-Garantie unter Standard; Knappheits-Elemente nur wahrheitsgemäß (Compliance) |
| **CT1** | „Cremes versagen – Öl ist das richtige Format“ (A1 + B1 + M1) | Validated · Hoch | Problem bestätigt; Lösungshälfte widersprochen (Obj. #5), Lotion-Benchmarks erfolgreich (P06, Thread C086) | **VALIDIERT (eingeschränkt)** | Vom Twin Evora identisch besetzt; mechanistisch angreifbar bei „Crepe Researchers“ |
| **CT4** | Derm-Autorität + Aktivstoff „face-grade for body“ (A4 + A6 + M4) | Validated · Mittel-hoch | bestätigt im Actives-Segment; Derm-Vertrauen gemischt | **VALIDIERT – für FALUNARA derzeit nicht zugänglich** | Abhängigkeit INCI, Studien, echte Expertise |
| **CT6** | Persona-Seiten-Distribution mit Long-form (C1 + C2) | Validated · Mittel-hoch | Seeding-/Werbe-Erkennung in der Zielgruppe (A0054, C0482) | **VALIDIERT als Wettbewerberverhalten – Compliance-Beobachtung** | Nur dokumentiert |
| **CT-E** | Evora-spezifisch: Luxus-Insider-Long-form, „437 Orders“, „Try Evora risk-free for 90 days“, Story-Video-Shell | Candidate (Einzel-Advertiser) | Luxusmotiv widersprochen; Rest stumm | **KANDIDAT** | Nachahmung = Austauschbarkeit mit dem Twin |

**Ranking der Control-Territorien nach Playbook-Robustheit:** CT2 > CT3 (bedingt) > CT5 (Standard) > CT1 (eingeschränkt) > CT4 (unzugänglich) > CT6 (nur Beobachtung).

---

## 13. Challenger territories

*Challenger = Lücke oder Wachstumszeichen; oft stärkere Kunden- als Werbeevidenz. Absenz in der Werbung ist kein Performance-Beleg (Survivorship Bias) [AIS §5].*

**13.1 Upstream-Challenger, neu bewertet**

| # | Territorium | Upstream | VOC-Re-Check | **Playbook-Einschätzung** | Hauptrisiko / Abhängigkeit |
|---|---|---|---|---|---|
| **CH3** | Sensorik/Ritual als Lead (feuchte Haut, zieht ein, Komfort/Juckreiz) | Candidate · Mittel | **stark verstärkt**: P01 132 / 50; P03 192 / 59; Desire #1 120 / 62; Juckreiz P22 76 / 31; Ritual 25 / 23 | **KANDIDAT (stark gestärkt) – Top-Challenger** | „Non-greasy“ ist table stakes; „$49 statt $10“ unbeantwortet; **Sensorik von FALUNARA unbekannt** |
| **CH5** | Ehrliche Erwartungen / Pflege statt Anti-Aging-Kampf | Candidate · Niedrig-mittel | **verstärkt**: Desire #5 16 / 12; P21 81 / 45; Obj. #14 30 / 24; P14 84 / 33 | **KANDIDAT (gestärkt)** | Nur Absenzsignal in der Werbung; Stufe-4-Markt belohnt evtl. laute Claims kurzfristig |
| **CH1** | Post-GLP-1/Gewichtsverlust-Haut | Candidate · Mittel | **verstärkt**: P20 29 / 17 / 5 | **KANDIDAT (gestärkt)** | Claim-Nähe („reverses“, „rebuild“); Evora 0 Ads = offene Flanke; VOC-Untererfassung möglich |
| **CH2** | Transparenter Einmalkauf ohne Abo | Candidate · Mittel („kundenseitig stark“) | **stumm** (0 Abo-Zeilen) | **KANDIDAT (Kundenevidenz enger: nur Trustpilot [WP])** | Angebotsentscheidung offen; Hypothese, nicht belegt |
| **CH6** | Explizite Menopause im Short-form | Candidate · Niedrig-mittel | VOC: Kontext allgegenwärtig (P19), aber „nicht Produktthema“; HRT-Skepsis | **KANDIDAT (unverändert)** | Medizinische Claim-Nähe; nicht alle Kernkundinnen rahmen hormonell |
| **CH7** | Fragilität: dünne Haut, Blutergüsse | Candidate · Niedrig-mittel | verstärkt (Desire #16 28 / 12; „thin“ 25 / 14) | **KANDIDAT (gestärkt), Compliance-kritisch** | Bluterguss/Hautverletzung = medizinische Aussagen |
| **CH4** | Drittanbieter-Vergleiche/Rankings | Candidate · Mittel | Risiko verstärkt (Werbe-Erkennung) | **KANDIDAT (geschwächt) – Compliance-Beobachtung** | Fake-/Eigen-Rankings als Täuschung |
| **CH8** | Spanischsprachige U.S.-Varianten | Candidate · Niedrig | stumm (Corpus englisch) | **KANDIDAT (unverändert)** | Keine Kundenevidenz |

**13.2 Neue Challenger aus der VOC-Synthese (ohne Werbe-Validierung)**

| # | Territorium | VOC-Evidenz | Werbe-Lage | **Status** | Abhängigkeit |
|---|---|---|---|---|---|
| **CH9** | **Beine/Schienbeine („desert shins“, „dragon scales“, Knie)** als eigene Zone | crepey_legs 57 / 35 / 8 (fast gleichauf mit Armen 99 / 39); Thread „What are we doing about desert shins?“ (C029); „The bottom half of my legs look like snake skin“ (A0130) | Arme 219 Anzeigen vs. Beine/Knie 59 [AIS D2]; NØRD „shorts“ | **KANDIDAT** | Zonen-Wirkung unbelegt; nur Trockenheit/Gefühl |
| **CH10** | **Winter / trockene Saison** statt nur Sommer | P23 86 / 48 / 9; Trigger #3 51 / 32 | 1 Goda-Langläufer (150 Tage, gestoppt) [SF OPEN-06]; sonst Sommer-Fokus | **KANDIDAT** | Saisonaler Test; Komfort-Claims belegen |
| **CH11** | **Anwendungs-Klarheit** (Öl vs. Lotion, Reihenfolge, „do I still need lotion?“) | P04 168 / 58 / 10; Contradiction „Öl zuerst oder Lotion zuerst?“ | kaum (Evora Bullets) | **KANDIDAT** | Produkt-Rolle (allein vs. Layering) muss intern festgelegt werden |
| **CH12** | **„Dressable“-Zeit & Bettwäsche** (Wartezeit bis Anziehen, Abfärben) | Trigger #10 45 / 30; #11 15 / 14; Obj. #3 70 / 38 | Evora „absorbs in seconds“ als Bullet | **KANDIDAT** | Messbare Einziehzeit von FALUNARA nötig |
| **CH13** | **Duft-Klarheit** (duftfrei vs. dezent) als Vertrauenssignal; Lücke durch AmLactin-Geruch | P05 181 / 59; AmLactin∩Geruch 28 / 19 / 6 | kaum | **KANDIDAT** | **FALUNARA-Duftprofil unbekannt** |
| **CH14** | **„Der vergessene Körper“** (Gesicht vs. Körper) | P18 29 / 20 / 7 | kein Gegenstück | **KANDIDAT (VOC-only)** | – |
| **CH15** | **Probieren vor Festlegen** (Probiergröße, Duftprobe) | trial_before_commit 7 / 7 [PB-Nachzählung] | Evora: Garantie statt Probe | **HYPOTHESE** | Sortiments-/Offer-Entscheidung |

**Top-Challenger nach Playbook-Robustheit:** CH3 > CH5 > CH9/CH10/CH12 (VOC-stark, werblich leer) > CH1 (gestärkt, Claim-Risiko) > CH2 (Hypothese mit dünner Primär-Evidenz).

---

## 14. Evidence conflicts and unknowns

**14.1 Inhaltliche Konflikte (nicht aufgelöst)**

| # | Konflikt | Position A | Position B | Playbook-Einordnung |
|---|---|---|---|---|
| K1 | **Öl dringt ein vs. Öl versiegelt** | Werbung: 86 Anzeigen / 7 Cluster, Goda 314 Tage („oils penetrate deep where the real problems start“ [SF OPEN-01]); Evora „melt through it“ [SF OPEN-02]; VOC-Minderheit B0581, A0404 | VOC Obj. #5 48 / 31 / 9; Experten Garshick/Queller/AAD [MB]; Dr. Ramachandra „dermis“-Aussage anatomisch ungenau [MB] | Werbe-Konsens ≠ Kundenglaube. **M2 bleibt KANDIDAT (geschwächt), Claim-Risiko hoch.** |
| K2 | **„Cremes versagen“ vs. Lotion-Benchmarks wirken** | A1/B1/CT1 | AmLactin 147 / 44, Gold Bond, CeraVe (Thread C086, B0515) | Problemhälfte valide, Generalisierung nicht |
| K3 | **$49 vs. VOC-Preiserwartung** | Prestige-Band $50–80 existiert (B0636; OSEA „pricey“ aber genutzt A0668); „Pricey, but … pickier“ (A0406) | „Do not spend more than like $20 on a bottle…“ (A0593); „$20-$30“ (B0490); „$70.00 for 16oz. Way too expensive“ (B0039); „$55 … TINY“ (B0097) | Mehrheit preissensibel, Minderheit qualitätsorientiert [VOC3 §9]. $49 braucht einen nachvollziehbaren Grund; [PW] rechtfertigt Premium über Finish (#35). **Zahlungsbereitschaft für FALUNARA unbekannt.** |
| K4 | **Abo-Misstrauen: Stärke der Evidenz** | [MB]/[PW]: hoch (Trustpilot Evora/Crepe Erase, BBB, Aggregatoren; WP) | Reddit-VOC: 0 Zeilen | Evidenz ist plattformgebunden. Plausibel, aber nur sekundär belegt |
| K5 | **Desire-Rangfolge** | [PW]: „Bare my arms again“ #1 | [VOC3]: taktil/Einziehen höchste Thread-Rekurrenz | Warum vs. Wie – beide valide (§4.2) |
| K6 | **Evora-Preise** | [CI]/[MB]: $49 (compare $69), $39/$34 je Flasche im Bundle | [PW #39]: $54 (compare $69), $88/2, $119/3 (Shopify-JSON); Trustpilot „$28 vs. $34“ [WP] | Mehrere Handles/Zeitpunkte [MB Datenqualität]; Preis-Parität FALUNARA = Evora nur „ungefähr“ belegt |
| K7 | **Evora-Bewertungszahlen** | Trustpilot 4.6 / 1,169 | Onsite „4.9/5 (1113)“, „1560“, „50.000+ purchased“ | Inkonsistent; Onsite-Reviews teils 2021 datiert [MB] |
| K8 | **Gold Bond „82 % in two days“** | Primärseite zitiert [MB] | Nur Aggregator-Snippets laut anderer Notiz [MB] | Status unklar |
| K9 | **Zeit bis Ergebnis** | „Immediately. Overnight.“ (A0823); „about a week“ (A0525) | „a little over three months“ (B0851); „third bottle … still waiting“ (A0331) | Gefühl schnell, Optik langsam (Interpretation [VOC3 §9]) |
| K10 | **Menopause: Kaufmotiv oder Kontext?** | [AIS] D5 validiert; Evora 79 Ads (Long-form) | [VOC3] F13: „Kontext – nicht Produktthema“; HRT-Skepsis | Kontext VALIDIERT, Lead KANDIDAT |
| K11 | **Textur leicht vs. reichhaltig** | „Heavy,heavy moisturizers.“ (A0132) | „I hate the feeling of stuff on my body“ (C0086) | Segmentvariable |
| K12 | **Duft** | Duftliebe 75 / 36 | Duftempfindlichkeit 111 / 50 | Segmentvariable; FALUNARA-Duft unbekannt |
| K13 | **Alterskorridor** | Kern 48–58 | Evora-Narratorinnen 56–64, Reviewerinnen 61–69; VOC-Alter breit 19–76 | Werbe-Persona liegt älter als Kern |
| K14 | **Training/HRT als Lösung** | „No lotion will affect leg skin like exercise.“ (A0086) | „My biceps are firm from training at 65 and the crepeyness is still totally present“ (B0026) | Konkurrenzüberzeugung, kein Konsens |
| K15 | **Ad-Synthese-Zählungen** | [AIS] 83 Wasser-Ads | [CI] 86 | Regex-Definitionen; Größenordnung gleich |

**14.2 Unbekannte (kritische Abhängigkeiten)**

| Unbekannt | Warum kritisch | Betroffene Territorien |
|---|---|---|
| **FALUNARA-INCI, Konzentrationen** | Jede Mechanismus- oder Wirk-Aussage; „Crepe Researchers“; Mineralöl-/Duft-Ängste | M1–M6, CT1, CT4, CH13, E7, E13 |
| **Sensorik (Einziehzeit, Finish, Abfärben)** | Gatekeeper-Kriterium P03 | CH3, CH12, BI-1 |
| **Duftprofil / ätherische Öle** | P05-Polarisierung, Reizung | CH13, E9 |
| **Klinische/Verbraucher-Studien** | Optik-/Firming-Aussagen | D2, BI-3, C6 |
| **Reviews / echte Testimonials** | CT3, O7 | CT3, H2, S1 |
| **Garantie- und Abo-Entscheidung** | CT5, O5, CH2 | §11 |
| **Größen/Varianten (100 vs. 200 ml)** | Menge-pro-$ (B0097) | O3, K3 |
| **Glasflasche in der Dusche (Sicherheit/Handling)** | Obj. #10; keine VOC-Evidenz zu Glas | E11 |
| **Name/Domain „Falunara“ vs. „Falurana“** | Vertrauen, Auffindbarkeit, Fälschungsangst | §11.3 |
| **Spend/Performance jeder Wettbewerber-Anzeige** | Alle „Control“-Aussagen sind Verhaltens-Proxys | §9–13 |
| **Retail-Reviews (Amazon/Ulta/Target)** | Stimmen 48–58 zu $30–80-Ölen fehlen | K3, CH3 |
| **TikTok, Facebook-Gruppen, YouTube-Kommentare** | Plattform-Bias Reddit | gesamt |
| **Suchvolumen „crepey“ vs. Trockenheitsbegriffe** | Segmentgröße „Overnight Dry-Out“ | §2 |
| **Diversität** (Schwarze, Latina-, asiatisch-amerikanische Frauen) | Keine Evidenz außer Einzelstimme [PW] | CH8 |

**14.3 Compliance-sensible Territorien (Forschungsbeobachtungen, keine Rechtsauskunft)**

| Beobachtung | Wo | Warum sensibel |
|---|---|---|
| Firming-/„restores firmness“-/„reverse“-Aussagen ohne Substantiierung | Evora Link-Description „visibly restores firmness … See real results in 3–4 weeks“ (48 Ads) [CI §4]; NØRD „Rebuilds Collagen In 4 Weeks“; VitaeCharm GLP-1-„rebuild“ [SF OPEN-07] | Wirkaussagen brauchen Belege; Struktur-/Kollagen-Aussagen nähern sich Arzneimittel-Claims |
| Tiefenwirkungs-Mechanismus („melts through the barrier“, „Penetrates 5 layers deep“) | M2 [AIS] | Kein Experten-/Quellenbeleg [MB] |
| „Natural Botox in a bottle?“ | Evora-Visual [CI §4] | Vergleich mit Arzneimittel/Prozedur |
| Unbenanntes „Dermatologist Approved“, Persona-„Ärzte“ („Dr. Emily Carter“, „Dr Lila Merrit“, „Harvard dermatologist“) | [AIS A4], [CI §1.1] | Nicht verifizierbare Expertise |
| Drittanbieter-artige Rankings mit Eigenplatzierung (skinglowmagazine „Top 5“, Evora A+) | [CI §4], [AIS A10] | Verdeckte Eigenwerbung / irreführende Vergleiche |
| Persona-Seiten und link-lose Seeding-Fragen („Joanna Woodley“, 308 Tage) | [AIS C1, H8] | Authentizität, verdeckte Werbung |
| Vergütete Testimonials (Evora-Footer) | [MB] | Offenlegungspflichten für Endorsements |
| Echtzeit-Knappheit („437 Orders in Last Hour“, „89% sold“) | [SF HEAD-03], Evora PDP | Unverifizierbare Dringlichkeit |
| Vorausgewähltes Abo / Auto-Ship | Evora, Goda, VitaeCharm PDP [AIS O5] | Negative-Option-/Auto-Renewal-Regeln; Beschwerden [MB, WP] |
| Medizinische Kontexte (Juckreiz/Ekzem, Blutergüsse, Menopause/HRT, GLP-1) | CH6, CH7, CH1; VOC-Flag hrt_medical_context 140 Zeilen | Krankheits-/Heilaussagen vermeiden |

---

## 15. Research-backed creative hypotheses for future testing

*Nur Hypothesen. Keine Ad-Copy, keine Headlines. Jede Hypothese ist ungetestet (Status HYPOTHESE).*

| # | Hypothese | Begründung | Evidenz-Refs | Was würde sie falsifizieren | Offene Abhängigkeit |
|---|---|---|---|---|---|
| HY-01 | Ein **sensorik-geführter Einstieg** (Einziehen, „anziehbar“, kein Abfärben) erzeugt bei 48–58 mehr qualifizierte Aufmerksamkeit als ein Firming-geführter Einstieg. | Gatekeeper-Kriterium und stärkstes VOC-Desire; Firming ist gesättigt und misstraut | P03 192/59; Desire #1–2; [PW] Kaufkriterium #1; [MB] Stufe 4–5; [AIS] CH3 | Kein Unterschied oder Nachteil in Hold-/Klick-/Conversion-Metriken; Kommentare thematisieren weiter „greasy“ | **Sensorik-Messung** (Einziehzeit, Transfer-Test) für FALUNARA |
| HY-02 | **Anwendungs-Aufklärung** (feuchte Haut, Rolle neben Lotion) senkt den Fett-Einwand stärker als „non-greasy“-Behauptungen. | „meteor of knowledge“; P04-Verwirrung; Anwendung ist Allgemeingut, Reihenfolge nicht | P01 132/50; P04 168/58; C0503, C0608; [PW] #27 | Einwand-Anteil in Kommentaren/Umfragen unverändert; Retouren wegen „greasy“ gleich | Interne Festlegung: Öl allein oder Layering; Sensorik |
| HY-03 | **Beine/Schienbeine** als Zone ist weniger gesättigt als Arme und erreicht ein ebenso betroffenes Publikum. | VOC fast gleichauf, Werbung stark arm-lastig | crepey_legs 57/35 vs. arms 99/39; [AIS] D2 (219 vs. 59 Anzeigen); C029 | Niedrigere Resonanz bei Bein-Fokus über ≥2 Tests | Nur Trockenheits-/Gefühlsaussagen ohne Studie |
| HY-04 | **Winter-/Trockensaison-Rahmung** öffnet ein zweites Saisonfenster neben dem Sommer. | P23 breit; Goda-Winter-Langläufer 150 Tage | P23 86/48; Trigger #3; [SF] OPEN-06 | Kein saisonaler Unterschied oder schwächer als Sommer-Rahmung im Winter | Komfort-Claims belegen; Testzeitpunkt |
| HY-05 | **Ehrliche Zeitachse** (Gefühl sofort, sichtbare Veränderung nur mit Geduld) erhöht Vertrauen bei „Tried-Everything Skeptics“ gegenüber Zeitversprechen. | Fatalismus, „bandaids“, moderate Ziele | P21 81/45; Obj. #14; Desire #5; [MB] „I don't expect miracles“; [AIS] CH5 | Geringere Kaufabsicht vs. Zeitversprechen bei gleicher Zielgruppe | Keine Optik-Aussage ohne Studie |
| HY-06 | **Transparente Inhaltsstoff-/Formelangaben** sind für „Crepe Researchers“ Eintrittsbedingung, nicht Differenzierung. | Transparenzforderung, Buzzword-Misstrauen | P12 101/50; Obj. #7; A0185, A0272, C0463; [MB] Lücke INCI | Kein Unterschied in Conversion/Fragen-Volumen mit vs. ohne INCI-Sichtbarkeit | **INCI-Freigabe** |
| HY-07 | **Kaufbedingungen ohne Abo-Druck** wirken als Vertrauenssignal – bezogen auf Käuferinnen mit Evora/Crepe-Erase-Erfahrung. | Trustpilot-Beschwerden, NØRD „No subscription“ | [MB] Einwand 5; [PW] #36, #38; [AIS] CH2; **VOC stumm** | Kein messbarer Effekt; Reddit-artige Zielgruppe reagiert indifferent | **Abo-/Offer-Entscheidung** |
| HY-08 | Eine **längere Garantie** (gegenüber 30 Tagen) senkt die Kaufbarriere bei $49. | Kategorie-Standard 60–90 Tage; Probier-Wunsch | [AIS] O1/CT5; [MB] Garantie-Vergleich; C0410, A0666 | Kein Unterschied in Conversion; VOC liefert bislang keine Garantie-Evidenz | **Garantie-Entscheidung** |
| HY-09 | **Peer-Beweis nach VOC-Muster** (Alter + Zone + Dauer + moderates Ergebnis + Einschränkung) ist glaubwürdiger als Superlative. | So formuliert die Zielgruppe Erfolge selbst | [PW] Vertrauen; S1/CT3; B0851; H4 (B0092) | Superlativ-Testimonials performen gleich oder besser bei gleicher Glaubwürdigkeitsbewertung | **Echte Reviews mit Einwilligung** (keine Fabrikation) |
| HY-10 | **Duft-Klarheit** (Profil oder Duftfreiheit klar benannt) senkt Abbruch-/Retourenrisiko. | Polarisierung; AmLactin-Geruch als Benchmark-Schwäche | P05 181/59; Obj. #1–2; C0577 | Keine Veränderung in Duft-bezogenen Einwänden | **Duftprofil von FALUNARA** |
| HY-11 | **„Der vergessene Körper“**-Einstieg erreicht Problem-aware-Frauen, die sich nicht mit „crepey“ identifizieren. | Vernachlässigungs-Narrativ; Segment „Overnight Dry-Out“ spricht nicht „crepey“ | P18 29/20; F1; [MB] Segment | Niedrige Resonanz im Vergleich zu „crepey“-Vokabular | – |
| HY-12 | **Post-GLP-1-Trockenheit/-Textur** (ohne Rebuild-/Reverse-Aussagen) ist eine offene Flanke gegenüber Evora. | Evora 0 Ads; VOC-Rekurrenz gestiegen | P20 29/17; [AIS] CH1; B0514 | Geringe Resonanz oder primär „loose skin“-Erwartungen, die ein Öl nicht erfüllen kann | **Rechtliche Prüfung**; keine Struktur-Claims |
| HY-13 | **Visuelle Abgrenzung vom Evora-Look** (Klarglas, goldenes Öl, weiße Pumpe) ist nötig, um Verwechslung im Feed zu vermeiden. | Identisches Format, gleicher Preis | [CI] §1.1, §6.8; [AIS] CT-E | Brand-Recall-/Verwechslungstests zeigen keine Verwechslung | **Packaging-/Brand-Entscheidung** |
| HY-14 | **In-Shower-Handhabung** (Pumpe mit nassen/öligen Händen, rutschiger Boden) ist ein unterschätzter Einwand, den Demo-Formate adressieren können. | Obj. #10 | C0042, C0488, A0597, C0179 | Einwand taucht in Tests/Kommentaren nicht auf | **Sicherheitsbewertung Glasflasche in der Dusche** |
| HY-15 | **„Pflege ohne Kampf“-Ton** reduziert Reaktanz bei Akzeptanz-orientierten Frauen, ohne Veränderungs-Orientierte zu verlieren. | Ambivalenz Akzeptanz/Veränderung | P14 84/33; C0199; [PW] Mass Desire #5; E16 | Ton-Test zeigt Verlust bei Veränderungs-Orientierten ohne Gewinn bei Akzeptierenden | – |
| HY-16 | **Mutter-/Spiegel-Moment** als emotionaler Einstieg ist stärker als „old lady“-Labels, weil er Identifikation statt Beschämung auslöst. | Mutter-Vergleich wiederkehrend; Ablehnung von Unsicherheits-Marketing | Trigger #5 27/19; A0850, B0227; C0640 | „old lady“-Rahmung zeigt höhere Resonanz ohne negative Kommentare | – |

---

## 16. Source / evidence appendix

**16.1 Upstream-Dateien und genutzte Abschnitte**

| Datei | Genutzte Abschnitte |
|---|---|
| `reports/FALUNARA Marktbewusstsein USA.md` | Executive Summary; Problem-language map; Known-solution map; Existing-belief/mechanism map; Objection map (#1–7); Sophistication; Awareness segmentation; Messaging implications; Contradictions; Source ledger |
| `reports/FALUNARA Psychografie und Wünsche USA.md` | BLUF; Desire inventory D1–D16; Desire map; Pain map; Tried-and-failed; Purchase criteria; Trigger map; Belief/objection map; Candidate mass desires; Evidence table #1–#53; Contradictions/Unknowns |
| `ad_intelligence/Competitor_Intelligence_Research.md` | §1 Landscape (inkl. Evora-Ökosystem); §2 Top-25; §3 Konzepte; §4 Muster, Visuals, Landingpages; §5–6 Territorien; §7 Limits |
| `ad_intelligence/Advertising_Intelligence_Synthesis.md` / `synthesis_table.csv` | §1 Methodik (V1–V4); §2 Items D1–CH8; §3–5; §7 Evidenzlücken |
| `ad_intelligence/Swipe_File.md` | HOOK-01–25, HEAD-01–22, OPEN-01–12 |
| `ad_intelligence/swipe_ledger.csv`, `access_test.md` | Felddefinitionen, Zugriffstests |
| `voc/VOC1_Community_Map.md` | Methode, Tiers, nicht nutzbare Communities, Off-Reddit-Zugriff |
| `voc/VOC2_URL_Corpus.md` | Rubrik, Corpus C001–C090, Ausschlüsse, Limits |
| `voc/VOC3_Deep_Reddit_VOC_Research.md` | §1 Methodik; F1–F13; Phrase Bank; Objection Bank #1–15; Desire Bank #1–16; Failed-Solution Bank #1–15; Trigger Bank #1–15; P01–P25; Contradictions; Limitations |
| `VOC_Master.xlsx` | Tabs 02_Raw_VOC (Nachzählungen), 03–09 |

**16.2 [PB-Nachzählungen] in `02_Raw_VOC` (Seeding ausgeschlossen, Regex auf Zitatfeld)**

| Abfrage | Ergebnis |
|---|---|
| `subscri|auto-ship|autoship|auto-renew|cancel` | 1 Zeile / 1 Thread (B0213, HRT-„subscription“ = Rezept; kein Abo-Bezug). Zusätzlich Grep über `voc/thread_cache/`: keine Abo-Beschwerde |
| `guarantee|refund|money back|return it` | 0 Zeilen |
| `\$ ?\d` (Preisnennungen) | 23 Zeilen / 19 Threads (u. a. A0019, A0197, A0354, A0593, A0603, B0039, B0097, B0163, B0255, B0490, B0541, B0636) |
| `evora|crepe erase` | 5 Zeilen / 5 Threads; Evora 0 |
| `penetrat|deeper|deep into` | 6 Zeilen / 5 Threads (A0282, A0283, A0385, B0156, B0494, B0581) |
| `mostly water|water-based|evaporat` | 2 Zeilen (C0122, C0417) |
| `glass|pump` | 13 Zeilen / 13 Threads (Pumpe bevorzugt A0597; Glas nur DIY A0516, C0177) |
| `husband|partner|boyfriend` | 6 Zeilen / 6 Threads |
| `wedding|bride|vacation|beach|cruise|event` | keine thematisch relevanten Anlass-Zeilen |
| `sample|travel size|blind buy|smell it before` | 6 Zeilen / 6 Threads |
| `winter` | 32 Zeilen / 21 Threads |
| Tags: price_value 167/65; marketing_distrust 92/48; fragrance_sensitivity 111/50; scent_love 75/36; routine_fatigue 97/46; self_care_ritual 25/23; trial_before_commit 7/7; oil_shower_packaging_friction 11/8; body_neglect_vs_face 17/12 | (Zeilen/Threads) |

**16.3 Zentrale Ad-Library-IDs** (https://www.facebook.com/ads/library/?id=…)

| ID | Advertiser/Seite | Bezug |
|---|---|---|
| 4109833019265205 | Goda / Over 40 & Fabulous (314 Tage) | H2, S1, CT1, CT3, M2 |
| 1637558804018844 / 1611807499919232 / 1811884486444866 | NØRD BODY / Body Confidence Daily | H1, CT2, O1 |
| 1570129684499222 | Evora Body | A1, M1, M2, H3 |
| 1361129475914444 | Evora Body („Try Evora risk-free for 90 days“) | O1, O2, CT-E |
| 854380807531360 / 2515907112242718 | Evora Body / Daily Discounts („437 Orders…“) | O4, CT-E |
| 1076748835007888 / 1954753225212676 | Evora / Ageless Glow Today (Video-Shell) | C4 |
| 1021976634228403 / 2329433507867811 / 1467338712082607 | Evora / Natalie Brooks, Hannah Lewis | A8, H6, S3 |
| 980035185081066 | DRMTLGY (185 Tage) | A4, A6, CT4 |
| 1564770261945264 / 2116539015744078 / 4092537667704644 | Miami MD / Feline | A2, A4, H5, S1 |
| 2202226780628780 / 1048726737582951 / 880796694467063 | VitaeCharm | A5, D7/CH1, CH7 |
| 1183652923933432 | Goda (Winter, 150 Tage) | CH10 |
| 965929252430847 / 1070866808556946 | Goda (Myth-busting, Identity) | A2, D4 |
| 1994209947876803 | Remedy Skin / Dr. Muneeb Shah | C6 |
| 971890085912295 / 1592473439201348 | „Dr. Emily Carter“ / HealthyClub (Rankings) | A10, CH4 |
| 1908949839699218 / 25994710613513758 | Seeding „Joanna Woodley“ | H8 |
| 2455348678278754 | NØRD (Menopause, „No subscription“-Bezug) | CH2, CH6 |

**16.4 Zentrale VOC-Threads** (Corpus-ID → URL; vollständige Liste [VOC2 §3])

C001 https://www.reddit.com/r/40PlusSkinCare/comments/1q7st6w/share_your_best_skin_care_routine_for_body_not/ · C002 https://www.reddit.com/r/40PlusSkinCare/comments/1tcgl5d/how_are_you_keeping_crepey_legs_at_bay/ · C003 https://www.reddit.com/r/40PlusSkinCare/comments/1txwn4j/wtf_is_going_on_with_my_skin_im_freaking_out_and/ · C023 https://www.reddit.com/r/45PlusSkincare/comments/190412g/best_body_oil/ · C024 https://www.reddit.com/r/45PlusSkincare/comments/1dldr06/severe_crepey_arm_skin/ · C025 https://www.reddit.com/r/45PlusSkincare/comments/1en6t65/very_dry_skinwhole_body_moisturizer_help_needed/ · C029 https://www.reddit.com/r/45PlusSkincare/comments/1tk4zmu/what_are_we_doing_about_desert_shins/ · C031 https://www.reddit.com/r/45PlusSkincare/comments/1vr68n7/best_products_for_crepey_arms_and_neck_creams/ (Seeding-Flag niedrig) · C032 https://www.reddit.com/r/45PlusSkincare/comments/1bsuuc2/iso_suggestions_for_a_body_moisturizer_or_dry_oil/ · C052 https://www.reddit.com/r/30PlusSkinCare/comments/1oz5er4/does_anyone_use_body_oil_instead_of_lotion_what/ · C057 https://www.reddit.com/r/Menopause/comments/1fd0h17/my_hands_and_arms_have_suddenly_become_crepey/ · C058 https://www.reddit.com/r/Menopause/comments/1hvpiqd/what_happened_to_my_arms/ · C059 https://www.reddit.com/r/Menopause/comments/1lwrmvw/crepe_skin/ · C064 https://www.reddit.com/r/Menopause/comments/1d2qhua/lizard_skin/ · C071 https://www.reddit.com/r/Menopause/comments/1n0taq6/dry_skin/ · C080 https://www.reddit.com/r/SkincareAddiction/comments/1pg9y2o/psa_dont_buy_the_more_expensive_amlactin_the_kp/ · C081 https://www.reddit.com/r/beauty/comments/1dhgg35/people_why_did_no_one_tell_me_about_postshower/ · C083 https://www.reddit.com/r/beauty/comments/1qfgegt/help_turning_50_overwhelmed_by_body_washoil/ · C088 https://www.reddit.com/r/TwoXChromosomes/comments/m540tj/so_tired_of_womens_insecurities_being_sold_to_us/

**16.5 Überlappung der Kundenevidenz (Unabhängigkeits-Hinweis).** [MB], [PW] und [VOC3] teilen mehrere Threads (u. a. 1lwrmvw, 1fd0h17, 1hvpiqd, 1kkbxtg, 10h8dgw, otvj5z, 14cn06o, 1oz5er4, 1n721qj, m540tj). „Bestätigt durch VOC“ heißt in diesen Fällen teils *dieselbe Quelle, systematischer gezählt*, nicht *unabhängige Zweitquelle*. Die stärkste Zusatz-Unabhängigkeit liefert VOC über r/40PlusSkinCare und r/45PlusSkincare (39 von 90 Threads), die in [MB]/[PW] nicht ausgewertet wurden.

**16.6 Weitere Quellen-URLs (aus Upstream, nicht neu abgerufen):** falurana.com · falurana.com/products.json · evorabody.com/products/botanical-body-oil · trustpilot.com/review/evorabody.com · trustpilot.com/review/www.crepeerase.com · goldbond.com/en-us/products/crepe-corrector-age-defense · thebodyfirm.com · necessaire.com/products/the-body-retinol · ulta.com/p/undaria-algae-body-oil-pimprod2017702 · aad.org (Menopause; Dry skin) · health.clevelandclinic.org/whats-causing-your-crepey-skin-and-how-can-you-fix-it · today.com/shop/best-body-oils-t231712 · yougov.com/en-us/articles/49300-… · aarp.org/entertainment/beauty-style/women-beauty-aging-survey/ (vollständige Liste: [MB Source ledger], [PW], [CI]).

*Ende des Playbooks. Keine Inhalte dieses Dokuments sind Werbetexte oder Wirkaussagen für FALUNARA.*
