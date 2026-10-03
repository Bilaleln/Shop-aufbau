# VOC Prompt 1 — Relevant Community / Subreddit Research
**Product:** FALUNARA Botanical Body Oil · **Market:** U.S. · **Target:** U.S. women 40–65+ (core 48–58) with dry, crepey-looking, mature body skin
**Date of research:** 2026-10-03 · **Status:** Community map only — no VOC conclusions drawn. Feeds VOC Prompt 2 (URL corpus).
**Raw discovery hits (title + URL + date per subreddit/query, 944 rows):** `voc1_raw_search_hits.md` (same folder)

---

## 1. Method (what was actually done)

- **Reddit (primary):** curl against Reddit Atom/RSS endpoints (subreddit feed `/r/<sub>/.rss` and in-sub search `/r/<sub>/search.rss?q=…&restrict_sr=1&sort=relevance&t=all&limit=25`), ≥7–8 s between requests, 45 s back-off on HTTP 429 (heavy 429s observed; shared IP with other agents). 68 Reddit requests completed across 30 candidate subreddits.
- **Activity gauge:** the default `.rss` feed (Reddit "hot" listing, 25 entries) — counted how many entries are dated within the last 2 / 7 days. Feed fetched for 12 core candidates; for lower-priority subs only searches were run (existence confirmed by results returned).
- **Relevance counts:** an automated title keyword screen (crepey/crepe, body oil/lotion/cream/care, dry/itchy skin, arms/legs/shins/knees/hands/chest/neck, menopause + skin, aging skin, firming…). Two numbers are reported per query: **topic-screened** (any topic keyword) and **body-area** (also names a body area/body product). This is a *title-only heuristic*: it over-counts face/eye "crepey" threads in the topic number and under-counts some clearly relevant body threads (e.g. "Over 40s gang who neglected the skin on your bodies…" was not flagged). Thread bodies/comments were **not** read.
- **Member counts:** Reddit's `about.json` returned HTML (blocked) from this environment, so **subscriber/member counts are not visible and are not reported**.
- **Off-Reddit:** WebSearch (reddit.com is not searchable by WebSearch here — returns a 400 domain error) plus curl/WebFetch accessibility tests on forum candidates.
- Dates are the Atom `<updated>` value of each post.

---

## 2. Prioritized Community Map (Reddit)

### TIER 1 — Core corpus sources (build VOC 2 here first)

