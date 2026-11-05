import json,sys
sys.path.insert(0,'bin')
A={r['name']:r for r in (json.loads(l) for l in open('manifest.jsonl')) if r['state']=='success'}
U=lambda n:A[n]['files'][0]['url']
exec(open('bin/specs_a.py').read().split("def s(")[0])
REFS=[REF1,U('t01_hero')]
LBL=" The label must match the clean packshot reference exactly: spaced capital 'FADILAL' wordmark at top, faint rose line drawing, 'wild rose.' large lowercase serif, 'Massage candle' below, italic 'Melts into a warm skin oil.' and '7 oz · 200 g' at the bottom. Label faces the camera."
def s(name,ar,prompt,extra=()):
    return {"name":name,"model":"nano-banana-pro","input":{"prompt":BASE+prompt+LBL+STYLE,"image_input":REFS+[U(e) for e in extra],"aspect_ratio":ar,"resolution":"2K","output_format":"png"}}
SC=" Use the additional scene reference image for the setting, lighting and the person's appearance."
B=[
s("a08_ingredients_v2","1:1","Overhead editorial flat-lay on white linen: the closed FADILAL wild rose candle in the center, standing upright seen from a high three-quarter angle so the front label is fully readable; around it in small handmade white ceramic dishes: golden beeswax pellets with a small piece of natural honeycomb, white coconut wax flakes, ivory soy wax flakes; a few pale-pink wild rose petals; soft daylight, clean, balanced spacing."),
s("a11_evening_woman_v2","4:5","Candid vertical lifestyle photo of "+WOMAN+" sitting on the edge of a white freestanding bathtub in a calm warmly lit bathroom in the evening, smoothing a little oil onto her forearm with a relaxed smile; the lit FADILAL wild rose candle on a small wooden stool in the foreground, label clearly readable. Natural, unstaged."+SC,["w_evening_woman"]),
s("a13_hero_wide_v2","16:9","Wide premium campaign photograph: calm bathroom at dusk, the lit FADILAL wild rose candle on a white oval ceramic tray on a pale stone ledge in the right third of the frame, label facing camera and readable, folded white towels and a small glass with a wild rose stem beside; the left half is soft uncluttered bright negative space (softly lit plaster wall) for a headline; soft evening window light."+SC,["a06_bathroom"]),
s("a13_hero_mobile_v2","4:5","Vertical premium campaign photograph: calm bathroom at dusk, the lit FADILAL wild rose candle on a white oval ceramic tray on a pale stone ledge in the lower third, label facing camera and readable, folded white towels and a glass with a wild rose stem beside; the upper half is soft uncluttered negative space (softly lit plaster wall); soft evening window light."+SC,["a06_bathroom"]),
# Video 1 keyframes (9:16)
s("k1_bath","9:16","Vertical close-up: the open unlit FADILAL candle (lid lying beside) on a white ceramic tray on a white marble bathroom countertop by a window, folded white towels and a sprig of eucalyptus softly blurred behind, soft evening daylight."+SC,["a06_bathroom"]),
s("k2_light","9:16","Vertical shot: "+HANDS+" holds a long wooden match with a small flame just above the wick of the open unlit FADILAL candle on a white ceramic tray on white marble by a window; careful calm gesture; other hand resting on the counter."+SC,["a10_step1_light"]),
s("k3_melt","9:16","Vertical macro close-up looking slightly down into the lit FADILAL candle: small calm flame, a clear golden pool of melted oil spreading around the wick, pale solid wax at the rim, soft reflections on amber glass, label visible at the bottom of the frame."+SC,["a04_melting"]),
s("k4_lit","9:16","Vertical shot: the lit FADILAL candle burning calmly with a wide golden pool of melted oil, on a white ceramic tray on white marble by a window, lid lying beside, no hands."+SC,["a10_step2_melt"]),
s("k5_test","9:16","Vertical shot: the candle flame is out, a thin wisp of smoke rises from the wick; "+HANDS+" gently touches the edge of the golden oil pool with one fingertip to test the warmth; white ceramic tray on white marble by a window."+SC,["a10_step3_test"]),
s("k6_apply","9:16","Vertical close-up: a mature woman's forearm, about 55, real skin with fine lines; the fingertips of her other hand gently smoothing a thin satin layer of golden oil onto it; the open unlit FADILAL candle softly out of focus in the background on white marble."+SC,["a05_application"]),
s("k7_beauty","9:16","Vertical premium beauty shot: the closed FADILAL wild rose candle standing on white marble beside a single wild rose stem and a folded white towel, soft directional window light, gentle shadow, generous clean space above."+SC,["a12_guarantee"]),
# Video 2 keyframes
s("e1_woman","9:16","Vertical medium shot of "+WOMAN+" standing at a white marble bathroom vanity in the evening, holding the lit FADILAL candle on its ceramic tray in both hands and looking at it with a calm soft smile; warm soft lighting."+SC,["w_evening_woman"]),
s("e2_hands","9:16","Vertical close-up of the same woman's hands and forearm in a cream knit sleeve, slowly smoothing a thin satin layer of oil into her forearm, the lit FADILAL candle glowing softly out of focus behind on the bathroom vanity; warm evening light."+SC,["w_evening_woman"]),
s("e3_glow","9:16","Vertical close-up: the lit FADILAL candle on the edge of a white bathtub in sharp focus, in the softly blurred background the same woman in a cream cardigan sits relaxed with eyes closed; warm calm evening light."+SC,["w_evening_woman"]),
# Video 3 (UGC) keyframes
s("u1_show","9:16","Smartphone-style vertical photo in an ordinary bright living room in the evening (sofa, throw blanket, floor lamp): "+HANDS.replace('cream knit sleeve','grey sweatshirt sleeve')+" holding the closed FADILAL candle toward the camera at arm's length so the label is readable; natural casual framing, slight phone-camera look, realistic home light."),
s("u2_oil","9:16","Smartphone-style vertical photo looking down at a wooden coffee table in an ordinary living room: the open, unlit FADILAL candle with a glossy golden melted oil surface, lid beside it, a woman's hand in a grey sweatshirt sleeve pointing near (not touching) the jar; casual natural home light, slight phone-camera look."),
]
json.dump(B,open('spec_b.json','w'),indent=1); print(len(B))
