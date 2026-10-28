---
name: winner-ad-analyse
description: Zerlegt Winner- und Verlierer-Ads (Video, Bild, Long-Copy) nach Zakarias Ad Learning Lab. Bei: Ad zerlegen, Breakdown, Winner-Analyse, Autopsie, Ad ohne Spend, warum floppt die Ad.
---

# Winner- und Verlierer-Ads zerlegen (Ad Learning Lab)

Dieser Skill zerlegt Ads systematisch, damit aus jeder Ad, ob Gewinner oder Verlierer, eine überprüfbare Hypothese für die nächste Ad wird. Er deckt vier Fälle ab: Winner-Ads (eigene und fremde), Verlierer mit Spend, Verlierer ohne Spend und Long-Copy-Native-Ads.

**Herkunft:** Zakaria Airakaz, ECOM Masterclass 2026, Modul „4. Creatives Mastery behind 100M$ Brand“, Teile „4. Ad Learning Lab“ (Lektionen 13 bis 20) und „6. Ad Learning Lab Losing Ad“ (Lektionen 1 bis 5). Ergänzt um einzelne Discord-Antworten von Zakaria. Die Regeln sind **noch nicht in einer eigenen Produktion bestätigt**. Nach jeder Analyse Abschnitt 13 ergänzen.

**Wann welche Datei lesen:**
| Datei | Lesen, wenn … |
|---|---|
| `references/winner-workbook.md` | du einen Winner zerlegst. Komplettes Arbeitsblatt (4 Ebenen, Teile 1 bis 13). |
| `references/autopsie-video.md` | eine Video-Ad Spend bekam und verloren hat. Schritte 1 bis 7 mit allen Prüffragen. |
| `references/autopsie-no-spend.md` | Meta der Ad 7 bis 14 Tage kaum Budget gab. |
| `references/long-copy-native.md` | du eine Long-Copy-Native-Ad (Bild plus langer Primärtext) zerlegst, Winner oder Verlierer. |
| `references/prompts.md` | du Gemini oder Claude für Analyse und Vergleich einsetzt. |
| `references/beispiele.md` | du ein durchgearbeitetes Beispiel brauchst (Pet Lab Co, First Day, Feuerlöschdecke) oder die Übertragung auf das eigene Produkt üben willst. |

---

## 0. Grundhaltung (die wichtigsten Regeln zuerst)

1. **Die meisten Learnings stecken in den Verlierern.** 80 bis 90 % aller Ads scheitern, bei Anfängern fast alle. Wer nur Winner zerlegt, lernt aus 1 von 100 Ads. Zakarias Werte für die Trefferquote: Anfänger ca. 1 %, gut 20 bis 25 %, über 50 % außergewöhnlich.
2. **Jede Ad startet mit einer schriftlichen Hypothese.** Vor dem Launch ins Ad-Lab-Sheet schreiben: „Warum glauben wir, dass diese Ad funktioniert?“ Bei der Analyse genau diese Annahme prüfen. Nie im Nachhinein erfinden.
3. **Intent vor Ausführung.** Die Kette ist Recherche-Intent → Ad-Idee → Umsetzung → Winner oder Verlierer. Erst klären, ob die Idee falsch war (nicht aus der Recherche, nur ein Kommentar, falsches Timing) oder nur die Umsetzung.
4. **Erst manuell, dann KI, dann vergleichen.** Das Lernen passiert beim langsamen, eigenen Zerlegen. KI deckt blinde Flecken auf, ersetzt das eigene Denken aber nicht.
5. **Nicht beschreiben, sondern hinterfragen.** Zu jeder Beobachtung das **Warum** aufschreiben („Warum diese Sprecherin? Warum Logik vor Social Proof?“). Ein Haken ohne Begründung ist keine Analyse. Das war Zakarias größter Punktabzug im KI-Vergleich.
6. **Daten zeigen, wo es bricht. Ansehen zeigt, warum.** Immer beides. Gute Zahlen können lügen (Clickbait-Hook mit hoher Hook Rate, unterhaltsamer Body ohne Kaufimpuls).
7. **Als Avatar ansehen, nicht als Macher.** Beim Schreiben ist man hochkonzentriert. Der Avatar scrollt um 23 Uhr halb müde. Was dir klar vorkommt, ist für ihn oft zu komplex.
8. **Eine Hauptursache benennen.** Am Ende genau einen „Fatal Flaw“ festlegen und **von oben nach unten** reparieren: Was früh in der Ad bricht, macht alles Spätere unmessbar.
9. **Pro neue Version nur eine große Variable ändern**, sonst weißt du nicht, was gewirkt hat.
10. **Keine Oberflächentaktiken kopieren.** Fremde Ads nur dann als Vorlage nehmen, wenn Bewusstseinsstufe und Marktsättigung (Sophistication) ähnlich wie bei deinem Avatar sind. Ein kopierter Hook ohne verstandenes Warum ergibt Verlierer.
11. **Nicht perfekt sein müssen.** Fehler bei der Analyse sind normal. Ziel ist ein wachsender Datensatz im Kopf und im Notizbuch.
12. **Lernzeit fest einplanen.** Feste Zeit pro Woche (z. B. einmal wöchentlich oder alle 3 bis 4 Tage), alles in einer Sitzung, ohne Handy. Vorher 10 Minuten Ruhe oder Meditation. Mit allen, die an Ads mitarbeiten (Creative Strategist, Texter, Editor), gemeinsam.

