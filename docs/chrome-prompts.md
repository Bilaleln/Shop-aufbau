# Prompts für Claude in Chrome

Zwei Prompts zum Kopieren. **Prompt A zuerst** — er sichert die App-Einstellungen,
die über die Shopify-API nicht lesbar sind und mit dem Store verloren gehen.
Prompt B baut das Setup auf dem neuen Store nach.

Vorbereitung für beide: im selben Chrome-Profil bei Shopify eingeloggt sein und
den Tab auf dem Admin des jeweiligen Stores offen haben.

---

## Prompt A — Alles sichern (im ALTEN Store ausführen)

```text
Du arbeitest im Shopify-Admin des Stores veilkind.com (Handle: 0vmyhz-pn).

AUFGABE: Dokumentiere die Konfiguration von zwei Apps vollständig, damit ich sie
auf einem neuen Store nachbauen kann. Der Store wird danach gelöscht.

STRENGE REGELN:
- Nur lesen. Klicke NIE auf Speichern, Löschen, Deaktivieren, Deinstallieren
  oder Veröffentlichen.
- Ändere kein Feld, auch nicht "nur zum Ausprobieren".
- Wenn ein Bildschirm eine Bestätigung verlangt, brich ab und frag mich.

GEHE DIESE SEITEN DURCH UND NOTIERE JEDEN SICHTBAREN WERT:

1. Apps → Kaching Bundle Quantity Breaks
   - Liste aller Bundles: Name, Status (aktiv/inaktiv), zugewiesene Produkte
   - Öffne JEDES Bundle einzeln, besonders "Bundle #2", und notiere aus allen
     Tabs: Anzahl Optionen, Titel/Untertitel je Option, Menge je Option,
     Rabatt je Option (Typ und Wert), Badges/Labels, Vorauswahl, Farben,
     Schriftgrößen, Layout-Variante
   - Ganz besonders: die Subscription-/Abo-Einstellungen. Welche Option ist ein
     Abo? Auf welchen Selling Plan zeigt sie? Wie heißt der ausgewählte Plan
     genau? Gibt es getrennte Preise für One-time und Subscribe?
   - Platzierung/Placement: welcher CSS-Selector, davor oder danach eingefügt
   - Alle globalen App-Einstellungen (Übersetzungen, Währungsformat, Analytics)

2. Apps → Loop Subscriptions
   - Selling Plans / Pläne: die Gruppe "Subscribe and Save" mit allen
     Frequenzen und Rabatten
   - Widget-Einstellungen, Kundenportal-Einstellungen, Dunning/
     Zahlungsfehler-Regeln, E-Mail-Benachrichtigungen
   - Gibt es aktive Abo-Verträge (Subscriptions/Contracts)? Wie viele?

3. Discounts (Rabatte)
   - Alle Einträge mit Name, Typ, Status, Kombinierbarkeit

4. Apps (Übersicht)
   - Liste ALLER installierten Apps mit Namen

AUSGABE:
- Ein zusammenhängendes Markdown-Dokument, nach den vier Punkten oben gegliedert,
  mit Tabellen für alles, was Werte hat.
- Mach zusätzlich von jeder Konfigurationsseite einen Screenshot.
- Schreib ausdrücklich dazu, wenn du eine Seite nicht öffnen konntest.
```

---

## Prompt B — Setup nachbauen (im NEUEN Store ausführen)

Vorher: Theme-ZIP im neuen Store hochgeladen und veröffentlicht. Die Werte unten
stammen aus der API-Analyse (`docs/veilkind-loop-kaching.md`); ergänze die
Bundle-Details aus dem Ergebnis von Prompt A, wo `[aus Prompt A]` steht.

