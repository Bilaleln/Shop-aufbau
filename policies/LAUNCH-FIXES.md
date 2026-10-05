# FALUNARA: remaining merchant actions

The API can't publish themes, write policies, delete theme files, edit Kaching settings, change the
store name, or set shipping prices without your approval. Everything below is left for you.

Theme copy with all fixes applied: **"FALUNARA – launch fixes (2026-10-05)"** (unpublished).
It was copied from the live theme when the live theme was last edited (2026-10-05 20:46 UTC).
**Do not edit the live theme before publishing the copy.** Edits made to the live theme now would not be in the copy.

---------------------------------------------------------------------------------------------------
## CRITICAL — BEFORE ADS
---------------------------------------------------------------------------------------------------

### CRITICAL #1 — Remove the leftover VEILKIND template (from the copy, before publishing)
Shopify Admin → Online Store → Themes → "FALUNARA – launch fixes (2026-10-05)" → **⋯** → **Edit code**
→ left sidebar **Templates** → `product.milk-thistle.json` → hover → **⋯** → **Delete** → confirm.
(Already verified: no product uses this template.)

### CRITICAL #2 — Preview, then publish the fixed theme
1. Online Store → Themes → "FALUNARA – launch fixes (2026-10-05)" → **⋯** → **Preview**.
2. On the product page, check:
   - The "Customer Reviews" carousel, the "What Women Are Saying" testimonials, the "Isabelle … 50.000+ others purchased" badge, the "Marleen J." review card, the "Knock-off" comparison table and the "Watch Out For Cheap Replicas" box are **gone**.
   - The guarantee section shows: "30-Day Money-Back Guarantee" · "Shipping Calculated at Checkout" · "Email Support".
   - FAQ: "What size is the bottle?" → "100 ml / 3.4 fl oz" and "30-Day Money-Back Guarantee" (new answer). *Note: this FAQ block is set to show 4 items. If the guarantee question isn't visible, go to Customize → Products → Default product → Product information → FAQ block → item limit → 5.*
   - The line under the buy box reads "For a consistent body-care routine, continued daily use is recommended."
   - Bundle and subscription widgets (Kaching) still show and add to cart.
3. Home page: hero benefit reads "100 ml / 3.4 fl oz bottle"; brand block reads "What FALUNARA"; announcement bar reads "FALUNARA — made for…".
4. Footer: new **"Help"** menu column with Contact · Search · Your Privacy Choices; policy links in the bottom row; payment icons still there. Check on desktop and phone.
5. Back in Themes: the copy's **⋯** → **Publish** → **Publish**.

*Fallback if you don't want to publish the copy:* make the same edits on the live theme in
**Customize → Products → Default product**:
| Section → Block | Setting | Action |
|---|---|---|
| Product information → "Custom Liquid" (sp-badge, "Isabelle") | eye icon | Hide |
| Product information → "Customer review" (Marleen J.) | eye icon | Hide |
| Product information → "Replica warning" | eye icon | Hide |
| "Customer Reviews" (carousel) section | eye icon | Hide |
| "What Women Are Saying" testimonials section | eye icon | Hide |
| Product comparison ("Thoughtful Care. Simple Routine.") section | eye icon | Hide |
| Money-Back Guarantee section | Benefit 1 / 2 / 3 | "30-Day Money-Back Guarantee" / "Shipping Calculated at Checkout" / "Email Support" |
| Money-Back Guarantee section | Description | "Not satisfied? Contact us within 30 days of delivery to request a return and refund. Return instructions are provided once your request is approved. See our Return & Refund Policy for full details." |
| Money-Back Guarantee section | Product name | "FALUNARA Botanical Body Oil" |
| Product information → FAQ block | Question/Answer 4 | "What size is the bottle?" / "FALUNARA Botanical Body Oil comes in a 100 ml / 3.4 fl oz bottle." |
| Product information → FAQ block | Question/Answer 5 | "30-Day Money-Back Guarantee" / the FAQ answer text you provided |
| Product information → Custom text ("Best results…") | Text | "For a consistent body-care routine, continued daily use is recommended." |
| Home page → Hero | Benefit 3 | "100 ml / 3.4 fl oz bottle" |
| Home page → FAQ → "Which size…" | Q/A | same as product FAQ 4 |
| Home page → Brand section | Heading / paragraph | "Falunara" → "FALUNARA" |
| Header → Announcement bar | Text | "FALUNARA — made for the minute after the shower" |
| Collections → Collection Grid | Show rating | Off |
| Footer → Add block → Menu | Heading "Help", Menu "Footer menu" | Save |