---

## 1. Voraussetzungen und Tools

- **Meta Ads Manager** mit Zugriff auf Spend, CPA, Hook Rate, Hold Rate, Ø Wiedergabezeit, CTR (Link), CPC, CPM, Conversion Rate und die **Video-Performance-Karte** (Retention-Kurve, erste 60 s). Wenn der AdKit-Connector verbunden ist, kann er die Zahlen liefern.
- **Ad-Lab-Sheet** mit Hypothese, Angle, Avatar-Segment und Format pro Ad.
- **Avatar-Recherche** (Zitate aus Reddit, Foren, Bewertungen, Umfragen, Kundengespräche). Ohne sie ist kein Sprach- oder Schmerzpunkt-Abgleich möglich.
- **Winner fremder Marken finden:** Meta-Werbebibliothek (lange Laufzeit), ein Ad-Spy-Tool mit Likes, Kommentaren und Shares, Trendtrack (Filter: Land, Nische, Ad-Länge, Seitenreichweite, Shop-Traffic). Trendtrack ist hier als Connector verbunden.
- **Gemini** (AI Studio), weil es Video mit Ton und Bild analysiert. Claude für Text-Ads, Vergleiche und Iterationen.
- **Microsoft Clarity oder Hotjar** für Landingpage-Probleme.
- Eine **Breakdown-Vorlage** pro Ad-Typ (die Reference-Dateien), dazu ein **Lern-Notizbuch** für eigene blinde Flecken.

---

## 2. Welcher Weg?

```
Ist es eine eigene Ad mit Daten?
├─ nein → fremde Ad → Weg A (Winner-Workbook), Zahlen nur als Indiz
└─ ja → Hat sie in 7 Tagen nennenswert Spend bekommen?
        ├─ nein (7–14 Tage CBO, kaum $) → Weg C (No-Spend-Diagnose)
        └─ ja → CPA am oder unter Ziel?
                ├─ ja → Weg A (Winner-Workbook) + Learning Extraction
                └─ nein → Weg B (Autopsie Video) bzw. Weg D (Long-Copy-Native)
```
- **Long-Copy-Native-Ads** (auffälliges Bild plus 300 bis 700 Zeilen Primärtext) laufen immer über Weg D, egal ob Winner oder Verlierer.
- **Statische Bild-Ads:** Laut Kurs kommt dafür eine eigene Vorlage. Bis dahin die 4 Ebenen aus Weg A nutzen und Bild plus Headline als Hook bewerten.

---

## 3. Ablauf im Überblick

```
Ad auswählen → Weg bestimmen → Metriken ziehen und einordnen → Hypothese aus dem Ad-Lab holen
  → 5× ansehen (Gesamteindruck / stumm / nur Ton / Emotion / mit Vorlage)
  → Vorlage ausfüllen, jede Antwort mit Warum → Hauptursache bzw. Erfolgsfaktor
  → KI-Analyse (Gemini) → KI-Vergleich (Bewertung, Lücken) → eigene Gegenargumente klären
  → Learnings: Must-have vs. Nice-to-have, 2 bis 3 Hypothesen, Aktionsplan
  → Lern-Notizbuch und Ad-Lab aktualisieren → nächste Version testen
```

---

## 4. Winner finden und einstufen

