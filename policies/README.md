# US-LLC-Umstellung – M and B the MBFs LLC (Florida)

Store: **Falurana** (falurana.com). Betreiber ab jetzt: **M and B the MBFs LLC**, Florida, USA.

## Bereits erledigt (per API)

- [x] Markt **United States** angelegt (aktiv, USD, Steuern werden im Checkout addiert)
- [x] Markt **Germany** auf *Entwurf* gesetzt (kein Verkauf mehr nach DE)
- [x] Theme-Templates/Texte im Repo auf US-Englisch umgestellt (US-Versand, 30-Tage-Rückgabe, US-Support)

## Rechtstexte einfügen (Admin → Settings → Policies)

Die Verbindung darf keine Policies schreiben, daher hier zum Kopieren (jeweils in der HTML-Ansicht `<>` einfügen):

| Datei | Shopify-Feld |
|---|---|
| `privacy-policy.html` | Privacy policy (Titel auf „Privacy Policy" ändern, statt „Datenschutzerklärung") |
| `refund-policy.html` | Return and refund policy |
| `shipping-policy.html` | Shipping policy |
| `terms-of-service.html` | Terms of service |
| `contact-information.html` | Contact information – `[ADD YOUR US BUSINESS ADDRESS]` ersetzen |

„Legal notice" / Impressum leeren – in den USA nicht nötig.

## Nur im Shopify-Admin möglich (per API gesperrt)

1. **Settings → General → Store details**
   - Legal business name: `M and B the MBFs LLC`
   - Billing/Store address: US-Adresse in Florida (ersetzt Sankt Augustin) – davon hängt ab, dass der US-Markt zum **Primärmarkt** wird
   - Phone: US-Nummer (optional)
2. **Settings → General → Store defaults**
   - Time zone: `(GMT-05:00) Eastern Time (US & Canada)`
   - Unit system: `Imperial system`, Default weight unit: `lb`
3. **Settings → Taxes and duties**
   - „Include sales tax in product price" **deaktivieren** (US-Preise netto)
   - United States → Sales-Tax-Registrierungen für Bundesstaaten mit Nexus (mindestens **Florida**) eintragen; EU-/DE-USt-Registrierungen entfernen
4. **Settings → Payments**
   - Shopify Payments ist an Land + Unternehmen gebunden. Für eine US-LLC brauchst du ein US-Payout-Konto (EIN, US-Bankkonto). Das deutsche Shopify-Payments-Konto lässt sich i. d. R. nicht auf USA umstellen → Shopify Support kontaktieren
   - DE-Zahlarten (Klarna DE, SEPA, giropay usw.) entfernen; PayPal-Konto auf die LLC umstellen
5. **Settings → Shipping and delivery**
   - Versandzonen außer **United States** löschen (aktuell ~40 Länder hinterlegt)
   - US-Raten anlegen (z. B. Free Shipping ab X USD)
6. **Settings → Locations**
   - Standort „Hubert-Wallich-Straße" (DE) auf die US-Lager-/Versandadresse umstellen bzw. neuen US-Standort anlegen
7. **Settings → Languages**
   - Englisch als Standardsprache (falls Deutsch noch Standard ist)
8. **Settings → Plan / Billing**
   - Rechnungsadresse + Zahlungsmethode für die Shopify-Rechnung auf die LLC umstellen
9. **Produkte**
   - Vendor „Falunara" vs. Shopname „Falurana" prüfen (Tippfehler?)
   - Produktgewichte in lb prüfen, Preise USD prüfen
