"""Align scene-plan lyric lines to the STT word timestamps and write timeline.json."""
import json, re, sys, difflib

STT, PLAN, LYRICS, OUT = sys.argv[1:5]

NUM = {'53': 'fifty three', '30': 'thirty', '60': 'sixty', '2': 'two', '3': 'three', '4': 'four', '5': 'five'}


def norm(text):
    text = text.lower().replace('-', ' ').replace('fa lu na ra', 'falunara')
    toks = []
    for w in re.findall(r"[a-z0-9']+", text):
        toks += NUM.get(w, w).split()
    return [t.replace("'", '') for t in toks]


stt = json.load(open(STT))
swords = []
for w in stt['words']:
    for t in norm(w['word']):
        swords.append((t, w['start'], w['end']))

lyric_lines = [l.strip() for l in open(LYRICS) if l.strip() and not l.startswith('[')]
ltoks, owner = [], []
for i, line in enumerate(lyric_lines):
    for t in norm(line):
        ltoks.append(t)
        owner.append(i)

sm = difflib.SequenceMatcher(a=ltoks, b=[w[0] for w in swords], autojunk=False)
tok_time = [None] * len(ltoks)
for a, b, n in sm.get_matching_blocks():
    for k in range(n):
        tok_time[a + k] = (swords[b + k][1], swords[b + k][2])

line_start, line_end = [], []
for i in range(len(lyric_lines)):
    ts = [tok_time[j] for j in range(len(ltoks)) if owner[j] == i and tok_time[j]]
    line_start.append(ts[0][0] if ts else None)
    line_end.append(ts[-1][1] if ts else None)

# fill unmatched lines by linear interpolation between neighbours
known = [i for i, s in enumerate(line_start) if s is not None]
for i in range(len(lyric_lines)):
    if line_start[i] is None:
        prev = max([k for k in known if k < i], default=None)
        nxt = min([k for k in known if k > i], default=None)
        if prev is not None and nxt is not None:
            frac = (i - prev) / (nxt - prev)
            line_start[i] = line_start[prev] + frac * (line_start[nxt] - line_start[prev])
        elif prev is not None:
            line_start[i] = line_end[prev] + 0.5
        line_end[i] = line_end[i] or line_start[i] + 2.0

scenes = []
for row in open(PLAN):
    cells = [c.strip() for c in row.strip().strip('|').split('|')]
    if len(cells) < 6 or not re.match(r'^\d+[a-z]?$', cells[0]):
        continue
    scenes.append({'id': cells[0], 'lyric': cells[1], 'desc': cells[3], 'chars': cells[4], 'mood': cells[5]})

key = [' '.join(norm(l)) for l in lyric_lines]
for s in scenes:
    first = ' '.join(norm(s['lyric'].split('/')[0]))
    idx = next(i for i, k in enumerate(key) if k == first)
    s['line_idx'] = idx

for i, s in enumerate(scenes):
    s['start'] = 0.0 if i == 0 else round(line_start[s['line_idx']], 2)
for i, s in enumerate(scenes):
    s['end'] = round(scenes[i + 1]['start'] if i + 1 < len(scenes) else stt['duration'], 2)
    s['dur'] = round(s['end'] - s['start'], 2)

subs = [{'text': lyric_lines[i], 'start': round(line_start[i], 2), 'end': round(line_end[i], 2)} for i in range(len(lyric_lines))]
json.dump({'duration': stt['duration'], 'scenes': scenes, 'subtitles': subs}, open(OUT, 'w'), indent=1)
matched = sum(1 for t in tok_time if t)
print(f'tokens matched {matched}/{len(ltoks)}  scenes {len(scenes)}  unmatched lines {len(lyric_lines) - len(known)}')
for s in scenes:
    print(f"{s['id']:>4} {s['start']:7.2f} {s['dur']:5.2f}  {s['lyric'][:60]}")
