---
name: singing-ad
description: Erstellt hochwertige gesungene Werbe-Ads (Singing Ads / Suno Ads) im Pixar-3D-Look aus einer Winning-Copy. Song über Suno, Startbilder über Nano Banana Pro bzw. GPT Image 2, Clips über Kling 3.0, alles über einen Kie.ai-API-Key, Schnitt und Untertitel mit ffmpeg. Verwenden bei "Singing Ad", "Suno Ad", "gesungene Ad", "Song-Ad", "Copy als Song", "Musical-Ad". Enthält erprobte Qualitätsregeln, Modellwahl, Kosten und Endkontrolle aus einer echten 5-Minuten-Produktion.
---

# Singing Ad (Suno Ad) im Pixar-Look

Dieser Skill macht aus einer bewährten Verkaufs-Copy eine **komplett gesungene Ad**: Die Copy wird als durchgehender Song über einen treibenden Beat erzählt. Jede gesungene Zeile bekommt einen stummen Pixar-3D-Clip, dazu kommen eingebrannte Untertitel. Das Ergebnis ist ein 9:16-Video mit 3 bis 5 Minuten Länge.

Alle Regeln unten stammen aus einer echten Produktion. Die Beispiel-Ad lief 5:22 mit 74 Szenen und brauchte drei Korrekturrunden. **Jede Regel steht hier, weil ihr Fehlen einmal eine Korrekturrunde gekostet hat.** Halte dich daran, dann wird schon der erste Durchgang deutlich besser.

---

## 0. Grundhaltung (die wichtigsten Regeln zuerst)

1. **Qualität ist das Ziel, nicht das billigste Video.** Gesucht ist das beste Ergebnis zum nötigen Preis. Für einen Clip nie mehr zahlen als nötig, aber auch nie an der Qualität sparen.
2. **Keine Flicken.** Nie Bereiche unscharf machen. Nie Bildausschnitte (Displays, Zahlen, Packungen, Poster) über laufende Clips legen. Nie digitale Zooms oder Zeitlupe als Notlösung einsetzen. Das sieht billig und fake aus und fällt sofort auf. Eine fehlerhafte Szene wird **komplett neu und sauber generiert** oder bleibt, wie sie ist.
3. **Einheitlicher Look:** ein Standard-Videomodell für alle Clips (Kling 3.0). Ein anderes Modell nur für einzelne Clips, die der Standard nachweislich nicht schafft, und nur, wenn der Stil passt.
4. **Szenen im Detail richtig, nicht nur grob.** Jedes Bild muss exakt zur gesungenen Zeile passen: Körperstelle, Tageszeit, Reihenfolge, Medikamente, Aufzählungen und die Frage, wer was in der Hand hält.
5. **Alles Geschriebene im Bild in der Sprache der Ad.** Bei einer deutschen Ad sind Poster, Formulare, Zettel, Broschüren und Medikamentenpackungen deutsch oder ohne Schrift. Englische Wörter im Bild passen nicht.
6. **Flüssig im Originaltempo.** Clips höchstens um 8 % dehnen, mehr wirkt zeitlupig und lagghaft. Nie ein Standbild am Clip-Ende.
7. **Mimik passt zur Zeile.** Bei traurigen oder schlechten Momenten lächelt niemand. Die Videomodelle setzen gern ungefragt ein Lächeln.
8. **4:5-Sicherheitszone.** Facebook schneidet 9:16 im Feed auf 4:5 zu. Gesichter und alles Wichtige gehören in die mittleren 70 % der Bildhöhe (bei 1080×1920 die Zeilen 285 bis 1635). Ziel: 95 bis 100 % der Clips.
9. **Vor jedem Kostenschritt die Freigabe holen:** Song, Szenenplan, Figuren, dann Produktion. Nichts hochladen oder veröffentlichen ohne ausdrückliche Freigabe.
10. **Nach jedem Schritt selbst prüfen** (hören, ansehen, messen), erst dann weiter.

---