### Fremde Winner finden
- **Meta-Werbebibliothek:** Lange Laufzeit ist das erste Indiz (Beispiel aus dem Kurs: 627 Tage, also fast zwei Jahre). Viele Iterationen desselben Scripts mit nur anderem visuellem Hook sind ein starkes Winner-Signal.
- **Ad-Spy-Tool:** Likes, Kommentare und Shares im Verhältnis prüfen. Beispiel aus dem Kurs: ca. 1.700 Likes, 300 Kommentare, 3.000 Shares hieß „ordentlich, nicht der beste“. Engagement beweist Aufmerksamkeit, nicht Conversion: „mit Vorsicht genießen“.
- **Trendtrack:** Filter nach Land, Nische und Ad-Länge. Marken mit hohem Shop-Traffic und hoher Facebook-Seitenreichweite (über 1 Mio.) bevorzugen, dann den Seitennamen im Ad-Spy suchen und nach Likes sortieren.
- **Ähnlicher Markt:** Gleiche Nische oder andere Nische mit gleicher Bewusstseinsstufe und Marktsättigung.
- Zakaria im Discord: Konkurrenz-Winner nachbauen ist am Anfang okay. Wer nur kopiert, bekommt aber nur „die Reste“ und muss darüber hinaus.

### Eigene Ads einstufen
| Stufe | Kriterien (laut Kurs) |
|---|---|
| **Super-Winner** | CPA am oder unter Ziel, läuft länger als 14 Tage, Top-Spender mit ca. 15 % oder mehr des Spends. Meta ist sehr sicher. DNA auf neue Konzepte übertragen. |
| **Winner** | CPA am oder unter Ziel, läuft 7 oder mehr Tage, bekommt ca. 20 % des Tagesbudgets. Solide. Verstehen, wie er noch weiter skaliert. |
| **Verlierer mit Spend** | CPA über Ziel nach 7 Tagen, oder hoher Spend bei klar schlechten Werten (dann früher stoppen). |
| **No-Spend** | 7 bis 14 Tage in der CBO und kaum oder kein Spend (unter 10 % des Gesamtspends). |
| **Konkurrenz-Ad** | Keine echten Zahlen. Architektur und Technik übernehmen, Ergebnis als Indiz. |

### Richtwerte für Metriken (aus dem Kurs, im eigenen Konto kalibrieren)
| Metrik | Schwach | Okay | Gut |
|---|---|---|---|
| Hook Rate (3-s-Views ÷ Impressionen) | unter 20 % → Hook ersetzen | 30 bis 45 % | ab 50 % (Discord: 30 % = Durchschnitt, 60 % = stark) |
| Hold Rate (ThruPlays ÷ 3-s-Views) | unter 25 % | | ab 25 % |
| CTR (Link) | unter 1 % | 1 bis 2 % | ab 2 % |
| Conversion Rate der Seite | unter 2 % | 2 bis 4 % | ab 4 % |
| CPM | über dem Kontodurchschnitt → Zielgruppe zu eng oder falsch | | |
| CPA | über Ziel | am Ziel | unter Ziel |

Zakaria im Discord: **„Keine Metrik allein zählt.“** Ein Advertorial mit Preis hat niedrigere CTR, aber höhere Conversion auf der Angebotsseite. Ein Clickbait-Hook hat hohe CTR, aber schlechte Folgeschritte. Immer den ganzen Funnel lesen. Trends immer im 7-Tage-Fenster bewerten, nie Tag gegen Tag.

---

## 5. Weg A: Winner zerlegen

**Vollständiges Arbeitsblatt:** `references/winner-workbook.md`. Hier der Kern.

### Fünfmal ansehen
1. **Gesamteindruck**, ohne zu analysieren. Was fällt auf?
2. **Stumm.** Passen Bild und Botschaft zusammen? Versteht man die Idee und spürt man die Emotion ohne Ton? (Bis zu 85 % sehen zunächst ohne Ton.)
3. **Nur Ton**, Augen zu, Kopfhörer. Stimme, Tempo, Pausen, Musik, Musikwechsel, Soundeffekte.
4. **Emotion.** Was fühlt der Avatar in welcher Sekunde?
5. **Mit der Vorlage**, Bild für Bild, und ausfüllen.

