# FADILAL – Medienproduktion & Theme-Integration (Wild Rose)

Stand: 2026-11-05 · Shop: fadilal.com · Theme: Palo Alto 9.2.0

## Status auf einen Blick

| Bereich | Status |
|---|---|
| KI-Bilder (KIE, Nano Banana Pro) | 22 freigegeben, 5 verworfen (Label-Drift) |
| KI-Videos (KIE, Kling 3.0 pro) | 12 Clips → 3 geschnittene Videos + 4:5-Version |
| Upload Shopify Files | 22 Bilder + 4 Videos, alle `READY` (verifiziert) |
| Theme-Integration | **nur im Preview-Theme** `FADILAL PALO – Media Preview 2026-11-04` (ID 190902337916) |
| Live-Theme | **unverändert** – Veröffentlichen ist per API gesperrt und bleibt deine Entscheidung |
| Produktgalerie | Von dir parallel neu befüllt (9 eigene Bilder) – meine Ergänzungen wurden nicht erneut gesetzt |
| KIE-Kosten | **1.761,6 Credits** (Bilder 702 · Videos 1.059,6), Guthaben 9.847,55 → 8.085,95 |

Preview ansehen:
- Produktseite: https://fadilal.com/products/fadilal-warm-oil-candle?preview_theme_id=190902337916
- Startseite: https://fadilal.com/?preview_theme_id=190902337916

## A. Bilder (alle WebP, Shopify CDN, mit englischem Alt-Text)

| Datei | Format | Platzierung (Preview-Theme) |
|---|---|---|
| fadilal-wildrose-hero.webp | 1:1 2048² | Packshot (Galerie-Kandidat) |
| fadilal-wildrose-melted-oil.webp | 1:1 | PDP Social-Galerie · Startseite „Warm oil, not hot wax“ |
| fadilal-wildrose-handheld.webp | 1:1 | PDP Social-Galerie · Startseite Social 1 |
| fadilal-wildrose-melting.webp | 1:1 | PDP „Warm oil, not hot wax“ |
| fadilal-wildrose-application.webp | 1:1 | PDP „What makes it different?“ · Social |
| fadilal-wildrose-bathroom.webp | 4:5 | Slideshow (mobil) · Startseite Social 3 |
| fadilal-wildrose-bedroom.webp | 4:5 | Inhaltsstoffe „Soy wax“ · Slideshow (mobil) · Social |
| fadilal-wildrose-ingredients.webp | 1:1 | Inhaltsstoffe „Beeswax“ · Startseite Social 4 |
| fadilal-wildrose-detail.webp | 1:1 | Galerie-Kandidat |
| fadilal-how-to-1-light / 2-melt / 3-test / 4-apply.webp | 4:5 | PDP „How to use“ (4 Schritte); 2-melt auch „Coconut wax“ |
| fadilal-evening-ritual.webp | 4:5 | PDP „Your 10 minutes. Every night.“ · Slideshow (mobil) · Social |
| fadilal-wildrose-guarantee.webp | 1:1 | PDP Garantie-Sektion (ohne eingebrannten Text) |
| fadilal-wildrose-lifestyle.webp | 4:5 | Startseite Hero · PDP Social |
| fadilal-campaign-hero-desktop.webp | 16:9 | PDP Slideshow 1 · Startseite Banner (Desktop) |
| fadilal-campaign-hero-mobile.webp | 4:5 | PDP Slideshow 1 (mobil) · Startseite Banner (mobil) |
| fadilal-evening-ritual-wide / bathroom-wide / bedroom-wide / lifestyle-wide.webp | 16:9 | PDP Slideshow 2–4 (Desktop) / Reserve |

Shopify-IDs und CDN-URLs: `manifests/shopify-files.json`.

## B. Videos (H.264, 1080p, 24 fps, ohne Ton, eigene Poster)

| Datei | Dauer | Format | Shopify-ID | Einsatz |
|---|---|---|---|---|
| fadilal-product-demo.mp4 | 20,5 s | 9:16 | Video/70038570008956 | Reels/Ads, Produkt-Demo (7 Shots: Bad → anzünden → Schmelzen → aus → Fingertest → Auftragen → Beauty-Shot) |
| fadilal-product-demo-4x5.mp4 | 20,5 s | 4:5 | Video/70038569976188 | Produktgalerie (war Position 3, wurde von dir entfernt) |
| fadilal-evening-ritual.mp4 | 12,8 s | 9:16 | Video/70038570041724 | Emotionales Abendritual (Ads/Social) |
| fadilal-ugc-demo.mp4 | 9,7 s | 9:16 | Video/70038570074492 | UGC-Stil, ohne Testimonial/Lip-Sync |

## C. KIE-Modelle, Task-IDs, Kosten

