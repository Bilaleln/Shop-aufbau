#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Punkt 1 - Bestandsaufnahme des Shopify-Bestellexports.

Grundsaetze:
  * Es wird nichts geschaetzt und nichts ergaenzt. Fehlende oder leere Spalten
    werden als solche ausgewiesen.
  * Der Shopify-Export enthaelt eine Zeile je Line-Item. Kopfdaten (Summen,
    Status, Adressen) stehen nur in der ersten Zeile einer Bestellung.
    Es wird daher zuerst auf Bestellebene aggregiert und erst danach summiert.
  * Betraege werden je Waehrung getrennt gefuehrt. Es findet KEINE
    Waehrungsumrechnung statt.

Aufruf:  python3 bestandsaufnahme.py <orders_export.csv> [ausgabeverzeichnis]
"""

import csv
import json
import os
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from datetime import datetime, timedelta, timezone

csv.field_size_limit(10 * 1024 * 1024)

# ---------------------------------------------------------------- Hilfsmittel

def norm(s):
    """Spaltennamen vergleichbar machen: klein, ohne Sonder-/Leerzeichen."""
    return re.sub(r'[^a-z0-9]', '', (s or '').lower())


class Spalten:
    """Loest logische Feldnamen auf die tatsaechlichen Kopfzeilen des Exports auf."""

    # logischer Name -> Liste moeglicher Kopfzeilen (in Prioritaetsreihenfolge)
    KANDIDATEN = OrderedDict([
        ('bestellnummer',    ['Name', 'Order', 'Order Name']),
        ('id',               ['Id', 'Order ID']),
        ('email',            ['Email', 'Contact Email', 'Customer Email']),
        ('erstellt',         ['Created at', 'Created At']),
        ('bezahlt_am',       ['Paid at', 'Paid At']),
        ('fulfilled_am',     ['Fulfilled at', 'Fulfilled At']),
        ('storniert_am',     ['Cancelled at', 'Canceled at']),
        ('financial_status', ['Financial Status']),
        ('fulfillment_status', ['Fulfillment Status']),
        ('waehrung',         ['Currency']),
        ('summe',            ['Total']),
        ('zwischensumme',    ['Subtotal']),
        ('versandkosten',    ['Shipping']),
        ('steuern',          ['Taxes']),
        ('rabattbetrag',     ['Discount Amount']),
        ('rabattcode',       ['Discount Code']),
        ('erstattet',        ['Refunded Amount']),
        ('ausstehend',       ['Outstanding Balance']),
        ('zahlungsart',      ['Payment Method']),
        ('zahlungsreferenz', ['Payment Reference', 'Payment References']),
        ('risk',             ['Risk Level']),
        ('quelle',           ['Source']),
        ('tags',             ['Tags']),
        ('notiz',            ['Notes', 'Note']),
        ('telefon',          ['Phone']),
        ('versand_land',     ['Shipping Country']),
        ('rechnung_land',    ['Billing Country']),
        ('versand_name',     ['Shipping Name']),
        ('rechnung_name',    ['Billing Name']),
        ('versand_strasse',  ['Shipping Street', 'Shipping Address1']),
        ('versand_adresse1', ['Shipping Address1']),
        ('versand_adresse2', ['Shipping Address2']),
        ('versand_plz',      ['Shipping Zip']),
        ('versand_ort',      ['Shipping City']),
        ('versand_telefon',  ['Shipping Phone']),
        ('rechnung_telefon', ['Billing Phone']),
        ('versandart',       ['Shipping Method']),
        ('lineitem_menge',   ['Lineitem quantity']),
        ('lineitem_name',    ['Lineitem name']),
        ('lineitem_preis',   ['Lineitem price']),
        ('lineitem_sku',     ['Lineitem sku']),
        ('lineitem_fulfillment', ['Lineitem fulfillment status']),
        ('vendor',           ['Vendor']),
    ])

    def __init__(self, kopfzeile):
        self.kopfzeile = kopfzeile
        self._map = {}
        vorhanden = {norm(h): h for h in kopfzeile}
        for logisch, kandidaten in self.KANDIDATEN.items():
            for k in kandidaten:
                if norm(k) in vorhanden:
                    self._map[logisch] = vorhanden[norm(k)]
                    break

    def hat(self, logisch):
        return logisch in self._map

    def real(self, logisch):
        return self._map.get(logisch)

    def get(self, zeile, logisch, default=''):
        sp = self._map.get(logisch)
        if sp is None:
            return default
        wert = zeile.get(sp, default)
        return wert if wert is not None else default

    def fehlend(self):
        return [l for l in self.KANDIDATEN if l not in self._map]

    def unbekannte_kopfzeilen(self):
        belegt = set(norm(v) for v in self._map.values())
        return [h for h in self.kopfzeile if norm(h) not in belegt]


def zahl(wert):
    """'1'234.50', '1 234,50', '12.90' -> float. Leer/unparsbar -> None."""
    if wert is None:
        return None
    s = str(wert).strip()
    if s == '':
        return None
    s = s.replace('’', '').replace("'", '').replace('\xa0', '').replace(' ', '')
    if ',' in s and '.' in s:
        if s.rfind(',') > s.rfind('.'):      # 1.234,50
            s = s.replace('.', '').replace(',', '.')
        else:                                 # 1,234.50
            s = s.replace(',', '')
    elif ',' in s:
        s = s.replace(',', '.')
    try:
        return float(s)
    except ValueError:
        return None


