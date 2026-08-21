#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ruft die Trackingseiten zu den Sendungsnummern ab und sichert sie beweisfest.

DIESES SKRIPT WIRD AUF DEM RECHNER DES STORE-INHABERS AUSGEFUEHRT.
In der Analyseumgebung ist die Domain epsfullfil.com durch eine
Netzwerkrichtlinie gesperrt, ein Abruf ist dort nicht moeglich.

Beweissicherung: Zu jeder abgerufenen Seite werden gespeichert
  * der unveraenderte HTML-Quelltext (nichts gekuerzt, nichts umformatiert)
  * die vollstaendigen HTTP-Antwortkopfzeilen
  * der SHA-256-Pruefwert des Quelltextes
  * der Abrufzeitpunkt in UTC und in Ortszeit
Der Pruefwert erlaubt es, spaeter nachzuweisen, dass die gesicherte Datei
seit dem Abruf nicht veraendert wurde.

Aufruf:
    python3 tracking_abrufen.py orders_export.csv analyse/tracking_raw

    # nur die ersten 20 Nummern (Stichprobe):
    python3 tracking_abrufen.py orders_export.csv analyse/tracking_raw --limit 20

    # Zweitabruf an einem spaeteren Tag, um zu pruefen, ob sich das
    # angezeigte Zustelldatum mitbewegt:
    python3 tracking_abrufen.py orders_export.csv analyse/tracking_raw --durchgang 2

    # Nummern aus einer einfachen Textdatei statt aus dem CSV:
    python3 tracking_abrufen.py --nummern nummern.txt analyse/tracking_raw
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

csv.field_size_limit(10 * 1024 * 1024)

BASIS_URL = 'https://epsfullfil.com/track/%s'

# Spaltennamen, unter denen Shopify-Exporte Sendungsdaten fuehren koennen.
TRACKING_SPALTEN = [
    'Tracking Number', 'Tracking Numbers', 'Tracking number',
    'Lineitem tracking number', 'Fulfillment Tracking Number',
    'Tracking Url', 'Tracking URL', 'Tracking Company',
]

# Erkennt Sendungsnummern in beliebigen Feldern, falls keine eigene Spalte da ist.
MUSTER_URL = re.compile(r'epsfullfil\.com/track/([A-Za-z0-9._-]{4,})', re.I)
MUSTER_NUMMER = re.compile(r'\b([A-Z]{2}\d{7,}[A-Z]{0,2}|[A-Z0-9]{10,24})\b')


def norm(s):
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


def nummern_aus_csv(pfad):
    """Sucht Sendungsnummern im Export. Rueckgabe: (liste, bericht)."""
    with open(pfad, 'r', encoding='utf-8-sig', newline='') as fh:
        probe = fh.read(64 * 1024)
        fh.seek(0)
        try:
            dialekt = csv.Sniffer().sniff(probe, delimiters=',;\t')
        except csv.Error:
            dialekt = csv.excel
        leser = csv.DictReader(fh, dialect=dialekt)
        kopf = leser.fieldnames or []
        vorhanden = {norm(h): h for h in kopf}
        treffer_spalten = []
        for kandidat in TRACKING_SPALTEN:
            echt = vorhanden.get(norm(kandidat))
            if echt and echt not in treffer_spalten:
                treffer_spalten.append(echt)

        namensspalte = None
        for kandidat in ('Name', 'Id'):
            if norm(kandidat) in vorhanden:
                namensspalte = vorhanden[norm(kandidat)]
                break

        gefunden = []          # (bestellnummer, sendungsnummer, herkunft)
        gesehen = set()
        letzte_bestellung = ''
        zeilen = 0

        for zeile in leser:
            zeilen += 1
            bestellung = (zeile.get(namensspalte) or '').strip() if namensspalte else ''
            if bestellung:
                letzte_bestellung = bestellung
            else:
                bestellung = letzte_bestellung

            kandidaten = []
            for sp in treffer_spalten:
                wert = (zeile.get(sp) or '').strip()
                if wert:
                    kandidaten.append((wert, 'Spalte "%s"' % sp))
            if not kandidaten:
                # Notfall: alle Felder nach epsfullfil-URLs absuchen
                for sp, wert in zeile.items():
                    if not wert:
                        continue
                    for m in MUSTER_URL.finditer(str(wert)):
                        kandidaten.append((m.group(1), 'URL in Spalte "%s"' % sp))

            for wert, herkunft in kandidaten:
                m = MUSTER_URL.search(wert)
                nummer = m.group(1) if m else wert.strip()
                if not nummer or nummer.lower() in ('n/a', 'none', '-'):
                    continue
                if '://' in nummer:
                    continue
                schluessel = (bestellung, nummer)
                if schluessel in gesehen:
                    continue
                gesehen.add(schluessel)
                gefunden.append((bestellung, nummer, herkunft))

    bericht = {
        'zeilen_gelesen': zeilen,
        'kopfzeile': kopf,
        'gefundene_tracking_spalten': treffer_spalten,
        'anzahl_nummern': len(gefunden),
    }
    return gefunden, bericht


