---
name: ugc-script
description: Schreibt UGC-Scripts: TOF-UGC, Story-UGC, Testimonials, Yapping, Mini-VSL, natürliche Sprache und Creator-Briefing. Bei UGC Script, Story Ad, Creator Brief oder Testimonial.
---

# UGC-Scripts schreiben

Dieser Skill macht aus deiner Avatar-Recherche verkaufende UGC-Scripts: kurze Top-of-Funnel-Videos, Story-UGC, Testimonial-Storys, UGC-Mini-VSLs und lange Storys. Danach kommen die Prüfung des Scripts, die gesprochene Fassung und das Briefing für die Creatorin.

**Herkunft:** Zakaria Airakaz, ECOM Masterclass 2026. Verwendet wurden die Module „4. Creatives Mastery / 2. Master TOF UGC“ (Lektionen 6 bis 11), „5. Elite Copywriting / Part 5 – Story & Drama“ (Lektionen 1 bis 15), „2. Ecom Masterclass / 8. Ads creation“ (Lektionen 26 und 27) und Zakarias Antworten im Discord. Die Regeln sind **noch nicht in einer eigenen Produktion bestätigt**. Zahlen und Beispiele stammen aus dem Kurs. Was übertragen oder geschätzt ist, trägt den Vermerk **(Annahme)**.

**Verwandte Skills:**
- `copywriting-grundlagen`: Bewusstseinsstufen, Kaufemotionen, Hooks, Techniken
- `winner-ad-analyse`: Winner- und Verlierer-Ads zerlegen
- `yapping-ad`: KI-Produktion von Yapping-UGC

**Referenzen (nur lesen, wenn gebraucht):**
- `references/story-strukturen.md`: die drei Story-Typen, die kurze Story, die Testimonial-Story, Yapping und der volle Story-Bogen mit 12 Beats. Lesen, bevor du ein Script baust.
- `references/beispiel-breakdowns.md`: zerlegte Winner-Ads (Primal Queen 21M/27M, Pet Lab 19M/21M, Happy Mammoth 8,3M, Derila Ergo, Protein Coffee und andere) und die PCOS-Script-Entwicklung von der ersten Fassung bis zur Endfassung. Lesen, wenn du Vorbilder oder Formulierungsideen brauchst.
- `references/prompts.md`: fertige Prompts für Ad-Konzept, Script-Analyse, Natural Speech und Creator-Brief. Lesen, sobald du einen davon ausführst.
- `references/creator-brief-vorlage.md`: Vorlage für das Creator-Briefing. Lesen, wenn das Script freigegeben ist.

---

## 0. Grundhaltung (die wichtigsten Regeln zuerst)