ZEIT_FORMATE = [
    '%Y-%m-%d %H:%M:%S %z',
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%dT%H:%M:%S%z',
    '%Y-%m-%dT%H:%M:%S',
    '%Y-%m-%d %H:%M',
    '%d.%m.%Y %H:%M:%S',
    '%d.%m.%Y %H:%M',
]


def zeit(wert):
    """Shopify-Zeitstempel -> timezone-bewusstes datetime. Unparsbar -> None."""
    if wert is None:
        return None
    s = str(wert).strip()
    if s == '':
        return None
    s2 = re.sub(r'(?<=[+-]\d{2}):(?=\d{2}$)', '', s)   # +02:00 -> +0200
    if s2.endswith('Z'):
        s2 = s2[:-1] + '+0000'
    for f in ZEIT_FORMATE:
        try:
            dt = datetime.strptime(s2, f)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            continue
    return None


MEZ = timezone(timedelta(hours=1))
MESZ = timezone(timedelta(hours=2))


def mitteleuropaeisch(dt):
    """Nach mitteleuropaeischer Zeit umrechnen (Sommerzeit Ende Maerz - Ende Oktober).
    Rueckgabe: (datetime, Kuerzel)."""
    if dt is None:
        return (None, '')
    utc = dt.astimezone(timezone.utc)
    jahr = utc.year
    # letzter Sonntag im Maerz, 01:00 UTC
    d = datetime(jahr, 3, 31, 1, 0, tzinfo=timezone.utc)
    while d.weekday() != 6:
        d -= timedelta(days=1)
    # letzter Sonntag im Oktober, 01:00 UTC
    e = datetime(jahr, 10, 31, 1, 0, tzinfo=timezone.utc)
    while e.weekday() != 6:
        e -= timedelta(days=1)
    if d <= utc < e:
        return (utc.astimezone(MESZ), 'MESZ')
    return (utc.astimezone(MEZ), 'MEZ')


def f2(x):
    return '-' if x is None else ('%.2f' % x)


