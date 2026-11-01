# 07 Social Media Research and 09 Ad Style Analysis: Núan Ritual Candle + Lumera lamp

Research date: 2026-11-01. Scope: Step 7 (social research) and Step 9 (ad style analysis).

## 0. Method, tool status and how far to trust this

- **Trendtrack MCP did not work.** The first call, `search_ads` ("massage candle", longest running), returned "Not enough credits". `check_credits` then showed the workspace "Bilal's Workspace" on the professional plan with **0 of 10,000 credits left**. The period resets on **2026-11-10**. `search_tiktok_library` failed the same way. This means **no Meta or TikTok ad-library data was pulled** for this report: no days-running figures, no spend estimates, no reach. Every "longest-running ad" question below is still open. Rerun these after 2026-11-10: `search_ads` with `trend_signal=longest_running` for "massage candle", "lotion candle", "candle warmer lamp", "non-toxic candle", "hand balm", "cuticle oil", "sleep spray", and `search_advertisers` for "Neom".
- **Meta Ad Library** returned HTTP 403 to direct fetches. adlibrary.com's Neom page showed 8 TikTok ads with no copy (it is paywalled). TikTok, YouTube and Instagram pages give no captions, views or comments to WebFetch. I also tried to fetch TikTok with a crawler user agent, and that was blocked, so I dropped the approach.
- **What the report does use:**
  - TikTok video captions that appear verbatim in search-engine results, each with its video URL.
  - Journalism that quotes TikTok videos, view counts and comments (Daily Dot, Distractify, AJC, Beauty Independent, Irish Examiner, Dazed, Yahoo/House Beautiful).
  - Modash's index of sponsored Neom creator posts.
- **Rules followed:** every hook, view count and comment below has a link. Where I could not verify a view count, I say "views not verified". When I interpret a pattern or recommend something, it is labelled **[Inference]**.
- **Main gap:** most of the hooks are **organic posts and creator or brand posts, not confirmed paid ads.** The exceptions are posts disclosed as sponsored: Neom #ad posts, @sydmiller as a "brand partner", and @noodle_yess with a discount code. Treat the hook bank as "what earns attention in the category". It does not tell you what has been scaled with paid spend.

---

## 1. Hook analysis (verified hooks, verbatim)

Pattern key: CS = claim size, SP = speed, AU = authority, BA = before/after, RC = rival comparison, RL = removing limitations, Q = question, IN = information, NW = newness, EX = exclusivity, BC = belief-challenging, DC = direct call-out.

