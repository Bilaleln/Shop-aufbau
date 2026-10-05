# Storefront text inventory — live theme

- **Theme:** "OLEG - Falunara PDP (work copy)" — `gid://shopify/OnlineStoreTheme/189437477244` (role MAIN, live)
- **Pulled:** 2026-10-05, read-only, through the Admin GraphQL API. Nothing in Shopify was changed.
- **Product:** `botanical-body-oil`. Title "FALUNARA Botanical Body Oil". ACTIVE. templateSuffix "" so it uses `templates/product.json`. It has **one variant only** ("Default Title", $49.00, no compare-at price). It is the only product in the store.
- **Product description (descriptionHtml, rendered by `main` because show_product_info = true):** "<p>A slow, deliberate body oil for skin that deserves more than a rushed routine. Press it into damp skin after a shower and let it settle — the finish is soft and lived-in, never slick.</p><p>Made to be part of the evening, not another step to get through.</p>"
- **Location format:** template → section id → block id → setting key. "(hidden)" means the value is stored but a toggle hides it, as noted. "(DISABLED)" means the section or block is disabled, so it is not rendered.
- `templates/product.milk-thistle.json` (VEILKIND Milk Thistle) is **not assigned to any product**. Any product URL can still render it with `?view=milk-thistle`, so it is listed separately, marked **[MT]**.

---

## SUMMARY

### 1. Placeholder / template text

**Live and visible on the PDP (product.json):**
- "What is the 100% results guarantee?" / "<p>Details about the guarantee go here.</p>" — product → `main` → `buy_faq` → `question_5` / `answer_5`. **VISIBLE placeholder.**
- "Premium Product" — product → `guarantee` → `product_name`. Rendered as the **alt text** of every guarantee photo (show_photos = true). The liquid also replaces "Premium Product" in description_text with this value.
- "We're so confident in the quality of our product that we offer a satisfaction guarantee. If you're not completely satisfied with your purchase, simply return the item within 30 days for a full refund." — product → `guarantee` → `description_text`. This is the stock section text, not tailored to the product.
- "ADD TO CART" — product → `guarantee` → `button_text`. Stock text; elsewhere the PDP says "Add to bag".
- Sample persona plus stock photos: product → `main` → `custom_liquid_AmeieR` → `custom_liquid`. Avatars are `https://randomuser.me/api/portraits/women/44.jpg`, `/68.jpg` and `/12.jpg` (random stock portraits), named "Isabelle", with "and 50.000+ others purchased".
- "<p>Real experiences with FALUNARA Botanical Body Oil</p>" heading over testimonial cards whose images are AI-generated. Filenames start with `hf_20260921_…` (Higgsfield-generated) or are named `composite.png`, `CqZUL3Xt5r.jpg` and `wJlxrl1NzA.jpg`. Location: product → `ss_testimonials_42_yU96KH` → blocks `testimonial_*` → `image`. Flagged as possible sample content.

**Stored but hidden or not rendered on the PDP:**
- "Custom Product Title" — product → `main` → `title_main` → `custom_title` (hidden: use_custom_title = false). Same in index → `product` → `p_title` → `custom_title` (hidden).
- "<p>Add additional descriptive text here</p>" — product → `main` → `subhead` → `description` and product → `main` → `reassurance` → `description` (hidden: show_description = false).
- "Improves user experience, Saves time and effort, Provides excellent value" — product → `content_tabs_V6yix7` → `tab_y4L9iB` / `tab_iqpdpn` / `tab_qepWtn` / `tab_EVzFf4` → `second_benefits`. Not rendered, because second_content_type = image_with_text and second_text_content is empty.
- "Product Name", "$29.99", "$39.99" — product → `customer_reviews_carousel_AjfT8a` → `review_FQajei` / `review_mpmqRT` / `review_BGQDjx` → `product_title` / `product_price` / `product_compare_price`. Not rendered, because product_reference = botanical-body-oil, so the card shows the live title "FALUNARA Botanical Body Oil" and the price $49.00. `review_BGQDjx` has no price fields.
- "See what our customers are saying about our products" — product → `customer_reviews_carousel_AjfT8a` → `description_text` (hidden: show_description = false).
- "Improves user experience, …" also appears in product → `tabs` (DISABLED section) → tab blocks → `second_benefits`.

**Disabled placeholders (product.json):**
- `main` → `labels`: "Product Label", "Featured Item", "Premium Choice", "Additional Info" (x3)
- `main` → `review_quote`: "Lauren J." / "This product exceeded my expectations. The quality is outstanding and I would highly recommend it to anyone."
- `main` → `rating` (trustpilot_rating): "Excellent" / "4.7 sur 5"
- `main` → `bundles`: "Buy 1".."Buy 4", "SAVE", "BEST VALUE", "You save {savings}"
- `tabs` → `tab_ingredients`: "<p>Add the confirmed INCI list here.</p>"
- `faq` → `q_ing`: "<p>Add the confirmed ingredient list here.</p>"; `q_last`: "<p>Add the confirmed usage duration here.</p>"; `q_ship`: "<p>Add the confirmed shipping terms here.</p>"; `q_ret`: "<p>Add the confirmed returns policy here.</p>"
- `story` → `secondary_image_Lar8jq` → `image_alt`: "Descriptive image text"
- `lifestyle_grid` → `title`: "Photo Collection"

**Other templates:**
- index → `faq` → `f_ing` / `f_ship` / `f_ret` (DISABLED): "<p>Add the confirmed ingredient list here.</p>", "<p>Add the confirmed shipping terms here.</p>", "<p>Add the confirmed returns policy here.</p>"
- index → `grid` (DISABLED) → `title`: "Photo Collection"
- collection → `collection_grid_page_hDiTDB` → `heading`: "Featured Collection" (stock). Its blocks point at collection handles "theme" (x4) and "frontpage". These look like stock or default references.
- collection → `newsletter_xRjFbi`: "Subscribe to our emails" / "<p>Be the first to know about new collections and exclusive offers.</p>" (Dawn defaults, visible)
- password → `main`: "Opening soon" / "<p>Be the first to know when we launch.</p>" (Dawn defaults)
- footer-group → `footer` → `newsletter_heading`: "Subscribe to our emails" (hidden: newsletter_enable = false)
- header-group → `announcement_bar_W34fB6` "Countdown Banner" (DISABLED): end_date "2023-12-31 23:59:59", labels "DAYS" / "HRS" / "MIN" / "SEC"

**[MT] product.milk-thistle.json (unassigned alternate template):**
- `main` → `quick_faq` → `answer_2`: "<p>Take [SERVING SIZE] daily with a glass of water, ideally at the same time each day. Consistency matters more than timing.</p>"
- `main` → `quick_faq` → `answer_4`: "<p>Information about efficacy goes here.</p>"
- `main` → `quick_faq` → `answer_5`: "<p>Details about the guarantee go here.</p>"
- `main` → `subtitle` → `description`: "<p>Add additional descriptive text here</p>"
- `main` → `labels` → `label_*_serving_count`: "Additional Info"
- `ugc_videos` → `rating_text`: "Rated [4.8]/5 by [REVIEW COUNT] customers"; captions "Example customer clip" (x3)
- `testimonials` → `description_text`: "Placeholder cards — connect your review app or paste real reviews before publishing."
- `testimonials` → `review_1..3`: "[PLACEHOLDER — replace with a real verified review. Do not publish this section until genuine customer reviews are connected.]" / "[CUSTOMER NAME]"
- `faq` → `faq_4`: "[SERVING SIZE]" plus "<em>Store owner: confirm the serving size against the finished label before publishing.</em>"
- `faq` → `faq_5`: "[CAPSULE COUNT]", "[X] days" plus "<em>Store owner: confirm the capsule count…</em>"
- `faq` → `faq_6`: "<em>Store owner: confirm this against your manufacturer's specification before publishing.</em>"
- `final_cta` → `featured_product`: "placeholder-product"
- `final_cta` → `cta_reviews`: custom_rating "[4.8]", custom_rating_count "[REVIEW COUNT]"
- `sticky_atc` → `rating_text`: "Rated [4.8] | [REVIEW COUNT] reviews"

### 2. Brand spellings
Search covered every template and section-group JSON, case-insensitive, for falunara, falurana, oleg, ringani, elixer/elixir, milk thistle and veilkind. **No "Falurana", "OLEG", "RINGANI" or "elixer/elixir" appears in any customer-facing setting.** "OLEG" appears only in the theme name (admin-only).

**"Falunara" (title case):**
- header-group → `custom_announcement_bar_KbrQgt` → `text`: "Falunara — made for the minute after the shower" (**every page**)
- index → `brand` → `heading`: "What Falunara" (+ heading_accent "is for")
- index → `brand` → `b_par` → `paragraph_text`: "<p>Falunara makes body care for the parts of the routine nobody photographs. …"
- index → `grid` (DISABLED) → `title_primary`: "Falunara,"
- product → `main` → `replica_warning_wPCWEg` → `warning_text`: "…authentic Falunara Botanical Body Oil…"
- product → `main` → `video_ugc` (DISABLED) → `heading`: "Falunara, in use"
- product → `story` (DISABLED) → `s_par`: "<p>Falunara started with a small frustration…"
- product → `lifestyle_grid` (DISABLED) → `title_primary`: "Falunara"

**"FALUNARA" (all caps):**
- Product title: "FALUNARA Botanical Body Oil" (product record, rendered by main / title_main, the index featured product and the review cards)
- product → `content_tabs_V6yix7` → `accent_text`: "FALUNARA"
- product → `product_comparison_hgQaih` → `subheading`: "See what's inside FALUNARA—and what to look for in your body care."
- product → `product_comparison_hgQaih` → `product_column_gfNRJc` → `product_name`: "FALUNARA"
- product → `customer_reviews_carousel_AjfT8a` → `review_FQajei` → `review_text`: "…What appealed to me about FALUNARA was having something simple…"
- product → `ss_testimonials_42_yU96KH` → `sub_heading_gaPy6a` → `sub_heading`: "Real experiences with FALUNARA Botanical Body Oil"

**"VEILKIND" / "Milk Thistle" — [MT] only (the unassigned template):**
- `ugc_videos` → `subheading`: "Short clips showing where VEILKIND fits into an ordinary morning. Swipe to watch."
- `why_it_works` → `image_alt`: "VEILKIND bottle with vegetarian capsules"
- `lifestyle` → `lifestyle_copy`: "…VEILKIND is built for that: one capsule…"
- `comparison` → `col_ours` → `product_name`: "VEILKIND"
- "Milk Thistle Complex" appears as `custom_title`, `product_title`, `product_name` and `cta_title` across MT sections
- `main` → `pdp_styles` loads the asset `veilkind-pdp.css`. Image files are named `veilkind-*`.

### 3. Shipping / delivery claims
- **product → `guarantee` → `benefit_2`: "Fast Shipping"** (VISIBLE on the PDP)
- product → `main` → `shipping` (DISABLED, shipping_notice): only suffix "."
- product → `faq` → `q_ship` (DISABLED): "Shipping and delivery" / "<p>Add the confirmed shipping terms here.</p>"
- index → `faq` → `f_ship` (DISABLED): the same placeholder
- settings_data: `product_free_show` = false (free-shipping bar off), `product_free_shipping` = 40
- **[MT]:** "FREE U.S. SHIPPING" (`trust_bar` → `trust_shipping`); "Free U.S. Shipping" (`main` → `guarantee_badges` → `badge_2_text`; `final_cta` → `cta_guarantee` → `badge_2_text`; `guarantee` → `benefit_2`); "<p>Free shipping within the United States. If it isn't for you, contact us within 90 days of delivery for a refund.</p>" (`main` → `quick_faq` → `answer_3`); `sticky_atc` → `delivery_text_prefix` "Get It By" with an estimated delivery date.
- No "ships from", "tracked" or delivery-days claims anywhere.

### 4. Guarantee / refund / return claims
**Visible on the PDP:**
- product → `main` → `guarantee_badges_CtLiLL` → `badge_1_text`: "30-Day Money-Back Guarantee"; `badge_2_text`: "Secure Checkout"
- product → `main` → `buy_faq` → `question_5`: "What is the 100% results guarantee?"; `answer_5`: "<p>Details about the guarantee go here.</p>"
- product → `guarantee` → `heading_risk_free` + `heading_beauty_revolution`: "Money-Back" "Guarantee"
- product → `guarantee` → `description_text`: "We're so confident in the quality of our product that we offer a satisfaction guarantee. If you're not completely satisfied with your purchase, simply return the item within 30 days for a full refund."
- product → `guarantee` → `benefit_1`: "100% Satisfaction"; `benefit_3`: "Easy Returns"
- product → `main` → `reassurance` → `text`: "<p>Best results come with 90 days of consistent use.</p>" (results framing next to the guarantee)

**Hidden or disabled:**
- index → `hero` → `guarantee_text`: "30-Day Money-Back Guarantee" (hidden: show_guarantee = false)
- product → `main` → `guarantee_badge` (DISABLED, custom_money_back): "30-Day Money Back Guarantee" / "That's how confident we are in your results. But if you're not thrilled, send it back and we'll refund your purchase."
- product → `faq` → `q_ret` and index → `faq` → `f_ret` (DISABLED): "Returns and refunds" / "<p>Add the confirmed returns policy here.</p>"
- settings_data: `money_back_guarantee_icon` "shield" (cart drawer; no text)