1. **Das Script entsteht aus der Avatar-Recherche, nicht aus einer Formel.** Copywriting heißt hier: die Worte deiner Kundinnen nehmen und in eine Struktur setzen. Lies vor jeder Schreibsession das Avatar-Dokument mit den Originalzitaten. Schau zusätzlich in die aktuellen Top-Posts der Community (z. B. den Subreddit), um frische Formulierungen zu finden.
2. **Erzählen, nicht verkaufen.** Ganz oben im Funnel verdient die Ad Aufmerksamkeit, unterhält und bildet. Die Ad öffnet das Gespräch, die Landingpage, das Listicle oder das Quiz schließt den Verkauf ab. Gesehen werden soll „eine Person wie ich erzählt ihre Geschichte“, nicht „eine Marke will mir etwas verkaufen“.
3. **Wiedererkennung schlägt Clickbait.** Die Zuschauerin muss denken: „Das bin ich.“ Das erreichst du am schnellsten über konkrete Alltagsmomente (die Dusche, der Friseur, das Foto von oben), nicht über laute Scroll-Stopper.
4. **Das Wunschergebnis genau so beschreiben, wie der Avatar es erwartet, nicht mehr und nicht weniger.** Versprichst du mehr, wirkt es unglaubwürdig („volle Haare nach zwei Wochen“). Versprichst du weniger, weckt es kein Verlangen. Bei Haaren sind realistische Zeiträume etwa 3 Monate bis zu den ersten Babyhaaren und etwa 6 Monate bis zu sichtbaren Ergebnissen.
5. **Das Problem in der Vergangenheit erzählen** („ich hatte …“, „früher …“). Die Zuschauerin hat das Problem jetzt, die Sprecherin hatte es früher. Daraus entsteht Hoffnung und die Frage „Was hat sich geändert?“. Bei problembewussten Zuschauerinnen nicht Angst machen und nicht zusätzlich Salz in die Wunde streuen: Auf Social Media wollen sie ihrem Alltag entkommen. Mehr Druck und Dringlichkeit nur bei Zuschauerinnen, die das Problem noch nicht kennen.
6. **Konkret statt allgemein:** „3 Uhr nachts“, „sechs Wochen“, „1.847 € für Supplements im letzten Jahr“, „elf Ärzte“. Konkrete Details glaubt das Gehirn, weil sie sich niemand ausdenkt.
7. **Es gibt keine Zauberformel.** Die Strukturen sind Gerüste. Den ersten Entwurf schreibst du selbst. Claude glättet, kürzt und prüft. Am Ende liest du das Ergebnis selbst kritisch.
8. **Für das Sprechen schreiben, nicht für das Lesen.** Unvollständige Sätze, Füllwörter und Selbstkorrekturen sind erwünscht (Abschnitt 9).
9. **Bild und Text passen in jeder Sekunde zusammen.** Was gesagt wird, ist zu sehen. Das müde Gehirn beim Scrollen soll nichts entschlüsseln müssen.
10. **Deutsche Ads auf Deutsch denken.** Ein englisches Vorbild wird nicht übersetzt, sondern so geschrieben, wie eine deutsche Frau oder ein deutscher Mann es erzählen würde, mit deutschen Füllwörtern und deutschem Alltag (Hausarzt statt OB-GYN, dm statt Target).
11. **Nur belegte Aussagen.** Health Claims, Testimonials und Vorher-Nachher-Bilder siehe Abschnitt 13.

---

## 1. Voraussetzungen

- **Avatar-Dokument mit Originalzitaten:** Schmerzen, Alltagsprobleme, Auslöser-Momente, Glaubensfehler („Minoxidil hilft allen, nur mir nicht“), Wünsche, Einwände, Sprachmuster.
- **Dokument zur Ursache des Problems** und **Dokument zum Lösungsmechanismus**.
- **Produktdokument:** Zutaten mit Dosis, Einnahme, realistische Zeitachse, Studien, Angebot, Garantie.
- **Einwand-Dokument**, z. B. aus Bewertungen ähnlicher Produkte.
- **Gewählter Winkel (Angle)**, z. B. „Identitätsverlust → Identität zurück“, und die **Bewusstseinsstufe** des Avatars. Beides kommt aus `copywriting-grundlagen`.
- **Swipe-Sammlung zerlegter Winner-Ads** aus der eigenen Nische und von fremden Marken (`winner-ad-analyse`).
- Am besten ein **Claude-Projekt**, in dem alle Dokumente liegen. Dann kennt Claude bei jedem Prompt den Kontext.
- Vom Auftraggeber: **Pflichtsätze**, **verbotene Aussagen**, **Markenrichtlinien**.

---

## 2. Ablauf

```
Recherche lesen (1 bis 2 h) → Kopf frei machen → 3 bis 5 Winner-Ads zerlegen
  → Angle, Format und Story-Typ wählen → Rohentwurf selbst schreiben (Kundenzitate hineinkopieren)
  → Claude: Grammatik, Fluss, Kürzung, Hook-Varianten → Script-Analyse (Abschnitt 8) → Überarbeitung
  → Langfassung und Kurzfassung → [Freigabe] → Natural-Speech-Fassung (Abschnitt 9)
  → Creator-Brief (Abschnitt 10) → [Freigabe] → Dreh → Review gegen Brief → Test
```

**Fokus vor dem Schreiben:** Zakaria meditiert vor jeder Schreibsession 10 bis 15 Minuten in Stille, mit Noise Cancelling, und schreibt am liebsten gleich morgens. Während der Session sind keine anderen Tabs offen. Der Grund: Ein Script über 1 bis 3 Minuten braucht einen roten Faden von Anfang bis Ende. Wer zerstreut schreibt, verliert ihn in der Mitte.

**Ohne eigene Erfahrung zuerst zerlegen:** Wer noch keine Winner geschrieben hat, startet nicht mit einem leeren Blatt. Erst Ads zerlegen, die schon lange laufen. Das Gehirn braucht Vorlagen, aus denen es Strukturen ableiten kann. Danach kopierst du keine fremden Scripts, sondern schreibst aus der eigenen Recherche.

