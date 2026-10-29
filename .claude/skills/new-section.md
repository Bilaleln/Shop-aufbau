# Skill: /new-section

Wenn der Nutzer `/new-section` eingibt, führe diesen Prozess durch.

## Zweck
Eine neue Shopify Liquid Section für das RINGANI-Theme erstellen – nach exakt
denselben Konventionen wie alle bestehenden Sections im Projekt.

## Schritt 1 – Informationen sammeln
Frage nacheinander (nicht alles auf einmal):

1. **Name der Section** – z. B. "Testimonials", "Vertrauens-Logos", "Video-Hero"
2. **Zweck** – Was soll diese Section zeigen / tun?
3. **Blöcke** – Welche wiederholbaren Elemente gibt es? (z. B. jedes Testimonial ist ein Block)
4. **Settings** – Welche fixen Einstellungen braucht die Section? (Überschrift, Hintergrundfarbe, …)
5. **Mobile-Verhalten** – Wie soll es auf Mobilgeräten aussehen?

Lass den Nutzer reden / ramble – du räumst es danach auf.

## Schritt 2 – Zusammenfassung zeigen
Zeige eine kurze Zusammenfassung:
- Section-Name (Dateiname: `ringani-[name].liquid`)
- Blöcke mit ihren Settings
- Schema-Aufbau
Frage: "Passt das so, oder soll ich etwas ändern?"

## Schritt 3 – Dateien erstellen
Erstelle:
1. `sections/ringani-[name].liquid` – vollständige Section mit:
   - `ringani-section-vars.liquid` Einbindung
   - Sauberem HTML mit `ringani-*` Klassen
   - `{% schema %}` Block mit `name`, `settings`, `blocks`, `presets`
2. Falls nötig: CSS-Ergänzungen in `assets/ringani.css` hinzufügen

## Regeln (nie brechen)
- Namespace `ringani-*` für alle Klassen und Liquid-Variablen
- Design-Tokens aus `ringani.css` verwenden, nie Hardcode-Farben
- `ringani-image.liquid` für alle Bilder nutzen
- Echte `<button>` Tags, `aria-*` Attribute
- `loading="lazy"` unter dem Fold
- Kein externes JavaScript
- Schema immer mit `"presets": [{"name": "RINGANI – [Name]"}]`
