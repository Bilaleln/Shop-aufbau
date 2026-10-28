---
name: yapping-ad
description: Erstellt realistische Yapping Ads (AI UGC), in denen eine KI-Person in die Kamera erzählt. Bei Yapping Ad, AI UGC, UGC Ad, Talking Head Ad oder organisches Video zur Ad machen.
---

# Yapping Ad (AI UGC)

Dieser Skill macht aus einem Video, das organisch schon viele Aufrufe hat, eine **Yapping Ad**: Eine realistische KI-Person erzählt im Hochformat direkt in die Kamera, als wäre es ein normales TikTok. Das Produkt kommt so beiläufig in die Geschichte, dass das Video nicht nach Werbung aussieht. Das Ergebnis ist ein 9:16-Video mit 1,5 bis 3 Minuten Länge, gebaut aus mehreren KI-Segmenten von bis zu 15 s plus B-Roll.

**Herkunft der Regeln:** Grundlage ist das Modul „13. AI ADS / Make AI UGC“ (Zakaria Airakaz, ECOM Masterclass, Okt./Nov. 2026). Die Beispiel-Ad dort: PCOS-Haarausfall, Produkt „Root Restore“, 2:34 Minuten, Vorlage ein organisches TikTok mit 4,7 Mio. Aufrufen. Anders als bei der Singing Ad stammen diese Regeln **noch nicht aus einer eigenen Produktion**. Regeln mit dem Vermerk **(Annahme)** sind übertragen oder geschätzt und müssen in der ersten Produktion bestätigt werden. Nach jeder Produktion Abschnitt 15 ergänzen.

---

## 0. Grundhaltung (die wichtigsten Regeln zuerst)

1. **Das Script entscheidet, nicht das Tool.** Laut Kurs ist das größte Problem nicht der Realismus, sondern ein Script, das unterhält, sich echt anfühlt und trotzdem verkauft. Die meiste Zeit gehört in das Script.
2. **Keine Ad-Schablone.** Nicht in Hook → Problem → Agitation → Lösung → Angebot → CTA umbauen, denn genau diese Struktur lässt Ads nach Ads aussehen. Den Grund finden, warum das Original geschaut wird (Unterhaltung, Emotion, Neugier, Persönlichkeit, Wissen), ihn schützen und das Produkt hineinweben.
3. **Dem Prompt nie blind vertrauen.** Es gibt keinen Universal-Prompt. Jedes Ergebnis von Claude oder Gemini lesen, laut im Kopf sprechen und gezielt nachsteuern: Was klingt nicht wie ein Mensch? Was ist überflüssig, was zu kompliziert?
4. **Realismus kommt aus Referenzen.** Echtes Setup-Video als Referenz plus ein sauberes Gesichtsbild. Avatare nicht frei aus dem Nichts erfinden lassen.
5. **Erst ein Testsegment, dann alle.** Das erste Segment so lange verbessern (Emotion, Hände, Aussprache, Lipsync, Licht), bis es sitzt. Erst danach die übrigen Segmente erzeugen.
6. **Feedback immer an einer konkreten Stelle festmachen:** „Bei ‚perfekt‘ zu ruhig, mehr Erleichterung, Hände öffnen.“ Nicht „mach es besser“.
7. **Scriptwörter nie ändern** beim Zerlegen in Segmente. Der Text im SAYS-Feld ist exakt der freigegebene Text.
8. **Alles Geschriebene und Gesprochene in der Sprache der Ad.** Bei einer deutschen Ad ist das Script deutsch, auch wenn die Vorlage englisch ist. Packung, Zettel und Screens im Bild sind deutsch oder ohne Schrift.
9. **4:5-Sicherheitszone.** Gesicht, Hände mit Produkt und Untertitel liegen in den mittleren 70 % der Bildhöhe (bei 1080×1920 die Zeilen 285 bis 1635).
10. **Vor jedem Kostenschritt die Freigabe holen:** Script, Avatar-Gesicht, Referenzclip, Testsegment, dann Produktion. Nichts hochladen oder veröffentlichen ohne ausdrückliche Freigabe.
11. **Recht und Plattform beachten** (Abschnitt 12): keine fremden Gesichter oder Stimmen ohne Einwilligung, nur belegte Aussagen, nur echte Vorher-Nachher-Bilder, KI-Kennzeichnung.

---

## 1. Voraussetzungen

- **Video-Plattform mit Referenz-Video-Modus und Face-Swap.** Im Kurs ist das **MaxFusion** (Switch Actor, Wan 3.0 Prime, Seedance 2.5, ElevenLabs-Anbindung). Laut Kurs gehen auch Kie.ai oder Higgsfield, weil dort dieselben Modelle laufen: die günstigste Plattform nehmen. **(Annahme)** Ob Kie.ai einen „Switch Actor“-Ersatz und Wan 3.0 Prime mit Video-Referenz anbietet, vor der ersten Produktion prüfen. Bei Higgsfield ist `motion_control` (Kling-Recast mit einer Figur) der naheliegende Kandidat. Keine Endpunkte raten, sondern die Doku lesen und eine Testszene fahren.
- **Gemini** (kann Videos mit Ton analysieren), **Claude-Projekt** mit allen Marken-Unterlagen (Produkt, Mechanismus, Zutaten, Belege, Avatar-Recherche).
- **ElevenLabs** (optional) für Stimme oder Voice-Switch, siehe Abschnitt 9.
- **Diktier-Tool** (im Kurs Whisper Flow), um Claude per Sprache Feedback zum Script zu geben. Spart Zeit und führt zu natürlicheren Anweisungen.
- **ffmpeg** für Zuschnitt (Referenzclip auf 30 s bzw. 15 s), Schnitt und Endkontrolle.
- Vom Auftraggeber: **Produkt-Fakten mit Belegen**, ein **sauberes Produktfoto** (Bild von der Produktseite reicht), **Aussprache** des Markennamens, **Avatar-Beschreibung** (Alter, Look, Situation), **Dinge, die nicht gesagt werden dürfen**, **Naming** bzw. Ablageort.

