# VOC Prompt 3 – Batch B notes (corpus C031–C060)

Source: `voc/VOC2_URL_Corpus.csv` + cached Atom files in `voc/thread_cache/` (mapping §8 of `VOC2_URL_Corpus.md`). No new fetching. All 30 threads are Reddit (r/45PlusSkincare C031–C039, r/30PlusSkinCare C040–C055, r/Menopause C056–C060). Every cached entry (OP + all comments, 13–101 per thread) was parsed (author, link href, HTML-unescaped and tag-stripped content) and read in full.

## Output
- `batch_B.csv`: **892 rows** (B0001–B0892), 15 columns in the spec's order. Source URL = comment permalink from the Atom `<link href>` (813 rows). For OP rows it is the thread URL.
- Paraphrases are in German. Quotes are verbatim English. 17 quotes use "…" to join two verbatim fragments.

## Verification
- Script check: each normalised quote, or each "…"-separated fragment in order, must appear (a) in the normalised text of the **specific entry** cited and (b) in an independent normalisation of the raw cached XML (double HTML-unescape, tags stripped, whitespace collapsed).
- Result: 892/892 pass. One quote (C051 #23) first failed the raw check only because of an inline `<em>` tag. The check was fixed to accept tag removal both with and without a space. The quote is verbatim.
- **Dropped: 2 rows** (not verification failures):
  - C031 #83: "House of glows cold then hot gold gel". This is an obvious product plug ("my older sister recommended it"), so it is treated as seeding.
  - C057 #63: VettedBot, an automated bot comment.
- AutoModerator and deleted/[removed] entries were skipped. Quotes run up to 44 words. Only 2 are over 40 (B0611, B0859), and both are kept for context.

## Rows per thread
C031 51 · C032 40 · C033 23 · C034 34 · C035 27 · C036 45 · C037 21 · C038 35 · C039 10 · C040 40 · C041 35 · C042 28 · C043 32 · C044 41 · C045 21 · C046 19 · C047 21 · C048 22 · C049 20 · C050 29 · C051 19 · C052 47 · C053 14 · C054 13 · C055 13 · C056 53 · C057 41 · C058 33 · C059 33 · C060 32

## Rows per category
Product / routine preferences 109 · Successful attempts 92 · Emotional reactions 74 · Purchase criteria 68 · Tactile descriptions 55 · Ingredient / mechanism beliefs 53 · Identity / social implications 52 · Skepticism 52 · Routine friction 49 · Exact phrases / metaphors / repeated wording 45 · Objections 45 · Questions customers repeatedly ask 43 · Failed attempts 41 · Situational triggers 40 · Symptoms / visible texture descriptions 26 · Time-to-result expectations 21 · Desired outcomes 17 · Problem descriptions 10

Evidence strength: high 155 · medium 656 · low 81. Stated age is filled on 181 rows. It is filled only where the poster states a number; approximations like "Gen X", "mid-sixties" and "early 60s" are left blank and mentioned in Context instead. Body area: whole_body 408 · arms 166 · unspecified 128 · hands 79 · legs 63 · neck 16 · chest 16 · abdomen 11 · face_transfer 3 · knees 2.

## Flags
- `hrt_medical_context` 59 rows. The r/Menopause threads are HRT-heavy (estradiol on hands, HRT credited over topicals).
- `non_us_signal` 42 rows: C032 OP (Canada), C038 OP (Canada), C058 poster (France), C057/C059 (NZ, Vancouver), plus UK/Australia posters.
- `under_40_signal` 26 rows. C041, C043, C049 and C042 contain many posters in their 30s.
- `possible_seeding` 20 rows:
  - C031 OP (B0001–B0008): the corpus already flagged this OP as polished, never replying and pushing no product. The rows are kept and flagged.
  - Individual promo-tone or link comments: B0030 Sofwave, B0051 "can't post what really works", B0145 "Certified Clean" brand list, B0234 device link, B0283 Hempz, B0317 YouTuber self-promo, B0388 luxury brand, B0502, B0538, B0545, B0646, B0853 brand-named.
- `possible_male_poster` 3 rows: C047 OP mentions "my wife".
- `face_only_transferable` 3 rows.
- Note: the corpus says the C034 OP is 55, but in the text "55" is stated by a different poster (entry 26), so the OP rows have no age.

## New pattern tags (prefixed `new_`)
new_face_product_transfer (7), new_body_firmness (7), new_hydration_water (7), new_crepey_abdomen (4), new_invisibility (4), new_age_community_alienation (2), new_self_tanner_camouflage, new_oil_hair_growth_worry, new_leathery_skin (1 each).

## Recurring patterns observed (basis = row and thread counts in this batch; not a final synthesis)
1. **Damp/wet-skin oil application is the dominant oil behaviour.** `oil_on_damp_skin`: 63 rows in 21/30 threads. Examples: oil before towelling off, oil kept in the shower, "steamy bathroom" (B0047, B0119, C050/C052/C056).
2. **Confusion about oil vs lotion and layering order.** `question_order_of_application` 25 rows / 15 threads, `oil_seals_not_hydrates` 28 / 15, `oil_vs_lotion_confusion` 21 / 13. Posters directly contradict each other: "lotion first, oil second" vs "body oil and then body butter/lotion" (C051 #23 vs #25). Some say "oils are just occlusives" (C050), others that "some oils … penetrate" (C050 #16).
3. **Greasy, staining and wait-to-dress friction with oils.** `oil_greasy_staining` 36 / 15. Examples: "ruined every fabric", "slick pig", robe for half an hour, "greaseball for half an hour". In-shower application is offered as the fix (C052 #20).
4. **Scent cuts both ways.** `fragrance_sensitivity` 37 / 17 vs `scent_love` 23 / 12. AmLactin odour is a repeated objection ("similar to urine", "maple syrup", "gaggy"; `amlactin_lactic` 40 rows / 16 threads). Some premium oils are also rejected for scent ("floor cleaner"). There is an explicit unmet wish for a fragrance-free oil mist (C056 #74).
5. **Sudden onset ("overnight", "BOOM").** `sudden_onset` 36 / 11, and "overnight" appears in 15 quotes. Ages are mostly 40–65.
6. **Old-lady / mother / grandmother identity.** `old_lady_identity` 26 / 12, `mothers_skin` 18 / 12. Examples: "grandma's arms", "old lady legs", "74 year old mother's crepey arms", "my MIL complaining … Now I know".
7. **Concealing the arms with sleeves.** `hiding_arms_sleeveless` 14 / 7. "sleeve" appears in 18 quotes. Going sleeveless again is used as the success marker (C058 #36).
8. **Category fatigue and the belief that topicals are temporary.** `nothing_works` 51 / 18, `lotion_temporary` 27 / 13. Examples: "Lotions are just bandaids", AmLactin works "for about 30 minutes. Not with the $$", "only short-term hydration". Many name procedures, HRT or weightlifting as the "real" fix.
9. **Price and value sensitivity.** `price_value` 65 / 26, the most widespread tag. Examples: "I don't think I'd spend more than $20-$30 on a body product", Osea "$50-$80", a "$3" Target oil dupe. Cheap kitchen/baby/coconut oil is offered as an alternative (`cheap_oil_alternative` 21 / 12). One belief is that "the secret is the massage, not the oil" (C031 #69).
10. **Transparency distrust.** `marketing_distrust` 34 / 18. Retinol body products are distrusted because they don't state percentages (C046, C054, C059). Other examples: "Nada. It's all marketing", "hype".
11. **Desired outcomes are tactile.** `soft_smooth_desire` 57 / 28. Examples: "soft as a baby's butt", "soft and supple", "plump", "skin like butter". Glow appears less often (15 / 11).
12. **Weight loss and GLP-1 as a trigger** (17 / 11), and **winter/dry-climate triggers** (21 / 14; desert, Colorado, Arizona and Vegas posters).
13. **Time-to-result expectations** cluster at 3–6 months for real change, with immediate or 1–3 week perceived softness (26 rows / 16 threads).
