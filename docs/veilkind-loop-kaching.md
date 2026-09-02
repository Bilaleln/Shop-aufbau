# Veilkind: Loop Subscriptions × Kaching Bundles — Analyse & Wiederaufbau

Analyse des Live-Zustands im Store **Veilkind** (`veilkind.com`, Store-Handle
`0vmyhz-pn`, Plan Basic) — erstellt, bevor der Store gelöscht wird, damit das
Setup auf einem neuen Store 1:1 nachgebaut werden kann.

Alles unter „Befund" ist direkt aus der Shopify Admin API bzw. dem Theme-Code
ausgelesen. Was **nicht** auslesbar war, steht unter
[§6 Was ich nicht sehen konnte](#6-was-ich-nicht-sehen-konnte) — das ist genau
das, was du **vor** dem Löschen selbst sichern musst.

---

## 1. Die drei Bausteine

| Baustein | Was es tut | Wo es liegt |
|---|---|---|
| **Loop Subscriptions** (App-ID `5284869`, Loop Solutions Inc) | Liefert die Abo-Logik: eine native Shopify *Selling-Plan-Gruppe* mit 3 Lieferrhythmen und 10 % Abo-Rabatt | Shopify-Kern (Selling Plans) + Loop-App |
| **Kaching Bundle Quantity Breaks (4.0)** (App-Key `74f3a88c…82ca`) | Liefert die Auswahl-UI auf der Produktseite (die Bundle-Leisten „1× / 2× / 3×") **und** den Mengenrabatt als Shopify Function | Theme-App-Embed + automatischer Rabatt |
| **Theme „CLAUDE CODE ELIXIER"** (Haupt-Theme) | Klebt beides optisch zusammen: übernimmt Kaching-Preise in die Theme-Preisanzeige und in den ATC-Button, schaltet die theme-eigenen Selektoren ab | 3 Stellen im Theme-Code (siehe §4) |

Wichtig für das Verständnis: **Loop und Kaching sind nicht über Theme-Code
verbunden.** Im gesamten Theme kommt kein einziges `selling_plan` vor (außer
der Dawn-Standard-Anzeige im Warenkorb). Die Selling-Plan-ID wird zur Laufzeit
vom Kaching-App-Embed an den Add-to-Cart geschickt — die Verbindung passiert
also **in den App-Einstellungen von Kaching**, nicht im Code.

---

## 2. Befund: Loop-Seite

Selling-Plan-Gruppe (`gid://shopify/SellingPlanGroup/78789083479`), angelegt am
**18.08.2026, 00:34 UTC** von App `5284869` (Loop):

```
Name / Merchant-Code : "Subscribe and Save"
Options-Label        : "Frequency"
Zusammenfassung      : 3 delivery frequencies, 10% discount
```

| Plan | Abrechnung | Lieferung | Rabatt |
|---|---|---|---|
| Deliver every month | jeden 1 Monat | jeden 1 Monat | 10 % |
| Deliver every 3 months | alle 3 Monate | alle 3 Monate | 10 % |
| Deliver every 5 months | alle 5 Monate | alle 5 Monate | 10 % |

- Kategorie `SUBSCRIPTION`, Preisregel `PERCENTAGE 10` (kein fixer Betrag).
- Billing-Intervall = Delivery-Intervall → **kein Prepaid**, jede Lieferung wird
  einzeln abgerechnet.
- Zugewiesen an Produkt **„Vei"** (`placeholder-product`) **und dessen Variante**
  („Default Title"). Die Zuweisung auf Varianten-Ebene ist entscheidend — ohne
  sie taucht das Abo im Storefront nicht auf.
- `requiresSellingPlan: false` → Einmalkauf bleibt möglich (Kaching kann also
  „One-time" und „Subscribe" nebeneinander anbieten).

---

## 3. Befund: Kaching-Seite

**a) App-Embed im Theme aktiv** — in `config/settings_data.json`:

```json
"blocks": {
  "15557474716127144420": {
    "type": "shopify://apps/kaching-bundles/blocks/app-embed-block/6c637362-a106-4a32-94ac-94dcfd68cdb8",
    "disabled": false,
    "settings": {}
  }
}
```

`"settings": {}` heißt: die gesamte Bundle-Konfiguration (Optionen, Preise,
Platzierung, Abo-Verknüpfung) liegt **in der Kaching-App**, nicht im Theme.

**b) Automatischer Rabatt (Shopify Function)**

```
Titel      : "Kaching Bundles - Bundle #2"
Function   : "Kaching Bundle Quantity Breaks (4.0)"
functionId : 006e62fe-88a7-41f7-a302-99e32e19ed55
Status     : ACTIVE
```

Das ist der Mechanismus hinter dem Mengenrabatt: Kaching zeigt im Widget nur
den *reduzierten Preis an*; abgezogen wird er erst im Warenkorb/Checkout durch
diese Function. Der Name „Bundle #2" verrät, dass in der App mindestens zwei
Bundles angelegt wurden — aktiv ist nur dieses eine.

---

## 4. Befund: Der Theme-Glue-Code

Genau **drei** Stellen im Theme kennen Kaching. Alle hängen sich an
Kaching-CSS-Klassen (`.kaching-bundles__bar*`) — es gibt keine offizielle API,
das ist DOM-Scraping.

### 4.1 `sections/shop-product-details.liquid`, Zeilen 211–263 (Inline-Script)

Der eigentliche Kern. Beim Wechsel der Bundle-Auswahl:

```js
const bundleRadioName = document.querySelector(".kaching-bundles__bar input")?.name;
if (bundleRadioName) {
  const bundleRadios = document.querySelectorAll(`input[name='${bundleRadioName}']`);
  bundleRadios.forEach(radio => {
    radio.addEventListener("change", function() {
      const currentQuantity = this.value;
      const parentElem = this.parentElement;
      const curPrice        = parentElem.querySelector(".kaching-bundles__bar-price").innerText;
      const curComparePrice = parentElem.querySelector(".kaching-bundles__bar-full-price").innerText;

      document.querySelector(".shop-product-price-block").innerHTML = curPrice;
      document.querySelector(".shop-compare-price").innerText       = curComparePrice;

      form.querySelectorAll('input[type="hidden"][name="quantity"]').forEach(el => el.remove());
      form.setAttribute('data-quantity', currentQuantity);
    });
  });
}
```

Was hier passiert:
1. Kaching-Preis + Streichpreis werden in die **Theme-Preisanzeige** kopiert
   (`.shop-product-price-block`, `.shop-compare-price`).
2. Alle vorhandenen versteckten `quantity`-Inputs werden aus dem Produktformular
   **entfernt** und die Menge stattdessen als `data-quantity` am Formular
   gesetzt — damit sich Theme-Menge und Kaching-Menge nicht widersprechen.

### 4.2 `assets/shop-product-details.js` (Z. 128–160) und `assets/product-details.js` (Z. 665–695)

Zweimal derselbe Code (Dublette!): 1 Sekunde nach `DOMContentLoaded` wird auf
jede `.kaching-bundles__bar` ein Click-Listener gesetzt, der den ATC-Button
umschreibt:

```js
buttonTextContainer.innerHTML = `Add to Cart - ${price} <span class="compare-price">${fullPrice}</span>`;
```

Der `setTimeout(..., 1000)` ist ein Workaround, weil Kaching sein Widget erst
nach dem Theme rendert. Beim Nachbau solltest du das durch einen
`MutationObserver` ersetzen — bei langsamer Verbindung greift das Timeout sonst
zu früh.

### 4.3 `assets/custom.css`, Zeile 129

```css
.gb-cart-drawer-lb kaching-bundle { display: none; }
```

Blendet das Kaching-Web-Component im Cart-Drawer aus — es soll nur auf der
Produktseite erscheinen.

---

## 5. Befund: Wie das Produkt-Template aufgebaut ist

Das Produkt „Vei" nutzt `templateSuffix: milk-thistle`, also
`templates/product.milk-thistle.json` mit der Custom-Section
`shop-product-details`.

Entscheidend ist, **was dort abgeschaltet wurde**, damit Kaching die Auswahl
übernehmen kann:

| Block | Typ | Status |
|---|---|---|
| `supply_label` („Choose your supply") | `custom_text` | **disabled** |
| `variant_picker` | `simple_variant_picker` | **disabled** |
| `quantity` | `quantity_selector` | **disabled** |
| `add_to_cart` | `add_to_cart` | aktiv, `show_price_in_button: true`, Text „ADD TO CART" |

Block-Reihenfolge: `pdp_styles → title → trustpilot_rating → subtitle → labels →
divider → price → benefits → divider → [supply_label, variant_picker, quantity —
alle aus] → add_to_cart → payment_icons → guarantee_badges → money_back → quick_faq`

→ Zwischen `price` und `add_to_cart` klafft bewusst eine Lücke: **dort injiziert
das Kaching-App-Embed seine Bundle-Leisten.** Die Platzierung steuerst du in der
Kaching-App über einen CSS-Selector, nicht über das Theme.

Zum Vergleich: das ältere `templates/product.json` benutzt noch den
**theme-eigenen** Quantity-Break-Block (`snippets/quantity-break.liquid`, 89 KB)
mit „1-Month Supply / 2-Month Supply (39,99 $, Badge LIMITED TIME) / 3-Month
Supply". Dieser Weg wurde offenbar zugunsten von Kaching verworfen — der Code
liegt aber noch im Theme. Er kennt **keine** Abos.

---

## 6. Was ich nicht sehen konnte

Diese Daten liegen in den App-Datenbanken von Kaching und Loop und sind über die
Shopify-API nicht lesbar. **Sie sind mit dem Store weg — bitte vor dem Löschen
abfotografieren/dokumentieren:**

1. **Kaching → Bundle #2, komplett**: Anzahl Optionen, Mengen je Option, Rabatt
   je Option, Titel/Untertitel/Badges, Farben, Platzierungs-Selector, und vor
   allem: **die Abo-Einstellung** (welche Option „Subscribe" ist und auf welchen
   Loop-Selling-Plan sie zeigt).
2. **Kaching → weitere Bundles** (Bundle #1 existiert offenbar, ist inaktiv).
3. **Loop → Widget-, Kundenportal- und Dunning-Einstellungen**, Rabattregeln,
   E-Mail-Templates.
4. App-eigene Metafelder beider Apps (privat, nur für die App lesbar).

Ebenfalls nicht auslesbar war die Liste der installierten Apps (fehlende
`read_apps`-Berechtigung) — es kann also weitere Apps geben, die ich hier nicht
aufführe.

---

## 7. Wiederaufbau auf einem neuen Store

### Schritt 0 — Sichern, **bevor** du löschst

- [ ] **Theme-ZIP**: Admin → *Online Store → Themes → „CLAUDE CODE ELIXIER" →
      … → Theme-Datei herunterladen*. Die ZIP kommt per E-Mail und enthält
      **alles** inkl. Bilder — das ist die einzige vollständige Sicherung.
      (Im Ordner `veilkind-snapshot/` dieses Repos liegt nur ein **Auszug** der
      integrationsrelevanten Dateien, siehe dessen README.)
- [ ] **Alle Themes**, nicht nur das Haupt-Theme (es gibt noch `Horizon`,
      `routine-theme`, 2× `elixer-1-1-theme`).
- [ ] **Screenshots** von allem aus §6.
- [ ] **Produkte/Kunden** als CSV exportieren, **Dateien** (Admin → Content →
      Files) und Produktbilder herunterladen.
- [ ] **Prüfen, ob es aktive Abo-Verträge gibt.** Mit dem Store sterben laufende
      Subscription Contracts — Kunden müssten neu abschließen. (Im aktuellen
      Store gibt es nur ein Platzhalter-Produkt, aber prüfe es in Loop.)

### Schritt 1 — Theme

Neuen Store anlegen → Theme-ZIP hochladen → veröffentlichen.

### Schritt 2 — Loop installieren und Plan anlegen

Loop Subscriptions installieren, dann eine Selling-Plan-Gruppe exakt so:

```
Name          : Subscribe and Save
Options-Label : Frequency
Plan 1: Deliver every month     → alle 1 Monat,  10 % Rabatt
Plan 2: Deliver every 3 months  → alle 3 Monate, 10 % Rabatt
Plan 3: Deliver every 5 months  → alle 5 Monate, 10 % Rabatt
```

Abrechnung = Lieferung (kein Prepaid). Danach die Gruppe dem Produkt **und der
Variante** zuweisen und „Einmalkauf erlauben" anlassen.

*Kontrolle:* Im Admin muss beim Produkt unter „Purchase options" die Gruppe
stehen. Wenn nicht, findet Kaching später keinen Plan.

### Schritt 3 — Kaching installieren und Bundle bauen

1. Kaching Bundle Quantity Breaks installieren.
2. **App-Embed im Theme aktivieren** (*Themes → Anpassen → App-Einbettungen →
   Kaching Bundles*). Ohne das rendert nichts.
3. Bundle mit den Optionen aus deinen Screenshots anlegen (Mengen, Rabatte,
   Badges, Farben).
4. **Abo verknüpfen**: In der Bundle-Konfiguration die Subscription-/Selling-Plan-
   Option aktivieren und den Loop-Plan „Subscribe and Save" auswählen. Kaching
   liest die von Loop erzeugten Selling Plans direkt aus Shopify — deshalb muss
   Schritt 2 **vorher** fertig sein.
5. Platzierung setzen: Widget zwischen Preisblock und ATC-Button, im
   Veilkind-Theme also zwischen `.shop-product-price-block` und
   `.shop-add-to-cart-button`.

*Kontrolle:* Der automatische Rabatt „Kaching Bundles - Bundle #…" muss unter
Admin → *Discounts* auftauchen und **aktiv** sein.

### Schritt 4 — Produkt-Template anpassen

Im Theme-Editor auf dem Produkt-Template die Blöcke `simple_variant_picker`,
`quantity_selector` und das Label „Choose your supply" **deaktivieren** (nicht
löschen — deaktiviert bleiben sie umschaltbar). Sonst hast du zwei konkurrierende
Mengen-/Varianten-Auswahlen.

### Schritt 5 — Glue-Code einsetzen

Die drei Stellen aus §4 übernehmen. Sie sind theme-spezifisch — passe die
Selektoren an, falls du ein anderes Theme nutzt:

| Kaching-Selector | Theme-Ziel (Veilkind) |
|---|---|
| `.kaching-bundles__bar input` | Produktformular `product-form-{section.id}` |
| `.kaching-bundles__bar-price` | `.shop-product-price-block` |
| `.kaching-bundles__bar-full-price` | `.shop-compare-price` |
| `.kaching-bundles__bar` (click) | `.shop-add-to-cart-button .button-text` |
| `kaching-bundle` im Drawer | via CSS ausblenden |

Empfehlung beim Nachbau: die Dublette in `shop-product-details.js` /
`product-details.js` auf **eine** Datei reduzieren und das `setTimeout(1000)`
durch einen `MutationObserver` auf den Widget-Container ersetzen.

### Schritt 6 — Testen

- [ ] Bundle-Auswahl wechseln → Preis, Streichpreis und ATC-Button aktualisieren sich.
- [ ] Abo-Option wählen → im Warenkorb steht der Plan-Name
      (`item.selling_plan_allocation.selling_plan.name` wird in
      `snippets/cart-drawer.liquid` Z. 1130 und
      `sections/main-cart-items.liquid` Z. 262 gerendert).
- [ ] Checkout: Mengenrabatt (Kaching-Function) **und** 10 % Abo-Rabatt (Loop)
      greifen beide — Rabatt-Stacking in den Rabatt-Einstellungen prüfen, sonst
      schluckt einer den anderen.
- [ ] Testbestellung → in Loop muss ein Subscription Contract entstehen.
- [ ] Cart-Drawer: kein Kaching-Widget sichtbar.

---

## 8. Stolperfallen

- **Reihenfolge zählt.** Erst Loop-Plan, dann Kaching-Bundle. Kaching kann nur
  Selling Plans anbieten, die es beim Anlegen des Bundles schon gibt.
- **Varianten-Zuweisung.** Der Plan muss an der *Variante* hängen, nicht nur am
  Produkt.
- **Gratis-Zugaben im Bundle**: Ein Geschenk-Artikel darf in **keinem**
  Loop-Selling-Plan hängen, sonst wird er als Abo-Position mitverkauft. Loop
  empfiehlt dafür eine Duplikat-SKU, die nur Kaching verwendet.
- **DOM-Abhängigkeit.** Der Glue-Code hängt an Kaching-CSS-Klassen. Ein
  Kaching-Update, das die Klassennamen ändert, bricht Preisanzeige und
  ATC-Button — dann sind §4.1/§4.2 die ersten Stellen zum Nachziehen.
- **Preis-Anzeige ≠ Preis.** Kaching zeigt den Bundle-Preis nur an; abgezogen
  wird er durch die Function. Ist der Rabatt inaktiv, sieht der Kunde einen
  Preis, den er nicht bekommt.

---

## Quellen

- [Kaching bundles — Loop Subscriptions Help Center](https://help.loopwork.co/en/articles/12745875-kaching-bundles)
- [How To Sell Subscriptions For Bundles in Shopify — Kaching Bundles Help Center](https://support.kachingappz.com/en/articles/11660573-how-to-sell-subscriptions-for-bundles-in-shopify)

Beide Seiten waren aus dieser Session nicht direkt abrufbar (Netzwerk-Policy) —
die Setup-Schritte oben stammen aus dem ausgelesenen Store-Zustand, nicht aus
diesen Artikeln. Lies sie vor dem Nachbau trotzdem einmal durch.
