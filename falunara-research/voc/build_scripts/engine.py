import re, csv
from collections import Counter
from norm import load, MAP

D = load()
BYID = {r['VOC ID']: r for r in D}
CORE = [r for r in D if 'possible_seeding' not in r['flags']]
RANK = {'high': 0, 'medium': 1, 'low': 2}

# ---------- selector helpers ----------
def T(*tags):
    s = set(tags)
    return lambda r: bool(s & set(r['tags']))
def C(*cats):
    s = set(cats)
    return lambda r: r['Category'] in s
def RX(p):
    rx = re.compile(p, re.I)
    return lambda r: bool(rx.search(r['Exact short quote']))
def B(*areas):
    s = set(areas)
    return lambda r: r['Body area'] in s
def F(flag):
    return lambda r: flag in r['flags']
def AND(*fs): return lambda r: all(f(r) for f in fs)
def OR(*fs): return lambda r: any(f(r) for f in fs)
def NOT(f): return lambda r: not f(r)

PROB = 'Problem descriptions'; SYM = 'Symptoms / visible texture descriptions'; TAC = 'Tactile descriptions'
EMO = 'Emotional reactions'; SIT = 'Situational triggers'; DES = 'Desired outcomes'; FAIL = 'Failed attempts'
SUCC = 'Successful attempts'; PREF = 'Product / routine preferences'; OBJ = 'Objections'; SKEP = 'Skepticism'
PUR = 'Purchase criteria'; ING = 'Ingredient / mechanism beliefs'; TIME = 'Time-to-result expectations'
FRIC = 'Routine friction'; IDN = 'Identity / social implications'; PHR = 'Exact phrases / metaphors / repeated wording'
QUE = 'Questions customers repeatedly ask'

# ---------- stats ----------
def sel(f, base=None):
    return [r for r in (CORE if base is None else base) if f(r)]

def nmk(rows):
    return len(rows), len({r['Corpus ID'] for r in rows}), len({r['Community'] for r in rows})

def rec(rows):
    n, m, k = nmk(rows)
    return f"{n} rows / {m} threads / {k} communities"

def label(rows):
    m = len({r['Corpus ID'] for r in rows})
    if m >= 20: return 'stark wiederkehrend'
    if m >= 8: return 'wiederkehrend'
    if m >= 3: return 'begrenzt wiederkehrend'
    return 'isoliert'

def conf(rows):
    n, m, k = nmk(rows)
    hi = sum(r['Evidence strength'] == 'high' for r in rows)
    if m >= 15 and k >= 4: return 'hoch'
    if m >= 6 and k >= 2: return 'mittel'
    return 'niedrig'

def sens(f):
    allr = [r for r in D if f(r)]
    core = [r for r in allr if 'possible_seeding' not in r['flags']]
    seed = len(allr) - len(core)
    strict = [r for r in core if not ({'non_us_signal', 'under_40_signal'} & set(r['flags']))]
    hrt = sum('hrt_medical_context' in r['flags'] for r in core)
    nonus = sum('non_us_signal' in r['flags'] for r in core)
    u40 = sum('under_40_signal' in r['flags'] for r in core)
    hi = sum(r['Evidence strength'] == 'high' for r in core)
    n2, m2, k2 = nmk(strict)
    return (f"Seeding ausgeschlossen: {seed} | ohne non_US/U40: {n2} rows / {m2} threads | "
            f"non_US {nonus}, U40 {u40}, HRT-Kontext {hrt} | high-Evidenz {hi}/{len(core)}")

def q(i, maxlen=None):
    r = BYID[i]
    s = r['Exact short quote']
    return f"„{s}“ ({i})"

def url(i): return BYID[i]['Source URL']

def srcs(ids):
    return '\n'.join(f"{i}: {url(i)}" for i in ids)

def pick(rows, n=4, exclude=()):
    seen = Counter(); out = []
    for r in sorted(rows, key=lambda r: (RANK[r['Evidence strength']], len(r['flags']), abs(len(r['Exact short quote']) - 90))):
        if r['VOC ID'] in exclude or seen[r['Corpus ID']]: continue
        seen[r['Corpus ID']] += 1; out.append(r['VOC ID'])
        if len(out) >= n: break
    return out

WARN = []
def examples(item, rows):
    ids = item.get('ex') or []
    rid = {r['VOC ID'] for r in rows}
    for i in ids:
        if i not in BYID: raise SystemExit(f"unknown id {i}")
        if i not in rid: WARN.append(f"{item['name'][:40]}: example {i} not in selector set")
    if len(ids) < 2:
        ids = ids + pick(rows, 4 - len(ids), exclude=ids)
    return ids

def ids_str(rows):
    return ', '.join(r['VOC ID'] for r in rows)