def median(werte):
    w = sorted(v for v in werte if v is not None)
    if not w:
        return None
    n = len(w)
    return w[n // 2] if n % 2 else (w[n // 2 - 1] + w[n // 2]) / 2.0


# ------------------------------------------------------------------- Einlesen

def einlesen(pfad):
    """Liest den Export und aggregiert auf Bestellebene.
    Rueckgabe: (bestellungen als OrderedDict, spalten, statistik)"""
    with open(pfad, 'r', encoding='utf-8-sig', newline='') as fh:
        probe = fh.read(64 * 1024)
        fh.seek(0)
        try:
            dialekt = csv.Sniffer().sniff(probe, delimiters=',;\t')
        except csv.Error:
            dialekt = csv.excel
        leser = csv.DictReader(fh, dialect=dialekt)
        kopfzeile = leser.fieldnames or []
        sp = Spalten(kopfzeile)
        if not sp.hat('bestellnummer') and not sp.hat('id'):
            raise SystemExit(
                'ABBRUCH: Der Export enthaelt weder eine Spalte "Name" noch "Id".\n'
                'Ohne Bestellkennung ist keine Aggregation auf Bestellebene moeglich.\n'
                'Gefundene Spalten: ' + ', '.join(kopfzeile))

        schluesselfeld = 'bestellnummer' if sp.hat('bestellnummer') else 'id'
        bestellungen = OrderedDict()
        zeilen_gesamt = 0
        zeilen_ohne_schluessel = 0
        letzter_schluessel = None

        for zeile in leser:
            zeilen_gesamt += 1
            schluessel = str(sp.get(zeile, schluesselfeld)).strip()
            if schluessel == '':
                # Fortsetzungszeile ohne wiederholte Bestellnummer
                if letzter_schluessel is None:
                    zeilen_ohne_schluessel += 1
                    continue
                schluessel = letzter_schluessel
            letzter_schluessel = schluessel

            if schluessel not in bestellungen:
                bestellungen[schluessel] = {
                    'schluessel': schluessel, 'kopf': {}, 'zeilen': 0, 'positionen': [],
                }
            b = bestellungen[schluessel]
            b['zeilen'] += 1

            # Kopfdaten: erster nicht-leerer Wert je Feld gewinnt
            for logisch in Spalten.KANDIDATEN:
                if logisch.startswith('lineitem'):
                    continue
                wert = str(sp.get(zeile, logisch)).strip()
                if wert != '' and logisch not in b['kopf']:
                    b['kopf'][logisch] = wert

            b['positionen'].append({
                'name':  str(sp.get(zeile, 'lineitem_name')).strip(),
                'menge': zahl(sp.get(zeile, 'lineitem_menge')),
                'preis': zahl(sp.get(zeile, 'lineitem_preis')),
                'sku':   str(sp.get(zeile, 'lineitem_sku')).strip(),
                'ff':    str(sp.get(zeile, 'lineitem_fulfillment')).strip(),
            })

    statistik = {
        'zeilen_gesamt': zeilen_gesamt,
        'zeilen_ohne_schluessel': zeilen_ohne_schluessel,
        'schluesselfeld': sp.real(schluesselfeld),
    }
    return bestellungen, sp, statistik


def nummernluecken(schluessel_liste):
    """Extrahiert die laufende Nummer aus '#1234' und sucht Luecken."""
    paare = []
    for s in schluessel_liste:
        m = re.search(r'(\d+)\s*$', s)
        if m:
            paare.append((int(m.group(1)), s))
    if not paare:
        return None
    nummern = sorted(n for n, _ in paare)
    vorhanden = set(nummern)
    luecken = []
    start, ende = nummern[0], nummern[-1]
    lauf = None
    for n in range(start, ende + 1):
        if n not in vorhanden:
            if lauf is None:
                lauf = [n, n]
            else:
                lauf[1] = n
        else:
            if lauf is not None:
                luecken.append(tuple(lauf))
                lauf = None
    if lauf is not None:
        luecken.append(tuple(lauf))
    doppelt = [n for n, c in Counter(n for n, _ in paare).items() if c > 1]
    return {
        'kleinste': start, 'groesste': ende,
        'spanne': ende - start + 1,
        'vorhanden': len(vorhanden),
        'fehlend_gesamt': sum(b - a + 1 for a, b in luecken),
        'luecken': luecken,
        'doppelte_nummern': sorted(doppelt),
    }


# ----------------------------------------------------------------- Auswertung

def auswerten(bestellungen, sp):
    """Verdichtet die Bestellebene zu Kennzahlen. Keine Schaetzungen."""
    e = {
        'anzahl': len(bestellungen),
        'je_waehrung': defaultdict(lambda: {'anzahl': 0, 'summe': 0.0, 'werte': [],
                                            'erstattet': 0.0, 'erstattet_bekannt': 0}),
        'ohne_betrag': [], 'ohne_waehrung': [], 'ohne_datum': [],
        'zahlungsart': defaultdict(lambda: defaultdict(lambda: {'anzahl': 0, 'summe': 0.0})),
        'zahlungsart_leer': 0,
        'financial': Counter(), 'fulfillment': Counter(), 'risk': Counter(),
        'land': Counter(), 'land_quelle': Counter(),
        'storniert': 0, 'daten': [],
    }

    for b in bestellungen.values():
        k = b['kopf']
        waehrung = k.get('waehrung', '')
        betrag = zahl(k.get('summe'))
        erstattet = zahl(k.get('erstattet'))

        if waehrung == '':
            e['ohne_waehrung'].append(b['schluessel'])
            waehrung = '(keine Angabe)'
        if betrag is None:
            e['ohne_betrag'].append(b['schluessel'])

        w = e['je_waehrung'][waehrung]
        w['anzahl'] += 1
        if betrag is not None:
            w['summe'] += betrag
            w['werte'].append(betrag)
        if sp.hat('erstattet'):
            if erstattet is not None:
                w['erstattet'] += erstattet
                w['erstattet_bekannt'] += 1

        za = k.get('zahlungsart', '')
        if za == '':
            e['zahlungsart_leer'] += 1
            za = '(keine Angabe)'
        z = e['zahlungsart'][za][waehrung]
        z['anzahl'] += 1
        if betrag is not None:
            z['summe'] += betrag

        e['financial'][k.get('financial_status', '') or '(leer)'] += 1
        e['fulfillment'][k.get('fulfillment_status', '') or '(leer)'] += 1
        e['risk'][k.get('risk', '') or '(leer)'] += 1

        land = k.get('versand_land', '')
        if land:
            e['land_quelle']['Shipping Country'] += 1
        else:
            land = k.get('rechnung_land', '')
            if land:
                e['land_quelle']['Billing Country (Ersatz)'] += 1
        e['land'][land or '(leer)'] += 1

        if k.get('storniert_am'):
            e['storniert'] += 1

        d = zeit(k.get('erstellt'))
        if d is None:
            e['ohne_datum'].append(b['schluessel'])
        else:
            e['daten'].append(d)

    return e


def markdown(pfad_csv, bestellungen, sp, statistik, e, luecken):
    z = []
    A = z.append
    A('# Punkt 1 - Bestandsaufnahme des Bestellexports')
    A('')
    A('Quelldatei: `%s`' % os.path.basename(pfad_csv))
    A('')
    A('Alle Zahlen sind aus dem Export berechnet. Es wurde nichts geschaetzt, '
      'nichts ergaenzt und keine Waehrung umgerechnet.')
    A('')

    # --- Datengrundlage
    A('## 1.1 Datengrundlage')
    A('')
    A('| Kennzahl | Wert |')
    A('|---|---|')
    A('| Zeilen im Export (ohne Kopfzeile) | %d |' % statistik['zeilen_gesamt'])
    A('| Eindeutige Bestellungen | **%d** |' % e['anzahl'])
    A('| Bestellkennung aus Spalte | `%s` |' % statistik['schluesselfeld'])
    if statistik['zeilen_ohne_schluessel']:
        A('| Zeilen ohne zuordenbare Bestellkennung (verworfen) | %d |'
          % statistik['zeilen_ohne_schluessel'])
    A('')
    fehlend = sp.fehlend()
    if fehlend:
        A('**Im Export nicht enthaltene Spalten** (die betreffenden Auswertungen '
          'entfallen ersatzlos, es wird nichts geschaetzt):')
        A('')
        for l in fehlend:
            A('- `%s` (erwartet als "%s")' % (l, Spalten.KANDIDATEN[l][0]))
        A('')
    unbekannt = sp.unbekannte_kopfzeilen()
    if unbekannt:
        A('Weitere Spalten im Export, die fuer diese Auswertung nicht verwendet wurden: '
          + ', '.join('`%s`' % u for u in unbekannt))
        A('')

    # --- Umsatz
    A('## 1.2 Bestellungen, Umsatz, Zeitraum')
    A('')
    A('| Waehrung | Bestellungen | Umsatz | Mittelwert | Median | kleinste | groesste |')
    A('|---|---:|---:|---:|---:|---:|---:|')
    for waehrung, w in sorted(e['je_waehrung'].items(), key=lambda x: -x[1]['summe']):
        werte = w['werte']
        A('| %s | %d | %s | %s | %s | %s | %s |' % (
            waehrung, w['anzahl'], f2(w['summe']),
            f2(w['summe'] / len(werte)) if werte else '-',
            f2(median(werte)),
            f2(min(werte)) if werte else '-',
            f2(max(werte)) if werte else '-'))
    A('')
    if len(e['je_waehrung']) > 1:
        A('> **Achtung:** Der Export enthaelt mehrere Waehrungen. Die Betraege wurden '
          'bewusst NICHT zu einer Gesamtsumme addiert, weil dafuer ein Wechselkurs '
          'noetig waere, der nicht im Export steht. Fuer die Akte muss der Kurs zum '
          'jeweiligen Buchungstag belegt werden.')
        A('')
    if e['ohne_betrag']:
        A('Bestellungen ohne Betragsangabe (%d): %s' % (
            len(e['ohne_betrag']), ', '.join(e['ohne_betrag'][:20])
            + (' ...' if len(e['ohne_betrag']) > 20 else '')))
        A('')

    if e['daten']:
        ersteM, ek = mitteleuropaeisch(min(e['daten']))
        letzteM, lk = mitteleuropaeisch(max(e['daten']))
        A('| Zeitraum | Zeitstempel im Export | mitteleuropaeisch |')
        A('|---|---|---|')
        A('| Erster Bestelleingang | %s | %s %s |'
          % (min(e['daten']).isoformat(), ersteM.strftime('%d.%m.%Y %H:%M:%S'), ek))
        A('| Letzter Bestelleingang | %s | %s %s |'
          % (max(e['daten']).isoformat(), letzteM.strftime('%d.%m.%Y %H:%M:%S'), lk))
        A('| Spanne | %d Tage | |' % ((max(e['daten']) - min(e['daten'])).days))
        A('')
    if e['ohne_datum']:
        A('Bestellungen ohne lesbares Bestelldatum: %d (%s)' % (
            len(e['ohne_datum']), ', '.join(e['ohne_datum'][:20])))
        A('')

    # --- Zahlungsarten
    A('## 1.3 Zahlungsarten')
    A('')
    if not sp.hat('zahlungsart'):
        A('Die Spalte "Payment Method" ist im Export nicht vorhanden. '
          'Eine Aufschluesselung nach Zahlungsart ist aus dieser Datei nicht moeglich.')
    else:
        A('| Zahlungsart | Waehrung | Bestellungen | Umsatz | Anteil an Bestellungen |')
        A('|---|---|---:|---:|---:|')
        geordnet = sorted(e['zahlungsart'].items(),
                          key=lambda x: -sum(v['summe'] for v in x[1].values()))
        for za, je_w in geordnet:
            for waehrung, v in sorted(je_w.items(), key=lambda x: -x[1]['summe']):
                A('| %s | %s | %d | %s | %.1f %% |' % (
                    za, waehrung, v['anzahl'], f2(v['summe']),
                    100.0 * v['anzahl'] / e['anzahl'] if e['anzahl'] else 0))
        A('')
        A('Die Werte stammen unveraendert aus der Spalte "Payment Method". '
          'Welche dieser Bezeichnungen technisch ueber Shopify Payments abgewickelt '
          'wurden, laesst sich aus dem Bestellexport allein nicht abschliessend '
          'feststellen - dafuer ist der Payouts-/Transaktionsexport noetig. '
          'Siehe Punkt 3.')
        A('')

    # --- Statusverteilungen
    A('## 1.4 Status, Risiko, Land')
    A('')
    for titel, zaehler, spalte in [
            ('Financial Status', e['financial'], 'financial_status'),
            ('Fulfillment Status', e['fulfillment'], 'fulfillment_status'),
            ('Risk Level', e['risk'], 'risk'),
            ('Land', e['land'], 'versand_land')]:
        A('### %s' % titel)
        A('')
        if not sp.hat(spalte) and titel != 'Land':
            A('Spalte im Export nicht vorhanden - keine Auswertung moeglich.')
            A('')
            continue
        A('| Wert | Bestellungen | Anteil |')
        A('|---|---:|---:|')
        for wert, n in zaehler.most_common():
            A('| %s | %d | %.1f %% |' % (wert, n, 100.0 * n / e['anzahl'] if e['anzahl'] else 0))
        A('')
    if e['land_quelle']:
        A('Herkunft der Landangabe: ' + ', '.join(
            '%s: %d' % (k, v) for k, v in e['land_quelle'].items()))
        A('')

    # --- Erstattungen
    A('## 1.5 Erstattungen und offene Salden')
    A('')
    if not sp.hat('erstattet'):
        A('Die Spalte "Refunded Amount" ist im Export nicht vorhanden. '
          'Bereits erstattete Betraege koennen aus dieser Datei nicht ermittelt werden.')
    else:
        A('| Waehrung | Umsatz | erstattet | offen (Umsatz minus erstattet) |')
        A('|---|---:|---:|---:|')
        for waehrung, w in sorted(e['je_waehrung'].items(), key=lambda x: -x[1]['summe']):
            A('| %s | %s | %s | %s |' % (waehrung, f2(w['summe']),
                                         f2(w['erstattet']), f2(w['summe'] - w['erstattet'])))
        A('')
        A('"Offen" ist hier rein rechnerisch Umsatz minus ausgewiesener Erstattung. '
          'Das ist keine Aussage darueber, ob ein Betrag tatsaechlich noch auf dem '
          'Merchant-Konto liegt - Auszahlungen und Rueckbuchungen stehen im '
          'Payouts-Export, nicht hier.')
        A('')
    if e['storniert']:
        A('Bestellungen mit gesetztem Stornodatum ("Cancelled at"): %d' % e['storniert'])
        A('')

    # --- Nummernlücken
    A('## 1.6 Luecken in der Bestellnummerierung')
    A('')
    if luecken is None:
        A('Aus der Bestellkennung liess sich keine fortlaufende Nummer ableiten. '
          'Keine Lueckenanalyse moeglich.')
    else:
        A('| Kennzahl | Wert |')
        A('|---|---|')
        A('| Kleinste Bestellnummer | %d |' % luecken['kleinste'])
        A('| Groesste Bestellnummer | %d |' % luecken['groesste'])
        A('| Nummernspanne | %d |' % luecken['spanne'])
        A('| Im Export vorhanden | %d |' % luecken['vorhanden'])
        A('| **In der Spanne fehlend** | **%d** |' % luecken['fehlend_gesamt'])
        A('')
        if luecken['luecken']:
            A('Fehlende Nummern im Einzelnen:')
            A('')
            A('| Luecke | Anzahl |')
            A('|---|---:|')
            for a, bb in luecken['luecken']:
                A('| %s | %d |' % (('%d' % a) if a == bb else '%d bis %d' % (a, bb), bb - a + 1))
            A('')
            A('**Was das bedeutet:** Shopify vergibt Bestellnummern fortlaufend. '
              'Eine fehlende Nummer heisst, dass zu dieser Nummer einmal eine Bestellung '
              'existierte, die im Export nicht mehr auftaucht. Moegliche Ursachen: die '
              'Bestellung wurde geloescht, sie liegt ausserhalb des exportierten '
              'Zeitraums oder Filters, oder es war ein abgebrochener Bestellversuch. '
              'Welcher Fall vorliegt, laesst sich aus dieser Datei nicht entscheiden - '
              'das muss ueber das Shopify-Aktivitaetsprotokoll geklaert werden.')
            A('')
        else:
            A('Keine Luecken - die Nummerierung ist im vorhandenen Bereich vollstaendig.')
            A('')
        if luecken['doppelte_nummern']:
            A('Mehrfach vergebene Nummern: %s' % ', '.join(str(x) for x in luecken['doppelte_nummern']))
            A('')

    # --- Abgleich mit der Schätzung
    A('## 1.7 Abgleich mit der Schaetzung (165 Bestellungen / rund 18.000 EUR)')
    A('')
    A('| | Schaetzung | Export | Abweichung |')
    A('|---|---:|---:|---:|')
    A('| Bestellungen | 165 | %d | %+d |' % (e['anzahl'], e['anzahl'] - 165))
    for waehrung, w in sorted(e['je_waehrung'].items(), key=lambda x: -x[1]['summe']):
        A('| Umsatz %s | 18000.00 | %s | %s |' % (waehrung, f2(w['summe']),
                                                  f2(w['summe'] - 18000.0)))
    A('')
    A('Der Umsatzvergleich ist nur dann direkt aussagekraeftig, wenn die Waehrung des '
      'Exports auch die Waehrung der Schaetzung ist. Bei abweichender Waehrung ist die '
      'Zeile "Abweichung" ohne belegten Wechselkurs nicht zu verwenden.')
    A('')
    return '\n'.join(z) + '\n'


def main():
    if len(sys.argv) < 2:
        raise SystemExit('Aufruf: python3 bestandsaufnahme.py <orders_export.csv> [ausgabeverzeichnis]')
    pfad = sys.argv[1]
    ausgabe = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.getcwd(), 'analyse')
    os.makedirs(ausgabe, exist_ok=True)

    bestellungen, sp, statistik = einlesen(pfad)
    e = auswerten(bestellungen, sp)
    luecken = nummernluecken(list(bestellungen.keys()))

    md = markdown(pfad, bestellungen, sp, statistik, e, luecken)
    ziel_md = os.path.join(ausgabe, 'bestandsaufnahme.md')
    with open(ziel_md, 'w', encoding='utf-8') as fh:
        fh.write(md)

    # Zwischenstand maschinenlesbar sichern, damit die Punkte 2-7 darauf aufsetzen
    ziel_json = os.path.join(ausgabe, 'tools', 'bestellungen.json')
    os.makedirs(os.path.dirname(ziel_json), exist_ok=True)
    with open(ziel_json, 'w', encoding='utf-8') as fh:
        json.dump({'quelle': os.path.abspath(pfad), 'statistik': statistik,
                   'spalten_vorhanden': {l: sp.real(l) for l in Spalten.KANDIDATEN if sp.hat(l)},
                   'spalten_fehlend': sp.fehlend(),
                   'bestellungen': [{'schluessel': b['schluessel'], 'kopf': b['kopf'],
                                     'zeilen': b['zeilen'], 'positionen': b['positionen']}
                                    for b in bestellungen.values()]},
                  fh, ensure_ascii=False, indent=1)

    print(md)
    print('Geschrieben: %s' % ziel_md)
    print('Geschrieben: %s' % ziel_json)


if __name__ == '__main__':
    main()