### Budget (MaxFusion-Credits laut Kurs)
| Posten | Preis |
|---|---|
| Switch Actor Pro (Referenzclip, bis 30 s) | 250 |
| Segment Wan 3.0 Prime, 15 s | 135 |
| Segment Seedance 2.5, 15 s | 465 |
| B-Roll Seedance 2.5 (Draft 480p / 1080p) | laut Screenshot um 237 für 1080p, vorher prüfen |

**Faustregel (Annahme):** Eine 2,5-Minuten-Ad hat ca. 11 bis 13 Segmente. Mit Wan 3.0 Prime sind das ca. 1.500 bis 1.750 Credits im ersten Durchgang plus 250 für den Referenzclip. Weil jedes Segment oft zwei bis drei Versuche braucht, mit **50 bis 100 % Puffer** rechnen, also ca. 2.500 bis 3.500 Credits inklusive B-Roll. Mit Seedance 2.5 durchgehend etwa das Dreifache. Nach der ersten Produktion durch echte Werte ersetzen.

---

## 2. Ablauf im Überblick

```
Referenz finden (TikTok organisch oder Winner-Ad) → Daten prüfen → Video laden
  → Gemini-Analyse → Claude: Script adaptieren → eigene Überarbeitung (mehrere Runden) → [Freigabe Script]
  → Avatar-Gesicht → [Freigabe] → Setup-Video auf < 30 s schneiden → Switch Actor → bestes Startbild wählen
  → Referenzclip auf 15 s schneiden → [Freigabe Referenzclip]
  → Segment-Prompts (Abschnitt 7) → 1 Testsegment, so lange verbessern bis es sitzt → [Freigabe + Hochrechnung]
  → alle Segmente → Produkt-Halteszene → B-Roll → Prüfung/Korrektur
  → Schnitt + Untertitel + B-Roll + Vorher/Nachher → Endkontrolle → [Abnahme] → Naming + Ablage
```

---

## 3. Referenz finden und auswählen

Es gibt zwei Quellen:

1. **Organisches Video aus der Nische** (TikTok-Suche, z. B. „PCOS hair loss“). Das schaut der Avatar freiwillig. Hook und Story funktionieren schon für genau diese Zielgruppe. **Hier muss man nichts an den Avatar anpassen, nur das Produkt sauber einführen.**
2. **Winner-Ad einer anderen Marke** (Trendtrack für Marken mit gut laufenden Yapping Ads, dann den Markennamen in einem Ad-Spy-Tool gegenprüfen). Kommt sie aus einer anderen Nische, muss man **anpassen**: Hook-Typ, Neugier-Element und Ablauf verstehen und auf Avatar, Bewusstseinsstufe, Emotion und Glaubwürdigkeit der eigenen Nische übertragen.

**Validieren:** Eine Referenz braucht Daten, die zeigen, dass sie gewinnt: Aufrufe, Likes, Kommentare, Shares, Laufzeit der Ad. Das Kursbeispiel hatte organisch 4,7 Mio. Aufrufe.

**Verstehen, warum es funktioniert:** Meist liegt es an der Person, nicht am Inhalt. Wie sie spricht, sich ausdrückt, Gefühle zeigt und Dinge formuliert, macht den Winner. Im Beispiel: Sie „ventet“ einfach. Man spürt keinen Verkauf, nur jemanden wie die Zuschauerin, die von ihrer Erfahrung erzählt. Diese Delivery wird nachgebaut, das Script nicht kopiert.

Das Video lokal speichern. Es dient nur als Analyse- und Setup-Referenz und kommt **nie** in die fertige Ad (Abschnitt 12).

---

## 4. Gemini-Analyse

Das Video mit Ton in Gemini laden und um eine vollständige, wörtliche Analyse bitten. Ergebnis als `gemini_analyse.md` speichern. Es geht später an Claude für das Script und für die Segment-Prompts, damit dort Gestik, Mimik, Licht und Sprechweise des Originals nachgebaut werden.

**Prompt-Kern (sinngemäß aus dem Kursmaterial):** „Du bist Direct-Response-Video-Analyst. Zerlege dieses organische Video so genau, dass ein Team Gefühl, Struktur und Wirkung nachbauen kann, ohne das Original je zu sehen. Wörtlich und konkret, mit Zeitstempeln (mm:ss). Wenn etwas unklar ist, schreib ‚unklar‘, nicht raten.“ Dann diese Abschnitte in dieser Reihenfolge verlangen:

0. **Vollständiges Transkript zuerst**, Wort für Wort mit Füllwörtern, Wiederholungen, Versprechern und Selbstkorrekturen. Zeile pro natürlicher Pause mit Zeitstempel. Sprecher-Labels, Delivery in Klammern ([pause], [laughs], [sighs], [emphasis on "…"], [voice breaks], [speeds up]), unklare Wörter als [inaudible]. Bei anderen Sprachen erst das Original, dann die Übersetzung. Danach eine **saubere VO-Fassung** und alle **Bildschirmtexte** getrennt mit Zeitstempel.
1. **Überblick:** Länge, Zusammenfassung, worum es emotional wirklich geht, warum es organisch funktioniert.
2. **Sprecher:** Anzahl, Alter, Look, Vibe, Kleidung, Haare, Make-up, Schmuck, Körpersprache, Gesten, Blickkontakt, Mimikverlauf mit Zeitstempeln, Energie und ihre Wechsel, Rolle gegenüber dem Zuschauer.
3. **Setting:** Ort, alles im Hintergrund, inszeniert oder bewohnt, Ortswechsel.
4. **Licht:** Art, Richtung, Helligkeit, Farbtemperatur, Schatten, Stimmung.
5. **Kamera:** Handy oder Profi, Selfie, Stativ oder angelehnt, Bildausschnitt, Winkel, Bewegung, Shot-Liste mit jedem Schnitt.
6. **Visuals und Schnitt:** B-Roll, Produkt, Screenshots, Vorher/Nachher, Untertitel-Stil, Emojis, Zooms, Schnitttempo, Rohheit.
7. **Audio und Stimme:** Ton, Tempo, Pausen, Betonungen, Lautstärke, Stimmqualität, Musik, Geräusche.
8. **Sprache:** Dialekt, Slang, Füllwörter, Satzstil, Perspektive, stärkste Sätze, Schmerzpunkte, Fragen an den Zuschauer, gescriptet oder spontan.
9. **Struktur:** Hook (0 bis 3 s: Worte, Bild, warum er stoppt), Hook-Typ, Beats mit Zeitstempeln, emotionaler Bogen, Ende und CTA.
10. **Psychologie:** Zielperson, Problem oder Wunsch, Vertrauens-Elemente, Einwände, was es „nicht wie Werbung“ wirken lässt.
11. **Ad-Umbau:** was bleiben muss, was als Paid Ad schadet, 3 bis 5 Hook-Varianten im selben Gefühl, wo ein Produkt natürlich hineinpasst.

„Nichts kürzen oder auslassen, vor allem nicht das Transkript.“

---

## 5. Script adaptieren (der wichtigste Schritt)

### Claude-Prompt (sinngemäß aus dem Kursmaterial)
Im Claude-Projekt der Marke: „Du bist Weltklasse-Ad-Stratege und machst aus organischen Videos, die schon Aufrufe haben, verkaufende Ads, OHNE sie in Ads zu verwandeln. Baue es NICHT in Hook → Problem → Agitation → Lösung → Angebot → CTA um. Finde den Grund, warum das Video funktioniert, schütze ihn und schiebe mein Produkt so sanft hinein, dass es sich wie derselbe organische Inhalt anfühlt. Das Produkt ist Teil des Werts, keine Unterbrechung.“

Dazu: die komplette Gemini-Analyse und das Produkt-Briefing (Marke, Produkt, Darreichung, Zutaten und Dosis, Mechanismus in einfachen Worten, Avatar mit Alter, Situation, Kernschmerz, Bisher-versucht und heimlichem Wunsch, Nutzen, Belege, Angebot, CTA, **Verbotene Aussagen**).

**Schritt 1, Diagnose (A bis F):**
- A) **View-Driver:** Bildung, Unterhaltung, Neugier, Emotion oder Persönlichkeit, primär und sekundär, und wie genau.
- B) **Wie sie spricht:** Rhythmus, Satzlänge, Slang, Füllwörter, Reaktionen, typische Wendungen, Energieverlauf.
- C) **Wert:** welche Info, warum überraschend, wie einfach erklärt.
- D) **Unterhaltung „neben der Story“:** Abschweifungen, Seitenkommentare, Witze, Zufallsdetails, also alles, was eine normale Ad streichen würde, weshalb die Leute aber schauen.
- E) **Retention:** offene Schleifen, Überraschungen, Tempo, Enthüllungen, wo die Aufmerksamkeit steigt oder fällt.
- F) **Natürliche Produkt-Öffnungen:** wo schon ein Problem, ein Tipp, ein „was mir geholfen hat“ oder eine Frage steht. Von natürlich bis weniger natürlich ranken.

**Schritt 2, Produkt einweben:**
- Struktur, Ablauf und View-Driver bleiben. **Ziel: 70 bis 80 % wie das Original.**
- Ihre Stimme bleibt: Rhythmus, Slang, Füllwörter, Abschweifungen, Reaktionen.
- Produkt an der natürlichsten Öffnung aus 1F, z. B. „das hat wirklich geholfen“, „das Ding, das ich dann angefangen habe“.
- Das Produkt **löst oder ergänzt etwas, das schon im Video ist**, keine neue Verkaufsstrecke.
- Wirkung im selben Erklärstil wie der Rest des Videos. Belege als persönliche Erfahrung oder Nebenbemerkung, nie als Feature-Liste.
- CTA locker, so wie sie es sagen würde.
- Bildend bleibt bildend, unterhaltsam bleibt unterhaltsam, emotional bleibt emotional.
- Keine Marketing-Floskeln („Game-Changer“, „revolutionär“, „sag Tschüss zu“).

**Ausgabe in dieser Reihenfolge:** 1. Diagnose A bis F, 2. Integrationsplan, 3. komplettes Ad-Script mit Delivery-Cues ([pause], [laughs], [softer], [emphasis on "…"]) und Zeitstempeln, neue Zeilen mit ★ markiert, 4. saubere VO-Fassung, 5. Bildschirmtexte, 6. B-Roll- und Bildnotizen inklusive des Moments, in dem das Produkt im Bild auftaucht, 7. drei alternative Integrationen zum Testen.

### Die eigene Überarbeitung (hier entsteht die Qualität)
Im Kurs war das erste Claude-Script schlecht: Es hatte die unterhaltsamen Teile entfernt und war zu direkt. Erst mehrere Runden mit gezieltem Feedback ergaben die Endfassung. Diese Lehren gelten allgemein:

1. **Bei einer organischen Vorlage mit Millionen Aufrufen das Script so lassen, wie es ist.** Nur die Produkt-Einführung neu bauen. Die „überflüssigen“ Details (Eizellen zählen, Ärzte, Rückschläge) sind genau das, was unterhält.
2. **Produkt über ein Element einführen, das schon in der Story steckt.** Im Beispiel macht der Freund ein Foto von ihrem Kopf. Daraus wird: Er sieht, wie fertig sie ist, recherchiert selbst und findet die Marke. So kommt das Produkt nicht aus dem Nichts.
3. **Wie ein echter Mensch klingen.** Eine Frau, die vom Freund erzählt, sagt eher „er ist echt der süßeste Freund überhaupt“. Solche Einschübe machen es echt. Sie dürfen später wiederkehren („bester Freund ever“).
4. **Skepsis zeigen.** „Ugh, nicht noch eins“, weil sie schon viel probiert hat. Das nimmt dem Zuschauer den Einwand ab.
5. **Spezifität betonen:** nicht für Haarausfall allgemein, sondern speziell für PCOS-Haarausfall. Das schafft Glaubwürdigkeit.
6. **Mechanismus einfach halten (System-1-Denken).** Ein kurzer Kreislauf, der erklärt, warum alles andere nicht geholfen hat, z. B. Insulin → Androgene → Entzündung → Haarfollikel. Keine Fachsprache. Wer mehr wissen will, schaut auf der Produktseite.
7. **Was die Avatar-Person nicht sein kann, rausnehmen.** Die Original-Creatorin ist bekannt, deshalb „kommentieren Leute im Internet“. Eine unbekannte KI-Person sagt stattdessen „bis Leute mich gefragt haben, ob ich schwanger bin“. Sonst entstehen unbewusste Fragen („Ist sie berühmt?“).
8. **Namen der Original-Creatorin ersetzen** (im Original spricht sie von sich in der dritten Person).
9. **Kürzen, aber an den richtigen Stellen.** Eine 5-Minuten-Fassung wurde auf ca. 3 Minuten gekürzt, das fertige Beispiel lief 2:34. Langatmige Teile in der Produkt-Erklärung streichen, die unterhaltsame Vorgeschichte bleibt.
10. **Sätze prüfen:** Würde ein normaler Mensch das so sagen? Gehört das in die Geschichte? Ist das zu kompliziert?
11. **Feedback per Diktat** geben (Whisper Flow o. Ä.). Erklären, wohin es gehen soll, statt Text selbst zu tippen.
12. **Muster sammeln:** Eigene und fremde Winner-Ads regelmäßig zerlegen. Wie wird das Produkt eingeführt, wie wird übergeleitet, wie wird erklärt? Nur so erkennt man ein gutes Script.

### Long-Form-Story (Yapping Style) laut Story & Drama
Diese Ergänzung stammt aus „Elite Copywriting / Part 5 – Story & Drama“, Lektionen 12 und 13. Sie hilft, wenn kein organisches Video als Vorlage da ist und das Script neu geschrieben wird. Die vollständigen Struktur- und Script-Regeln stehen im Skill `ugc-script`.

- **Abgrenzung:** Eine UGC-VSL macht die Sprecherin zur Autorität (Ursache, Mechanismus, Abschluss mit Dringlichkeit). Beim Yapping erzählt eine ganz normale Person wie die Zuschauerin, ohne schweres Direct-Response-Marketing. Den Mechanismus deshalb nur andeuten: „Da ist X und Y drin, keine Ahnung, wie genau das wirkt, aber …“ Wichtiger ist, **was** es für sie getan hat, nicht **wie**. Laut Zakaria wirkt das Format besonders gut bei Frauen.
- **Beats für 1 Minute:**

  | Beat | Zeit |
  |---|---|
  | Hook mitten in die Szene | 5 s |
  | Vorgeschichte | 15 s |
  | Tiefpunkt (ein Moment, keine Entscheidung) | 10 s |
  | Entdeckung mit Skepsis | 8 s |
  | Verlauf („Woche 1 nichts, fast aufgehört …“) | 12 s |
  | Jetzt plus sanfter CTA | 10 s |

  Bei 2 Minuten dehnst du jeden Beat, der Hook bekommt etwa 8 s.
