# Prompts für KI-Analyse und Vergleich

Die Original-Prompts aus dem Kurs liegen als separate Dateien unter den Videos und stehen nicht im Transkript. Die Prompts hier sind **nachgebaut** aus dem, was Zakaria im Video vorliest und bewertet. Vor dem ersten Einsatz testen und Verbesserungen in SKILL.md, Abschnitt 13 notieren.

**Reihenfolge:** eigene manuelle Analyse → Prompt 1 (Gemini) → Prompt 2 (Vergleich, gleicher Chat) → eigene Gegenargumente (Prompt 3) → blinde Flecken ins Lern-Notizbuch.

---

## Prompt 1: Winner-Breakdown mit Gemini (Video hochladen in AI Studio)

```
Du bist Direct-Response-Analyst für ein 100-Mio-$-DTC-Team. Ich lade dir eine Ad hoch, die nachweislich gut läuft. Zerlege sie so detailliert, dass mein Team ihre Wirkung nachbauen kann. Achte auf Bild UND Ton. Schreibe zu JEDER Antwort, WARUM du das denkst. Wenn etwas unklar ist, schreib "unklar" statt zu raten. Nutze Zeitstempel (mm:ss). Lass KEINEN Abschnitt aus.

0. Vollständiges Transkript mit Zeitstempeln, dann alle Bildschirmtexte separat.
EBENE 1 FUNDAMENT
1. Avatar: Demografie (Alter, Geschlecht, Status, inkl. Begründung: wer hat das meiste Geld und den größten emotionalen Schmerz?), Kernwert, größte tägliche Frustration, was hält ihn nachts wach, geheimer Wunsch, was sollen andere denken / nicht denken.
2. Bewusstseinsstufe (unaware bis most aware) und Marktsättigung (Stufe 1–5; 3 = neuer Mechanismus, 4 = verbesserter Mechanismus) mit Beleg. Was hat der Avatar schon versucht, warum scheiterte es?
3. Identität: aktuell, gefürchtet, gewünscht, Wert der Lücke in Euro und Begründung.
4. Wettbewerbsposition: was alle anderen machen, was diese Ad anders macht, welche Normen sie bricht.
EBENE 2 STRUKTUR
5. Hook Sekunde für Sekunde (Aufmerksamkeit, Qualifizierung, Bindung), Hook-Typen, Thumbstop 1–10.
6. Problem: primärer und sekundäre Schmerzpunkte (auch die des Käufers), Agitationstechnik, Trigger-Sätze, Intensität 1–10 und warum genau so viel.
7. Lösung: Brücke, Aha-Moment, Mechanismus, Secret Reveal (warum nie gehört), Glaubenswechsel alt → neu und WIE er erzeugt wird.
8. Beweisfolge: jedes Beweiselement mit Typ, Inhalt und WARUM an dieser Position; stärkstes Element.
9. Transformation: vorher, nachher, Zeitlinie, Aufwand, Glaubwürdigkeit 1–10.
10. Angebot und CTA: Kernangebot, Boni, Garantie, CTA-Wortlaut, Dringlichkeit, Mikro-Commitments, Risikoumkehr.
EBENE 3 PSYCHOLOGIE
11. Trigger mit Intensität 1–10 (Social Proof, Autorität, Knappheit, Dringlichkeit, Reziprozität, Konsistenz, Sympathie, FOMO, Verlustangst, Neuheit).
12. Emotionale Reise je Abschnitt und emotionaler Höhepunkt (mit Zeitstempel).
EBENE 4 UMSETZUNG
13. Visuals (Farben, Einstellungen, Schnitttempo und Tempowechsel, Overlays, B-Roll-Kongruenz), Audio (Sprecher, Ton, Tempo, Autoritätslevel, Musik und wann/warum sie wechselt, Soundeffekte), Sprache (stärkste Sätze, Lesestufe, Insider-Sprache, emotional:logisch in %, Spezifität, Einwände).
ERGEBNIS
14. Die eine Sache, ohne die diese Ad nicht funktioniert. Top-3-Gründe. Schwächen.
15. Learnings: Must-have vs. Nice-to-have, 3 übertragbare Muster, 2–3 Hypothesen im Format "Wenn wir X, dann Y, weil Z" für mein Produkt: [PRODUKT / AVATAR / BEWUSSTSEINSSTUFE].
```

