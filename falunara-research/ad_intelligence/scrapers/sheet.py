"""Contact sheet: python3 sheet.py out.jpg id1 id2 ... (uses thumbs/<id>.jpg)"""
import sys, os
from PIL import Image, ImageDraw
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "thumbs")
ids = sys.argv[2:]; W = 360; cols = 4; rows = (len(ids) + cols - 1) // cols
S = Image.new("RGB", (cols * W, rows * (W + 20)), "white"); dr = ImageDraw.Draw(S)
for k, i in enumerate(ids):
    try:
        im = Image.open(f"{D}/{i}.jpg").convert("RGB"); im.thumbnail((W, W))
        x, y = (k % cols) * W, (k // cols) * (W + 20); S.paste(im, (x, y + 20)); dr.text((x + 4, y + 4), i, fill="red")
    except Exception as e: print(i, e)
S.save(f"{D}/{sys.argv[1]}", quality=70)