- **Hook:** keine Vorstellung („Hi Leute, ich bin …“ ist verboten). „Okay, ich muss euch erzählen, was passiert ist, ich bin echt geschockt“ ist laut Zakaria zu schwach. Besser ist eine intensive Szene aus dem Alltag, z. B. „Mein Mann dachte, ich betrüge ihn, weil ich jede Nacht um 3 Uhr aufgestanden bin.“ Stichworte wie „fast abgezockt“, „fast erwischt“ oder „er dachte, ich betrüge ihn“ ziehen, solange die Story sie einlöst.
- **Drei Stile:** **Story** („Lass mich erzählen, was passiert ist“, für Verwandlungen), **Geständnis** („Ich wollte das eigentlich nicht posten …“, für peinliche Themen wie Wechseljahre, Sex, Gewicht), **Rant** („Mich regt so auf, dass keiner darüber redet“, für den Angle „von Ärzten abgespeist“).
- **Sprechweise im Prompt mitgeben:** Unsicherheit („Woche drei, vielleicht vier“), echte Gefühle („Ich hätte fast geweint“), schneller bei Aufregung, langsamer in emotionalen Momenten, Abschweifungen („Ich weiß, das klingt verrückt, aber …“).
- **Die Delivery entscheidet:** Eine starke Performerin macht aus einem mittelmäßigen Script einen Winner. Bei KI deshalb in jedem Segment-Prompt Intensität und Gestik festlegen (Hände, Pausen, Blick) und in Abschnitt 8 konsequent nachsteuern. Das KI-Gesicht passt zum Avatar: Alter, Look und im Kopf der Zuschauerin auch die Herkunft.
- **Beispiel Happy Mammoth (8,3 Mio. Aufrufe, 56 s):** „Ich bin in meinen 40ern, und Ende 30 fingen diese komischen Gesundheitsprobleme an“, dann Symptome, dann „alles voller Mist“ (sie hat für die Zuschauerin gefiltert), dann „über ein Online-Quiz gestolpert … warum nicht?“, dann „besser als in den letzten zehn Jahren“, dann „Was hast du zu verlieren?“. Der CTA verkauft **nicht das Produkt, sondern den nächsten Schritt** (das Quiz). Das ist eine Option, wenn die Seite danach den Verkauf übernimmt.
- **Ehrlicher Hinweis:** Zakaria empfiehlt, Yapping-Ads über die Seite der Creatorin oder eine Drittseite laufen zu lassen. Mit einer KI-Person ist das eine Täuschung über die Person und kommt nicht in Frage (Abschnitt 12). Er selbst setzt für seine Marken laut Discord keine erfundenen KI-Creatorinnen ein (Stichworte FTC und Exit), sondern KI nur für B-Roll und Animation.

### Deutsche Ads (Annahme)
- Vorlage englisch, Ad deutsch: Script nicht wörtlich übersetzen, sondern wie eine deutsche Creatorin sprechen lassen, mit deutschen Füllwörtern („also“, „ehrlich gesagt“, „keine Ahnung“) und Alltagssprache.
- Zahlen und Abkürzungen so schreiben, wie sie gesprochen werden sollen. Für Fremd- und Markennamen eine PRONUNCIATION-Zeile vorbereiten (Abschnitt 7).
- Nur belegte Aussagen und zulässige Health Claims (Abschnitt 12).

---

## 6. Avatar und Referenzclip

### Avatar-Gesicht
- Wer ist der Avatar? Auf Basis von Recherche (andere Marken, organische TikToks der Nische) Alter, Look und Typ festlegen, z. B. „Frau, 30+, natürlich, nahbar“.
- **Ein echt wirkendes Gesicht ist Pflicht.** Je realer, desto besser das Ergebnis. Im Kurs wird dafür ein Pinterest-Foto genommen. Das ist das Gesicht einer echten fremden Person und deshalb rechtlich riskant (Abschnitt 12). **Besser:** ein fotorealistisches Gesicht mit einem Bildmodell erzeugen (Pinterest nur als Look-Vorlage) oder ein lizenziertes bzw. eingewilligtes Modelfoto verwenden.
- **Bild auf das Gesicht zuschneiden.** Bei einem Ganzkörperbild übernimmt das Tool auch Kleidung und Körper. Mit reinem Gesicht tauscht es nur das Gesicht und behält Kleidung, Raum und Bewegung des Videos.
- Frontal, gut ausgeleuchtet, Kopf gerade zur Kamera.

### Setup-Video
- Das Video mit dem gewünschten Setup: Hintergrund, Licht, Kleidung, Sitzposition und Art zu sprechen. Oft ist es dieselbe Vorlage wie für das Script, es kann aber auch ein anderes Video sein, nur weil Setup und Delivery gefallen. Was darin gesagt wird, ist egal.
- Person schaut in die Kamera, Kopf und Oberkörper sind vollständig im Bild (Hinweis von MaxFusion).
- Auf **unter 30 s** schneiden: `ffmpeg -ss 0 -t 29 -i vorlage.mp4 -c copy setup_29s.mp4` (bei ungenauem Schnitt neu encodieren).

### Switch Actor (MaxFusion → Switch Actor → Pro, 250 Credits)
- Setup-Video links, Gesicht rechts. Anweisung: „Switch only the face. Keep the same [Oberteil], [Raum], lighting and camera framing.“
- Das Tool zeigt **drei Startbilder**. Das glaubwürdigste wählen und dabei Haaransatz, Augen, Haut und den Übergang von Gesicht zu Körper prüfen. Bei Zweifel „Re-generate“.
- „Preserve scene“ und „Choose voice“ bewusst setzen (Stimme siehe Abschnitt 9).
- Ergebnis prüfen: Gesicht stabil über die ganze Länge? Keine Verformung bei Kopfdrehung und Handbewegung?
- Dann auf **15 s** schneiden, denn die meisten Modelle nehmen höchstens 15 s Video-Referenz. Das ist der **Referenzclip `@Video1`**. Er hat das neue Gesicht plus Setup, Licht, Kamera, Gestik und Sprechweise des Originals. Er dient nur als Kontinuitäts-Referenz und kommt nicht in die Ad. Ausnahme: Er sagt schon den richtigen Anfang des Scripts, dann darf er Segment 1 sein.

---

## 7. Segment-Prompts

Claude bekommt das **freigegebene Script**, die **Gemini-Analyse** und den Auftrag, das Script in Segmente zu zerlegen, die den Referenzclip nahtlos fortsetzen. Im Kurs ist das der Skill „ugc-extension-segments“. Die Regeln daraus:

- **Identität kommt aus `@Video1`** (dem neuen Gesicht). Beschreibt die Gemini-Analyse das Gesicht der Original-Creatorin, das ignorieren. Haare und Kleidung kommen aus der Analyse bzw. aus `@Video1`.
- **Nur an Satzenden trennen**, nie einen Satz auf zwei Segmente verteilen.
- **Länge:** Englisch ca. **3,5 Wörter pro Sekunde**, maximal ca. 15 s bzw. ca. 50 Wörter. Output-Länge = Wortzahl ÷ 3,5, gerundet. **Deutsch (Annahme):** Startwert 3,0 Wörter pro Sekunde (ca. 45 Wörter für 15 s), im Testsegment messen und den Wert anpassen.
- **Scriptwörter nie ändern, ergänzen oder streichen.**
- **PRONUNCIATION-Zeile** nur, wenn das Segment ein Akronym, einen Markennamen oder ein Fachwort enthält, z. B. `"PCOS" = "P-C-O-S"`, `"Root Restore" = "ROOT re-STORE"`.
- **Stimme:** keine Anweisung zum Klonen der Stimme aus `@Video1`, außer es ist nachweislich die eigene oder eine lizenzierte Stimme.
- Ist ein einzelner Satz zu lang für ein Segment, oben in einer Zeile markieren, ohne ihn zu ändern.
- Weicht die Performance vom Standard ab (geht, sitzt im Auto, hält das Produkt, männlicher Sprecher), nur die Punkte 2 und 3 der Vorlage anpassen.

### Vorlage (eine pro Segment, ein Codeblock je Segment)
```
GOAL: Continue the previous clip seamlessly — same person, same look, no cut. Output length: ~[N] seconds.

INPUT:
- @Video1 = the reference clip (drives the motion, timing and scene).

WHAT TO DO:
1. KEEP THE SAME: same face, same hair ([Haarbeschreibung aus der Gemini-Analyse]), same clothes, same body as the previous clip. Do not restyle the hair or change the outfit.
2. SCENE + MOTION: use @Video1 for the setting, camera framing, movements, hand gestures, pacing and energy. Continue straight on from the previous clip — no cut, no scene change, same position.
3. PERFORMANCE: she talks straight to camera, head and upper body visible, facing forward, casual UGC energy with natural hand gestures that match the words.
4. SCRIPT: she says ONLY the line below, lip-synced to these exact words. Ignore @Video1's original speech.
5. NO SUBTITLES: do not generate any subtitles, captions or on-screen text of any kind.

PRONUNCIATION: "[WORT]" = "[Lautschrift]".

SAYS: "[exakter Scripttext dieses Segments]"

Ambient room-tone only. No music. No on-screen text.
```
- **Gute Prompts haben Zeitmarken für Mimik und Gestik** aus der Gemini-Analyse, z. B. „0–5 s: Hände offen … 5–9 s: zählt an den Fingern ab, sagt ‚…‘ … 9–13 s: kleines stolzes Lächeln … Ende: Lächeln klingt ab, Hände tief. Audio: same voice as @Video1, RELIEVED and LIGHTER, NOT bubbly. Quiet closet room tone, NO music.“
- **Deutsche Ads (Annahme):** Den Prompt auf Englisch lassen (die Modelle folgen englischen Anweisungen zuverlässiger), SAYS auf Deutsch und Punkt 4 ergänzen: „She speaks German, natural native German pronunciation.“ Im Testsegment prüfen, ob Lipsync und Aussprache sitzen.

---

## 8. Segmente erzeugen

**Standardmodell laut Kurs: Wan 3.0 Prime** (MaxFusion → Videos → Wan 3.0 Prime → References), 9:16, 1080p, Dauer Auto, Referenzclip als Video 1. Etwa dreimal günstiger als Seedance 2.5 und bei gutem Prompt für den normalen Zuschauer realistisch genug.

**Seedance 2.5** ist sichtbar realistischer, vor allem bei der Stimme, kostet aber das Dreifache. Nur für Segmente nehmen, die mit Wan nachweislich nicht sauber werden, z. B. Produkt-Halteszenen oder emotionale Schlüsselstellen. Preis und Qualität vor jeder Produktion neu vergleichen, statt anzunehmen, dass ein Modell immer am besten ist.

### Vorgehen
1. **Segment 1 als Test erzeugen.** Ansehen und mit dem Referenzclip vergleichen.
2. **Konkret prüfen:** Emotion und Energie wie im Original? Handbewegungen vorhanden? Aussprache von Marken- und Fachwörtern? Lipsync? Licht und Hintergrund stabil? Gesicht, Haare und Kleidung gleich?
3. **Fehler an einer Stelle festmachen** und Claude den alten Prompt plus das Feedback geben. Beispiel aus dem Kurs: „Diese Version sagt ‚everything looked perfect‘ zu ruhig. Wie in der Referenz schnelle Energie: kurze Nicker, mehr sichtbare Handbewegung, dann offene Hände und ein erleichtertes Lächeln auf ‚perfect‘. Schreib nur diesen Segment-Prompt neu.“
4. **Erkenntnisse in die anderen Prompts übernehmen** („sorge dafür, dass das auch in den anderen Segment-Prompts steht“), damit derselbe Fehler nicht in jedem Segment neu auftaucht.
5. Erst wenn Segment 1 sitzt, die übrigen erzeugen. Jedes Segment wieder prüfen und bei Bedarf gezielt nachsteuern.
6. Jede Generierung mit Segmentnummer, Modell, Prompt-Version und Kosten loggen. Verworfene Clips in `verworfen/` verschieben, nie löschen.

