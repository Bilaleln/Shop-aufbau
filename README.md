# RINGANI – Shopify Produktseite (Online Store 2.0)

Konvertierung des HTML-Designs `RINGANI Produktseite.dc.html` in ein echtes,
natives Shopify-Produkt-Template. Kein „Custom-Liquid-Block", keine einzelne
Riesen-Section – jede sichtbare Einheit des Designs ist eine eigene,
im **Theme-Editor** bearbeitbare Shopify-Section mit Blöcken, Schema-Settings
und Presets. Der Kaufbereich nutzt **echte Produkt-, Varianten- und
Preisdaten** von Shopify.

> Diese Dateien sind bewusst **theme-neutral** (Dawn-kompatibel) und
> namespaced (`ringani-*`), damit sie sich in ein bestehendes OS-2.0-Theme
> einfügen, ohne vorhandene Funktionen zu überschreiben.

---

## 1. Dateien

```
templates/
  product.ringani.json          OS-2.0-Produkt-Template (Section-Reihenfolge + Inhalte)
sections/
  ringani-product-main.liquid   Kaufbereich: Galerie, Preis, Varianten, ATC, Sticky-Bar, Größen-Modal
  ringani-statement.liquid      Zentriertes Statement (Hero dunkel / "Kein Abo" hell)
  ringani-feature-rows.liquid   Abwechselnde Bild/Text-Reihen (Schlaf/Erholung/Aktivität)
  ringani-app-showcase.liquid   App-Screens
  ringani-insights.liquid       Kennzahl-Karten (Score + Balken)
  ringani-image-banner.liquid   Full-Bleed-Lifestyle-Banner mit Overlay + Stats (Komfort)
  ringani-split.liquid          Text/Bild mit Kennzahlen (Akku)
  ringani-everyday.liquid       Alltags-Kacheln (Wasserbeständigkeit)
  ringani-comparison.liquid     Vergleichstabelle
  ringani-steps.liquid          So funktioniert's (nummerierte Schritte)
  ringani-in-the-box.liquid     Lieferumfang
  ringani-specifications.liquid Technische Daten (Akkordeon: Gruppen + Zeilen)
  ringani-reviews.liquid        Bewertungen (+ @app-Block für Review-Apps)
  ringani-faq.liquid            FAQ-Akkordeon (+ FAQ-Rich-Snippet)
  ringani-services.liquid       Service-Zusagen
  ringani-final-cta.liquid      Finaler Hero-CTA
snippets/
  ringani-media.liquid          Rendert product.media (image/video/external/model)
  ringani-image.liquid          Rendert image_picker + optionales Mobil-Bild + Fallback
  ringani-section-vars.liquid   Abstands-/Farb-CSS-Variablen pro Section
assets/
  ringani.css                   Design-Tokens + geteilte Komponenten-Styles
  ringani-product.js            Varianten-Logik, Galerie, Akkordeons, Sticky-Bar, Warenkorb
```

---

## 2. HTML-Komponente → Shopify-Architektur (Mapping)

| HTML-Abschnitt | Shopify-Umsetzung | Daten/Blöcke |
|---|---|---|
| Produkt-Hero (Galerie + Kaufbox) | `ringani-product-main` | `product.media`, `product.variants`, Preis, Blöcke: `benefit`, `panel`, `size_row` |
| „Gesundheit beginnt…" / „Kein Abo" | `ringani-statement` (2×) | Settings + `image_picker` |
| Schlaf/Erholung/Aktivität | `ringani-feature-rows` | Block `feature` (Bild, Text, Punkte) |
| App-Screens | `ringani-app-showcase` | Block `screen` |
| Insight-Karten | `ringani-insights` | Block `insight` |
| „Gemacht, um ihn zu vergessen" | `ringani-image-banner` | Block `stat` |
| Akku | `ringani-split` | Block `stat` |
| Alltag/Wasser | `ringani-everyday` | Block `tile` |
| Vergleich | `ringani-comparison` | Block `row` |
| So funktioniert's | `ringani-steps` | Block `step` |
| Lieferumfang | `ringani-in-the-box` | Block `item` |
| Technische Daten | `ringani-specifications` | Blöcke `group` + `row` |
| Bewertungen | `ringani-reviews` | Block `review` + `@app` |
| FAQ | `ringani-faq` | Block `faq` |
| Service-Zusagen | `ringani-services` | Block `service` |
| Finaler CTA | `ringani-final-cta` | Settings + `image_picker` |
| Header / Ankündigungsbar / Footer / Warenkorb-Drawer / Mobile-Nav | **Theme-global** – bleibt beim bestehenden Theme | – |

Die globale Chrome (Header, Ankündigungsbar, Footer, Cart-Drawer, mobile
Navigation) ist bewusst **nicht** nachgebaut: Sie gehört zum Theme-Layout und
wird über die vorhandenen globalen Sections gesteuert. `ringani-product.js`
integriert sich mit dem **vorhandenen** Cart-Drawer (siehe §5).

---

## 3. Installation

