# Live theme edits: manual (the API is blocked from writing to the live theme)

Where: **Online Store → Themes → "OLEG - Falunara PDP (work copy)" → Customize**. Use the top
dropdown to switch templates (Home page / Products → Default product / Collections). Click the section,
then the block, then edit the text field. Each item lists template → section id → block id → setting,
current text, and new text.

## A. Required: placeholders, guarantee, shipping (product page)
| # | Location | Current | New |
|---|---|---|---|
| A1 | product → main → buy_faq → question_5 | What is the 100% results guarantee? | How does the 30-day money-back guarantee work? |
| A2 | product → main → buy_faq → answer_5 | Details about the guarantee go here. | If you're not satisfied, contact us within 30 days of delivery to request a return and refund. Once your request is approved, we'll send you return instructions. See our <a href="/policies/refund-policy">Refund Policy</a> for details. |
| A3 | product → guarantee → description_text | We're so confident … simply return the item within 30 days for a full refund. | Not satisfied? Contact us within 30 days of delivery to request a return and refund. Return instructions are provided once your request is approved. See our Refund Policy for full details. |
| A4 | product → guarantee → benefit_1 | 100% Satisfaction | 30-Day Money-Back Guarantee |
| A5 | product → guarantee → benefit_2 | Fast Shipping | Shipping Calculated at Checkout |
| A6 | product → guarantee → benefit_3 | Easy Returns | Email Support |
| A7 | product → guarantee → product_name (image alt) | Premium Product | FALUNARA Botanical Body Oil |
| A8 | product → guarantee → button_text | ADD TO CART | ADD TO BAG (optional; matches the rest of the page) |
| A9 | product → main → reassurance → text | Best results come with 90 days of consistent use. | For a consistent body-care routine, continued daily use is recommended. |

A6 note: return shipping is normally paid by the customer, so "Easy Returns" overstates the process.

## B. Required: unverified reviews / social proof (hide; do NOT replace with new reviews)
There is no review app. All reviews are hardcoded in the theme. The FTC rule on fake reviews and
testimonials (16 CFR Part 465) covers fake or misrepresented reviews and fake social-proof indicators.
Hide these until genuine reviews are connected through a review app:
| # | Location | Why |
|---|---|---|
| B1 | product → main → **custom_liquid_AmeieR** → hide block (eye icon) | "Isabelle … and 50.000+ others purchased" with randomuser.me stock avatars; the number is unverified; German "Verifiziert" label |
| B2 | product → **customer_reviews_carousel_AjfT8a** → hide section | "+10,839 Total Ratings", "Rated 4.8", "Verified Buyer", dates "March 14th, 2025" (before the store/product existed) |
| B3 | product → **ss_testimonials_42_yU96KH** → hide section | "Verified customer" on images that appear AI-generated (hf_20260921_*); "before and after photos", "more youthful" |
| B4 | product → main → **customer_review_MCrBQE** → hide block | "Marleen J." 5★; image file "Authentic-UGC-style-customer-photo…"; cannot be verified |
| B5 | collection → collection_grid_page_hDiTDB → turn off the hardcoded "4.7" rating | Unverified rating |
If any of these come from real customers you can document, they can stay, but only with their true
dates and wording, and with "Verified" only for real purchasers.

## C. Recommended: comparative / replica claims (product page)
| # | Location | Current | Recommendation |
|---|---|---|---|
| C1 | product → product_comparison_hgQaih | Competitor column "Other Body Care" labelled "Knock-off", "No" on every row incl. "Helps Lock In Moisture" | Hide the section, or relabel the column "Typical lotion" and keep only factual ingredient rows. "No" for all other body care's moisturizing is not substantiated. |
| C2 | product → main → replica_warning_wPCWEg | "Watch Out For Cheap Replicas." … "authentic Falunara Botanical Body Oil…" | Hide unless replicas actually exist. If kept, change "Falunara" → "FALUNARA". |

## D. Required: product size (only one 100 ml variant exists)
| # | Location | Current | New |
|---|---|---|---|
| D1 | index → hero → benefit_3_text | Two sizes — 100 ml for the shelf, 200 ml when it sticks | 100 ml / 3.4 fl oz bottle |
| D2 | product → main → buy_faq → answer_4 **and** index → faq → f4 | 100 ml is the everyday bottle and the easier first purchase. 200 ml makes sense once… | FALUNARA Botanical Body Oil currently comes in a 100 ml (3.4 fl oz) bottle. (Also adjust question_4 if it asks about sizes.) |
Verify 100 ml / 3.4 fl oz against the physical label.

## E. Brand spelling → FALUNARA
| # | Location | Current |
|---|---|---|
| E1 | header-group → custom_announcement_bar_KbrQgt → text | Falunara — made for the minute after the shower → FALUNARA — made for the minute after the shower |
| E2 | index → brand → heading | What Falunara → What FALUNARA |
| E3 | index → brand → b_par | Falunara makes body care… → FALUNARA makes body care… |

## F. Footer
Customize → Footer → Add block → **Menu** → Menu: "Footer menu" → Save. (The menu now contains
Contact, Search, Your Privacy Choices. Do not remove the payment icons. Policy links already render
automatically in the bottom row.)

## G. Other-brand template (code editor)
`templates/product.milk-thistle.json` (VEILKIND Milk Thistle, a supplement) is not assigned to any
product, but it can still be opened at `/products/botanical-body-oil?view=milk-thistle`. It contains a
90-day guarantee, "Free U.S. Shipping", supplement claims, and placeholder reviews.
→ Themes → … → Edit code → templates/product.milk-thistle.json → Delete (after confirming no product
uses it: Products → each product → Theme template).

## H. Minor (optional)
- Directions conflict: FAQ says "press — do not rub", steps say "Massage" / "Gently work into". Use one instruction, matching the label.