### Produkt-Halteszene
- Für die Zeile, in der der Avatar das Produkt hält, als Video 1 **das zuletzt freigegebene Sprech-Segment** nehmen (nicht den ursprünglichen Referenzclip) und **das echte Produktfoto** als Bild anhängen. Ob das Bild „Image 1“ oder „Image 2“ heißt, steht in Claudes Prompt. Dem Label im Prompt folgen.
- Prompt-Cue aus dem Kurs: „Bei ‚also hat er es für mich bestellt‘ ruht die Flasche schon aufrecht in ihrer Hand. Sie hebt sie natürlich an, das Etikett zeigt zur Kamera. Keine einfliegende Flasche, kein wechselndes Etikett. Gleiche Person, gleicher Raum, gleiches Sprechtempo.“
- Ein normales Produktfoto von der Produktseite reicht. Etikett im Video Bild für Bild prüfen: Text richtig, nicht verzerrt, Packung wechselt nicht die Form. Kippt das Etikett, Seedance 2.5 für dieses Segment probieren.

### B-Roll
- **Für B-Roll ein echtes Aktionsvideo suchen**, das die Handlung schon zeigt (Pinterest, Stock, z. B. „Frau verliert Haare“). Nicht Claude eine Handlung frei erfinden lassen.
- Seedance 2.5: Aktionsvideo als Video 1, Avatar-Gesicht als Image 1. Anweisung: „Use Video 1 for the same [Handlung] and timing. Match the face and hair color to Image 1. Keep the rest of the action unchanged; no extra objects or text.“
- Hände, Haare, Gesicht und Bewegung prüfen. Stimmt die Handlung nicht, **erst ein besseres Aktionsvideo suchen**, bevor ein langer Prompt umgeschrieben wird.
- Rechte am Aktionsvideo beachten (Abschnitt 12). Am sichersten sind lizenziertes Stock-Material oder eigene Aufnahmen.

---

## 9. Stimme

- Seedance 2.5 bringt die beste Stimme mit. Bei Wan 3.0 Prime kann die Stimme schwächer sein.
- **Voice-Switch:** MaxFusion lässt sich mit ElevenLabs verbinden (API-Key). Dann im fertigen Clip „Switch voice“ wählen und eine ElevenLabs-Stimme einsetzen. Laut Kurs kostet der Wechsel bei einem fertigen Clip nichts.
- Der Kurs schlägt vor, die Stimme der Original-Creatorin aus dem TikTok bei ElevenLabs zu klonen. **Das nicht machen:** Es ist die Stimme einer echten Person ohne Einwilligung. Auch der Kurs-Skill selbst verbietet Voice-Cloning ohne eigene oder lizenzierte Stimme. Stattdessen eine passende Stimme aus der ElevenLabs-Bibliothek, eine per Voice Design erzeugte Stimme oder die Stimme einer Sprecherin mit Vertrag verwenden.
- Für alle Segmente **dieselbe** Stimme. Lautstärke und Klang zwischen den Segmenten angleichen. Die Stimme nicht mit Kompressor oder Rauschfilter bearbeiten, das macht sie hörbar schlechter (Erfahrung aus der Singing Ad).

---

## 10. Schnitt und Untertitel

Im Kurs übernimmt das der Editor. Die Regeln hier sind **(Annahme)**, übertragen aus der Singing Ad, und in der ersten Produktion zu bestätigen.

- **Segmente in Reihenfolge** zusammensetzen. Übergänge prüfen: Sitzt die Person am selben Platz, sind die Hände ähnlich? Kleine Sprünge sind bei UGC normal (Jump Cuts). Große Sprünge mit B-Roll überdecken.
- **B-Roll** an die passenden Stellen legen. Die Stimme läuft darunter weiter.
- **Vorher/Nachher** am Ende („Ich bin von dem hier zu dem hier gekommen“) nur mit echten, belegten Kundenbildern und deren Einwilligung (Abschnitt 12).
- **Untertitel im TikTok-Stil** wie im Original (die Gemini-Analyse beschreibt Schrift, Farbe und Position). Mit Ziffern, in der 4:5-Zone, nach Pixelbreite umbrechen, damit nichts abgeschnitten wird. Ohne `libass` wie bei der Singing Ad als Pillow-PNGs rendern und darüberlegen.
- **Hook-Text** in den ersten Sekunden wie im Original (im Beispiel „PCOS disaster: my hair is falling out“).
- Jedes Segment auf 1080×1920, 25 oder 30 fps vereinheitlichen. Endencode mit libx264 CRF 18, AAC 192k, `-movflags +faststart`.
- **Nie** Zeitlupe, eingefrorene Bilder oder digitale Zooms als Flicken. Ein fehlerhaftes Segment wird neu erzeugt.

---

## 11. Endkontrolle (vor dem Versand an den Auftraggeber)

1. `ffmpeg -v error -i final.mp4 -f null -` meldet nichts.
2. **Standbild-Suche:** `ffmpeg -i final.mp4 -vf "freezedetect=n=0.001:d=0.8" -an -f null -`.
3. **Komplett in Echtzeit mit Ton ansehen.** Bei einer sprechenden Person fallen Lipsync-Fehler, falsche Betonungen und Stimmsprünge nur so auf.
4. **Script-Abgleich:** Das fertige Video per STT transkribieren und Wort für Wort mit dem freigegebenen Script vergleichen. Fehlt etwas, ist etwas doppelt, wurde ein Markenname falsch ausgesprochen?
5. **Sichtprüfung je Segment** (6 Standbilder als Bogen): Gesicht gleich, Haare und Kleidung gleich, keine dritte Hand, keine verformten Finger, Etikett lesbar, kein Text vom Modell eingeblendet, 4:5-Zone.
6. **Wirkung:** Fühlt es sich an wie das organische Original, oder kippt es irgendwo in Werbung?
7. **Ehrlich berichten:** was geprüft wurde, was nicht und welche bekannten Kleinigkeiten bewusst geblieben sind.

---

## 12. Recht und Plattform (vor jeder Produktion)