**[MT]:**
- "90-DAY MONEY-BACK GUARANTEE" (`trust_bar`)
- "90-Day Money-Back Guarantee" (`main` → `guarantee_badges` and `final_cta` → `cta_guarantee` → `badge_1_text`)
- "Try it for 90 days" / "Take it as part of your daily routine. If it isn't for you, contact us within 90 days of delivery and we'll refund your order — bottle open or not." (`main` → `money_back`)
- "What is the 100% results guarantee?" / "Details about the guarantee go here." (`quick_faq`)
- "90 days," "no argument" / "Take it for three months. If it hasn't earned its place in your routine, email us within 90 days of delivery and we'll refund the order — you don't need to send back an unopened bottle, and you don't need to explain yourself." (`guarantee`)
- "90-Day Refund Window", "Real Human Support" (`guarantee` benefits)
- "Money-back window" "90 days" vs "30 days typical" (`comparison` → `row_6`)
- "90-Day Guarantee" (`final_cta` → `cta_reviews` → `satisfaction_text`)
- "<p>Email us within 90 days of delivery and we'll refund the order. An opened bottle is fine — that's the point of a 90-day window.</p>" (`faq` → `faq_8`)

**Conflict:** the PDP says 30 days. The repo's policies/ folder has its own refund-policy.html and was not compared here.

### 5. Health / skin / medical / efficacy claims (all verbatim)
**Visible on the PDP (product.json):**
- `main` → `subhead` → `text`: "<p>Botanical body care for dry, crepey-looking skin — for softer, smoother-looking skin.</p>"
- `main` → `bullet_list_CpGCaF` → `bullet_1`: "Leaves skin feeling soft & smooth"; `bullet_2`: "Helps lock in moisture"; `bullet_3`: "Gives skin a healthy-looking glow"
- `main` → `bullet_list_mWYJnq` → `bullet_1`: "Simple everyday body care"
- `main` → `reassurance` → `text`: "<p>Best results come with 90 days of consistent use.</p>"
- `main` → `buy_faq` → `question_5`: "What is the 100% results guarantee?"
- `content_tabs_V6yix7` → `subheading`: "<p>Get to know the ingredients in your daily body-care ritual.</p>"
- `content_tabs_V6yix7` → `tab_KbmqAf` (WAKAME ALGAE): "A Little Ocean-Inspired Care" / "<p>Wakame algae extract helps condition skin, leaving dry areas feeling softer and smoother.</p>"
- `content_tabs_V6yix7` → `tab_y4L9iB` (BRAZIL NUT OIL): "Comfort for Dry Skin" / "<p>Brazil nut oil helps soften and nourish dry skin, leaving your arms, legs, and body feeling comfortably supple.</p>"
- `content_tabs_V6yix7` → `tab_iqpdpn` (PASSIONFLOWER SEED OIL): "Softness for Everyday Skin" / "<p>Passionflower seed oil helps seal in moisture and soften rough-feeling areas for a smoother, more comfortable feel.</p>"
- `content_tabs_V6yix7` → `tab_qepWtn` (RICE BRAN OIL): "A Softer, Smoother Feel" / "<p>Rice bran oil helps condition dry skin and smooth rough-feeling patches, leaving skin soft to the touch.</p>"
- `content_tabs_V6yix7` → `tab_EVzFf4` (ARGAN OIL): "A Naturally Radiant Finish" / "<p>Argan oil helps soften dry skin and adds a healthy-looking glow, leaving it feeling smooth and supple.</p>"
- `steps_9hzN8c` → `title` + `title_highlight`: "Your Daily Ritual for" "Softer-Feeling Skin"; `subtitle`: "A simple daily ritual for your arms, legs, and body."
- `steps_9hzN8c` → `step_bR8Jz7` → `step_title`: "Focus on Dry Areas"
- `product_comparison_hgQaih` → feature rows, each "Yes" for FALUNARA (Original) and "No" for "Other Body Care" (Knock-off): "Helps Soften Dry, Rough Skin"; "Helps Lock In Moisture"; "Leaves Skin Looking Radiant"; "Botanical Oils + Squalane"; "With Vitamin E"; "Easy Pump Application"
- `benefits` → `subtitle`: "Most body products are a step to get through. This one is meant to be the reason you slow down for a minute."
- `features` → `f1`: "The finish" / "The point of an oil is the first ten minutes and the eight hours after. It should stop feeling like something you put on."
- Testimonials with efficacy and before/after claims (`ss_testimonials_42_yU96KH`; full text in section 7):
  - `testimonial_AUnk7f`: "…after comparing my before and after photos… I didn't realize how much my skin had changed until I looked back at the photo I took about 6 weeks ago…"
  - `testimonial_pNYDWX`: "…my skin feels noticeably softer and more nourished… how healthy and smooth my arms look now."
  - `testimonial_HzGjVi`: "…Since menopause, I've struggled with crepey-looking skin on my arms…"
  - `testimonial_Dg7dMV`: "I'm 67, and honestly, my skin looks so much smoother and more youthful now…"
  - `testimonial_eKCnnJ`: "…My skin looks noticeably better and feels much smoother…"
  - `testimonial_aRMXmj`: "…leaves my skin feeling hydrated…"
  - `testimonial_tA8Fqt`: "…My skin feels smoother, looks healthier…"
  - `testimonial_tiwBzr`: "…help with the dry, crepey look on my arms and legs. My skin feels much more moisturized now…"
- `ss_testimonials_42_yU96KH` → `heading_dPtD7d`: "What Women Are Saying"

**Disabled on the PDP:**
- `statistics_grid_iVeXPU`: "Squalane and vitamin E meet a nourishing blend of botanical oils."
- `main` → `guarantee_badge`: "That's how confident we are in your results…"
- `main` → `benefits`: "A little goes far"

**index.json (visible):**
- `faq` → `f1`: "…the water is already there and the oil holds it in place."
- `alternating_features_9wEzGD` → `feature_UBWTi4`: "…the first ten minutes and the eight hours after…"
- Index copy is otherwise sensory/usage only, with no efficacy wording.

**Absent:** no wrinkles, collagen, anti-aging, eczema, inflammation, healing/repair, clinically, dermatologist, "proven", FDA, cure/treat, firm/tighten or "%" efficacy claims in Botanical Body Oil text. Exceptions: "crepey-looking" (subhead and 2 testimonials), "youthful" (testimonial), and "before and after photos" (testimonial). "100%" appears only in "100% results guarantee" and "100% Satisfaction".

**[MT] supplement claims:**
- "Daily liver support built on milk thistle extract standardized to 80% silymarin, with turmeric, artichoke and inositol."
- "Supports Healthy Liver Function"
- "Supports Comfortable Digestion"
- "Antioxidant Support From Silymarin"
- "80% STANDARDIZED SILYMARIN"
- "…in a liver and digestion routine…"
- "…included here for its own antioxidant compounds…"
- "…to support the everyday wellness side of the routine."
- "No clinical claims and no invented percentages — just what is actually in the bottle."
- "Does it really work?" / "Information about efficacy goes here."
- Disclaimer (faq_7): "This is a dietary supplement, not a treatment, and it isn't intended to diagnose, treat, cure or prevent any disease."

### 6. Ingredients / INCI, net contents, directions, warnings
**Ingredients:** **No full INCI list exists anywhere live.**
- The only ingredient mentions are the 5 content-tab names: "WAKAME ALGAE", "BRAZIL NUT OIL", "PASSIONFLOWER SEED OIL", "RICE BRAN OIL", "ARGAN OIL" (product → `content_tabs_V6yix7`).
- The comparison rows name "Botanical Oils + Squalane" and "With Vitamin E" (product → `product_comparison_hgQaih`).
- INCI placeholders are disabled: "Add the confirmed INCI list here." (product → `tabs` → `tab_ingredients`) and "Add the confirmed ingredient list here." (product → `faq` → `q_ing`; index → `faq` → `f_ing`).
- "Squalane and vitamin E…" is in a disabled section (`statistics_grid_iVeXPU`).

**Net contents:**
- "100 ml / 3.4 fl oz" — product → `ticker` → `t2` → `text` (visible); index → `benefitbar` → `h3` → `text` (visible)
- "Two sizes — 100 ml for the shelf, 200 ml when it sticks" — index → `hero` → `benefit_3_text` (visible)
- "<p>100 ml is the everyday bottle and the easier first purchase. 200 ml makes sense once it has become the one you reach for.</p>" — product → `main` → `buy_faq` → `answer_4` and index → `faq` → `f4` (visible)
- "The 100 ml bottle is the perfect size for everyday body care." — index → `alternating_features_9wEzGD` → `feature_MdKTbi` (visible); product → `features` → `f3` (DISABLED)
- Disabled: "3.4 fl oz" / "100 mL of botanical body oil for your arms, legs, and body." (`statistics_grid_iVeXPU`); "Two sizes, one habit" / "100 ml for your bathroom shelf…" (`benefits` → `b4`)
- **Problem:** the product has only one variant, so **no 200 ml size is purchasable**, yet the visible copy claims "Two sizes" and 200 ml.

**Directions (visible):**
- product → `main` → `buy_faq`:
  - `answer_1`: "<p>Warm two or three pumps between your palms and press — do not rub — into skin that is still damp from the shower. Give it a minute before you dress.</p>"
  - `answer_2`: "<p>Everywhere below the jaw: arms, legs, chest, and the dry patches on elbows, shins and heels. Use less than you think on the backs of the knees.</p>"
  - `answer_3`: "<p>Straight after a shower or bath, while skin still holds water. At night it doubles as the last step before bed.</p>"
- product → `steps_9hzN8c`: "Apply After Showering" / "Massage a small amount onto clean, slightly damp skin."; "Focus on Dry Areas" / "Gently work into your arms, legs, and rough-feeling areas. Let absorb before dressing."; "Make It Your Daily Ritual" / "Keep your routine simple with a little body care every day."
- product → `faq` → `q4`: "<p>Two or three pumps for the whole body is a sensible starting point. Use less on the backs of the knees and more on elbows, shins and heels.</p>"
- product → `faq` → `q5` and index → `faq` → `f5`: "<p>This one is made for the body, so we would keep it below the jaw.</p>"
- index → `howto` → `s1`–`s3`; `routine` → `r_list`; `hero` benefits. Full text is in the detail section below.

**Note:** product → `main` → `buy_faq` → `answer_1` says "press — do not rub". product → `steps_9hzN8c` says "Massage a small amount" and "Gently work into". These directions are inconsistent.

**Warnings / cautions:**
- **ABSENT.** There is no patch-test, external-use, keep-out-of-reach-of-children, eye-contact, allergy/nut-allergy or discontinue-if-irritation text anywhere, even though "BRAZIL NUT OIL" is named.
- The only cautions are about staining: product → `faq` → `q3` "<p>Any body oil can if you dress before it has absorbed…</p>" and index → `faq` → `f3`.
- Storage text "Store the bottle out of direct sunlight…" exists only in a DISABLED section (product → `tabs` → `tab_know`).
- Shelf life / PAO and batch information are absent.

**[MT]:**
- Serving size and capsule count are bracket placeholders.
- faq_7 tells pregnant or nursing customers, people taking medication, or people managing a medical condition to check with a doctor.

### 7. Reviews / testimonials / social proof / urgency
**All review content is hardcoded in theme settings. No review app is installed or embedded.** settings_data has only the Kaching Bundles and Kaching Subscriptions app embeds, and no reviews-app blocks appear in any template.

**A. Purchase-count badge** — product → `main` → `custom_liquid_AmeieR` → `custom_liquid` (hardcoded HTML):
- 3 avatars from randomuser.me
- "**Isabelle**" plus a check icon with aria-label "Verifiziert"
- "and 50.000+ others purchased"
- The product has a single SKU in a new store, so this number is unverified. It uses the German thousands separator.

**B. Single review card** — product → `main` → `customer_review_MCrBQE`:
- Name "Marleen J."
- Rating 5
- Avatar `shopify://shop_images/Authentic-UGC-style-customer-photo-for-F.png` (the filename suggests an AI-generated "UGC-style" image)
- Text: "Anyone else have a whole routine for their face… and barely give their arms a second thought? 😅 Your body deserves a little care too. A warm shower, your favorite body oil, and a few quiet minutes just for you. 🤎"

**C. Customer Reviews carousel** — product → `customer_reviews_carousel_AjfT8a` (name "Customer Reviews"):
- Header: "Customer" "Reviews"; summary "Rated" "4.8" "based on" "+10,839 Total Ratings"; badge "Verified Buyer"; label "Item Purchased"; "Purchased on"
- `review_FQajei`:
  - rating 5; name "Susan L"; verified badge shown; purchase date "March 14th, 2025"
  - Displayed product: live title "FALUNARA Botanical Body Oil" at $49.00 (stored product_title "Product Name", price "$29.99", compare "$39.99" are not rendered)
  - Text: "I've always been good about taking care of my face, but my arms barely got a second thought until my fifties. Suddenly I was paying attention to every little change. What appealed to me about FALUNARA was having something simple to add to my routine. A little after my shower, a gentle massage, and a few minutes for myself before getting dressed. I'm not looking to look twenty again. I just want to give the rest of my skin the same attention I've been giving my face all these years."