### Die vier Ebenen plus Learnings
| Ebene | Frage | Inhalt |
|---|---|---|
| **1. Fundament (Wer und Warum)** | Spricht die Ad mit der richtigen Person die richtige Botschaft? | Demografie, Psychografie, Bewusstseinsstufe (unaware bis most aware), Marktsättigung (Stufe 1 bis 5), Identität (aktuell, gefürchtet, gewünscht, Wert der Lücke), Wettbewerbsposition, Kern-Erfolgsfaktor |
| **2. Struktur (Ablauf)** | Stimmt die Reihenfolge? | Hook → Problem und Verstärkung → Lösungseinführung (Aha) → Beweisfolge → Transformation → Angebot und CTA |
| **3. Psychologie (warum es wirkt)** | Welche Emotion treibt zum Kauf? | Trigger und Intensität (1 bis 10), emotionale Reise, Glaubenswechsel (alt → neu, wie), Einwände, Dringlichkeit |
| **4. Umsetzung (Delivery)** | Trägt die Ausführung die Botschaft? | Bild, Farben, Einstellungen, Schnitttempo, Text-Overlays, Stimme, Autorität, Musik, Soundeffekte, Sprache, Spezifität |
| **5. Learning Extraction** | Was nehme ich mit? | Muster, Must-have vs. Nice-to-have, Übertragung aufs eigene Produkt, 2 bis 3 Hypothesen, 3 Sofortmaßnahmen, Briefing-Elemente |

### Der Hook hat drei Aufgaben
- **Sekunde 1: Aufmerksamkeit holen** (Pattern Interrupt, z. B. ein 3D-Medizin-Modell eines Hundeohrs mit Wattestäbchen).
- **Sekunde 2: Qualifizieren.** Ist das für mich? (Text „3 Anzeichen von Hefe in den Ohren deines Hundes“ plus Bild.)
- **Sekunde 3 bis 5: Bindung schaffen** durch eine offene Schleife oder Spiegelung („Das macht mein Hund auch“, kurze Liste = wenig Zeitaufwand).
- Hook-Typ einordnen (Frage, Schock, Story, Demonstration, Social Proof, Autorität, Problem, Curiosity Gap, Pattern Interrupt, Kontroverse) und mit 1 bis 10 plus Begründung bewerten.

### Fragen, die in jedem Breakdown stehen
- Kommt die Idee aus Recherche-Daten? Passt das Timing (Saison)?
- Welcher **Bösewicht** wird aufgebaut, und **nimmt er dem Avatar die Schuld ab**? („Es ist nicht deine Schuld, es ist der versteckte Hunger.“)
- Wie entsteht der **Aha-Moment**? (Reframe der Ursache: „Die Antwort liegt nicht im Ohr, sondern im Darm.“)
- In welcher **Reihenfolge** kommen die Beweise, und **warum** diese Reihenfolge? (Beispiel: erst Logik für die neue Ursache, dann breiter Social Proof, dann Demo des Mechanismus, dann emotionale Testimonials.)
- Wird die **Autorität** gezeigt statt behauptet? (Setting, Medizin-Visuals, Tonfall, ohne „Ich bin Ärztin“.)
- Welche **Einwände** werden beiläufig beantwortet? (Mag mein Kind das? Ist es sicher? Wie lange dauert es?)
- Was **fehlt**? Die Kommentare der Ad lesen: Fragen wie „Wie lange dauert es, bis es wirkt?“ zeigen Lücken. Das ist eine Idee für die eigene Version.

### Learnings sauber trennen
- **Must-have = tragende Wände.** Ohne sie funktioniert die Ad nicht (z. B. Hook, Reframe der Ursache, UGC-Testimonials im Split Screen).
- **Nice-to-have = Deko.** Macht es angenehmer, trägt aber nicht (z. B. Hintergrundmusik).
- **Hypothesen im Format:** „Wenn wir **X** testen, steigt **Y**, weil **Z** (Avatar-Psychologie).“ Höchstens 2 bis 3, die besten, nicht alle möglichen.
- **Übertragung** aufs eigene Produkt sofort skizzieren, z. B. „Hier ist das Lustige: Die Antwort liegt nicht in der Kopfhaut …“ für PCOS-Haarausfall.

---

## 6. Weg B: Verlierer mit Spend (Video-Autopsie)

**Vollständiger Ablauf:** `references/autopsie-video.md`.

**Zeitrahmen:** Mindestens 7 Tage laufen lassen. Verbrennt die Ad schnell Budget bei klar schlechten Werten, sofort stoppen und mit **Spend-Limit von 2 bis 3 × Ziel-CPA** neu starten, dann analysieren. Generell: jeder Ad ein Spend-Limit geben.

