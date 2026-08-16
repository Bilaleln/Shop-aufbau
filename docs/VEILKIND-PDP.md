# VEILKIND — Milk Thistle PDP (theme: CLAUDE CODE ELIXIER)

A dedicated product page built **inside the existing Elixier section system**. No new
section files were created; every part of the page is an existing Elixier section,
configured and restyled through a new product template.

- **Theme:** `CLAUDE CODE ELIXIER` (`gid://shopify/OnlineStoreTheme/203450876247`) — left **unpublished**.
- **Template:** `templates/product.milk-thistle.json`
- **Brand accent:** `#3ab6e4` · Ink: `#12304a` · Soft surface: `#f7fbfd` · Pale brand tint: `#eaf8fd`

## Preview

The product's `templateSuffix` was deliberately **not** changed, because that field is
store-wide and the live theme (Horizon) has no `product.milk-thistle` template. Preview
without touching the live store:

```
https://0vmyhz-pn.myshopify.com/products/placeholder-product?view=milk-thistle&preview_theme_id=203450876247
```

When you publish, set the product's theme template to **milk-thistle** (Product → Online
store → Theme template).

## Section map

| # | Page block | Elixier section (existing) | Notes |
|---|---|---|---|
| 1 | Trust bar | `scrolling-features-bar` | 4 messages, navy bar, brand-blue icons |
| 2 | Hero / buy box | `shop-product-details` | 17 existing blocks, see below |
| 3 | Risk reversal | `guarantee_badges` + `custom_money_back` blocks | inside the buy box |
| 4 | UGC videos | `customer-reviews` *(extended)* | 4 vertical 9:16 clips, swipeable |
| 5 | Why it works | `product-benefits` | 4 explanation blocks + product image |
| 6 | Ingredients | `alternating-features` | 4 ingredient cards w/ macro photos |
| 7 | Formula facts | `statistics-grid` | 4 rings — **unmodified section** |
| 8 | Emotional lifestyle | `image-with-text` | wide lifestyle shot + CTA |
| 9 | Customer journey | `steps` | 3 stages, routine-framed |
| 10 | Testimonials | `customer-reviews-carousel` | **placeholder cards** |
| 11 | Comparison | `product-comparison` | 6 rows, our column brand-tinted |
| 12 | Guarantee | `satisfaction-guarantee` | 90-day risk reversal |
| 13 | FAQ | `store-faq` | 8 questions |
| 14 | Final CTA | `featured-product-details` | real product, price, variants, ATC |
| 15 | Sticky ATC | `sticky-add-to-cart` | brand blue, delivery-date estimate off |

Buy-box block order: `custom_liquid` (loads the PDP stylesheet) → `title` → `unique_rating`
→ `custom_text` → `product_labels` → `divider` → `price` → `benefits_grid` → `divider` →
`custom_text` → `simple_variant_picker` → `quantity_selector` → `add_to_cart` →
`payment_icons` → `guarantee_badges` → `custom_money_back` → `product_faq`.

## Files changed

| File | Change |
|---|---|
| `templates/product.milk-thistle.json` | **New** template (the whole PDP) |
| `assets/veilkind-pdp.css` | **New** asset, loaded only by this template |
| `sections/customer-reviews.liquid` | Extended: optional video per card, poster image, tap-to-unmute, viewport-gated playback, `enable_autoscroll` + `card_radius` settings |
| `assets/customer-reviews-slider.js` | Honours `data-autoscroll="false"` (swipe instead of marquee); now initialises every slider on the page rather than only the first |

Both `customer-reviews` changes are backward compatible — existing usages keep the marquee
and image-only rendering because the new settings default to the old behaviour.

**Deliberately not touched:** `templates/product.json`, `sections/statistics-grid.liquid`,
`layout/theme.liquid`, `config/settings_data.json`, `sections/header-group.json`, and every
other section. The live theme and the other duplicated themes were never written to.

## Loop (subscriptions / bundles)

**No bundle or subscription logic was implemented.** Specifically:

- No bundle or subscription app was installed.
- The theme's `quantity_break` block (its built-in bundle selector, with hardcoded
  "1/2/3-Month Supply" cards and custom prices) is **not used** on this template.
- The purchase area is a plain `simple_variant_picker` + `quantity_selector` +
  `add_to_cart`, driven by the product's real Shopify variants (1 / 3 / 6 Bottles).
