# RINGANI – Shopify Product Page (Online Store 2.0)

Conversion of the HTML design `RINGANI Produktseite.dc.html` into a real,
native Shopify product template built for the US market. No "Custom Liquid
block", no single giant section – every visible unit of the design is its own
Shopify section, editable in the **theme editor**, with blocks, schema settings
and presets. The buy box uses **real product, variant and price data** from
Shopify.

> These files are intentionally **theme-neutral** (Dawn-compatible) and
> namespaced (`ringani-*`) so they can be dropped into an existing OS 2.0
> theme without overriding existing functionality.

---

## 1. Files

```
templates/
  product.ringani.json          OS 2.0 product template (section order + content)
sections/
  ringani-product-main.liquid   Buy box: gallery, price, variants, ATC, sticky bar, size modal
  ringani-statement.liquid      Centered statement (dark hero / light "No Subscription")
  ringani-feature-rows.liquid   Alternating image/text rows (Sleep/Recovery/Activity)
  ringani-app-showcase.liquid   App screens
  ringani-insights.liquid       Metric cards (score + bar)
  ringani-image-banner.liquid   Full-bleed lifestyle banner with overlay + stats (comfort)
  ringani-split.liquid          Text/image with stats (battery)
  ringani-everyday.liquid       Everyday tiles (water resistance)
  ringani-comparison.liquid     Comparison table
  ringani-steps.liquid          How it works (numbered steps)
  ringani-in-the-box.liquid     What's in the box
  ringani-specifications.liquid Specifications (accordion: groups + rows)
  ringani-reviews.liquid        Reviews (+ @app block for review apps)
  ringani-faq.liquid            FAQ accordion (+ FAQ rich snippet)
  ringani-services.liquid       Service promises
  ringani-final-cta.liquid      Final hero CTA
snippets/
  ringani-media.liquid          Renders product.media (image/video/external/model)
  ringani-image.liquid          Renders image_picker + optional mobile image + fallback
  ringani-section-vars.liquid   Per-section spacing/color CSS variables
assets/
  ringani.css                   Design tokens + shared component styles
  ringani-product.js            Variant logic, gallery, accordions, sticky bar, cart
```

---

## 2. HTML Component → Shopify Architecture (Mapping)

| HTML section | Shopify implementation | Data/blocks |
|---|---|---|
| Product hero (gallery + buy box) | `ringani-product-main` | `product.media`, `product.variants`, price, blocks: `benefit`, `panel`, `size_row` |
| "Better health starts…" / "No Subscription" | `ringani-statement` (2×) | Settings + `image_picker` |
| Sleep/Recovery/Activity | `ringani-feature-rows` | Block `feature` (image, text, points) |
| App screens | `ringani-app-showcase` | Block `screen` |
| Insight cards | `ringani-insights` | Block `insight` |
| "Made to be forgotten" | `ringani-image-banner` | Block `stat` |
| Battery | `ringani-split` | Block `stat` |
| Everyday/water | `ringani-everyday` | Block `tile` |
| Comparison | `ringani-comparison` | Block `row` |
| How it works | `ringani-steps` | Block `step` |
| What's in the box | `ringani-in-the-box` | Block `item` |
| Specifications | `ringani-specifications` | Blocks `group` + `row` |
| Reviews | `ringani-reviews` | Block `review` + `@app` |
| FAQ | `ringani-faq` | Block `faq` |
| Service promises | `ringani-services` | Block `service` |
| Final CTA | `ringani-final-cta` | Settings + `image_picker` |
| Header / announcement bar / footer / cart drawer / mobile nav | **Theme-global** – stays with the existing theme | – |

The global chrome (header, announcement bar, footer, cart drawer, mobile
navigation) is intentionally **not** rebuilt: it belongs to the theme layout
and is controlled through the existing global sections. `ringani-product.js`
integrates with the **existing** cart drawer (see §5).

---

## 3. Installation

Since this repo contains the RINGANI extension rather than a complete theme,
the files are copied into an existing OS 2.0 theme (e.g. Dawn):

