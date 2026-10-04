Du arbeitest in meinem Shopify-Shop „Falunara“ (falunara.com). Die Apps **Kaching Bundles** und **Kaching Subscriptions** sind installiert und ihre App-Embeds im Live-Theme „OLEG - Falunara PDP (work copy)“ sind aktiv. Ziel: Auf der Produktseite von **FALUNARA Botanical Body Oil** (falunara.com/products/botanical-body-oil) soll ein Bundle-Widget mit Abo-Checkbox erscheinen, aufgebaut wie unten beschrieben und in den Farben meines Shops.

## Regeln
- Ändere **keine** Produktpreise, Vergleichspreise oder Shopify-Rabatte.
- Ändere am Theme nur das, was in Schritt 3 steht. Kein anderes Theme veröffentlichen, nichts löschen.
- Wenn ein Feld anders heißt als hier beschrieben, nimm das sinngemäß passende. Wenn du unsicher bist oder etwas Geld kostet (z. B. ein Plan-Upgrade), **halte an und frag mich**.
- Vor jedem „Save“/„Publish“ kurz prüfen, dass Preise und Texte exakt stimmen.

## Schritt 1 – Kaching Bundles: neuen Deal anlegen
Shopify Admin → Apps → Kaching Bundles → neuen Deal erstellen.
- **Deal-Name:** Falunara Body Oil – Buy 2 Get 1
- **Produkt:** FALUNARA Botanical Body Oil (nur dieses Produkt)
- **Layout:** vertikale Liste (Karten untereinander), Bild links, Titel/Text Mitte, Preis rechts

**Bar 1**
- Titel: `Buy 1`
- Menge: 1
- Preis: Standardpreis ($49.00), **kein Rabatt**, kein Streichpreis
- Untertitel: leer lassen (keine „You save“-Zeile)
- Bild: Produktbild mit 1 Flasche

**Bar 2**
- Titel: `Buy 2 Get 1 FREE`
- Menge: 3
- Preis: Gesamtpreis **$98.00** als fester Gesamtpreis („Fixed price“ / „Total price“). Nur falls das nicht geht: 33.33 % Rabatt und prüfen, dass genau $98.00 herauskommt (nicht $97.99 / $98.01) – sonst mich fragen.
- Streichpreis: $147.00 (= 3 × $49, Standard-Vergleich von Kaching)
- Badge: `Most Popular`
- **Standardmäßig ausgewählt**
- Bild: Produktbild mit 3 Flaschen (falls keins vorhanden: Hauptbild verwenden und mir Bescheid geben)
- Vorteile mit Häkchen (je eine Zeile):
  - `You save $49.00`
  - `Only $32.67 per bottle`
  - `Includes free shipping`

## Schritt 2 – Abo-Checkbox im selben Deal (Kaching Subscriptions)
Im Deal die Subscription-/„Subscribe & Save“-Option aktivieren und mit dem bestehenden Kaching-Subscriptions-Plan **„FALUNARA – Subscribe & Save“** (15 % Rabatt, Lieferung alle 30 / 60 / 90 Tage) verknüpfen.
- Darstellung: **Checkbox** in einer Box mit **gestricheltem Rahmen** (wie „Save 50% With Automatic Refills!“ bei Konkurrenz-Shops)
- Titel: `Save 15% With Automatic Refills!`
- Untertitel: `Zero Commitment, Cancel Anytime`
- Gilt für **beide** Bars (auch für das 3er-Bundle)
- Standard-Intervall: 60 days
- Checkbox standardmäßig: **nicht angehakt**

Danach in Kaching Subscriptions prüfen: Wird für dieses Produkt zusätzlich das separate Widget „Choose your purchase option“ (One-time purchase / Subscribe & Save 15%) angezeigt? Wenn ja, **dieses separate Widget für dieses Produkt ausblenden**, damit es nicht doppelt erscheint (Abo läuft nur noch über die Checkbox im Bundle).

## Schritt 3 – Design in Kaching (Farben meines Shops)
| Element | Wert |
|---|---|
| Schrift | Theme-Schrift übernehmen (Bricolage Grotesque) |
| Hintergrund normale Karte | `#FFFFFF` |
| Rahmen normale Karte | `#E7DFD2`, 1–1.5 px |
| Hintergrund ausgewählte Karte | `#FDF6E3` |
| Rahmen ausgewählte Karte | `#C99506`, 2 px |
| Ecken-Radius Karten | 12 px |
| Badge „Most Popular“ Hintergrund | `#C99506` |
| Badge-Text | `#241F1A`, fett |
| Titel & Preis | `#241F1A`, fett |
| Untertitel / Vorteile | `#5C534A` |
| Häkchen | `#C99506` |
| Streichpreis | `#9A9187` |
| Abo-Box Rahmen (gestrichelt) | `#C99506`, 2 px dashed |
| Abo-Box Hintergrund | `#FBF8F3` |
| Checkbox (angehakt) | Rahmen + Haken `#C99506` |

Deal speichern und aktivieren.

## Schritt 4 – Widget ins Theme setzen
Online Store → Themes → „OLEG - Falunara PDP (work copy)“ → **Customize** → Produkt-Template (Default product) öffnen.
- In der Haupt-Section (Produktdetails) → **Add block** → Apps → **Kaching Bundles** einfügen.
- Den Block **direkt über den Block „Add to cart“** ziehen.
- Das bestehende Theme-Block „Quantity break“ / „bundles“ muss **ausgeblendet** bleiben.
- Speichern.

## Schritt 5 – Prüfen und mir berichten
Öffne falunara.com/products/botanical-body-oil und prüfe:
1. Bar 2 ist vorausgewählt und zeigt **$98.00**, durchgestrichen **$147.00**, Badge „Most Popular“, die 3 Häkchen-Zeilen.
2. Bar 1 zeigt **$49.00** ohne Streichpreis.
3. Darunter die gestrichelte Abo-Box „Save 15% With Automatic Refills!“, nicht angehakt. Beim Anhaken sinken die Preise um 15 %.
4. Das alte Widget „Choose your purchase option“ ist nicht mehr doppelt zu sehen.
5. Bar 2 in den Warenkorb legen (ohne Abo) → Warenkorb zeigt 3 Flaschen für **$98.00**. Danach den Warenkorb wieder leeren. **Nicht** zur Kasse gehen.

Schick mir am Ende eine kurze Liste: was erledigt ist, was abweicht, und einen Screenshot der Produktseite.
