import sys, time, json
sys.path.insert(0, __file__.rsplit("/",1)[0])
from pw_common import launch, sync_playwright
URL = sys.argv[1] if len(sys.argv)>1 and sys.argv[1] else ("https://www.facebook.com/ads/library/?active_status=all&ad_type=all"
       "&country=US&q=evorabody&search_type=keyword_unordered&media_type=all")
out = sys.argv[2] if len(sys.argv)>2 else "/tmp/meta"
with sync_playwright() as p:
    b, ctx = launch(p)
    page = ctx.new_page()
    r = page.goto(URL, wait_until="domcontentloaded", timeout=60000)
    print("status", r.status if r else None, page.url)
    time.sleep(8)
    for _ in range(3):
        page.mouse.wheel(0, 3000); time.sleep(2)
    page.screenshot(path=out+".png", full_page=False)
    txt = page.inner_text("body")
    open(out+".txt","w").write(txt)
    open(out+".html","w").write(page.content())
    print(txt[:4000])
    b.close()
