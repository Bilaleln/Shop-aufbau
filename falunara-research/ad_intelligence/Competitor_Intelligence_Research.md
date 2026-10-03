# Competitor & Advertising Intelligence: FALUNARA Botanical Body Oil (U.S.)

**Data collected:** 2026-10-03 (all "days running" figures are as of this date)
**Scope:** U.S. advertising for mature-body-care and crepey-skin products aimed at women 40-65+.
**Sources:** Public Meta Ad Library (US, logged out) and Google Ads Transparency Center, both pulled with Playwright scrapers. TrendTrack was not used (0 credits). TikTok US was not available.
**Files:**
- `swipe_ledger.csv`: 122 analysed ads, one row each.
- `raw/*.jsonl`: raw scrapes. 40 non-empty Meta query files (plus 6 `.empty` markers for queries that returned 0 ads), 3 reused sample files in `scrapers/samples/`, and 4 Google files. The deduplicated master is `raw/_master_meta.jsonl` (849 unique Meta ad IDs).
- `raw/landing/*.txt`: rendered text of 22 landing-page attempts, 17 of them with usable content.
- `thumbs/`: 40 downloaded ad thumbnails and 3 contact sheets.
- `scrapers/`: the scripts used (`meta_batch.py`, `consolidate.py`, `select_ledger.py`, `build_ledger.py`, `landing_text.py`, `thumbs.py`, `sheet.py`).

**How to read the evidence:**
- The Meta Ad Library shows no spend, impressions, revenue or ROAS for non-political US ads. Nothing here is inferred about them.
- "Active" ads show today's date as their end date. In this report, `end_date ≥ 2026-10-02` means "still delivering".
- `days_running` = end_date − start_date.
- **Variants** = Meta's "N ads use this creative and text" (`collation_count`). **Concept IDs** = the number of distinct ad IDs in *our sample* that carry the same headline (Evora) or the same opening body text (competitors).
- Every count below comes from our scraped sample. The sample is a subset of the library: 30 ads are visible per page load.

---

## 1. Competitor landscape

### 1.1 Prioritised competitor set (ranked by relevance × advertising activity)

