"""FALUNARA singing ad: generate start images (Nano Banana Pro) and clips (Veo 3.1 Fast) per scene.

Usage: python3 production.py plan|images|videos [scene ids...]
State is kept in prod_state.json so reruns never pay twice for a finished scene.
"""
import json, os, sys, time, ssl, urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = 'https://raw.githubusercontent.com/Bilaleln/Shop-aufbau/claude/intelligent-galileo-n26o8k/singing-ad/'
CTX = ssl.create_default_context(cafile='/root/.ccr/ca-bundle.crt')
STATE = os.path.join(HERE, 'prod_state.json')

REFS = {
    'claire': ('ref_claire.jpeg', 'the character Claire'),
    'claire_bath': ('scene30_pump_start_v2.jpg', 'Claire in her bathroom (style, lighting and location reference)'),
    'lily': ('ref_lily.jpeg', "the character Lily, Claire's daughter"),
    'bottle': ('ref_bottle_pixar_crop.jpg', 'the FALUNARA bottle in the target Pixar style'),
    'bottle_front': ('ref_bottle_front.jpg', 'the real FALUNARA bottle, front view'),
    'bottle_pump': ('ref_bottle_pump_closeup.jpg', 'the real FALUNARA pump head under its transparent cap'),
    'box': ('falunara-product-ref.jpg', 'the real FALUNARA bottle next to its gold box'),
    'dieline': ('ref_box_dieline.jpg', 'the real FALUNARA gold box, all sides'),
}

STYLE = ('Pixar/Disney-style 3D animation still, glossy soft-shaded render, expressive eyes, soft skin textures, '
         'cinematic depth of field, vertical 9:16 frame. Keep faces, hands and key objects within the central 70% '
         'of the image height. No captions, letters, logos or readable text anywhere')
CLAIRE = ('Claire is a 53-year-old woman: keep her face exactly as in the reference - visible fine lines, '
          'shoulder-length soft silver-blonde wavy hair, warm hazel-brown eyes, one small beauty mark on her left '
          'cheekbone. Mouth closed.')
OUTFIT = {
    'day': 'She wears a cream linen blouse, dark navy trousers and small gold stud earrings, hair loose.',
    'robe': 'She wears a soft white terrycloth robe, hair loosely clipped up.',
    'night': 'She wears a light grey cotton pajama top, hair down.',
}
LILY = "Lily is Claire's daughter, about 28, long straight dark brown hair, oversized sage green sweater and jeans; keep her face as in the reference."
BOTTLE = ('The FALUNARA bottle must match the bottle references exactly: tall slim clear glass cylinder full of golden '
          'oil, text printed directly on the glass in dark brown - FALUNARA with a small gold brush stroke below, '
          'BOTANICAL BODY OIL, NOURISH · RESTORE · GLOW, 100 mL - and a compact white stepped pump head with no spout, '
          'covered by a straight transparent cylindrical cap. This label is the only text allowed in the image.')
GENERIC = 'All other bottles and jars are plain and unbranded with no text at all.'

SAD = 'Expression: tired and worried, no smile.'
SOFT = 'Expression: calm, relaxed and content, a soft gentle smile.'

MSTYLE = ('Stylized Pixar 3D animated film, glossy soft cartoon render; keep exactly the art style, characters, '
          'faces and objects of the first frame, not photorealistic. One continuous shot, no cuts. Nobody speaks, '
          'mouths stay closed. No text appears on screen. ')

