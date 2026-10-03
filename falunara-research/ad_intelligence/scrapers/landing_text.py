"""Render landing pages and dump visible text. Usage: python3 landing_text.py name=url [name=url ...]"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pw_common import launch, sync_playwright
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "raw", "landing")
with sync_playwright() as p:
    b, ctx = launch(p)
    for arg in sys.argv[1:]:
        name, url = arg.split("=", 1)
        pg = ctx.new_page()
        try:
            r = pg.goto(url, wait_until="domcontentloaded", timeout=60000); time.sleep(5)
            for _ in range(6): pg.mouse.wheel(0, 3000); time.sleep(0.7)
            txt = pg.inner_text("body")
            open(f"{OUT}/{name}.txt", "w").write(f"URL {url}\nFINAL {pg.url}\nHTTP {r.status if r else None}\n\n{txt}")
            print(name, r.status if r else None, len(txt))
        except Exception as e: print(name, "ERR", e)
        pg.close()
    b.close()
