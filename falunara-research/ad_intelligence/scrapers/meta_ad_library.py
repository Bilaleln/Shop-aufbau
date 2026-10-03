"""Meta Ad Library scraper (no login) via headless Chromium + Playwright.

Prereqs in this cloud env (one-time):
  pip install playwright
  apt-get install -y libnss3-tools
  # Chromium uses the NSS store, not the system CA store -> import proxy CA bundle:
  cd /tmp && awk '/BEGIN CERT/{n++} {print > ("ca_" n ".pem")}' /root/.ccr/ca-bundle.crt && \
    for f in ca_*.pem; do certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n "ccr-$f" -i $f; done

Usage:
  python3 meta_ad_library.py --q evorabody --scrolls 10 --out evorabody_meta.jsonl
  python3 meta_ad_library.py --page-id 1031841923353593 --scrolls 20 --out evora_page.jsonl
Collects ad objects from the server-rendered JSON and from /api/graphql/ responses
fired while scrolling (infinite scroll).
"""
import argparse, json, re, sys, time, datetime, csv
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from pw_common import launch, sync_playwright

def build_url(a):
    base = ("https://www.facebook.com/ads/library/?active_status={st}&ad_type=all&country={c}"
            "&media_type=all")
    u = base.format(st=a.status, c=a.country)
    if a.page_id:
        u += f"&search_type=page&view_all_page_id={a.page_id}"
    else:
        from urllib.parse import quote
        u += f"&q={quote(a.q)}&search_type={'keyword_exact_phrase' if a.exact else 'keyword_unordered'}"
    return u

def walk(o, found):
    if isinstance(o, dict):
        if "ad_archive_id" in o and "snapshot" in o:
            found[o["ad_archive_id"]] = o
        for v in o.values(): walk(v, found)
    elif isinstance(o, list):
        for v in o: walk(v, found)

def parse_json_blobs(text, found):
    for m in re.finditer(r'<script type="application/json"[^>]*>(.*?)</script>', text, re.S):
        try: walk(json.loads(m.group(1)), found)
        except Exception: pass

def parse_graphql(body, found):
    for line in body.splitlines():  # FB graphql may return multiple JSON docs
        line = line.strip()
        if line.startswith("for (;;);"): line = line[9:]
        try: walk(json.loads(line), found)
        except Exception: pass

def ts(x):
    return datetime.datetime.utcfromtimestamp(x).strftime("%Y-%m-%d") if x else None

def flatten(o):
    s = o.get("snapshot") or {}
    cards = s.get("cards") or []
    c0 = cards[0] if cards else {}
    return {
        "ad_archive_id": o.get("ad_archive_id"),
        "page_id": o.get("page_id"),
        "page_name": s.get("page_name"),
        "is_active": o.get("is_active"),
        "start_date": ts(o.get("start_date")),
        "end_date": ts(o.get("end_date")),
        "collation_count": o.get("collation_count"),   # "N ads use this creative and text"
        "collation_id": o.get("collation_id"),
        "publisher_platform": o.get("publisher_platform"),
        "display_format": s.get("display_format"),
        "body": ((s.get("body") or {}).get("text") if isinstance(s.get("body"), dict) else s.get("body")) or c0.get("body"),
        "title": s.get("title") or c0.get("title"),
        "link_description": s.get("link_description") or c0.get("link_description"),
        "cta_text": s.get("cta_text") or c0.get("cta_text"),
        "caption": s.get("caption") or c0.get("caption"),
        "link_url": s.get("link_url") or c0.get("link_url"),
        "n_cards": len(cards),
        "video_urls": [v.get("video_hd_url") or v.get("video_sd_url") for v in (s.get("videos") or [])] +
                      [c.get("video_hd_url") or c.get("video_sd_url") for c in cards if c.get("video_hd_url") or c.get("video_sd_url")],
        "image_urls": [i.get("original_image_url") for i in (s.get("images") or [])] +
                      [c.get("original_image_url") for c in cards if c.get("original_image_url")],
        "page_profile_uri": s.get("page_profile_uri"),
        "page_like_count": s.get("page_like_count"),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--q", default="evorabody")
    ap.add_argument("--exact", action="store_true")
    ap.add_argument("--page-id")
    ap.add_argument("--country", default="US")
    ap.add_argument("--status", default="all", choices=["all", "active", "inactive"])
    ap.add_argument("--scrolls", type=int, default=8)
    ap.add_argument("--out", default="meta_ads.jsonl")
    a = ap.parse_args()
    url = build_url(a); print("URL", url, file=sys.stderr)
    found, total, gql_hits = {}, None, []
    with sync_playwright() as p:
        b, ctx = launch(p)
        page = ctx.new_page()
        def on_resp(r):
            if "/api/graphql" in r.url:
                try:
                    before = len(found); parse_graphql(r.text(), found)
                    gql_hits.append(len(found) - before)
                except Exception as e: gql_hits.append(f"err {e}")
        page.on("response", on_resp)
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        time.sleep(6)
        html = page.content()
        if "login" in page.url or "checkpoint" in page.url:
            print("BLOCKED: redirected to", page.url, file=sys.stderr)
        m = re.search(r'"search_results_connection":\{"count":(\d+)', html)
        total = int(m.group(1)) if m else None
        parse_json_blobs(html, found)
        print("after html parse:", len(found), file=sys.stderr)
        for i in range(a.scrolls):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)"); time.sleep(3)
            print(f"scroll {i+1}: {len(found)} ads, graphql responses={gql_hits}", file=sys.stderr)
        b.close()
    rows = [flatten(o) for o in found.values()]
    with open(a.out, "w") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"total_reported={total} collected={len(rows)} -> {a.out}", file=sys.stderr)

if __name__ == "__main__":
    main()