# id: (start, refs, outfit, extra, image prompt, motion prompt)
S = [
 ('1', 0.0, ['claire'], 'day', SAD, 'Close-up of Claire in her bright kitchen in warm afternoon light, looking down pensively, slightly sad.', 'Very slow push-in. She slowly lowers her gaze and blinks, lost in thought.'),
 ('2', 2.78, ['claire'], 'day', '', "Claire's point of view looking down at her own two hands resting on a kitchen counter: fine lines, dry, dull skin, warm daylight. Only her hands and blouse sleeves visible, no face.", 'Her fingers flex slowly and she turns her hands over, inspecting the dry skin.'),
 ('3', 5.76, ['claire'], 'day', SAD, 'Close-up of Claire\'s face, brow slightly furrowed, eyes troubled, blurred kitchen behind her.', 'Subtle slow head tilt, her eyes narrow with worry. Static camera.'),
 ('4', 8.34, ['claire', 'claire_bath'], 'robe', SAD, 'Side shot of Claire in her bathroom by the mirror, running her right hand along her left forearm; the forearm skin looks dry and dull, like paper.', 'Her right hand slides slowly along her dry forearm, she frowns slightly.'),
 ('5', 11.50, ['claire', 'claire_bath'], 'robe', SAD, 'Low angle: Claire sitting on the edge of a white bathtub, looking down at her shins, which show dry flaky patches. Soft bathroom light.', 'She touches her dry shin with her fingertips and frowns.'),
 ('6', 13.30, ['claire', 'claire_bath'], 'robe', SAD + ' ' + GENERIC, "Bathroom counter close-up: three plain unbranded lotion bottles, Claire's hand in frame pushing them aside, one already tipped over.", 'Her hand pushes the lotion bottles aside in frustration and one tips over.'),
 ('7', 16.94, ['claire'], 'day', SAD, 'Morning bedroom: Claire putting on a cream silk blouse; close on her bent elbow, the rough dry elbow skin catching on the silk sleeve.', 'The silk sleeve snags on her rough elbow as she pulls it on, she winces slightly.'),
 ('9', 22.86, ['claire', 'claire_bath'], 'day', SAD + ' ' + GENERIC, 'Morning in the bathroom, harsh light: Claire hastily pumping a plain unbranded white lotion bottle onto her arm while staring at a phone in her other hand, barely looking.', 'She quickly pumps lotion and smears it on in a hurry, eyes on her phone.'),
 ('10', 25.92, ['claire'], 'day', SAD, 'Claire at her front door grabbing her keys and handbag, rushing out, morning light, slight motion.', 'She grabs the keys and hurries out of the door. Quick motion, static camera.'),
 ('11', 27.78, ['claire'], 'day', 'Expression: tired but loving.', 'Warm nostalgic kitchen with brighter colours: Claire carrying heavy grocery bags, a child\'s backpack hanging on a kitchen chair.', 'She sets the grocery bags on the counter and lets out a tired sigh.'),
 ('12', 29.58, ['claire'], 'day', SAD, 'Claire at the kitchen table with a laptop and stacks of papers, an overflowing laundry basket next to her, busy evening light.', 'She rubs her temple, glances from the laptop to the laundry basket.'),
 ('13', 33.20, ['claire', 'claire_bath'], 'night', SAD, 'Night: Claire standing in her bathroom doorway, looking at herself in the mirror from a distance, dim light.', 'Slow push-in towards her, she exhales tiredly.'),
 ('14', 36.28, ['claire', 'claire_bath'], 'robe', SAD, "Close-up of Claire's reflection in the bathroom mirror, her hand touching her forearm, soft sad lighting.", 'Her fingers trace her forearm slowly, her eyes glisten slightly.'),
 ('15', 41.44, ['claire'], 'day', GENERIC, "Department store: glass shelves with rows of fancy luxury cream jars under cold fluorescent light, Claire's hand reaching for one jar.", 'Her hand reaches in and picks up one of the jars.'),
 ('16', 44.46, [], None, GENERIC, 'Close-up of two hands with cream linen blouse cuffs opening a glossy, expensive-looking generic white luxury cream jar with a gold lid on a department-store glass counter. Only the hands are visible: no face, no person, no head anywhere in the frame.', 'The lid unscrews and lifts, revealing the smooth white cream inside.'),
 ('17', 46.78, ['claire', 'claire_bath'], 'night', 'Expression: hopeful and expectant. ' + GENERIC, 'Night, bathroom mirror: Claire applying a fancy cream from the generic jar to her cheek.', 'She dabs the cream on her cheek, looking hopefully at her reflection.'),
 ('18', 51.16, ['claire', 'claire_bath'], 'robe', 'Expression: disappointed. ' + GENERIC, 'Next morning: Claire looking at her dry arm, disappointed; a small white cream jar with a gold lid stands almost empty on the counter. No oil, no golden liquid, no other bottles.', 'She looks at her arm, sighs and her shoulders drop.'),
 ('19', 54.72, [], None, GENERIC, 'A bathroom shelf crowded with exactly eight half-used plain unbranded cream jars and lotion bottles, harsh light, no other items. They are ordinary inanimate objects with no faces, no eyes, no characters.', 'Slow sideways pan along the cluttered shelf.'),
 ('20', 58.98, ['claire', 'claire_bath'], 'robe', 'Expression: resigned.', 'Claire closing a mirrored medicine cabinet, her reflection briefly visible.', 'She slowly swings the mirrored cabinet door shut.'),
 ('21', 60.34, ['claire'], 'night', 'Expression: contemplative, quiet.', 'Night bedroom: Claire sitting on the edge of her bed with grey linen bedding, hands in her lap, warm low lamp light.', 'Slow push-in, she looks down at her hands and thinks.'),
 ('23', 65.26, ['claire', 'claire_bath'], 'day', SAD + ' ' + GENERIC, 'Close-up in cold bathroom light: Claire\'s hands hastily rubbing lotion together while a phone buzzes on the counter next to a plain unbranded lotion bottle.', 'Hurried hand rubbing, the phone vibrates on the counter.'),
 ('24', 70.22, ['claire'], 'day', 'Expression: distracted.', 'Claire, dressed for work, walking away out of her bathroom while rubbing her hands together and glancing at her watch.', 'She walks out of the room rubbing her hands, not looking back.'),
 ('25', 74.52, [], None, '', 'Slow, warm close-up of a woman\'s bare forearm skin in soft golden light, no product, just skin and light.', 'Golden light slowly warms and moves across the skin.'),
 ('26', 76.88, ['claire', 'claire_bath'], 'robe', 'Expression: soft dawning realization, gentle.', 'Claire in her bathroom in the evening, the light starting to turn warm golden; she pauses and stops rushing. The counter is empty: no bottles, jars or products anywhere.', 'She stops, her eyes lift, she takes a slow breath and her face softens.'),
 ('27', 82.20, ['box', 'dieline', 'bottle'], None, BOTTLE, 'Product reveal: the gold FALUNARA box (matching the box references, FALUNARA, gold brush stroke, botanical leaves, BOTANICAL BODY OIL) standing upright on a cream marble surface with the FALUNARA bottle beside it, warm golden backlight, soft glow.', 'Slow push-in, a warm golden glow shimmers around the box and bottle.'),
 ('28', 85.50, ['claire', 'claire_bath', 'bottle', 'bottle_front'], 'robe', SOFT + ' ' + BOTTLE, 'Claire in her evening bathroom holding the FALUNARA bottle in both hands at chest height, looking at it with gentle curiosity.', 'She gently turns the bottle in her hands and smiles softly.'),
 ('29', 88.48, [], None, '', 'Magical Pixar-style botanical scene: a sunflower, almonds, a jojoba branch, argan fruits and olives, each releasing glowing golden oil drops that flow together into one luminous golden stream, warm light, no labels.', 'Golden drops fall from each plant and merge into one flowing luminous stream.'),
 ('31', 98.34, ['claire', 'claire_bath'], 'robe', SOFT, 'Close-up: Claire presses golden oil from her open flat palm onto her damp forearm (an open-palm press, not rubbing), glistening skin, warm amber light, robe sleeve visible.', 'Her open palm presses slowly onto the forearm, lifts and presses again further up. No rubbing.'),
 ('32', 101.50, ['claire', 'claire_bath'], 'robe', SOFT, "Extreme close-up of Claire's forearm with the white terrycloth robe sleeve pushed back, a thin sheen of oil absorbing into the skin in warm bathroom light, Pixar-style soft golden glow, skin hydrated and luminous. No bottle, no other objects, no other person.", 'The glossy oil sheen slowly sinks into the skin and a soft golden glow blooms.'),
 ('33', 107.68, ['claire_bath', 'bottle', 'bottle_front'], 'robe', SOFT + ' ' + BOTTLE, "Claire's softly glowing forearm in the background, the FALUNARA bottle in sharp focus in the foreground on the marble counter, warm golden light.", 'Gentle pulses of warm light run along her arm, slow rack focus to the bottle.'),
 ('34', 110.38, ['claire', 'claire_bath'], 'robe', 'Expression: pleasantly surprised, starting to smile.', 'Claire after her shower, running her hand along her arm, noticing how soft it feels, warm bathroom light.', 'Her hand glides down her arm and her eyebrows lift in pleasant surprise.'),
 ('35', 114.96, ['claire', 'claire_bath'], 'robe', SOFT, "Close-up of Claire's forearm, skin soft with a healthy glow, two of her fingers touching it gently, her smiling face softly blurred at the frame edge.", 'Two fingers stroke the skin slowly, her smile grows.'),
 ('36', 120.14, ['claire', 'claire_bath'], 'robe', 'Expression: relieved.', 'Claire sitting on the edge of the bathtub looking down at her shins, which are now smooth, warm golden light.', 'She looks at her smooth shins and exhales with relief.'),
 ('37', 124.72, ['claire', 'claire_bath'], 'robe', 'Expression: a genuine, warm smile.', "Claire's hand gliding down her smooth shin while she smiles, sitting on the bathtub edge.", 'Her hand glides down her shin and she breaks into a warm smile.'),
 ('38', 129.98, ['claire', 'lily'], 'day', LILY + ' Both look warm and loving.', 'Cozy living room in warm evening light: Lily hugging Claire from the side, both happy.', 'Lily hugs her tighter, both close their eyes and smile.'),
 ('39', 131.96, ['claire', 'lily'], 'day', LILY + ' Expression: deeply moved, eyes glistening, a touched smile.', "Close-up of Claire's face during the hug, eyes glistening with emotion; Lily's dark hair and green sweater shoulder in the foreground.", 'A tear glistens in her eye as she smiles, Lily holds her.'),
 ('40', 139.72, ['claire', 'claire_bath', 'bottle'], 'robe', SOFT + ' ' + BOTTLE, 'Claire standing calmly in her bathroom in the evening, candle lit, the FALUNARA bottle on the counter, peaceful, unhurried.', 'She breathes slowly and calmly, the candle flickers.'),
 ('41', 142.44, ['claire', 'claire_bath', 'bottle'], 'robe', 'Expression: blissful, eyes closed, slight smile. ' + BOTTLE, 'Claire pressing FALUNARA oil from her palm onto her arm with her eyes closed, steam wisps, candle glow, warm amber light, the bottle on the counter.', 'She slowly presses her palm onto her arm, eyes closed, serene.'),
 ('42', 150.38, ['claire', 'claire_bath', 'bottle'], 'robe', SOFT + ' ' + BOTTLE, 'Wide shot of Claire in her bathroom during her evening ritual, golden light, the FALUNARA bottle and a candle on the counter, she looks present and at peace.', 'Slow dolly-in towards her.'),
 ('42b', 155.26, ['claire', 'claire_bath'], 'robe', 'Expression: peaceful, eyes closed, then a content smile.', "Close-up of Claire's face in warm golden light, eyes closed, completely at peace.", 'She takes a deep breath in, opens her eyes and smiles contentedly.'),
 ('43', 163.82, ['bottle', 'bottle_front', 'bottle_pump'], None, BOTTLE, 'The FALUNARA bottle with its cap on standing on a wooden nightstand next to a closed book and reading glasses, warm reading-lamp glow, cozy bedroom.', 'Slow push-in, soft lamp glow.'),
 ('44', 167.24, [], None, '', 'Pixar-style close-up of golden botanical oil drops and green leaf silhouettes floating in warm light, clean, pure, natural.', 'The golden drops and leaves float and drift slowly.'),
 ('45', 173.32, ['claire', 'bottle', 'bottle_front'], 'night', BOTTLE, "Wider shot of the bedroom nightstand: the FALUNARA bottle in the foreground, Claire's hand in a grey pajama sleeve reaching for the book behind it, soft focus.", 'Her hand picks up the book, the bottle stays in the foreground.'),
 ('46', 177.64, [], None, GENERIC, 'Front view of a cramped, cold-lit bathroom medicine cabinet with its mirrored door half open, shelves crammed with generic unbranded jars, tubes and bottles. Objects only: no people, no faces, no hands.', 'The cabinet door swings shut.'),
 ('47', 179.64, ['claire'], 'night', 'Expression: serene.', 'Claire standing by her bedroom window at night, starry sky outside, calm.', 'She takes a slow deep breath and her shoulders relax.'),
 ('47b', 183.78, ['bottle', 'bottle_front', 'bottle_pump'], None, BOTTLE, 'Three identical FALUNARA bottles with caps on arranged beautifully on cream marble, warm golden light.', 'Slow gentle camera arc, warm glints on the glass.'),
 ('48', 188.44, ['bottle', 'bottle_front'], None, BOTTLE, 'Three FALUNARA bottles in a row on a cozy bathroom shelf with a candle, warm evening light through the window.', 'The window light shifts slowly from dusk to night, candle glows.'),
 ('49', 192.54, ['claire', 'claire_bath'], 'robe', 'Expression: truly happy, confident, calm smile.', 'Claire smiling softly at herself in the bathroom mirror.', 'She smiles at her reflection and tilts her head slightly.'),
 ('50', 197.32, ['bottle', 'bottle_front', 'bottle_pump'], None, BOTTLE, 'Clean shot of the FALUNARA bottle with its cap on, surrounded by a gentle golden protective glow, trust and safety feeling, no symbols.', 'The golden glow pulses gently around the bottle.'),
 ('50b', 200.38, ['claire', 'bottle', 'bottle_front'], 'day', SOFT + ' ' + BOTTLE, 'Claire in a warm living room holding the FALUNARA bottle, smiling reassuringly at the camera.', 'She gives a small reassuring nod and smiles.'),
 ('51', 206.42, ['claire', 'claire_bath', 'bottle'], 'robe', SOFT + ' ' + BOTTLE, 'Claire in her warm bathroom gesturing gently downward with an open hand, smiling at the camera, the FALUNARA bottle on the counter.', 'She gestures gently downward with her open hand and smiles.'),
 ('52', 209.66, ['claire', 'claire_bath'], 'robe', SOFT, "Upright, natural composition: close-up of Claire's healthy, softly glowing forearm in warm golden bathroom light, white robe sleeve, her softly smiling face slightly blurred at the frame edge. No other person.", 'Golden light glides softly along the arm.'),
 ('53', 211.48, ['claire', 'claire_bath'], 'robe', 'Expression: confident, warm, at peace, slight knowing smile, looking directly at the camera.', 'Portrait of Claire in warm light.', 'Her knowing smile slowly grows, steady eye contact.'),
 ('54', 215.42, ['claire', 'claire_bath', 'bottle'], 'robe', SOFT + ' ' + BOTTLE, 'Bathroom ritual: Claire pressing oil onto her shoulder with her open palm, candle, steam, golden light, the FALUNARA bottle on the counter.', 'She slowly presses her palm onto her shoulder, steam drifts.'),
 ('55', 220.14, ['bottle', 'bottle_front', 'bottle_pump'], None, BOTTLE, 'Final hero shot: the FALUNARA bottle with its cap on, center frame on cream marble, warm golden light radiating softly, clean and iconic.', 'Very slow push-in, the warm glow intensifies softly.'),
]
FIXED = {'30': {'start': 93.48, 'video_path': 'scene30_pump_veo.mp4'}}