- `assets/veilkind-pdp.css` reserves a `.vk-loop-slot` hook in the buy box for the
  Loop widget.

## Generated media (Higgsfield)

All uploaded to Shopify Files. Images used the existing product packshot as a reference
input so the bottle, label, cap and proportions stay identical across every asset.

Images (`marketing_studio_image`, 2K): `veilkind-hero-packshot`,
`veilkind-bottle-with-ingredients`, `veilkind-lifestyle-kitchen`,
`veilkind-bottle-capsules-detail`, `veilkind-ingredient-milk-thistle`,
`veilkind-ingredient-turmeric`, `veilkind-ingredient-artichoke`,
`veilkind-ingredient-inositol`, `veilkind-lifestyle-wide`, `veilkind-journey-step-1..3`,
`veilkind-bottle-white-cutout`, `veilkind-ugc-poster-1..4`.

Videos (`seedance_2_0`, 9:16, 5s, 720p, silent): `veilkind-ugc-1..4.mp4` — man in a
kitchen, woman's morning routine, man showing the bottle, and product b-roll.

Videos were uploaded as **generic files**, not Shopify `Video` objects, because the Admin
API only accepts a remote URL for images and generic files (videos require a staged
upload). The UGC section therefore takes a video **URL** per card. If you later re-upload
the MP4s through Content → Files in admin, they become native videos and you can switch
the block to a video picker.

The clips are intentionally **silent** — no spoken testimonials, so nothing implies a
health outcome, and four autoplaying clips cost far less bandwidth.

## Confirm before publishing

These are the only claims on the page that could not be verified against store data. Each
is either bracketed on the page or noted here.

**Bracketed on the page (search for `[`):**

1. `[4.8]` and `[REVIEW COUNT]` — appear in the hero rating, UGC section, testimonials,
   final CTA and sticky bar. No review app or review metafields were found on the store,
   so no rating was invented. Connect your review app or replace these.
2. `[SERVING SIZE]` — buy-box FAQ and FAQ #4.
3. `[CAPSULE COUNT]` / `[X]` days — FAQ #5. The `custom.servings` metafield is still
   `[NUMBER OF SERVINGS]`.
4. Testimonial cards are explicit `[PLACEHOLDER …]` text. **Do not publish that section
   until real reviews are in.**

**Not bracketed — taken from your brief, but unverified against the label:**

5. **Vegetarian capsules** — used in a hero pill, a comparison row, a formula-fact ring
   and FAQ #6. Confirm with your manufacturer.
6. **90-day money-back guarantee** — trust bar, guarantee badges, money-back card,
   guarantee section, comparison row, FAQ #8.
7. **Free U.S. shipping** — trust bar, guarantee badges, final CTA. Confirm your shipping
   zones; the store's currency is EUR and its address is in Germany, so this needs a real
   U.S. shipping profile behind it.
8. **"One capsule, once a day"** — final-CTA bullet and "One step, once a day" in the
   why-it-works section. Confirm the serving size; if it is two capsules, change both.
9. **Comparison column "Typical alternatives"** — the right-hand values ("Varies",
   "Often gelatin", "30 days typical") are general market statements, not claims about a
   named competitor. Keep it that way.

**Verified from the store**, so used as hard claims: milk thistle standardized to **80%
silymarin**, plus **turmeric, artichoke and inositol** — this came from the copy already in
your theme's `product-benefits` section.

## Other things you may want to do

- The product record is still a placeholder: title `Vei`, vendor `[BRAND NAME]`, empty
  description, and `custom.benefits` / `custom.usage_instructions` metafields full of
  placeholders. The PDP works around this with a custom title ("Milk Thistle Complex"), but
  the real product record should be filled in — it drives SEO, cart and checkout.
- The global announcement bar (`custom-announcement-bar`, "LIMITED TIME: SAVE UP TO 48%")
  is red `#ef4a65` and lives in the shared header group, so it renders on every page. It
  was left alone rather than restyled store-wide. One colour change in the theme editor
  will bring it in line with `#3ab6e4`.
- `settings_data.json` has `global_section_button_color: #3AB6E4` but
  `use_dedicated_button_colors: false`, so global buttons still fall back to the dark
  accent. Every CTA on this template sets its own brand-blue colour, so the PDP is correct
  either way; flipping that global switch would brand the rest of the store too.