| # | Community / URL | Relevance rationale | Recurring relevant topics (from titles observed) | Activity / quality (observed) | Noise risks | Recommended search terms |
|---|---|---|---|---|---|---|
| 1 | **r/40PlusSkinCare** — https://www.reddit.com/r/40PlusSkinCare/ | Age-gated audience closest to the 48–58 core; body-skin and crepiness discussed explicitly | Crepey legs/knees/neck/hands; "anti aging body care routine"; body lotion texture/absorption; lactic acid / urea / retinol body lotions; scaly lower legs; Gold Bond Crepe Corrector reactions | Feed: 24 of 25 hot posts dated within last 7 days (21 within 2 days). `crepey OR crepe`: 24/25 topic, 9/25 body-area; 20 of 25 hits from 2026. `body`: 12/25 body-area | Many crepey threads are face/eye/neck (≈ half); in-office procedure talk (RF microneedling, Sculptra, Profhilo, HALO); some off-topic personal posts | `crepey legs`, `crepey arms`, `crepey knees`, `body care routine`, `body lotion`, `body oil`, `dry legs`, `scaly`, `urea`, `lactic acid body`, `crepe corrector`, `menopause skin` |
| 2 | **r/30PlusSkinCare** — https://www.reddit.com/r/30PlusSkinCare/ | Large anti-aging sub with many 40+/50+ posters; strongest volume of body-oil usage threads | Body oil vs lotion; when/how to apply body oil (damp skin, step order); "after 50"; crepe-paper hands; crepey forearms; anti-aging body care (retinol, exfoliant); "neglected the skin on your bodies" | Feed: 24 of 25 hot posts within 2 days. `"body oil"`: 20/25 topic, 19/25 body-area (2020–2026). `crepey OR crepe`: 12/25 topic, 7/25 body-area. `aging skin body`: 5/25 by screen, several more relevant on manual read | Skews 30s; face-dominant; injectables/laser threads; Mounjaro/weight-loss skin | `body oil`, `body oil vs lotion`, `crepey arms`, `crepey hands`, `body anti-aging`, `after 50 body`, `rest of my body`, `dry skin body`, `retinol body` |
| 3 | **r/Menopause** — https://www.reddit.com/r/Menopause/ | Contextual: hormonal-transition women describing sudden body-skin change in their own words (use as context, not assumed for all customers) | "My hands and arms have suddenly become crepey"; "What happened to my arms?"; "Super dry skin on legs"; "Lizard skin!!"; itchy skin; shiny legs/arms; HRT & skin | Feed: 24 of 25 hot posts within 2 days. `dry skin arms legs`: 12/25 topic, 6/25 body-area (7 of 12 from 2025). `crepey OR crepe`: 8/25 topic. `"body oil"` only 10 results (4 topic) | Very high HRT/medical noise (estrogel application site, vulvar care, formication/itch as symptom); emotional/relationship threads; titles often vague ("Grrrrr") | `crepey`, `crepe skin`, `dry skin`, `itchy skin`, `lizard skin`, `arms skin`, `legs skin`, `body lotion`, `skin changes`, `sagging skin` |
| 4 | **r/SkincareAddiction** (SCA) — https://www.reddit.com/r/SkincareAddiction/ | Largest general skincare sub; very high body-oil thread volume; some mature body crepiness | Body oil recs (unscented, dry skin, after-shower, dupes); oil + lotion layering; AmLactin "Crepe" vs regular; "all over body crepey skin"; "old lady crepey wrinkly skin" | Feed: 25 of 25 hot posts within 2 days. `"body oil"`: 24/25 topic+body (22 of 24 from 2025–26). `dry skin arms legs`: 18/25 topic, 11/25 body-area. `crepey OR crepe`: 21/25 topic but only 4/25 body-area | Skews younger (teens–30s); face/acne dominant; crepey hits mostly eyes; fragrance-driven body-oil posts | `body oil dry skin`, `after shower body oil`, `unscented body oil`, `crepey body`, `crepey arms`, `crepey legs`, `body lotion aging`, `amlactin crepe` |

### TIER 2 — Strong supplementary sources (mine selectively; filter for age/body)