- `review_mpmqRT`:
  - rating 5; name "Karen L"; verified; "March 14th, 2025"; same product/price fields as above
  - Text: "At 53, I'm much more interested in a routine I enjoy than a bathroom full of the latest trends. I spend so much of my day doing things for everyone else that it's easy to rush through my own. Taking a little time after my shower has become a reminder to slow down. Nothing complicated, just a few minutes devoted to caring for my skin. I like the idea that body care can be a small everyday pleasure instead of something I only think about when summer comes around."
- `review_BGQDjx`:
  - rating 4; name "Jessica"; verified; stored product_title "Product Name" (live product rendered instead), no price or date stored
  - Text: "My bathroom cabinet is full of things I bought with the best intentions and then stopped using. I know myself—if a routine takes too much effort, it won't last. That's why the idea of a body oil appealed to me. I keep it next to my towel so I remember that step after showering. Arms, elbows, legs, done. For me, skincare at this age is about taking a little more care of myself without turning it into another chore on an already long to-do list"
- **Flags:**
  - Two reviews share the identical purchase date "March 14th, 2025", which predates the 2026 store.
  - All three are badged "Verified Buyer" with no review app behind them.
  - Their wording reads as aspirational ("the idea of a body oil appealed to me") rather than as post-use reviews.

**D. Testimonials** — product → `ss_testimonials_42_yU96KH` (name "SS - Testimonials #42"):
- Badge "Verified customer"; sub-heading "Real experiences with FALUNARA Botanical Body Oil"; heading "What Women Are Saying". All cards have stars_count 5.
- `testimonial_AUnk7f` — "Laura S." — image hf_20260921_171829…webp — "<p>I almost never leave reviews, even though I always read them before buying something online. But after comparing my before and after photos, I felt like I had to share. I was skeptical in the beginning, but I'm so glad I gave it a try. I didn't realize how much my skin had changed until I looked back at the photo I took about 6 weeks ago. I still have some progress to make, but I'm really impressed so far.</p>"
- `testimonial_pNYDWX` — "Evelyn K." — image CqZUL3Xt5r.jpg — "<p>I've been using it consistently and my skin feels noticeably softer and more nourished. I especially love how healthy and smooth my arms look now.</p>"
- `testimonial_HzGjVi` — "Kimberly C." — image hf_20260921_171730…webp — "<p>I honestly didn't expect to notice this much of a difference. Since menopause, I've struggled with crepey-looking skin on my arms and stopped feeling comfortable in sleeveless tops. I've spent so much money trying different products with barely any improvement. I'm really happy I decided to try this.</p>"
- `testimonial_Dg7dMV` — "Lenny S." — image hf_20260921_171828…webp — "<p>I'm 67, and honestly, my skin looks so much smoother and more youthful now. I'm really happy with the difference!</p>"
- `testimonial_eKCnnJ` — "Charlotte W." — image wJlxrl1NzA.jpg — "<p>I've been using this for a couple of months now and already placed another order. My skin looks noticeably better and feels much smoother. I've been so happy with it that I even ordered a few bottles for my sister.</p>"
- `testimonial_aRMXmj` — "Megan R." — image composite.png — "<p>My skin used to feel extremely dry no matter what moisturizer I used. This oil absorbs beautifully and leaves my skin feeling hydrated without that heavy, greasy feeling.</p>"
- `testimonial_tA8Fqt` — "Diane M." — image hf_20260921_174900…png — "<p>I started noticing the biggest difference after using it every day for a few weeks. My skin feels smoother, looks healthier, and I actually look forward to applying it after my shower.</p>"
- `testimonial_tiwBzr` — "Susan T." — image hf_20260921_175648…png — "<p>I was mainly looking for something to help with the dry, crepey look on my arms and legs. My skin feels much more moisturized now, and I'm really pleased with how it looks</p>"
- **Flag:** `hf_2026092…` images are Higgsfield AI generations dated 2026-09-21. These are presented as "Verified customer" testimonials with before/after language.

**E. Other social proof:**
- product → `replica_warning_wPCWEg` (visible): "Watch Out For Cheap Replicas." / "Shop directly from our official website to ensure you receive authentic Falunara Botanical Body Oil and support from our team." This implies replicas exist.
- product → `product_comparison_hgQaih` (visible): column 2 is "Other Body Care" with subtitle "**Knock-off**", and it gets "No" on every row. This is a comparative claim against competitors.
- index → `hero` (hidden: show_rating = false): rating_value "4.8/5", review_count "137,135"
- index → `product` (hidden: show_social_badge = false): "Over" 56 "M Views On TikTok"
- collection → `collection_grid_page_hDiTDB` (**visible**, show_rating = true, show_rating_text = true): rating_number "4.7", rating_value 5. A hardcoded star rating appears on product cards, but use_product_rating = true may override it with metafields.

**Disabled:**
- product → `reviews` (duplicate carousel, "+10,839 Total Ratings", 4.8)
- product → `customer_reviews_Fedj3c` "Image Reviews": "Look At How Others Are Loving Their Product!", "Real Reviews From Real People", "CLAIM OFFER", "Rated 4.8/5 by 1,319+ Happy Customers"
- product → `main` → `rating` (Trustpilot "Excellent" "4.7 sur 5")
- product → `main` → `review_quote` (Lauren J.)
- view-count badges "Over … M Views On TikTok / Instagram": `video_carousel_standalone_X3wGnC`, `video_ugc`, `lifestyle_grid` view_count "5.6"; index → `grid`; index → `p_video_reel`

**Urgency:**
- No countdowns, stock counters or "selling fast" text are live.
- header-group → `announcement_bar_W34fB6` "Countdown Banner" is DISABLED (end_date 2023-12-31).
- settings_data `show_social_proof_bar` = false; `show_discount_banner` = false.

**[MT]:** "Rated [4.8]/5 by [REVIEW COUNT] customers"; `testimonials` rating 4.7 with "73.000 reviews"; Trustpilot block "Excellent" "4.7 out of 5" (enabled in MT `main`); 3 placeholder review cards with price $29.99/$39.99 and date "March 14th, 2025".

### 8. Subscription disclosures
- **No subscribe-and-save, recurring, auto-renew or cancel text exists in any theme template or section group.** A search for "subscri", "recurring" and "cancel" found only newsletter text: "Subscribe to our emails" (collection newsletter visible; footer hidden).
- **Kaching Subscriptions app embed** — config/settings_data.json → `current.blocks` → `2724325275511621162`: type `shopify://apps/kaching-subscriptions/blocks/app-embed-block/1fa39fd7-f6a3-4bbc-9383-7d91d27b44f5`, `"disabled": false` (ENABLED), `"settings": {}`.
  - **No theme-side settings are stored.** There are no labels and no default-selection value.
  - Any subscription widget text, default selection (one-time vs. subscribe), discount and cancellation wording is configured inside the Kaching Subscriptions app admin. It cannot be read from the theme. Check it in the app (and whether selling plans are attached to the product).
- **Kaching Bundles app embed** — `current.blocks` → `15557474716127144420`: type `shopify://apps/kaching-bundles/blocks/app-embed-block/6c637362-a106-4a32-94ac-94dcfd68cdb8`, `"disabled": false` (ENABLED), `"settings": {}`. Bundle text is configured in the app.
- No other app embeds exist. No app blocks are placed in product.json: sections `1789876088cf71a722` and `1789876176d8b27025` are empty `_blocks` sections, and `custom_liquid_UmXqin` has an empty custom_liquid.
- The repo has `policies/subscription-policy.html`. No link to it from the PDP theme text was found.

### 9. German-language / non-English customer-visible text
- product → `main` → `custom_liquid_AmeieR` → `custom_liquid`: `aria-label="Verifiziert"` (German, read by screen readers).
- The same block uses "50.000+" with a German/European thousands separator. US format would be 50,000+.
- product → `main` → `rating` (DISABLED): "4.7 sur 5" (French).
- [MT] `testimonials` → `custom_review_count_text`: "73.000 reviews" (German separator).
- No other German or non-English strings were found in any template or section group.
- Not audited: the theme's locale files (locales/*.json) and hardcoded strings inside section .liquid files.

---

# DETAILED INVENTORY

