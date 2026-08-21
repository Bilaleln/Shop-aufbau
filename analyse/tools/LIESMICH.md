# Auswertungswerkzeuge

Die Skripte in diesem Ordner erzeugen die Auswertungen im uebergeordneten
Ordner `analyse/`. Sie sind bewusst ohne Fremdbibliotheken geschrieben
(nur Python-Standardbibliothek), damit die Auswertung jederzeit von einem
Dritten - etwa einem Sachverstaendigen - nachvollzogen und wiederholt
werden kann.

## bestandsaufnahme.py

    python3 analyse/tools/bestandsaufnahme.py orders_export.csv analyse/

Liest den Shopify-Bestellexport, aggregiert die Line-Item-Zeilen auf
Bestellebene und schreibt `analyse/bestandsaufnahme.md` sowie den
maschinenlesbaren Zwischenstand `analyse/tools/bestellungen.json`.

Festlegungen:

* Kopfdaten stehen im Shopify-Export nur in der ersten Zeile einer
  Bestellung. Je Feld wird der erste nicht-leere Wert einer Bestellung
  uebernommen. Betraege werden dadurch je Bestellung genau einmal gezaehlt.
* Es findet keine Waehrungsumrechnung statt. Betraege werden je Waehrung
  getrennt ausgewiesen.
* Fehlende Spalten werden im Bericht benannt. Die betroffene Auswertung
  entfaellt, es wird kein Wert geschaetzt oder abgeleitet.

## Datenschutz

Die Ausgabedateien enthalten personenbezogene Daten der Geschaedigten.
`analyse/.gitignore` schliesst sie von der Versionsverwaltung aus.