**Sieben Schritte:**
1. **Metriken ziehen, Bruchzone bestimmen.** Vier Zonen: **1 Hook** (Hook Rate niedrig) → **2 Body** (Hook gut, Hold Rate oder Watch Time niedrig) → **3 CTA/Angebot** (Hook und Hold gut, CTR niedrig) → **4 Funnel** (CTR gut, Conversion niedrig). **Immer die früheste kaputte Zone zuerst reparieren.**
2. **Video-Performance-Karte lesen.** Kurvenmuster: **Steile Klippe** (0 bis 3 s, Hook), **langsames Leck** (Abfall vor 15 s, Hook und Body passen nicht, Tempo, Wert kommt zu spät), **plötzlicher Absturz** (Reibung an einer Stelle: Verwirrung, Übergang, „klingt nach Ende“), **Plateau oder Spike** (hohes Interesse, oder Verwirrung durch Zurückspulen). Den größten Abfall in Prozentpunkten finden, die Scriptzeile dazu notieren, die Aufgabe dieser Stelle benennen und prüfen: **Hat sie ihre Aufgabe erfüllt? Wenn nein, warum nicht?**
3. **Ehrlicher Selbstcheck als Avatar.** Die Daten sagen, wo es bricht. Jetzt nur diese Zone als Avatar ansehen. Gute Zahlen trotzdem anzweifeln.
4. **Mismatch-Diagnose** (nur bei Zone 2 und 3): Sprache, Bewusstseinsstufe, Emotion und offene Schleifen, Glaubwürdigkeit, Tempo und Energie.
5. **Format- und Delivery-Check:** echte UGC, KI-UGC, Voiceover plus B-Roll, nur Text, KI-Animation. Liest der Creator ab? **Lag es am Briefing?**
6. **Einen Fatal Flaw benennen** und einer Ursachen-Kategorie zuordnen: Avatar-Recherche, Script-Struktur, Hook, Creator-Delivery, Angebot/CTA, Marktsättigung, Produktion. **Festhalten, was funktioniert hat**, damit es nicht mit weggeworfen wird.
7. **Version 2 bauen:** Hypothese, Änderungstabelle (was scheiterte, was stattdessen, warum), Briefing-Anpassungen, Format-Wechsel. Struktur: Erreichen nur ca. 10 % das Ende, das Produkt früher zeigen und den CTA nach vorn ziehen. **Nur eine große Variable ändern.**

---

## 7. Weg C: Verlierer ohne Spend (CBO lehnt ab)

**Vollständiger Ablauf:** `references/autopsie-no-spend.md`.

- **Wann:** 7 bis 14 Tage in der CBO, kaum oder kein Spend. Discord: „7 bis 14 Tage ohne Spend → abschalten.“
- **Die Frage ist nicht „Warum klickt keiner?“, sondern „Warum will Meta das niemandem zeigen?“**
- Wahrscheinliche Ursachen ankreuzen: geringe vorhergesagte Interaktion (erster Frame wie Tapete), interne CBO-Konkurrenz (zu ähnlich zu einer laufenden Ad), sieht von Frame 1 an wie Werbung aus (Produkt, Logo, Angebot zuerst, bei Top of Funnel), Creative passt nicht zum Pixel-Publikum, Policy-Soft-Flag, Ermüdung durch Mini-Iterationen, geringe vorhergesagte CTR, Format-Nachteil (verschiedene Formate im selben Ad Set), schwache Copy oder Headline.
- **Mit dem Spender derselben CBO vergleichen:** erster Frame, erste Worte, Format, Energie und Tonfall, Angle und Hook-Typ, Primärtext und Headline.
- **Selbstcheck ohne Metriken:** Scroll-Test im Feed, erster-Frame-Test, würde jemand liken, kommentieren oder teilen?
- **Aktionsplan:** 3 Änderungen, Hypothese, Version 2. Wenn das Konzept selbst falsch war: neues Konzept statt Iteration.
- **Formate im Ad Set nicht mischen**, sonst gewinnt oft das Bild-Format durch Aufmerksamkeit, nicht durch Botschaft.
- **Native Ads:** viele Varianten bekommen keinen Spend. In eine eigene „Graveyard“-CBO mit Cost Cap auf Ziel-CPA verschieben. Analysiert wird nur, was Spend bekam.

