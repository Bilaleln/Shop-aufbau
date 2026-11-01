# 03 – Competitor & Market Landscape + Ad Research (Núan Ritual Candle)

Research date: 2026-11-01. Scope: Step 3 of the market-research framework, covering direct competitors, candle-warmer competitors, indirect categories, ad research, market data, seasonality, guarantees and objections.

**Method and honesty notes (read first)**
- Every claim below carries a source link. Where I could not verify something, I say so. I did not invent any quotes, prices, URLs or ad data.
- Prices are snapshots from brand or retailer pages on or around 2026-11-01. Many were sale prices, and UK brands are quoted in GBP.
- **Trendtrack credits were exhausted.** `check_credits` returned `includedQuota.limit 10000, used 10000, remaining 0` (the billing period resets 2026-11-10). As a result `search_ads` and `search_advertisers` failed with "Not enough credits". Only the free `lookup` endpoint worked. It returns advertiser-level signals (active ad count, 30-day reach, Facebook page ID), but no ad creatives or hooks. The AdKit ad library timed out (60 s). Meta Ad Library pages return HTTP 403 to the fetch tool. **Section D therefore holds advertiser-level ad-volume data plus landing-page messaging, not verbatim ad hooks.** It ends with a query plan to run after the credit reset.

---

## Executive snapshot

