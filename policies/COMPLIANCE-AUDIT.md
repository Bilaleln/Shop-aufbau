# FALUNARA: compliance & trust audit (2026-10-05)

Operator: M and B the MBFs LLC (Florida LLC), dba FALUNARA. Domain falurana.com.
This is an operational audit, not legal advice. It does not establish compliance with any law.

## 1. Live-store changelog
| When (2026-10-05) | Object | Change |
|---|---|---|
| Session 1 | Navigation → Footer menu | Added "Contact" (→ /pages/contact) above "Search" and "Your Privacy Choices" |
| Session 2 | Product "FALUNARA Botanical Body Oil" | Vendor "Falunara" → "FALUNARA"; SEO title "Botanical Body Oil \| Falunara" → "… \| FALUNARA"; SEO description "…from Falunara…" → "…from FALUNARA…" |
| Session 2 | Page "Contact" (/pages/contact) | Body was empty; added support text with badush71@proton.me. The native contact form is unchanged. |
| Session 3 | Theme duplicate "FALUNARA – launch fixes (2026-10-05)" (UNPUBLISHED, id 189900292476) | product.json: social-proof/review/testimonial/comparison/replica sections & blocks disabled; guarantee/FAQ/size/90-day texts replaced. index.json: size + brand. header-group: brand. collection.json: hardcoded rating off. footer-group: Menu block "Help" → Footer menu. Live theme untouched. |
| Session 3 | Files | Temporary upload files created and deleted again (falunara-product/index-template.txt) |

Nothing else was changed: no prices, bundles, subscriptions, shipping rates, checkout, payments or theme files.
Read-only check: `draftOrderCalculate` for a US address (nothing was saved).

## 2. Claim audit (product page / home page)
| Current claim | Risk | Reason | Recommended wording | Changed? |
|---|---|---|---|---|
| "Best results come with 90 days of consistent use." | Medium | Implies a substantiated 90-day result; conflicts with the 30-day guarantee | "For a consistent body-care routine, continued daily use is recommended." | No (manual A9) |
| "Fast Shipping" | High | No verified processing or delivery time; US orders apparently ship from Germany | "Shipping Calculated at Checkout" | No (manual A5) |
| "Easy Returns" / "simply return the item…" | Medium | Customer pays return shipping; return address is provided only after approval | "Email Support"; guarantee text per A3 | No (A3/A6) |
| "What is the 100% results guarantee?" / "Details about the guarantee go here." | High | Placeholder; "results guarantee" implies a guaranteed physiological outcome | A1/A2 | No (manual) |
| "100% Satisfaction" | Low–Med | Absolute claim | "30-Day Money-Back Guarantee" | No (A4) |
| "and 50.000+ others purchased" + stock avatars | High | Unverified sales figure; fake social proof | Hide | No (B1) |
| "+10,839 Total Ratings", "Rated 4.8", "Verified Buyer", "March 14th, 2025" | High | No review app; dates before the store existed; count unverified | Hide until real reviews exist | No (B2) |
| Testimonials: "Verified customer", AI-like images; "before and after photos… 6 weeks", "more youthful" | High | Reviews can't be verified; images appear AI-generated; "youthful" is anti-aging framing | Hide; do not rewrite or replace with invented reviews | No (B3) |
| Comparison: "Other Body Care" = "Knock-off", "No" for "Helps Lock In Moisture" etc. | Medium | Unsubstantiated comparative/disparaging claims | Hide, or factual rows only | No (C1) |
| "Watch Out For Cheap Replicas." | Low–Med | Implies replicas exist; unverified | Hide unless documented | No (C2) |
| "Two sizes — 100 ml … 200 ml" | Medium | Only one 100 ml variant is for sale | "100 ml / 3.4 fl oz bottle" | No (D1/D2) |
| "Botanical body care for dry, crepey-looking skin — for softer, smoother-looking skin" | Low | Cosmetic "appearance" wording | Keep | n/a |
| "Leaves skin feeling soft & smooth", "Helps lock in moisture", "healthy-looking glow", "Leaves Skin Looking Radiant" | Low | Cosmetic | Keep | n/a |
| Ingredient tabs ("helps condition skin", "helps soften and nourish dry skin", "seal in moisture") | Low | Cosmetic, but the ingredients must actually be in the formula | Keep once the INCI list confirms them | n/a |
| [Unassigned template] VEILKIND Milk Thistle: liver/digestion/antioxidant supplement claims, 90-day guarantee, "Free U.S. Shipping" | High (if reachable) | Other brand/product, reachable via ?view=milk-thistle | Delete the template | No (G) |
No live drug claims (treat, cure, heal, collagen, wrinkles, FDA, clinically proven, dermatologist) were
found for the body oil.

## 3. Product information (from Shopify; nothing invented)
| Item | Status |
|---|---|
| Identity | "FALUNARA Botanical Body Oil" ✔ |
| Net contents | "100 ml / 3.4 fl oz" appears in theme copy; SKU FAL-BBO-100. Verify against the label |
| Ingredient (INCI) list | **Missing.** Only 5 ingredient names in tabs plus "Squalane" / "Vitamin E" mentions. Get the full INCI list from the manufacturer |
| Directions | Present (FAQ + steps). Minor press-vs-massage inconsistency |
| Warnings / cautions | **Missing.** None provided (external use, eyes, patch test, discontinue if irritation). Contains Brazil nut oil (tree nut); add the manufacturer's allergen caution if one exists |
| Responsible business information | Not on the product page; the label must carry it (see §5) |

