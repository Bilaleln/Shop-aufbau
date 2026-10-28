"""Cut all scene clips to the song timeline, add the song and burn in lyric subtitles.

Usage: python3 assemble.py [output.mp4]
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'falunara_singing_ad.mp4')
WORK = os.path.join(HERE, 'build')
W, H, FPS = 1080, 1920, 30

plan = json.load(open(os.path.join(HERE, 'production_plan.json')))
state = json.load(open(os.path.join(HERE, 'prod_state.json')))
timeline = json.load(open(os.path.join(HERE, 'timeline.json')))
os.makedirs(WORK, exist_ok=True)


def probe_dur(path):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                          '-of', 'csv=p=0', path]).decode().strip())


segments = []
for s in plan:
    src = os.path.join(HERE, s['fixed'] if 'fixed' in s else state[s['id']]['vid_path'])
    have = probe_dur(src) - 0.05
    slow = max(1.0, s['dur'] / have)
    seg = os.path.join(WORK, f"seg_{s['id']}.mp4")
    vf = (f'setpts={slow:.4f}*PTS,scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,'
          f'crop={W}:{H},fps={FPS},format=yuv420p')
    if not (os.path.exists(seg) and os.path.getmtime(seg) > os.path.getmtime(src)):
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-t', f"{s['dur']:.3f}", '-vf', vf, '-an',
                        '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', seg + '.tmp.mp4'], check=True)
        os.replace(seg + '.tmp.mp4', seg)
    segments.append(seg)
    print(f"{s['id']:>4} {s['dur']:5.2f}s  src {have:.2f}s  slow x{slow:.3f}", flush=True)

with open(os.path.join(WORK, 'concat.txt'), 'w') as f:
    f.writelines(f"file '{p}'\n" for p in segments)


def ts(t):
    h, rem = divmod(max(t, 0), 3600)
    m, sec = divmod(rem, 60)
    return f'{int(h)}:{int(m):02d}:{sec:05.2f}'


subs = timeline['subtitles']
events = []
for i, sub in enumerate(subs):
    nxt = subs[i + 1]['start'] if i + 1 < len(subs) else timeline['duration']
    end = min(max(sub['end'] + 0.35, sub['start'] + 1.0), nxt - 0.05)
    text = sub['text'].replace('Fa-lu-NA-ra', 'Falunara')
    events.append(f"Dialogue: 0,{ts(sub['start'])},{ts(end)},Lyric,,0,0,0,,{text}")

# MarginV keeps the text inside the 4:5 safe zone (central 1350 px of the 1920 px frame)
ass = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,Inter ExtraBold,66,&H00FFFFFF,&H00FFFFFF,&H00202020,&H64000000,0,0,0,0,100,100,0,0,1,5,2,2,90,90,330,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + '\n'.join(events) + '\n'
ass_path = os.path.join(WORK, 'lyrics.ass')
open(ass_path, 'w').write(ass)

total = timeline['duration']
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', os.path.join(WORK, 'concat.txt'),
                '-i', os.path.join(HERE, 'song_variant_1.mp3'),
                '-vf', f"ass={ass_path},fade=t=in:st=0:d=0.4,fade=t=out:st={total - 1.2:.2f}:d=1.2",
                '-af', f'afade=t=out:st={total - 1.5:.2f}:d=1.5',
                '-map', '0:v', '-map', '1:a', '-t', f'{total:.3f}',
                '-c:v', 'libx264', '-preset', 'slow', '-crf', '21', '-maxrate', '3M', '-bufsize', '6M',
                '-profile:v', 'high', '-pix_fmt', 'yuv420p',
                '-c:a', 'aac', '-b:a', '192k', '-movflags', '+faststart', OUT], check=True)
print('wrote', OUT, f'{probe_dur(OUT):.2f}s')