def plan():
    total = json.load(open(os.path.join(HERE, 'timeline.json')))['duration']
    starts = sorted([(s[1], s[0]) for s in S] + [(v['start'], k) for k, v in FIXED.items()])
    end_of = {sid: (starts[i + 1][0] if i + 1 < len(starts) else total) for i, (_, sid) in enumerate(starts)}
    scenes = []
    for sid, start, refs, outfit, extra, img, motion in S:
        dur = round(end_of[sid] - start, 2)
        legend = ' '.join(f'Reference image {i + 1} shows {REFS[r][1]}.' for i, r in enumerate(refs))
        people = ''
        if outfit:
            people = CLAIRE + ' ' + OUTFIT[outfit]
        prompt = ' '.join(p for p in [STYLE + '.', legend, people, extra, 'Scene: ' + img] if p)
        scenes.append({'id': sid, 'start': start, 'dur': dur, 'refs': [RAW + REFS[r][0] for r in refs],
                       'img_prompt': prompt, 'motion': MSTYLE + motion,
                       'veo_dur': 4 if dur <= 4.0 else 6 if dur <= 6.0 else 8})
    for k, v in FIXED.items():
        scenes.append({'id': k, 'start': v['start'], 'dur': round(end_of[k] - v['start'], 2), 'fixed': v['video_path']})
    return sorted(scenes, key=lambda s: s['start'])


