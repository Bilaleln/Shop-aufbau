# VOC Prompt 3 — Extraction spec (shared by all extraction batches)

Source of truth: "7. VOC PROMPT 3 — DEEP REDDIT / FORUM VOC RESEARCH" of the FALUNARA Master Prompt List.

## Dependency
Use ONLY the URL corpus produced by VOC Prompt 2: `voc/VOC2_URL_Corpus.csv` (C001–C090) and the cached thread text in `voc/thread_cache/` (mapping in `voc/VOC2_URL_Corpus.md` §8). Do not replace it with a convenience sample. Do not fetch new threads. The 86-item "unverified backlog" is NOT part of the corpus.

## Extraction rule
Read the supplied discussions deeply (OP + every cached comment). Extract customer language faithfully and keep short quotations attached to their source URLs. Do not manufacture quotations.
- Exact short quote: verbatim substring of the cached text (after HTML-unescaping and whitespace normalisation), ideally ≤ 40 words. Never translate, correct spelling, or paraphrase inside the quote. Use "…" only to mark an omission between two verbatim fragments.
- Every quote must be machine-verified against the cached file (script check: normalised quote fragments appear in normalised thread text). Unverifiable quotes are dropped.
- Source URL: the thread URL from the corpus; if the comment permalink is available in the Atom entry `<link href>`, use the comment permalink instead (more precise) and keep the thread URL in a separate column.
- Skip AutoModerator, mod notices, obvious brand/seeded accounts (flag them instead).

## Categories (use exactly these labels)
Problem descriptions · Symptoms / visible texture descriptions · Tactile descriptions · Emotional reactions · Situational triggers · Desired outcomes · Failed attempts · Successful attempts · Product / routine preferences · Objections · Skepticism · Purchase criteria · Ingredient / mechanism beliefs · Time-to-result expectations · Routine friction · Identity / social implications · Exact phrases / metaphors / repeated wording · Questions customers repeatedly ask

One quote may yield more than one row if it genuinely serves two categories (separate rows, same quote).

## Columns (CSV, UTF-8, this exact order)
VOC ID | Category | Exact short quote | Paraphrased meaning | Source URL | Thread URL | Corpus ID | Community | Context | Recurrence/pattern tag | Evidence strength | Potential research implication | Stated age | Body area | Flags

- VOC ID: batch prefix + running number, e.g. `A0001`, `B0001`, `C0001`.
- Paraphrased meaning: short, in GERMAN (for the German-speaking client). Quote stays English.
- Context: 1 short line (English or German) — what the thread/comment is about, e.g. "reply to OP asking about crepey legs; poster 52".
- Recurrence/pattern tag: snake_case tag(s) from the controlled list below; add new tags only if nothing fits, prefixed `new_`.
- Evidence strength: `high` (explicit first-person, specific, body-skin, target age/community), `medium` (first-person but vague, or age/body area unclear), `low` (second-hand, off-target body area, or likely non-US / under-40).
- Potential research implication: research implication only — NO ad copy, no headlines.
- Stated age: number only if the poster states it (else blank). Body area: arms/legs/knees/hands/chest/neck/abdomen/whole_body/face_transfer/unspecified.
- Flags: `non_us_signal`, `under_40_signal`, `possible_seeding`, `hrt_medical_context`, `face_only_transferable` etc.

## Controlled pattern tags (starter list)
crepey_arms, crepey_legs, crepey_knees, crepey_hands, crepey_chest, sudden_onset, mothers_skin, old_lady_identity, hiding_arms_sleeveless, shorts_dresses_avoidance, summer_trigger, winter_dryness, itch_flake, thin_skin_bruising, lotion_temporary, nothing_works, only_procedures_work, acceptance_aging, marketing_distrust, subscription_distrust, price_value, cheap_oil_alternative, oil_greasy_staining, oil_on_damp_skin, oil_absorbs_fast, oil_seals_not_hydrates, oil_vs_lotion_confusion, scent_love, fragrance_sensitivity, amlactin_lactic, urea, retinol_body, gold_bond_crepe, crepe_erase, evora, collagen_supplement, hrt_estrogen_skin, sunscreen_sun_damage, exfoliation_dry_brush, weight_loss_glp1, consistency_effort, routine_fatigue, time_to_result, derm_recommendation, peer_proof, soft_smooth_desire, glow_desire, feel_like_myself, confidence_desire, self_care_ritual, question_what_works, question_oil_or_lotion, question_order_of_application

## Output per batch
`voc/voc3_batches/batch_<X>.csv` + `voc/voc3_batches/batch_<X>_notes.md` (threads processed, rows per category, dropped/unverifiable quotes count, seeding flags, observations of recurring patterns WITH basis — but no final synthesis).