**Option A – Shopify CLI**
```bash
# In a copy of your theme (unpublished!):
cp -r assets/* <theme>/assets/
cp -r sections/* <theme>/sections/
cp -r snippets/* <theme>/snippets/
cp templates/product.ringani.json <theme>/templates/
shopify theme push --unpublished --theme "RINGANI (Dev)"
```

**Option B – Admin (code editor of a duplicated theme)**
1. Online Store → Themes → **duplicate** the active theme (do not publish).
2. In the duplicate: create/paste the files from `assets/`, `sections/`,
   `snippets/`, `templates/` in the same locations.

**Assign the template to the product**
- Product "RINGANI Smart Ring" → Admin → **Theme template** → choose `ringani`,
  **or** select the `product.ringani` template at the top of the theme editor.

---

## 4. Product Data in Shopify (one-time setup)

For color and size selection to work properly, the product needs two options
with exactly these names (changeable in the section settings):

- **Color** → e.g. Black, Silver, Gold
- **Size** → e.g. 6, 7, 8, 9, 10, 11, 12, 13 (US ring sizes)

The color swatches automatically use Shopify's **native option value swatches**
(color/image). Without a swatch, a name-based fallback kicks in
(Black/Silver/Gold/Blue; legacy German names are still recognized). Sold-out
combinations are grayed out based on real inventory – nothing is hardcoded.

Price, compare-at price and the calculated savings come from the variant
(`variant.price`, `variant.compare_at_price`) and are shown in the store
currency (USD).

---

## 5. Cart Integration

`ringani-product.js` sends a real `cart/add.js` request and works together with
the theme:

1. **Dawn-compatible:** If a `<cart-drawer>` (or `<cart-notification>`) is
   present, its sections are re-rendered and the drawer is opened.
2. **Fallback (setting "After adding"):** open the cart page or stay on the
   page (short toast notice) + update the cart bubble.
3. Additionally, `cart:refresh` / `cart:build` events are dispatched, which
   many themes listen for.

The main button and the sticky bar share **one** variant state.

> For unusual themes, the target section IDs can be adjusted in
> `themeSections()` / `replaceSection()`.

---

## 6. Dynamic Sources & Metafields (recommended, optional)

Page presentation → **theme editor setting**. Product-specific facts →
**product data/metafields** (connectable via "Connect dynamic source" in the
editor). Useful metafields for RINGANI:

- `custom.battery_life`, `custom.charging_time`, `custom.material`,
  `custom.weight`, `custom.water_resistance`, `custom.compatibility`,
  `custom.sensors`
- Text fields in Statement/Split/Specifications support dynamic sources
  (product/metafield binding) directly in the editor.

**No** metafields were created automatically – the default content is
provided as section/block settings and can be switched to metafields as
needed.

---

## 7. Quality

- **Responsive** (mobile-first, no horizontal overflow scrollbar),
  breakpoints follow Dawn conventions (749/750px).
- **A11y:** real `<button>` elements, `aria-pressed/expanded/controls`, focus
  styles, keyboard-accessible accordions, alt text.
- **Performance:** responsive `image_url`/`image_tag`, `loading="lazy"` below
  the fold, first gallery image eager; JS `defer`, no third-party libraries.
- **Motion:** `prefers-reduced-motion` is respected.
- **SEO:** exactly one `<h1>` (product title), optional FAQ rich snippet.
- **Theme-editor-robust:** custom elements upgrade on section reload
  (`shopify:section:load`).

---

## 8. Open Items / Notes

- **Images:** All marketing images can be swapped via `image_picker`; the
  product gallery uses `product.media`. Without images, placeholders are shown.
- **Reviews:** The built-in cards are marked as **demo** content. For real
  reviews, add your review app as an `@app` block in "RINGANI – Reviews".
- **US policies:** Shipping (free within the US, 3–5 business days), 30-day
  returns and the 1-year limited warranty are content defaults – make sure
  they match your store's actual shipping, refund and warranty policies.
- **Health claims:** RINGANI is positioned as a wellness product, not a
  medical device; keep copy free of diagnostic or treatment claims.
- **Publishing:** Test only in an **unpublished** dev theme and go live only
  after your approval.
