"""Shared Playwright launcher for this cloud env (proxy + preinstalled Chromium)."""
import os
from playwright.sync_api import sync_playwright

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")

def launch(p):
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    browser = p.chromium.launch(
        executable_path=CHROME, headless=True,
        proxy={"server": proxy} if proxy else None,
        args=["--disable-blink-features=AutomationControlled"])
    # proxy CA is in system store; fall back to ignore_https_errors only if TLS fails
    ctx = browser.new_context(user_agent=UA, locale="en-US",
                              viewport={"width": 1400, "height": 2000},
                              ignore_https_errors=os.environ.get("PW_IGNORE_TLS") == "1")
    return browser, ctx
