# veilkind-snapshot — Teil-Sicherung des Themes „CLAUDE CODE ELIXIER"

Ausgelesen am 02.09.2026 aus dem Live-Store `veilkind.com` (Haupt-Theme
`gid://shopify/OnlineStoreTheme/203450876247`), bevor der Store gelöscht wird.

**Das ist ausdrücklich KEINE vollständige Theme-Sicherung.** Hier liegen nur die
Dateien, die für die Loop-×-Kaching-Integration und die Produktseite relevant
sind — keine Bilder, keine Übersetzungen, nicht alle Sections/Snippets.

➡ Für eine vollständige Sicherung im Admin
*Online Store → Themes → … → Theme-Datei herunterladen* nutzen (ZIP per E-Mail,
inkl. aller Assets). Das bitte für **alle** Themes machen, nicht nur das
Haupt-Theme.

## Was hier drin steckt

| Datei | Warum |
|---|---|
| `sections/shop-product-details.liquid` | Haupt-Section der Produktseite, enthält den Kaching-Glue-Code (Z. 211–263) |
| `assets/shop-product-details.js`, `assets/product-details.js` | ATC-Button-Umschrift auf Kaching-Klick (dublizierter Code) |
| `assets/custom.css` | blendet `kaching-bundle` im Cart-Drawer aus (Z. 129) |
| `templates/product.milk-thistle.json` | aktives Produkt-Template, Varianten-/Mengen-Blöcke deaktiviert |
| `templates/product.json` | älteres Template mit theme-eigenem Quantity-Break |
| `snippets/quantity-break.liquid` | der theme-eigene Bundle-Selector (ohne Abo-Logik) |
| `snippets/product-info.liquid` | rendert die Blöcke der Produktseite |
| `snippets/cart-drawer.liquid`, `sections/main-cart-items.liquid` | zeigen den Selling-Plan-Namen im Warenkorb |
| `config/settings_data.json` | enthält das aktivierte Kaching-App-Embed |
| übrige Dateien | Kontext (Buy-Buttons, Variant-Picker, Sticky-ATC, Cart-JS) |

Die Auswertung dazu: [`../docs/veilkind-loop-kaching.md`](../docs/veilkind-loop-kaching.md)
