# Autopsie: Video-Ad mit Spend, die verloren hat (Weg B)

Nach Lektion „The Full Autopsy“ (Losing Ad Lab). Für Ads, die echtes Geld bekommen und trotzdem nicht funktioniert haben.

**Zeitregel:** mindestens 7 Tage. Ausnahme: Die Ad verbrennt Budget bei klar schlechten Werten. Dann sofort aus, mit Spend-Limit von 2 bis 3 × Ziel-CPA neu starten, einige Tage laufen lassen, dann analysieren. Bei hohem Tagesbudget (z. B. 10.000 $/Tag) jeder Ad ein Maximum geben.

**Immer im Team** mit allen, die an der Ad beteiligt waren: Jeder sieht etwas anderes.

---

## Schritt 1: Metriken ziehen und Bruchzone bestimmen

**Basisdaten:** Ad-ID und Link, Name, Produkt, Gesamtspend bis zum Stopp, Laufzeit, Länge, Iterationsnummer (Version 1, 2, 3 …), **ursprüngliche Hypothese aus dem Ad-Lab**.

| Metrik | Wert | Richtwert | Urteil |
|---|---|---|---|
| Hook Rate (3-s-Views ÷ Impressionen) | | 30 bis 45 %, ab 50 % stark, unter 20 % ersetzen | |
| Hold Rate (ThruPlays ÷ 3-s-Views) | | ab 25 % | |
| Ø Wiedergabezeit (s und % der Länge) | | | |
| CTR (Link) | | ab 2 % gesund | |
| CPC | | | |
| CPM | | vs. Kontodurchschnitt | |
| Conversion Rate der Seite | | 2 bis 3 % gesund | |
| CPA | | vs. Ziel-CPA | |

Hinweis zur Hook Rate: Meta zeigt die Ad bereits den Pixel-ähnlichsten Menschen. Wenn selbst die nicht stoppen, ist der Hook schwach. Eine niedrige Hook Rate bei guter Conversion heißt: Die Ad ist gut, aber der Hook kann mehr.

### Die vier Zonen
| Zone | Erkennungsmerkmal | Bedeutung |
|---|---|---|
| **1 Hook** | Hook Rate niedrig | Die ersten 3 s verdienen keine Aufmerksamkeit. |
| **2 Body** | Hook Rate okay, Hold Rate und Watch Time niedrig | Clickbait-Hook, oder der Body hält das Versprechen nicht (BS-Detektor, schwache Visuals, Frage zu früh beantwortet). |
| **3 CTA/Angebot** | Hook und Hold gut, CTR niedrig | Unterhaltsam, aber kein Kaufimpuls: schwacher CTA, kein Angebot, keine Dringlichkeit. |
| **4 Funnel** | CTR gut, Conversion niedrig | Die Ad hat ihren Job gemacht. Landingpage prüfen: Kongruenz, Design, Ladezeit. |

**Priorität:** Immer die früheste kaputte Zone zuerst. Kombinationen:
- Body-Klippe + niedrige CTR → Body zuerst.
- Body-Klippe + niedrige Conversion → Body zuerst, dann Funnel.
- Hook-Klippe + niedrige CTR → Hook. Vielleicht ist die ganze Ad daneben.
- Keine Klippe + hoher CPC → Publikum zu eng oder Engagement-Problem.

---

## Schritt 2: Video-Performance-Karte lesen

Ads Manager → Ad → Diagramm-Symbol → Video-Performance. Zeigt Sekunde für Sekunde die ersten 60 s. Danach nur 25/50/75/100 %-Marken.

**Kurvenmuster erkennen:**
| Muster | Bild | Ursache |
|---|---|---|
| **Steile Klippe** | senkrechter Abfall in 0 bis 3 s | Hook. Erster Frame statisch, unklar oder nicht stoppend. |
| **Langsames Leck** | stetiger Abfall bis 15 s | Hook und Body passen nicht, zu langsam, Kernwert kommt zu spät, keine Emotion. |
| **Plötzlicher Absturz** | scharfer Knick in sonst stabiler Kurve | Reibung an genau dieser Stelle: Verwirrung, Erklärung, Übergang, Rhythmuswechsel, etwas, das nach Ende klingt. |
| **Plateau oder Spike** | Kurve flacht ab oder steigt | Sehr fesselnde Stelle (Demo, Info), oder Verwirrung, sodass zurückgespult wird. Ansehen, was es war. |

**Größte Klippe finden:** Prozentwerte je Abschnitt eintragen (z. B. 0 bis 3 s 100 %, 3 bis 5 s 72 %, 5 bis 10 s 54 %, 10 bis 15 s 21 % → größte Klippe 33 Punkte zwischen 10 und 15 s).

