# Skill: /new-block

Wenn der Nutzer `/new-block` eingibt, führe diesen Prozess durch.

## Zweck
Einen neuen Block-Type zu einer bestehenden Section hinzufügen.

## Schritt 1 – Kontext holen
Frage:
1. In welcher Section soll der Block hinzugefügt werden?
2. Was soll der Block darstellen? (Kurze Beschreibung)
3. Welche Settings braucht der Block? (Bilder, Texte, Links, …)

## Schritt 2 – Zusammenfassung
Zeige den geplanten Block-Type im Schema-Format. Bestätigung einholen.

## Schritt 3 – Umsetzen
1. Block-Type im `{% schema %}` `"blocks"` Array ergänzen
2. Entsprechendes Liquid im `{%- for block in section.blocks -%}` Loop einbauen
3. CSS falls nötig in `ringani.css` ergänzen

## Regeln
- Block-Type `"type"` immer lowercase, keine Sonderzeichen
- `{{ block.shopify_attributes }}` im Root-Element des Blocks einfügen
- Bilder über `ringani-image.liquid` rendern