```text
Du arbeitest im Shopify-Admin meines NEUEN Stores. Ich baue ein Setup nach, das
auf meinem alten Store veilkind.com lief: Loop Subscriptions liefert die Abos,
Kaching Bundle Quantity Breaks liefert die Bundle-Auswahl auf der Produktseite.

REGELN:
- Arbeite die Schritte streng der Reihe nach ab. Die Reihenfolge ist wichtig:
  Kaching kann nur Selling Plans verknüpfen, die vorher schon existieren.
- Nach jedem Schritt: prüfe das Ergebnis und berichte mir, bevor du weitermachst.
- Wenn ein Feld nicht existiert oder anders heißt als beschrieben, rate NICHT —
  beschreib mir, was du siehst, und frag.
- Lösche nichts und deinstalliere nichts.

SCHRITT 1 — Loop Subscriptions installieren
Installiere die App "Loop Subscriptions" aus dem Shopify App Store.

SCHRITT 2 — Selling Plan anlegen
Lege in Loop eine Selling-Plan-Gruppe exakt so an:
  Name / Merchant-Code : Subscribe and Save
  Options-Label        : Frequency
  Plan 1: "Deliver every month"    – Lieferung alle 1 Monat,  10 % Rabatt
  Plan 2: "Deliver every 3 months" – Lieferung alle 3 Monate, 10 % Rabatt
  Plan 3: "Deliver every 5 months" – Lieferung alle 5 Monate, 10 % Rabatt
Wichtig: Abrechnungsintervall = Lieferintervall (KEIN Prepaid). Rabatt ist
prozentual, nicht als fixer Betrag. Einmalkauf muss weiterhin erlaubt sein.

SCHRITT 3 — Plan zuweisen und prüfen
Weise die Gruppe meinem Produkt zu — und stell sicher, dass sie auch an der
VARIANTE hängt, nicht nur am Produkt. Öffne danach das Produkt im Admin und
bestätige mir, dass unter "Purchase options" die Gruppe "Subscribe and Save"
steht. Wenn nicht, stopp und sag es mir.

SCHRITT 4 — Kaching installieren und App-Embed aktivieren
Installiere "Kaching Bundle Quantity Breaks". Geh dann in
Online Store → Themes → Anpassen → App-Einbettungen und aktiviere die
Kaching-Bundles-Einbettung. Ohne diesen Schritt rendert das Widget nicht.

SCHRITT 5 — Bundle anlegen
Lege ein Bundle mit diesen Optionen an:
  [aus Prompt A: Optionen, Mengen, Rabatte, Titel, Badges, Farben]
Aktiviere in der Bundle-Konfiguration die Subscription-Option und wähle den
Loop-Plan "Subscribe and Save" aus.
Platzierung: das Widget soll auf der Produktseite zwischen dem Preisblock
(.shop-product-price-block) und dem Add-to-Cart-Button (.shop-add-to-cart-button)
erscheinen.

SCHRITT 6 — Rabatt prüfen
Öffne Discounts. Es muss ein automatischer Rabatt "Kaching Bundles - Bundle #…"
existieren und AKTIV sein. Sag mir Name und Status. Prüfe außerdem die
Kombinierbarkeit, damit sich Kaching-Mengenrabatt und Loop-Abo-Rabatt nicht
gegenseitig ausschließen.

SCHRITT 7 — Produkt-Template anpassen
Geh in den Theme-Editor auf das Produkt-Template und DEAKTIVIERE (nicht löschen)
diese Blöcke, damit sie nicht mit dem Kaching-Widget konkurrieren:
  - den Varianten-Picker (simple_variant_picker)
  - den Mengenwähler (quantity_selector)
  - das Textlabel "Choose your supply"
Speichern.

SCHRITT 8 — Testen und berichten
Öffne die Produktseite im Storefront und prüfe:
  a) Bundle-Auswahl wechseln → aktualisieren sich Preis, Streichpreis und der
     Text im Add-to-Cart-Button?
  b) Abo-Option wählen und in den Warenkorb legen → steht der Plan-Name
     ("Deliver every month" o. ä.) beim Artikel im Warenkorb/Cart-Drawer?
  c) Weiter zum Checkout → greifen Mengenrabatt UND 10 % Abo-Rabatt?
  d) Ist im Cart-Drawer versehentlich ein Kaching-Widget sichtbar?
Berichte mir jeden Punkt einzeln mit Screenshot. Schließe den Checkout NICHT ab.

Was danach noch von Hand im Theme-Code nachgezogen werden muss (mach das NICHT
selbst, sag mir nur Bescheid, wenn a) oder d) nicht funktionieren): der
Glue-Code in sections/shop-product-details.liquid, assets/shop-product-details.js,
assets/product-details.js und assets/custom.css.
```
