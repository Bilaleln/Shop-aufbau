"""Batch runner for Meta Ad Library (no login). Spaces loads, backs off on 403.
Usage: python3 meta_batch.py jobs.json
jobs.json: [{"name":"evora_page_video","page_id":"...","status":"active","media":"video",
             "q":null,"exact":false,"smin":"2026-01-01","smax":"2026-06-30"}, ...]
Each job writes raw/<name>.jsonl (flattened + video preview image + total_reported)."""
import json, sys, time, re, os
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pw_common import launch, sync_playwright
from meta_ad_library import parse_json_blobs, flatten
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "raw")
SPACING = int(os.environ.get("SPACING", "25"))

def url_for(j):
    u = (f"https://www.facebook.com/ads/library/?active_status={j.get('status','all')}&ad_type=all"
         f"&country={j.get('country','US')}&media_type={j.get('media','all')}")
    if j.get("page_id"):
        u += f"&search_type=page&view_all_page_id={j['page_id']}"
    else:
        u += f"&q={quote(j['q'])}&search_type={'keyword_exact_phrase' if j.get('exact') else 'keyword_unordered'}"
    if j.get("smin"): u += f"&start_date[min]={j['smin']}"
    if j.get("smax"): u += f"&start_date[max]={j['smax']}"
    return u

def extra(o):
    s = o.get("snapshot") or {}
    vids = (s.get("videos") or []) + [c for c in (s.get("cards") or []) if c.get("video_preview_image_url")]
    prev = [v.get("video_preview_image_url") for v in vids if v.get("video_preview_image_url")]
    cards = [{k: c.get(k) for k in ("title", "body", "link_url", "link_description", "cta_text")} for c in (s.get("cards") or [])]
    return {"video_preview_urls": prev, "cards": cards, "cta_type": s.get("cta_type"),
            "page_categories": s.get("page_categories"), "contains_digital_created_media": o.get("contains_digital_created_media")}

def run(ctx, j):
    url = url_for(j); found = {}; status = [None]
    page = ctx.new_page()
    def on_resp(r):
        if r.url.startswith("https://www.facebook.com/ads/library/") and r.request.resource_type == "document":
            status[0] = r.status
    page.on("response", on_resp)
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=60000); time.sleep(6)
        html = page.content()
    except Exception as e:
        page.close(); return None, f"err {e}", url
    page.close()
    m = re.search(r'"search_results_connection":\{"count":(\d+)', html)
    total = int(m.group(1)) if m else None
    parse_json_blobs(html, found)
    rows = []
    for o in found.values():
        r = flatten(o); r.update(extra(o)); r["total_reported"] = total; r["query"] = j; r["query_url"] = url
        r["scraped_at"] = "2026-10-03"; rows.append(r)
    return rows, status[0], url

def main():
    jobs = json.load(open(sys.argv[1]))
    with sync_playwright() as p:
        b, ctx = launch(p)
        for i, j in enumerate(jobs):
            out = os.path.join(RAW, j["name"] + ".jsonl")
            if os.path.exists(out) and os.path.getsize(out) > 0 and not j.get("force"):
                print("skip", j["name"], flush=True); continue
            for attempt in range(3):
                rows, st, url = run(ctx, j)
                n = len(rows) if rows else 0
                print(f"[{j['name']}] http={st} ads={n} total={rows[0]['total_reported'] if rows else None} {url}", flush=True)
                if st == 403 or (rows is None):
                    print("  403/err -> backoff 240s", flush=True); time.sleep(240); continue
                break
            if rows:
                with open(out, "w") as f:
                    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
            else:
                open(out + ".empty", "w").write(f"http={st} url={url}\n")
            time.sleep(SPACING)
        b.close()
main()