Each entry lists section id, type, editor name where it is stored in JSON (otherwise the theme editor shows the section schema's default name for that type), block id, block type, and every non-empty string setting verbatim. Colors, numbers, image refs and booleans are skipped; star ratings are included. Inline SVG icons are shown as "(inline SVG icon — no text)". Entries marked [DISABLED] are not rendered. Each file ends with its list of disabled items.


## `templates/product.json`
Template used by product `botanical-body-oil`. Sections and blocks are in render order (`order` / `block_order`). Note: `main` also renders the product title "FALUNARA Botanical Body Oil", the price $49.00, the product description (see the header) and the gallery.

### Section `main` — type `shop-product-details`
  - Block `custom_liquid_AmeieR` — type `custom_liquid`
    - `custom_liquid`: "<div class=\"sp-badge\">\n  <div class=\"sp-badge__avatars\">\n    <span class=\"sp-badge__avatar\"><img src=\"https://randomuser.me/api/portraits/women/44.jpg\" width=\"48\" height=\"48\" loading=\"lazy\" alt=\"\"></span>\n    <span class=\"sp-badge__avatar\"><img src=\"https://randomuser.me/api/portraits/women/68.jpg\" width=\"48\" height=\"48\" loading=\"lazy\" alt=\"\"></span>\n    <span class=\"sp-badge__avatar\"><img src=\"https://randomuser.me/api/portraits/women/12.jpg\" width=\"48\" height=\"48\" loading=\"lazy\" alt=\"\"></span>\n  </div>\n\n  <p class=\"sp-badge__text\">\n    <strong class=\"sp-badge__name\">Isabelle</strong>\n    <svg class=\"sp-badge__check\" viewBox=\"0 0 24 24\" role=\"img\" aria-label=\"Verifiziert\" focusable=\"false\">\n      <path fill=\"currentColor\" fill-rule=\"evenodd\" d=\"M23 12l-2.44-2.78.34-3.68-3.61-.82-1.89-3.18L12 2.96 8.6 1.54 6.71 4.72l-3.61.81.34 3.68L1 12l2.44 2.78-.34 3.69 3.61.82 1.89 3.18L12 21.04l3.4 1.42 1.89-3.18 3.61-.82-.34-3.68L23 12zm-12.91 4.72l-3.8-3.81 1.48-1.48 2.32 2.33 5.85-5.87 1.48 1.48-7.33 7.35z\"></path>\n    </svg>\n    <span>and 50.000+ others purchased</span>\n  </p>\n</div>\n\n<style>\n  .sp-badge {\n    display: flex;\n    align-items: center;\n    gap: 10px;\n    padding: 0;\n    border: 0;\n    background: none;\n    font-size: 14px;\n    line-height: 1.3;\n    color: #241F1A;\n  }\n  .sp-badge__avatars { display: flex; flex-shrink: 0; }\n  .sp-badge__avatar {\n    width: 26px;\n    height: 26px;\n    border-radius: 50%;\n    overflow: hidden;\n    border: 2px solid #FBF8F3;\n    background: #E7DFD2;\n    display: block;\n  }\n  .sp-badge__avatar + .sp-badge__avatar { margin-left: -10px; }\n  .sp-badge__avatar img { width: 100%; height: 100%; object-fit: cover; display: block; }\n  .sp-badge__text { margin: 0; display: flex; align-items: center; flex-wrap: wrap; gap: 4px; }\n  .sp-badge__name { font-weight: 700; color: #241F1A; }\n  .sp-badge__check { width: 16px; height: 16px; color: #C99506; flex-shrink: 0; }\n  @media (max-width: 480px) { .sp-badge { font-size: 13px; } }\n</style>"
  - Block `title_main` — type `title`
    - `custom_title`: "Custom Product Title"
  - Block `subhead` — type `custom_text`
    - `text`: "<p>Botanical body care for dry, crepey-looking skin — for softer, smoother-looking skin.</p>"
    - `description`: "<p>Add additional descriptive text here</p>"
    - `custom_icon`: (inline SVG icon — no text)
  - Block `bullet_list_CpGCaF` — type `bullet_list`
    - `bullet_1`: "Leaves skin feeling soft & smooth"
    - `bullet_2`: "Helps lock in moisture"
    - `bullet_3`: "Gives skin a healthy-looking glow"
    - `gradient_direction`: "to right"
  - Block `bullet_list_mWYJnq` — type `bullet_list`
    - `bullet_1`: "Simple everyday body care"
    - `gradient_direction`: "to right"
  - Block `rule_1` — type `divider`
  - Block `price_block` — type `price`
  - [DISABLED] Block `benefits` — type `benefits_grid`
    - `benefit_1_text`: "Best on damp skin"
    - `benefit_1_custom_icon`: (inline SVG icon — no text)
    - `benefit_2_text`: "A little goes far"
    - `benefit_2_custom_icon`: (inline SVG icon — no text)
    - `benefit_3_text`: "For the whole body"
    - `benefit_3_custom_icon`: (inline SVG icon — no text)
    - `benefit_4_text`: "Morning or night"
    - `benefit_4_custom_icon`: (inline SVG icon — no text)
  - [DISABLED] Block `variant` — type `simple_variant_picker`
    - `size_option_label`: "Size"
    - `custom_color_mappings`: "red=#FF0000\nblue=#0000FF\ngreen=#00FF00\nyellow=#FFFF00\nblack=#000000\nwhite=#FFFFFF"
  - Block `atc` — type `add_to_cart`
    - `button_text_override`: "Add to bag"
  - Block `guarantee_badges_CtLiLL` — type `guarantee_badges`
    - `badge_1_text`: "30-Day Money-Back Guarantee"
    - `badge_2_text`: "Secure Checkout"
  - Block `reassurance` — type `custom_text`
    - `text`: "<p>Best results come with 90 days of consistent use.</p>"
    - `description`: "<p>Add additional descriptive text here</p>"
    - `custom_icon`: (inline SVG icon — no text)
  - Block `customer_review_MCrBQE` — type `customer_review`
    - `reviewer_name`: "Marleen J."
    - `review_text`: "Anyone else have a whole routine for their face… and barely give their arms a second thought? 😅 Your body deserves a little care too. A warm shower, your favorite body oil, and a few quiet minutes just for you. 🤎"
    - `rating`: 5
  - Block `buy_faq` — type `product_faq`
    - `question_1`: "How to use it"
    - `answer_1`: "<p>Warm two or three pumps between your palms and press — do not rub — into skin that is still damp from the shower. Give it a minute before you dress.</p>"
    - `question_2`: "Where it works"
    - `answer_2`: "<p>Everywhere below the jaw: arms, legs, chest, and the dry patches on elbows, shins and heels. Use less than you think on the backs of the knees.</p>"
    - `question_3`: "When to use it"
    - `answer_3`: "<p>Straight after a shower or bath, while skin still holds water. At night it doubles as the last step before bed.</p>"
    - `question_4`: "Which size should I start with?"
    - `answer_4`: "<p>100 ml is the everyday bottle and the easier first purchase. 200 ml makes sense once it has become the one you reach for.</p>"
    - `question_5`: "What is the 100% results guarantee?"
    - `answer_5`: "<p>Details about the guarantee go here.</p>"
  - [DISABLED] Block `video_carousel_standalone_X3wGnC` — type `video_carousel_standalone`
    - `heading`: "See it in action"
    - `social_platform`: "instagram"
    - `badge_text`: "Over"
    - `badge_suffix`: "M Views On TikTok"
  - Block `replica_warning_wPCWEg` — type `replica_warning`
    - `warning_title`: "Watch Out For Cheap Replicas."
    - `warning_text`: "Shop directly from our official website to ensure you receive authentic Falunara Botanical Body Oil and support from our team."
  - Block `custom_content_Wy4xTa` — type `custom_content`
  - [DISABLED] Block `review_quote` — type `customer_review`
    - `reviewer_name`: "Lauren J."
    - `review_text`: "This product exceeded my expectations. The quality is outstanding and I would highly recommend it to anyone."
    - `rating`: 5
  - Block `rule_2` — type `divider`
  - [DISABLED] Block `video_ugc` — type `video_carousel_standalone`
    - `heading`: "Falunara, in use"
    - `social_platform`: "instagram"
    - `badge_text`: "Over"
    - `badge_suffix`: "M Views On Instagram"
  - [DISABLED] Block `video_shopify_1` — type `carousel_default_video`
  - [DISABLED] Block `video_shopify_2` — type `carousel_default_video`
  - [DISABLED] Block `video_shopify_3` — type `carousel_default_video`
  - [DISABLED] Block `video_shopify_4` — type `carousel_default_video`
  - [DISABLED] Block `video_shopify_5` — type `carousel_default_video`
  - [DISABLED] Block `video_shopify_6` — type `carousel_default_video`
  - [DISABLED] Block `labels` — type `product_labels`
    - `label_1_name`: "Product Label"
    - `label_1_serving_count`: "Additional Info"
    - `label_2_name`: "Featured Item"
    - `label_2_serving_count`: "Additional Info"
    - `label_3_name`: "Premium Choice"
    - `label_3_serving_count`: "Additional Info"
  - [DISABLED] Block `rating` — type `trustpilot_rating`
    - `rating_text`: "Excellent"
    - `rating_score`: "4.7 sur 5"
    - `background_gradient_direction`: "to right"
  - [DISABLED] Block `bundles` — type `quantity_break`
    - `option_1_title`: "Buy 1"
    - `option_2_title`: "Buy 2"
    - `option_3_title`: "Buy 3"
    - `option_4_title`: "Buy 4"
    - `selected_gradient_direction`: "to right"
    - `save_badge_text`: "SAVE"
    - `save_badge_format`: "dollar"
    - `save_badge_custom_text`: "BEST VALUE"
    - `savings_text_format`: "You save {savings}"
    - `preselected_option`: "first_visible"
  - [DISABLED] Block `shipping` — type `shipping_notice`
    - `suffix_text`: "."
  - [DISABLED] Block `guarantee_badge` — type `custom_money_back`
    - `title_text`: "30-Day Money Back Guarantee"
    - `description_text`: "That's how confident we are in your results. But if you're not thrilled, send it back and we'll refund your purchase."
  - [DISABLED] Block `payments` — type `payment_icons`

### Section `ticker` — type `scrolling-features-bar`
  - Block `t1` — type `feature_item`
    - `text`: "Press into damp skin"
    - `icon`: (inline SVG icon — no text)
  - Block `t2` — type `feature_item`
    - `text`: "100 ml / 3.4 fl oz"
    - `icon`: (inline SVG icon — no text)
  - Block `t3` — type `feature_item`
    - `text`: "Body oil — not lotion"
    - `icon`: (inline SVG icon — no text)
  - Block `t4` — type `feature_item`
    - `text`: "Morning or night"
    - `icon`: (inline SVG icon — no text)
  - Block `t5` — type `feature_item`
    - `text`: "Unhurried by design"
    - `icon`: (inline SVG icon — no text)

### Section `content_tabs_V6yix7` — type `content-tabs` — name "Content Tabs"
- `heading`: "What’s Inside"
- `accent_text`: "FALUNARA"
- `subheading`: "<p>Get to know the ingredients in your daily body-care ritual.</p>"
- `accent_font_family`: "Bodoni Moda"
  - Block `tab_KbmqAf` — type `tab`
    - `tab_title`: "WAKAME ALGAE"
    - `first_title`: "A Little Ocean-Inspired Care"
    - `first_text_content`: "<p>Wakame algae extract helps condition skin, leaving dry areas feeling softer and smoother.</p>"
  - Block `tab_y4L9iB` — type `tab`
    - `tab_title`: "BRAZIL NUT OIL"
    - `first_title`: "Comfort for Dry Skin"
    - `first_text_content`: "<p>Brazil nut oil helps soften and nourish dry skin, leaving your arms, legs, and body feeling comfortably supple.</p>"
    - `second_benefits`: "Improves user experience, Saves time and effort, Provides excellent value"
  - Block `tab_iqpdpn` — type `tab`
    - `tab_title`: "PASSIONFLOWER SEED OIL"
    - `first_title`: "Softness for Everyday Skin"
    - `first_text_content`: "<p>Passionflower seed oil helps seal in moisture and soften rough-feeling areas for a smoother, more comfortable feel.</p>"
    - `second_benefits`: "Improves user experience, Saves time and effort, Provides excellent value"
  - Block `tab_qepWtn` — type `tab`
    - `tab_title`: "RICE BRAN OIL"
    - `first_title`: "A Softer, Smoother Feel"
    - `first_text_content`: "<p>Rice bran oil helps condition dry skin and smooth rough-feeling patches, leaving skin soft to the touch.</p>"
    - `second_benefits`: "Improves user experience, Saves time and effort, Provides excellent value"
  - Block `tab_EVzFf4` — type `tab`
    - `tab_title`: "ARGAN OIL"
    - `first_title`: "A Naturally Radiant Finish"
    - `first_text_content`: "<p>Argan oil helps soften dry skin and adds a healthy-looking glow, leaving it feeling smooth and supple.</p>"
    - `second_benefits`: "Improves user experience, Saves time and effort, Provides excellent value"

### Section `steps_9hzN8c` — type `steps` — name "Steps Results Section"
- `title`: "Your Daily Ritual for"
- `title_highlight`: "Softer-Feeling Skin"
- `subtitle`: "A simple daily ritual for your arms, legs, and body."
  - Block `step_4PL8dJ` — type `step`
    - `step_title`: "Apply After Showering"
    - `step_description`: "Massage a small amount onto clean, slightly damp skin."
  - Block `step_bR8Jz7` — type `step`
    - `step_title`: "Focus on Dry Areas"
    - `step_description`: "Gently work into your arms, legs, and rough-feeling areas. Let absorb before dressing."
  - Block `step_VWxkNK` — type `step`
    - `step_title`: "Make It Your Daily Ritual"
    - `step_description`: "Keep your routine simple with a little body care every day."

### Section `product_comparison_hgQaih` — type `product-comparison` — name "Product Comparison"
- `title_part_1`: "Thoughtful Care."
- `title_part_2`: "Simple Routine."
- `subheading`: "See what’s inside FALUNARA—and what to look for in your body care."
  - Block `product_column_gfNRJc` — type `product_column`
    - `product_name`: "FALUNARA"
    - `product_subtitle`: "Original"
  - Block `product_column_mjMzXa` — type `product_column`
    - `product_name`: "Other Body Care"
    - `product_subtitle`: "Knock-off"
    - `subtitle_custom_icon`: (inline SVG icon — no text)
  - Block `feature_row_qqDLrQ` — type `feature_row`
    - `feature_name`: "Helps Soften Dry, Rough Skin"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "No"
  - Block `feature_row_ArCPiF` — type `feature_row`
    - `feature_name`: "Helps Lock In Moisture"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "No"
  - Block `feature_row_xGkART` — type `feature_row`
    - `feature_name`: "Leaves Skin Looking Radiant"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "No"
  - Block `feature_row_HtXwHD` — type `feature_row`
    - `feature_name`: "Botanical Oils + Squalane"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "No"
  - Block `feature_row_WjW9Yt` — type `feature_row`
    - `feature_name`: "With Vitamin E"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "No"
  - Block `feature_row_KEpQVP` — type `feature_row`
    - `feature_name`: "Easy Pump Application"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "No"

### Section `customer_reviews_carousel_AjfT8a` — type `customer-reviews-carousel` — name "Customer Reviews"
- `title_text`: "Customer"
- `accent_text`: "Reviews"
- `accent_font_family`: "Georgia Pro"
- `description_text`: "See what our customers are saying about our products"
- `verified_badge_text`: "Verified Buyer"
- `product_label`: "Item Purchased"
- `rating_prefix`: "Rated"
- `rating_number`: "4.8"
- `based_on_text`: "based on"
- `custom_review_count_text`: "+10,839 Total Ratings"
- `purchase_date_prefix`: "Purchased on"
- `rating_summary_gradient_direction`: "to right"
  - Block `review_FQajei` — type `review`
    - `image_position`: "center center"
    - `rating`: 5
    - `review_text`: "I’ve always been good about taking care of my face, but my arms barely got a second thought until my fifties. Suddenly I was paying attention to every little change. What appealed to me about FALUNARA was having something simple to add to my routine. A little after my shower, a gentle massage, and a few minutes for myself before getting dressed. I’m not looking to look twenty again. I just want to give the rest of my skin the same attention I’ve been giving my face all these years."
    - `reviewer_name`: "Susan L"
    - `product_reference`: "botanical-body-oil"
    - `product_title`: "Product Name"
    - `product_price`: "$29.99"
    - `product_compare_price`: "$39.99"
    - `purchase_date`: "March 14th, 2025"
  - Block `review_mpmqRT` — type `review`
    - `image_position`: "center center"
    - `rating`: 5
    - `review_text`: "At 53, I’m much more interested in a routine I enjoy than a bathroom full of the latest trends. I spend so much of my day doing things for everyone else that it’s easy to rush through my own. Taking a little time after my shower has become a reminder to slow down. Nothing complicated, just a few minutes devoted to caring for my skin. I like the idea that body care can be a small everyday pleasure instead of something I only think about when summer comes around."
    - `reviewer_name`: "Karen L"
    - `product_reference`: "botanical-body-oil"
    - `product_title`: "Product Name"
    - `product_price`: "$29.99"
    - `product_compare_price`: "$39.99"
    - `purchase_date`: "March 14th, 2025"
  - Block `review_BGQDjx` — type `review`
    - `image_position`: "center center"
    - `rating`: 4
    - `review_text`: "My bathroom cabinet is full of things I bought with the best intentions and then stopped using. I know myself—if a routine takes too much effort, it won’t last. That’s why the idea of a body oil appealed to me. I keep it next to my towel so I remember that step after showering. Arms, elbows, legs, done. For me, skincare at this age is about taking a little more care of myself without turning it into another chore on an already long to-do list"
    - `reviewer_name`: "Jessica"
    - `product_reference`: "botanical-body-oil"
    - `product_title`: "Product Name"
    - `product_price`: "$29.99"
    - `product_compare_price`: "$39.99"
    - `purchase_date`: "March 14th, 2025"

### Section `benefits` — type `product-benefits`
- `list_gradient_direction`: "to bottom"
- `heading_accent`: "worn, not applied"
- `heading_regular`: "Built to be"
- `subtitle`: "Most body products are a step to get through. This one is meant to be the reason you slow down for a minute."
- `image_alt`: "Feature product image"
  - Block `b1` — type `benefit`
    - `title`: "Made for damp skin"
    - `description`: "Oil behaves differently on skin that still holds water from the shower. That is the moment this is built for."
    - `custom_icon_svg`: (inline SVG icon — no text)
  - Block `b2` — type `benefit`
    - `title`: "One product, whole body"
    - `description`: "Arms, legs, chest, elbows, shins, heels. No separate formulas and no decision to make at 7am."
    - `custom_icon_svg`: (inline SVG icon — no text)
  - Block `b3` — type `benefit`
    - `title`: "A ritual, not a routine"
    - `description`: "Two minutes with the lights low. It is meant to feel like something rather than another box to tick."
    - `custom_icon_svg`: (inline SVG icon — no text)
  - [DISABLED] Block `b4` — type `benefit`
    - `title`: "Two sizes, one habit"
    - `description`: "100 ml for your bathroom shelf. A little everyday luxury that becomes the bottle you reach for."
    - `custom_icon_svg`: (inline SVG icon — no text)
  - [DISABLED] Block `benefit_3fApJD` — type `benefit`
    - `title`: "A little care, right at hand"
    - `description`: "An easy-to-use pump keeps your daily body care simple. Dispense a little, massage in, and take a moment for yourself."
    - `custom_icon_svg`: (inline SVG icon — no text)

### [DISABLED] Section `statistics_grid_iVeXPU` — type `statistics-grid` — name "Statistics Grid"
- `heading_part_1`: "Small Ritual."
- `heading_part_2`: "Everyday Care."
- `subheading`: "Get to know the bottle behind your daily body-care ritual."
- `container_gradient_direction`: "to bottom"
  - Block `statistic_AFUpX8` — type `statistic`
    - `value_text`: "3.4 fl oz"
    - `title`: "Care in Every Bottle"
    - `description`: "100 mL of botanical body oil for your arms, legs, and body."
  - Block `statistic_ANN498` — type `statistic`
    - `value_text`: "2"
    - `title`: "Skincare Favorites"
    - `description`: "Squalane and vitamin E meet a nourishing blend of botanical oils."
  - Block `statistic_e4wQee` — type `statistic`
    - `value_text`: "1"
    - `title`: "Simple Daily Ritual"
    - `description`: "Massage onto slightly damp skin after showering. Let absorb before dressing."

### [DISABLED] Section `story` — type `image-with-text`
- `heading`: "A body oil, and"
- `heading_accent`: "not much else"
  - Block `secondary_image_Lar8jq` — type `secondary_image`
    - `image_alt`: "Descriptive image text"
  - Block `s_sub` — type `subtitle`
    - `subtitle_text`: "What it is"
  - Block `s_par` — type `paragraph`
    - `paragraph_text`: "<p>Falunara started with a small frustration: body care that felt like admin. Lotions that vanished into nothing, bottles that ran out in a month, scents that announced themselves from across the room.</p><p>Botanical Body Oil is the answer we wanted — something warm and quiet you press into damp skin and then forget about, except that you keep noticing it.</p>"
  - Block `s_list` — type `bullet_list`
    - `list_title`: "In short"
    - `list_item_1`: "Press it in rather than rubbing it in"
    - `list_item_1_svg`: (inline SVG icon — no text)
    - `list_item_2`: "Damp skin, straight out of the shower"
    - `list_item_2_svg`: (inline SVG icon — no text)
    - `list_item_3`: "Two or three pumps is usually enough"
    - `list_item_3_svg`: (inline SVG icon — no text)
    - `list_item_4`: "Give it a minute before you dress"
    - `list_item_4_svg`: (inline SVG icon — no text)
    - `list_item_5_svg`: (inline SVG icon — no text)
  - Block `s_btn` — type `button`
    - `button_label`: "Add to bag"
    - `button_link`: "#shopify-section-main"

### [DISABLED] Section `tabs` — type `content-tabs`
- `heading`: "Everything else"
- `accent_text`: "worth knowing"
- `subheading`: "<p>The practical detail, without the sales pitch.</p>"
  - Block `tab_use` — type `tab`
    - `tab_title`: "How to use"
    - `first_title`: "The two-minute version"
    - `first_text_content`: "<p>Shower. Pat yourself down until you are no longer dripping, but still damp. Warm two or three pumps in your palms and press the oil upward from your ankles to your shoulders. Wait a minute, then dress.</p><p>That is the whole thing. Nothing to layer on top.</p>"
    - `second_title`: "Small things that help"
    - `second_bullet_points`: "Apply while the bathroom is still warm, Press rather than rub, Use less on the backs of the knees, More on elbows and heels"
    - `second_benefits`: "Improves user experience, Saves time and effort, Provides excellent value"
  - Block `tab_where` — type `tab`
    - `tab_title`: "Where to use it"
    - `first_title`: "Below the jaw"
    - `first_text_content`: "<p>This is a body oil, so we would keep it below the jaw. It is made for the large, forgettable areas — the ones that get the least attention and show it first.</p>"
    - `second_title`: "Works well on"
    - `second_bullet_points`: "Arms and shoulders, Legs and shins, Chest and collarbones, Elbows and knees, Heels and feet"
    - `second_benefits`: "Improves user experience, Saves time and effort, Provides excellent value"
  - Block `tab_know` — type `tab`
    - `tab_title`: "Good to know"
    - `first_title`: "Before you buy"
    - `first_text_content`: "<p>Oil and fabric need a moment to get along. If you dress straight away you may notice a mark; give it a minute or two and you will not.</p><p>Store the bottle out of direct sunlight — a bathroom shelf away from the window is ideal.</p>"
    - `second_title`: "Key Benefits"
    - `second_benefits`: "Improves user experience, Saves time and effort, Provides excellent value"
  - [DISABLED] Block `tab_ingredients` — type `tab`
    - `tab_title`: "Ingredients"
    - `first_title`: "Full ingredient list"
    - `first_text_content`: "<p>Add the confirmed INCI list here.</p>"
    - `second_title`: "Key Benefits"
    - `second_benefits`: "Improves user experience, Saves time and effort, Provides excellent value"

### Section `features` — type `alternating-features`
- `title`: "Three things we"
- `title_accent`: "cared about"
  - Block `f1` — type `feature`
    - `title`: "The finish"
    - `description`: "The point of an oil is the first ten minutes and the eight hours after. It should stop feeling like something you put on."
  - Block `f2` — type `feature`
    - `title`: "The scent"
    - `description`: "Low and warm, and close to the skin. Noticeable when someone is near you, not when they walk into the room."
  - [DISABLED] Block `f3` — type `feature`
    - `title`: "The size"
    - `description`: "The 100 ml bottle is the perfect size for everyday body care."

### [DISABLED] Section `lifestyle_grid` — type `photo-grid`
- `title`: "Photo Collection"
- `title_primary`: "Falunara"
- `title_accent`: "in use"
- `view_count`: "5.6"
- `badge_text`: "Over"
- `badge_suffix`: "M Views On TikTok"
- `image_position`: "center center"
  - Block `p1` — type `image_item`
    - `custom_position`: "center center"
  - Block `p2` — type `image_item`
    - `custom_position`: "center center"
  - Block `p3` — type `image_item`
    - `custom_position`: "center center"
  - Block `p4` — type `image_item`
    - `custom_position`: "center center"
  - Block `p5` — type `image_item`
    - `custom_position`: "center center"
  - Block `p6` — type `image_item`
    - `custom_position`: "center center"

### [DISABLED] Section `reviews` — type `customer-reviews-carousel`
- `title_text`: "Customer"
- `accent_text`: "Reviews"
- `description_text`: "See what our customers are saying about our products"
- `verified_badge_text`: "Verified Buyer"
- `product_label`: "Item Purchased"
- `rating_prefix`: "Rated"
- `rating_number`: "4.8"
- `based_on_text`: "based on"
- `custom_review_count_text`: "+10,839 Total Ratings"
- `purchase_date_prefix`: "Purchased on"
- `rating_summary_gradient_direction`: "to right"

### Section `guarantee` — type `satisfaction-guarantee`
- `heading_risk_free`: "Money-Back"
- `heading_beauty_revolution`: "Guarantee"
- `description_text`: "We're so confident in the quality of our product that we offer a satisfaction guarantee. If you're not completely satisfied with your purchase, simply return the item within 30 days for a full refund."
- `product_name`: "Premium Product"
- `button_text`: "ADD TO CART"
- `benefit_1`: "100% Satisfaction"
- `benefit_2`: "Fast Shipping"
- `benefit_3`: "Easy Returns"
- `background`: "linear-gradient(90deg, rgba(255, 232, 236, 1), rgba(255, 249, 240, 1) 100%)"
- `section_gradient_direction`: "to right"
- `container_gradient_direction`: "to bottom"

### Section `faq` — type `store-faq`
- `heading`: "Questions, answered"
- `subtitle`: "<p>The things people actually ask before their first bottle.</p>"
  - Block `q1` — type `faq_item`
    - `question`: "Is this an oil or a lotion?"
    - `answer`: "<p>It is an oil. There is no water in it, which is why you use it on damp skin — the water is already there and the oil holds it in place.</p>"
  - Block `q2` — type `faq_item`
    - `question`: "Damp skin or dry skin?"
    - `answer`: "<p>Damp. Pat yourself with a towel until you are no longer dripping, then apply. On fully dry skin it takes longer to absorb and you will end up using more than you need.</p>"
  - Block `q3` — type `faq_item`
    - `question`: "Will it mark my clothes or my sheets?"
    - `answer`: "<p>Any body oil can if you dress before it has absorbed. Give it a minute or two and you will be fine. The same rule applies before you get into bed.</p>"
  - Block `q4` — type `faq_item`
    - `question`: "How much should I use?"
    - `answer`: "<p>Two or three pumps for the whole body is a sensible starting point. Use less on the backs of the knees and more on elbows, shins and heels.</p>"
  - Block `q5` — type `faq_item`
    - `question`: "Can I use it on my face?"
    - `answer`: "<p>This one is made for the body, so we would keep it below the jaw.</p>"
  - [DISABLED] Block `q_ing` — type `faq_item`
    - `question`: "What is in it?"
    - `answer`: "<p>Add the confirmed ingredient list here.</p>"
  - [DISABLED] Block `q_last` — type `faq_item`
    - `question`: "How long does a bottle last?"
    - `answer`: "<p>Add the confirmed usage duration here.</p>"
  - [DISABLED] Block `q_ship` — type `faq_item`
    - `question`: "Shipping and delivery"
    - `answer`: "<p>Add the confirmed shipping terms here.</p>"
  - [DISABLED] Block `q_ret` — type `faq_item`
    - `question`: "Returns and refunds"
    - `answer`: "<p>Add the confirmed returns policy here.</p>"

### [DISABLED] Section `closing_cta` — type `image-with-text`
- `heading`: "Start the"
- `heading_accent`: "ritual"
  - Block `c_par` — type `paragraph`
    - `paragraph_text`: "<p>Two minutes, most nights. Press it into damp skin, give it a moment, and get on with your evening.</p>"
  - Block `c_btn` — type `button`
    - `button_label`: "Add to bag"
    - `button_link`: "#shopify-section-main"

### Section `1789876088cf71a722` — type `_blocks`

### Section `1789876176d8b27025` — type `_blocks`

### [DISABLED] Section `customer_reviews_Fedj3c` — type `customer-reviews` — name "Image Reviews"
- `heading`: "Look At How Others Are Loving Their Product!"
- `subheading`: "Real Reviews From Real People"
- `button_text`: "CLAIM OFFER"
- `rating_text`: "Rated 4.8/5 by 1,319+ Happy Customers"
  - Block `review_image_jQmz7M` — type `review_image`
  - Block `review_image_ckFeEA` — type `review_image`
  - Block `review_image_wHgjh7` — type `review_image`
  - Block `review_image_ghwfDX` — type `review_image`

### Section `custom_liquid_UmXqin` — type `custom-liquid` — name "t:sections.custom-liquid.presets.name"

### Section `ss_testimonials_42_yU96KH` — type `ss-testimonials-42` — name "SS - Testimonials #42"
- `verify`: "Verified customer"
- `verify_font`: "josefin_sans_n4"
- `text_font`: "josefin_sans_n4"
- `author_font`: "josefin_sans_n4"
- `arrow_hover_effect`: "color"
- `background_gradient`: "linear-gradient(180deg, #FFFFFF 0%, #F2F2F2 100%)"
  - Block `sub_heading_gaPy6a` — type `sub_heading`
    - `sub_heading`: "<p><strong>Real experiences with FALUNARA Botanical Body Oil</strong></p><p></p>"
    - `sub_heading_font`: "josefin_sans_n4"
  - Block `heading_dPtD7d` — type `heading`
    - `heading`: "<p><strong>What Women Are Saying</strong></p>"
    - `heading_font`: "josefin_sans_n4"
    - `heading_accent_gradient`: "linear-gradient(180deg, #121212 0%, #333333 100%)"
  - Block `testimonial_AUnk7f` — type `testimonial`
    - `stars_count`: 5
    - `text`: "<p>I almost never leave reviews, even though I always read them before buying something online. But after comparing my before and after photos, I felt like I had to share. I was skeptical in the beginning, but I’m so glad I gave it a try. I didn’t realize how much my skin had changed until I looked back at the photo I took about 6 weeks ago. I still have some progress to make, but I’m really impressed so far.</p>"
    - `author`: "Laura S."
  - Block `testimonial_pNYDWX` — type `testimonial`
    - `stars_count`: 5
    - `text`: "<p>I’ve been using it consistently and my skin feels noticeably softer and more nourished. I especially love how healthy and smooth my arms look now.</p>"
    - `author`: "Evelyn K."
  - Block `testimonial_HzGjVi` — type `testimonial`
    - `stars_count`: 5
    - `text`: "<p>I honestly didn’t expect to notice this much of a difference. Since menopause, I’ve struggled with crepey-looking skin on my arms and stopped feeling comfortable in sleeveless tops. I’ve spent so much money trying different products with barely any improvement. I’m really happy I decided to try this.</p>"
    - `author`: "Kimberly C."
  - Block `testimonial_Dg7dMV` — type `testimonial`
    - `stars_count`: 5
    - `text`: "<p>I’m 67, and honestly, my skin looks so much smoother and more youthful now. I’m really happy with the difference!</p>"
    - `author`: "Lenny S."
  - Block `testimonial_eKCnnJ` — type `testimonial`
    - `stars_count`: 5
    - `text`: "<p>I’ve been using this for a couple of months now and already placed another order. My skin looks noticeably better and feels much smoother. I’ve been so happy with it that I even ordered a few bottles for my sister.</p>"
    - `author`: "Charlotte W."
  - Block `testimonial_aRMXmj` — type `testimonial`
    - `stars_count`: 5
    - `text`: "<p>My skin used to feel extremely dry no matter what moisturizer I used. This oil absorbs beautifully and leaves my skin feeling hydrated without that heavy, greasy feeling.</p>"
    - `author`: "Megan R."
  - Block `testimonial_tA8Fqt` — type `testimonial`
    - `stars_count`: 5
    - `text`: "<p>I started noticing the biggest difference after using it every day for a few weeks. My skin feels smoother, looks healthier, and I actually look forward to applying it after my shower.</p>"
    - `author`: "Diane M."
  - Block `testimonial_tiwBzr` — type `testimonial`
    - `stars_count`: 5
    - `text`: "<p>I was mainly looking for something to help with the dry, crepey look on my arms and legs. My skin feels much more moisturized now, and I’m really pleased with how it looks</p>"
    - `author`: "Susan T."

**Disabled in this file:** block `main` → `benefits` (benefits_grid); block `main` → `variant` (simple_variant_picker); block `main` → `video_carousel_standalone_X3wGnC` (video_carousel_standalone); block `main` → `review_quote` (customer_review); block `main` → `video_ugc` (video_carousel_standalone); block `main` → `video_shopify_1` (carousel_default_video); block `main` → `video_shopify_2` (carousel_default_video); block `main` → `video_shopify_3` (carousel_default_video); block `main` → `video_shopify_4` (carousel_default_video); block `main` → `video_shopify_5` (carousel_default_video); block `main` → `video_shopify_6` (carousel_default_video); block `main` → `labels` (product_labels); block `main` → `rating` (trustpilot_rating); block `main` → `bundles` (quantity_break); block `main` → `shipping` (shipping_notice); block `main` → `guarantee_badge` (custom_money_back); block `main` → `payments` (payment_icons); block `benefits` → `b4` (benefit); block `benefits` → `benefit_3fApJD` (benefit); section `statistics_grid_iVeXPU` (statistics-grid); section `story` (image-with-text); section `tabs` (content-tabs); block `tabs` → `tab_ingredients` (tab); block `features` → `f3` (feature); section `lifestyle_grid` (photo-grid); section `reviews` (customer-reviews-carousel); block `faq` → `q_ing` (faq_item); block `faq` → `q_last` (faq_item); block `faq` → `q_ship` (faq_item); block `faq` → `q_ret` (faq_item); section `closing_cta` (image-with-text); section `customer_reviews_Fedj3c` (customer-reviews)

## `templates/index.json`

### Section `hero` — type `new-hero`
- `gradient_direction`: "to right"
- `badge_text`: "BOTANICAL BODY OIL"
- `rating_value`: "4.8/5"
- `review_count`: "137,135"
- `heading`: "Body care worth"
- `heading_accent`: "slowing down for"
- `benefit_1_text`: "Press it into damp skin, straight out of the shower"
- `benefit_2_text`: "One oil for arms, legs, chest and the dry patches"
- `benefit_3_text`: "Two sizes — 100 ml for the shelf, 200 ml when it sticks"
- `button_text`: "Shop Botanical Body Oil"
- `button_link`: "/products/botanical-body-oil"
- `guarantee_text`: "30-Day Money-Back Guarantee"
- `container_gradient_direction`: "to bottom"

### Section `benefitbar` — type `scrolling-features-bar`
  - Block `h1` — type `feature_item`
    - `text`: "Press into damp skin"
    - `icon`: (inline SVG icon — no text)
  - Block `h2` — type `feature_item`
    - `text`: "One oil, head to toe"
    - `icon`: (inline SVG icon — no text)
  - Block `h3` — type `feature_item`
    - `text`: "100 ml / 3.4 fl oz"
    - `icon`: (inline SVG icon — no text)
  - Block `h4` — type `feature_item`
    - `text`: "Morning or night"
    - `icon`: (inline SVG icon — no text)

### Section `product` — type `featured-product-details`
- `featured_product`: "botanical-body-oil"
- `social_platform`: "tiktok"
- `badge_text`: "Over"
- `badge_suffix`: "M Views On TikTok"
  - Block `p_title` — type `title`
    - `custom_title`: "Custom Product Title"
  - Block `p_price` — type `price`
  - Block `p_bullets` — type `bullet_list`
    - `bullet_1`: "An oil, not a lotion — no water in the bottle"
    - `bullet_2`: "Goes on damp skin and settles in a minute"
    - `bullet_3`: "Everywhere below the jaw, morning or night"
    - `gradient_direction`: "to right"
  - Block `p_atc` — type `add_to_cart`
    - `button_text_override`: "Add to bag"
  - [DISABLED] Block `p_video_1` — type `carousel_default_video`
  - [DISABLED] Block `p_video_reel` — type `video_carousel_standalone`
    - `heading`: "See it in action"
    - `social_platform`: "tiktok"
    - `badge_text`: "Over"
    - `badge_suffix`: "M Views On TikTok"

### Section `routine` — type `image-with-text`
- `heading`: "A ritual, not"
- `heading_accent`: "another step"
  - Block `r_sub` — type `subtitle`
    - `subtitle_text`: "Every evening"
  - Block `r_par` — type `paragraph`
    - `paragraph_text`: "<p>Most of us do body care in the ninety seconds before we get dressed, half paying attention. This is built for the other version of that — the one where you take a minute, press the oil in properly, and let it settle before you move on.</p>"
  - Block `r_list` — type `bullet_list`
    - `list_title`: "The habit"
    - `list_item_1`: "Straight out of the shower, skin still damp"
    - `list_item_1_svg`: (inline SVG icon — no text)
    - `list_item_2`: "Two or three pumps warmed between your palms"
    - `list_item_2_svg`: (inline SVG icon — no text)
    - `list_item_3`: "Press upward, then wait a minute before dressing"
    - `list_item_3_svg`: (inline SVG icon — no text)
    - `list_item_4_svg`: (inline SVG icon — no text)
    - `list_item_5_svg`: (inline SVG icon — no text)
  - Block `r_btn` — type `button`
    - `button_label`: "Shop Botanical Body Oil"
    - `button_link`: "/products/botanical-body-oil"

### Section `texture` — type `alternating-features`
- `title`: "Texture,"
- `title_accent`: "up close"
  - Block `x1` — type `feature`
    - `title`: "An oil, not an emulsion"
    - `description`: "There is no water in the bottle. That is why it goes onto damp skin rather than dry, and why a small amount covers more than you expect."
  - Block `x2` — type `feature`
    - `title`: "Warm before it touches you"
    - `description`: "Rubbed between the palms for a second first, it goes on at skin temperature instead of cold out of the bottle."
  - Block `x3` — type `feature`
    - `title`: "Made to disappear"
    - `description`: "Pressed in rather than rubbed in, it settles within a minute or two — long before you need to get dressed."

### Section `howto` — type `steps`
- `title`: "Three steps,"
- `title_highlight`: "two minutes"
- `subtitle`: "The whole routine, start to finish. It works best when you do not rush it."
  - Block `s1` — type `step`
    - `step_title`: "Shower, then wait"
    - `step_description`: "Pat yourself down until you are no longer dripping. You want skin that is still slightly damp."
  - Block `s2` — type `step`
    - `step_title`: "Warm it first"
    - `step_description`: "Two or three pumps into your palms, rubbed together for a second so it does not go on cold."
  - Block `s3` — type `step`
    - `step_title`: "Press, do not rub"
    - `step_description`: "Work upward from the ankles. Give it a minute to settle before you get dressed."

### [DISABLED] Section `grid` — type `photo-grid`
- `title`: "Photo Collection"
- `title_primary`: "Falunara,"
- `title_accent`: "up close"
- `view_count`: "5.6"
- `badge_text`: "Over"
- `badge_suffix`: "M Views On TikTok"
- `image_position`: "center center"
  - Block `g1` — type `image_item`
    - `custom_position`: "center center"
    - `link`: "/products/botanical-body-oil"
  - Block `g2` — type `image_item`
    - `custom_position`: "center center"
    - `link`: "/products/botanical-body-oil"
  - Block `g3` — type `image_item`
    - `custom_position`: "center center"
    - `link`: "/products/botanical-body-oil"

### Section `brand` — type `image-with-text`
- `heading`: "What Falunara"
- `heading_accent`: "is for"
  - Block `b_par` — type `paragraph`
    - `paragraph_text`: "<p>Falunara makes body care for the parts of the routine nobody photographs. Not a ten-step ritual, not a shelf of bottles — one good oil and two minutes at the end of the day.</p><p>We would rather do a small number of things properly than release something new every season. Botanical Body Oil is where we started.</p>"
  - Block `b_btn` — type `button`
    - `button_label`: "Shop Botanical Body Oil"
    - `button_link`: "/products/botanical-body-oil"

### Section `faq` — type `store-faq`
- `heading`: "Before you buy"
- `subtitle`: "<p>The questions people actually ask about a body oil.</p>"
  - Block `f1` — type `faq_item`
    - `question`: "Is this an oil or a lotion?"
    - `answer`: "<p>An oil. There is no water in it, which is why you use it on damp skin — the water is already there and the oil holds it in place.</p>"
  - Block `f2` — type `faq_item`
    - `question`: "Damp skin or dry skin?"
    - `answer`: "<p>Damp. Towel off until you are no longer dripping, then apply. On fully dry skin it takes longer to absorb and you will use more than you need.</p>"
  - Block `f3` — type `faq_item`
    - `question`: "Will it mark my clothes or sheets?"
    - `answer`: "<p>Any body oil can if you dress before it has absorbed. Give it a minute or two and you will be fine — the same applies before getting into bed.</p>"
  - Block `f4` — type `faq_item`
    - `question`: "Which size should I start with?"
    - `answer`: "<p>100 ml is the everyday bottle and the easier first purchase. 200 ml makes sense once it has become the one you reach for.</p>"
  - Block `f5` — type `faq_item`
    - `question`: "Can I use it on my face?"
    - `answer`: "<p>This one is made for the body, so we would keep it below the jaw.</p>"
  - [DISABLED] Block `f_ing` — type `faq_item`
    - `question`: "What is in it?"
    - `answer`: "<p>Add the confirmed ingredient list here.</p>"
  - [DISABLED] Block `f_ship` — type `faq_item`
    - `question`: "Shipping and delivery"
    - `answer`: "<p>Add the confirmed shipping terms here.</p>"
  - [DISABLED] Block `f_ret` — type `faq_item`
    - `question`: "Returns and refunds"
    - `answer`: "<p>Add the confirmed returns policy here.</p>"

### Section `alternating_features_9wEzGD` — type `alternating-features`
- `title`: "Three things we"
- `title_accent`: "cared about"
  - Block `feature_UBWTi4` — type `feature`
    - `title`: "The finish"
    - `description`: "The point of an oil is the first ten minutes and the eight hours after. It should stop feeling like something you put on."
  - Block `feature_Ltwfnf` — type `feature`
    - `title`: "The scent"
    - `description`: "Low and warm, and close to the skin. Noticeable when someone is near you, not when they walk into the room."
  - Block `feature_MdKTbi` — type `feature`
    - `title`: "The size"
    - `description`: "The 100 ml bottle is the perfect size for everyday body care."

**Disabled in this file:** block `product` → `p_video_1` (carousel_default_video); block `product` → `p_video_reel` (video_carousel_standalone); section `grid` (photo-grid); block `faq` → `f_ing` (faq_item); block `faq` → `f_ship` (faq_item); block `faq` → `f_ret` (faq_item)

## `sections/header-group.json`

### Section `custom_announcement_bar_KbrQgt` — type `custom-announcement-bar`
- `text`: "Falunara — made for the minute after the shower"

### [DISABLED] Section `announcement_bar_W34fB6` — type `announcement-bar` — name "Countdown Banner"
- `end_date`: "2023-12-31 23:59:59"
- `days_label`: "DAYS"
- `hours_label`: "HRS"
- `minutes_label`: "MIN"
- `seconds_label`: "SEC"

### Section `header` — type `header`
- `menu`: "main-menu"
- `menu_type_desktop`: "dropdown"

**Disabled in this file:** section `announcement_bar_W34fB6` (announcement-bar)

## `sections/footer-group.json`

### Section `footer` — type `footer`
- `newsletter_heading`: "Subscribe to our emails"

**Disabled in this file:** none

## `templates/cart.json`
Cart page. No custom strings; all text comes from theme locale defaults. The store uses `cart_type: drawer` (settings_data), so the cart drawer is the main cart UI. It has no stored text settings: `show_social_proof_bar` false, `show_discount_banner` false, `product_free_show` false, `show_cart_drawer_payment_icons` false, `product_shipping_protection` empty.

### Section `cart-items` — type `main-cart-items`

### Section `cart-footer` — type `main-cart-footer`
  - Block `subtotal` — type `subtotal`
  - Block `buttons` — type `buttons`

**Disabled in this file:** none

## `templates/page.json`
Page text comes from the Shopify Page content (Online Store > Pages), not the theme. Contact form heading is empty.

### Section `main` — type `main-page`

**Disabled in this file:** none

## `templates/page.contact.json`
Page text comes from the Shopify Page content (Online Store > Pages), not the theme. Contact form heading is empty.

### Section `main` — type `main-page`

### Section `form` — type `contact-form`

**Disabled in this file:** none

## `templates/page.new.json`
Page text comes from the Shopify Page content (Online Store > Pages), not the theme. Contact form heading is empty.

### Section `main` — type `main-page`

**Disabled in this file:** none

## `templates/collection.json`

### Section `collection_banner_main` — type `collection-banner`
- `heading`: "{{ collection.title }}"

### Section `collection_grid_page_hDiTDB` — type `collection-grid-page` — name "Collection Grid"
- `collection`: "frontpage"
- `heading`: "Featured Collection"
- `rating_value`: 5
- `rating_number`: "4.7"
- `rating_text_weight`: "normal"
- `metadata_label_weight`: "bold"
- `collection_all_text`: "Shop All"
- `sort_label`: "Sort by:"
  - Block `collection_WrhcNq` — type `collection`
    - `collection`: "theme"
  - Block `collection_DeXYCy` — type `collection`
    - `collection`: "theme"
  - Block `collection_YMWkGQ` — type `collection`
    - `collection`: "theme"
  - Block `collection_y683B8` — type `collection`
    - `collection`: "frontpage"
  - Block `collection_gYmDKn` — type `collection`
    - `collection`: "theme"

### [DISABLED] Section `banner` — type `main-collection-banner`

### [DISABLED] Section `product-grid` — type `main-collection-product-grid`
- `quick_add`: "none"

### Section `newsletter_xRjFbi` — type `newsletter` — name "t:sections.newsletter.presets.name"
  - Block `heading_h66giP` — type `heading`
    - `heading`: "Subscribe to our emails"
  - Block `paragraph_q4ebfh` — type `paragraph`
    - `text`: "<p>Be the first to know about new collections and exclusive offers.</p>"
  - Block `email_form_crJR9K` — type `email_form`

**Disabled in this file:** section `banner` (main-collection-banner); section `product-grid` (main-collection-product-grid)

## `templates/search.json`

### Section `main` — type `main-search`

**Disabled in this file:** none

## `templates/404.json`

### Section `main` — type `main-404`

**Disabled in this file:** none

## `templates/password.json`

### Section `main` — type `email-signup-banner`
  - Block `heading` — type `heading`
    - `heading`: "Opening soon"
  - Block `paragraph` — type `paragraph`
    - `text`: "<p>Be the first to know when we launch.</p>"
  - Block `email_form` — type `email_form`

**Disabled in this file:** none

## `templates/list-collections.json`

### Section `main` — type `main-list-collections`
- `title`: "Collections"
- `sort`: "alphabetical"

**Disabled in this file:** none

## `templates/article.json`

### Section `main` — type `main-article`
  - Block `featured_image` — type `featured_image`
  - Block `title` — type `title`
  - Block `share` — type `share`
    - `share_label`: "Share"
  - Block `content` — type `content`

**Disabled in this file:** none

## `templates/blog.json`

### Section `main` — type `main-blog`

**Disabled in this file:** none

## `templates/product.milk-thistle.json`
[MT] Alternate template, **not assigned** to any product. It can be rendered with `?view=milk-thistle`.

### Section `trust_bar` — type `scrolling-features-bar`
  - Block `trust_guarantee` — type `feature_item`
    - `text`: "90-DAY MONEY-BACK GUARANTEE"
    - `icon`: (inline SVG icon — no text)
  - Block `trust_silymarin` — type `feature_item`
    - `text`: "80% STANDARDIZED SILYMARIN"
    - `icon`: (inline SVG icon — no text)
  - Block `trust_shipping` — type `feature_item`
    - `text`: "FREE U.S. SHIPPING"
    - `icon`: (inline SVG icon — no text)
  - Block `trust_formula` — type `feature_item`
    - `text`: "TRANSPARENT FORMULA"
    - `icon`: (inline SVG icon — no text)

### Section `main` — type `shop-product-details`
  - Block `pdp_styles` — type `custom_liquid`
    - `custom_liquid`: "{{ 'veilkind-pdp.css' | asset_url | stylesheet_tag }}"
  - Block `title` — type `title`
    - `custom_title`: "Milk Thistle Complex"
  - Block `trustpilot_rating_YWWnA6` — type `trustpilot_rating`
    - `rating_text`: "Excellent"
    - `rating_score`: "4.7 out of 5"
    - `background_gradient_direction`: "to right"
  - Block `subtitle` — type `custom_text`
    - `text`: "<p>Daily liver support built on milk thistle extract standardized to 80% silymarin, with turmeric, artichoke and inositol.</p>"
    - `description`: "<p>Add additional descriptive text here</p>"
    - `custom_icon`: (inline SVG icon — no text)
  - Block `labels` — type `product_labels`
    - `label_1_name`: "80% Silymarin"
    - `label_1_serving_count`: "Additional Info"
    - `label_2_name`: "Vegetarian Capsules"
    - `label_2_serving_count`: "Additional Info"
    - `label_3_serving_count`: "Additional Info"
  - Block `divider_top` — type `divider`
  - Block `price` — type `price`
  - Block `benefits` — type `benefits_grid`
    - `benefit_1_text`: "Supports Healthy Liver Function"
    - `benefit_1_custom_icon`: (inline SVG icon — no text)
    - `benefit_2_text`: "Supports Comfortable Digestion"
    - `benefit_2_custom_icon`: (inline SVG icon — no text)
    - `benefit_3_text`: "Antioxidant Support From Silymarin"
    - `benefit_3_custom_icon`: (inline SVG icon — no text)
    - `benefit_4_text`: "Simple Daily Routine"
    - `benefit_4_custom_icon`: (inline SVG icon — no text)
  - Block `divider_buy` — type `divider`
  - [DISABLED] Block `supply_label` — type `custom_text`
    - `text`: "<p><strong>Choose your supply</strong></p>"
    - `description`: "<p>Add additional descriptive text here</p>"
    - `custom_icon`: (inline SVG icon — no text)
  - [DISABLED] Block `variant_picker` — type `simple_variant_picker`
    - `size_option_label`: "Size"
    - `custom_option_label_1`: "Supply"
    - `custom_color_mappings`: "red=#FF0000\nblue=#0000FF\ngreen=#00FF00\nyellow=#FFFF00\nblack=#000000\nwhite=#FFFFFF"
  - [DISABLED] Block `quantity` — type `quantity_selector`
  - Block `add_to_cart` — type `add_to_cart`
    - `button_text_override`: "ADD TO CART"
  - Block `payment_icons` — type `payment_icons`
  - Block `guarantee_badges` — type `guarantee_badges`
    - `badge_1_text`: "90-Day Money-Back Guarantee"
    - `badge_2_text`: "Free U.S. Shipping"
  - Block `money_back` — type `custom_money_back`
    - `title_text`: "Try it for 90 days"
    - `description_text`: "Take it as part of your daily routine. If it isn't for you, contact us within 90 days of delivery and we'll refund your order — bottle open or not."
    - `badge_svg`: (inline SVG icon — no text)
  - Block `quick_faq` — type `product_faq`
    - `question_1`: "What's in it"
    - `answer_1`: "<p>Milk thistle extract standardized to 80% silymarin, plus turmeric, artichoke and inositol. Every active and its amount is printed on the label — no proprietary blend.</p>"
    - `question_2`: "How to take it"
    - `answer_2`: "<p>Take [SERVING SIZE] daily with a glass of water, ideally at the same time each day. Consistency matters more than timing.</p>"
    - `question_3`: "Shipping & returns"
    - `answer_3`: "<p>Free shipping within the United States. If it isn't for you, contact us within 90 days of delivery for a refund.</p>"
    - `question_4`: "Does it really work?"
    - `answer_4`: "<p>Information about efficacy goes here.</p>"
    - `question_5`: "What is the 100% results guarantee?"
    - `answer_5`: "<p>Details about the guarantee go here.</p>"

### Section `ugc_videos` — type `customer-reviews`
- `heading`: "A routine people actually keep"
- `subheading`: "Short clips showing where VEILKIND fits into an ordinary morning. Swipe to watch."
- `button_text`: "ADD TO CART"
- `rating_text`: "Rated [4.8]/5 by [REVIEW COUNT] customers"
  - Block `ugc_1` — type `review_image`
    - `review_video_url`: "https://cdn.shopify.com/s/files/1/1038/2285/2439/files/veilkind-ugc-1.mp4?v=1786910034"
    - `caption`: "Example customer clip"
  - Block `ugc_2` — type `review_image`
    - `review_video_url`: "https://cdn.shopify.com/s/files/1/1038/2285/2439/files/veilkind-ugc-2b.mp4?v=1786921073"
    - `caption`: "Example customer clip"
  - Block `ugc_3` — type `review_image`
    - `review_video_url`: "https://cdn.shopify.com/s/files/1/1038/2285/2439/files/veilkind-ugc-3.mp4?v=1786910182"
    - `caption`: "Example customer clip"
  - Block `ugc_4` — type `review_image`
    - `review_video_url`: "https://cdn.shopify.com/s/files/1/1038/2285/2439/files/veilkind-ugc-4b.mp4?v=1786921073"
    - `caption`: "How the daily routine looks"

### Section `why_it_works` — type `product-benefits`
- `list_gradient_direction`: "to bottom"
- `heading_accent`: "Why"
- `heading_regular`: "this formula is built the way it is"
- `subtitle`: "Most milk thistle products tell you the herb is in there. Very few tell you how much of the active you are actually getting. That difference is the whole point of this formula."
- `image_alt`: "VEILKIND bottle with vegetarian capsules"
  - Block `why_1` — type `benefit`
    - `title`: "Standardized, not guessed"
    - `description`: "Milk thistle seed varies from harvest to harvest. Ours is extracted and standardized to 80% silymarin, so the amount of active compound in your capsule is a defined number rather than whatever the batch happened to contain."
    - `custom_icon_svg`: (inline SVG icon — no text)
  - Block `why_2` — type `benefit`
    - `title`: "Four actives that work as a set"
    - `description`: "Milk thistle carries the formula. Turmeric, artichoke and inositol sit alongside it — chosen because they are the botanicals most often paired with silymarin in a liver and digestion routine, not to pad the label."
    - `custom_icon_svg`: (inline SVG icon — no text)
  - Block `why_3` — type `benefit`
    - `title`: "One step, once a day"
    - `description`: "No powders to mix, no three-times-daily schedule to remember. You take it with water when you already do something else — which is the only reason any supplement routine survives past week two."
    - `custom_icon_svg`: (inline SVG icon — no text)
  - Block `why_4` — type `benefit`
    - `title`: "Nothing hidden behind a blend"
    - `description`: "Every active and its amount is printed on the label. If a formula hides its doses inside a proprietary blend, you have no way to compare it against anything — including this one."
    - `custom_icon_svg`: (inline SVG icon — no text)

### Section `ingredients` — type `alternating-features`
- `title`: "Four ingredients."
- `title_accent`: "Every amount on the label."
  - Block `ing_1` — type `feature`
    - `title`: "Milk Thistle — standardized to 80% silymarin"
    - `description`: "The backbone of the formula. Silymarin is the group of compounds from the milk thistle seed that the plant is actually valued for, and standardizing to 80% is what turns contains milk thistle into a number you can check."
  - Block `ing_2` — type `feature`
    - `title`: "Turmeric"
    - `description`: "A root used in kitchens and herbal traditions for centuries, included here for its own antioxidant compounds. It is the ingredient most commonly paired with milk thistle in a daily wellness routine."
  - Block `ing_3` — type `feature`
    - `title`: "Artichoke"
    - `description`: "Artichoke leaf has a long history in European herbalism as part of a digestive routine. It rounds out the formula rather than competing with the milk thistle for space on the label."
  - Block `ing_4` — type `feature`
    - `title`: "Inositol"
    - `description`: "A naturally occurring compound found in foods such as citrus fruit and beans. It is the one non-botanical in the formula, included to support the everyday wellness side of the routine."

### Section `formula_facts` — type `statistics-grid`
- `heading_part_1`: "The formula,"
- `heading_part_2`: "in four numbers"
- `subheading`: "No clinical claims and no invented percentages — just what is actually in the bottle."
- `container_gradient_direction`: "to bottom"
  - Block `fact_1` — type `statistic`
    - `title`: "Standardized Silymarin"
    - `description`: "The milk thistle extract is standardized to 80% silymarin, so every batch delivers the same defined amount."
  - Block `fact_2` — type `statistic`
    - `title`: "Vegetarian Capsule"
    - `description`: "A plant-based capsule shell rather than gelatin, so the formula suits more people."
  - Block `fact_3` — type `statistic`
    - `title`: "Doses On The Label"
    - `description`: "Every active ingredient and its amount is printed on the bottle, so you can compare it against anything."
  - Block `fact_4` — type `statistic`
    - `title`: "Proprietary Blends"
    - `description`: "None. Nothing in this formula hides behind a blend name that conceals how much you are actually getting."

### Section `lifestyle` — type `image-with-text`
- `heading`: "A quieter kind of"
- `heading_accent`: "daily upkeep."
  - Block `lifestyle_copy` — type `paragraph`
    - `paragraph_text`: "<p>Nobody starts a supplement because they want another bottle on the counter. They start because they want the ordinary parts of the day to feel less like work — the morning, the meal out, the week that ran long.</p><p>VEILKIND is built for that: one capsule, taken at the same time each day, as part of a routine you keep rather than a programme you finish.</p>"
  - Block `lifestyle_cta` — type `button`
    - `button_label`: "Start your routine"

### Section `journey` — type `steps`
- `title`: "What the first"
- `title_highlight`: "90 days look like"
- `subtitle`: "This is about building a routine, not hitting milestones. Everyone's experience differs — what follows is simply how the habit tends to form."
  - Block `step_1` — type `step`
    - `step_title`: "Week one — pick your moment"
    - `step_description`: "Take it with water at a point in the day you never skip: with breakfast, or right after you make coffee. Attaching it to something existing is what makes it stick."
  - Block `step_2` — type `step`
    - `step_title`: "Weeks two to four — it stops being a decision"
    - `step_description`: "By the third or fourth week most people are no longer reminding themselves. The bottle lives where the routine happens and taking it is automatic."
  - Block `step_3` — type `step`
    - `step_title`: "Month two onward — keep it going"
    - `step_description`: "Milk thistle is a daily-habit supplement, not a course you finish. People who keep a multi-bottle supply on the shelf are the ones who never fall out of the routine."

### Section `testimonials` — type `customer-reviews-carousel`
- `title_text`: "What customers"
- `accent_text`: "say"
- `description_text`: "Placeholder cards — connect your review app or paste real reviews before publishing."
- `verified_badge_text`: "Verified Buyer"
- `product_label`: "Item Purchased"
- `rating_prefix`: "Rated"
- `rating_number`: "4.7"
- `based_on_text`: "based on"
- `custom_review_count_text`: "73.000 reviews"
- `purchase_date_prefix`: "Purchased on"
- `rating_summary_gradient_direction`: "to bottom"
  - Block `review_1` — type `review`
    - `image_position`: "center center"
    - `rating`: 5
    - `review_text`: "[PLACEHOLDER — replace with a real verified review. Do not publish this section until genuine customer reviews are connected.]"
    - `reviewer_name`: "[CUSTOMER NAME]"
    - `product_title`: "Milk Thistle Complex"
    - `product_price`: "$29.99"
    - `product_compare_price`: "$39.99"
    - `purchase_date`: "March 14th, 2025"
  - Block `review_2` — type `review`
    - `image_position`: "center center"
    - `rating`: 5
    - `review_text`: "[PLACEHOLDER — replace with a real verified review. Do not publish this section until genuine customer reviews are connected.]"
    - `reviewer_name`: "[CUSTOMER NAME]"
    - `product_title`: "Milk Thistle Complex"
    - `product_price`: "$29.99"
    - `product_compare_price`: "$39.99"
    - `purchase_date`: "March 14th, 2025"
  - Block `review_3` — type `review`
    - `image_position`: "center center"
    - `rating`: 5
    - `review_text`: "[PLACEHOLDER — replace with a real verified review. Do not publish this section until genuine customer reviews are connected.]"
    - `reviewer_name`: "[CUSTOMER NAME]"
    - `product_title`: "Milk Thistle Complex"
    - `product_price`: "$29.99"
    - `product_compare_price`: "$39.99"
    - `purchase_date`: "March 14th, 2025"

### Section `comparison` — type `product-comparison`
- `title_part_1`: "How it compares"
- `subheading`: "Measured against the generic milk thistle capsules you'll find on most shelves."
  - Block `col_ours` — type `product_column`
    - `product_name`: "VEILKIND"
    - `product_subtitle`: "Milk Thistle Complex"
  - Block `col_others` — type `product_column`
    - `product_name`: "Typical alternatives"
    - `product_subtitle`: "Generic milk thistle"
  - Block `row_1` — type `feature_row`
    - `feature_name`: "Extract standardized to 80% silymarin"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "Varies"
  - Block `row_2` — type `feature_row`
    - `feature_name`: "Turmeric, artichoke and inositol included"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "Rarely"
  - Block `row_3` — type `feature_row`
    - `feature_name`: "Every amount printed on the label"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "Often a blend"
  - Block `row_4` — type `feature_row`
    - `feature_name`: "Vegetarian capsule"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "Often gelatin"
  - Block `row_5` — type `feature_row`
    - `feature_name`: "Simple once-a-day routine"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "Yes"
    - `value_2`: "no"
    - `text_value_2`: "Varies"
  - Block `row_6` — type `feature_row`
    - `feature_name`: "Money-back window"
    - `feature_icon`: (inline SVG icon — no text)
    - `value_1`: "yes"
    - `text_value_1`: "90 days"
    - `value_2`: "no"
    - `text_value_2`: "30 days typical"

### Section `guarantee` — type `satisfaction-guarantee`
- `heading_risk_free`: "90 days,"
- `heading_beauty_revolution`: "no argument"
- `description_text`: "Take it for three months. If it hasn't earned its place in your routine, email us within 90 days of delivery and we'll refund the order — you don't need to send back an unopened bottle, and you don't need to explain yourself."
- `product_name`: "Milk Thistle Complex"
- `button_text`: "ADD TO CART"
- `benefit_1`: "90-Day Refund Window"
- `benefit_2`: "Free U.S. Shipping"
- `benefit_3`: "Real Human Support"
- `background`: "linear-gradient(to right, #FFE8EC, #FFF9F0)"
- `section_gradient_direction`: "to right"
- `container_gradient_direction`: "to bottom"

### Section `faq` — type `store-faq`
- `heading`: "Questions, answered"
- `subtitle`: "<p>If something isn't covered here, email us — a person replies.</p>"
  - Block `faq_1` — type `faq_item`
    - `question`: "What is milk thistle?"
    - `answer`: "<p>Milk thistle (<em>Silybum marianum</em>) is a flowering plant that has been used in European herbal traditions for a very long time. The part that matters is the seed, which contains a group of plant compounds called silymarin.</p>"
  - Block `faq_2` — type `faq_item`
    - `question`: "What does 80% silymarin actually mean?"
    - `answer`: "<p>Silymarin is the active compound group in the milk thistle seed. Standardizing the extract to 80% silymarin means 80% of the extract is that compound group — so each batch delivers the same defined amount instead of varying with the harvest.</p><p>Plain milk thistle powder isn't standardized at all, which is why two products can list the same herb and deliver very different amounts of the thing you actually want.</p>"
  - Block `faq_3` — type `faq_item`
    - `question`: "What's in the formula?"
    - `answer`: "<p>Four actives: milk thistle extract standardized to 80% silymarin, turmeric, artichoke and inositol. Each one and its amount is printed on the label — there's no proprietary blend.</p>"
  - Block `faq_4` — type `faq_item`
    - `question`: "How and when do I take it?"
    - `answer`: "<p>Take [SERVING SIZE] daily with a glass of water. Most people take it in the morning with food, but the specific time matters far less than taking it at the same time each day.</p><p><em>Store owner: confirm the serving size against the finished label before publishing.</em></p>"
  - Block `faq_5` — type `faq_item`
    - `question`: "How long does one bottle last?"
    - `answer`: "<p>One bottle contains [CAPSULE COUNT] capsules, which is [X] days at the suggested serving. The 3- and 6-bottle options exist so you don't run out mid-routine.</p><p><em>Store owner: confirm the capsule count against the finished label before publishing.</em></p>"
  - Block `faq_6` — type `faq_item`
    - `question`: "Is it vegetarian?"
    - `answer`: "<p>Yes — the capsule shell is plant-based rather than gelatin.</p><p><em>Store owner: confirm this against your manufacturer's specification before publishing.</em></p>"
  - Block `faq_7` — type `faq_item`
    - `question`: "Should I check with my doctor first?"
    - `answer`: "<p>Yes, if you're pregnant or nursing, taking prescription medication, or managing a medical condition. This is a dietary supplement, not a treatment, and it isn't intended to diagnose, treat, cure or prevent any disease.</p>"
  - Block `faq_8` — type `faq_item`
    - `question`: "What if it isn't for me?"
    - `answer`: "<p>Email us within 90 days of delivery and we'll refund the order. An opened bottle is fine — that's the point of a 90-day window.</p>"

### Section `final_cta` — type `featured-product-details`
- `featured_product`: "placeholder-product"
- `social_platform`: "tiktok"
- `badge_text`: "Over"
- `badge_suffix`: "M Views On TikTok"
  - Block `cta_title` — type `title`
    - `custom_title`: "Milk Thistle Complex"
  - Block `cta_reviews` — type `reviews`
    - `rating_label`: "Rated"
    - `custom_rating`: "[4.8]"
    - `custom_rating_count`: "[REVIEW COUNT]"
    - `satisfaction_text`: "90-Day Guarantee"
  - Block `cta_bullets` — type `bullet_list`
    - `bullet_1`: "80% standardized silymarin"
    - `bullet_2`: "Turmeric, artichoke and inositol"
    - `bullet_3`: "One capsule, once a day"
    - `gradient_direction`: "to right"
  - Block `cta_price` — type `price`
  - Block `cta_variants` — type `simple_variant_picker`
    - `size_option_label`: "Size"
  - Block `cta_button` — type `add_to_cart`
    - `button_text_override`: "ADD TO CART"
  - Block `cta_guarantee` — type `guarantee_badges`
    - `badge_1_text`: "90-Day Money-Back Guarantee"
    - `badge_2_text`: "Free U.S. Shipping"

### Section `sticky_atc` — type `sticky-add-to-cart`
- `button_text`: "ADD TO CART"
- `rating_text`: "Rated [4.8] | [REVIEW COUNT] reviews"
- `delivery_date_display_format`: "weekday_month_day"
- `delivery_text_prefix`: "Get It By"

**Disabled in this file:** block `main` → `supply_label` (custom_text); block `main` → `variant_picker` (simple_variant_picker); block `main` → `quantity` (quantity_selector)

## `config/settings_data.json`
**App embed blocks (`current.blocks`):**
- `15557474716127144420`: type `shopify://apps/kaching-bundles/blocks/app-embed-block/6c637362-a106-4a32-94ac-94dcfd68cdb8`, disabled: false (**enabled**), settings: `{}` (none stored in the theme)
- `2724325275511621162`: type `shopify://apps/kaching-subscriptions/blocks/app-embed-block/1fa39fd7-f6a3-4bbc-9383-7d91d27b44f5`, disabled: false (**enabled**), settings: `{}` (none stored in the theme; labels and default selection live in the Kaching app)

**Customer-visible text settings:**
- `brand_headline`: "" (empty)
- `brand_description`: "<p></p>" (empty)
- `discount_banner_suffix`: "" (empty)
- `product_shipping_protection`: "" (empty)
- `cart_drawer_sp_icon`: "" (empty)
- All social links are empty.
- `money_back_guarantee_icon`: "shield" (icon only)
- `logo`: shopify://shop_images/LOGOLOGLO.png

**Toggles affecting text:**
- `show_social_proof_bar`: false
- `show_discount_banner`: false
- `product_free_show`: false (`product_free_shipping`: 40, `product_free_amount`: 60)
- `show_cart_drawer_payment_icons`: false
- `cart_type`: "drawer"
- `currency_code_enabled`: true

**Password-page sections** (`main-password-header`, `main-password-footer`) have no settings.

`platform_customizations.custom_css` only bolds `.custom-text-block-custom_text_L3wXdj`. No block with that id exists in the current templates.