Für die größte Klippe ausfüllen:
1. Was passiert an dieser Stelle? Nüchtern beschreiben: Bild, Voiceover, Text.
2. Welche Scriptzeile läuft genau dort?
3. Welcher Abschnitt ist es? Hook, Problem, Übergang, Mechanismus, Beweis, CTA, Story-Beat, Produkt in Aktion, Vergleich, Unterhaltung …
4. Was soll diese Stelle leisten?
5. **Hat sie es geleistet? Wenn ja, warum gingen die Leute trotzdem? Wenn nein, warum nicht?** (Beispiel: Script gut, aber neue Visuals schwach. Oder Mechanismus zu komplex. Oder Avatar ist solution-aware und bekommt eine Ursachen-Vorlesung.)

---

## Schritt 3: Ehrlicher Selbstcheck als Avatar

Schreiber-Gehirn ≠ Avatar-Gehirn. Werde der Mensch, der um 23 Uhr müde und skeptisch scrollt. Gute Zahlen nicht blind glauben.

**Zone 1, nur die ersten 3 s:**
- Würde ich stoppen? Signalisiert es sofort „das ist für mich“?
- Gibt es Neugier, Pattern Interrupt oder Spiegelung, die die nächsten 3 s verdient?
- Etwas Neues, das ich im Feed noch nicht gesehen habe?
- Wirkt es organisch oder schreit es „Werbung“?
- **Funktioniert es stumm?** (Bis zu 85 % sehen zunächst ohne Ton: Untertitel, fetter Text, visuelle Hinweise.)

**Zone 2, vom Hook bis zur Klippe:** Warum habe ich das Interesse verloren?
- keine offene Schleife, nichts, worauf ich warte
- Antwort zu früh gegeben
- etwas wirkte fake oder übertrieben (BS-Detektor)
- über mich statt mit mir gesprochen (belehrend)
- fühlte sich wie ein Pitch an
- „das ist nicht für mich“-Moment
- Energie flach (gleicher Ton, gleiches Tempo, keine B-Roll-Variation)
- verwirrend, Logik bricht (häufig bei Mechanismus oder Analogie)
- Übergang zum Produkt zu hart (Bait and Switch)
- schon hundertmal gesehen (gleicher Angle, gleiche Claims)
- Creator-Stimme verlor mich (klang abgelesen)

Dann: In welcher Sekunde driftete meine Aufmerksamkeit? Passt das zur Kurve? Wenn nicht, trotzdem reparieren, denn bei wenig Spend ist die Kurve dünn.

**Zone 3, ganze Ad:**
- War ich beim CTA emotional bereit (Hype, Neugier, sehe mich mit dem Ergebnis, Konsequenzen spürbar)?
- War das Angebot den Klick wert (Wert, Zeit, Aufwand, Wunschergebnis)?
- War der nächste Schritt glasklar?
- Gab es Dringlichkeit, einen Grund, jetzt zu handeln?
- Wirkte das Risiko zu hoch (keine Garantie, wirkt wie Scam)?
- Kam der CTA abrupt, ohne Aufbau oder Mikro-Commitments?
- Habe ich dem Versprechen geglaubt (Beweise, echte Erfahrung, Social Proof)?

**Zone 4, Landingpage** (die Ad nur kurz zur Kongruenz ansehen):
- Passt die Headline zum Versprechen der Ad? Ist der erste Eindruck kongruent?
- Lädt sie schnell? Gibt es Reibung (zu viele Schritte, CTA versteckt)?
- Sind Social Proof und Garantie sichtbar? Liegen gesuchte Infos zu tief?
- Clarity oder Hotjar: Wo klicken die Leute ins Leere, wo springen sie ab?

**Routing:** Zone 1 → Schritt 4 überspringen, Hook-Diagnose ist mit Schritt 3 erledigt. Zone 4 → Schritte 3 und 4 überspringen, Landingpage analysieren. Schritt 4 nur für Zone 2 und 3.

---

## Schritt 4: Mismatch-Diagnose (Zone 2 und 3)

Je nach Gefühl aus Schritt 3 den passenden Block wählen:
| Gefühl in Schritt 3 | Block |
|---|---|
| belehrt, „nicht für mich“ | 4.1 Sprache |
| „nicht für mich“, verwirrt | 4.2 Bewusstseinsstufe |
| gelangweilt, keine Schleife, Energie flach | 4.3 Emotion, 4.5 Tempo |
| fake, BS-Detektor | 4.4 Glaubwürdigkeit |
| „schon gesehen“ | Marktsättigung → direkt zu Schritt 6 |
| Creator-Stimme | direkt zu Schritt 5 |

**4.1 Sprache:** Avatar-Recherche öffnen. Wörtlich vergleichen: Was sagt die Ad an der Klippe? Wie sagt es der Avatar? (Beispiel: Ad sagt „stechender Schmerz im Fuß“, Avatar sagt „direkt neben dem Knie“.) Wo Marketingsprache statt ihrer Worte? Wo beschönigt statt ehrlich? Wo ein Schmerzpunkt angenommen, der nicht in der Recherche steht?

**4.2 Bewusstseinsstufe:** Stufe des Avatars vs. Stufe, für die die Ad spricht. Bekanntes erklärt (herablassend)? Schritte übersprungen (Mechanismus der Lösung vor der Ursache)? Fachbegriffe, die der Avatar nicht kennt?