def nummern_aus_textdatei(pfad):
    out = []
    with open(pfad, 'r', encoding='utf-8') as fh:
        for i, zeile in enumerate(fh, 1):
            z = zeile.strip()
            if not z or z.startswith('#'):
                continue
            m = MUSTER_URL.search(z)
            out.append(('(Zeile %d)' % i, m.group(1) if m else z, 'Textdatei'))
    return out, {'anzahl_nummern': len(out), 'quelle': pfad}


def abrufen(nummer, ziel_ordner, durchgang, pause, timeout=45):
    url = BASIS_URL % nummer
    sicher = re.sub(r'[^A-Za-z0-9._-]', '_', nummer)
    praefix = 'd%d_%s' % (durchgang, sicher)
    pfad_html = os.path.join(ziel_ordner, praefix + '.html')
    pfad_kopf = os.path.join(ziel_ordner, praefix + '.headers.txt')

    satz = {
        'sendungsnummer': nummer,
        'url': url,
        'durchgang': durchgang,
        'abruf_utc': datetime.now(timezone.utc).isoformat(),
        'abruf_ortszeit': datetime.now().astimezone().isoformat(),
    }

    anfrage = urllib.request.Request(url, headers={
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/126.0.0.0 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'de-DE,de;q=0.9,en;q=0.8',
    })

    try:
        with urllib.request.urlopen(anfrage, timeout=timeout) as antwort:
            rohdaten = antwort.read()
            satz['http_status'] = antwort.status
            satz['end_url'] = antwort.geturl()
            kopfzeilen = str(antwort.headers)
    except urllib.error.HTTPError as f:
        rohdaten = f.read() if hasattr(f, 'read') else b''
        satz['http_status'] = f.code
        satz['end_url'] = url
        satz['fehler'] = 'HTTPError %s %s' % (f.code, f.reason)
        kopfzeilen = str(f.headers) if f.headers else ''
    except Exception as f:                                   # noqa: BLE001
        satz['http_status'] = None
        satz['fehler'] = '%s: %s' % (type(f).__name__, f)
        satz['gespeichert'] = None
        time.sleep(pause)
        return satz

    with open(pfad_html, 'wb') as fh:
        fh.write(rohdaten)
    with open(pfad_kopf, 'w', encoding='utf-8') as fh:
        fh.write('Abruf UTC:      %s\n' % satz['abruf_utc'])
        fh.write('Abruf Ortszeit: %s\n' % satz['abruf_ortszeit'])
        fh.write('Angefragte URL: %s\n' % url)
        fh.write('Endgueltige URL:%s\n' % satz.get('end_url', ''))
        fh.write('HTTP-Status:    %s\n' % satz.get('http_status'))
        fh.write('\n--- Antwortkopfzeilen ---\n')
        fh.write(kopfzeilen)

    satz['bytes'] = len(rohdaten)
    satz['sha256'] = hashlib.sha256(rohdaten).hexdigest()
    satz['gespeichert'] = os.path.basename(pfad_html)
    satz['kopfzeilen_datei'] = os.path.basename(pfad_kopf)
    time.sleep(pause)
    return satz


