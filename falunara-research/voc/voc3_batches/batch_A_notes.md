# Batch A — VOC Prompt 3 extraction notes (C001–C030)

Spec: `voc/VOC3_extraction_spec.md`. Source: cached Atom files in `voc/thread_cache/` per §8 of `VOC2_URL_Corpus.md`. Nothing fetched from the internet. No other research folders read.

## Summary

- Threads processed: 30 (C001–C030), all 30 cached files parsed, OP + every cached comment read in full.
- Total rows: **850** (VOC IDs A0001–A0850).
- Evidence strength: medium 631, high 176, low 43
- Quote verification: two scripted passes. (1) The build script checks each quote fragment, after HTML-unescaping, whitespace and quote-mark normalisation, against the specific Atom entry it is attributed to. (2) A separate `verify.py` re-checks the final CSV against the entry behind each Source URL. Final result: 850/850 verified, 0 failures.
- Quotes that failed the first check: 7. Six were fixed so that they are now verbatim: one was attributed to the wrong comment and got the correct permalink; two needed the poster's original typos restored ("kayo g", "robe of money"); one needed "forget to did it" restored; two needed a "…" omission marker where text had been skipped. **One was dropped**: in C008 the OP's text exists only in the thread title, not in the entry content.
- Typographic apostrophes and quote marks were restored from the source, so each quote matches the original characters.
- AutoModerator entries and [deleted]/[removed] entries were skipped. No quotes were taken from them.

## Rows per category

| Category | Rows |
|---|---|
| Problem descriptions | 10 |
| Symptoms / visible texture descriptions | 32 |
| Tactile descriptions | 39 |
| Emotional reactions | 45 |
| Situational triggers | 30 |
| Desired outcomes | 18 |
| Failed attempts | 31 |
| Successful attempts | 72 |
| Product / routine preferences | 96 |
| Objections | 57 |
| Skepticism | 59 |
| Purchase criteria | 78 |
| Ingredient / mechanism beliefs | 79 |
| Time-to-result expectations | 34 |
| Routine friction | 33 |
| Identity / social implications | 52 |
| Exact phrases / metaphors / repeated wording | 51 |
| Questions customers repeatedly ask | 34 |

## Rows per thread

| Corpus ID | Community | Rows | Note |
|---|---|---|---|
| C001 | r/40PlusSkinCare | 41 |  |
| C002 | r/40PlusSkinCare | 50 |  |
| C003 | r/40PlusSkinCare | 49 |  |
| C004 | r/40PlusSkinCare | 44 | mostly cellulite/acceptance discussion; only body-skin-texture items extracted |
| C005 | r/40PlusSkinCare | 37 |  |
| C006 | r/40PlusSkinCare | 20 | hands; HRT context |
| C007 | r/40PlusSkinCare | 31 |  |
| C008 | r/40PlusSkinCare | 19 | 1 quote dropped (title-only) |
| C009 | r/40PlusSkinCare | 29 |  |
| C010 | r/40PlusSkinCare | 25 |  |
| C011 | r/40PlusSkinCare | 21 |  |
| C012 | r/40PlusSkinCare | 15 |  |
| C013 | r/40PlusSkinCare | 15 |  |
| C014 | r/40PlusSkinCare | 13 |  |
| C015 | r/40PlusSkinCare | 24 | mostly facial oil context → face_only_transferable flags where face |
| C016 | r/40PlusSkinCare | 25 | neck (body-adjacent); before/after angle skepticism |
| C017 | r/40PlusSkinCare | 13 |  |
| C018 | r/40PlusSkinCare | 24 |  |
| C019 | r/40PlusSkinCare | 11 | thin; some lip/hand side-talk, Canada/UK signals |
| C020 | r/40PlusSkinCare | 13 | thin; neck reactions |
| C021 | r/40PlusSkinCare | 26 | neck; GLP-1 confounder |
| C022 | r/40PlusSkinCare | 31 | neck; AmLactin over-use cautions |
| C023 | r/45PlusSkincare | 36 | core body-oil thread (highest oil relevance) |
| C024 | r/45PlusSkincare | 36 |  |
| C025 | r/45PlusSkincare | 36 |  |
| C026 | r/45PlusSkincare | 31 | adverse-reaction thread (Gold Bond Crepe Corrector) |
| C027 | r/45PlusSkincare | 31 |  |
| C028 | r/45PlusSkincare | 31 |  |
| C029 | r/45PlusSkincare | 33 |  |
| C030 | r/45PlusSkincare | 40 |  |

## Seeding / commercial flags (`possible_seeding`): 12 rows

- A0240 (C006): an Adipeau 'comment' that reads as copied product marketing.
- A0380, A0381 (C012): a link to a 'best body care products' list, and the account 'anglopeptides' pushing peptides.
- A0405 (C014): a commenter recommending a friend's organic oil company with a link.
- A0414, A0415 (C015): two accounts praising CircCell in matching wording.
- A0564 (C022): the account 'RESET_skin_protocol' giving ingredient-protocol advice.
- A0638 (C024): an Oliveda collagen push ('DM me when back in stock'), MLM-style.
- A0642 (C024) and A0683 (C025): the same account, 'Beautythusiast', promotes Esker products in two threads.
- A0682 (C025): a small-brand shop link (white label body care). A0684 (C025): the account 'cleanbeautybytina', whose name reads like an influencer's.
- Not flagged as seeding, but kept as skepticism data: C002 'Did Amlactin hire a social media team?', C027 'covert marketing tactics', and C016/C022 doubts about before/after photo angles. The C031 OP flag from VOC2 falls outside this batch.

## Other flags

