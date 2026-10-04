# VOC3 Batch C – Notes (Corpus C061–C090)

## Scope & method
- Threads processed: **30 / 30** (C061–C088 Reddit Atom caches, C089–C090 Inspire HTML). Mapping per `VOC2_URL_Corpus.md` §8. No web fetches; only the corpus CSV, §8 mapping and `thread_cache/` were used.
- Each cache file was parsed with Python (Atom entries → author, `<link href>`, HTML-unescaped and tag-stripped content; Inspire → HTML with scripts/styles stripped). The full OP and every cached comment were then read manually and VOC items extracted.
- Source URL = comment permalink from the Atom `<link href>` whenever the quote comes from a comment (545 rows). For OP quotes and for both Inspire threads (they have no per-reply permalinks), Source URL = thread URL. For Inspire rows the poster's username is given in Context.
- Quotes: the build script matched each quote (fragments split at "…") against the normalised entry text (HTML-unescaped, curly quotes and dashes mapped, whitespace collapsed, lowercased). It then **wrote out the original source substring**, so typos, curly apostrophes and casing are kept exactly as posted. A second, independent script checked every fragment against the normalised raw cache file.
- Paraphrases are in German. Implications are research implications only (no ad copy).

## Output
- `batch_C.csv`: **672 rows** (C0001–C0672), 15 columns in the order the spec requires.
- Verification: 672/672 quotes verified, **0 failed**. 0 quotes over 40 words.
- Dropped/unverifiable quotes: **0 failed verification**. One drafted row was removed before the build because it quoted a bot (VettedBot product-summary bot in C067).
- AutoModerator, mod-team and TeamInspire staff posts were skipped. Deleted comments were ignored.

## Rows per category
| Category | Rows |
|---|---|
| Purchase criteria | 71 |
| Successful attempts | 70 |
| Product / routine preferences | 61 |
| Objections | 51 |
| Exact phrases / metaphors / repeated wording | 49 |
| Emotional reactions | 45 |
| Ingredient / mechanism beliefs | 44 |
| Skepticism | 38 |
| Failed attempts | 37 |
| Routine friction | 37 |
| Problem descriptions | 33 |
| Questions customers repeatedly ask | 28 |
| Identity / social implications | 25 |
| Tactile descriptions | 25 |
| Symptoms / visible texture descriptions | 24 |
| Situational triggers | 12 |
| Time-to-result expectations | 12 |
| Desired outcomes | 10 |

Rows per thread: C072 45 · C081 39 · C074 34 · C061 33 · C065 32 · C062 31 · C077 31 · C070 30 · C064 26 · C063 25 · C087 25 · C073 24 · C085 24 · C069 23 · C079 22 · C084 22 · C078 20 · C080 20 · C075 18 · C089 18 · C071 16 · C083 16 · C067 15 · C086 14 · C076 13 · C090 13 · C066 12 · C068 12 · C082 10 · C088 9.

Evidence strength: high 262 · medium 367 · low 43. Rows with a stated age: 73 (ages in this batch range from 41 to 74).
Body area: whole_body 402 · unspecified 93 · arms 83 · legs 52 · hands 19 · neck 10 · chest 8 · knees 3 · face_transfer 2.

## Flags
- `hrt_medical_context` 60 rows, concentrated in C066, C068, C069, C070, C074 and C090. Menopause appears only as context and is not a product claim.
- `non_us_signal` 25 rows (Canadian commenters in C068, C070 and C080; UK in C061; Australia in C072; Europe/Germany in C078 and C081).
- `face_only_transferable` 15 rows (mostly C061, a face/neck-dominant thread).
- `under_40_signal` 6 rows (C078 general SCA; C088 OP mid-20s; C074 "bog witch" commenter).
- `possible_seeding` 4 rows, all low weight:
  - C063 #37 links the commenter's own YouTube routine.
  - C072 #79 is a short brand-named "Whish Body $22" testimonial.
  - C072 #97 is a self-declared soap seller.
  - C061 #86 promotes a Beauty-Heroes retailer.
  - No coordinated seeding was seen in C083, the brand-list OP.

## Recurring patterns (with basis: rows / threads)
- **Lotion works only briefly, or stops working in this life stage** (`lotion_temporary`, 29 rows / 19 threads). Examples:
  - "doesn't even come close to an hour before I have to put more on" (C069)
  - "Osea smells nice but does not last … by mid-afternoon I need to put lotion on my legs" (C083)
  - "temporarily makes the skin look better" (C079)