| Rank | Brand / product (price context) | Meta pages seen | Library volume (reported total for that query) | Earliest start seen → still live? | Why it matters to FALUNARA |
|---|---|---|---|---|---|
| 1 | **Evora Body: Botanical Body Oil™.** $49 (compare $69); 2-pack $39/bottle, 3-pack $34/bottle; subscription pre-selected; 90-day money-back guarantee. Clear glass bottle, golden oil, white pump. | Evora Body (1031841923353593) plus persona pages: **Natalie Brooks** (998946876632416), **Hannah Lewis** (885138048026249), **Ageless Glow Today** (957899007407821), **Daily Discounts** (1237233869479317), **HealthyClub** (686797521181950 → skinglowmagazine.com "Top 5" listicle that ranks Evora #1) | Evora page 291 (all statuses); Natalie Brooks 576; Ageless Glow Today 210; Daily Discounts 43; Hannah Lewis 33; HealthyClub 8 (active). Sum is 1,161, close to the 1,168 returned by the keyword "evorabody". | 2026-06-10 → yes (176 of 218 collected IDs still delivering) | **Direct twin:** same $49 price, same format (golden oil in a glass pump bottle), same audience and same "crepey" problem. It is the most aggressive advertiser in the set. |
| 2 | **Goda: Silk Body Oil.** $59 (compare $98); Buy 2 Get 1 / Buy 3 Get 2; countdown timer and "ONLY 12 LEFT" | Goda Perfume (123971964123694) plus persona pages **Over 40 & Fabulous** (691427450714766), **YiayiaEleni** (1212968901904027), **Dr Lila Merrit** (732023073327451). Perfume personas: Natasha Knows Scents, Steve The Perfumer | Goda page 96 active; Over 40 & Fabulous 8,854 (all statuses, includes perfume ads); keyword "goda.co" 3,953 active. Google: 164 creatives (UMAEZ LLC) since 2024-04-10 | 2025-05-29 (Over 40 & Fabulous) → yes | **Closest body-oil analog with the longest proven run.** Its crepey-skin testimonial concept has run about 16 months across 4 pages. |
| 3 | **NØRD BODY: Triple/Multi-Peptide Body Oil** (price not captured) | NØRD BODY (1162941896892016) plus persona **Body Confidence Daily** (820493664476157) | 609 active (brand page); 181 active (persona page) | 2026-06-08 → yes | A peptide body oil aimed at crepey skin and cellulite. Heavy replication of one short call-out (56 IDs in our sample). Advertorials cover GLP-1 and peptides. |
| 4 | **Besque: Magic Body Oil (XL 200 ml).** $120, or $78 on subscription (35% off); 7 cold-pressed oils | Besque (114239804036917) plus persona **40 Plus & Fabulous** (465173070005445) | 257 active (brand); 72 active (persona) | 2026-07-07 → yes | A natural body oil for women 50+. The persona page runs GLP-1 and family-story long copy. Evora's listicle ranks Besque "D+". |
| 5 | **VitaeCharm: Body Oil.** $32 for 1, $19/ea for 3, $15/ea for 5, plus free gifts | VitaeCharm (321287208643721) | 59 active | 2026-06-15 → yes | A crepey-skin body oil built around niche triggers (GLP-1, bruising, cancer survivors). Its mechanism is a "fat cushion layer". |
| 6 | **DRMTLGY: Retinol Body Lotion.** $36, or $27 on auto-ship | DRMTLGY (1089860041103335), Jamie's Finds, Derma Blogger | Keyword "retinol body lotion crepey" 825 active; page ≤2026-05-31 subset 43. Google: 80 creatives since 2023-01-03 | 2026-04-01 → yes | Retinol positioning. The single most-replicated competitor creative (50 IDs). |
| 7 | **Miami MD: Advanced Crepe Fix** (affiliate funnels) | Miami MD (109505650695478) | 753 active | 2026-05-09 → yes | "Harvard dermatologist" persona plus a named cause ("Fibroblast Failure"). Pages are affiliate prelanders, VSLs and quizzes. |
| 8 | **OSEA: Undaria Algae™ Body Oil.** $100 → $84 (subscription $75.60) | OSEA | Keyword "undaria algae body oil" 36 active | 2026-09-09 → yes | Premium "clean meets clinical" seaweed body oil. Evora also leads with wakame (Undaria) algae. |
| 9 | **Feline Skinscience: Advanced Crepe Fix**; **Frøya Organics** (via "Anne's Skincare Blog"); **Saeskyn** (K-beauty balm/PDRN); **TurmSkin** (HA serum) | own pages | Feline 82; Anne's Skincare Blog 468; Saeskyn 430; TurmSkin 23 (active) | Frøya 2025-02-21; Saeskyn 2025-12-10; TurmSkin 2025-12-31 | Adjacent face/neck crepey players with very long-running creatives (see §3). They are not body-oil competitors. |
| 10 | **Comparison and advertorial affiliates:** "Dr. Emily Carter" (emilycarterblog.com → **Cellu Deep Firming Body Cream**); "Women Skin Digest" (theskinmag.com → **Noor Copper Peptide Body Repair Cream**); "Crepey Skin Reset" (Orgatics softgels) | — | Keyword "crepe corrector" 277 active | 2026-08-18 → yes | They target the same "crepey arms" buyer through "I tested 5 creams" exposés. They name Gold Bond, Crépe Erase, StriVectin and Miami MD as losers. |

**Searched but not significant in the public library:**
- **Crepe Erase / The Body Firm:** the keyword "crepe erase" returned 0 ads. Its site sells a $49.95 2-step kit with the claim "91% experienced improvement in the appearance of crepiness in 8 weeks".
- **Gold Bond Crepe Corrector:** appears only as a "loser" inside competitor comparison ads.
- **Nécessaire Body Retinol:** 2 ads in the "body retinol" query.
- **Sol de Janeiro:** not searched separately. It did not surface in any crepey query.

**Category size signals (Meta keyword search, active, US):**

| Keyword | Active ads |
|---|---|
| "crepey skin" | 14,299 |
| "crepey arms" | 6,036 |
| "crepey body oil" | 4,981 |
| "body oil women over 50" | 50,001 (display cap; unordered match, includes irrelevant ads) |

### 1.2 The Evora ecosystem in detail
- **Five Meta pages plus one listicle page**, all linking to `evorabody.com`.
  - The brand page carries offer and scarcity ads plus story videos.
  - "Natalie Brooks" and "Hannah Lewis" carry long-form first-person advertorials. Median body length is 8,803 and 10,481 characters.
  - "Ageless Glow Today" mostly carries the story-video shell (median body 36 characters) plus Spanish variants.
  - "Daily Discounts" carries the offer and scarcity copy.
  - "HealthyClub" carries the comparison teaser.
- **218 unique Evora-ecosystem ad IDs collected**, about 19% of the 1,161 reported. Of these, 119 are video and 99 image. 200 of the 211 English ads use the CTA "Shop now".
- **Landing URLs:**

| Destination | Ads |
|---|---|
| PDP `/products/botanical-body-oil` | 195 |
| skinglowmagazine.com/top5-body-oil | 8 |
| Spanish PDP | 7 |
| quiz.evorabody.com | 4 |
| /pages/listicle8 | 3 |
| -cc PDP | 1 |

- **Scaling timeline:**
  - Start dates of the collected IDs: June 1, July 29, August 49, September 136, October (1-3) 3.
  - Library totals for the Evora page: 15 ads started ≤ 2026-07-31; 40 started ≤ 2026-08-31; 105 started 2026-09-01 to 09-15; 291 in total.
  - Natalie Brooks: 40 of 576 ads started ≤ 2026-08-31.
  - In other words, most ad volume was launched in September 2026. This shows repeated advertiser investment behaviour. It is not proof of profitability.
- **Google:** 35 creatives from advertiser "Snow Branding LLC" for evorabody.com.
  - First shown 2026-08-12. 34 are coded VIDEO.
  - Six videos ran from 2026-08-21 to 2026-09-30 (about 40 days).
  - One creative (CR03193359664054009857) has been shown 53 days and is still live.
- **Placements:** every collected Evora ad runs on Facebook, Instagram, Audience Network and Threads. 106 of 211 also run on Messenger and 75 on WhatsApp.

---

## 2. Ad swipe ledger

**`swipe_ledger.csv`** has **122 analysed ads**:
- 65 from the Evora ecosystem across 6 pages.
- 57 from 17 other advertisers/brands: Goda 11, Besque 7, NØRD 6, VitaeCharm 5, Miami MD 4, Frøya 4, DRMTLGY 3, OSEA 3, Saeskyn 3, Feline 2, theskinmag/Noor 2, and 1 each for Cellu/emilycarter, Beekman 1802, Beauty From Bees, Remedy Skin, Orgatics and an unbranded seeding page.

**How rows were chosen:**
- Every Evora headline × page combination is represented by its longest-running ad.
- The three highest-volume Evora concepts get extra rows for their longest-running and highest-variant IDs.
- For competitors: one row per concept × page, capped per brand.

**Fields:**
- Copy fields (`hook`, `headline`, `body_excerpt`) are verbatim. `body_excerpt` is cut at 320 characters and marked `[...]`.
- Analysis fields are analyst coding.
- `visual_pattern` states whether this exact ad's thumbnail was viewed.
- `evidence_strength` takes one of these values:
  - **HIGH**: ≥60 days running plus at least one more signal (replication ≥10 IDs, cross-page, or ≥3 collation), and still live.
  - **HIGH-historical**: the same signals, but the ad is now stopped.
  - **HIGH (concept-level)**: the ad ID is newer than 60 days, but its concept shows ≥3 non-longevity signals.
  - **MEDIUM** or **LOW** otherwise.

Evidence distribution in the ledger:

| Level | Rows |
|---|---|
| HIGH | 16 |
| HIGH (concept-level) | 10 |
| HIGH-historical | 9 |
| MEDIUM | 42 |
| MEDIUM (not delivering) | 10 |
| LOW | 35 |

### Top 25 ads by evidence strength
(Ranked by evidence tier, then days running. At most two rows per brand × headline.)

| # | Ad (Library link) | Page → brand | Start | Days | Variants / concept IDs in sample | Headline (verbatim) | Angle | Evidence |
|---|---|---|---|---|---|---|---|---|
| 1 | [980035185081066](https://www.facebook.com/ads/library/?id=980035185081066) | DRMTLGY → DRMTLGY | 2026-04-01 | 185 | 1 / 50 across 3 pages | Firm + Hydrate: Retinol Body Lotion That Enhances Elasticity | Dermatologist-developed retinol body lotion | HIGH: 185d; 50 IDs; 3 pages; live |
| 2 | [866991852497319](https://www.facebook.com/ads/library/?id=866991852497319) | Jamie's Finds → DRMTLGY | 2026-06-04 | 121 | 1 / 50 across 3 pages | Firm + Hydrate: Retinol Body Lotion That Enhances Elasticity | same | HIGH: 121d; 50 IDs; 3 pages; live |
| 3 | [1637558804018844](https://www.facebook.com/ads/library/?id=1637558804018844) | NØRD BODY → NØRD BODY | 2026-06-08 | 117 | 1 / 32 across 2 pages | Money Back Guarantee | Body-confidence call-out ("Ever avoid wearing shorts because of sagging or creepy skin?") | HIGH: 117d; 32 IDs; 2 pages; live |
| 4 | [1611807499919232](https://www.facebook.com/ads/library/?id=1611807499919232) | NØRD BODY → NØRD BODY | 2026-06-11 | 114 | 1 / 23 across 2 pages | Money Back Guarantee | Cellulite variant of the same call-out | HIGH: 114d; 23 IDs; 2 pages; live |
| 5 | [1361129475914444](https://www.facebook.com/ads/library/?id=1361129475914444) | Evora Body → Evora | 2026-06-16 | 108 | 1 / 18 across 3 pages | Try Evora risk-free for 90 days | Direct offer / risk reversal | HIGH: 108d; 18 IDs; 3 pages; live |
| 6 | [1564770261945264](https://www.facebook.com/ads/library/?id=1564770261945264) | Miami MD → Miami MD | 2026-06-18 | 107 | 1 / 11 | Smooth Away Crepey Skin - Try It Risk-Free! | Harvard-derm authority + named culprit | HIGH: 107d; 11 IDs; live |
| 7 | [2202226780628780](https://www.facebook.com/ads/library/?id=2202226780628780) | VitaeCharm → VitaeCharm | 2026-06-26 | 99 | 1 / 15 | Order Now & Get 4 Free Gifts ($70 value) | "Women Over 50 Are Ditching $400 Worth of Creams" | HIGH: 99d; 15 IDs; live |
| 8 | [999552596247291](https://www.facebook.com/ads/library/?id=999552596247291) | Dr Lila Merrit → Goda | 2026-06-28 | 97 | 1 / 27 across 4 pages | From dull to radiant—firmer, smoother skin in every touch 😍 | Testimonial transformation ("Dryness, saggy and crepey skin…") | HIGH: 97d; 27 IDs; 4 pages; live |
| 9 | [986622734003880](https://www.facebook.com/ads/library/?id=986622734003880) | Goda Perfume → Goda | 2026-06-28 | 97 | 1 / 27 across 4 pages | From dull to radiant—firmer, smoother skin in every touch 😍 | same | HIGH: 97d; 27 IDs; 4 pages; live |
| 10 | [1994209947876803](https://www.facebook.com/ads/library/?id=1994209947876803) | Dr. Muneeb Shah → Remedy Skin | 2026-07-01 | 94 | 1 / 2 across 2 pages | 93% saw smoother-looking neck skin after 4 weeks | Dermatologist-creator clinical stat | HIGH: 94d; 2 pages; live |
| 11 | [854380807531360](https://www.facebook.com/ads/library/?id=854380807531360) | Evora Body → Evora | 2026-07-17 | 78 | 1 / 44 across 2 pages | 437 Orders in Last Hour — Almost gone | Scarcity "LIVE UPDATE" | HIGH: 78d; 44 IDs; 2 pages; live |
| 12 | [1706136800647003](https://www.facebook.com/ads/library/?id=1706136800647003) | Evora Body → Evora | 2026-07-17 | 78 | 1 / 44 across 2 pages | 437 Orders in Last Hour — Almost gone | same | HIGH: 78d; 44 IDs; 2 pages; live |
| 13 | [1570129684499222](https://www.facebook.com/ads/library/?id=1570129684499222) | Evora Body → Evora | 2026-07-18 | 77 | 1 / 3 across 2 pages | Why most body lotions & creams don't work | Mechanism-led ("70 to 80 percent water") | HIGH: 77d; 2 pages; live |
| 14 | [2329433507867811](https://www.facebook.com/ads/library/?id=2329433507867811) | Hannah Lewis → Evora | 2026-07-20 | 75 | **7** / 6 | The Spa Owner's Personal Oil | Professional-insider discovery | HIGH: 75d; 7 ads use creative; live |
| 15 | [1021976634228403](https://www.facebook.com/ads/library/?id=1021976634228403) | Natalie Brooks → Evora | 2026-08-20 | 44 | 4 / 12 across 2 pages | The secret inside a wealthy family's house | Wealthy-household insider confession | HIGH (concept): 12 IDs; 2 pages; 4 variants; live |
| 16 | [1954753225212676](https://www.facebook.com/ads/library/?id=1954753225212676) | Evora Body → Evora | 2026-08-22 | 42 | 4 / 41 across 3 pages | Here’s What Actually Works… | Story-video shell | HIGH (concept): 41 IDs; 3 pages; live |
| 17 | [1094353849622035](https://www.facebook.com/ads/library/?id=1094353849622035) | Daily Discounts → Evora | 2026-09-21 | 12 | 5 / 18 across 3 pages | Try Evora risk-free for 90 days | Direct offer | HIGH (concept) |
| 18 | [1140179468691458](https://www.facebook.com/ads/library/?id=1140179468691458) | Evora Body → Evora | 2026-09-22 | 11 | 6 / 41 across 3 pages | Here’s What Actually Works… | Story-video shell | HIGH (concept) |
| 19 | [4109833019265205](https://www.facebook.com/ads/library/?id=4109833019265205) | Over 40 & Fabulous → Goda | 2025-08-04 | **314** | 1 / 27 across 4 pages | Visibly Firmer & Glowing Silky Smooth Skin 😍 | Testimonial transformation | HIGH-historical (stopped 2026-06-14) |
| 20 | [4351937398417845](https://www.facebook.com/ads/library/?id=4351937398417845) | Over 40 & Fabulous → Goda | 2025-11-28 | 202 | 1 / 14 across 4 pages | 2 Drops That Will Change Your Life! 😍 | Perfume copy (off-category) linking to the body-oil page | HIGH-historical (stopped 2026-06-18) |
| 21 | [1070866808556946](https://www.facebook.com/ads/library/?id=1070866808556946) | Over 40 & Fabulous → Goda | 2026-02-13 | 170 | 4 / 1 | One Bottle That Changed My Skin Game 😍 | Identity / future-self ("She doesn't analyze her arms in every mirror") | HIGH-historical (stopped 2026-08-02) |
| 22 | [965929252430847](https://www.facebook.com/ads/library/?id=965929252430847) | Over 40 & Fabulous → Goda | 2026-03-25 | 118 | 3 / 1 | Firmer neck and arms in 30 days 😍 | Cause-explainer | HIGH-historical (stopped 2026-07-21) |
| 23 | [1544710363874243](https://www.facebook.com/ads/library/?id=1544710363874243) | Natalie Brooks → Evora | 2026-07-09 | 73 | 1 / 4 across 2 pages | The “Weird Oil” In Our 5-Star Airbnb | Luxury-rental insider discovery | HIGH-historical (stopped 2026-09-20) |
| 24 | [4208470512761373](https://www.facebook.com/ads/library/?id=4208470512761373) | Ageless Glow Today → Evora | 2026-07-13 | 70 | 1 / 3 across 2 pages | Why most body lotions & creams don't work | Mechanism-led | HIGH-historical (stopped 2026-09-21) |
| 25 | [2475651179440524](https://www.facebook.com/ads/library/?id=2475651179440524) | Anne's Skincare Blog → Frøya Organics | 2025-02-24 | **586** | 2 / 2 | Save 40% if you buy right now! | Blogger-persona testimonial (face balm) | MEDIUM: 586d single concept; live |

---

## 3. Longest-running and strongest-evidence concepts

**Concept-level evidence (our sample):**

| Concept | Signals | Evidence label |
|---|---|---|
| **Goda: "Dryness, saggy and crepey skin… I struggled with it all for years until I realized I was doing it all wrong" (Michelle D. testimonial; creams sit on top, oils penetrate)** | 27 brand-attributed IDs plus 2 unlinked Over 40 & Fabulous posts with the same verbatim body. **4 pages** (Over 40 & Fabulous 15, Goda Perfume 9, YiayiaEleni 2, Dr Lila Merrit 1). The earliest instance started 2025-05-29 and the concept is still delivering on 2026-10-03, a **~16-month concept span**. The single longest ID ran 314 days. 16 IDs are live. Headlines rotate ("Visibly Firmer & Glowing Silky Smooth Skin 😍", "From dull to radiant…", "Buy 2 Get 1 FREE NOW! 😍", BFCM). Formats: image (before/after back, "#1 choice" graphic), video and DCO. | **High-confidence control (Goda).** It has longevity, replication, cross-page and cross-creative persistence. |
| **Evora: "437 Orders in Last Hour — Almost gone" / "LIVE UPDATE: Stock dropping faster than we can count."** | 44 IDs (Evora Body 27, Daily Discounts 17). 26 video and 18 image. Collation sum 66. Runs from 2026-07-03 to still live (longest 79 days; 36 IDs live). The creative visuals differ from the copy: one is "EVORA SENIOR SALE – ENDS MIDNIGHT … CODE SENIOR62". | **High-confidence Evora control** for the offer/scarcity slot (prospecting status unknown). |
| **Evora: "Try Evora risk-free for 90 days" / "Evora Botanical Body Oil — 50% off until midnight tonight."** | 18 IDs across 3 pages (Evora 9, Daily Discounts 8, Ageless Glow 1). 108-day oldest still live. Spanish clone launched 2026-09-30. | **High-confidence Evora control.** |
| **Evora: "Here’s What Actually Works…" / "THIS is what Oil does for your skin…" (video shell)** | 41 IDs across 3 pages (Ageless Glow 21, Evora 17, Natalie Brooks 3). Collation sum 91, the highest of any concept. 39 live. Started 2026-08-22, with most IDs from 2026-09-15 to 10-02. Each ID carries a different 9:16 story video. | **High replication, short history.** This is Evora's current scaling vehicle, not yet a proven long-run control. |
| **Evora: long-form persona "luxury insider" advertorials** (Natalie Brooks plus Hannah Lewis) | 85 Evora ads have bodies over 1,500 characters (Natalie Brooks 54, Hannah Lewis 27, Ageless Glow 4). There are ≥25 distinct headlines. Specific headlines persist across pages: "The secret inside a wealthy family's house" (12 IDs, 2 pages), "The butler brought me this “weird” oil" (9 IDs, 2 pages; collation 11 on one ID), "The “Weird Oil” In Our 5-Star Airbnb" (4 IDs, 2 pages, 73d). July-launched story ads still live after about 78-84 days: "He ‘hates’ this oil now 😂" 84d, "He's still mad about a $14 drink someone else bought me 😂" 78d, "This One Package Has Women Waiting at the Door" 78d, "The “Weird Serum” In Our 5-Star Airbnb" 78d. | **Medium-high.** The territory shows persistence and heavy reinvestment (576 Natalie Brooks ads in total). Individual stories rotate quickly. |
| **DRMTLGY: "Firm + Hydrate: Retinol Body Lotion That Enhances Elasticity"** | 50 IDs across 3 pages (DRMTLGY, Jamie's Finds, Derma Blogger). Oldest live 185 days (from 2026-04-01). DCO catalogue format. | **High** (for a retinol/clinical positioning, not an oil). |
| **NØRD: "Money Back Guarantee" + "Ever avoid wearing shorts because of sagging or creepy skin?"** | 56 IDs across 2 pages (brand plus "Body Confidence Daily") for the sagging and cellulite variants combined. Oldest 117 days, live. | **High** replication and longevity. A short call-out paired with advertorial landers. |
| **Saeskyn "One Stick. Zero Wrinkles. 48 Hours."** (297d), **TurmSkin "⏰LAST CHANCE!⏰Sale Ends Today..."** (276d, 21 IDs), **Frøya "Save 40%…"** (586d), **Frøya "Retinol thins your skin [Try the real fix]"** (525d, stopped 2026-09-29) | Very long single-concept runs by adjacent face-care advertisers. | Medium-high for those brands. Low transferability to body oil. |
| **Unbranded seeding: "Joanna Woodley"** text-only, link-less question ads (e.g. "my esthetician said i need a hyaluronic acid body serum for my crepey arms. anyone have a brand they actually love?") | 30 distinct question texts collected (75 active on the page). 14 of the 30 are about crepey arms, body serums or hyaluronic acid. Others cover different categories (for example liver detox, mullein). Earliest 2025-11-29, longest crepey-related ID 308 days. Similar crepey question pages: "Fiona Hughes" (from 2026-02-05), "Claudia Neumann" (from 2026-02-24). | Medium (longevity). The beneficiary brand cannot be identified from the library. The page appears to be a multi-category seeding account. |

**What is *not* established:**
- No spend, reach or ROAS for any ad.
- Whether "437 Orders" or the persona stories are profitable cannot be determined. Evora's shift of new volume into September story videos and persona pages is a behavioural signal only.

---

## 4. Recurring patterns (counts from our data)

**Evora base:** 211 English Evora-ecosystem ads across 6 pages. The story-video shell (41 IDs) has almost no body text, so text-based counts understate patterns that live only inside videos.

**Hooks and openers**

| Pattern | Evora ads (of 211) | Pages |
|---|---|---|
| "Let me rewind" / "Let me back up" / "Let me tell you the story" story pivot | 63 | 2 (Natalie Brooks, Hannah Lewis) |
| Confession / forbidden opener ("I'm probably going to get fired for posting this", "I'm going to lose this job for telling you this", "I'm not proud of it", "I stole a bottle of body oil…") | 29 | 2 |
| Insider/servant narrator (nanny, butler, chauffeur, caregiver, Biltmore tour guide, spa owner, cruise massage therapist, cabin attendant, vacation-rental manager, USPS driver, flight attendant) | 52 | 3 |
| Wealth/luxury setting (Ritz Paris, Aman Tokyo, yacht, private island, first-class Dubai, Biltmore, Hamptons, cruise) | 71 | 3 |
| Self-stated age 56-64 ("I'm 56", "I'm 62", "I'm 64") | 57 | 3 |
| Husband/spouse reaction line | 81 | 2 |

Competitors use the same hook families: Goda's quoted-testimonial opener; NØRD's "Ever avoid wearing shorts…"; Feline's "The Crepey Skin Myth"; theskinmag's "My sister is 4 years older. Her arms looked 10 years younger."; Orgatics' profane rogue-doctor opener.

**Problem framing and desire**

| Pattern | Evora ads (of 211) | Pages |
|---|---|---|
| "crepey" | 97 | 6 |
| "papery/thin" | 92 | 4 |
| arms | 88 | 4 |
| chest | 84 | — |
| hands | 81 | — |
| Hiding/sleeveless desire (sleeveless, sleeves, cardigan, cover-up, swimsuit) | 80 | 3 |
| Menopause | 79 | 4 (mostly long-form personas) |

Evora's standard link description, "Say goodbye to crepey, saggy & dry skin. This botanical body oil visibly restores firmness and smoothness in just 2 minutes a day. See real results in 3–4 weeks — or get your money back.", appears in 48 ads across 4 pages.

Among 466 competitor ads from 15 crepey/body brands:

| Pattern | Ads | Brands | Main users |
|---|---|---|---|
| "crepey" | 189 | 14 | — |
| Sleeveless/shorts/hiding | 93 | 7 | NØRD 56, Goda 19, Besque 10 |
| Explicit menopause | 8 | 4 | — |

**Mechanisms**
- **"Creams are mostly water and evaporate; oil passes the lipid barrier and reaches deeper"** is the category's dominant mechanism.
  - Evora: 86 of 211 ads mention water/evaporation; 83 mention lipid barrier, melt, sink in or reach deeper; 70 mention replacing what skin "stopped making/producing" after 50 or menopause.
  - Competitors: 98 of 466 ads across 9 brands (VitaeCharm 26, Goda 22, Besque 13, Saeskyn 13, Frøya 10, Orgatics 6).
  - Landing pages for NØRD, VitaeCharm and Evora all repeat "~80% water" or "70 to 80 percent water".
- **Named-ingredient proof.** Evora names wakame/Undaria algae, Brazil nut, passionflower seed, rice bran, argan and vitamin E (wakame appears in 81 ads). "Cold-pressed" appears in 103 Evora ads.
- **Competitors use different mechanism stories:**
  - Peptides: NØRD (copper peptides, caffeine, CoQ10); theskinmag/Noor ("1973 Nobel Prize discovery").
  - "Fat cushion layer" plus GLA/palmitoleic acid: VitaeCharm.
  - "Fibroblast Failure" / ribose and "Progerin": Miami MD.
  - Retinol: DRMTLGY.
  - PDRN / salmon DNA: Saeskyn.
  - TEWL: Goda's dermatologist page.

**Promises and claims**
- Time-boxed results: "2 minutes a day", "3–4 weeks"; 111 of 211 Evora ads mention "two minutes" or "two pumps".
- Evora's PDP gives a results timeline: Day 1 → Week 2–3 → Week 6–8 → Week 8–12 ("Sleeveless tops. Bracelets.").
- Competitors cite stat claims: Feline "21.7% Reduction in visible crepiness in 7 days"; NØRD "91% said…"; Saeskyn "94% saw firmer skin in 4 weeks"; Goda "89% Reduction on sagging skin and thigh" on its PDP.

**Offers and CTAs**

| Offer element | Evora ads (of 211) |
|---|---|
| 90-day money-back guarantee | 148 |
| 50% off / sale | 107 |
| Scarcity/stock language | 98 |
| "50,000+" customers | 19 |

- Evora stacks codes: SENIOR62 (+12%) and LABOR64 (50% + 14%).
- Evora CTA button: "Shop now" on 200 ads, "Learn more" on 11 (the HealthyClub listicle teaser and quiz).
- Competitors:
  - BOGO-style ("Buy 2 Get 4 FREE", "Buy 2 Get 1 FREE"): 44 ads across 6 brands.
  - "% off": 82 ads across 8 brands.
  - Guarantee language: 175 ads across 9 brands.
  - Subscription pre-selected with a "BUY ONCE - NO SAVINGS →" link: Evora, Goda and VitaeCharm PDPs all use this identical UI pattern.

**Stories and advertorial structures**
1. **Luxury-insider discovery** (Evora core): forbidden confession → "Let me rewind" → narrator age and job → luxury inventory with dollar figures → minimalist bathroom shelf with "one small amber pump bottle" (amber appears in 62 Evora ads) → "it costs about forty dollars" (a ~$40 price anchor in 53 ads, 3 pages) → transformation noticed by others → mechanism → offer.
2. **Spouse-jealousy comedy:** husband's punchline at dinner → "Let me rewind" → trip → hotel-bathroom oil.
3. **Quoted-testimonial transformation** (Goda): "I was doing it all wrong" → aesthetician's tip → skepticism about greasiness → weeks-based result → P.S. about the daughter.
4. **Comparison exposés:** Evora's own "Top 5 Body Oils for Crepey, Dry & Dimpled Skin of 2026 — Tested & Reviewed by a Dermatologist" (Evora A+, Goda C, Besque D+). The "Emily Carter" 5-cream test (Cellu wins).
5. **Niche-trigger reason-why** (VitaeCharm, Besque persona, NØRD advertorial): post-GLP-1 skin. 24 of 466 competitor ads across 3 brands. Evora: 0.
6. **Life-event emotional** (Evora): solo World Cup trip, a widow's World Cup promise, mother-of-the-bride sleeveless dress (Besque persona).

**Visual patterns** (from 40 thumbnails viewed; see `thumbs/sheet1-3.jpg`)
- **Evora persona images** are native, non-product photos: superyacht, Ritz Paris street, Biltmore exterior, Hawaii airport arrivals, police SUV outside a Honolulu hotel, delivery-truck POV, sauna with robed women. The product is not shown.
- **Evora story videos (9:16)** come in two styles:
  - (a) AI-generated cinematic scenes with burned-in captions ("Three years inside", "My son got married in June,", "My ex-husband", "Every August for nineteen years,", a stylised blue-skinned woman reading "To every Evora customer").
  - (b) A grey-haired female narrator on green screen over luxury photos ("I stayed at the Burj Al Arab in Dubai", "The richest family in American history", "The family I nanny for has eight crew on their boat").
- **Evora offer images:**
  - "EVORA SENIOR SALE – ENDS MIDNIGHT" with a bottle line-up.
  - "Almost sold out… Restock in 2 months" with a cartoon bottle mascot running ahead of a crowd of women.
  - "NATURAL BOTOX IN A BOTTLE?" product-callout diagram.
  - A clean bathroom-vanity hero shot of a clear glass bottle with golden oil and a white pump.
- **Competitors:**
  - Goda: before/after split of a mature woman's back/arm ("BEFORE GODA / 2 WEEKS ON GODA") with a 50% OFF badge.
  - NØRD: handwritten "Rebuilds Collagen In 4 Weeks" on a thigh beside the bottle.
  - VitaeCharm: macro of an oiled crepey forearm with "stop using coconut oil for Ozempic skin anymore".
  - Besque: "The World's No.1 Body Oil", Trustpilot badge, $120 → $78.
  - Evora/HealthyClub: "READ THIS BEFORE BUYING CREPEY SKIN BODY OILS" with a BAD→EXCELLENT scale.
  - theskinmag: side-by-side forearms ("Her arm. My arm. MY CREPEY ARMS AT 61.").
  - Feline: clinical-stat card.

**Landing-page patterns**
- **Evora:**
  - Most traffic (195 of 218 ads) goes straight to the PDP: $49/$69, three bundle tiers, pre-selected subscription, "89% sold" bar, 90-day guarantee, lipid-barrier mechanism block, six hero ingredients plus full INCI, week-by-week timeline, and a "vs Others" table.
  - Secondary destinations: a 7-reasons listicle, a $105-discount quiz with an age gate, and a third-party-styled "Top 5" ranking.
- **Competitors:**
  - Advertorial listicles: NØRD "7 Reasons Women Are Switching to Peptides…", TurmSkin "7 Reasons Why Women Over 30…", VitaeCharm "10 reasons / 7 reasons" variants.
  - First-person long-form landers: NØRD "Down 38 Pounds…", theskinmag "1973 Nobel Prize Discovery".
  - Affiliate prelanders, VSLs and quizzes: Miami MD.

---

## 5. Candidate control territories
(These are territories with multi-signal evidence that the category's advertisers keep paying to run. They describe competitor behaviour only. They are not FALUNARA copy.)

1. **"Creams sit on the surface / are mostly water → a pure oil reaches deeper and replaces what mature skin stopped making."**
   - Evidence: 86 of 211 Evora ads plus 98 of 466 competitor ads across 9 brands.
   - Carried by Goda's ~16-month cross-page testimonial and repeated on the Evora, NØRD and VitaeCharm landers.
   - **Strength: High** (cross-advertiser convergence plus longevity).
2. **Quoted first-person crepey-skin transformation testimonial** (Goda "Dryness, saggy and crepey skin… I was doing it all wrong").
   - Evidence: 27+ IDs, 4 pages, single ad 314 days, concept span 2025-05-29 → live.
   - **Strength: High.**
3. **Hiding arms / sleeveless confidence as the core desire**, with arms, chest and hands as the named zones.
   - Evidence: Evora 80 ads on hiding/sleeveless and 88 on arms; NØRD 56 ads on "Ever avoid wearing shorts/sleeveless…" (117 days); Goda identity ad 170 days.
   - **Strength: High.**
4. **Offer architecture: 50% off with a deadline + long money-back guarantee (90 days at Evora and VitaeCharm) + scarcity/stock + subscription default.**
   - Evidence: Evora "437 Orders" 44 IDs over 2 pages for up to 79 days; "Try Evora risk-free" 18 IDs, 108 days; the same PDP UI at Goda and VitaeCharm.
   - **Strength: High** for prevalence. Effectiveness is not measurable.
5. **Long-form persona-page "luxury insider" advertorials** (the rich woman's single amber bottle; five-star hotel "weird oil"; ~$40 price anchor).
   - Evidence: Evora's primary prospecting engine by volume (Natalie Brooks 576 ads; ≥25 headlines; July stories still live at 78-84 days; several headlines cloned across 2 pages).
   - **Strength: Medium-high.** The territory persists, individual executions churn, and there is no performance data.

## 6. Candidate challenger territories
(Emerging or under-exploited. Evidence is lower or newer.)

1. **Post-GLP-1 / weight-loss crepey skin.**
   - Evidence: VitaeCharm (10 IDs, 110 days live), Besque persona (Sept 2026), NØRD advertorial "Down 38 Pounds…", Beekman "Firm Skin After Weight Loss".
   - Evora has 0 ads here, so it is an open flank.
   - **Strength: Medium.**
2. **Third-party comparison / "ranked #1" listicles.**
   - Evidence: HealthyClub → skinglowmagazine (8 IDs since 2026-08-22, all live); "Dr. Emily Carter" → Cellu (since 2026-08-18).
   - Rival brands are already being named and graded publicly.
   - **Strength: Medium** (newer than 60 days).
3. **AI-generated story reels / green-screen narrator videos on a single caption shell.**
   - Evidence: Evora 41 IDs and collation 91, launched mostly in the second half of September.
   - **Strength: Medium.** High replication but no longevity yet.
4. **Peptide / "science-upgrade" body oil** (copper peptides, triple peptides, "1973 Nobel" story).
   - Evidence: NØRD 117 days; theskinmag/Noor since Sept 24.
   - **Strength: Medium-low** for the newer executions.
5. **Explicit menopause framing in short-form ads.**
   - Evidence: only 8 of 466 competitor ads say "menopause". Evora uses it mostly inside long-form personas (79 ads).
   - **Strength: Low** (an absence signal, not a performance signal).
6. **Spanish-language U.S. Hispanic variants.**
   - Evidence: Evora 7 Spanish ads (from 2026-09-13, Ageless Glow Today and Evora); Saeskyn has Spanish DCO running 221 days.
   - **Strength: Low-medium.**
7. **Organic-looking question "seeding" text ads.**
   - Evidence: "Joanna Woodley", 75 active ads; 14 of 30 collected are crepey/HA-body-serum questions, the longest running 308 days; brand unidentified.
   - **Strength: Low-medium.** It also carries compliance and authenticity risk.
8. **Product-format similarity.**
   - Observation: Evora's bottle (clear glass, golden oil, white pump), $49 price and "botanical body oil" name sit very close to FALUNARA's stated format and price.
   - This is a positioning observation for the brief, not an ad territory. Differentiation needs will need validation against VOC.

---

## 7. Evidence gaps and tool limitations

**Data sources**
- **TrendTrack unavailable** (0 credits). There is no third-party ad-spend, impression or "scaling" estimate, and no transcript or creative-history data. Everything comes from the public Meta Ad Library (US, logged out) and the Google Ads Transparency Center.

**Meta Ad Library limits**
- **About 30 ads per page load.** Scroll pagination returns a rate-limit error when logged out. Coverage was widened by splitting queries:
  - by page ID;
  - by status;
  - by media type;
  - with `start_date[max]`, which worked;
  - with `start_date[min]`, which on its own appeared to be ignored but worked combined with max;
  - with exact-phrase search.
- **Evora coverage is 218 of about 1,161 reported ads (~19%).** Competitor coverage is mostly 30 ads per page. Concept counts are therefore lower bounds from the sample and should not be read as library totals.
- **HTTP 403 rate limiting.** It occurred 2 times across about 50 Meta loads, spaced about 25 seconds apart. Both were handled with 240-second back-offs, and the retries succeeded. Two more loads hit transient navigation errors and were also retried successfully.
- **The inactive filter returned 0 ads** for every query (Evora page, keyword "evorabody"). It is unclear whether logged-out access hides inactive ads or none exist. As a result, ads that stopped are visible only when their `end_date` is in the past while still listed. Historical (stopped) creative history is largely invisible.
- **No spend, reach, impressions or ROAS.** Meta does not disclose these for non-political US ads, and none were inferred. Longevity, replication and cross-page persistence are proxies for advertiser behaviour, not proof of profit.
- **Dates:** the `end_date` of active ads equals the scrape date. `days_running` therefore measures observed delivery so far. Start dates are Meta's "Started running on".
- **DCO / catalogue ads** show template placeholders. Copy was recovered from the first dynamic card only, so other card permutations are not analysed.
- **Story-video content** was assessed from thumbnails only (40 viewed). No transcripts or audio were captured, which is why text counts understate video-only patterns.

**Other channels**
- **Google Ads Transparency:** advertiser, first/last-shown dates and a days-shown field were captured:

| Domain | Creatives | Advertiser |
|---|---|---|
| evorabody.com | 35 | Snow Branding LLC |
| goda.co | 164 | UMAEZ LLC |
| drmtlgy.com | 80 | Drmtlgy, LLC (+1 other) |
| saeskyn.com | 0 | — |

  Copy for video and text creatives sits in preview JS and was not extracted. The scraper's format labels (1=TEXT, 2=IMAGE, 3=VIDEO) are an unverified mapping.
- **TikTok US is unavailable.** The TikTok Ad Library covers EU/EEA/UK/CH only (US returns HTTP 421). Creative Center keyword search is disabled, so no TikTok evidence is included.

**Landing pages**
- 22 page renders were attempted (text only, no screenshots), plus 3 WebFetch reads. Several could not be read:
  - Miami MD: a plain-HTTP URL that the proxy refused.
  - Feline product page: 404.
  - VitaeCharm advertorial: redirected to the homepage.
  - Nécessaire and Gold Bond URLs: 404.
- Evora's PDP was read on 2026-10-03. Prices and offers change frequently.

**Attribution limits**
- Persona pages are linked to brands only by landing domain. No ownership claim is made beyond that.
- Two "Over 40 & Fabulous" posts with no link were matched to Goda by verbatim body text only.
- The "Joanna Woodley" seeding ads have no identifiable beneficiary.

**Other caveats**
- Some competitor claims quoted from pages (for example "dermatologist", "clinically proven", review counts, "437 orders") are the advertisers' own statements and were not verified.
- FALUNARA's ingredients are unknown. No comparison of FALUNARA's ingredients with competitors' ingredients was made.