### CRITICAL #3 — Publish the policies (repo folder `policies/`)
For each one: Shopify Admin → **Settings → Policies** → click the policy → in the editor click **Show HTML** (`<>`)
→ select all → paste the file's full contents → **Save**.
| Policy | File | HTML view | Action |
|---|---|---|---|
| Return and refund policy | `refund-policy.html` | Yes | Paste, then Save. **Final.** |
| Privacy policy | `privacy-policy.html` | Yes | Replace all, then Save. **Final.** |
| Subscription policy (cancellation policy) | `subscription-policy.html` | Yes | Paste, then Save. **Final.** |
| Shipping policy | `shipping-policy.html` | Yes | Paste, then Save. Contains no unverified fulfillment facts. Add the customs paragraph later (IMPORTANT #2). |
| Terms of service | — | — | Click **Create from template**, then make the edits in `terms-of-service-instructions.md` (FALUNARA brand; "operated by M and B the MBFs LLC, doing business as FALUNARA"; email badush71@proton.me; address only as a mailing address; delete any empty phone wording), then Save |
Then open each policy link in the store footer and check that it loads and that there are no "Falurana" or "[" placeholders.

### CRITICAL #4 — Store name
Settings → **General** → Store details → pencil icon → **Store name** → `FALUNARA` → Save.
(Do not change the legal business name field if one is shown: "M and B the MBFs LLC". Do not change the domain.)

### CRITICAL #5 — Kaching Subscribe & Save disclosure
Shopify Admin → **Apps → Kaching Subscriptions** → open the subscription widget/offer used on
"FALUNARA Botanical Body Oil" (plan group "FALUNARA – Subscribe & Save"). Exact menu labels in Kaching
may differ slightly. Set:
1. **Default selection → One-time purchase** (subscription must NOT be preselected).
2. Subscription option title: `Subscribe & Save — 15% off`
3. Subscription option description/subtitle:
   `Recurring order: delivered and charged automatically every 30, 60, or 90 days (you choose) at 15% off until you cancel. No minimum commitment, no cancellation fee. Cancel future renewals anytime before your next order is processed.`
4. If there's a link/footnote field: `Subscription policy` → `/policies/subscription-policy`
5. Plan names: "Delivered every 30 days", "Delivered every 60 days", "Delivered every 90 days".
6. Confirm that customers can cancel through the Kaching customer portal / customer account. Place a test subscription order, cancel it, and refund it.
Save, then reload the product page and check that one-time purchase is selected by default.

### CRITICAL #6 — US shipping rate (choose the USD price first)
Currently US checkout shows "Standard International – $22.50" (converted from €19.99).
1. Settings → **Shipping and delivery** → Shipping → **General shipping rates** ("Allgemeines Profil") → click it.
2. Zone **International** → **⋯** → **Edit zone** → uncheck **United States** → **Done**.
3. **Create zone** → name `United States` → tick **United States** → **Done**.
4. In the new zone → **Add rate** → Use flat rate → Rate name `Standard Shipping` → Price **$[your chosen USD amount]** → **Done**.
5. **Save**. Test: add the product to the cart → checkout → enter a US address → confirm the USD rate.
Do not add delivery-time text or "fast/free shipping" until fulfillment timing is confirmed.

---------------------------------------------------------------------------------------------------
## IMPORTANT — BEFORE SCALE
---------------------------------------------------------------------------------------------------

### IMPORTANT #1 — Ingredients and warnings
**VERIFIED INCI REQUIRED FROM SUPPLIER.**
**VERIFIED WARNINGS/CAUTIONS REQUIRED FROM SUPPLIER.**
No complete ingredient list or warning text exists in the store or the repo. When you receive them:
Products → FALUNARA Botanical Body Oil → Description → add an "Ingredients" paragraph (paste the INCI list
exactly as on the label) and a "Cautions" paragraph (the supplier's wording) → Save.

### IMPORTANT #2 — Customs paragraph in the Shipping policy
Once the supplier confirms the ship-from country for US orders: Settings → Policies → Shipping policy →
Show HTML → paste ONE of the options from COMPLIANCE-AUDIT.md §8 before "Questions" → Save.

### IMPORTANT #3 — Genuine reviews
Online Store → Apps → install a review app (e.g. Judge.me or Shopify Product Reviews) → enable its
product-page block (Customize → Default product → Add block → [review app]). Show only real,
order-verified reviews. Do not re-enable the hidden theme review sections.

### IMPORTANT #4 — Remove the leftover review images (optional cleanup)
Content → Files → search `hf_20260921` and `Authentic-UGC` → select → Delete. (Only after the copy is
published, so nothing live references them.)

---------------------------------------------------------------------------------------------------
## OPTIONAL — TRUST/UX
---------------------------------------------------------------------------------------------------
1. Branded support email: Settings → General → Store contact details → Customer email (e.g. support@falurana.com, after creating the mailbox) → Save; then update the email in the 5 policies and the Contact page.
2. Privacy policy title: after saving, check the footer link reads "Privacy Policy" (the API returned the German title "Datenschutzerklärung"). If German: Settings → Users → your profile → Language → English, then re-save the policy.
3. Directions wording: FAQ "press — do not rub" vs. steps "Massage…": Customize → Default product → "Your Daily Ritual" steps → pick one instruction that matches the label.
4. Old unpublished themes ("Horizon", "elixer-1-1-theme-1", "FALUNARA PDP – Subscription preview", and the old live theme after publishing): Themes → ⋯ → Remove, if no longer needed.