## 4. Subscriptions (Kaching Subscriptions)
- Selling plan group "Subscribe and save": 15% off, every 30/60/90 days, no min/max cycles, **no plan descriptions**.
- The Kaching widget's labels and **default selection are configured inside the Kaching app**, not in the theme, so I could not verify them.
- **Merchant must check in the Kaching Subscriptions app:**
  1. One-time purchase is the default; subscription is not preselected.
  2. The subscription option states near the button: "Recurring order: charged automatically every [30/60/90] days at 15% off until you cancel. Cancel anytime."
  3. Link to the Subscription Policy (/policies/subscription-policy) from the widget.
  4. Add plan descriptions (Kaching or Shopify selling plan) with the same disclosure.
  5. Confirm how customers cancel (Kaching customer portal / customer account) and that it works.
- Shopify checkout shows recurring-payment terms automatically, but the product-page disclosure is still needed.

## 5. Outside Shopify: FDA / MoCRA / labeling (not resolved by policies or theme edits)
Not verified; FALUNARA is **not** stated to meet any of these:
1. **Cosmetic product listing** (MoCRA) with FDA by the responsible person.
2. **Facility registration** of the manufacturing/processing facility (usually done by the manufacturer).
3. **Safety substantiation** records for the product.
4. **Adverse event** handling: serious adverse event reporting, record keeping, and the label must show a US domestic address, phone number, or electronic contact (e.g. website) where adverse events can be reported.
5. **Physical label** (FPLA/FDA cosmetic labeling): identity, net quantity (metric + US units), INCI ingredient declaration in descending order, name and place of business of the manufacturer/packer/distributor, required warnings.
6. **Responsible person**: identify who (manufacturer, packer, or distributor, i.e. the LLC or the supplier) holds MoCRA obligations.
7. Import: if the product ships from Germany, US import/customs entry requirements apply (FDA-regulated cosmetics).

## 6. Shipping configuration (€19.99)
- Store currency **USD**; the only enabled market is **United States** (USD). The Germany market is disabled.
- Delivery profile "Allgemeines Profil" (German admin defaults). The US sits in zone **"International"** with one rate, **"Standard International" = 19.99 EUR**. That rate amount is stored in EUR, apparently left over from an EUR store setup.
- **Tested (draft order calculation, not saved):** a US address is offered **"Standard International – $22.50 USD"**. The customer sees **USD**, converted from 19.99 EUR, so the price will **change with the exchange rate**.
- The only location is Sankt Augustin, Germany (manual fulfillment). Free shipping (≥ €55) exists only for the disabled Germany zone.
- **Recommended correction (merchant decision; not changed):**
  1. Confirm where US orders actually ship from. If a supplier/3PL ships from the US, add that location and assign the product to it.
  2. Settings → Shipping and delivery → General profile → create a zone **"United States"** with a fixed **USD** rate you choose (or free shipping, only if you will fund it), and remove the US from "International".
  3. Rename the rate to something factual (e.g. "Standard Shipping"), and add a delivery-time estimate only once you can meet it.
  4. Optionally rename the profile and zones to English.

## 7. FTC Mail/Internet Order Rule: internal notes (not storefront copy)
- Advertise a shipping time only if you have a reasonable basis to meet it. If no time is stated, you must have a reasonable basis to ship within **30 days**.
- If you can't ship on time: notify the customer before the deadline with a revised date and offer the option to **consent to the delay or cancel for a prompt full refund**. Refund unshipped orders within 7 business days (card orders: credit within 1 billing cycle).
- Keep records of shipping times and delay notices.
- The Shipping Policy commits to the 30-day fallback; keep operations consistent with it.

## 8. Customs (US recipients)
If US orders ship from Germany, US import duties/fees may apply at delivery. The US no longer applies
the duty-free de minimis exemption to most low-value imports; confirm this with your carrier. Shopify
Basic does not collect duties at checkout by default. **Decide and tell me:**
- (a) **Ships from inside the US:** add no customs section.
- (b) **Ships from outside the US, customer pays:** add "Orders shipped from outside the United States may be subject to import duties, taxes, or fees collected by the carrier on delivery. These charges are not included in the price or shipping charges shown at checkout and are the recipient's responsibility."
- (c) **Ships from outside the US, FALUNARA pays (DDP):** add "Any import duties or fees for U.S. deliveries are covered by us."

## 9. Other trust items
- Store name "Falurana" shows in checkout, emails, the footer copyright and the browser title (manual change).
- Privacy policy title is stored as "Datenschutzerklärung" (German admin). Check that the footer shows "Privacy Policy"; if not, set the admin language to English and re-save the policy.
- Support email is a personal Proton address. Consider a branded address (e.g. support@falurana.com) and set it in Settings → General → Customer email and Settings → Notifications → Sender email.
- Placeholder copy exists in hidden/disabled sections (safe while hidden). Never enable them as they are.