| # | Community / URL | Relevance rationale | Recurring relevant topics | Activity / quality (observed) | Noise risks | Recommended search terms |
|---|---|---|---|---|---|---|
| 5 | **r/Perimenopause** — https://www.reddit.com/r/Perimenopause/ | Contextual: transition-stage skin change ("normal to crepey", "what are we doing about body skin") | Crepey onset; dry/itchy skin; which body lotion; puffy fingers/dry skin | Feed: 24 of 25 within 2 days. `crepey OR crepe`: 3/23 topic; `dry skin arms legs`: 5/25 topic, 1/25 body-area; `"body oil"`: 5 results (1 relevant) | Medical/HRT-dominated; skews late 30s–40s; low body-skin density | `crepey`, `body skin`, `dry skin`, `itchy skin`, `body lotion` |
| 6 | **r/SkincareAddicts** — https://www.reddit.com/r/SkincareAddicts/ | High-volume general skincare; many direct crepey-body product requests | "body lotions that are good for crepey skin"; "crepe on my legs arms and neck"; body oil on damp skin; Bio-Oil experiences; product dupes | Feed: 25 of 25 within 2 days. `"body oil"`: 25/25 topic+body. `crepey OR crepe`: 23/25 topic, 10/25 body-area | Ages mixed/young; self-promotion ("free product for reviews", "how much would you pay"); duplicate cross-posts | `crepey body`, `crepey legs`, `crepey arms`, `body oil`, `damp skin`, `dry body skin` |
| 7 | **r/Skincare_Addiction** — https://www.reddit.com/r/Skincare_Addiction/ | Parallel general skincare sub; body-oil and crepey threads | "Crepey Arms"; "Body Oil vs Moisturizer vs Both for Dry Skin?"; body oil vs lotion order; "Creppy skin at 43" | Feed: 23 of 25 within 2 days. `"body oil"`: 21/25 topic+body. `crepey OR crepe`: 21/25 topic, 5/25 body-area | Many young posters ("crepey at 21/28/33"); face/eye heavy | `crepey arms`, `body oil vs lotion`, `dry skin body`, `body oil` |
| 8 | **r/beauty** — https://www.reddit.com/r/beauty/ | General beauty with real mature-body questions and body-oil discovery talk | "What Body Wash for Crepey Body Skin?"; "Crepey skin and bat wings"; "Turning 50 + overwhelmed by body wash/oil options (Osea vs Saltair vs Iota…)"; "Texture on legs"; post-shower body oil; whole-body application | Feed not fetched. `"body oil"`: 23/25 topic+body (15 from 2026). `crepey OR crepe`: 12/25 topic, 6/25 body-area | Scent/glow/shimmer focus; young skew; brand-hype | `crepey`, `body oil`, `after shower body oil`, `bat wings`, `legs texture`, `turning 50 body` |
| 9 | **r/AskWomenOver40** — https://www.reddit.com/r/AskWomenOver40/ | Age-gated, conversational women 40+; lifestyle framing of skin change | "Best Solution for 'Crepey' Skin?"; "Body butter and shower things?"; itch in peri | Feed: 20 of 25 within 7 days (8 within 2 days). Searches return few results: `crepey OR crepe` 3 results (2 topic), `body lotion OR body oil` 7 (1 topic), `skin arms legs aging` 6 (0) | Low skin-thread density; broad life topics | `crepey`, `skin`, `body lotion`, `dry skin`, `aging body` |
| 10 | **r/Sephora** — https://www.reddit.com/r/Sephora/ and **r/Ulta** — https://www.reddit.com/r/Ulta/ | U.S. retailer communities; body-oil purchase decisions, brand comparisons (competitive context: Osea, Saltair, Sol de Janeiro, Moroccanoil) | Body oil recs/"first body oil"; dupes & sale timing; "My New Fave for Crepey Skin!" (Ulta); "Stretchey/Crepey Reccomendations?" (Sephora) | Feeds not fetched. Combined `crepey OR "body oil"`: Sephora 22/25 topic (9 from 2026); Ulta 24/25 topic (14 from 2026). Mostly body-oil, few crepey | Haul/points/sale talk, scent-led, younger; purchase-driven not problem-driven | `body oil`, `crepey`, `firming`, `body oil dry skin`, `Osea`/`Saltair`/`Sol de Janeiro` (competitor context) |

### TIER 3 — Low-yield / niche / context-only (spot-check, do not mine broadly)