## Prompt 2: Manuell vs. KI vergleichen (im selben Chat, eigene Analyse anhängen)

```
Du bist mein Lern-Coach und sollst meine Fähigkeit verbessern, Ads zu analysieren. Oben steht deine KI-Analyse dieser Ad. Im Anhang ist meine manuelle Analyse derselben Ad. Vergleiche ehrlich:

1. Bewertung je /10 mit Begründung: Tiefe, Genauigkeit, Psychologie-Verständnis, Umsetzbarkeit, Mustererkennung. Gesamt /50.
2. Wo ich richtig lag (mit Zitat aus meiner Analyse und deiner Beobachtung daneben).
3. Kritische Lücken: was ich übersehen habe und warum es wichtig ist.
4. Wo ich tiefer oder treffender war als du.
5. Meine wiederkehrenden blinden Flecken.
6. Verbesserungsplan: die 3 Dinge, auf die ich beim nächsten Breakdown achten soll, und die Fragen, die ich mir dafür stellen muss.
7. Das EINE, das meine Analysefähigkeit am meisten verbessern würde.
```
Kursbeispiel für die Auswertung: 1. Versuch 25/50 (Genauigkeit 8, Tiefe 4, Psychologie 3) mit der Kernkritik „vom Beschreiben zum Hinterfragen“. 2. Versuch 43/50.

## Prompt 3: Widersprechen (wenn du anderer Meinung bist)

```
Bei Punkt [X] sehe ich es anders: [deine Sicht + Beleg aus der Ad, z. B. Zeitstempel]. Begründe deine Einschätzung noch einmal konkret anhand der Ad, und sag mir dann, wer von uns näher an der Wahrheit liegt, oder ob beide Sichtweisen gelten (z. B. Kernkäufer vs. Halo-Publikum).
```
Erfahrung aus dem Kurs: Die KI irrt bei Ton und Musik (hörte einen Schrei, der nicht da war; deutete Spannungsmusik als „beruhigend“). Bei Visuals ist sie oft besser als der Mensch.

## Prompt 4: Verlierer-Autopsie vorbereiten (Claude, Text plus Metriken)

```
Hier sind Script/Copy, Metriken (Hook Rate, Hold Rate, Ø Watch Time, CTR, CPC, CPM, CVR, CPA vs. Ziel), die Retention-Werte je Abschnitt und meine ursprüngliche Hypothese einer Ad, die verloren hat. Dazu meine Avatar-Recherche.
1. Bestimme die Bruchzone (Hook / Body / CTA / Funnel) und begründe sie mit den Zahlen.
2. Ordne die größte Klippe der Scriptzeile zu: Welche Aufgabe hatte die Stelle, hat sie sie erfüllt?
3. Prüfe Sprache (wörtlicher Abgleich mit Avatar-Zitaten), Bewusstseinsstufe, Emotion/offene Schleifen, Glaubwürdigkeit, Tempo.
4. Nenne EINEN Fatal Flaw mit Kategorie und was erhalten bleiben sollte.
5. Schlage max. 3 Hypothesen für Version 2 vor, jede mit nur einer geänderten Variable.
Sei streng. Ich mache danach meinen eigenen Avatar-Selbstcheck und vergleiche.
```

## Prompt 5: Kommentare auswerten

```
Hier sind die Kommentare unter einer Ad. Sortiere nach: (a) Spiegelung/Wiedererkennung ("sieht aus wie mein Kind"), (b) offene Fragen und Einwände ("wie lange dauert es?", "gibt es das ohne Abo?"), (c) Skepsis, (d) Social Proof. Leite ab: welche Lücken die Ad hat und welche 3 Einwände eine neue Version beiläufig beantworten sollte.
```