**4.3 Emotion:** Welche Emotion sollte an der Klippe entstehen? Was entstand tatsächlich (Langeweile, Verwirrung, Skepsis, Genervtheit, nichts)? Gab es eine offene Schleife? Wenn nein: Welche Frage hätten wir für die nächsten 10 bis 30 s in den Kopf setzen können?

**4.4 Glaubwürdigkeit:** Welcher Claim oder Moment löste den BS-Detektor aus? Welcher Beweis fehlte? War der Mechanismus zu komplex oder zu dünn?

**4.5 Tempo und Energie:** Energie der Ad an der Klippe (zu hoch, zu flach, monoton) vs. Energie, die der Avatar braucht (ältere Zielgruppe: ruhiger; jüngere: schneller, mehr Schnitte). Wo genau verlor das Tempo sie?

---

## Schritt 5: Format- und Delivery-Check

**Echte UGC:** Klang es abgelesen? Hat der Creator die Beats verstanden oder nur auswendig gelernt? Echte Emotion mit Höhen und Tiefen? Energie passend zum Avatar? Würde der Avatar dieser Person vertrauen (Alter, Typ, Autorität)? Hat der Creator eigene Emotion abgerufen oder gespielt?
**Lag es am Briefing?** Avatar erklärt? Emotionale Cues statt nur Text? Script in verdauliche Stücke geteilt? Raum für natürliche Sprache?

**KI-UGC / KI-Avatar:** Hält der Avatar für echt, was er sieht? Wo bricht es (Mimik, Bewegung, Stimme)? Natürliche oder robotische Stimme? **Hat das Format der Glaubwürdigkeit geschadet, oder war das Script das Problem?** (Siehe Leitplanken in SKILL.md und Skill `yapping-ad`.)

**Voiceover + B-Roll:** Passt die Stimme zum Avatar und klingt sie vertrauenswürdig? Stützt die B-Roll die Botschaft oder lenkt sie ab? Genug visuelle Abwechslung? Synchron zum Voiceover?

**Nur Text:** In Scrollgeschwindigkeit lesbar? Genug auf dem Bildschirm? Lenkt der Hintergrund ab? Tempo des Textes? Story oder PowerPoint?

**KI-Animation / Motion Graphics:** Wirkt es hochwertig oder billig? Passt der Stil zur Marke und zum Avatar (ältere Zielgruppe ≠ Cartoon)? Lenkt Animation von der Botschaft ab? Wäre UGC oder Voiceover besser?

**Analogien im Mechanismus:** Bild und Analogie müssen zur Ursache passen. Kursbeispiel Lymphödem: Lymphbahnen = Straße, Blockade = Autounfall, Stau = Schwellung. Die besten Analogien stammen aus Reddit und Foren, wo Betroffene es sich gegenseitig erklären.

---

## Schritt 6: Den einen Fatal Flaw benennen

„Die Ad scheiterte vor allem, weil …“ (ein Satz, darf Unterpunkte haben).

**Ursachen-Kategorie:**
- Avatar-Recherche (falsche Sprache, falscher Schmerzpunkt, falsche Stufe)
- Script-Struktur (Fluss bricht, holpriger Übergang, schwacher Mechanismus, fehlender Beweis)
- Hook (kommt nicht über 3 s)
- Creator-Delivery (Script gut, Performance oder Format tötet es)
- Angebot/CTA (geschaut, aber nicht gehandelt)
- Marktsättigung (Angle totgeritten)
- Produktion/Visuals (billig, verwirrend, Bild passt nicht)

**Was hat funktioniert?** (Das Kind nicht mit dem Bade ausschütten.) Hook, Hold, Positionierung, Creator usw. als Bausteine für die nächste Version festhalten.

---

## Schritt 7: Version 2 bauen

- **Hypothesen (1 bis 3):** „Wenn wir [Element] von [Ansatz] zu [neuem Ansatz] ändern, erwarten wir [Metrik-Verbesserung], weil [Avatar-Psychologie].“
- **Änderungstabelle:** Was scheiterte | Was wir stattdessen tun | Warum (Avatar-Einsicht), je Zone.
- **Briefing-Anpassung:** emotionale Cues, Beats vereinfachen, Story mit Gefühl des Creators verbinden, Energie und Ton, Format-Wechsel (z. B. KI → Creator).
- **Struktur:** Erreichen nur ca. 10 % das Ende, nichts für den Schluss aufheben. Produkt früher zeigen, beiläufigen CTA vorziehen („ich hab das bei dieser Marke gefunden …“).
- **Eine Variable isolieren:** neuer Hook, neuer Body-Mechanismus, neues Voiceover-Framing, neuer Creator, neues Format, neuer Angle, CTA vorziehen.
- Ist das ganze Konzept falsch (passt nicht zum Avatar), ist das keine Iteration mehr. Dann ein neues Konzept mit den Learnings bauen.