| Community / URL | Observed result | Notes / noise risk | Search terms if used |
|---|---|---|---|
| r/AskWomenOver30 — https://www.reddit.com/r/AskWomenOver30/ | `crepey OR crepe`: 11 results, 3 topic ("How old were you when crepey skin started creepin in?", wrinkly hands) | Younger skew; occasional age-onset questions | `crepey`, `hands` |
| r/SkincareAddictionUK — https://www.reddit.com/r/SkincareAddictionUK/ | `crepey OR crepe` 7/20 topic; `"body oil"` 9/20 topic+body | **Non-U.S.** (UK products/spelling) — use only for language patterns, exclude from U.S. corpus | `body oil`, `crepey` |
| r/AsianBeauty — https://www.reddit.com/r/AsianBeauty/ | `"body oil"` 11/25 topic (mostly 2015–2019); `crepey` 0/8 | Dated, K-beauty product focus, global audience | `body oil` |
| r/fragrance — https://www.reddit.com/r/fragrance/ | `"body oil"` 25/25 hits, all about scent/perfume body oils | Scent-layering, not skin condition — relevant only to fragrance expectations of a body oil | `body oil` + `dry skin` |
| r/eczema — https://www.reddit.com/r/eczema/ | `"body oil"` 8/25 topic | Medical dermatitis; claims-risk context; not the target condition | `body oil` |
| r/loseit — https://www.reddit.com/r/loseit/ ; r/xxfitness — https://www.reddit.com/r/xxfitness/ | loseit: 14/25 topic, almost all "loose skin" after weight loss; xxfitness: 9/25, loose skin (2015–2023), incl. "Loose arm skin – is it an age thing or a weight loss thing?" | Weight-loss loose skin ≠ crepey-looking texture; male posters in loseit; adjacent at best (also GLP-1 skin talk) | `loose arm skin`, `crepey` |
| r/AskOldPeople — https://www.reddit.com/r/AskOldPeople/ | `crepey OR crepe skin`: 3/25 topic (hand lotion, anti-aging routine payoff) | Mixed-gender 60+; sparse | `hand lotion`, `skin` |
| r/AskDocs — https://www.reddit.com/r/AskDocs/ ; r/Dermatology — https://www.reddit.com/r/Dermatology/ | AskDocs: 3/13 topic ("Sudden dry and crepey skin"); Dermatology: 1 result (2019) | Medical symptom posts; claims-sensitive | `crepey skin` |
| r/MakeupAddiction — https://www.reddit.com/r/MakeupAddiction/ | `crepey skin body`: 5/25 topic, eyelid/concealer only | Makeup; not body | — |
| r/tretinoin — https://www.reddit.com/r/tretinoin/ | `body crepey OR arms OR legs`: 2/25 topic | Body-tret threads rare | `body tret`, `arms` |
| r/drugstoreMUA — https://www.reddit.com/r/drugstoreMUA/ | `"body oil"` 1/7; `crepey` 2/6 (eye) | Makeup | — |
| r/TwoXChromosomes — https://www.reddit.com/r/TwoXChromosomes/ | `crepey OR crepe skin`: 1/25 topic; one manually notable: "So tired of women's insecurities being SOLD to us (A tale of Crêpe Erase)" (2021) | Mostly unrelated; occasional skepticism toward crepe-marketing (useful objection context) | `Crepe Erase`, `crepey` |
| r/BeautyGuruChatter — https://www.reddit.com/r/BeautyGuruChatter/ | `crepey OR "crepe erase"`: 2 results, 0 relevant | Influencer drama | — |
| r/GenX — https://www.reddit.com/r/GenX/ | `crepey OR crepe skin`: 0/25 relevant | Age-appropriate but no skin discussion surfaced | — |

### Checked and NOT usable

| Community | Observed status |
|---|---|
| r/AgingGracefully | Feed returned only 1 entry (dated 2025-01-18); all 3 searches returned 0 results — appears inactive/near-empty |
| r/over40 | Feed: 0 of 25 posts within 7 days (latest 2026-07-03); both searches 0 results; mixed-gender social/dating content |
| r/AntiAging | Feed: newest post "r/AntiAging is available for adoption" (2026-10-02); other entries from 2017; searches ~0 relevant — abandoned/spam |
| r/over50 | Feed HTTP 403 (private/restricted) — not accessible |
| r/BodyCare | Feed HTTP 404 (label "r/bodycare") — banned or nonexistent; not accessible |
| r/KeratosisPilaris | `"body oil"` search: 0 results (existence not confirmed) |
| r/Skincare_Addiction vs r/SkincareAddicts vs r/SkincareAddiction | All three exist and are active (separate communities); watch for cross-posts (e.g. "Help! Is this crepey under eye skin or something else?" appears in both SCA and SkincareAddicts; "What the crepe?" in r/40PlusSkinCare and r/SkincareAddictionUK) |