| # | Hook (verbatim, first line of caption or spoken/on-screen) | Account / link | Reach info | Pattern |
|---|---|---|---|---|
| 1 | "My husband's reaction to buying a candle warmer" (on-screen). Spoken punchline: "you spent money on a machine that also costs us money when a flame is free, Shelby." | @shelbanddyl, covered by [Distractify, 7 Jun 2024](https://www.distractify.com/p/man-reacts-to-candle-warmer) | Views not given; article calls it viral | RC (flame vs. lamp), humour, objection-led |
| 2 | "This is the best purchase I have ever made from Amazon" | @sunrisevalleyfarm.co, quoted in [AJC, 11 Jan 2023](https://www.ajc.com/life/private-quarters/tiktoks-candlewarmer-lamps-are-trending-inside-homes/6BB5MCUXDVDFFIXHMQXN3PS3MM) | Not given; follow-up caption "Yall LOVED these candle warming lamps!" | CS |
| 3 | "This makes your candles last longer and look good while doing it!" | @apartmenttherapy, quoted in [AJC](https://www.ajc.com/life/private-quarters/tiktoks-candlewarmer-lamps-are-trending-inside-homes/6BB5MCUXDVDFFIXHMQXN3PS3MM) | Not given | RL + CS |
| 4 | "actually obsessed with this and totally worth the hype 👏 this is a candle warmer and it seriously extends the life of my candle x10" | [@sloanevosen](https://www.tiktok.com/@sloanevosen/video/7480316210027040031) | Not verified; tags #candletok #springtok | CS (x10), social proof |
| 5 | "A candle warmer lamp works by heating up the wax in the candle and diffusing the scent throughout your home! No flame required." | [@nataliemarceta](https://www.tiktok.com/@nataliemarceta/video/7241610955241671982) | Not verified | IN + RL |
| 6 | "This is why you need a candle warmer! Yes, candle warmers are safer than burning." | [@louiselaceda](https://www.tiktok.com/@louiselaceda/video/7247367150556450053) | Not verified | DC + BC |
| 7 | "Replying to @Beth's birds 🐦 Elevate your home with this Electric Candle Warmer! … Perfect for moms, furr owners, or anyone who loves cozy vibes without the worry." | [@vanjeafinds](https://www.tiktok.com/@vanjeafinds/video/7652279139596111135) | Not verified; TikTok Shop affiliate | Comment-reply, DC (moms, pet owners) |
| 8 | "Making a mini simmer pot for my candle warmer lamp! 🤎" | [@ourwintonhome](https://www.tiktok.com/@ourwintonhome/video/7505401630171483434) | Not verified | NW (hack/new use) |
| 9 | "Have you ever tried a massage oil candle? 🕯️" | [@purewow](https://www.tiktok.com/@purewow/video/7227493204168330542) (Dame launch) | Not verified | Q |
| 10 | "Try out a soy massage candle for the ultimate spa-like pampering in the comfort of your own home." | [@naturasoy](https://www.tiktok.com/@naturasoy/video/7241957790577659141) | Not verified | CS + EX ("spa at home") |
| 11 | "Replying to @kdeci no you cant peel it off, but it is the perfect transition to after care!" | [@rosaliebodyworks](https://www.tiktok.com/@rosaliebodyworks/video/7197626434624490795) | Not verified | Comment-reply Q/objection |
| 12 | "The Rosalie lotion candle is best way to elevate your night ..." | [@rosaliebodyworks](https://www.tiktok.com/@rosaliebodyworks/video/7399086243600026911) | Not verified | CS, night ritual |
| 13 | "🕯️🍁 Fall candle season but make it non toxic✨🎃" | [@holisticeli](https://www.tiktok.com/@holisticeli/video/7555958641061399830) | Not verified | Seasonal + BC |
| 14 | "5 BEST NON-TOXIC CANDLES & how toxic some regular candles really are 🫣😳" | [@by.erinmarie](https://www.tiktok.com/@by.erinmarie/video/7581647158802206007) | Not verified | IN (listicle) + BC + RC (names Bath & Body Works) |
| 15 | "Here is what to look for instead!👇 If your scented candles contain paraffin wax or artificial fragrance, throw them away!" | [@cleankitchennutrition](https://www.tiktok.com/@cleankitchennutrition/video/7319710731119906094) | Not verified | BC + DC |
| 16 | "5 reasons to not burn candles:" (cites PMIDs) | [@dryvonneburkart](https://www.tiktok.com/@dryvonneburkart/video/7162181201346841899) (toxicologist) | Not verified | AU + BC |
| 17 | "SAFER CANDLE OPTIONS All candles generate pollutants, but are coconut, soy, and beeswax candles truly safer?" | [@dryvonneburkart](https://www.tiktok.com/@dryvonneburkart/video/7196084514521713966) | Not verified | AU + Q |
| 18 | "Myself and Toxicologist Dr Yvonne Burkart discussed how dangerous scented candles can really be?!" | [@steven](https://www.tiktok.com/@steven/video/7438711919600602401) (Diary of a CEO clip) | Not verified | AU (podcast clip) |
| 19 | "Did you know that burning home candles could be toxic to your health??..." | [@amena.kay](https://www.tiktok.com/@amena.kay/video/7302488442347277599) | Not verified | Q + BC |
| 20 | "Friendly reminder that the same chemicals that are causing her wall to melt, are in [Bath & Body Works] candles as well" | @silycandleco (duet), covered by [Daily Dot, Dec 2021](https://dailydot.com/unclick/bath-body-works-chemicals-products-tiktok) | **629,500+ views** | RC + BC |
| 21 | "Anyone else notice their Bath & Body Works candles burning quicker than normal?" | @_bybrittney, covered by [Daily Dot, 22 Dec 2024](https://dailydot.com/bath-body-works-candle-quality) | **670,000+ views** | Q + RC (Q4 "Candle Day" timing) |
| 22 | "Glade & Air Wick plug-ins will take you out of here" | @therealogk_, covered by [Daily Dot, 8 Jan 2025](https://dailydot.com/glade-air-wick-plug-ins-headache) | **375,800+ views** | BC |
| 23 | "Dry cracked hands? This simple hack will change your life." | [@dermguru](https://www.tiktok.com/@dermguru/video/7174406612528942379) | Not verified; posted Dec (winter) | DC + CS, seasonal |
| 24 | "My dermatologist approved hack to help fight dry, itchy or eczema prone hand dermatitis: At home hand masks!" | [@denverskindoc](https://www.tiktok.com/@denverskindoc/video/7153089900538088746) | Not verified | AU + RL |
| 25 | "How to moisturize dry hands with #moisturizinggloves" | [@drdrayzday](https://www.tiktok.com/@drdrayzday/video/7156260844047748394) | Not verified | IN + AU |
| 26 | "Instantly asleep 😴 💤 🌝 Deep sleep pillow spray: proven to help you fall asleep faster and wake feeling more refreshed" | [@thisworkssocial](https://www.tiktok.com/@thisworkssocial/video/7512512683854335264) (brand) | Not verified | SP + CS + AU ("proven") |
| 27 | "Reviewing 4 cuticle oils!" | [@missleahmei](https://www.tiktok.com/@missleahmei/video/7528979147067100421) | Not verified | RC (side-by-side review). Notes Dior cream "I use this at night!😴" |
| 28 | "How often should you apply cuticle oil? 🤔" | [@kiaraskynails](https://www.tiktok.com/@kiaraskynails/video/7185229788494449966) | Not verified | Q |
| 29 | "The Magic of Nail Slugging: Before and After Results Revealed" | [@jacquelinekilikita](https://www.tiktok.com/@jacquelinekilikita/video/7127390583819209989) | 533 likes (per search snippet) | BA |
| 30 | "bed by 8pm is my kinda fun" (low-dopamine evening routine) | @momentsabloom, reported by [Irish Examiner, 1 Jan 2026](https://www.irishexaminer.com/lifestyle/advice/arid-41733384.html) | **~600,000 views** | BC (anti-hustle), identity |
| 31 | Candle tunneling fix with foil, 31 sec (verbatim hook not published) | Otherland, per [Beauty Independent, Mar 2023](https://www.beautyindependent.com/otherlands-candle-care-content-sizzles-tiktok/) | **6.6M+ views** | RL / IN (problem fix) |
| 32 | "this and bed before 9pm 🙏🏼 as a @neomwellbeing brand partner" | @sydmiller (Sydney Miller, HOUSEWORK), via [Modash Neom index](https://www.modash.io/content-library/brands/neom-examples) | 0:37 video | Identity, early-bed |
| 33 | "comment SLEEPY for all my bedside basket essentials ☁️✨" | @livingwithtish, via [Modash](https://www.modash.io/content-library/brands/neom-examples) | Unlabelled figures 1.7k / 178 | CTA-as-hook (comment-to-DM) |

### Longest-running and best-proven hooks
- **Ad longevity: not verifiable this cycle** because Trendtrack had no credits.
- **Longest-lived organic theme: the candle warmer lamp.** It went viral in mid-2023 (the AJC piece is from Jan 2023). Coverage continues through 2024: [Yahoo/House Beautiful, Oct 2024](https://www.yahoo.com/lifestyle/honest-review-candle-warmer-lamp-215200683.html) and the [Distractify husband clip, Jun 2024](https://www.distractify.com/p/man-reacts-to-candle-warmer). Fresh TikTok Shop affiliate posts keep appearing; video IDs 7480… and 7652… point to 2025–2026. A [Baijing/Cifnews trade article (Dec 2023)](https://www.baijing.cn/article/47092) reports a home creator with only 20,000+ followers whose warmer sales video reached **10.5M impressions**, and **181M views** for the "lamp candle warmer" keyword. Reported #candlewarmer counts vary from 57.4M to 100M+ depending on source and date (see the Ideal Home, Yahoo and Taste of Home figures quoted in search coverage).
- **"Toxic candle" fear hooks** have stayed effective from 2021 to 2025. The Daily Dot clips reached 375K to 670K views each, and a toxicologist was featured on Diary of a CEO in Nov 2024.

### Seasonal hooks found
- **Q4 / gifting:** #21 ran on Bath & Body Works "Candle Day" in December. TikTok Shop warmer listings are named "Christmas Birthday Gifts for Women Mom Her" ([TikTok Shop search](https://www.tiktok.com/shop/product/candle-warmer-lamp)). Google's Holiday 100 included the Cozyberry Candle Lamp (per [Yahoo coverage](https://www.yahoo.com/lifestyle/honest-review-candle-warmer-lamp-215200683.html) as summarized in search).
- **Fall / "candle season":** #13 "Fall candle season but make it non toxic".
- **Winter dry hands:** #23 (@dermguru, posted in December) and #24/#25 (posted in October).
- **Dark evenings / daylight saving:** "cozy season" and low-dopamine evening content (#30). [Irish Examiner](https://www.irishexaminer.com/lifestyle/advice/arid-41733384.html) counts **#cosyseason at 36M+ views**. [Her Campus](https://www.hercampus.com/school/tamu/resetting-your-productivity-post-daylight-savings-edition/) describes post-DST evenings as "5pm rolls around and… it's pitch black outside." **[Inference]** The US clocks change on 2 Nov 2026, one day after this report. Núan's "Close the day tonight" and "the hour after bedtime" fit this window exactly.

### Hook takeaways for Núan [Inference]
1. **The flame objection is itself a hook.** The "a flame is free" husband video and the "why do I need a lamp" doubt drive comments. Answer them directly: "A flame is free. Falling asleep with one isn't."
2. **Reply-to-comment openers** (#7, #11) are common in the lotion candle and warmer niches. The main question to answer is "can I actually put this on my skin / how hot is it?"
3. **Authority plus specificity wins in the non-toxic niche** (PMIDs, "toxicologist"). Núan's "every note named" claim needs the same level of specificity to compete, and should stay away from unsupported health claims (see the caution in section 3).
4. **No creator has yet owned the "candle that ends as cuticle balm" idea.** Massage and lotion candles on TikTok are framed around couples, sensuality and spa. Hand and cuticle care sits in a separate niche (derm, nails). Bridging the two is open territory.

---

## 2. Visual analysis (15–20 approaches)

The examples come from the verified posts above and the article descriptions. Lines marked **[Inference]** are recommendations, not observations.

| # | Visual approach | Verified example | Notes for Núan |
|---|---|---|---|
| 1 | **Lamp-glow product-in-action** (warm halogen cone over a jar, room dimmed) | Warmer posts #2–#7; article descriptions of "wooden bases, gold-tone metal arms" ([Yahoo summary](https://www.yahoo.com/lifestyle/honest-review-candle-warmer-lamp-215200683.html)) | This is Lumera's core visual. Real wood and amber glass suit the same aesthetic. |
| 2 | **Wax-pool reveal** (top-down, liquid pool after a lit period) | Massage candle how-to shorts: "light… wait 10–15 minutes for a warm oil pool, blow it out, test on your wrist" ([YouTube short](https://www.youtube.com/shorts/nOa7YvJoTts)) | The "Melt" step. Use a macro, top-down shot. |
| 3 | **Pour shot onto skin/hands** | Dame/PureWow "#waxpouringvideo" ([PureWow](https://www.tiktok.com/@purewow/video/7227493204168330542)); Rosalie lotion candle pour ([Rosalie](https://www.tiktok.com/@rosaliebodyworks/video/7399086243600026911)) | Núan's version would be a fingertip dip into the pool followed by a knuckle and cuticle rub. This is gentler than a pour and fits the ritual better. |
| 4 | **Dip-and-rub ASMR close-up** (hands, oil sheen, slow strokes) | YouTube "Warm Oil Hand Massage ASMR" ([link](https://www.youtube.com/watch?v=X16ee8fIAs8)); "Slow & Gentle ASMR – Oil Application and Hand Movements [No Talking]" ([link](https://www.youtube.com/watch?v=A8U_KaFHVxA)) | Proven ASMR genre for long-form YouTube. Cut to 6–10 s loops for Reels. |
| 5 | **Problem shot: cracked or dry hands** | Derm posts #23–#25; glove and occlusive routines | Before/after should be cautious and real, not filtered. |
| 6 | **Soot / tunneling / black-glass problem visual** | Otherland foil tunneling fix, 6.6M views ([Beauty Independent](https://www.beautyindependent.com/otherlands-candle-care-content-sizzles-tiktok/)); "blackened glass" lead-wick claim ([non-toxic search coverage](https://www.tiktok.com/@dryvonneburkart/video/7162181201346841899)); renter comment about cleaning "SOOT off my walls" (Distractify) | The lamp removes soot and tunneling. Show it as a split screen. |
| 7 | **Ingredient flat-lay / label-reading** | Non-toxic listicles #14 and #15 ("look for 100% beeswax or coconut wax… essential oils") | Show the beeswax/coconut/soy blend and the plant-fiber wick. Read the full scent note list on camera. |
| 8 | **Talking-head expert with on-screen citations** | @dryvonneburkart (PMIDs in caption); @denverskindoc | Authority format. Núan would need a real esthetician, derm or chemist, never a fake "doctor". |
| 9 | **Podcast clip / green-screen** | @steven + Dr Burkart | Low production cost; borrowed authority. |
| 10 | **Couple / reaction comedy** | @shelbanddyl husband reaction | Strong comment driver. Partner skepticism, then partner converted. |
| 11 | **"Night routine" / itinerary vlog** (lights off, lamps on, slow pacing) | @momentsabloom (~600K); Dazed's #nightroutine 9.3B; @hanauchocolat winter itinerary 338K ([Dazed](https://www.dazeddigital.com/life-culture/article/61579/1/routine-videos-tiktok-trend-psychology-gen-z-millenials)) | Núan's ritual (Glow → Melt → Seal) is ready-made for a 3-scene routine. |
| 12 | **Bedside table / "bedside basket" product stack** | @livingwithtish "bedside basket essentials", "homebody bedside table essentials" (Modash) | Show the candle and Lumera as the bedside "anchor". |
| 13 | **Simmer-pot / alternate-use hacks on the lamp** | @ourwintonhome simmer pot; chocolate-melting warmer video by Shelby Austin, 1.7M+ views (per search coverage of [Fox News](https://www.foxnews.com/video/6367047898112)) | Hacks extend reach. Keep them product-safe. |
| 14 | **TikTok Shop "unbox + glow" affiliate demo** | @vanjeafinds, @sloanevosen ("I got mine on tikt0k shop") | Fast cuts, text overlays, price callouts. |
| 15 | **Spa-night / partner treatment** | #SpaNightRoutine (~800M views per [My Imperfect Life, May 2021](https://myimperfectlife.com/news/spa-night-routine-tiktok-trend)); "Boyfriend does my skincare 🥺" (@noeminikita) | Partner hand-massage variant: "he does my cuticles". |
| 16 | **Seasonal decor framing** (fall leaves, pumpkins, Christmas styling) | #13 Fall non-toxic; TikTok Shop "Halloween candle warmer" and gothic skull warmer listings | Q4 gift-wrap, kraft box, a three-candle stack. |
| 17 | **Cottagecore / dark-cottage aesthetic** | #cottagecore tags on @ourwintonhome and @woodlarkblog beeswax spiral ("after baby goes to bed"); Pinterest Predicts reports "dark cottagecore kitchen" +915% (per [Home Accents Today](https://www.homeaccentstoday.com/trends/pinterest-predicts-comfort-and-authenticity-for-2026)) | Matches amber glass, wood and kraft. |
| 18 | **Review-comparison grid** (4 products side by side) | @missleahmei "Reviewing 4 cuticle oils!" | "Cuticle oil vs hand cream vs Núan wax pool". |

**Colors and environment [Inference, based on the examples above]:** warm amber and tungsten tones, low-key lighting, cream and oatmeal textiles, wood. Bright white is avoided except in the derm and "toxic" content, which uses bright, clinical, talking-head lighting.

**Camera angles:**
- Top-down for the pool and pour.
- 45° bedside for the lamp.
- Macro on knuckles and cuticles.
- Selfie talking-head for authority and reply-to-comment videos.

**Pacing:** ASMR and routine content is slow (1–3 s shots or long holds). TikTok Shop demos are fast (≤1 s cuts with text).

**Text overlays:** big top-third hook text is standard in TikTok Shop and derm posts. Routine videos use minimal lowercase captions (for example "bed by 8pm is my kinda fun").

---

## 3. Comment section (verbatim, with links)

I could not open TikTok or YouTube comment threads directly. The comments below are **verbatim as quoted by journalists** or come from **reply-to-comment videos**. Count: 27.

### Theme A: Skepticism / objection about the lamp (sentiment: negative to mixed)
1. "Not only did you spend money on the candle warmer, you're spending money on the electricity to warm the candle" ([Distractify](https://www.distractify.com/p/man-reacts-to-candle-warmer))
2. "*Immediately taking a candle warmer out of my cart.*" (ibid.)
3. "Not in this energy crisis!" (Ideal Home, as reported in search coverage of [Ideal Home](https://www.idealhome.co.uk/all-rooms/all-rooms-decor/candle-warmer-lamp-cost-to-run); I could not open the article itself)
4. "The light is broken within six months." (Amazon verified purchaser quoted by [AJC](https://www.ajc.com/life/private-quarters/tiktoks-candlewarmer-lamps-are-trending-inside-homes/6BB5MCUXDVDFFIXHMQXN3PS3MM))

### Theme B: Safety, kids and pets: "I need this because" (positive)
5. "Burning candles makes me nervous sometimes with the flames! Especially with littles, I love my candle warmer!" ([Distractify](https://www.distractify.com/p/man-reacts-to-candle-warmer))
6. "No but when I cleaned prolly years of SOOT off my walls/ceiling from the old renters burning hella candles… I feel candle warmers are the way to go." (ibid.)
7. "Just wait until he sees how long they last, I was also a skeptical boy…" (ibid.)
8. "Candle warmer is the best thing to use," ([Daily Dot](https://dailydot.com/glade-air-wick-plug-ins-headache))
9. "I use a candle warmer lamp, have been using the same candle, every day, 6-9 hours a day." ([Daily Dot](https://dailydot.com/bath-body-works-candle-quality))
10. "And they're a fire hazard," (on plug-ins, [Daily Dot](https://dailydot.com/glade-air-wick-plug-ins-headache))

### Theme C: Headaches, migraines and "toxic" fear (negative toward mass-market; opening for Núan)
11. "Them Bath & Body Works candles too especially mahogany teakwood," ([Daily Dot](https://dailydot.com/glade-air-wick-plug-ins-headache))
12. "Yesss gives me a migraine," (ibid.)
13. "I plugged one up next to my bed… Every night I was coughing uncontrollably. Something told me to unplug it and I was fine." (ibid.)
14. "Haven't bought B&BW in years. It's all toxic." (@authentically_rachel, [Daily Dot](https://dailydot.com/unclick/bath-body-works-chemicals-products-tiktok))
15. "I worked at B&BW in 2000 and people constantly brought these in because they damaged anything above them and started fires." (@crysteanac, ibid.)
16. "I use the water diffuser with the essential oil, it cleans the air and it's not strong at all," ([Daily Dot](https://dailydot.com/glade-air-wick-plug-ins-headache))

### Theme D: Pushback against "toxic" content (indifferent or defiant; a warning not to over-preach)
17. "You breathe in chemicals just by driving that car, walking outside… A wall plug won't kill anyone." (@heathers_03, [Daily Dot](https://dailydot.com/unclick/bath-body-works-chemicals-products-tiktok))
18. "I'm here for a good time and not a long time, may as well have my house smelling good." (@ktbee471, ibid.)
19. "Unfortunately I will keep using all of these," ("highly-favorited", [Daily Dot](https://www.dailydot.com/news/air-freshener-scents-bad-for-health/), video at 1.7M+ views)
20. "I can't give up perfumes, let me smell good even when I'm dead please," (ibid.)

### Theme E: Value and burn-time complaints (negative toward incumbents; supports "~53¢ per evening" and "3x longer")
21. "My Walmart brand candles last longer," (top comment, [Daily Dot](https://dailydot.com/bath-body-works-candle-quality))
22. "Yes' I just said the same thing yesterday! They burn way too fast for the price we pay!" (ibid.)
23. "Yes and the scent is so weak," (ibid.)

### Theme F: Questions about how to use it (neutral or curious; these are the FAQ)
24. "Can you peel it off?" Inferred from the creator reply "Replying to @kdeci no you cant peel it off, but it is the perfect transition to after care!" ([@rosaliebodyworks](https://www.tiktok.com/@rosaliebodyworks/video/7197626434624490795)). The original comment text was not visible, so this item is a paraphrase.
25. A question from @Beth's birds that prompted the reply "Elevate your home with this Electric Candle Warmer! With on and off buttons and you can also set a timer…" ([@vanjeafinds](https://www.tiktok.com/@vanjeafinds/video/7652279139596111135)). The comment text was not visible; the reply suggests it asked about timer or shut-off.

### Theme G: Tag-a-friend / sharing (positive)
26. The Baijing trade report notes that viral warmer videos draw comment sections where "viewers tag friends and buyers share experiences" ([Baijing](https://www.baijing.cn/article/47092)). No verbatim text was available.
27. Neom creator CTA-driven comment loops: "comment 'shop' & i'll send you the links to all my homebody bedside table essentials" and "comment SLEEPY…" (@livingwithtish via [Modash](https://www.modash.io/content-library/brands/neom-examples)). These prove comment-to-DM mechanics work in the sleep and cozy niche.

### Sentiment summary [Inference]

| Theme | Share of sample | Sentiment | Implication for Núan |
|---|---|---|---|
| A. Lamp cost / durability | 4 | − | Pre-empt with a spare bulb, real wood, the timer, and "candle lasts up to 3x longer" maths |
| B. Safety, kids, pets, soot | 6 | + | Lead with "no open flame while you fall asleep" |
| C. Headaches / toxic | 6 | − toward incumbents | "Balanced – gentle for sensitive noses" and "every note named" are relevant. Avoid fear claims you can't substantiate |
| D. Anti-preachy pushback | 4 | defiant | Sell pleasure and ritual first, "clean" second |
| E. Value / burn time | 3 | − toward B&BW | "53¢ per evening" works |
| F. How-to questions | 2 | curious | Make "is it hot? is it greasy? does it absorb?" content |
| G. Tag / comment CTA | 2 | + | Use comment-keyword CTAs |

**Gap:** I found no verbatim comments on massage or lotion candle videos about greasiness, absorption or burns. Review snippets on Maude Burn at [Beauty Bay](https://www.beautybay.com/p/maude/burn-massage-candle/) and [Thirteen Lune](https://thirteenlune.com/products/maude-burn-massage-candle-no-1-4oz) say it is not too hot to pour and melts in without stickiness, but those are paraphrased from search summaries, not verbatim. A search summary of a lotion candle listing also mentions a buyer calling it "very thick and 'slippery'" ([candlestock](https://www.candlestock.com/products/the-lotion-candle)). Validate these objections in comment mining once TikTok comment access is available.

---

## 4. Influencers (key creators)

| Creator | Niche | Size (verified source) | Content strategy |
|---|---|---|---|
| **@dryvonneburkart** (Dr Yvonne Burkart, toxicologist) | Non-toxic home | Follower count not verified; appeared on Diary of a CEO ([@steven clip](https://www.tiktok.com/@steven/video/7438711919600602401)) | Cites PMIDs. "Lowest risk" lists favour organic beeswax, wooden or untreated wicks and essential oils ([video](https://www.tiktok.com/@dryvonneburkart/video/7196084514521713966)). She is a **gatekeeper**: also says "no evidence beeswax purifies the air", so overclaiming will be called out. |
| **Sir Candle Man** (Kudzi Chikumbu, TikTok's creator-community lead) | #candletok reviews | Count not verified ([Fortune 40u40](https://fortune.com/40-under-40/2020/kudzi-chikumbu/), [Scentbird](https://scentbird.com/blog/?p=31043)) | Unbox, sniff, review. Says he looks for a candle's story first. Fits Núan's story-led brand. |
| **Candlestyles** | Candle making | ~1.3M followers per [IZEA](https://izea.com/resources/tiktok-influencers-strong-followings/) (older figure) | Process and ASMR pours |
| **Soyful Scents Candle Co.** | Decorative candle maker | ~816K TikTok followers per [Collabstr](https://collabstr.com/top-influencers/candles) (snapshot) | Maker content; available for paid collabs |
| **@livingwithtish** | Cozy / homebody / sleep | Followers not verified; 4 Neom posts in [Modash](https://www.modash.io/content-library/brands/neom-examples) (unlabelled engagement up to 3.7k / 1.7k) | Bedside-basket content and "comment SLEEPY" DM funnels. Strongest fit for the "hour after bedtime" angle. |
| **@sydmiller** (Sydney Miller, HOUSEWORK) | Fitness / wellness | Followers not verified (Modash "22.1k" unlabelled) | Neom brand partner; "bed before 9pm" |
| **@momentsabloom** (amy sarah) | Slow living, low-dopamine evenings | Single video ~600K views ([Irish Examiner](https://www.irishexaminer.com/lifestyle/advice/arid-41733384.html)) | Lamps, candles, "bed by 8pm". Ideal for dark-evening seasonal content. |
| **@drcharlesmd1** (Dr Charles Puza) | Dermatology | Count not verified; credited with starting #nailslugging ([Yahoo](https://news.yahoo.com/nail-slugging-latest-tiktok-trend-120042427.html)) | Hacks with a "GRANDMAS ALWAYS KNOW" tone. A natural expert for "seal your cuticles overnight". |
| **@denverskindoc / @dermguru / @drdrayzday** | Derm hand care | Not verified | Overnight occlusive and glove routines. The Núan wax pool is effectively an occlusive, which gives a credible bridge. |
| **@shelbanddyl** | Couple comedy | Not verified | Proven candle-warmer skeptic format; a paid sequel is plausible |
| **Otherland (brand)** | Candle care how-tos | 16.7K followers / 1.4M likes in 2023 ([Beauty Independent](https://www.beautyindependent.com/otherlands-candle-care-content-sizzles-tiktok/)) | **Model for Núan's organic strategy.** Short (27–31 s) problem-fix tutorials went viral 10+ times. CEO: "For this generation, TikTok has become the new Google." |

**[Inference] Creator mix for launch:**
- Two or three cozy / slow-evening creators (the @livingwithtish / @momentsabloom type).
- One derm or esthetician for hand-care credibility.
- One non-toxic "swap list" creator, but only after Núan has a full ingredient disclosure page.
- Two or three moms-after-bedtime creators. This fits the @woodlarkblog "after baby goes to bed" pattern and the postpartum self-care routine results on [TikTok "Self Care Mom Routine"](https://www.tiktok.com/discover/self-care-mom-routine).

---

## 5. Hashtags, themes and crossover trends

### Hashtags with reported volumes (dates vary, so compare with care)

| Hashtag | Reported views | Source |
|---|---|---|
| #nightroutine | 9.3B | [Dazed, Dec 2023](https://www.dazeddigital.com/life-culture/article/61579/1/routine-videos-tiktok-trend-psychology-gen-z-millenials) |
| #showertok | 6bn+ | [everything-shower coverage](https://www.womensweekly.com.sg/beauty-and-health/the-everything-shower-is-the-new-self-care-trend-to-follow) |
| #SpaNightRoutine | ~800M | [My Imperfect Life, 2021](https://myimperfectlife.com/news/spa-night-routine-tiktok-trend) |
| #everythingshower | 123.7M–300M (varies by source); ~7.5M/week per Spate | [Grazia](https://www.grazia.my/beauty/everything-shower-tiktok-beauty-trend/?page=3), [Glam](https://www.glam.com/1188503/tiktoks-relatable-everything-shower-trend-is-an-intimate-look-into-self-care-culture) |
| #candlewarmer | 57.4M–100M+ | Ideal Home, Yahoo and Taste of Home figures via search |
| #sleeptips | ~463M | [Advisorpedia](https://advisorpedia.com/viewpoints/sleeptok-anyone) |
| #candlecare | 43.2M (2023) | [Beauty Independent](https://www.beautyindependent.com/otherlands-candle-care-content-sizzles-tiktok/) |
| #cosyseason | 36M+ | [Irish Examiner, Jan 2026](https://www.irishexaminer.com/lifestyle/advice/arid-41733384.html) |
| #candlewarmerlamps | 23.3M | [Baijing, Dec 2023](https://www.baijing.cn/article/47092) |

Tags in active use on verified posts include #candletok, #nontoxicliving, #cleancandles, #nontoxiccandles, #cuticleoil, #nailcare, #dryhands, #handcream, #dermtok, #massagecandle, #lotioncandle, #cozyhome, #cottagecore, #slowliving, #amazonhome and #DealsforYouDays.

I could not verify volumes for #candletok, #sleeptok or #cozygirl.

### Content themes and emerging formats
1. **Low-dopamine / slow evenings.** Lamps instead of overheads, candles, "bed by 8pm". This is the newest and closest match to Núan.
2. **Sleepmaxxing.** Stacking small sleep habits such as magnesium and dim lights ([Elite Daily](https://www.elitedaily.com/wellness/tiktok-sleepmaxxing-trend-routine-review)). Kylie Day's sleep routine reached 8M+ views (per [Popsugar](https://popsugar.com.au/?p=931825) as summarized in search).
3. **Non-toxic swaps listicles** ("5 best non-toxic candles").
4. **Candle care how-tos** (tunneling, wick trimming). Evergreen.
5. **Candle warmer hacks** (simmer pots, melting chocolate).
6. **Comment-reply videos** and **comment-keyword DM CTAs**.
7. **Routine / itinerary videos.** Per Dazed, they appeal through "autonomy and control" and "romanticising the mundane" under cost-of-living pressure.

### Crossover trends from adjacent niches
- **Slugging → nail slugging.** Cuticle oil sealed under an occlusive, overnight ([Refinery29](https://refinery29.com/en-us/2022/08/11075755/tiktok-nail-slugging-trend), [Who What Wear](https://www.whowhatwear.com/nail-slugging)). Experts advise keeping "thicker products to your pre-bedtime routine". **This is the single best crossover for Núan.** The wax pool is a warm, self-contained version of "seal your cuticles before bed". Positioning line [Inference]: "Hand slugging, but it smells like Wild Rose."
- **Hand masks with gloves overnight** (derm content, #23–#25). Núan is a no-glove alternative.
- **Everything shower / spa night.** Multi-step self-care evenings. Núan becomes the "last step".
- **Sunday reset** ([The List](https://www.thelist.com/935230/the-tiktok-sunday-reset-trend-explained)) and **closing-shift cleaning** ([Yahoo](https://ca.style.yahoo.com/closing-shift-cleaning-why-many-224909500.html)). Núan's "Close the day tonight" mirrors closing-shift language.
- **Pinterest Predicts 2026.** Comfort found in "daily rituals", and "scent layering / scent stacking" ([Pinterest newsroom](https://newsroom.pinterest.com/en-ca/news/pinterest-predicts-nonconformity-self-preservation-and-escapism-drive-21-trends-for-2026/), [Home Accents Today](https://www.homeaccentstoday.com/trends/pinterest-predicts-comfort-and-authenticity-for-2026)).
- **Dark cottagecore / cozy decor.** Fits amber glass and real wood.

---

## 6. Content structure patterns (observed) [classification is Inference]

1. **Objection → demo → conversion** (husband skeptic → "wait until he sees how long they last").
2. **Problem close-up → fix → result** (Otherland tunneling foil fix; derm cracked-hands hack).
3. **Myth-bust authority** ("5 reasons to not burn candles" + citations → "what to look for instead").
4. **Listicle swap** ("5 best non-toxic candles", brands tagged → "look for beeswax/coconut").
5. **Comment-reply FAQ** ("Replying to @kdeci…").
6. **Routine / itinerary in 3–6 scenes** (lamp on → candle → skincare → bed; "bed by 8pm").
7. **Unbox + glow + feature stack** (TikTok Shop: timer, dimmer, "2–3x longer", "no soot").
8. **Side-by-side review** ("Reviewing 4 cuticle oils!").
9. **Hack / alt-use** (simmer pot, melt chocolate on the lamp).
10. **Launch explainer by a media brand** (PureWow: "Have you ever tried…?" → ingredients → "10/10").

## 7. CTAs observed (verbatim where available)
1. "I got mine on tikt0k shop!" (@sloanevosen)
2. "These exact ones linked on my LTK & Amazon storefront in bio 🫶🏻" (@nataliemarceta)
3. "I found this candle warming lamp on Amazon!" (@ourwintonhome)
4. "Find non-toxic candle recommendations on our website welpr.com" (@by.erinmarie)
5. "Have you ever tried a candle warmer lamp?!" (question CTA, @nataliemarceta)
6. "comment 'shop' & i'll send you the links…" (@livingwithtish)
7. "comment SLEEPY for all my bedside basket essentials" (@livingwithtish)
8. "Questions? Drop 'em in the comments :)" (@drcharlesmd1)
9. "code: NOODLE10" (discount code, [@noodle_yess](https://www.tiktok.com/@noodle_yess/video/7623179020775017741))
10. "Full conversation on The Diary Of A CEO out now 🕯️" (@steven)
11. "We give it a 10/10!" (@purewow, endorsement CTA)
12. "📌 Save this post as a reminder to unplug 🔁 Share it with someone who's always 'on'" ([@jimkwik](https://www.tiktok.com/@jimkwik/video/7557947182033194295))
13. "What other popular products/devices should we debunk?" (@drcharlesmd1, engagement CTA)
14. "Your lungs (and your space) will thank you." (@holisticeli, benefit close)

**[Inference] for Núan:** "Comment RITUAL and I'll send the scent quiz", "Save this for the first dark evening", "Tag who needs a no-flame bedtime", and "Buy 2, get the 3rd free: three months of evenings".

## 8. Offers seen in the niche
- TikTok Shop affiliate pricing and "Deals for You Days" (#DealsforYouDays tag on @vanjeafinds).
- Creator discount codes (NOODLE10).
- Neom sponsored giveaways and event sponsorships (Modash: @juliana_lovesglam giveaway, @kylashaii events).
- Warmer price anchors from $8.99 to $54.99 on TikTok Shop, and Cozyberry at $48.99 on Amazon (search coverage). **Lumera's $55 is at the top of the mass range.** It needs the real-wood, spare-bulb and timer story, and works best in a bundle ($119 set).

## 9. Durations
- Otherland viral tutorials: **27 s and 31 s** ([Beauty Independent](https://www.beautyindependent.com/otherlands-candle-care-content-sizzles-tiktok/)).
- Neom sponsored Instagram creator videos per [Modash](https://www.modash.io/content-library/brands/neom-examples): 0:07, 0:07, 0:07, 0:10, 0:32, 0:33, 0:36, 0:37, 1:00, 1:02, 1:10, 1:21, 2:15, 4:03.
  - The split is **7–10 s aesthetic loops** versus **30–70 s routines**. Long (2–4 min) pieces are event or giveaway recaps.
- **[Inference]** Test 7–9 s lamp-glow and pool loops for Reels, 20–35 s problem/fix and routine videos for TikTok, and 45–60 s UGC testimonial cuts for Facebook.

## 10. Music and sound design
- #SpaNightRoutine was soundtracked by "You Got It" by Vedo ([My Imperfect Life](https://myimperfectlife.com/news/spa-night-routine-tiktok-trend)).
- Massage and oil ASMR on YouTube is "No Talking": slow oil, hand sounds, soft pressure ([example](https://www.youtube.com/watch?v=A8U_KaFHVxA)).
- **[Inference]** For Núan, use wick-blow-out "pff", lighter click, lamp switch click, soft wax-rub sound and room tone. Use lo-fi or soft piano for routines, and a trending audio only on TikTok Shop-style demos.

## 11. UGC vs professional by platform [Inference based on the examples above]

| Platform | Dominant style in niche | Evidence |
|---|---|---|
| TikTok | UGC / affiliate demo, comment-reply, expert talking-head | @sloanevosen, @vanjeafinds, @dryvonneburkart, Otherland lo-fi tutorials |
| Instagram | Creator-aesthetic Reels, gifted/#ad partnerships, bedside flat-lays | Neom's 20+ creator posts on Modash, nearly all Instagram |
| Facebook | **Not verified (Ad Library 403, Trendtrack offline).** Expect longer UGC testimonials and older-skewing "gift for mom" angles; Neom's audience per adlibrary.com is women aged 25–54 | [adlibrary.com Neom](https://adlibrary.com/brands/neom-organics-tiktok-ads) |
| Pinterest | Decor/aesthetic stills; ritual and comfort themes rising | Pinterest Predicts 2026 |
| YouTube Shorts | How-to ("How To Use a Massage Candle!"), "candle warmer vs burning a candle — which is actually better?" comparisons, long-form ASMR | [YouTube Short](https://www.youtube.com/shorts/cePX9pVM9Ws), [How-to](https://www.youtube.com/shorts/nOa7YvJoTts) |

---

## 12. Step 9: Ad style analysis

**Caveat:** I could not pull paid-ad libraries this cycle. The examples are brand, media and creator posts, plus disclosed sponsored posts. The style classifications are my judgement from captions and coverage.

### 12.1 Professional / brand-produced (examples)
1. This Works brand post "Instantly asleep… proven to help you fall asleep faster" ([link](https://www.tiktok.com/@thisworkssocial/video/7512512683854335264))
2. PureWow Dame massage candle explainer ([link](https://www.tiktok.com/@purewow/video/7227493204168330542))
3. Apartment Therapy warmer post "This makes your candles last longer…" (AJC)
4. Otherland candle-care tutorials (brand, lo-fi but scripted)
5. Rosalie Body Works lotion candle brand videos ([1](https://www.tiktok.com/@rosaliebodyworks/video/7399086243600026911), [2](https://www.tiktok.com/@rosaliebodyworks/video/7197626434624490795))
6. Naturasoy massage candle brand post ([link](https://www.tiktok.com/@naturasoy/video/7241957790577659141))
7. Diary of a CEO podcast clip (@steven)
8. Frostbeard Studio maker post "Candle problems. Am I right, makers?" ([link](https://www.tiktok.com/@frostbeardstudio/video/7351867201793592619))
9. Fontana Candle Co. positioning: "The world is full of toxins, but we don't think they should be in your home." ([site](https://fontanacandlecompany.com/pages/about-our-candles); sells via TikTok Shop per [MyChesCo](https://www.mychesco.com/a/news/regional/fontana-candle-expands-factory-after-2-million-sales/))
10. Neom brand-partner posts (@sydmiller "as a @neomwellbeing brand partner")

### 12.2 UGC / creator (examples)
1. @shelbanddyl husband reaction
2. @sloanevosen "actually obsessed…"
3. @nataliemarceta warmer explainer
4. @vanjeafinds comment-reply affiliate
5. @ourwintonhome simmer-pot hack
6. @louiselaceda "This is why you need a candle warmer!"
7. @_bybrittney B&BW burn-time complaint (670K)
8. @therealogk_ plug-in warning (375.8K)
9. @missleahmei cuticle-oil review
10. @momentsabloom low-dopamine evening (~600K)

**Reasoning:** UGC dominates reach in this category. Every verified view count above 300K belongs to a creator or a lo-fi brand tutorial; none is a polished ad. Polished brand content shows up mainly as media-brand explainers and in the sleep category (This Works, Neom). **[Inference]** Run Núan as roughly 70/30 UGC to polished, with polished assets used as Pinterest and Meta retargeting stills and product-detail loops.

### 12.3 Style dimensions

| Dimension | What the category does (evidence) | Recommendation for Núan [Inference] |
|---|---|---|
| **Emotional vs logical** | Warmer and routine content is emotional ("cozy vibes without the worry"). Non-toxic and derm content is logical (PMIDs, "5 reasons"). Sleep brands blend both ("proven" + "instantly asleep"). | Emotional lead (closing the day, hands that feel cared for) and a logical close (no paraffin, every note named, 53¢/evening, no flame overnight). |
| **Bright vs dark** | Cozy, warmer and routine content is dark and warm (lamp glow, "leaving corners dark", per Irish Examiner). Derm and toxic content is bright and clinical. | Mostly dark-warm. Use bright only for the hand close-ups and the ingredient panel. |
| **Short vs long** | 7–10 s loops and 27–37 s tutorials or routines carry most reach. 1–4 min only for recaps (Neom/Modash durations; Otherland 27–31 s). | Mostly 8 s and 25 s cuts; a 45–60 s testimonial for Facebook. |
| **Serious vs humorous** | Mostly serious or soothing. The single biggest comment generator found is humorous (husband "a flame is free"). | Mainly serious and soothing, with a humour line built from objections (a partner skit). |
| **Presenter gender** | Overwhelmingly female creators (Neom list, warmer affiliates, routine creators). Male voices appear as skeptic (Dylan), authority (Dr Charles, Steven Bartlett) or reviewer (Sir Candle Man). | Female hand-model and narrator as the core. Test a male skeptic and a male derm. Couples' "he does my cuticles" spa-night variant. |
| **Studio vs real-world** | Real homes dominate: bedside, kitchen, cottage. Studio appears only in brand pack shots. | Real bedrooms after 9pm, with the kids' toys still visible (the "hour after bedtime" truth). |
| **Text-heavy vs image** | TikTok Shop and toxic content is text-heavy (big hook overlays, feature lists). Routine and ASMR content is image-led with minimal lowercase text. | Prospecting: one bold hook line plus image. Retargeting: a text stack of offer, scent strength and "no flame". |
| **Technical vs lifestyle** | The lamp is sold on technical features (2/4/8h timer, dimmer, 50W halogen, "2–3x longer"). Candles are sold on lifestyle. | Lumera gets one technical explainer (timer, top-down melt, no soot). The candle stays lifestyle. |

### 12.4 Risks and compliance notes from the research
- **Health claims:** "Proven to fall asleep faster" style claims, and claims like "paraffin = benzene", invite pushback. Dr Burkart herself says there is "no evidence that beeswax candles purify the air". Núan should avoid sleep-efficacy and detox claims and keep to sensory and ritual benefits.
- **Massage and lotion candle associations:** on TikTok these skew toward couples, sensuality and kink tags (#waxplay and #kinktok on Rosalie posts). Hand and cuticle framing keeps Núan out of restricted-content ad review and is clearer to understand.
- **Social proof:** the brief notes "4.7 stars from 6,800+ reviews" on a brand created on 2026-10-31. Do not put that number in ads until it is verifiable. Comment culture in this niche is quick to call things out (Theme D).

---

## Sources (primary links used)
Distractify; AJC; Yahoo/House Beautiful; Daily Dot (four articles); Beauty Independent; Irish Examiner; Dazed; My Imperfect Life; Baijing; Modash Neom index; adlibrary.com Neom; Refinery29 / Who What Wear / Yahoo on nail slugging; Pinterest newsroom and Home Accents Today; plus the individual TikTok and YouTube URLs given inline. Trendtrack: unavailable (0 credits, reset 2026-11-10).
