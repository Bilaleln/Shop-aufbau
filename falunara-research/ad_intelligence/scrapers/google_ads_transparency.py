"""Google Ads Transparency Center (no login) - capture SearchCreatives RPC JSON via headless Chromium.
Usage: python3 google_ads_transparency.py --domain evorabody.com --region US --out g.jsonl
Fields per creative: advertiser_id, creative_id, advertiser_name, format, first_shown, last_shown,
preview (image src or preview content.js URL). Ad copy for text/video ads lives in the preview JS
(render the creative detail page to read it): https://adstransparency.google.com/advertiser/<AR>/creative/<CR>?region=US
"""
import argparse, json, sys, time, datetime
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from pw_common import launch, sync_playwright
FMT = {1: "TEXT", 2: "IMAGE", 3: "VIDEO"}
def d(x):
    try: return datetime.datetime.utcfromtimestamp(int(x["1"])).strftime("%Y-%m-%d")
    except Exception: return None
ap = argparse.ArgumentParser()
ap.add_argument("--domain", default="evorabody.com"); ap.add_argument("--region", default="US")
ap.add_argument("--scrolls", type=int, default=5); ap.add_argument("--out", default="google_ads.jsonl")
a = ap.parse_args()
found = {}
with sync_playwright() as p:
    b, ctx = launch(p); page = ctx.new_page()
    def on(r):
        if "SearchService/SearchCreatives" in r.url:
            try:
                for c in json.loads(r.text()).get("1", []):
                    prev = c.get("3", {})
                    found[c["2"]] = {
                        "advertiser_id": c.get("1"), "creative_id": c.get("2"),
                        "advertiser_name": c.get("12"), "format": FMT.get(c.get("4"), c.get("4")),
                        "first_shown": d(c.get("6", {})), "last_shown": d(c.get("7", {})),
                        "field_13": c.get("13"), "domain": c.get("14"),
                        "preview": (prev.get("3", {}) or {}).get("2") or (prev.get("1", {}) or {}).get("4"),
                        "detail_url": f"https://adstransparency.google.com/advertiser/{c.get('1')}/creative/{c.get('2')}?region={a.region}"}
            except Exception as e: print("parse err", e, file=sys.stderr)
    page.on("response", on)
    page.goto(f"https://adstransparency.google.com/?region={a.region}&domain={a.domain}", timeout=60000)
    time.sleep(8)
    try:
        page.get_by_text("See all ads").first.click(timeout=5000); time.sleep(5)
    except Exception: pass
    for _ in range(a.scrolls):
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)"); time.sleep(3)
    b.close()
with open(a.out, "w") as f:
    for r in found.values(): f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(f"collected={len(found)} -> {a.out}", file=sys.stderr)
