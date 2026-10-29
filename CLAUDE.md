# RINGANI – Shopify Theme (Shop-aufbau)

## Was dieses Projekt ist
Shopify Online Store 2.0 Produktseite für den **RINGANI Smart Ring**.
Alle Dateien sind theme-neutral und namespaced mit `ringani-*`, damit sie in
ein bestehendes Dawn-Theme eingebaut werden können ohne es zu überschreiben.

## Dateistruktur
```
sections/     → Shopify Liquid Sections (jede = eigener Block im Theme-Editor)
snippets/     → Wiederverwendbare Liquid-Hilfsdateien
assets/       → ringani.css (Design-Tokens) + ringani-product.js (Varianten-Logik)
templates/    → product.ringani.json (Section-Reihenfolge)
```

## Sections im Überblick
| Datei | Zweck |
|---|---|
| `ringani-product-main` | Kaufbereich: Galerie, Preis, Varianten, ATC, Sticky-Bar |
| `ringani-statement` | Zentriertes Statement (Hero dunkel / "Kein Abo" hell) |
| `ringani-feature-rows` | Abwechselnde Bild/Text-Reihen |
| `ringani-app-showcase` | App-Screens |
| `ringani-insights` | Kennzahl-Karten |
| `ringani-image-banner` | Full-Bleed-Banner mit Overlay + Stats |
| `ringani-split` | Text/Bild mit Kennzahlen |
| `ringani-everyday` | Alltags-Kacheln |
| `ringani-comparison` | Vergleichstabelle |
| `ringani-steps` | "So funktioniert's" – nummerierte Schritte |
| `ringani-in-the-box` | Lieferumfang |
| `ringani-specifications` | Technische Daten (Akkordeon) |
| `ringani-reviews` | Bewertungen |
| `ringani-faq` | FAQ-Akkordeon |
| `ringani-services` | Service-Zusagen |
| `ringani-final-cta` | Finaler Hero-CTA |

## Konventionen (immer einhalten)
- **Namespace:** Alle CSS-Klassen, Liquid-Variablen und IDs beginnen mit `ringani-`
- **Design-Tokens:** Farben/Abstände immer über CSS-Variablen aus `ringani.css` (`:root` Block)
- **Schema:** Jede Section hat `{% schema %}` mit `name`, `settings` Array und `presets`
- **Snippets nutzen:** Bilder immer über `ringani-image.liquid`, Media über `ringani-media.liquid`
- **Section-Vars:** Abstands- und Farb-CSS-Variablen immer über `ringani-section-vars.liquid`
- **Kein hartes CSS:** Keine Inline-Styles, keine `!important` ohne Grund
- **A11y:** Echte `<button>` Tags, `aria-*` Attribute, Alt-Texte bei Bildern
- **Performance:** `loading="lazy"` unter dem Fold, erstes Bild `eager`, kein externes JS

## Haupt-Design-Tokens (aus ringani.css)
```css
--ringani-text: #0E0E0E
--ringani-accent: #1B6FD4
--ringani-btn-from: #2C86EC  → --ringani-btn-to: #1257B4
--ringani-surface: #FBFAF8
--ringani-line: #E8E5DF
--ringani-page-width: 1280px
```

## Breakpoints
- Mobile: unter 750px
- Desktop: ab 750px (Dawn-Konvention)

## Wichtige Infos
- Keine Fremd-Libraries (kein jQuery, kein Alpine, kein GSAP)
- JS ist `defer` geladen, kein `type="module"` außer für Theme-Events-Bridge
- Cart-Integration: echtes `cart/add.js`, kompatibel mit Dawn Cart-Drawer
- Produktoptionen: "Farbe" und "Größe" (Namen sind über Section-Settings änderbar)