---

## 3. Format wählen

Zuerst legst du die **Botschaft (Big Idea)** fest, erst danach das Format. Welches Format sie am besten transportiert, ist die zweite Frage.

| Format | Länge | Wann | Gerüst |
|---|---|---|---|
| **Kurze TOF-UGC** | 15 bis 45 s | Neugier wecken, Klick auf die Vorverkaufsseite | Hook → Problem → Produkt bzw. Lösung → Nutzen und Funktionsweise → Beweis → sanfter CTA |
| **Lange TOF-UGC** | 45 bis 90 s | mehr Platz für Psychologie | wie die kurze Variante, dazu Schmerz verstärken, gescheiterte Lösungen, Autorität |
| **UGC-Mini-VSL** | 60 bis 120 s | Problem- bis lösungsbewusste Zuschauerinnen, Mechanismus nötig | Hook → Ursache vorstellen → Ursache erklären → Folgen → gescheiterte Lösungen → Lösung und einzigartiger Mechanismus → Produkt → Beweis und Autorität → sanfter CTA |
| **Story-UGC kurz** | 15 bis 60 s | Emotion, Wiedererkennung, auch ohne Voiceover | Hook → Spannung → Wendung → Ergebnis (Abschnitt 4) |
| **Testimonial-Story** | Kommentar, Review, 15 bis 30 s | Social Proof, Einwände ausräumen | Moment → Kampf → Entdeckung mit Skepsis → Jetzt (Abschnitt 7) |
| **Yapping** | 1 bis 3 min | wirkt besonders gut bei Frauen (Zakarias eigene Ads) | siehe `references/story-strukturen.md` und `yapping-ad` |
| **Voller Story-Bogen** | VSL, Advertorial, lange Ad-Texte | Story als Verkaufsseite | 12 Beats in 4 Akten (`references/story-strukturen.md`) |

**Wohin der Traffic geht:** UGC führt zu einem Listicle, einer Vorverkaufsseite oder einem Quiz, eine VSL kann direkt auf die Produktseite führen. Ad und Seite müssen zusammenpassen: Die Seite setzt genau das Gespräch fort, das die Ad begonnen hat.

**Story-Typ wählen:** Gründer-Story, Kunden-Story oder Moment-Story. Wann welcher passt, steht in `references/story-strukturen.md`. Faustregel: Für Hooks und kurze Formate die **Moment-Story**, für UGC und Testimonials die **Kunden-Story**, für Advertorials und Produkte mit eigenem Mechanismus die **Gründer-Story**. In langen Formaten kombinierst du alle drei: mit einem Moment öffnen, mit der Kundenreise weitermachen, über die Gründer- bzw. Entdeckungs-Story den Mechanismus erklären und mit einem Zukunftsmoment schließen.

---

## 4. Kurze Story-UGC (15 bis 60 s): vier Beats

1. **Hook:** mitten in einen konkreten Moment springen, der den Erzählfluss unterbricht. Beispiele: „Meine Friseurin hat gefragt, ob ich krank bin.“ „3 Uhr nachts, das Laken schon wieder durchgeschwitzt, das dritte Mal diese Woche.“ Diesen Moment findest du in der Recherche: Wo sagen viele „genau das“?
2. **Spannung:** das Problem spürbar machen, und zwar in der Vergangenheit, mit konkreten Details und dem, was auf dem Spiel stand. Beispiel: „Ich hab vielleicht vier Stunden geschlafen. Mein Mann ist ins Gästezimmer gezogen. Meine Ärztin meinte nur: ‚Das sind die Wechseljahre.‘“
3. **Wendung:** Was hat sich geändert? Eine Entdeckung, eine Empfehlung, mit Skepsis. Beispiel: „Dann hat mir meine Schwester das geschickt. Ich hab's nicht geglaubt, ich hatte schon alles probiert. Aber ich war verzweifelt.“
4. **Ergebnis:** das Wunschergebnis genau treffen, mit Sinneseindrücken. Beispiel: „Sechs Wochen später: sieben Stunden am Stück. Ich bin trocken aufgewacht, vor dem Wecker. Ausgeruht. Mein Mann schläft wieder neben mir.“ Den Wecker gar nicht erst zu hören, ist für eine erschöpfte Frau der Traum. Solche Bilder zählen mehr als jeder Nutzen-Claim.

