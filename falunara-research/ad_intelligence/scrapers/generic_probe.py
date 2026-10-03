"""Load a URL in headless Chromium (proxy-aware), dump text/html/screenshot + XHR JSON responses."""
import sys, time, json
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from pw_common import launch, sync_playwright
url, out = sys.argv[1], sys.argv[2]
wait = int(sys.argv[3]) if len(sys.argv) > 3 else 10
xhr = []
with sync_playwright() as p:
    b, ctx = launch(p)
    page = ctx.new_page()
    def on(r):
        ct = r.headers.get("content-type", "")
        if r.request.resource_type in ("xhr", "fetch"):
            try: body = r.text()[:3000] if ("json" in ct or "protobuf" in ct or "text" in ct) else ""
            except Exception: body = ""
            xhr.append({"url": r.url[:300], "status": r.status, "ct": ct, "body": body})
    page.on("response", on)
    r = page.goto(url, wait_until="domcontentloaded", timeout=60000)
    print("status", r.status if r else None, "final", page.url)
    time.sleep(wait)
    page.screenshot(path=out + ".png")
    open(out + ".txt", "w").write(page.inner_text("body"))
    open(out + ".html", "w").write(page.content())
    json.dump(xhr, open(out + "_xhr.json", "w"), indent=1)
    print(page.inner_text("body")[:3000])
    b.close()