- Bilder: `nano-banana-pro` (Image-to-Image mit Original-Produktfoto + freigegebenem Packshot als Referenz), 2K, 18 Credits/Bild.
- Videos: `kling-3.0/video`, mode `pro` (1080p), `sound:false`, Image-to-Video aus freigegebenen Keyframes; 60,6 Credits (3 s) / 80,8 (4 s) / 101 (5 s).
- Jede Generierung inkl. Prompt, Task-ID, Credits, Laufzeit: `manifests/kie-generations.json`.
- Verworfen nach QC (Label-/Typografie-Drift): ingredients v1, evening-woman v1, hero-wide v1, hero-mobile v1, Keyframe k3; u2 v1 (Wachs sah fest statt flüssig aus).

## D. Shopify-Uploads

Bilder per `fileCreate`, Videos per `stagedUploadsCreate` → POST → `fileCreate`; Poster per `fileUpdate.previewImageSource`. Jede Datei auf `READY` geprüft (nicht nur „UPLOADED“). Keine bestehenden Dateien gelöscht; die zwei zeitweise vom Produkt gelösten Original-Bilder liegen weiterhin in Files.

## E. Geänderte Dateien

Nur im Preview-Theme, nur JSON-Templates, kein Liquid/CSS/JS:
- `templates/product.candle.json` – 25 Bild-Settings ergänzt; Image-Accordions: `overlay_type: text`, Text unten links (Lesbarkeit).
- `templates/index.json` – 8 Bild-Settings; Hero-Bild; Banner: Text links (Desktop) / oben mittig + 750-px-Höhe (mobil).

Vorher/Nachher: `theme/before/`, `theme/after/`. Das Preview-Theme ist gleichzeitig das Backup des Live-Stands.

## F. Live oder Preview?

**Preview.** Live-Shop, Checkout, Preise, Varianten, Texte unverändert. Zum Livegang: Online Store → Themes → „FADILAL PALO – Media Preview 2026-11-04“ → Veröffentlichen. (Das zuvor aktive Theme bleibt als Fallback erhalten.)

## G. Verifikation (Playwright, Preview-Theme)

- PDP & Startseite, Desktop 1440 px und iPhone 13: 0 Platzhalter, 0 kaputte Bilder, kein horizontales Scrollen, keine JS-Fehler durch die Änderungen.
- Variantenwechsel (Provence) ✓, Add-to-Cart ✓ (Warenkorb 0 → 1, Variante korrekt).
- Screenshots & QC-Kontaktbögen: `evidence/`.

## H. Offene Punkte / Blocker

1. **Produktgalerie:** Während der Arbeit wurde die Galerie (15:48–15:50 und 16:53 UTC) extern neu befüllt; dabei wurden meine 7 Bilder und das Demo-Video wieder entfernt. Ich habe das bewusst nicht überschrieben. Bei Bedarf lassen sich Packshot, Melted-Oil, Handheld, Application, Bathroom, Ingredients, Detail und das 4:5-Video per `fileUpdate referencesToAdd` ohne Kopie wieder anhängen.
2. Theme-Writes über `themeFilesUpsert` mit URL-Body schlagen sporadisch still fehl (Job „done“, Datei unverändert) – jede Änderung wurde deshalb per MD5 gegengeprüft.
3. Mobiler Startseiten-Banner: Überschrift ist sehr groß (Size 150); „chore.“ und Button berühren den oberen Glasrand – lesbar, aber kleinere Schrift wäre ruhiger.
4. Video 3 (UGC): im zweiten Clip berührt der Finger die Öloberfläche der nicht brennenden Kerze – entspricht dem echten Wärmetest, aber vor Ads-Einsatz prüfen.

## I. Auffälligkeiten außerhalb des Medien-Scopes (nicht geändert)

- **Garantie widersprüchlich:** Galeriebild „90 Evenings“ vs. Text/Badge/FAQ „30 days“.
- Startseite: Platzhalter `[KUNDENZAHL]`, `[ANZAHL]`, `[REVIEW-HEADLINE …]`, `[ZITAT …]`, `[VORNAME N.]` mit „Verified buyer“, `[EXPERTIN …]`, `[INHALTSSTOFFE]`, `[@INSTAGRAM HANDLE]` sind live sichtbar.
- Startseiten-Links zeigen auf `/products/kerze-merze` (alter Handle) ; zwei der drei Bundle-Karten verlinken Varianten-IDs, die nicht zu diesem Produkt gehören.
- PDP: deaktivierte Custom-Code-Blöcke enthalten „50.000+ others purchased“ / „4,8/5 (42,3679 Bewertungen)“ mit Stock-Avataren – bitte nicht aktivieren, solange nicht belegt. Aktiv: „89% sold“-Balken + Countdown (Fake-Knappheit, rechtliches Risiko).
- Galerie-Bild „What to expect“ verspricht Hautveränderungen nach Wochen („Warm-Seal Method™“) – nicht belegt.
- Alle 8 Duftvarianten zeigen nur Wild-Rose-Bilder (keine Varianten-Medien zugeordnet).
- Galerie-Bilder haben keine Alt-Texte; `Image accordions` Block 4 und Slideshow-Slide 5 enthalten Theme-Demotext („Welcome to Palo Alto“, deaktiviert).
- Shop-Name in Shopify ist noch „Falunara“, Vendor „Falunara“.