def call(url, payload=None):
    req = urllib.request.Request(url, data=json.dumps(payload).encode() if payload else None,
                                 headers={'Authorization': f"Bearer {os.environ['KIE_API_KEY']}",
                                          'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(req, context=CTX, timeout=60).read())


def run_task(model, inp, every=10, tries=90):
    r = call('https://api.kie.ai/api/v1/jobs/createTask', {'model': model, 'input': inp})
    if r.get('code') != 200:
        raise RuntimeError(f'createTask: {r}')
    tid = r['data']['taskId']
    for _ in range(tries):
        time.sleep(every)
        try:
            d = call(f'https://api.kie.ai/api/v1/jobs/recordInfo?taskId={tid}')['data']
        except Exception:
            continue
        if d.get('state') == 'success':
            rj = json.loads(d['resultJson'])
            urls = rj.get('resultUrls') or rj.get('data', {}).get('result_urls') or rj.get('data', {}).get('origin_urls')
            return tid, urls[0], d.get('creditsConsumed')
        if d.get('state') == 'fail':
            raise RuntimeError(f"{tid} failed: {d.get('failCode')} {d.get('failMsg')}")
    raise RuntimeError(f'{tid} timeout')


def fetch(url, path):
    with open(path, 'wb') as f:
        f.write(urllib.request.urlopen(url, context=CTX, timeout=120).read())


def load_state():
    return json.load(open(STATE)) if os.path.exists(STATE) else {}


def save_state(st):
    json.dump(st, open(STATE, 'w'), indent=1)


def stage(kind, only):
    scenes = [s for s in plan() if 'fixed' not in s and (not only or s['id'] in only)]
    st = load_state()
    os.makedirs(os.path.join(HERE, 'scenes'), exist_ok=True)

    def work(s):
        e = st.setdefault(s['id'], {})
        try:
            if kind == 'images':
                if e.get('img_path') and s['id'] not in only:
                    return f"{s['id']} skip"
                inp = {'prompt': s['img_prompt'], 'image_input': s['refs'], 'aspect_ratio': '9:16',
                       'resolution': '2K', 'output_format': 'jpg'}
                tid, url, cr = run_task('nano-banana-pro', inp)
                path = f"scenes/s{s['id']}.jpg"
                fetch(url, os.path.join(HERE, path))
                e.update(img_task=tid, img_url=url, img_path=path, img_credits=cr)
                e.pop('vid_path', None)
                return f"{s['id']} image ok ({cr})"
            if e.get('vid_path') and s['id'] not in only:
                return f"{s['id']} skip"
            if not e.get('img_url'):
                return f"{s['id']} no image"
            inp = {'prompt': s['motion'], 'model': 'veo3_fast', 'image_urls': [e['img_url']],
                   'generation_type': 'FIRST_AND_LAST_FRAMES_2_VIDEO', 'aspect_ratio': '9:16',
                   'resolution': '720p', 'duration': s['veo_dur']}
            tid, url, cr = run_task('veo-3-1', inp, every=15)
            path = f"scenes/s{s['id']}.mp4"
            fetch(url, os.path.join(HERE, path))
            e.update(vid_task=tid, vid_url=url, vid_path=path, vid_credits=cr)
            return f"{s['id']} video ok ({cr})"
        except Exception as ex:
            e[f'{kind}_error'] = str(ex)[:300]
            return f"{s['id']} ERROR {str(ex)[:200]}"

    with ThreadPoolExecutor(max_workers=6) as pool:
        for msg in pool.map(work, scenes):
            print(msg, flush=True)
            save_state(st)
    save_state(st)


if __name__ == '__main__':
    cmd, only = sys.argv[1], set(sys.argv[2:])
    if cmd == 'plan':
        p = plan()
        json.dump(p, open(os.path.join(HERE, 'production_plan.json'), 'w'), indent=1)
        print(len(p), 'scenes;', sum(1 for s in p if 'fixed' not in s), 'to generate')
        for s in p:
            print(f"{s['id']:>4} {s['start']:7.2f} {s['dur']:5.2f} veo={s.get('veo_dur', '-')} refs={len(s.get('refs', []))}")
    else:
        stage(cmd, only)