- **Sudden onset, the "overnight" story** (`sudden_onset`, 44 / 14). Examples:
  - "aged 10 years in 10 months" (C074)
  - "didn't look like that yesterday" (C073)
  - "turning into a mummy in realtime" (C069)
  - "aged overnight" (C063, C070, C075, C076)
  - "almost overnight" (C090)
- **Oil on damp skin is common practical knowledge** (`oil_on_damp_skin`, 39 / 17). Applied in or straight out of the shower, "before toweling off". The same threads raise practical objections:
  - slippery shower or tub (`new_slippery_shower`, 4 threads: C062, C067, C068, C089)
  - packaging that is hard to use with oily hands (C081)
- **Absorption and greasiness decide whether oil gets used** (`oil_absorbs_fast` 37 / 16; `oil_greasy_staining` 22 / 12).
  - The OP of C071 states the core dilemma: "Using body oil and lotion leaves it too greasy. Just lotion still seems to be not enough."
  - Repeated objections are stickiness (Gold Bond Crepe "sticky ALL FREAKING DAY", C073), staining bed linen or clothes (C067, C081), and waiting time before dressing or going to bed (C067, C073, C081).
- **Confusion about oil vs. lotion and the order of application** (`oil_vs_lotion_confusion` 23 / 14; `question_order_of_application` 14 / 7; `oil_seals_not_hydrates` 16 / 10).
  - Many posters believe oil "doesn't actually hydrate" and only seals (C081, C064, C065).
  - Posters contradict each other on whether oil goes first or last. In C087, Saltair's own instructions are seen as inconsistent.
  - "And do I still need to use lotion?" (C087 OP) recurs as a question.
- **Scent splits the audience** (`fragrance_sensitivity` 39 / 15 vs. `scent_love` 26 / 10).
  - Some posters newly cannot tolerate scent in perimenopause ("smell of scented lotions have started making me upset", C075; headaches, C084).
  - Others love scent strongly: "grandma smell" is an exclusion (C077), and a C087 poster puts up with dermatitis to keep using a favourite scent.
  - The AmLactin smell is a recurring objection (C072, C077, C078, C086).
- **Price and value scrutiny, plus distrust of marketing** (`price_value` 49 / 16; `marketing_distrust` 34 / 15).
  - Cheap oils are named as the baseline (`cheap_oil_alternative` 23 / 16): baby oil, coconut, jojoba, sunflower, almond, tallow.
  - "Any other products are just a very expensive variation" (C064).
  - The AmLactin "Crepe Firming" product has an identical INCI to the cheaper version: "$12 extra just for the word 'firming'" (C080).
  - C088 sees "crepey" as a buzzword invented by marketing.
  - C083 (OP 50): "bombarded with ads … don't want to waste my money on hype".
- **Routine fatigue and inconsistency** (`routine_fatigue` 27 / 11; `consistency_effort` 25 / 15). Examples:
  - "This is tiring and I don't want to do it! But, I can't not do it either" (C062)
  - "consistency of application which I suck at" (C064)
  - "Bought it. Now I just have to remember to use it!" (C079, OP 74)
  - Workarounds: lotion kept on the couch or in several rooms (C064, C067, C072, C078).
- **Arms and legs are the main body zones** (`crepey_arms` 35 / 16; `crepey_legs` 21 / 13), with shins especially. Hands, neck/chest and knees are secondary.
- **Identity language.** "Old lady" / "grandma" / "70 year old" wording appears in 16 rows across 9 threads. Reptile, lizard and snake metaphors appear in 7 threads ("lizard skin", "look human again", "snake ready to shed"). Mirror shock and avoidance appear in C061, C070, C074 and C090.
  - The common desired outcome is modest: "slow it down", "not look older than I am" (C061, C074, C079).
- **Competitors seen in this batch:**
  - AmLactin: 18 rows / 8 threads.
  - Gold Bond Crepe / Retinol: 10 rows / 7 threads.
  - Neutrogena Body (Sesame) Oil: C062, C065, C071, C079, C081, C089.
  - Osea / Saltair (mixed views on durability, tackiness and price): C083, C085, C087.
  - CeraVe cream as the cheap "it was on my counter the whole time" success (C086).

## Observations (not synthesis)
- Several posters say face skincare habits are not carried over to the body ("strict skin regimen on face … not so much the rest of the body", C072; `new_body_neglect` 8 rows).
- Damp-skin application plus a light, fast-absorbing feel is the most consistent positive cluster. Greasiness, stickiness, staining and slippery showers are the most consistent negative cluster.
- In menopause threads, HRT talk dominates. Results described for HRT are mixed, and some posters distrust "miracle" posts (C070 #68 suspects "big pharma" is behind the HRT success stories).