Der Kurs geht darauf nicht ein. Für Ads im deutschen bzw. EU-Markt gelten diese Mindestregeln. Im Zweifel juristisch prüfen lassen.

- **Fremde Gesichter:** Kein Gesicht einer echten Person ohne Einwilligung (Recht am eigenen Bild). Das betrifft das Pinterest-Foto für den Avatar und das Original-Video, falls die Creatorin erkennbar bleibt. KI-generiertes Gesicht oder lizenziertes Foto nehmen.
- **Fremde Stimmen:** keine Stimme einer echten Person ohne Einwilligung klonen (Abschnitt 9).
- **Fremde Videos und Texte:** Das Original dient als Analyse- und Bewegungsreferenz. Es kommt nicht in die Ad. Struktur, Beats und Tonalität übernehmen ist Inspiration. Eine wörtliche Übernahme der persönlichen Geschichte einer anderen Person ist riskant (Urheberrecht, Irreführung). Details, Namen und Formulierungen eigenständig machen.
- **KI-Person als Kundin:** Wenn eine KI-Person von „meinen“ Ergebnissen spricht, wirkt das wie ein echtes Testimonial. Das ist irreführend, wenn es nicht gekennzeichnet ist. Die Transparenzpflichten der EU-KI-Verordnung für Deepfakes (Art. 50) und die KI-Kennzeichnung von Meta beachten. Die Ad als KI-generiert kennzeichnen.
- **Vorher/Nachher:** nur echte Bilder echter Kundinnen mit Einwilligung, nie KI-erzeugte Ergebnisbilder.
- **Gesundheitsaussagen:** Bei Nahrungsergänzung nur zugelassene Health Claims (EU-Verordnung 1924/2006, Liste 432/2012). Keine Heilversprechen wie „heilt PCOS“. Nur belegte Zahlen. Die Liste der verbotenen Aussagen aus dem Briefing einhalten.
- **Kein Upload** zu Meta oder anderswo ohne ausdrückliche Freigabe.

---

## 13. Korrekturrunden

- **Auf der besten Fassung aufbauen** und nur die genannten Punkte ändern.
- Fehler im Script → zurück zu Abschnitt 5, danach nur die betroffenen Segmente neu erzeugen.
- Fehler in einem Segment → nur dieses Segment mit präzisiertem Prompt neu erzeugen. Bleibt der Fehler nach zwei Versuchen, das Modell wechseln (Seedance 2.5).
- Alte Fassung als Vergleichsdatei **direkt neben** die neue legen.
- Vorher die **Kosten nennen** (Segmente × 135 bzw. 465, Referenzclip 250) und das Guthaben prüfen.

---

## 14. Modelle (Stand Kurs, Okt./Nov. 2026)

| Modell / Tool | Preis (MaxFusion) | Einsatz | Stärken | Schwächen |
|---|---|---|---|---|
| **Switch Actor Pro** | 250 / bis 30 s | Referenzclip mit neuem Gesicht | behält Setup, Licht, Kamera, Gestik | teuerster Einzelschritt, Haaransatz und Hautübergang prüfen |
| **Wan 3.0 Prime** (References) | 135 / 15 s | **Standard für Sprech-Segmente** | ca. 3× günstiger, mit gutem Prompt realistisch | weniger Emotion und Gestik ohne genauen Prompt, Stimme schwächer |
| **Seedance 2.5** | 465 / 15 s | Problem-Segmente, Produkt-Halteszene, B-Roll mit Face-Swap | sehr realistisch, beste Stimme | teuer |
| **ElevenLabs** (über MaxFusion) | Voice-Switch laut Kurs kostenlos | gleichbleibende Stimme | Stimme frei wählbar | nur eigene oder lizenzierte Stimmen |
| **Gemini** | – | Videoanalyse mit Ton | sieht Gestik, Licht, Delivery | Ergebnis auf Vollständigkeit prüfen |

Andere Plattformen (Kie.ai, Higgsfield) und neue Modelle erst an **einem** Testsegment gegen Wan 3.0 Prime vergleichen, bevor sie eingesetzt werden.

---

## 15. Technische Stolperfallen und Ausgabe

- Video-Referenzen: Switch Actor bis 30 s, die meisten Segment-Modelle bis 15 s. Vorher mit ffmpeg schneiden.
- Untertitel, die in der Vorlage eingebrannt sind, landen im Referenzclip (im Kursbeispiel sichtbar). Deshalb „NO SUBTITLES“ in jedem Prompt. Wenn möglich eine Vorlage ohne eingebrannten Text wählen oder den Ausschnitt so legen, dass kein Text im Bild ist.
- Downloads mit `curl --retry 5 --retry-all-errors` laden. Nichts doppelt starten, das kostet doppelt.
- **Naming** nach Vorgabe des Auftraggebers, z. B. `P7 - CAD80 - VIDEO81 - UGC - 9-16.mp4`, im vorgegebenen Batch-Ordner. Vorhandene Dateien nicht anfassen.
- Arbeitsdateien getrennt halten: `referenz/`, `gemini_analyse.md`, `script/` (alle Fassungen), `avatar/`, `referenzclip/`, `segmente/` (mit Prompt-Log), `broll/`, `schnitt/`, `verworfen/`.

### Erkenntnisse aus eigenen Produktionen
Nach jeder Produktion hier eintragen: gemessene Wörter pro Sekunde auf Deutsch, echte Kosten pro Ad, welche Plattform und welches Modell, typische Fehler und ihre Prompt-Lösung. Sobald eine Regel bestätigt ist, den Vermerk **(Annahme)** entfernen.

- _(noch keine eigene Produktion)_