**Zeitaufteilung (laut Kurs):**

| Länge | Hook | Spannung | Wendung | Ergebnis |
|---|---|---|---|---|
| 15 s | 2 s | 5 s | 3 s | 5 s |
| 30 s | 3 s | 10 s | 5 s | 12 s |
| 45 s | 3 s | 15 s | 8 s | 18 bis 20 s |
| 60 s | 3 bis 5 s | 20 s | 10 s | 25 s |

Das Ergebnis bekommt am meisten Zeit, weil es am meisten interessiert. Der Mechanismus darf kurz sein: Ein sichtbares Vorher-Nachher wirkt wie ein Freund, der sagt „Probier das, das hilft mir“. Dafür muss niemand verstehen, wie Koffein wirkt. Den Mechanismus vertieft die Landingpage.

**Regeln:** Vergangenheit, Ich-Form, gesprochene Sprache. Emotionen zeigen statt benennen: nicht „ich war so frustriert“, sondern „ich saß im Auto und hab geheult“. B-Roll oder Mimik tragen die Emotion mit.

---

## 5. Hooks für UGC

Die Grundlagen stehen in `copywriting-grundlagen`. Hier nur, was für UGC zählt:

- **Ein Moment aus der Recherche**, den die Zuschauerin sofort wiedererkennt („Meine Tochter hat seit zwei Jahren auf keinem Schulfoto gelächelt“).
- **Intensive offene Schleife:** Beziehungen, Scham, Gefahr („Mein Mann dachte, ich betrüge ihn“, „Ich wäre fast abgezockt worden“). Die Auflösung muss halten, was die Schleife verspricht. Sonst fühlt sich die Zuschauerin verarscht.
- **Konkret und sofort einordnen:** Statt „Wie hat mir niemand das über PCOS gesagt?“ besser „Ich hab drei Jahre lang nach jedem Duschen geweint, bevor mir jemand das über PCOS erzählt hat.“ Die zweite Fassung ordnet die Zuschauerin schneller zu, ist bildhaft (Dusche) und lässt trotzdem eine Frage offen.
- **Markenname als Neugier**, wenn er nicht nach Produkt klingt: „Ich hab beschlossen, Primal Queen zu probieren, und hatte keine Ahnung, dass das mein Leben verändert.“ Das funktioniert auch als Retargeting bei Leuten, die die Marke schon kennen.
- **Weitere Formen:** Widerspruch („Früher hab ich jeden Tag wegen meiner Haare geweint. Heute bin ich froh, dass ich PCOS habe.“), Rant („Das wird dich wütend machen …“), Liste („3 Zeichen, dass dein Haarausfall von PCOS kommt“, „3 Warnsignale“), Formate wie „Ein Tag mit mir“ oder „Komm mit einkaufen“.
- **Nie mit dem Produkt starten**, wenn die Zielgruppe es noch nicht kennt.
- Hook-Rate laut Kurs: 30 % ist Durchschnitt, ab 60 % läuft die Ad richtig gut.

---

## 6. Rohentwurf schreiben

1. **Recherche offen, Zitate hineinkopieren.** Zakaria kopiert echte Sätze aus Reddit wörtlich in den Entwurf und markiert sie farbig. Beispiele: „Meine Haare waren das Einzige an mir, bei dem ich mich schön gefühlt habe“, „Duschen ist das Schlimmste.“
2. **Frei herunterschreiben**, ohne auf Grammatik zu achten. Hauptsache, Gefühl und Struktur stimmen.
3. **Claude:** „Korrigiere Grammatik und Tippfehler, behalte Struktur und Emotion. Wie lang ist das gesprochen?“ Danach eine Lang- und eine Kurzfassung mit „gleicher Intensität“ anfordern.
4. **Pro Angle mehrere Konzepte** schreiben. Zakaria hat für den Angle Identitätsverlust geschrieben: den Mythos-Check („3 Mythen über PCOS-Haarausfall“), „Ein Tag mit mir“, Testimonial-Stil („Das Einzige, was bei mir wirklich geholfen hat“), Warnsignale, Widerspruch und Rant („Ärzte haben mich abgespeist“). Getestet werden mehrere, denn das perfekte Script gibt es nicht.