---

## 3. Off-Reddit discussion spaces (English, U.S.-relevant) — accessibility from this environment

| Platform | Example URL found | Relevance | Accessibility here | Notes |
|---|---|---|---|---|
| **Inspire.com — Menopause groups** (National Menopause Foundation; Red Hot Mamas Menopause) | https://www.inspire.com/groups/national-menopause-foundation/discussion/6276f1-anyone-else-have-itchy-flaky-skin-in-menopause/ ; https://www.inspire.com/groups/red-hot-mamas-menopause/discussion/skin-sagging-more-than-just-age-no-weight-gain-or-loss/ ; https://www.inspire.com/groups/red-hot-mamas-menopause/discussion/itchy-all-over-1/ | U.S. health-community; older women; menopause skin context (itchy/flaky, sagging) | **curl with browser UA: HTTP 200** (WebFetch: 403) | **Tier 2 off-Reddit** — usable for context; medical-leaning |
| **Mumsnet — Style & Beauty** | https://www.mumsnet.com/talk/style_and_beauty/5326348-crepey-skin-body ; …/5381176-menopausal-skin-crepey-arms-and-knees ; …/2360865-right-weve-done-facial-skincare-but-what-about-the-crepey-skin-on-my-body ; …/5336412-best-low-cost-body-lotion-butter-oil | Rich, on-topic mature-women body-crepey + body-oil threads | **WebFetch: accessible** (curl: 403) — WebFetch confirmed "Crepey Skin (Body)", created 2025-05-01, 12 replies | **UK, non-U.S.** — exclude from U.S. corpus; at most language-pattern reference |
| AgingCare.com Q&A | https://www.agingcare.com/questions/whats-the-best-moisturizer-for-dry-itchy-skin-all-over-491818.htm | Dry/thin aging skin | curl homepage HTTP 200 | Caregivers writing about elderly parents (80+) — wrong persona; Tier 3 |
| Sephora Beauty Insider Community | https://community.sephora.com/t5/Age-Defiers/Crepey-skin-solution/m-p/5821722 (search index) | Formerly had "Age-Defiers" crepey threads | **Not usable** — thread URL now 301-redirects to sephora.com/shop/anti-aging-skin-care (community appears discontinued); curl 403 | — |
| SkinCareTalk.com forum | https://skincaretalk.com/showthread.php/19069-crepey-looking-arms | On-topic ("crepey looking arms", poster ~69) | **Not accessible** — curl 202 stub; WebFetch redirects to tollbit paywall | — |
| PurseForum (PurseBlog) beauty threads | https://m.purseblog.com/threads/body-lotion-thats-good-for-your-skin.65047/ | Body-lotion threads, no crepey-specific thread found | **403** (curl + WebFetch) | — |
| Ask MetaFilter | https://ask.metafilter.com/321730/My-neck-My-hands-Help-this-skincare-dummy-please | One 2018 thread (late-40s, crepey neck/hands) | **403** | — |
| Mayo Clinic Connect | https://connect.mayoclinic.org/discussion/menopause-and-dry-skin/ | Menopause dry skin | **403** | — |
| Quora | — | — | **403** | — |
| Facebook groups, TikTok/YouTube comments, Amazon/retailer reviews | — | Likely high-volume for this persona | Not tested / login-walled; reviews are a separate VOC source type, not communities | Flag for later prompts if review mining is in scope |

---

## 4. Handoff notes for VOC Prompt 2

