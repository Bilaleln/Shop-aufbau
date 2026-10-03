# Ad-library access test (2026-10-03, cloud env, no login)

| Source | Accessible | Notes |
|---|---|---|
| **Meta Ad Library (US)** | **YES**, after a one-time fix to the proxy CA | Ad data sits as JSON inside the server-rendered HTML. You get **about 30 ads per page load**. Scroll pagination (`AdLibrarySearchPaginationQuery`) returns `Rate limit exceeded` (code 1675004) when logged out. After about 8 rapid loads, one load got **HTTP 403** with no ads. It worked again a few minutes later. |
| **Google Ads Transparency Center** | **YES** | `?region=US&domain=evorabody.com` returned 35 ads, all from advertiser "Snow Branding LLC" (verified). |
| **TikTok Ad Library** (library.tiktok.com) | **NO for US** | `api/v1/search?region=US` returns HTTP 421. The US is not in the list of 33 supported regions (EU/EEA/UK/CH only). |
| **TikTok Creative Center Top Ads** | Partial | The general US top-ads list loads without login (`creative_radar_api/v1/top_ads/v2/list`). Keyword search is off (`keyword_search:0`), so you can't search for a brand or for "crepey skin". |

## One-time setup needed (Chromium ignores the system CA store)
```
pip install playwright            # browser already at /opt/pw-browsers/chromium-1194
apt-get install -y libnss3-tools
cd /tmp && awk '/BEGIN CERT/{n++} {print > ("ca_" n ".pem")}' /root/.ccr/ca-bundle.crt
for f in ca_*.pem; do certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n "ccr-$f" -i $f; done
```
Without this, every page fails with `net::ERR_CERT_AUTHORITY_INVALID`. No `ignore_https_errors` is used.

## Meta: what you can read (from `snapshot` JSON, per ad)
ad_archive_id (Library ID), page_name / page_id, is_active, start_date ("Started running on"), end_date (for active ads this shows today's date), collation_count ("N ads use this creative and text"), publisher_platform, display_format, body text, title (headline), link_description, cta_text, caption (display domain), link_url (landing page), image/video URLs. The search total also comes back (`search_results_connection.count`).
- Keyword `evorabody` returned 1,168 results. The first 30 came from 5 pages: Natalie Brooks (998946876632416, 13 ads), **Evora Body (1031841923353593, 10)**, Ageless Glow Today (957899007407821, 5), Daily Discounts (1, video-only), Hannah Lewis (1). Advertorial "persona" pages link to evorabody.com.
- Page view `view_all_page_id=1031841923353593` (all statuses) returned 291 ads. The 30 collected were all active (20 VIDEO, 10 IMAGE). Landing pages: /products/botanical-body-oil (28) and /pages/listicle8 (1). quiz.evorabody.com was also seen in the keyword results.
- The `active_status=inactive` page view returned 0 ads twice. One of those loads was the HTTP 403. Not settled whether the page has no inactive ads or the request was blocked.
- Keyword `crepey skin` (active) works: 14,299 results. The top pages in the first 30 include DRMTLGY, Saeskyn and TurmSkin.

### Sample Evorabody ads (verbatim from the JSON)
1. 4075847312708860, Evora Body, active, started 2026-08-02, IMAGE. Body: "LIVE UPDATE: Stock dropping faster than we can count. ⠀ The body oil that went viral for actually reaching where lotions never could is causing checkout chaos right now. ⠀ 83% of this batch sold in the last 90 minutes. ⠀ If you've been "watching" or "researching" — this is your moment. ⠀ Everyone who hesitated yesterday is scrambling today. ⠀ Don't be the one refreshing for restock notifications next week." Title: "437 Orders in Last Hour — Almost gone". Link desc: "90 Day Money Back Guarantee". CTA: "Shop now". Caption: evorabody.com. Landing: https://evorabody.com/products/botanical-body-oil
2. 1954753225212676, Evora Body, active, started 2026-08-22, VIDEO, collation_count 4 ("4 ads use this creative and text"). Platforms: FACEBOOK, INSTAGRAM, AUDIENCE_NETWORK, MESSENGER, THREADS. Body: "THIS is what Oil does for your skin…". Title: "Here’s What Actually Works…". CTA: "Shop now". Landing: https://evorabody.com/products/botanical-body-oil
3. 857286387379018, Natalie Brooks (page 998946876632416), active, started 2026-09-17 (on the rendered page: "Started running on Sep 17, 2026"). Long advertorial body that begins "I stole a bottle of body oil from a hotel in Maui last summer. I'm not proud of it. The general manager wrote me a letter three weeks later." Title: "I'm not proud of what I took from suite 609". Link desc: "Say goodbye to crepey, saggy & dry skin. This botanical body oil visibly restores firmness and smoothness in just 2 minutes a day. See real results in 3–4 weeks — or get your money back." CTA: "Shop now". Caption: evorabody.com

## Google: what you can read
advertiser name and ID, creative ID, format code, first shown, last shown, a field that looks like days shown, and a preview (image src or a preview JS URL). The ad copy for video and text ads is inside the preview JS and was **not** pulled out in this test.
Samples: CR03193359664054009857, Snow Branding LLC, first shown 2026-08-12, last shown 2026-10-03, format code 1 (preview is an image). CR10786172827548516353, Snow Branding LLC, VIDEO, 2026-09-30 to 2026-10-03.

## Scripts (in scrapers/)
- `pw_common.py`: launcher (Chromium at /opt/pw-browsers/chromium-1194, HTTPS_PROXY)
- `meta_ad_library.py`: `--q <kw>` or `--page-id <id>`, `--status all|active|inactive`, outputs JSONL
- `google_ads_transparency.py`: `--domain`, `--region`, outputs JSONL
- `meta_probe.py`, `generic_probe.py`: dump raw text, HTML, screenshot and XHR
- `samples/`: raw JSONL from this test

## Ways to get past the 30-ad limit (not tested)
Split the queries: active vs. inactive, `media_type=video|image`, keyword_exact_phrase, each advertorial page ID separately, and date filters (`start_date[min]`/`[max]`). Space the loads out (one every 20 s or more) to avoid the 403.