Da hier kein komplettes Theme, sondern die RINGANI-Erweiterung liegt, werden
die Dateien in ein bestehendes OS-2.0-Theme (z. B. Dawn) übernommen:

**Variante A – Shopify CLI**
```bash
# In einer Kopie deines Themes (unveröffentlicht!):
cp -r assets/* <theme>/assets/
cp -r sections/* <theme>/sections/
cp -r snippets/* <theme>/snippets/
cp templates/product.ringani.json <theme>/templates/
shopify theme push --unpublished --theme "RINGANI (Dev)"
```

**Variante B – Admin (Code-Editor eines duplizierten Themes)**
1. Online Store → Themes → aktives Theme **duplizieren** (nicht veröffentlichen).
2. Im Duplikat: Dateien aus `assets/`, `sections/`, `snippets/`, `templates/`
   an gleicher Stelle anlegen/einfügen.

**Template dem Produkt zuweisen**
- Produkt „RINGANI Smart Ring" → Admin → **Theme-Template** → `ringani` wählen,
  **oder** im Theme-Editor oben das Template `product.ringani` auswählen.

---

## 4. Produktdaten in Shopify (einmalig)

Damit Farb- und Größenauswahl echt funktionieren, braucht das Produkt zwei
Optionen mit exakt diesen Namen (im Section-Setting änderbar):

- **Farbe** → z. B. Schwarz, Silber, Gold
- **Größe** → z. B. 6, 7, 8, 9, 10, 11, 12, 13

Die Farbfelder nutzen automatisch Shopifys **native Optionswert-Swatches**
(Farbe/Bild). Ohne Swatch greift ein Namens-Fallback
(Schwarz/Silber/Gold/Blau). Ausverkaufte Kombinationen werden aus dem echten
Lagerbestand ausgegraut – nichts ist hartkodiert.

Preis, Vergleichspreis und die berechnete Ersparnis kommen aus der Variante
(`variant.price`, `variant.compare_at_price`).

---

## 5. Warenkorb-Integration

`ringani-product.js` sendet ein echtes `cart/add.js` und arbeitet mit dem
Theme zusammen:

1. **Dawn-kompatibel:** Ist ein `<cart-drawer>` (oder `<cart-notification>`)
   vorhanden, werden dessen Sections neu gerendert und der Drawer geöffnet.
2. **Fallback (Setting „Nach dem Hinzufügen"):** Warenkorb-Seite öffnen oder
   auf der Seite bleiben (kurzer Hinweis-Toast) + Cart-Bubble aktualisieren.
3. Zusätzlich werden `cart:refresh` / `cart:build` Events ausgelöst, auf die
   viele Themes reagieren.

Haupt-Button und Sticky-Leiste teilen sich **einen** Varianten-Zustand.

> Für exotische Themes können die Ziel-Section-IDs in
> `themeSections()` / `replaceSection()` angepasst werden.

---

## 6. Dynamic Sources & Metafields (empfohlen, optional)

Seiten-Präsentation → **Theme-Editor-Setting**. Produktspezifische Fakten →
**Produktdaten/Metafelder** (per „Dynamische Quelle einbinden" im Editor
verknüpfbar). Sinnvolle Metafelder für RINGANI:

- `custom.battery_life`, `custom.charging_time`, `custom.material`,
  `custom.weight`, `custom.water_resistance`, `custom.compatibility`,
  `custom.sensors`
- Textfelder in Statement/Split/Spezifikationen unterstützen dynamische
  Quellen (Product-/Metafield-Bindung) direkt im Editor.

Es wurden **keine** Metafelder automatisch angelegt – die Standardinhalte
stehen als Section-/Block-Settings bereit und lassen sich bei Bedarf auf
Metafelder umstellen.

---

## 7. Qualität

- **Responsive** (Mobile-first, keine horizontale Überlauf-Scrollleiste),
  Breakpoints an Dawn-Konvention (749/750px).
- **A11y:** echte `<button>`, `aria-pressed/expanded/controls`, Fokus-Stile,
  Tastatur-Akkordeons, Alt-Texte.
- **Performance:** responsive `image_url`/`image_tag`, `loading="lazy"` unter
  dem Fold, erstes Galeriebild eager; JS `defer`, keine Fremd-Libraries.
- **Motion:** `prefers-reduced-motion` respektiert.
- **SEO:** genau ein `<h1>` (Produkttitel), FAQ-Rich-Snippet optional.
- **Theme-Editor-robust:** Custom Elements upgraden bei Section-Reload
  (`shopify:section:load`).

---

## 8. Offene Punkte / Hinweise

- **Bilder:** Alle Marketing-Bilder sind über `image_picker` austauschbar; die
  Produktgalerie nutzt `product.media`. Ohne Bilder erscheinen Platzhalter.
- **Bewertungen:** Die eingebauten Karten sind als **Demo** gekennzeichnet.
  Für echte Bewertungen die Review-App als `@app`-Block in „RINGANI –
  Bewertungen" hinzufügen.
- **Veröffentlichen:** Nur in einem **unveröffentlichten** Dev-Theme testen und
  erst nach deiner Freigabe live schalten.