---

## 8. Weg D: Long-Copy-Native-Ads

**Vollständige Vorlage:** `references/long-copy-native.md`.

- **Nutzerreise:** Bild stoppt das Scrollen → die ersten drei Zeilen entscheiden über „Mehr anzeigen“ → Story → Klick, sobald überzeugt → Produktseite. Erste Iteration bei einer schwachen Native-Ad: **Bild**, dann **die ersten drei Zeilen**.
- **10-Punkte-Architektur:** Hook (Zeile 1 bis 3), World Building, gescheiterte Versuche, Wendepunkt, Autoritätsfigur, Mechanismus, Einwandbehandlung, später Produkt-Reveal, Ergebnisse mit Future Pacing, Auflösung in der Beziehung, CTA mit Verlustangst. Dazu Format (eine Aussage pro Zeile, Leerzeilen, keine Emojis oder Fettungen, wie selbst bei Facebook getippt).
- **„Kann nicht aufhören zu lesen“-Analyse:** eine große Schleife bis zum Reveal, viele kleine Schleifen, **jede neue Schleife öffnen, bevor die alte schließt**, pro Abschnitt eine andere Emotion, Unterhaltung (Details, Dialoge, Wendungen, Tempowechsel).
- **Bei Verlierern zusätzlich:**
  - **Demografie-Check:** Liefert Meta an den Avatar aus? (Beispiel: 85 % Männer erreicht, Avatar sind 90 % Frauen. Dann ist es ein Signal-Problem in Bild oder Sprache, kein Qualitätsproblem der Copy.)
  - **Bewusstseinsstufe:** Passt die Architektur? Problem-aware Avatar mit 400 Zeilen Ursachenerklärung = Langeweile. Unaware Avatar mit sofortiger Lösung = Überforderung.
  - **Bauchgefühl-Lesung als Avatar:** Hast du überhaupt etwas gefühlt? Wenn nein, ist die Ad tot. Dann ist das Avatar-Verständnis zu flach, und keine Strukturänderung rettet sie.
  - **Reibungs-Lesung:** Wo wurde es langweilig, unlogisch, unglaubwürdig, zu komplex, oder wo klang es plötzlich nach Werbung?
  - **Die Zeile, an der es am häufigsten bricht, ist das Ende.** Alles danach ist ungelesen. Von oben reparieren.

---

## 9. KI richtig einsetzen

Details und fertige Prompts: `references/prompts.md`.

1. **Erst die eigene manuelle Analyse fertig machen.**
2. **Gemini (AI Studio):** Video hochladen, Breakdown-Prompt mit den 4 Ebenen. Verlangen, **keinen Abschnitt auszulassen**, denn Gemini hat im Kurs mehrfach Teile übersprungen.
3. **Vergleichs-Prompt** im selben Chat: eigene Analyse hochladen. Bewertung in 5 Kategorien (Tiefe, Genauigkeit, Psychologie, Umsetzbarkeit, Mustererkennung, je /10), Stärken, kritische Lücken, wo du tiefer warst, blinde Flecken, Verbesserungsplan. Kursbeispiel: erster Breakdown 25/50 („zu wenig Warum“), zweiter 43/50.
4. **Widersprechen, wenn du anderer Meinung bist.** Die KI liegt auch falsch. Im Kurs hörte sie einen „Schrei“, den es nicht gab, und deutete die Musik falsch. Die Diskussion selbst ist der Lerneffekt (Beispiel Alter: Kernkäufer 35+ mit Budget für ein Abo, Halo-Publikum 25+).
5. **Blinde Flecken ins Lern-Notizbuch** und beim nächsten Breakdown gezielt darauf achten. Zakarias typische Lücken: Visuals und Farben, Audio, Begründungen.

---

## 10. Typische Fehler

- Nur Winner analysieren, Verlierer ignorieren, und stattdessen „mehr Volumen“ fahren. Laut Zakaria ist Volumen ohne Learnings ein Spielautomat.
- Direkt zur KI springen. Man liest das Ergebnis, aber es bleibt nichts hängen.
- Häkchen ohne Warum.
- Nur auf Metriken schauen, ohne die Ad anzusehen, oder umgekehrt.
- Den CTA reparieren, obwohl schon der Hook bricht.
- Fünf Dinge gleichzeitig ändern.
- Aus Avatar-Sicht urteilen, ohne die Avatar-Recherche offen zu haben.
- Fremde Ads aus anderem Bewusstseins- oder Sättigungsniveau 1:1 übernehmen.
- Beim Verlierer alles wegwerfen, auch die Teile, die funktioniert haben.
- Bei der Analyse unterbrechen, Tage später weitermachen und die eigenen Gedanken vergessen haben (im Kurs passiert: Autorität erst mit 3, dann zu Recht mit 8 bewertet).

