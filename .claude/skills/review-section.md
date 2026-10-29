# Skill: /review-section

Wenn der Nutzer `/review-section` eingibt, führe diesen Prozess durch.

## Zweck
Eine bestehende RINGANI Section auf Qualität, Konventionen und Fehler prüfen.

## Schritt 1 – Welche Section?
Frage: "Welche Section soll ich reviewen?" (Dateiname oder Beschreibung)

## Schritt 2 – Prüfliste durchgehen
Prüfe die Section gegen diese Punkte:

### Konventionen
- [ ] Alle CSS-Klassen mit `ringani-` Prefix
- [ ] Keine Hardcode-Farben (nur CSS-Variablen aus `ringani.css`)
- [ ] `ringani-section-vars.liquid` eingebunden
- [ ] Bilder über `ringani-image.liquid` oder `ringani-media.liquid`
- [ ] Schema hat `presets` Array

### Performance
- [ ] `loading="lazy"` bei Bildern unter dem Fold
- [ ] Kein externes JavaScript geladen
- [ ] JS ist `defer` wenn nötig

### Accessibility
- [ ] Alle interaktiven Elemente sind echte `<button>` oder `<a>`
- [ ] `aria-*` Attribute wo nötig
- [ ] Alt-Texte bei Bildern vorhanden oder über Settings befüllbar

### Liquid
- [ ] Keine unnötigen `assign` in Loops
- [ ] `| escape` bei User-Inputs
- [ ] Korrekte `{%- -%}` Whitespace-Kontrolle

### Schema
- [ ] Jedes Setting hat `id`, `type`, `label`
- [ ] Sinnvolle `default` Werte gesetzt
- [ ] Block-Types haben `name` und `settings`

## Schritt 3 – Ergebnis
Zeige:
1. Was gut ist ✅
2. Was geändert werden sollte ⚠️ (mit konkretem Code-Vorschlag)
3. Was ein Fehler ist ❌ (mit Fix)

Frage dann: "Soll ich die Fixes direkt einbauen?"