1. **Corpus priority:** r/40PlusSkinCare → r/30PlusSkinCare → r/Menopause (context) → r/SkincareAddiction → r/SkincareAddicts / r/Skincare_Addiction / r/beauty → r/Perimenopause, r/AskWomenOver40 → r/Sephora/r/Ulta (body-oil purchase language) → Inspire menopause groups (off-Reddit context).
2. **Filter rules to apply when building the corpus:** keep threads where the *body* (arms, legs, knees, hands, chest/décolleté, "all over") is the subject; drop eye/eyelid/face-only "crepey" threads; drop weight-loss "loose skin" unless texture/crepiness is described; tag poster age when stated; treat menopause threads as contextual, not as default persona; exclude UK communities from U.S. corpus.
3. **Best-yield query families (observed):** `crepey legs|arms|knees|hands`, `body oil` (+ `vs lotion`, `damp skin`, `after shower`, `dry skin`), `body care routine` / `anti aging body`, `dry skin legs`, `lizard skin`, `crepe corrector`, `amlactin`.
4. **High-signal seed threads (discovery only, not yet read):**
   - r/40PlusSkinCare — "How are you keeping crepey legs at bay?" (2026-05-13) https://www.reddit.com/r/40PlusSkinCare/comments/1tcgl5d/how_are_you_keeping_crepey_legs_at_bay/
   - r/40PlusSkinCare — "Slowing down the inevitable crepey/saggy skin above the knees?" (2026-08-07) https://www.reddit.com/r/40PlusSkinCare/comments/1vhn81h/slowing_down_the_inevitable_crepeysaggy_skin/
   - r/40PlusSkinCare — "What’s the ultimate anti aging body care routine? I’ll go first" (2026-09-21) https://www.reddit.com/r/40PlusSkinCare/comments/1wm2fzu/whats_the_ultimate_anti_aging_body_care_routine/
   - r/40PlusSkinCare — "The best body lotion in my 40 years" (2026-05-21) https://www.reddit.com/r/40PlusSkinCare/comments/1tj4xhm/the_best_body_lotion_in_my_40_years/
   - r/40PlusSkinCare — "My body exfoliating routine gives me soft skin except my lower legs where it always feels scaly and gross…" (2025-10-20) https://www.reddit.com/r/40PlusSkinCare/comments/1oblvzz/my_body_exfoliating_routine_gives_me_soft_skin/
   - r/40PlusSkinCare — "Gold Bond Crepe Corrector causes itchy rash" (2026-06-30) https://www.reddit.com/r/40PlusSkinCare/comments/1ujsino/gold_bond_crepe_corrector_causes_itchy_rash/
   - r/30PlusSkinCare — "Body lotion and body oil? How important is it after 50?" (2026-07-17) https://www.reddit.com/r/30PlusSkinCare/comments/1uz95uc/body_lotion_and_body_oil_how_important_is_it/
   - r/30PlusSkinCare — "Does anyone use body oil instead of lotion? What brand is good?" (2025-11-17) https://www.reddit.com/r/30PlusSkinCare/comments/1oz5er4/does_anyone_use_body_oil_instead_of_lotion_what/
   - r/30PlusSkinCare — "Over 40s gang who neglected the skin on your bodies. What are you doing for it now that works?" (2021-07-29) https://www.reddit.com/r/30PlusSkinCare/comments/otvj5z/over_40s_gang_who_neglected_the_skin_on_your/
   - r/30PlusSkinCare — "What are we doing for body anti-aging?" https://www.reddit.com/r/30PlusSkinCare/comments/1buobyb/what_are_we_doing_for_body_antiaging/
   - r/30PlusSkinCare — "Crepe paper hands" (2026-05-30) https://www.reddit.com/r/30PlusSkinCare/comments/1trzqv3/crepe_paper_hands/
   - r/30PlusSkinCare — "Aging skin body lotion recommendations?" (2024-03-24) https://www.reddit.com/r/30PlusSkinCare/comments/1bmqref/aging_skin_body_lotion_recommendations/
   - r/Menopause — "My hands and arms have suddenly become crepey" (2024-09-09) https://www.reddit.com/r/Menopause/comments/1fd0h17/my_hands_and_arms_have_suddenly_become_crepey/
   - r/Menopause — "What happened to my arms?" (2025-01-07) https://www.reddit.com/r/Menopause/comments/1hvpiqd/what_happened_to_my_arms/
   - r/Menopause — "Super dry skin on legs" (2025-04-28) https://www.reddit.com/r/Menopause/comments/1ka0x6t/super_dry_skin_on_legs/
   - r/Menopause — "Lizard skin!!" (2024-05-28) https://www.reddit.com/r/Menopause/comments/1d2qhua/lizard_skin/
   - r/Menopause — "How to minimize crepey skin on legs and arms" (2017-07-23) https://www.reddit.com/r/Menopause/comments/6oz326/how_to_minimize_crepey_skin_on_legs_and_arms/
   - r/Perimenopause — "So what are we doing about body skin?" (2025-07-10) https://www.reddit.com/r/Perimenopause/comments/1lwdvsg/so_what_are_we_doing_about_body_skin/
   - r/Perimenopause — "Anyone else’s skin change from normal to “crepey”?" (2025-04-05) https://www.reddit.com/r/Perimenopause/comments/1jsf80m/anyone_elses_skin_change_from_normal_to_crepey/
   - r/SkincareAddiction — "[Skin Concern] What can I do about all over body crepey skin?" (2022-05-13) https://www.reddit.com/r/SkincareAddiction/comments/uoxoh4/skin_concern_what_can_i_do_about_all_over_body/
   - r/SkincareAddiction — "[Product Request] Need products for old lady crepey wrinkly skin" (2023-06-18) https://www.reddit.com/r/SkincareAddiction/comments/14cn06o/product_request_need_products_for_old_lady_crepey/
   - r/SkincareAddiction — "[product request] What’s a good body oil for dry skin?" (2025-07-08) https://www.reddit.com/r/SkincareAddiction/comments/1luqdnp/product_request_whats_a_good_body_oil_for_dry_skin/
   - r/SkincareAddicts — "I’m looking for products to help me with my crepe on my legs arms and neck that won’t cost a fortune. Can anyone help?" (2025-05-07) https://www.reddit.com/r/SkincareAddicts/comments/1kh2zca/im_looking_for_products_to_help_me_with_my_crepe/
   - r/SkincareAddicts — "Body oil works so much better on damp skin instead of fully dry skin" (2026-05-06) https://www.reddit.com/r/SkincareAddicts/comments/1t5c6ay/body_oil_works_so_much_better_on_damp_skin/
   - r/Skincare_Addiction — "Crepey Arms" (2023-09-03) https://www.reddit.com/r/Skincare_Addiction/comments/168y5o7/crepey_arms/
   - r/beauty — "What Body Wash for Crepey Body Skin?" (2025-02-09) https://www.reddit.com/r/beauty/comments/1ili5sj/what_body_wash_for_crepey_body_skin/
   - r/beauty — "Crepey skin and bat wings" (2024-04-24) https://www.reddit.com/r/beauty/comments/1cbkivk/crepey_skin_and_bat_wings/
   - r/beauty — "Help! Turning 50 + overwhelmed by body wash/oil options (Osea vs Saltair vs Iota vs Beauty From Bees vs Besque)" (2026-01-17) https://www.reddit.com/r/beauty/comments/1qfgegt/help_turning_50_overwhelmed_by_body_washoil/
   - r/AskWomenOver40 — "Best Solution for "Crepey" Skin?" (2024-06-21) https://www.reddit.com/r/AskWomenOver40/comments/1dla039/best_solution_for_crepey_skin/
   - r/TwoXChromosomes — "So tired of women's insecurities being SOLD to us (A tale of Crêpe Erase)" (2021-03-14) https://www.reddit.com/r/TwoXChromosomes/comments/m540tj/so_tired_of_womens_insecurities_being_sold_to_us/ (objection/skepticism context)
5. **Limitations:** title-only screening; Reddit relevance search caps at 25 results/query, so counts are per-query samples, not community totals; heavy 429 rate limiting meant feeds were fetched only for core candidates; member counts unavailable; poster ages/locations not yet verified (U.S. residency cannot be confirmed from Reddit titles).