**Inhaltliche Regeln aus der Überarbeitung des PCOS-Scripts:**
- **Fachbegriffe erklären:** Viele wissen nicht, was DHT ist. Also: „ein Hormon namens DHT, das die Haarwurzeln schrumpfen lässt“, mit einer kleinen Schleife („Bleib dran, ich erklär's dir“). Ein unerklärtes Fachwort verliert die Zuschauerin sofort.
- **Logische Lücke als Spannung nutzen:** „Wenn DHT das Problem ist und ich es blockiere, warum fallen mir dann immer noch die Haare aus?“ Diese Frage bringt die Ursache ins Spiel.
- **Die Ursache bildhaft erklären:** „Als würdest du die Badewanne ausschöpfen, während der Hahn noch läuft.“ „Den Boden wischen, während das Waschbecken überläuft.“ „Die Kopfhaut ist ein Garten, und der Körper gießt Gift statt Wasser.“
- **Bestehende Überzeugungen nicht frontal angreifen:** Nicht „Rosmarinöl wirkt nicht“, sondern „Es hilft bis zu einem Punkt, aber es durchbricht den Kreislauf nicht.“
- **Die Entdeckung muss logisch sein.** Zuerst wird das Produkt gefunden (Kommentare, Community, Empfehlung), danach recherchiert die Sprecherin Zutaten und Studien. Falsch ist die Reihenfolge „Ich habe den Mechanismus erforscht und dann zufällig ein Produkt mit genau diesen Zutaten gefunden.“ Das klingt erfunden. Ein Produkt, das aus dem Nichts auftaucht, ist der häufigste Fehler.
- **Social Proof in die Entdeckung legen:** „… und in den Kommentaren hundert Frauen mit PCOS: ‚Bei mir wirkt's auch.‘“
- **Abgrenzen:** „Nicht noch ein Haarvitamin, sondern endlich etwas, das für uns gemacht ist.“ Das trifft das Gefühl, als Frau von Medizin und Markt übersehen zu werden.
- **Zutatenlisten sind Emotionskiller.** Jede Zutat bekommt deshalb einen emotionalen Nutzen: „… um die Insulinresistenz zu beruhigen, die diesen ganzen Albtraum befeuert hat.“ Das langweilige Erklären darf auch Kommentar und Humor enthalten (Derila: „Das CPAP hat er drei Nächte benutzt, er meinte, er fühlt sich wie ein Laubbläser“).
- **Realistische Zeitachse und Risikoumkehr** in den CTA: „Die ersten Wochen nichts, ich hätte fast aufgehört.“ „Es gibt eine Geld-zurück-Garantie, also kein Risiko.“ Das räumt den Einwand aus, schon oft reingefallen zu sein.

---

## 7. Testimonial-Storys, die echt wirken

Die meisten Testimonials klingen gefälscht: glatt, rundum positiv, über Versand und Support. „Tolles Produkt, schneller Versand, hat mein Leben verändert“ passt auf jedes Produkt und überzeugt niemanden.

**Stil „zufällig mitgehört“:** Es soll klingen, als würde jemand im Café der Freundin erzählen. Locker, nicht poliert, mit merkwürdigen Details, verletzlich, ehrlich skeptisch.

**Struktur:** Moment („3 Uhr nachts, wieder durchgeschwitzt …“) → Kampf („drei Ärzte, acht Monate Traubensilberkerze, nichts“) → Entdeckung, beiläufig und skeptisch („in einer Facebook-Gruppe, in einer dieser Google-Spiralen um 3 Uhr, ich dachte, das ist Quatsch“) → Jetzt, ganz konkret („gestern hab ich mich hingehockt und meinen Enkel hochgehoben, ohne nachzudenken“).

**Ehrlichkeitsprinzip:** Skepsis zugeben („Ich hätte fast nicht bestellt“). Einschränken („Ich sag nicht, dass es bei allen wirkt“). Kleine Mängel nennen („Die erste Woche passierte nichts“, „Es hat länger gedauert, als sie gesagt haben“). Peinliches zugeben, das man öffentlich sonst nicht sagt. Ein Testimonial, das zu 100 % perfekt ist, glaubt niemand.

**Was die Primal-Queen-Kommentare zeigen** (Details in `references/beispiel-breakdowns.md`): Screenshots im Stil von Facebook-Kommentaren mitten auf der Seite, direkt nach der Lösung, nicht ganz unten. Kleine Tippfehler und Rohheit lassen sie echt wirken. Jeder Kommentar räumt einen Einwand aus: Libido, „Ich bin der größte Geizhals und Pessimist“, „Abo sofort gekündigt, aber das Produkt behalten“ und „Rollstuhl steht jetzt in der Ecke“.

**So nutzt du das (sauber):**
- Bitte echte Kundinnen gezielt um konkrete Bewertungen („Was war vorher, welcher Moment hat sich verändert?“).
- Wähle aus echten Bewertungen die konkretesten aus und zeige sie im Kommentar-Stil.
- Im Kurs heißt es offen, dass manche Marken Kommentare selbst erzeugen. **Das machst du nicht** (Abschnitt 13).

---

## 8. Script prüfen und überarbeiten

Die KI findet viel, aber nicht alles. Zakaria hat zwei Fehler selbst gefunden, die die KI übersehen bzw. als „8 von 10“ bewertet hatte: das unerklärte DHT und ein Produkt, das aus dem Nichts auftauchte. Deshalb prüfst du immer **KI-Analyse plus eigenes kritisches Lesen**. Der Prompt steht in `references/prompts.md`. Dazu gehören alle Dokumente (Avatar, Ursache, Mechanismus, Produkt, Einwände, Angebot) und eine kurze Produktzusammenfassung.

**Prüfkategorien:**
1. **Passt es zum Avatar?** Stimmen Bewusstseinsstufe und Marktreife, und zwar ab dem Hook? Kommen die Worte wirklich von Kundinnen? Wird Wissen vorausgesetzt, das sie nicht haben?
2. **Hook:** Wie schnell erkennt sich die Zuschauerin (Ziel: deutlich unter 1 s)? Welcher Typ ist es, gibt es einen konkreten Moment, ein Bild, eine Zuordnung zur Zielgruppe, eine offene Frage?
3. **Logik der Story:** Ausgangslage → Konflikt → gescheiterter Versuch → Entdeckung → Auflösung. Folgt B logisch aus A? Gibt es Sprünge?
4. **Glaubwürdigkeit:** Wirkt es echt, leicht gescriptet oder offensichtlich ausgedacht?
5. **Übergänge:** Spiegeln → Ursache → Lösung → Produkt. Jede Brücke muss tragen.
6. **Ursache:** konkret, neu, einfach. Bullshit-Warnzeichen: vager Mechanismus, erfundene Wissenschaft, Widerspruch zum Allgemeinwissen, Mechanismus passt auf jedes Problem, kein „Wie“, klingt beeindruckend und sagt nichts. **Test mit der skeptischen Freundin:** Kannst du es ihr in 30 Sekunden so erklären, dass sie es glaubt?
7. **Lösungsmechanismus:** Passt jede Zutat zu einem Teil der Ursache? Ist die Lösung abgegrenzt, machbar (z. B. 2 Kapseln am Tag) und mit einer glaubwürdigen Geschwindigkeit?
8. **Gescheiterte Versuche:** Werden sie konkret genannt (Minoxidil, Rosmarinöl, Biotin) und erklärt, warum sie scheitern mussten?
9. **Offene Schleifen:** Wo öffnen sie sich, wo schließen sie sich, nichts bleibt vor dem CTA offen?
10. **Emotionaler Verlauf:** Jeden Abschnitt einordnen (Neugier, Frust, Wiedererkennung, Verzweiflung, Hoffnung …) und Einbrüche finden. Im Beispiel fiel die Emotion bei der Zutatenliste auf 6 von 10.
11. **Konkretheit:** Verhältnis von konkreten zu allgemeinen Aussagen. 14 zu 3 war „exzellent“.
12. **Bildung und Emotion im Gleichgewicht:** Kein Erklärblock ohne Gefühl.
13. **CTA:** natürlicher Abschluss, Dringlichkeit, Risikoumkehr, eine einzige klare Handlung.

Danach Feedback geben, wie im Kurs: deine eigenen Notizen in den Text schreiben („hier fehlt eine offene Schleife“, „DHT erklären“, „Entdeckung über Kommentare statt aus dem Nichts“), Claude analysieren und neu schreiben lassen, wieder prüfen. So oft wiederholen, bis aus einem durchschnittlichen Script ein starkes wird.

---

## 9. Natural-Speech-Fassung

Ein geschriebenes Script klingt vorgelesen. Deshalb kommt vor dem Briefing eine **gesprochene Fassung**. Vorher legst du fest: Alter der Sprecherin, emotionaler Zustand und Energie. Der Prompt steht in `references/prompts.md`.

- Verkürzungen, Füllwörter, Selbstkorrekturen: „Ich hab drei Jahre, ehrlich, drei Jahre lang …“, „Warte, Moment …“, „Weißt du, was ich meine?“
- Unsicherheit wie in echten Erinnerungen: „Ich glaub, es war Woche drei, vielleicht vier.“
- Pausen und Tempo markieren: schneller, wenn sie aufgeregt ist, langsamer und leiser in emotionalen Momenten.
- **Pflichtsätze bleiben inhaltlich gleich**, z. B. die Erklärung der Ursache.
- Für **Deutsch (Annahme):** „also“, „ehrlich gesagt“, „keine Ahnung“, „so richtig“, „halt“, „boah“. Kein Übersetzungsdeutsch.

---

## 10. Creator-Brief

Es gibt zwei Arten von Creatorinnen. **Schauspielerinnen** lernen ein Script und spielen es glaubwürdig. **Yapperinnen** sind gut darin, frei zu erzählen, aber nicht darin, Text auswendig zu lernen. Die meisten gehören zur zweiten Art. Sie bekommen deshalb **kein Script zum Auswendiglernen**, sondern ein Briefing mit Beats, Kernideen, emotionalen Schlüsselmomenten und dem Script als Referenz („Erzähl es mit deinen Worten“). Die Vorlage steht in `references/creator-brief-vorlage.md`, der Prompt in `references/prompts.md`.

- **Die Creatorin passt zum Avatar:** Alter, Geschlecht, Look, Akzent. Eine Anti-Falten-Creme für Frauen ab 50 bewirbt keine 25-Jährige mit makelloser Haut. Ausnahme: Expertinnen und Autoritätsfiguren.
- Hatte die Creatorin das Problem nie, verbindet sie sich im Briefing mit einem eigenen ähnlichen Gefühl („Denk an etwas, das du nicht lösen konntest“). Erfundene Ergebnisse gibt sie trotzdem nicht als eigene aus (Abschnitt 13).
- **Muss gesagt werden:** die Kernhypothese, z. B. „DHT-Blocker allein reichen nicht, weil …“. **Darf nicht gesagt werden:** Heilversprechen, unrealistische Zeiträume, nicht vorhandene Zulassungen. Creatorinnen übertreiben gern, wenn sie begeistert sind.
- **Motivation:** feste Gage plus Aussicht auf Retainer und Bonus bei Winnern. Das Briefing ist ihr Vorsprechen.
- Prüfe die Beats, die die KI ins Briefing schreibt, gegen das Script.
- Gute Creatorinnen fest binden. Laut Kurs gewinnen Yapping-Ads oft eher durch die Creatorin als durch das Script.

---

## 11. B-Roll und Bild

- Alles, was gesagt wird, ist zu sehen („gelbe Zähne, Mundgeruch, Zahnstein“, jedes Mal mit passendem Bild).
- Etwa alle 3 Sekunden ein Schnitt oder Bildwechsel. Denkpausen werden herausgeschnitten.
- B-Roll-Clips von 3 bis 5 s im natürlichen Licht, ohne in die Kamera zu schauen. Typische Motive: das Problem (Haare in der Bürste, im Abfluss), die Emotion (weg vom Spiegel, nachts scrollen), gescheiterte Produkte nebeneinander, das Produkt in der Routine, das Ergebnis (durch die Haare streichen, sich im Spiegel mögen).
- Das Produkt erst zeigen, wenn es in der Story entdeckt wird, nicht vorher.
- Laut Zakaria laufen Ads oft besser von einer Drittseite oder dem Kanal der Creatorin aus als von der Markenseite, weil sie dort authentischer wirken.

---

## 12. Typische Fehler

- Mit dem Produkt starten, obwohl die Zielgruppe es nicht kennt. Gerade bei langen Ad-Texten tötet das die Ad.
- Fremde Scripts kopieren und nur Wörter austauschen, statt aus der eigenen Recherche zu schreiben.
- Allgemeines Vorher („Ich hatte wenig Energie“) statt konkreter Alltagsprobleme.
- **Wunderversprechen.** Das heißt: Du verstehst den Avatar nicht und weißt nicht, was er glauben kann.
- Schwacher Beweis, falsche Art Beweis für diese Zielgruppe.
- Den Mechanismus weglassen, wo er nötig ist (VSL, Mini-VSL), oder ihn so kompliziert machen, dass ihn niemand versteht.
- **Der Tiefpunkt ist eine Entscheidung** („Ich hab beschlossen, etwas zu ändern“) **statt eines Moments mit Zeugen** (der Sohn, der Partner, die Kollegin).
- Ein Fachwort ohne Erklärung. Ein Produkt, das aus dem Nichts auftaucht. Ein Zutaten-Block ohne Gefühl.
- Die Emotion trifft nicht: dramatischer als die echte Erfahrung („drei Tage nicht aus der Dusche gekommen“) oder schwächer.
- Bei problembewusstem Publikum Salz in die Wunde streuen, statt Wiedererkennung zu schaffen.
- Falsche Dringlichkeit und Fake-Countdowns.
- Ein Hook, dessen Schleife am Ende nicht eingelöst wird.

---

## 13. Recht und Plattform (kurz)

- **Nur echte Testimonials** von echten Kundinnen mit Einwilligung. Keine selbst geschriebenen Kommentare und Bewertungen. Das ist irreführend (UWG) und verstößt gegen die Regeln von Meta.
- **Creatorinnen erzählen nur, was stimmt.** Wer das Produkt nicht selbst genutzt oder das Problem nicht gehabt hat, gibt keine erfundenen persönlichen Ergebnisse als eigene aus. Dann eine echte Kundin finden oder das Format ändern (z. B. „Was uns Kundinnen schreiben“). Werbung muss als Werbung gekennzeichnet sein. Zakaria selbst verzichtet für seine Marken auf erfundene KI-Creatorinnen (Stichworte FTC und Exit) und nutzt KI nur für B-Roll und Animation.
- **Health Claims:** Bei Nahrungsergänzung nur zugelassene Aussagen (EU-Verordnung 1924/2006, Liste 432/2012). Keine Heilversprechen. Studien nur zu den tatsächlichen Zutaten und in der richtigen Dosis.
- **Vorher-Nachher** nur echt und mit Einwilligung.

---

## 14. Endkontrolle und Output

**Lieferung pro Script:**
1. Endfassung lang und kurz, mit Zeitangaben
2. 3 bis 5 Hook-Varianten im selben Gefühl
3. Natural-Speech-Fassung
4. Ergebnis der Script-Analyse mit den Werten aus Abschnitt 8 und den umgesetzten Änderungen
5. Creator-Brief inklusive B-Roll-Liste
6. Hinweis, auf welche Seite der Traffic geht (Listicle, Quiz, Vorverkaufsseite) und warum Ad und Seite zusammenpassen

**Checkliste vor der Freigabe:**
- [ ] Die Zuschauerin erkennt sich in den ersten 2 s, im Hook steht ein konkreter Moment.
- [ ] Die Story ist in der Vergangenheit und Ich-Form erzählt, gesprochene Sprache, keine Marketing-Floskeln („Game-Changer“, „revolutionär“).
- [ ] Mindestens 3 Originalformulierungen aus der Recherche sind drin.
- [ ] Jedes Fachwort ist erklärt, die Ursache besteht den 30-Sekunden-Test mit der skeptischen Freundin.
- [ ] Das Produkt taucht logisch auf (gefunden → geprüft), Social Proof liegt in der Entdeckung.
- [ ] Kein Abschnitt ohne Emotion, Zutaten sind mit Nutzen verknüpft.
- [ ] Ergebnis und Zeitachse sind realistisch, Skepsis und kleine Mängel kommen vor.
- [ ] Sanfter CTA mit Risikoumkehr, alle Schleifen sind geschlossen.
- [ ] Abschnitt 13 ist erfüllt, Pflichtsätze sind drin, verbotene Aussagen nicht.
- [ ] Bei deutschen Ads: klingt wie eine Deutsche, nicht übersetzt.

---

## 15. Erkenntnisse aus eigenen Produktionen

Nach jedem Test eintragen: welches Format und welcher Hook gewonnen haben, Hook-Rate, CTR und CPA, welche Kundenzitate funktioniert haben, welche Brief-Anweisungen die Creatorinnen falsch verstanden haben. Bestätigte Regeln verlieren den Vermerk **(Annahme)**.

- _(noch keine eigene Produktion)_
