# FALUNARA: policy pack (2026-10-05)

The connected API has no `write_legal_policies` scope and cannot write to the live theme, so policies
and theme text must be pasted manually. Paste each `.html` file in the policy editor's HTML (`<>`) view.

| Policy | File | Admin location | Status |
|---|---|---|---|
| Return & Refund | `refund-policy.html` | Settings → Policies → Return and refund policy | MANUAL (final text ready) |
| Shipping | `shipping-policy.html` | Settings → Policies → Shipping policy | NEEDS VERIFIED INPUT (customs/origin, see COMPLIANCE-AUDIT §8); the rest is publishable |
| Privacy | `privacy-policy.html` | Settings → Policies → Privacy policy (replace all) | MANUAL (corrected text ready) |
| Terms of Service | `terms-of-service-instructions.md` | Settings → Policies → Terms of service → Create from template | MANUAL |
| Subscription (cancellation) | `subscription-policy.html` | Settings → Policies → Cancellation policy / Subscription policy | MANUAL (final text ready) |

Other files:
- `THEME-EDIT-CHECKLIST.md`: exact theme-editor text changes (guarantee, "Fast Shipping", placeholders, reviews, sizes, brand, footer menu block).
- `COMPLIANCE-AUDIT.md`: changelog, claim audit, MoCRA/label items, shipping config, FTC notes, subscription audit.
- `storefront-text-inventory.md`: verbatim inventory of all theme text.

Store name: Settings → General → Store details → Store name → "FALUNARA" (no Admin API mutation exists for this).
