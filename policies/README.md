# FALUNARA: Policy setup (audit 2026-10-05)

| Policy | Status | File | Shopify Admin location |
|---|---|---|---|
| Refund Policy | Final text ready; **paste manually** (API lacks `write_legal_policies`) | `refund-policy.html` | Settings → Policies → Return and refund policy → paste the text in the HTML ("<>") view and Save |
| Privacy Policy | Exists (Shopify-generated); corrected text ready; **paste manually** | `privacy-policy.html` | Settings → Policies → Privacy policy |
| Terms of Service | Missing; **create from Shopify's template** (not available via API) | – | Settings → Policies → Terms of service → "Create from template" → Save |
| Shipping Policy | **Needs input** | `shipping-policy-DRAFT.md` | Settings → Policies → Shipping policy |
| Subscription (cancellation) policy | Missing; the product sells Kaching "Subscribe & Save" plans (15% off, every 30/60/90 days). **Needs your cancellation terms** | – | Settings → Policies → Cancellation policy |
| Contact page | Exists: `/pages/contact` (native contact form, template `page.contact`) | – | – |

## Privacy Policy changes (minimal)
- "Falurana operates this store…" / "Falurana is powered by Shopify" → "FALUNARA …"
- Contact line: "please call  or email us" (blank phone) → "please email us"
- Missing space fixed: "deleted.As of" → "deleted. As of"
- "Last updated" → October 5, 2026
Everything else is Shopify's generated text, unchanged.

## Footer
- The live footer (`sections/footer.liquid`) already renders the native policy links
  (`shop.policies`, setting "Show policy links" = on). Refund / Privacy / Terms / Shipping
  appear automatically once each policy has content. No code change is needed.
- The footer has **no Menu block**, so the Footer menu is not shown at all.
  - DONE (API): Added **Contact** to the Footer menu (Online Store → Navigation → Footer menu).
  - MANUAL (theme writes to the live theme are blocked for the API): Online Store → Themes →
    Customize → Footer → Add block → **Menu** → choose "Footer menu" → Save.