## 1. Voraussetzungen

- **Kie.ai-Account mit API-Key und Guthaben** (https://kie.ai). Ein Key deckt Suno, Nano Banana Pro, GPT Image 2, Kling, Veo, Hailuo und Seedance ab. Den Key in eine `.env` legen (`KIE_API_KEY=…`, Rechte 600) und nie in Chats, Notizen oder Code schreiben.
- **Speech-to-Text mit Wort-Zeitstempeln** für das Untertitel-Timing. Getestet ist ElevenLabs `scribe_v1` (erkennt deutschen Gesang gut). Alternativ Whisper.
- **ffmpeg** und **Python 3 mit Pillow und numpy**. Hinweis: Das Homebrew-ffmpeg bringt oft kein `libass`/`drawtext` mit, dann Untertitel als Bilder rendern (Abschnitt 9).
- Vom Auftraggeber: die **Winning-Copy**, belegte **Produkt-Fakten**, die **Packungsdatei** (freigestellte Vorderseite als PNG), die **Aussprache** des Markennamens, **Figurenwünsche** und das **Naming** bzw. den Ablageort.

### Budget (Kie-Credits, 1 Credit = 0,005 $)
| Posten | Preis |
|---|---|
| Suno Song (2 Varianten) | 12 |
| Startbild Nano Banana Pro 2K | 18 |
| Startbild GPT Image 2 2K | 10 |
| Clip Kling 3.0 std 720p | 70 (5 s), 140 (10 s) |

**Faustregel:** Eine 5-Minuten-Ad mit ca. 75 Szenen kostet im ersten Durchgang ca. 7.500 Credits, eine 3-Minuten-Ad ca. 4.500. Für Korrekturen 15 bis 25 % Puffer einplanen. Die Beispiel-Ad kam mit allen Korrekturen auf ca. 10.000 Credits. Mit diesem Skill sollte deutlich weniger nötig sein.

---

## 2. Ablauf im Überblick

```
Copy → Songtext → [Freigabe] → Suno (2 Varianten, prüfen) → [Auswahl] → Songanfang/-ende schneiden
     → Zeilen-Timing (STT) → Szenenplan → [Freigabe] → Figuren-Vorlagen → [Freigabe]
     → 1 Test-Szene (Bild + Clip, Kosten messen) → Hochrechnung → [Freigabe]
     → alle Startbilder → Prüfung/Korrektur → alle Clips → Prüfung/Korrektur
     → Schnittplan → Schnitt + Untertitel + Song → Endkontrolle → [Abnahme] → Naming + Ablage
```

---

## 3. Songtext (aus der Copy)

### Länge
- **Richtwert 3 bis 5 Minuten, Optimum 3 Minuten.** Starke Singing Ads laufen auch 5 Minuten.
- **Gemessen:** Suno singt Deutsch mit **ca. 125 bis 131 Wörtern pro Minute**, unabhängig von der BPM-Angabe, plus 5 bis 11 s Ausklang. Englisch liegt eher bei 2,4 Wörtern pro Sekunde.
  - **3 Minuten ≈ 370 Wörter, 5 Minuten ≈ 620 Wörter.** Harte Grenze für Lyrics: 5.000 Zeichen.
- **Copy nur so weit kürzen, wie es für die Länge nötig ist, nicht mehr.** Erst die Fassung mit minimaler Kürzung bauen, Wörter zählen, Länge hochrechnen, dann mit dem Auftraggeber entscheiden.
- Beim Kürzen die **Quintessenz jeder Stelle behalten**, nie relevante Beweise, Zahlen oder Wendepunkte streichen. Nichts streichen, was „nur Detail“ scheint, aber die Glaubwürdigkeit trägt (z. B. „Woche eins: noch nichts, nur mehr Boden unter den Füßen“).

### Verständlichkeit (gesungen hört man schlechter als gelesen)
- **Eine Sache einmal vollständig sagen, danach darf sie vereinfacht werden.** Beispiel: erst „nach dem Pinkeln blieben 95 Milliliter in der Blase“, später nur noch „Restharn 95“.
- **Bezüge ausschreiben:** nicht „die OP schneidet es weg“, sondern „die OP schneidet das Geschwollene weg, aber nicht den Grund“. Nicht „auf dem Zettel“, sondern „Sie schrieb mir auf: …“.
- Andeutungen, die man beim Hören nicht versteht, ausformulieren (z. B. „und als Mann ging seit zwei Jahren nichts mehr“).
- **Zahlen und Abkürzungen ausschreiben, wie sie gesungen werden sollen:** „hundertsiebenundzwanzig zu neunundsiebzig“, „Kuh zehn“ statt Q10, „Vitamin K zwei“. In den Untertiteln stehen sie später wieder als Ziffern.
- **Aussprache-Lock** für Marken- und Fremdwörter vorher mit dem Auftraggeber festlegen. Prüfen, wie Suno sie singt (STT-Transkript).

### Struktur (Message-Motor aus einer echten Winner-Singing-Ad)
1. **Hook als offene Schleife, sofort gesungen** (kein Intro): ein Ergebnis, das man verstehen muss.
2. **Vorgeschichte und Leidensdruck** des benannten Avatars mit konkreten Zahlen und Alltagsmomenten.
3. **Ein Villain:** viele Symptome auf eine Ursache ziehen.
4. **Mechanismus** anschaulich erklären (das wird später die Anatomie-Animation).
5. **Transformations-Kaskade:** Woche 1, 2, 3 … mit je **einem konkreten, sinnlichen Mikro-Ereignis pro Zeile**.
6. **Beweis** (Messwerte, Arztreaktion), **Angebot/Garantie**, **CTA** („Drück unter dem Video auf Mehr dazu“).
7. Emotionaler Schluss.

### Schreibregeln
- Zeilen mit 4 bis 8 Wörtern, eine Aussage pro Zeile, singbar betont.
- Du-Form, Alltagssprache, keine Gedankenstriche.
- **Gesungene Logik:** kein „wenn du das liest“ und kein „Link unten“. Es wird gehört.
- Nur belegte Aussagen, keine erfundenen Zahlen oder Studien.
- Struktur-Tags: `[Verse]`, `[Build]`, `[Chorus]` (optional), `[Bridge]`, `[Outro]`. **Kein `[Intro]`.**

---

## 4. Song mit Suno (über Kie.ai)

**Style-Prompt** (kommagetrennt, ohne Lyrics), z. B.:
`emotional cinematic pop, warm sincere male vocal, storytelling cadence, driving 96 BPM beat, clean modern production, no intro, vocals start immediately, short ending, German lyrics`

**API-Aufruf:**
```
POST https://api.kie.ai/api/v1/generate   (Authorization: Bearer <KEY>)
{"prompt": "<Lyrics mit Tags>", "style": "<Style>", "title": "<Titel>", "customMode": true,
 "instrumental": false, "model": "V4_5", "callBackUrl": "https://example.com/cb"}
→ data.taskId
GET https://api.kie.ai/api/v1/generate/record-info?taskId=…
→ bei status == SUCCESS: data.response.sunoData[].audioUrl (2 Varianten)
```
Für lange Songs (ab ca. 4 Minuten) V4_5 oder neuer verwenden. `callBackUrl` ist Pflicht, auch wenn gepollt wird.

**Jede Variante prüfen**, bevor sie dem Auftraggeber vorgelegt wird:
- Per STT transkribieren und gegen den Songtext abgleichen. Suno wiederholt manchmal ganze Strophen (einmal 792 statt 669 Wörter) oder lässt etwas aus.
- Länge und Ausklang notieren, Aussprache der Markennamen prüfen.
- Beide Varianten zum Anhören geben, der Auftraggeber wählt.

**Songanfang schneiden:** Suno setzt trotz `no intro` oft 2 bis 3 s Musik vor den Gesang.
- Den ersten Gesangseinsatz über die STT-Wortzeit bestimmen. Die Musikschläge über Lautstärke-Anstiege im Bass finden.
- **Genau auf einen Schlag kurz vor dem ersten Wort schneiden**, 10 ms Einblendung.
- Direkt am Wort wirkt es zu abrupt. Ein Schnitt zwischen zwei Schlägen klingt nach „Umschwung“.

**Ausklang:** Nach dem letzten Wort höchstens 2 bis 3 s Musik, sonst mit Ausblenden kürzen.

---

## 5. Zeilen-Timing

- Den geschnittenen Song per STT mit Wort-Zeitstempeln transkribieren. Wird erst danach geschnitten, alle Zeiten um den Schnitt-Versatz verschieben.
- Jede Songzeile auf Start- und Endzeit legen, per Sequenz-Abgleich Lyrics ↔ STT-Wörter (z. B. `difflib.SequenceMatcher`). Die **Schreibweise kommt aus den Lyrics**, nicht aus dem STT.
- Ergebnis als `zeilen_timing.json`. Das Zeitfenster jeder Szene beginnt ca. 0,15 s vor ihrer ersten Zeile.

---

## 6. Szenenplan

- **Eine Szene pro Songzeile oder pro zwei kurzen Zeilen**, jeweils 2 bis 7 s. Jede Szene zeigt genau, was gesungen wird.
- **Figuren-Bibel:** Hauptfigur (benannter Avatar), Partnerin, Arzt, Arzthelferin usw. Jede mit festem Aussehen, fester Kleidung und festen Details, z. B. „Ehering NUR an der rechten Hand“. Für Nachtszenen eine eigene Kleidungsbeschreibung (Schlafzeug).
- **Wiederkehrende Orte** fest beschreiben (Küche, Praxis, Bad), dazu ein Stil-Lock-Satz für alle Bilder.
- Heikle Inhalte (Toilette, Intimes) dezent, aber glaubwürdig zeigen: von hinten, angedeutet, nie explizit.
- **Vor der Freigabe Zeile für Zeile gegen die Copy prüfen:**
  - Tageszeit: Wird die Tablette abends genommen?
  - Körperstelle: Ultraschall am Unterbauch, nicht mittig.
  - Reihenfolge: Die Packung kommt erst, nachdem sie bestellt wurde.
  - Medizinische Logik: Retardkapseln halbiert man nicht, also zeigt man ein neues Rezept.
  - Exakte Aufzählungen: „sieben Sachen“ bedeutet genau sieben Symbole.
  - Mimik und Schrift.
- Den Szenenplan als Tabelle zur Freigabe vorlegen (Zeile | Szene | Figuren | Stimmung).

---

## 7. Startbilder

**Standardmodell: Nano Banana Pro, 2K, 9:16, 18 Credits.** Es hält die Figuren am besten, wenn die Figuren-Vorlagen als Referenzbilder mitgegeben werden.
```
POST https://api.kie.ai/api/v1/jobs/createTask
{"model": "nano-banana-pro", "input": {"prompt": "...", "aspect_ratio": "9:16", "resolution": "2K",
  "output_format": "png", "image_input": ["<URL Figur 1>", "<URL Ort>", ...]}}
GET https://api.kie.ai/api/v1/jobs/recordInfo?taskId=…   → state success, resultJson.resultUrls
```
Referenzbilder lädst du vorher über den Kie-Upload-Endpunkt hoch. Die URLs halten ca. 3 Tage, also cachen.

### Figuren-Vorlagen zuerst
- Pro Figur ein Einzelbild erzeugen (ausdrücklich „single character, one view, no character sheet“) und vom Auftraggeber freigeben lassen.
- Sitzt ein Detail falsch herum (Ring links statt rechts), das Bild **spiegeln** statt neu zu erzeugen. Das kostet nichts.

### Prompt-Regeln für Startbilder (alle aus echten Fehlern)
- Den **Stil-Lock** voranstellen: „Pixar/Disney-style 3D animation still, glossy soft-shaded render, warm stylized lighting, expressive eyes …“
- Die Referenzbilder im Prompt benennen: „Reference images in order: (1) Jürgen, (2) the kitchen …“
- **4:5-Zone** in jeden Prompt: „Keep heads, faces and all important objects in the middle of the image, within the central 70% of the image height.“
- **Schrift:** „No text anywhere“ oder deutsche Wörter vorgeben. Nano Banana schreibt in Anatomie- und Kalenderbildern gern englische Beschriftungen („PROSTATE“, „MONTH“, „Calendar“) und stellt englische Poster in Praxen. Das jedes Mal ausdrücklich verbieten.
- **Eindeutige Begriffe:** Aus „tablet“ wurde ein Tablet-Computer. Richtig ist „small round medicine pill, NOT a tablet computer“.
- **Aufzählungen nummerieren** und „EXACTLY SEVEN …, no other icons“ verlangen. Sonst fehlt oder verdoppelt sich etwas, z. B. drei statt zwei Kapseln.
- **Anatomie-Szenen:** „stylized, friendly Pixar-style medical animation inside the body, clean and not gory, soft glowing colors, rounded shapes, absolutely no text labels or letters“. Organe ohne Gesicht, außer es ist gewollt.
- **Gegenstände ohne Gesichter:** „Realistic objects: NO faces, no eyes on any object“. Sonst bekommen Kapseln, Gläser und Ultraschallgeräte Cartoon-Augen.
- **Wer hält was:** ausdrücklich, mit Ärmelfarbe beschreiben, z. B. „her RIGHT hand in the navy blue sleeve holds the probe; his hands are folded on his upper chest, far away from his belly; only one probe exists“. Sonst hält der Patient den Schallkopf selbst.
- **Toiletten-Szenen:** „normal white toilet directly in front of him, seat and lid flipped up leaning against the cistern (not sideways)“, Dreiviertel-Rückansicht, Hose hinten leicht unten, Hände vorne.
  - Ist der Strahl wichtig: „a thin yellow stream of water falls into the toilet bowl, visible through the gap between his legs“.
  - **Wörter wie „urine“ oder „urinating“ blockt Nano Banana als NSFW**, deshalb „stream of water“ schreiben.
- **Packung nie frei von der KI erfinden lassen** (falsche Texte wie „GARLIC OIL“). Stattdessen **GPT Image 2** mit der echten Packungsdatei als Referenz verwenden und jedes Wort der Packung im Prompt aufzählen. GPT Image 2 schreibt Packungstext fehlerfrei, Nano Banana nicht („CHOLESTERINSPIEDEL“).
  ```
  {"model": "gpt-image-2-image-to-image", "input": {"prompt": "...", "aspect_ratio": "9:16",
   "resolution": "2K", "input_urls": ["<Szene/Komposition>", "<echte Packung>"]}}
  ```
- **Kompositionsvorlage:** Ist ein Bild gut gelungen (z. B. eine WC-Szene), es als Referenz für ähnliche Szenen mitgeben („Recreate the composition reference exactly, but at night …“).
- **Displays mit Zahlen vermeiden**, wo es geht (siehe Abschnitt 8, Zahlen). Handschrift auf Papier bleibt im Video stabil.

### Prüfung der Startbilder
- Alle Bilder blockweise als **Übersichtsbogen** (6 bis 8 Bilder nebeneinander, Szenen-ID eingeblendet) ansehen und **jede Szene gegen ihre Songzeile halten**.
- Dazu einen **4:5-Rahmen** einzeichnen und Details vergrößern: Hände, Zahlen, Schrift, Ringe.
- Fehler per **Neuerzeugung** mit präzisiertem Prompt beheben. Bildbearbeitung („Edit this image …“) macht es oft schlimmer (plötzlich zwei Schallköpfe, neue Tippfehler), deshalb nur für kleine, klar begrenzte Änderungen.
- Verworfene Bilder in einen Ordner `verworfen/` verschieben, nie löschen.

---

## 8. Clips

**Standardmodell: Kling 3.0 std, 720p, ohne Ton** (`kling-3.0/video`). Sehr guter Pixar-Look, konsistente Figuren, hervorragende Anatomie-Animationen. Ausgabe 716×1284, 24 fps.
```
{"model": "kling-3.0/video", "input": {"prompt": "...", "duration": "5" | "10", "aspect_ratio": "9:16",
  "mode": "std", "sound": false, "multi_shots": false, "image_urls": ["<Startbild>"]}}
```
- **Clip-Länge so wählen, dass nichts gedehnt werden muss:** 10 s nehmen, wenn das Zeitfenster länger als 5,04 s × 1,08 ≈ 5,44 s ist, sonst 5 s.
- **Bewegungsprompt:** „Pixar-style 3D animation. <kleine, konkrete Handlung passend zur Zeile>. Static camera. Keep all characters, faces, clothes and the scene exactly consistent with the start image. No extra people, no extra objects, no scene cuts.“
  - Stumme Figuren: „Mouth closed, no talking, no lip movement.“ Sonst murmeln die Figuren.
  - Traurige Zeilen: „serious, worried face, no smiling at all“.
  - Dinge, die bleiben müssen: „The three jars stay on the table the whole time“, sonst verschwinden sie.
  - Handlungen, die gleich bleiben müssen: „she keeps the probe pressed on the same spot the entire video“.
- Bis zu **6 Aufträge parallel**, jeden Auftrag mit Task-ID loggen. Vorhandene Dateien überspringen, damit nichts doppelt bezahlt wird.
- **Kling lehnt manche medizinischen Nahaufnahmen ab** („violates our guidelines“). Dann Bildausschnitt oder Formulierung ändern und neu erzeugen, nicht das Standbild zoomen.

### Zahlen auf Displays: der bekannte Schwachpunkt aller Videomodelle
Getestet mit demselben Startbild (Blutdruckgerät „127/79“, 5 s):

| Modell | Ergebnis |
|---|---|
| Kling std | sauber bis ca. 3 s, danach „7Ω“ |
| Kling pro | ähnlich wie std |
| Kling mit Start = Endbild | schlechter |
| Hailuo 2.3 | 127 → 178 |
| Seedance 1.5 | 127 → 188 |
| Veo Lite | 79 ↔ 77 |
| Großes Display bei Kling | flackert sogar stärker |

**Lösungen ohne Flicken:**
- Nur den sauberen Teil des Clips nutzen und ihn genau auf die gesungene Zahl legen. Die Szene davor läuft dafür etwas länger (Schnittplan, Abschnitt 9).
- Oder die Zahl auf **Papier** zeigen (handgeschriebener Zettel, Notizbuch). Das bleibt stabil.
- Oder das Gerät weglassen, wenn die Zeile es nicht braucht.

### Prüfung jedes Clips
- **Je 6 Standbilder über die Länge**, die tatsächlich im Video zu sehen ist, als Bogen ansehen. Dabei prüfen:
  - wandernde oder verschwindende Objekte
  - dritte Hände
  - falsche Mimik (Lächeln)
  - Mund bei stummen Figuren
  - Zahlen und Schrift
  - Handlung (wer hält was)
- **Kling-eigene harte Schnitte** per Szenenwert-Suche finden: `ffmpeg -i clip.mp4 -vf "select='gte(scene,0)',metadata=print" -f null -`, Werte über ca. 0,12 sind Schnitte. Einen solchen Schnitt genau auf den Anfang der passenden Songzeile legen oder nur den Teil davor nutzen.
- Bei Detailfragen einen Ausschnitt im Halbsekundentakt vergrößern, z. B. wandert der Schallkopf oder öffnet sich der Mund.

---

## 9. Schnitt und Untertitel

### Schnittplan (verhindert Zeitlupe und Standbilder)
- Pro Szene das nutzbare Material ausrechnen: Clip-Länge (oder nur der saubere Teil) × 1,08.
- Ist das Zeitfenster länger, **die Szenengrenze verschieben**: Die Nachbarszene mit Reserve beginnt früher oder endet später, höchstens ca. 0,4 s. Das fällt beim Zuschauen nicht auf. Nie einfrieren, nie über 8 % dehnen, keine Rückläufe, keine digitalen Zooms.
- **Überblendungen (0,3 bis 0,5 s)** dort, wo zwei ähnliche Einstellungen hart aufeinander folgen, z. B. zweimal dieselbe Küche. Sonst harte Schnitte auf den Zeilenwechsel, wie in einem Musikvideo.
- Jedes Segment: `fps=25, scale=1080:1920:force_original_aspect_ratio=increase, crop=1080:1920`, dann exakt auf die Bildanzahl schneiden: `trim=end_frame=N` mit N = round(Ende × 25) − round(Start × 25). So summiert sich nichts auf.
- Segmente per concat-Demuxer verbinden, Überblendungspaare vorher per `xfade` zusammenbauen.

### Untertitel (Singing-Stil)
- **Eine Einblendung pro gesungener Zeile.** Lange Zeilen werden am Satzzeichen geteilt, maximal 8 Wörter pro Einblendung.
- Einzeilig bis ca. 26 Zeichen, sonst zweizeilig, bevorzugt nach einem Satzzeichen umbrechen.
- Zeiten aus den STT-Wortzeiten. Anzeige mit **Ziffern** (95, 127 zu 79, Q10, Dr.), obwohl die Lyrics ausgeschrieben sind.
- **Stil:** Arial Bold ca. 66 px, weiß mit ca. 7 px schwarzer Kontur, Unterkante ca. 560 px über dem Bildrand, also im unteren Bereich, aber noch in der 4:5-Zone.
- **Nach Pixelbreite umbrechen** (max. 920 px), damit links und rechts nie etwas abgeschnitten wird.
- Fehlt ffmpeg `libass`: Jede Einblendung mit Pillow als transparentes PNG rendern (`stroke_width`, `anchor="ma"`), per concat-Liste mit Dauern zu einer qtrle-Overlay-Spur (MOV mit Alpha) bauen und darüberlegen.
- Endencode: Bildspur + Untertitel-Overlay + Song, libx264 CRF 18, AAC 192k, `-movflags +faststart`, Länge = Songlänge. **Nie parallel zu anderen ffmpeg-Prozessen encodieren.**

---

## 10. Endkontrolle (vor dem Versand an den Auftraggeber)
1. `ffmpeg -v error -i final.mp4 -f null -` meldet nichts (Datei intakt).
2. **Standbild-Suche:** `ffmpeg -i final.mp4 -vf "freezedetect=n=0.001:d=0.8" -an -f null -`. Jeder Treffer außer bewusst ruhigen Produktaufnahmen ist ein Fehler.
3. **Sprung-Suche:** Szenenwechsel (Szenenwert über 0,3), die nicht auf einer Szenengrenze liegen, einzeln ansehen.
4. **Sichtprüfung aller Szenen:** je 6 Standbilder aus dem fertigen Video als Bogen, mit Untertiteln. Dabei alles aus Abschnitt 0 abhaken: Mimik, Schrift, 4:5, Handlung.
5. **Tempo-Vergleich** bei Neuschnitten: Die Bewegung pro Szene gegen die vorige Fassung messen. Unveränderte Szenen müssen bildgleich sein.
6. **Ehrlich berichten:** Was du geprüft hast, was nicht (z. B. „nicht komplett in Echtzeit angesehen“) und welche bekannten Kleinigkeiten bewusst geblieben sind.

---

## 11. Korrekturrunden
- **Immer auf der besten Fassung aufbauen**, meist der ersten, und nur die genannten Punkte ändern. Nicht nebenbei Dinge „verbessern“, die der Auftraggeber gut fand.
- Die alte Fassung immer als Vergleichsdatei **direkt neben** die neue legen.
- Jede Korrektur ist eine saubere Neuerzeugung, siehe Abschnitt 0.
- Vorher die **Kosten nennen** (Bilder × 18 bzw. 10, Clips × 70 bzw. 140) und das Guthaben prüfen.

---

## 12. Modelle bei Kie.ai (Stand 30.09.2026)

| Modell | Preis | Stärken | Schwächen | Note |
|---|---|---|---|---|
| **Kling 3.0 std 720p** | 70 / 5 s, 140 / 10 s | Pixar-Look, Konsistenz, Anatomie, flüssig | eigene Schnitte, murmelnde Münder, Display-Zahlen kippen nach ca. 3 s | **9/10 (Standard)** |
| Kling 3.0 pro 1080p | 90 / 5 s | schärfer | Zahlen nicht besser | 8/10 |
| Veo 3.1 Fast / Lite 720p | 60 / 30 pro 8 s | günstig, gute Physik | erzeugt immer Ton (bricht ab, wenn der nicht geht), blockt Figuren als „prominente Person“, Handlungen nicht zuverlässig, Look weicht ab | 6/10 |
| Hailuo 2.3 768p | 30 / 6 s | günstig, flüssig | Zahlen und Figuren instabil | 5/10 |
| Seedance 1.5 Pro 720p | 17,5 / 5 s | sehr günstig, `fixed_lens` | Zahlen instabil, Mimik übertrieben | 5/10 |
| Nano Banana Pro (Bild) | 18 | beste Figurenkonsistenz | Tippfehler in Schrift, erfindet englische Beschriftungen, NSFW-Filter streng | 9/10 für Szenen |
| GPT Image 2 (Bild) | 10 | **fehlerfreier Text** auf Packungen | Figurenkonsistenz ungetestet | 9/10 für Produkt-/Textbilder |

Neue Modelle (Seedance 2/2.5, Wan 3.0, MiniMax H3, PixVerse v6, Grok Imagine) erst an **einer** Testszene gegen Kling vergleichen, bevor du sie verwendest.

---

## 13. Technische Stolperfallen
- **Kie-Downloads** brechen manchmal ab („IncompleteRead“, Timeouts). Mit `curl --retry 5 --retry-all-errors` laden. Ergebnisse lassen sich jederzeit über die Task-ID neu abrufen (`jobs/recordInfo`). Dabei nichts neu starten, das kostet doppelt.
- „Internal Error“ bei Kie ist meist vorübergehend: 10 s warten, dann erneut versuchen, höchstens 3 bis 4 Mal.
- **zsh** teilt `$VAR` nicht in Wörter. Listen per `xargs` oder `${=VAR}` übergeben. `pgrep -f "<text>"` findet sich selbst, wenn der Text in der eigenen Befehlszeile steht.
- Veo hat einen eigenen Endpunkt (`/api/v1/veo/generate`, `veo/record-info`, Modelle `veo3_fast`, `veo3_lite`, `veo3`).
- Beim Filtern von Audio (Kompressor, dynaudnorm, Rauschfilter) wird die Stimme hörbar schlechter. Singing-Songs von Suno unverändert lassen und nur auf Schlag schneiden.

---

## 14. Ausgabe und Ablage
- Datei nach dem Naming des Auftraggebers benennen, z. B. `P7 - CAD80 - VIDEO80 - SUNO - 9-16.mp4`, und in den vorgegebenen Batch-Ordner legen. Vorhandene Dateien im Ordner nicht anfassen.
- Arbeitsdateien getrennt halten: Song, Timing, Szenenplan, Figuren, Startbilder, Clips, Schnitt. Verworfenes nicht löschen, sondern verschieben.
- **Kein Upload zu Meta oder anderswo ohne ausdrückliche Freigabe.** Anzeigennamen und Einstellungen vorher abstimmen.
- Erkenntnisse aus jeder Produktion in die eigene Wissensablage schreiben, damit die nächste Ad besser wird.