def main():
    p = argparse.ArgumentParser(description='Trackingseiten beweisfest sichern.')
    p.add_argument('csv_datei', nargs='?', help='orders_export.csv')
    p.add_argument('ziel', nargs='?', default='analyse/tracking_raw')
    p.add_argument('--nummern', help='Textdatei mit je einer Sendungsnummer pro Zeile')
    p.add_argument('--limit', type=int, default=0, help='nur die ersten N Nummern')
    p.add_argument('--durchgang', type=int, default=1,
                   help='1 = Erstabruf, 2 = Zweitabruf an einem spaeteren Tag')
    p.add_argument('--pause', type=float, default=2.0,
                   help='Sekunden Pause zwischen den Abrufen (Vorgabe 2)')
    a = p.parse_args()

    if a.nummern:
        gefunden, bericht = nummern_aus_textdatei(a.nummern)
    elif a.csv_datei:
        gefunden, bericht = nummern_aus_csv(a.csv_datei)
    else:
        p.error('Entweder eine CSV-Datei oder --nummern angeben.')

    print('Gelesene Quelle: %s' % (a.nummern or a.csv_datei))
    if 'gefundene_tracking_spalten' in bericht:
        if bericht['gefundene_tracking_spalten']:
            print('Sendungsdaten gefunden in: %s'
                  % ', '.join(bericht['gefundene_tracking_spalten']))
        else:
            print('')
            print('HINWEIS: Im Export gibt es keine eigene Spalte fuer Sendungsnummern.')
            print('Der Standard-Bestellexport von Shopify enthaelt diese Spalte nicht.')
            print('Moegliche Wege an die Nummern:')
            print('  * Shopify-Admin, Bestellung oeffnen, Sendungsnummer je Bestellung ablesen')
            print('  * Export ueber eine App, die Fulfillment-Daten mit ausgibt')
            print('  * Die Versandbestaetigungsmails an die Kunden')
            print('Die Nummern koennen anschliessend in eine Textdatei geschrieben')
            print('und mit --nummern uebergeben werden.')
            print('')
    print('Gefundene Sendungsnummern: %d' % len(gefunden))
    if not gefunden:
        sys.exit(2)

    if a.limit:
        gefunden = gefunden[:a.limit]
        print('Begrenzt auf die ersten %d Nummern.' % len(gefunden))

    os.makedirs(a.ziel, exist_ok=True)
    protokoll = []
    for i, (bestellung, nummer, herkunft) in enumerate(gefunden, 1):
        print('[%d/%d] %s (Bestellung %s) ... ' % (i, len(gefunden), nummer, bestellung),
              end='', flush=True)
        satz = abrufen(nummer, a.ziel, a.durchgang, a.pause)
        satz['bestellnummer'] = bestellung
        satz['herkunft_der_nummer'] = herkunft
        protokoll.append(satz)
        print('%s%s' % (satz.get('http_status'),
                        '  ' + satz['fehler'] if satz.get('fehler') else
                        '  %d Bytes' % satz.get('bytes', 0)))

    pfad_prot = os.path.join(a.ziel, 'abrufprotokoll_durchgang%d.json' % a.durchgang)
    with open(pfad_prot, 'w', encoding='utf-8') as fh:
        json.dump({'erzeugt_utc': datetime.now(timezone.utc).isoformat(),
                   'quelle': a.nummern or a.csv_datei,
                   'bericht': bericht, 'abrufe': protokoll}, fh,
                  ensure_ascii=False, indent=1)

    erfolg = sum(1 for s in protokoll if s.get('gespeichert'))
    print('')
    print('Erfolgreich gesichert: %d von %d' % (erfolg, len(protokoll)))
    print('Protokoll: %s' % pfad_prot)
    print('')
    print('Bitte den gesamten Ordner "%s" zurueckgeben, damit die' % a.ziel)
    print('Auswertung erfolgen kann.')


if __name__ == '__main__':
    main()