---

## 11. Output-Format und Endkontrolle

Jeder Breakdown endet als Dokument mit diesem Kopf, abgelegt im Ad-Lab beim jeweiligen Ad-Namen:

```
AD: [Name/ID] | Produkt | Format | Länge | Weg A/B/C/D | Analyse-Datum
STATUS: Super-Winner / Winner / Verlierer mit Spend / No-Spend / Konkurrenz
METRIKEN: Spend, Tage, CPA vs. Ziel, Hook Rate, Hold Rate, Ø Watch Time, CTR, CPC, CPM, CVR
URSPRÜNGLICHE HYPOTHESE: (aus dem Ad-Lab, vor Launch)
ERGEBNIS: Kern-Erfolgsfaktor ODER Fatal Flaw (1 Satz) + Ursachen-Kategorie
TOP 3 GRÜNDE (Winner) / WAS FUNKTIONIERT HAT (Verlierer)
MUST-HAVE / NICE-TO-HAVE
HYPOTHESEN (max. 3): Wenn wir X …, dann Y …, weil Z …
NÄCHSTE VERSION: geänderte Variable, Briefing-Änderungen
LERN-NOTIZ: Was habe ich gelernt, das ich vorher nicht wusste? Welches Muster sehe ich über mehrere Analysen?
```

**Endkontrolle:**
- [ ] Ursprüngliche Hypothese aus der Zeit vor dem Launch eingetragen, nicht nachträglich erfunden.
- [ ] Jede Bewertung hat eine Begründung.
- [ ] Metriken und Ansehen stimmen überein, oder der Widerspruch ist erklärt.
- [ ] Genau ein Fatal Flaw bzw. ein Kern-Erfolgsfaktor.
- [ ] Höchstens 3 Hypothesen, jede testbar, nur eine große Variable pro Version.
- [ ] KI-Vergleich gemacht, Lücken ins Notizbuch übertragen.
- [ ] Ergebnis an den Testing-Workflow übergeben (bei Testbatches über den Skill `falunara-creative-testing`).

---

## 12. Leitplanken

- **Gesundheitsaussagen:** Gute Winner formulieren vorsichtig („kann die Ursache sein“, „unterstützt“, „oft“). Nachgebaute Versionen nur mit zulässigen Claims (EU Health Claims bei Nahrungsergänzung) und ohne Heilversprechen.
- **Ergebnisse realistisch und gestaffelt** („an Tag 14 weniger Schmerz, nicht weg“). Wunder-Zeitlinien sind unglaubwürdig, führen zu Chargebacks und sind laut Zakaria „kein Brand, sondern Scam“.
- **Keine Schuld beim Avatar.** Immer einen Bösewicht außerhalb der Person aufbauen.
- **Testimonials und Vorher-Nachher nur echt.** KI-Avatare, die sich als echte Kundinnen ausgeben, sind problematisch. Zakaria im Discord zu echten vs. KI-Creators: „Eins ist legal, eins nicht.“ Für KI-Formate siehe Skill `yapping-ad`.
- **Fremde Ads analysieren, nicht 1:1 kopieren.** Struktur, Technik und Psychologie übernehmen, Inhalte eigenständig machen.

Verwandte Skills: `copywriting-grundlagen` (Bewusstseinsstufen, Sophistication, Kaufemotionen, Hooks), `ugc-script` (Script aus den Learnings schreiben), `yapping-ad` (KI-UGC umsetzen), `falunara-creative-testing` (Testbatches und Testing-Log).

---

## 13. Erkenntnisse aus eigenen Analysen

Nach jeder Analyse hier eintragen: eigene Benchmark-Werte im Konto (Hook Rate, Hold Rate, CTR, CVR), wiederkehrende Fatal Flaws, eigene blinde Flecken aus den KI-Vergleichen, Muster über mehrere Winner und Verlierer.

- _(noch keine eigene Analyse)_
