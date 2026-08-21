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

## tracking_abrufen.py

    python3 analyse/tools/tracking_abrufen.py orders_export.csv analyse/tracking_raw

Sichert die Trackingseiten zu den Sendungsnummern beweisfest. **Dieses Skript
muss auf dem Rechner des Store-Inhabers ausgefuehrt werden** - in der
Analyseumgebung ist die Domain epsfullfil.com durch eine Netzwerkrichtlinie
gesperrt.

Je Sendungsnummer werden gesichert: der unveraenderte HTML-Quelltext, die
vollstaendigen HTTP-Antwortkopfzeilen, der SHA-256-Pruefwert des Quelltextes
und der Abrufzeitpunkt in UTC und Ortszeit. Der Pruefwert belegt spaeter, dass
die gesicherte Datei seit dem Abruf unveraendert ist.

Wichtige Schalter:

* `--limit N` - nur die ersten N Nummern abrufen (Stichprobe)
* `--nummern datei.txt` - Nummern aus einer Textdatei statt aus dem CSV
* `--durchgang 2` - Zweitabruf an einem spaeteren Tag. Damit laesst sich
  pruefen, ob sich das angezeigte Zustelldatum mit dem Kalendertag mitbewegt.
* `--pause SEK` - Wartezeit zwischen den Abrufen, Vorgabe 2 Sekunden

Hinweis: Der Standard-Bestellexport von Shopify enthaelt keine Spalte fuer
Sendungsnummern. Findet das Skript keine, gibt es aus, auf welchen Wegen die
Nummern sonst zu beschaffen sind.