- hrt_medical_context: 21, non_us_signal: 13, possible_seeding: 12, face_only_transferable: 8, under_40_signal: 4
- Ages stated on 184 rows, ranging from 19 to 73. Most fall between 40 and 65. Under-40 posters (19, 34–36, 'early 20s') are flagged `under_40_signal`.
- Neck rows (76) are body-adjacent and come mainly from C016, C020, C021 and C022. They are kept but tagged `neck`. Hands account for 56 rows.

## Recurring patterns observed (rows / threads), with basis — observations only, no synthesis

1. **AmLactin as the community's default benchmark.** Tagged `amlactin_lactic` in 89 rows across 20 of 30 threads. The praise is extreme ('preserving myself', 'miracle', 'game changer'). Its **smell** is the most frequent objection: `fragrance_sensitivity` appears in 35 rows across 18 threads, with metaphors such as 'pee', 'cat pee', 'burnt/spoiled maple syrup', 'sour milk' and 'manure'. Sting, rash, hives and sun sensitivity are the next most common objections (C009, C016, C020, C022, C030).
2. **Gold Bond Crepe Corrector is polarising.** Tagged in 46 rows across 12 threads. Some posters report results within days ('in 4 days, it was GONE'). Others report no effect ('did jack squat for my knees'), a filmy feel, or rashes and hives after what they believe was a reformulation (C020 and C026, with Target/Amazon/Walmart batch suspicion). One poster dislikes the name 'Crepe Corrector' itself (C004).
3. **Oils are present but ambivalent.** 131 rows across 27 threads carry an oil-related tag. The positive side: oil 'locks in' or seals moisture (`oil_seals_not_hydrates`, 22 rows/12 threads), and damp-skin application is near-consensus (`oil_on_damp_skin`, 31 rows/13 threads). Several posters switched from lotion to oil ('much more absorbent', 'never need to reapply'). The negative side: oil feels too greasy on its own, takes too long to absorb before dressing (C011, and C023's bathrobe workaround), stains clothing (C004), or 'doesn't treat the issue' and only seals (C029). Users often mix oil with lotion or toner (C018, C023, C027).
4. **Absorption and stickiness are the main purchase criteria.** `oil_absorbs_fast` appears in 34 rows across 10 threads and `new_sticky_sheets` in 17 rows across 13 threads. Posters name a dress-quickly window, sticking to sheets, and 'sits on top' or film complaints (C008, C011, C018, C019, C024).
5. **Lotion results are seen as temporary, so consistency matters.** `lotion_temporary` appears in 26 rows/17 threads and `consistency_effort` in 34 rows/18 threads. Examples: 'after an hour or so the crepeiness is back'; 'returns if you stop using. Pick your poison'; 'fallen off the wagon … more crepiness'.
6. **Time-to-result anchors:** 'next day', 'one use', about 1 week, about 2 weeks (mentioned most often), 1 month, 4 months, and 6–12 months for retinoids. Tagged in 36 rows across 18 threads.
7. **Price and value are on everyone's mind.** `price_value` appears in 53 rows across 23 threads. Anchors: AmLactin from Costco at about $12–24, body oil at about $14–20 ('Do not spend more than like $20'), Prequel at about $22. OSEA is called 'so expensive' and 'underwhelming'. Posters also mention earlier wasted spending on prestige products.
8. **Sudden onset and identity loss.** `sudden_onset` appears in 37 rows across 9 threads, with 'aged overnight' and 'woke up' narratives at ages 40–52. `old_lady_identity` appears in 17 rows across 11 threads, with words like 'granny', 'old-people-legs', 'old lady body' and 'turkey neck'. Reptile and texture metaphors include alligator, snake, lizard, dragon scales, crocodile, dinosaur, desert, raisin and furry shins.
9. **Clothing avoidance and summer as a trigger.** `shorts_dresses_avoidance` and `hiding_arms_sleeveless` together cover 20 rows across 11 threads, and `summer_trigger` 18 rows across 12 threads. A counter-voice of acceptance and gratitude is also strong: `acceptance_aging` appears in 25 rows across 9 threads.
10. **Scent as a positive driver.** `scent_love` appears in 28 rows across 15 threads. Posters layer scented lotions or body sprays over actives and use Neutrogena Sesame oil 'as perfume'. Duftfrei (fragrance-free) and allergy needs run in parallel.
11. **Routine overwhelm and fatigue.** `routine_fatigue` appears in 22 rows across 14 threads. Examples: 'We have to put it on our bodies too?!', 'I need a decision tree', 'So many steps and this is just body', and sensory dislike of lotion feel. Questions about application order come up in 21 rows across 13 threads.
12. **Ingredient fears and 'clean'.** `new_ingredient_fear` appears in 17 rows across 11 threads, covering mineral oil, petroleum/EDTA, SLS, propylene glycol and vitamin E allergy, plus distrust of reformulations and counterfeits.
13. **Topical skepticism versus procedures and exercise.** `nothing_works` appears in 37 rows across 14 threads and `only_procedures_work` in 13 rows across 9 threads. A large 'lift weights, no cream will help' faction runs through C002, C003, C010 and C024.
14. **The body as a neglected or secondary zone next to the face.** Posters say 'neglected my skin below the neck' and that their hands look '10 years older than my face'. Facial product cast-offs are reused on the body (C001, C006, C027, C030).

## Caveats
- Context column: English. Paraphrase and research-implication columns: German, per spec.
- Some quotes serve two categories and appear as separate rows, as the spec allows.
- Thread-level counts above come from batch A only and are not a cross-batch synthesis.
- No FALUNARA ingredient claims were made. No ad copy was written.