| Theme | Key finding | Source |
|---|---|---|
| Closest big-brand rival | NEOM already sells a **"Perfect Night's Sleep Intensive Skin Treatment Candle"** (140g, £49 RRP) that melts into a massage oil, inside its sleep range | [LOOKFANTASTIC](https://www.lookfantastic.com/p/neom-perfect-night-s-sleep-intensive-skin-treatment-candle-140g/13507043/) |
| Closest "hands/cuticles" rival | butter LONDON **Manicure Candle** (launched 2022, Chelsea Blooms $34), a soybean + coconut oil candle poured onto hands and cuticles | [Bustle](https://www.bustle.com/beauty/butter-london-chelsea-blooms-manicure-candle) |
| Biggest "non-toxic candle" Meta advertiser | Fontana Candle Co: **427 active Meta ads** (Trendtrack lookup), "Truly clean candles for your low-tox home", MADE SAFE certified | [Fontana](https://fontanacandlecompany.com/) |
| Núan's ad status | nuan-organics.com is linked to FB page "Nuan" (ID 1173984032457067): **0 active ads, 0 monthly visits** in Trendtrack; it is already in this workspace's brandtracker | Trendtrack `lookup` (no public URL) |
| Market sizing | Global candles ≈ **$14.8B (2025), 7.3% CAGR** (Grand View); massage candles ≈ **$0.4B (2025), 6.8% CAGR** | [Grand View via MarketResearch.com](https://www.marketresearch.com/Grand-View-Research-v4060/Candle-44356426), [Marketintelo](https://marketintelo.com/report/massage-candle-market) |
| Seasonality | **~35% of candle sales happen in the Christmas/holiday season**; candle-warmer lamps peak in December | [NCA](https://candles.org/facts-figures/), [SellerSprite](https://www.sellersprite.com/en/blog/candle-warmer-lamps-report) |
| Warmer lamp pricing gap | Amazon warmer lamps sell for **$15.99–$29.99**; Núan's Lumera costs $55 | [NBC Select](https://www.nbcnews.com/select/shopping/best-candle-warmer-lamps-rcna244163) |

---

## A) Direct competitors (15)

Two clusters compete directly with Núan:
- **(A1) massage / lotion / skin-treatment candles**, which share Núan's "melts into a balm" mechanism.
- **(A2) natural "clean" and wellbeing/sleep candles**, which share Núan's "non-toxic, evening ritual" positioning.

### A1. Massage / lotion / manicure candles

#### 1. NEOM Wellbeing – Perfect Night's Sleep Intensive Skin Treatment Candle (UK; US via Ulta)
- **Product page:** [LOOKFANTASTIC listing](https://www.lookfantastic.com/p/neom-perfect-night-s-sleep-intensive-skin-treatment-candle-140g/13507043/)
- **Price / size:** £49.00 RRP, £39.20 on sale (20% off), 140g. The page lists no burn time. ([LOOKFANTASTIC](https://www.lookfantastic.com/p/neom-perfect-night-s-sleep-intensive-skin-treatment-candle-140g/13507043/))
- **Claims (paraphrased from listing):** a fragrant candle that melts into an oil you massage onto skin. The listing says the oil hydrates and brightens skin with baobab, jojoba and sweet almond. The English lavender, chamomile and patchouli scent is positioned for bedtime.
- **Ritual:** light it, bathe while the pool forms, blow it out after about 30 minutes, drizzle the oil and massage it in. This is almost the same ritual concept as Núan's "Glow → Melt → Seal".
- **Materials:** hydrogenated rapeseed oil, hydrogenated soybean oil, sweet almond oil, cocoa butter, baobab oil, jojoba oil, and Parfum (fragrance). ([LOOKFANTASTIC](https://www.lookfantastic.com/p/neom-perfect-night-s-sleep-intensive-skin-treatment-candle-140g/13507043/)) Note that "Parfum" is listed, so Núan's "every note named" is a point of difference.
- **Brand trust signals:**
  - B Corp.
  - Trustpilot "Excellent".
  - 374 reviews on the Perfect Night's Sleep 3-wick candle.
  - Free UK delivery over £60.
  - 15% off the first order (code 15FORYOU).
  - Loyalty points. ([NEOM UK](https://www.neomwellbeing.com/products/perfect-nights-sleep-scented-candle-3-wick))
- **Flagship and claims:** the Perfect Night's Sleep 3-wick candle costs **$59.00 / 14.8 oz at Ulta**. Its headline claim is "94% agree that the NEOM Sleep Programme helped them prepare for a Perfect Night's Sleep*". The footnote reads "*Independent blind study over 7 days on 100 volunteers using the NEOM Sleep Routine". It also claims "A complex blend of up to 13 essential oils". Rating: 4.5 stars from 24 reviews. ([Ulta](https://www.ulta.com/p/perfect-nights-sleep-scented-candle-pimprod2048904))
- **Sales approach:**
  - Range selling ("Sleep Programme" = candle + bath foam + pillow mist + body oil).
  - Heavy promotions: Black Friday edits at 44–45% off, and a Winter Wellbeing Candle Trio at £48 (was £63).
  - Gift builder. ([NEOM UK](https://www.neomwellbeing.com/products/perfect-nights-sleep-scented-candle-3-wick))
- **Momentum:**
  - FY2020 sales rose 84% to £28.9m, with 80% from digital. ([Cosmetics Business](https://cosmeticsbusiness.com/neom-organics-is-a-wellbeing-winner-as-sales-shoot-up-84-in-a-year--178907))
  - Revenue rose 35% over the 5 weeks to 2 Jan 2022. ([Retail Bulletin](https://www.theretailbulletin.com/health-and-beauty/neom-hails-very-strong-christmas-trading-17-01-2022/))
  - NEOM is expanding in the US via Ulta and has a new US GM. ([GCI](https://www.gcimagazine.com/brands-products/bath-body/news/22947760/neom-expands-ulta-partnership-hires-us-gm-to-tap-rising-wellness-trends-across-generations))
- **Threat level: HIGH.** It is the only large brand already combining *sleep ritual + candle → skin oil*. However, it is positioned for the body, not hands and cuticles, and at a higher price.

#### 2. butter LONDON – Manicure Candle (Champagne Fizz, Chelsea Blooms)
- **Product page:** [butterlondon.com](https://www.butterlondon.com/nail). The specific product URL returned 404 when fetched, so the product details below come from Bustle.
- **Price:** $34 (Chelsea Blooms). Size not stated. The line launched in 2022 with Champagne Fizz. ([Bustle](https://www.bustle.com/beauty/butter-london-chelsea-blooms-manicure-candle))
- **Claims:**
  - Made from soybean and coconut oils, 100% cotton wick.
  - Free from petrolatum, mineral oil, parabens and gluten. Cruelty-free and vegan.
  - The oils are said to hydrate cuticles and hands. The article says the oil won't burn or feel uncomfortably hot if used within 10 minutes of lighting.
  - Repurpose the jar as a planter. ([Bustle](https://www.bustle.com/beauty/butter-london-chelsea-blooms-manicure-candle))
- **Positioning:** a nail-care brand extension for an at-home spa manicure. Not sleep-focused.
- **Ads:** butter LONDON runs **22 active Meta ads** (FB page 198992439003) and has about 27.8k monthly site visits (Trendtrack lookup). Meta Ad Library page: [view_all_page_id=198992439003](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=198992439003) (URL built from the page ID; I could not open it).
- **Threat level: HIGH on the "hands/cuticles" angle,** with near-identical pricing ($34 vs Núan $32).

#### 3. Bee Inspired Goods – Massage Candles (Peace of Mind, Rose Garden, Autumn Harvest)
- **Product page:** [beeinspiredgoods.com/collections/massage-candles](https://beeinspiredgoods.com/collections/massage-candles)
- **Price / size:** **$32.00 each, 5.6 oz.** This is the same price as Núan for about 20% less wax. The 1–2 reviews shown suggest low volume.
- **Taglines (verbatim):** "Light It. Blow It Out. Pour the Warm Oil On." and "The Candle You're Supposed to Spill". ([Bee Inspired](https://beeinspiredgoods.com/collections/massage-candles))
- **Materials:** soy wax, shea butter, coconut oil, olive oil, cocoa butter and beeswax. Scented with essential oils only, "Skin-safe soy wax".
- **Usage:** burn about 12 minutes, never more than 15. Patch-test on the inner wrist and use within 6 months.
- **Trust signals:** woman-owned, made in Owings Mills, Maryland, with a portion of profits going to at-risk youth.
- **Shipping:** $10 flat or free over $85, plus a free gift over $75. No guarantee stated.
- **Ads:** 12 active Meta ads (page 282701878504870, Trendtrack lookup).
- **Takeaway:** a small US maker. Its copy is playful and instruction-led ("supposed to spill"), and that is a strong hook pattern.

#### 4. Beeline Skin Care – Bee Illuminated Lotion Candle
- **Product page:** [Old Farmer's Almanac Store](https://store.almanac.com/collections/for-you/products/bee-illuminated-lotion-candle)
- **Price / size:** $44.95, 5 oz stoneware jar. Backordered when checked. No burn time listed.
- **Claims (verbatim):** "Provides intense hydration with a high concentration of moisturizers." / "Helps prevent and repair cracking and splitting around fingernails." / "Long-lasting formula—just a little goes a long way!"
- **Materials:** beeswax, jojoba oil, coconut oil, shea butter, cocoa butter and essential oils. Described as hypoallergenic and free of parabens, GMOs, synthetic fragrance and dyes.
- **Takeaway:** the closest *claim* match to Núan's cuticle benefit ("cracking and splitting around fingernails"). It is sold through a heritage retailer with older buyers.

#### 5. Lumae (Mystic Nomad Aromatherapy) – Manicure Massage Candle (UK)
- **Product page:** [Country Living Shop](https://countrylivingshop.co.uk/products/lumae-manicure-massage-candle)
- **Price:** £39.00. Size and burn time are not stated, and stock showed "Less than 5 available".
- **Claims (verbatim):** "Jojoba oil mimics the skin's natural sebum for long-lasting moisture." / "Pink pepper gently warms the skin, perfect for those with cold hands." / "Myrrh, known as the gold standard in nail care, strengthens and protects." / "Geranium oil deeply nourishes cuticles, leaving hands silky-smooth."
- **Materials:** soy wax, shea, jojoba, caprylic/capric triglyceride, and pink pepper, geranium and myrrh essential oils.
- **Policy:** 14-day returns, unused items only.
- **Takeaway:** shows the UK has a niche "manicure candle" sub-category with ingredient-benefit copy for each oil. Núan names notes but could add *benefit-per-ingredient* copy like this.

#### 6. OSKIA – Rose de Mai Skin Smoothing Massage Candle (UK)
- **Product page:** [oskiaskincare.com](https://www.oskiaskincare.com/products/rose-de-mai-massage-candle)
- **Price / size:** £58.00 for 200g (official). Next shows £49. ([search summary of OSKIA/Next listings](https://www.lookfantastic.com/p/oskia-skin-smoothing-massage-candle/10539056/))
- **Claims:** a "natural massage & body candle" that leaves skin "super soft, nourished & smelling of spring roses". It contains coconut oil, beeswax and soya oil.
- **Takeaway:** a luxury skincare-brand massage candle. It confirms that about £50–60 is the ceiling price for 200g.

#### 7. Kama Sutra – Ignite Massage Candle (US mass / adult channel)
- **Product page (retailer):** [Sex with Emily shop](https://shop.sexwithemily.com/products/104kama-sutra-ignite-massage-candle). I found no official brand product page.
- **Price / size:** 6 oz. Prices vary by retailer: $26.00 (Sex with Emily), $25.99 MSRP ([Faire](https://www.faire.com/product/p_2n5b6s622t)), $16.25–$21.92 ([Walmart](https://www.walmart.com/ip/seort/130099948)).
- **Claims:** a soy and coconut oil-based candle that "melts into a warm, skin-safe massage oil". Retailers describe it as melting at a temperature safe for skin. ([Kate Minimalist listing](https://kateminimalist.com/products/kama-sutra-ignite-massage-candle-coconut-oil-and-soy-based-dose-of-rose-scented-6-oz-candle-melts-into-a-warm-massage-oil-couples-massage-pour-spout-massage-candle))
- **Takeaway:** in the US the "massage candle" search term is dominated by *couples/sensual* products. **Núan should avoid "massage candle" as a primary keyword** in ads and SEO, because of adult-category ad-policy risk and audience mismatch. "Lotion candle" or "hand balm candle" is safer.

#### 8. MUTHA – Aphrodisiac Massage Candle (luxury US)
- **Price:** $65. Described with "skin-softening coconut and soybean oils". This comes from a search snippet of [mutha.com/collections/candles](https://checkout.mutha.com/collections/candles); the product page returned 404, so I could not verify it live.
- **Ads:** **197 active Meta ads** (page 702035196865652, Trendtrack lookup). This is a heavy spender, but across its whole skincare line, not specifically the candle.
- **Takeaway:** the luxury ceiling for US massage candles.

#### 9. Modern Aromatherapy – Massage Candle with Essential Oils (US Shopify)
- **Product page:** [modernaromatherapy.com](https://modernaromatherapy.com/products/massage-candle-with-essential-oils)
- **Price / size:** $10.42 for 1 oz (a 2 oz size is also offered).
- **Claims (verbatim):** "Soy, Beeswax, Shea & Cocoa Butter · Pour-Spout Massage Oil · 6 Essential Oil Scents", "Handmade in Small Batches", "Built-in pour spout".
- **Trust signals:**
  - Claims 4.9/5 from 37,255 reviews store-wide, but only 8 product reviews (4.88).
  - "Trusted for Over 10 Years".
  - 14-day returns, free shipping over $100, and an FDA-style disclaimer.
- **Takeaway:** a typical Shopify pattern of large store-wide review counts next to tiny product-level counts. This is relevant to Núan's own "6,800+ reviews" claim (see Section F).

### A2. Natural / "clean" / wellbeing candles (no skin use)

#### 10. Fontana Candle Co. – beeswax + coconut oil, MADE SAFE (US)
- **Pages:** [Homepage](https://fontanacandlecompany.com/) and [About](https://fontanacandlecompany.com/pages/aboutus)
- **Price / size:** jar candles $25.99, collabs $26.99, advent calendar $124.99. The 9 oz jar holds 7.49 oz net wax. ([Shifting Gaia](https://shiftinggaia.com/products/lemongrass-eucalyptus-jar-candle))
- **Headline (verbatim):** "Truly clean candles for your low-tox home."
- **Other claims (verbatim):**
  - "The world is full of toxins, but we don't think they should be in your home."
  - "we were the first candle to ever be independently certified as non-toxic by MADE SAFE®"
  - Products are "formulated for the most sensitive noses!"
  - It claims "zero synthetic chemicals". ([Fontana](https://fontanacandlecompany.com/))
- **Materials:** beeswax, coconut oil and essential oils. No synthetic fragrance, and 100% ingredient transparency.
- **Story:** the founders reported headaches after burning a gifted paraffin candle in 2017, ran about 150 test batches, and launched in 2018. ([About](https://fontanacandlecompany.com/pages/aboutus))
- **Trust signals:** MADE SAFE seal, "from 3909 reviews", and a scent quiz.
- **Offers:** free US shipping at $70+, Build-Your-Bundle, and 15–20% off the first order.
- **Guarantee:** "Love at First Light Guaranteed", with a 30-day window and these terms:
  - Unused candles get a full refund.
  - Candles burned less than 25% carry a 20% restocking fee.
  - Candles burned more than 25% cannot be returned.
  - Store credit pays 25% extra. ([Refund policy](https://fontanacandlecompany.com/policies/refund-policy))
- **Ads:** **427 active Meta ads** (page 1572316736191286, Trendtrack lookup), the most of any "clean candle" brand checked. Ad Library: [view_all_page_id=1572316736191286](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=1572316736191286). Fontana also ran a billboard saying in effect that most candles are bad for you. ([CPBJ](https://www.cpbj.com/newsletter-category/morning-roundup/page/30))
- **Threat level: HIGH for the "non-toxic" angle.** Fontana owns the "beeswax + coconut + essential oils + certification" story with a large review base.

#### 11. Pure Plant Home – coconut wax aromatherapy candles (US)
- **Page:** [pureplanthome.com](https://www.pureplanthome.com/)
- **Headline (verbatim):** "Clean Aromatherapy Candles Made With Real Essential Oils"
- **Price / size:** 6 oz glass from $24.00, 7 oz amber apothecary jar from $25.00, 1.5 oz tins $5.50. The 3.1 oz jar is $12.49 at [Thrive Market](https://thrivemarket.com/p/pure-plant-home-amber-apotherapy-jar-wildcrafted-lavender-coconut-wax).
- **Claims (verbatim):** "Non-Toxic.", "No paraffin or toxins", "Petrochemical Free", "Vegan & Non-GMO", "No synthetic fragrance", "100% pure & therapeutic".
- **Trust signals:** Good Housekeeping and mindbodygreen logos, and 15% off for email signup. No guarantee listed. I found no massage or lotion candle.
- **Ads:** no Trendtrack shop or advertiser match for pureplanthome.com.
- **Takeaway:** Núan's **amber jar** looks similar, so differentiation must come from the balm function.

#### 12. Otherland – coconut + soy (US DTC)
- **Product page:** [otherland.com/products/canopy](https://otherland.com/products/canopy)
- **Price / size:** $20.00 for 8 oz with up to 55 h burn (price as displayed at fetch; possibly promotional).
- **Claims (verbatim):** "Perfumer crafted. Art inspired.™". Features listed: Toxin Free, Vegan, Cruelty Free, American poured. Formulated without parabens, sulfates, phthalates or dyes.
- **Offers:** free shipping over $75, Build Your Bundle, and refer-a-friend "Give 10%, Get 10%".
- **Returns:** 30 days. ([Otherland FAQ summary](https://www.otherland.com/pages/help-faq))
- **Ads:** 35 active Meta ads, about 22.8k monthly visits (Trendtrack lookup).
- **Takeaway:** at $20 for 55 h, Otherland **undercuts Núan's per-hour cost** ($0.36/h vs $0.53/h single). Núan's price must be justified by the dual function.

#### 13. Boy Smells – coconut + beeswax blend (US)
- **Specs:** 8.5 oz, about 50 h burn, zero paraffin, phthalate-free ([Kith listing summary](https://kith.com/products/bs-p219rsl)). Price about $36–38 ([Bustle](https://www.bustle.com/product/85305440), [reach.dog](https://reach.dog/shop/jenkins-co-tulsa/products/boysmellscandle)). The direct product URL returned 404.
- **Ads:** **104 active Meta ads**, about 153.5k monthly visits (page 368491270264152, Trendtrack lookup).
- **Takeaway:** a design- and identity-led brand. It shows that "coconut + beeswax, no paraffin" is now table stakes in premium candles.

#### 14. Brooklyn Candle Studio (US)
- **Page:** [brooklyncandlestudio.com/collections/all](https://www.brooklyncandlestudio.com/collections/all)
- **Price:** jar $34, 2-wick $45, XL 3-wick $95, travel $22.
- **Trust signals:** "3,200+ 5-STAR reviews" banner and "FREE SHIPPING ON U.S. ORDERS $100+". Bundles save 13–40%, and there is a Candle of the Month subscription.
- **Ads:** 24 active Meta ads, about 39.9k monthly visits (Trendtrack lookup).

#### 15. Keap – coconut wax blend, plastic-free (US premium)
- **Product page:** [keapcandles.com/products/timur-moon](https://www.keapcandles.com/products/timur-moon)
- **Price / size:** $59.50 single, $109 for 2, $208 for 4. 7.4 oz, about 45 h.
- **Wax:** mostly high-melt coconut oil plus soy and organic beeswax. The candle is "100% plant-based and 100% biodegradable". Packaging is plastic-free and gift-boxed with a coaster and matches. Subscribers save $10.
- **Ads:** 0 active Meta ads on keapcandles.com (Trendtrack lookup).

### Also checked (benchmarks, not core rivals)

| Brand / product | Price / size / burn | Key claim | Source |
|---|---|---|---|
| This Works Deep Sleep Heavenly Candle | $40 (Dermstore), 220g, ~40 h | Sleep-range candle (lavender, camomile, vetivert) | [Dermstore](https://www.dermstore.com/p/this-works-deep-sleep-heavenly-candle-220g/10524482/?rctxt=fbt) |
| Aromatherapy Associates Deep Relax Candle | £52 RRP (£34.84 sale), 200g, 40 h | Relax/sleep aromatherapy | [LOOKFANTASTIC](https://lookfantastic.com/p/aromatherapy-associates-deep-relax-candle-200g/12911574), [John Lewis](https://www.johnlewis.com/aromatherapy-associates-deep-relax-candle-200g/p5574250) |
| Diptyque Baies | $65–78 / £58–63, 190g, 50–60 h | Luxury benchmark | [Beauty Habit](https://beautyhabit.com/products/diptyque-baies-berries-and-bulgarian-roses-candle), [Liberty](https://www.libertylondon.com/uk/baies-scented-candle-190g-000874375.html) |
| Lush massage bars | €12–15 / 65–75g (EU); CA$14 / 65g | Solid bars that melt at body temperature; no candle format | [Lush GR](https://lush.gr/Therapy-Μπάρα-Μασάζ-), [Shop Midtown](https://shopmidtown.ca/whatsinstore/product/coconut-drench-lushfreshhandmadecosmetics-7bde2d) |
| Bath & Body Works | No massage or lotion candle found | Regular 3-wick candles only | [search result summary – NBC](https://www.nbcnews.com/select/shopping/bath-and-body-works-amazon-rcna260519) |
| Votary | Lavender & Chamomile soy candle £45 (sold out). No massage candle found | — | [Cult Beauty](https://www.cultbeauty.co.uk/p/votary-lavender-and-chamomile-soy-wax-candle/13313996) |
| Homesick | Not price-checked; 30-day returns in original condition | — | [Homesick returns](https://checkout.homesick.com/pages/returns) |
| Not verified | Malin+Goetz, Le Labo, Jo Malone, ESPA, Elemis, Sacheu, Lumira, Ritual Sanctuary, Nécessaire, Moroccanoil, Lavanila, Bloomscape. Not researched in depth; none surfaced as making a skin-use candle in my searches | — | — |

### A3. Price-per-hour comparison (where burn time was published)

| Product | Price | Burn | $/hour |
|---|---|---|---|
| **Núan Ritual Candle (single)** | $32 | ~60 h | **$0.53** |
| **Núan, 3 for $64** | $21.33 each | ~60 h | **$0.36** |
| Otherland Canopy 8 oz | $20 | 55 h | $0.36 ([Otherland](https://otherland.com/products/canopy)) |
| Boy Smells 8.5 oz | ~$36–38 | ~50 h | ~$0.74 ([Kith](https://kith.com/products/bs-p219rsl)) |
| This Works Deep Sleep 220g | $40 | ~40 h | $1.00 ([Dermstore](https://www.dermstore.com/p/this-works-deep-sleep-heavenly-candle-220g/10524482/?rctxt=fbt)) |
| Keap 7.4 oz | $59.50 | ~45 h | $1.32 ([Keap](https://www.keapcandles.com/products/timur-moon)) |
| Diptyque 190g | $78 | 50–60 h | $1.30–1.56 ([Beauty Habit](https://beautyhabit.com/products/diptyque-baies-berries-and-bulgarian-roses-candle)) |

**Insight:** the brief's "~53¢ per evening" claim is defensible. Massage candles almost never publish burn time; most instruct 10–30 minute burns. Núan's 60 h burn plus the balm function is a value story no direct massage-candle rival tells.

### A4. Positioning map: where Núan sits

| | Body / sensual | Hands / cuticles | Sleep / evening ritual | Non-toxic emphasis | Warmer lamp |
|---|---|---|---|---|---|
| NEOM Skin Treatment Candle | ✔ | – | ✔✔ | ✔ (natural wax) | – |
| butter LONDON Manicure Candle | – | ✔✔ | – | ✔ (free-from) | – |
| Bee Inspired / Beeline / Lumae | ✔ | ✔ (Beeline, Lumae) | – | ✔ | – |
| Kama Sutra / MUTHA | ✔✔ | – | – | – | – |
| Fontana / Pure Plant Home | – | – | – | ✔✔ | Fontana sells a wax warmer ($28.99) |
| **Núan** | – | **✔✔** | **✔✔** | **✔** | **✔ (Lumera)** |

**White space:** no competitor I verified combines *hands/cuticles + sleep ritual + flame-free warmer*.

---

## B) Candle-warmer lamp competitors

| Product | Price | Key features / claims | Source |
|---|---|---|---|
| Godonlif Candle Warmer Lamp | $19.99 | "Best overall" (NBC). Adjustable height, timer, spare bulb, glass shade | [NBC Select, Oct 1 2026](https://www.nbcnews.com/select/shopping/best-candle-warmer-lamps-rcna244163) |
| Funistree Flower lamp | $23.99 (was $26.99) | Petal shade, timer, two halogen bulbs, dimmer. "offers good throw in a large space" | same |
| Marycele lamp | $19.88 (was $39.99) | **Wooden base**, timer, adjustable brightness | same; also [Walmart](https://www.walmart.com/ip/Candle-Warmer-Lamp-Housewarming-Gifts-for-New-House-Women-Couple-Candle-Lamp-Warmer-Unique-Gift-Ideas-for-New-Home-Christmas-Decor/10641309501) |
| Maoyue lamp | $21.83 (was $49.99) | Melts top-down, 2/4/8 h auto shut-off, dimmable | NBC |
| Soilsiu lamp | $15.99 | 2/4/8 h timer, 4 brightness levels | NBC |
| Cozyberry Querencia | $29.99 | Modern design, cord dimmer | NBC |
| Candle Warmers Etc. plate / 2-in-1 | $21.98 / $21.89 | Hot-plate warmers (no light). The company popularised modern warmers in 2001 | NBC; [Wikipedia](https://en.wikipedia.org/wiki/Candle_warmer) |
| Candle Warmers Etc. punched-tin lantern | $38.99 | Lantern style | [GMA](https://ws.goodmorningamerica.com/shop/story/best-electric-candle-warmers-110185372) |
| Luzdiosa lamp | n/a | The TikTok origin product. Taste of Home "Best Overall"; newer version adds 2/4/6 h timer | [AJC](https://www.ajc.com/life/private-quarters/tiktoks-candlewarmer-lamps-are-trending-inside-homes/6BB5MCUXDVDFFIXHMQXN3PS3MM), [Taste of Home (TMBI mirror)](https://f-cce-6950.toh.r.tmbi.com/?p=2168036) |
| Briever (walnut wood base) | budget | 4 temperature levels, 2/4/8 h timer | [Talk of the House](https://www.talkofthehouse.com/?p=61519) |
| Generic dimmable + timer lamps | $17.99–$69 | Wide spread on Walmart, Target and Fruugo | [Target $19.99](https://www.target.com/p/candle-warmer-lamp-with-timer-adjustable-heigh-4-levels-dimmable/-/A-1005225708), [Fruugo $52.95–69](https://www.fruugo.us/candle-warmer-lamp-with-timer-and-stepless-dimming-for-large-scented-candles-auto-shutoff/p-446908892) |
| Mainstays (Walmart) | $4.47–$8.94 on deal | Mass/value | [Slickdeals](https://slickdeals.net/f/19062049-mainstays-candle-warmer-lamp-green-4-47-free-s-h-w-walmart-or-on-35) |
| "Hyoola" | **Not found** | No listing under that brand name surfaced | [search attempt shown via Fruugo/Walmart results](https://www.walmart.com/ip/HYEASTR-Dimmable-Candle-Warmer-Lamp-Timer-Wax-Melting-Lamp-Wood-Base-2-Bulbs-Wax-Warmer-Bedside-Lamp-Scented-Wax-Large-Small-Jar-Candle-White/5129348927) (closest: "HYEASTR") |
| "Bolt" | **Not found / not verified** | — | — |

**Category claims used across warmers:**
- **Safety:** FDNY's Jack Oehm says a warmer is less of a risk than a lit candle "that can be knocked down". Harlem Candle Co's founder says: "A candle warmer is a great option for anyone nervous about accidentally causing a fire in their space." ([NBC Select](https://www.nbcnews.com/select/shopping/best-candle-warmer-lamps-rcna244163))
- **Longevity:** House Digest says candles can last up to three times longer because "Since there's no flame directly on the wax, it melts slower." ([House Digest](https://housedigest.com/1213042/candle-warming-lamps-are-trending-but-are-they-better-than-burning-candles)) This supports Núan's "up to 3x longer" Lumera claim as a category-standard claim, not a proprietary one.
- **Cons:** House Digest flags messier cleanup and a higher electricity bill. A buyer quoted by AJC reported the light broke within six months ([AJC](https://www.ajc.com/life/private-quarters/tiktoks-candlewarmer-lamps-are-trending-inside-homes/6BB5MCUXDVDFFIXHMQXN3PS3MM)). Núan's spare bulb answers this objection directly and should be marketed.

**Lumera pricing implication:** at $55, Lumera costs **2–3x the Amazon category leaders ($16–30)**. Ways to justify the price:
- Real wood.
- Spare bulb.
- Designed for the balm ritual (top-down melt creates the hand-balm pool without a flame, so "No flame. No waiting.").
- Bundling: the $119 ritual set, rather than selling the lamp standalone against Amazon.

**Ads:** Candle Warmers Etc. runs 23 active Meta ads (page 80859832617). Luzdiosa has no Meta advertiser match and about 1.4k site visits (Trendtrack lookup). Most warmer demand is captured on Amazon and TikTok, not DTC Meta.

---

## C) Indirect competitor categories (by desire)

**Desire 1: evening wind-down, sleep, self-care ritual. Desire 2: soft hands and cuticles.**

| # | Category | Example and price | Language used (verbatim where quoted) | Pros vs Núan | Cons vs Núan | Growing or shrinking? |
|---|---|---|---|---|---|---|
| 1 | **Hand cream** (D2) | O'Keeffe's Working Hands 3.4 oz: $10.99 (Staples), $11.88 (Walmart). L'Occitane Shea Hand Cream 150ml: £20–27 | O'Keeffe's: "guaranteed relief or money back" ([Home Hardware](https://www.homehardware.ca/en/p/4670090)); "ideal for very dry, cracked hands" ([Staples](https://www.staples.com/product_1260243)). L'Occitane: "20% Shea butter" ([John Lewis](https://www.johnlewis.com/loccitane-shea-karite-hand-cream/p114443738)) | Cheap, fast, proven, portable, daytime-friendly | No ritual, no ambience, often "greasy" complaints ([LOOKFANTASTIC reviews](https://lookfantastic.com/p/l-occitane-shea-butter-hand-cream-150ml/13277476)) | **Growing**: global hand cream ≈ $514M (2025), 4.6% CAGR ([IMARC](https://www.imarcgroup.com/global-hand-cream-market)); ≈ $844M, 6.5% CAGR ([Market.us](https://market.us/report/hand-cream-market/)) |
| 2 | **Cuticle oil** (D2) | CND SolarOil 0.5 oz ≈ $7.55; 4 oz ≈ $32.70 | Penetrates "deeply into the nail plate to reduce brittleness"; jojoba, vitamin E, rice bran, sweet almond ([Ocean Nail Supply](https://www.oceannailsupply.com/products/cnd-solar-oil-cuticle-oil)) | Precise, salon-trusted, cheap per use | No scent ritual, easy to forget | Not quantified; no reliable growth data found |
| 3 | **Overnight hand masks and gloves** (D2) | Cotton gloves 5-pack $4.94; Aquaphor Repairing Hand Mask $5.97–8.59; premium overnight mask $32 | "Overnight", "repairing" | Very cheap, sits in the "night-time hand care" slot | Clinical, uncomfortable, no sensory pleasure | Not quantified ([Slickdeals](https://slickdeals.net/f/20056422-5-pack-cotton-moisturizing-overnight-gloves-4-94-w-s-s-free-shipping-w-prime-or-on-35), [Pasteur Pharmacy](https://pasteurpharmacy.com/products/aquaphor-advanced-therapy-repairing-hand-mask-0-7-fl-oz-1)) |
| 4 | **Paraffin wax hand baths** (D2 + ritual) **← most relevant** | HoMedics ParaSpa Plus ≈ $59.99; TheraSpa Deluxe $75.99–109.99; Therabath TB6 $242.99; generic $19.55–66.99 | "Heat therapy", "relieve arthritis/muscle stiffness" ([Walmart Therabath](https://www.walmart.com/ip/Therabath-Professional-Thermotherapy-Adjustable-TB9-Paraffin-Wax-Bath-Quick-Melt-Helps-Relieve-Arthritis-Muscle-Stiffness-Heat-Therapy-Hands-Feet-Bod/551408595)) | Proven warm-wax hand softening, spa feel | **Paraffin** (petroleum), bulky, messy, 20+ min, not ambient, not a candle | Refill segment concentrated: top 3 hold 65.9% click share on Amazon ([AsInsight](https://www.asinsight.com/report/US/therabath-paraffin-wax-refill)); no market CAGR found. **Angle:** "the warm-wax hand treatment without the paraffin" |
| 5 | **Sleep and pillow sprays** (D1) | This Works Deep Sleep Pillow Spray 2.5 oz $29–33 | "97% slept better, 89% fell asleep faster" (100-subject panel vs no product) ([Dermstore](https://www.dermstore.com/p/this-works-deep-sleep-pillow-spray-75ml/10524480/?rctxt=fbt)) | 5-second habit, strong claims | No hand benefit, scent-only | This Works runs **317 active Meta ads, 4.29M 30-day reach** (Trendtrack lookup), so the category is heavily advertised |
| 6 | **Magnesium and sleep supplements** (D1) | Magnesium glycinate (Luma claims >10k units/month on Amazon) | "Supports restful sleep" | Ingestible "fix", cheap | Not a ritual, no sensory element | **Growing**: magnesium supplements ≈ $7.9B (2025), 8.2% CAGR ([GMI](https://www.gminsights.com/industry-analysis/magnesium-supplements-market)); one retailer's magnesium segment grew 16.55% in 2025 ([Modern Retail](https://www.modernretail.co/?p=152663)) |
| 7 | **Wax melts and warmers** (D1) | Fontana Gingerbread Wax Warmer $28.99 ([Fontana](https://fontanacandlecompany.com/)); Scentsy-type melts | "Flameless fragrance" | Flame-free, cheap refills | No skin benefit | **Growing**: ≈ $1.52B (2025) → $2.12B (2032), 4.84% CAGR ([Fortune BI via 680thefan](https://lifestyle.680thefan.com/story/52774056/wax-melts-market-size-to-reach-212-billion-by-2032-with-a-cagr-of-484-from-2025-2032)); North America 36% share ([Market.us](https://www.news.market.us/wax-melts-market-news)) |
| 8 | **Diffusers (smart and essential oil)** (D1) | Pura 4 $37.49–55; refills $18–21, ~120 h each | App scheduling, "smart fragrance" | Scheduled scent, no flame | Subscription cost, no ritual or skin use | **Growing**: smart aroma diffusers ≈ $558.6M (2025), 9.22% CAGR ([Fortune BI](https://www.fortunebusinessinsights.com/zh/smart-aroma-diffusers-market-115923)); home diffusers ≈ $3.38B, 6.32% CAGR ([Ken Research](https://www.kenresearch.com/industry-reports/global-home-fragrance-diffuser-market)) |
| 9 | **Bath rituals** (D1) | Dr Teal's Sleep Soak with Melatonin 3 lb ≈ $5.79–6.99 | "Sleep", melatonin, lavender and chamomile ([Kroger](https://www.kroger.com/p/dr-teal-s-sleep-epsom-salt-magnesium-soak-with-melatonin-lavender-chamomile-essential-oils/0081106801972)) | Very cheap, mass reach | Needs a bathtub and 20+ min | Not quantified |
| 10 | **Sleep body lotion** (D1 + D2 hybrid) | Lush Sleepy Body Lotion $15 / 3.1 oz (Ulta) | Lavender + tonka; anecdotal "helped me sleep" ([Project Vanity](https://www.projectvanity.com/projectvanity/splurge-vs-save-this-love-beauty-amp-planet-lotion-smells-almost-exactly-like-lush-sleepy)) | Proof that **"skin product for sleep"** sells: launched 2016 as Christmas limited, made permanent on demand ([Today](https://www.today.com/today/amp/tdna115932)) | No candle or ambience | Strong demand signal (sell-outs) |
| 11 | **Herbal sleep tea** (D1) | Yogi Bedtime 16 ct $4.46–5.05; Celestial Sleepytime 20 ct $3.48–3.69 | "Supports a good night's sleep" ([Walmart](https://www.walmart.com/ip/23658488), [Target](https://www.target.com/s/sleeping+tea)) | Ritual, near-zero cost | No hand benefit | No growth data found |

**Indirect takeaways for Núan:**
1. The **paraffin hand bath** is Núan's most persuasive comparison: "the spa's warm-wax hand treatment, minus the paraffin, the machine and the mess, and it scents your room."
2. **Sleep claims** in the category lean on small self-reported panels (This Works 100 subjects; NEOM 100 volunteers on the full routine). Núan has no study, so it should stick to ritual and "prepare for sleep" language, as NEOM does, not "fall asleep faster".
3. Price anchors: daily-use hand cream about $11. A cuticle oil plus overnight mask plus a sleep candle together cost $50+. Núan at $32 replaces "two products in one jar".

---

## D) Ad research

### D1. Tool status
- **Trendtrack:** `check_credits` → 0 credits remaining (10,000/10,000 used; period ends 2026-11-10). `search_ads("massage candle")` and `search_advertisers` → "❌ Not enough credits". Only the free `lookup` endpoint worked, and intermittently.
- **AdKit ad library:** timed out after 60 s.
- **Meta Ad Library web:** HTTP 403 to the fetch tool.
- **Web search for published ad examples:** I found no article quoting live ad hooks for these brands. The one exception is outdoor: Fontana's Route 30 billboard saying most candles are bad for you ([CPBJ](https://www.cpbj.com/newsletter-category/morning-roundup/page/30)).
- **Therefore:** I cannot report verbatim Meta or TikTok ad hooks, running durations, formats or CTAs. **None are invented here.**

### D2. Advertiser-level signals (Trendtrack `lookup`, 2026-11-01)

| Advertiser | FB page ID | Active Meta ads | 30-day reach | Site visits/mo | Ad Library link (built from page ID) |
|---|---|---|---|---|---|
| **Nuan (nuan-organics.com)** | 1173984032457067 | **0** | n/a | **0** | [link](https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=1173984032457067) |
| diptyque | 103195896578 | 602 | 22.19M | n/a | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=103195896578) |
| Fontana Candle Company | 1572316736191286 | 427 | 0 (not reported) | n/a | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=1572316736191286) |
| This Works | 53281688329 | 317 | 4.29M | 96.6k | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=53281688329) |
| NEOM Wellbeing | 185057398135 | 227 | **16.93M** | n/a | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=185057398135) |
| MUTHA | 702035196865652 | 197 | 0 (not reported) | n/a | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=702035196865652) |
| Boy Smells | 368491270264152 | 104 | 0 (not reported) | 153.5k | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=368491270264152) |
| Aromatherapy Associates | 106293359404516 | 48 | 2.39M | 43.2k | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=106293359404516) |
| Otherland | 1805833923030215 | 35 | 0 (not reported) | 22.8k | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=1805833923030215) |
| Brooklyn Candle Studio | 174468439410399 | 24 | 0 (not reported) | 39.9k | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=174468439410399) |
| Candle Warmers Etc. | 80859832617 | 23 | 0 (not reported) | n/a | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=80859832617) |
| butter LONDON | 198992439003 | 22 | 0 (not reported) | 27.8k | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=198992439003) |
| Bee Inspired (goods) | 282701878504870 | 12 | 0 (not reported) | n/a | [link](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&view_all_page_id=282701878504870) |
| Keap Candles | (unrelated page linked) | 0 | — | 11.8k | — |
| Luzdiosa (warmer) | no advertiser | 0 | — | 1.4k | — |
| Pure Plant Home / Kama Sutra / Lush (US) | no reliable match | — | — | — | — |

Notes on the table:
- "Reach 0" means Trendtrack did not report reach (it lacks EU transparency data for US-only advertisers). It does not mean no reach.
- The Ad Library links use Meta's standard `view_all_page_id` URL pattern with IDs from Trendtrack. I could not open them to confirm content.

**Reading the signals:**
- **NEOM (16.9M 30-day reach, 227 ads)** is the most active advertiser in "wellbeing candle / sleep". **Fontana (427 ads)** is the most active in "non-toxic candle".
- High ad counts signal heavy creative testing. These two pages are the priority swipe files once credits reset.
- **Núan has never been seen running Meta ads, and its traffic is zero.** Trendtrack shows it already in the brandtracker, so Núan starts from a cold account and pixel.

### D3. Landing-page messaging that ads point to (verified; site copy, not ad copy)

| Brand | Hook-style line (verbatim, from site) | Angle |
|---|---|---|
| Fontana | "Truly clean candles for your low-tox home." / "The world is full of toxins, but we don't think they should be in your home." | Fear of toxins, then a clean swap |
| Fontana | "formulated for the most sensitive noses!" | Headache and sensitivity objection |
| Pure Plant Home | "Clean Aromatherapy Candles Made With Real Essential Oils" / "No paraffin or toxins" | Clean aromatherapy |
| Bee Inspired | "Light It. Blow It Out. Pour the Warm Oil On." / "The Candle You're Supposed to Spill" | Pattern-interrupt, product demo |
| Beeline | "Helps prevent and repair cracking and splitting around fingernails." | Problem/solution for hands |
| NEOM (Ulta) | "94% agree that the NEOM Sleep Programme helped them prepare for a Perfect Night's Sleep*" | Stat-led sleep proof |
| This Works (retailers) | "97% slept better, 89% fell asleep faster" | Stat-led sleep proof |
| Otherland | "Perfumer crafted. Art inspired.™" | Design and aesthetic |

**Creative implications (inferred, not ad-verified):**
1. **Demo hook** ("candle you're supposed to spill"): pour or rub the pool onto knuckles in close-up macro. This is the most "thumb-stopping" visual unique to the category.
2. **Fear → swap hook** (Fontana style): "Your candle is paraffin. Your hand balm is petroleum. This is neither."
3. **Stat or ritual hook** (NEOM style): needs Núan's own survey data before using numbers.
4. **Warmer-lamp hook** (TikTok origin was a creator review of a Luzdiosa lamp; [SheKnows](https://www.sheknows.com/living/articles/2632229/tiktok-candle-warming-lamp/)): "no flame, falls asleep with you (timer)" for parents and pet owners.

### D4. TikTok and organic evidence
- \#candlewarmer had **57.4M+ views** on TikTok per [Ideal Home](https://www.idealhome.co.uk/all-rooms/all-rooms-decor/candle-warmer-lamp-cost-to-run) (search-snippet figure). Other outlets cite 85M–100M+ views (third-party, unverified; see [SheKnows](https://www.sheknows.com/living/articles/2632229/tiktok-candle-warming-lamp/)).
- The trend began with SunriseValleyFarm.co's Luzdiosa review, which got 30k+ likes ([AJC](https://www.ajc.com/life/private-quarters/tiktoks-candlewarmer-lamps-are-trending-inside-homes/6BB5MCUXDVDFFIXHMQXN3PS3MM)).
- I found **no TikTok Shop or viral evidence for "lotion/manicure candle"** content. This is an under-saturated content niche.

### D5. Query plan for after the credit reset (2026-11-10). About 10 calls, cheapest first.
1. `search_ads` query "massage candle", `sort_by=longestRunning`, `status=active`, `limit=20`.
2. `search_ads` query "lotion candle" OR "manicure candle", same settings.
3. `search_ads` query "candle warmer lamp", `sort_by=longestRunning`, `ad_countries include US`.
4. `search_ads` query "non-toxic candle", `sort_by=longestRunning`.
5. `search_ads` with `search_in=brand` and query "NEOM Wellbeing", `sort_by=longestRunning`, `limit=20`.
6. `search_ads` with `search_in=brand` and query "Fontana Candle Company", `sort_by=longestRunning`.
7. `search_ads` with `search_in=brand` and query "This Works", `sort_by=longestRunning`.
8. `search_tiktok_library` query "candle warmer", `type=ad`, `sort_by=days_running`, `limit=10`.
9. `search_tiktok_library` query "massage candle", `type=all`, `sort_by=views`, `limit=10`.
10. `search_shops` query "nuan-organics.com", `match_mode=exact`, to re-confirm ad status after launch.

Record for each: hook, headline, days running, format, CTA, offer, visual setting and media link.

---

## E) Market data

### E1. Candle market (global and US)

| Metric | Figure | Source |
|---|---|---|
| Global candle market 2025 | $14.77B; 7.3% CAGR 2026–2033 | [Grand View Research via MarketResearch.com](https://www.marketresearch.com/Grand-View-Research-v4060/Candle-44356426) |
| Global candle market 2025 (alt.) | $21.3B; 4.5% CAGR 2026–2035 | [GMI](https://www.gminsights.com/industry-analysis/candle-market) |
| Global candle market (alt.) | +$3.96B growth, 7% CAGR 2024–2029 | [Technavio](https://labs.technavio.com/report/candle-market-industry-analysis) |
| Lower-bound estimate | $8.55B (2025), 2.7% CAGR | [Expert Market Research](https://www.marketresearch.com/Expert-Market-Research-v4220/Candle-Size-Share-Growth-Forecast-42021477) |
| US retail candle sales | ~$3.14B/yr (Mintel 2013, cited by NCA; dated) | [NCA](https://candles.org/facts-figures/) |
| Wax used in US annually | >1 billion lbs | [NCA](https://candles.org/facts-figures/) |
| Fragrance importance | "by far the most important characteristic"; ~¾ rate it extremely or very important | [NCA](https://candles.org/facts-figures/) |
| Candles as gifts | Holidays 76%, housewarming 74%, hostess 66%, thank-you 61%, adult birthdays 58% | [NCA](https://candles.org/facts-figures/) |

Estimates diverge because the reports define the market differently (scope and currency). Treat ~5–7% CAGR as the consensus range.

### E2. Natural / soy / non-toxic segment
- Soy-based candles: projected $9.33B by 2031 at **13.9% CAGR** ([KBV Research](https://www.kbvresearch.com/press-release/soy-based-candles-market)).
- Arizton calls soy the **fastest-growing** wax segment at 5.37% CAGR and describes soy as a preferred alternative to paraffin ([Arizton](https://arizton.com/market-reports/candle-market)).
- Transparency Market Research describes beeswax and soy as leading materials because of their "eco-friendly, non-toxic" character, within a candle market worth $16.9B by 2031 at 6.5% CAGR ([PR Newswire](https://prnewswire.co.uk/news-releases/candle-market-size-to-be-worth-usd-16-9-billion-by-2031--with-a-cagr-of-6-5--exclusive-report-by-transparency-market-research-inc-302006089.html)).
- **Gap:** I found **no consumer survey quantifying paraffin avoidance**. The trend is asserted by report summaries and by brand positioning (Fontana, Pure Plant Home, Boy Smells "zero paraffin"), not measured.

### E3. Paraffin and toxin concern: the scientific picture is mixed (important for claim compliance)
- A 2009 South Carolina State University study found paraffin candles emitted toluene and benzene while soy did not. Occasional use was deemed unlikely to be harmful, but frequent burning in unventilated rooms might aggravate asthma ([WASHplus summary](https://blogs.washplus.org/iaqupdates/2009/08/some-types-of-candles-may-pollute-indoor-air/index.html)).
- A 2014 chamber study concluded that "under normal conditions of use scented candles do not pose known health risks" ([PubMed 24582651](https://pubmed.ncbi.nlm.nih.gov/24582651/)).
- EPFL notes lead-core wicks as a clear concern and higher benzo(a)pyrene from pure paraffin, but calls for more study ([EPFL HOBEL](https://www.epfl.ch/labs/hobel/are-candles-toxic-to-indoor-air-quality-2/)). A newer review reported little pollutant difference between beeswax, stearin and paraffin ([Jerusalem Post](https://www.jpost.com/science/science-around-the-world/article-832617)).
- **Implication:** "No paraffin, every note named" (transparency) is safer than "non-toxic" (a health claim). Fontana backs "non-toxic" with third-party MADE SAFE certification ([MADE SAFE](https://www.madesafe.org/find-products/made-safe-certified-products-from-fontana-candle-company/)). Without certification, Núan should not use "non-toxic" as a headline.

### E4. Massage candle segment
- $0.4B (2025) → $0.7B (2034), 6.8% CAGR ([Marketintelo](https://marketintelo.com/report/massage-candle-market)).
- $0.4B (2026) → $0.66B (2035), 5.72% CAGR ([Business Research Insights](https://www.businessresearchinsights.com/market-reports/massage-candle-market-123716)).
- $164.4M (2025) → $343M (2033), 9.6% CAGR ([Verified Market Research](https://www.verifiedmarketresearch.com/product/massage-candle-market/)).

### E5. Sleep economy
- McKinsey ranks sleep as consumers' **second-highest wellness priority** and the area with the most unmet needs ([McKinsey explainer](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-the-future-of-wellness)).
- Gen Z and millennials rank sleep and health as their top two priorities (2025 edition, 9,000+ consumers in CN, DE, UK, US) ([Spa Business](https://www.spabusiness.com/wellness-news/Corporate-wellness-sleep-and-indifference-to-clean-beauty-McKinsey-research-reveals-six-crucial-US-wellness-trends/350728)).
- An earlier US survey found 45% rated better sleep "very high priority" ([Health Club Management](https://www.healthclubmanagement.co.uk/health-club-management-news/Corporate-wellness-sleep-and-indifference-to-clean-beauty-McKinsey-research-reveals-six-crucial-US-wellness-trends/350728)).
- Sizing (definitions vary enormously):
  - Broad "sleep economy" ≈ $500–616B ([HKTDC](https://newsbites.hktdc.com/trend/sleep-economy/)).
  - Sleep market $65.8B (2025) ([Straits Research](https://straitsresearch.com/report/sleep-market)).
  - Sleep aids $49–76B ([Marketintelo](https://marketintelo.com/report/sleep-aids-market)).

### E6. Hand care
- Hand cream: $514M (2025), 4.62% CAGR ([IMARC](https://www.imarcgroup.com/global-hand-cream-market)); $843.7M, 6.5% CAGR ([Market.us](https://market.us/report/hand-cream-market/)); $0.85B, 6.92% CAGR ([TechSci](https://techsciresearch.com/report/hand-cream-market/19215.html)).
- Broader hand care (incl. wash and sanitizer): $26.35B (2024), 5.5% CAGR ([Market Publishers](https://marketpublishers.com/report/industry/other_industries/hand-care-market-size-share-trends-analysis-report-by-product-hand-creamsmoisturizers-hand-washsoaps-n-hand-sanitizersdisinfectants-by-distribution.html)).

### E7. Candle-warmer trend
- "Candle warmer lamp" has **246K monthly searches and +825% growth, flagged as "peaked"** ([Exploding Topics](https://explodingtopics.com/topic/candle-warmer-lamp)).
- Amazon US weekly searches ≈ 132,554. The top seller sells about 40k units/month, and the top 3 hold 39.5% click share ([AsInsight, Jul 2026](https://www.asinsight.com/report/US/candle-warmer-lamp)).
- SellerSprite projected 67% growth in 2023 and noted a **December sales peak** ([SellerSprite](https://www.sellersprite.com/en/blog/candle-warmer-lamps-report)).
- Media framing is "TikTok's new obsession" ([Ideal Home](https://www.idealhome.co.uk/all-rooms/all-rooms-decor/candle-warmer-lamp-cost-to-run)) and "The Must-Have Gift of 2024" ([Weather.com](https://weather.com/atmosphere/reviews/news/2024-03-03-candle-warmer-lamp-gift-ideas)). NBC Select is still publishing roundups in Oct 2026 ([NBC](https://www.nbcnews.com/select/shopping/best-candle-warmer-lamps-rcna244163)).
- **Read:** the trend is mature. Awareness is high and price competition is intense, so the lamp is a strong *complement* but a weak *standalone* hero product.

---

## F) Seasonality, guarantees and objections

### F1. Seasonal patterns
- **Q4:** ~35% of candle sales fall in the Christmas/holiday season ([NCA](https://candles.org/facts-figures/)). Some vendors put it closer to 60% ([search summary citing trade press](https://drugstorenews.com/news/lighting-sales-during-holiday-season)).
  - Candle-warmer lamp sales peak in December ([SellerSprite](https://www.sellersprite.com/en/blog/candle-warmer-lamps-report)).
  - NEOM's revenue rose 35% over the Christmas 5 weeks of 2021 ([Retail Bulletin](https://www.theretailbulletin.com/health-and-beauty/neom-hails-very-strong-christmas-trading-17-01-2022/)).
  - Black Friday promotions now run 44–45% off at NEOM ([NEOM](https://www.neomwellbeing.com/products/perfect-nights-sleep-scented-candle-3-wick)), and Fontana sells a $124.99 advent calendar ([Fontana](https://fontanacandlecompany.com/)).
- **Other gifting peaks:** Valentine's Day and Mother's Day are commonly cited for candle advertising ([Podcads](https://podcads.ai/industries/candles-fragrance/meta/testimonial-campaign)). Fontana sells a "Best Mom Ever" candle ([Shifting Gaia](https://shiftinggaia.com/en-us/collections/home-living/products/best-mom-ever-jar-candle)).
- **Hand-care seasonality (inferred):** dry, cracked hands peak in winter. This overlaps Q4 and Q1, which suggests a "winter hands" angle for January–February after gifting ends. I found no hard data source for this; it is an inference.
- **Timing for Núan (today is 1 Nov 2026):** BFCM and holiday gifting are imminent. The "gift" audience in the brief and the $119 ritual set (3 candles + lamp) fit Q4. A 3-pack works naturally as "one to keep, two to gift".

### F2. Guarantee structures seen

| Brand | Guarantee | Source |
|---|---|---|
| Yankee Candle | "Happiness Guarantee": **1 year**, applies "even if you just change your mind", US original purchaser | [Yankee](https://www.yankeecandle.com/warranty-return-policy.html) |
| Antique Candle Co. | "100% Happiness Guarantee": replace the candle if you don't love it "right out of the box" (limit 2 per order) | [Antique Candle Co.](https://antiquecandleco.com/pages/happiness-guarantee) (page 404 on fetch; terms from search snippet) |
| Fontana | "Love at First Light Guaranteed": 30 days; full refund if unused, 20% fee if <25% burned, store credit +25% | [Fontana](https://fontanacandlecompany.com/policies/refund-policy) |
| Homesick | 30 days, original condition and packaging | [Homesick](https://checkout.homesick.com/pages/returns) |
| Otherland | 30 days; satisfaction guarantee excludes normal wear and misuse | [Otherland](https://otherland.com/products/canopy) |
| Modern Aromatherapy | 14-day returns | [Modern Aromatherapy](https://modernaromatherapy.com/products/massage-candle-with-essential-oils) |
| Lumae | 14 days, unused | [Country Living Shop](https://countrylivingshop.co.uk/products/lumae-manicure-massage-candle) |
| O'Keeffe's (hand cream) | "guaranteed relief or money back" | [Home Hardware](https://www.homehardware.ca/en/p/4670090) |
| **Núan (brief)** | **14 days, unused candles only** (checkout badge says 30: inconsistent) | brief |

**Insight:** Núan's policy is the weakest in the set, and the 14 vs 30-day inconsistency is a trust and compliance risk. A ritual product can only be judged after use, so a *used-product* guarantee is the strongest objection-killer. Benchmarks are Fontana's tiered model and Yankee's change-your-mind model, or a hand-focused promise in O'Keeffe's style ("softer hands in X nights or your money back").

### F3. Common objections and how competitors handle them

| Objection | How competitors address it | Source |
|---|---|---|
| "Will hot wax burn my skin?" | Use within 10 min of lighting ("won't burn or feel uncomfortably hot"); burn about 12 min max; wait 30 s; patch-test | [Bustle / butter LONDON](https://www.bustle.com/beauty/butter-london-chelsea-blooms-manicure-candle), [Bee Inspired](https://beeinspiredgoods.com/collections/massage-candles) |
| "Sensitive skin / allergies" | Patch test on inner wrist; "hypoallergenic"; essential oils only | [Bee Inspired](https://beeinspiredgoods.com/collections/massage-candles), [Beeline](https://store.almanac.com/collections/for-you/products/bee-illuminated-lotion-candle); Kama Sutra reviewer warning "Do not use if u have sensitive skin" ([Kama Sutra search summary](https://foreveryourslingerie.ca/products/kama-sutra-massage-candle)) |
| "Greasy / too slippery for hands" | Reviewers call some massage candles thick and slippery, better for massage than quick hand care | [MELONY review summary](https://www.cherrypicksreviews.com/brand/melony) |
| "Candles give me headaches / toxins" | Founder story (headaches from a paraffin candle) plus third-party certification | [Fontana About](https://fontanacandlecompany.com/pages/aboutus) |
| "Too strong for sensitive noses" | "formulated for the most sensitive noses!" | [Fontana](https://fontanacandlecompany.com/) |
| "Open flame with kids or pets" | Warmer lamps; FDNY: less risk than a candle "that can be knocked down" | [NBC Select](https://www.nbcnews.com/select/shopping/best-candle-warmer-lamps-rcna244163) |
| "Warmer bulbs break / electricity cost" | Spare bulb included (Godonlif); cost criticism exists | [NBC](https://www.nbcnews.com/select/shopping/best-candle-warmer-lamps-rcna244163), [House Digest](https://housedigest.com/1213042/candle-warming-lamps-are-trending-but-are-they-better-than-burning-candles), [AJC](https://www.ajc.com/life/private-quarters/tiktoks-candlewarmer-lamps-are-trending-inside-homes/6BB5MCUXDVDFFIXHMQXN3PS3MM) |
| "Is it really clean? soy can be blended" | Fontana warns that some soy candles contain paraffin and that soy can be hexane-extracted | [Fontana About](https://fontanacandlecompany.com/pages/aboutus) |
| "What do I do with the jar?" | Repurpose as planter or storage jar | [Bustle](https://www.bustle.com/beauty/butter-london-chelsea-blooms-manicure-candle) |
| "Shelf life once opened" | Use within 6 months of opening | [Bee Inspired](https://beeinspiredgoods.com/collections/massage-candles) |
| "Price / value" | Bundles (NEOM trio, Fontana Build-Your-Bundle, Brooklyn Candle Studio up to 28%), subscriptions (Keap, BCS) | sources above |

### F4. Trust-signal benchmark and a red flag for Núan

| Brand | Review count claimed | Context |
|---|---|---|
| Fontana | 3,909 (store-wide) | Since 2018, 427 active ads ([Fontana](https://fontanacandlecompany.com/)) |
| Brooklyn Candle Studio | "3,200+ 5-STAR reviews" | Established DTC brand ([BCS](https://www.brooklyncandlestudio.com/collections/all)) |
| NEOM Perfect Night's Sleep 3-wick | 374 | UK B Corp ([NEOM](https://www.neomwellbeing.com/products/perfect-nights-sleep-scented-candle-3-wick)) |
| NEOM PNS at Ulta | 24 | ([Ulta](https://www.ulta.com/p/perfect-nights-sleep-scented-candle-pimprod2048904)) |
| **Núan Ritual Candle** | **"6,800+ reviews, 4.7★"** | Product created 2026-10-31, 0 site traffic and 0 ads per Trendtrack |

**Red flag:** Núan claims about 1.7x Fontana's total review base on a product created yesterday, with no measurable traffic. That is not credible to a savvy shopper. In the US it is also a legal risk. The FTC's final rule on fake reviews and testimonials took effect on 21 Oct 2024. It bans writing, buying or disseminating fake reviews, and penalties are up to about $51,744 per violation ([NutraIngredients-USA](https://nutraingredients-usa.com/Article/2024/08/16/ftc-announces-final-rule-banning-fake-reviews-and-testimonials), [Dvorak Law Group](https://dvoraklawgroup.com/ftc-final-rule-on-fake-reviews-and-testimonials-now-in-effect)). I did not check the rule's current legal status, so a legal review is advised. Competitors gain trust from certifications (MADE SAFE, B Corp), founder stories, press logos and explicit study footnotes. Núan needs real, verifiable trust assets instead.

---

## Strategic implications (summary for the next steps)

1. **Own "hand balm candle for bedtime".** NEOM owns "sleep + body oil candle". butter LONDON owns "manicure candle", but not sleep. Nobody owns *hands and cuticles + bedtime ritual + flame-free lamp*.
2. **Avoid "massage candle" as the lead term.** In the US it is dominated by sensual and adult products (Kama Sutra, MUTHA, LELO), which brings ad-policy and audience risk. Use "hand balm candle", "lotion candle" or "candle that turns into hand balm".
3. **Use the paraffin hand-bath comparison** as a contrast: the spa warm-wax hand treatment without the paraffin, the machine or the mess.
4. **Lead with "No paraffin, every note named"**, not "non-toxic". The science is mixed, and the market leader backs "non-toxic" with third-party certification.
5. **Price is fine for the candle** ($0.53/h single, $0.36/h in the 3-pack, vs Otherland $0.36/h, Boy Smells about $0.74/h, Diptyque $1.30+/h). **The $55 lamp needs bundling** against $16–30 Amazon lamps.
6. **Fix trust before spending on ads:** the review count, the 14/30-day guarantee mismatch, and the lack of a used-product guarantee.
7. **Q4 is now.** Package the 3-pack and ritual set as gifts. After Q4, pivot to a "winter hands" angle (inference) in January–February.
8. **Ad research must be completed after the 2026-11-10 credit reset** using the query plan in D5. Priority swipe files: NEOM (16.9M reach, 227 ads), Fontana (427 ads) and This Works (317 ads).
