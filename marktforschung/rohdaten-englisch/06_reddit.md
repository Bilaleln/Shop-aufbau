# Step 6: Reddit Research for Núan Ritual Candle

Fetched 2026-11-01. Every quote below is copied exactly from a Reddit thread I fetched, and the thread URL is given with it. Spelling, emoji and typos are left as they were; the only change is that curly apostrophes and quotation marks are shown as straight ones. "..." marks text I cut, either by choice or because my capture was truncated.

## Method and access notes (read first)

- **Blocked:** Reddit's JSON API (`/search.json`, `/comments/ID/.json`, `old.reddit.com`, `api.reddit.com`) returned **HTTP 403 "blocked by network security"** from Reddit itself. The agent proxy was not involved. `old.reddit.com` redirected to a login wall (403). PullPush returned 522.
- **What worked:** Reddit's public **RSS/Atom feeds**: `https://www.reddit.com/r/SUB/search.rss?q=...&restrict_sr=1` for search, and `https://www.reddit.com/r/SUB/comments/ID/.rss?limit=N` for a thread plus its comments. In total I read about 95 threads in full or in part, and ran about 50 searches.
- **Limitations:**
  - RSS returns up to about 50 to 60 comments per thread, flattened and in Reddit's default order, so I could not see reply nesting.
  - Very long comments were truncated in my capture at about 420 to 650 characters. Those quotes end in "...".
  - I saw only search-result titles, not thread contents, for r/DIY, r/Fragrance and r/CozyPlaces. I quote nothing from them.
  - **Major gap:** I found almost no buyer-side posts reviewing massage or lotion candles used as hand balm. Nearly all massage-candle discussion comes from makers (r/candlemaking). That gap is a finding in its own right (see Patterns).

## Subreddits covered (20) and relevance

| Subreddit | Relevance to Núan |
|---|---|
| r/Candles | Core. Warmers vs. burning, tunneling, soot, headaches, price, the luxury-candle mindset. Very active. |
| r/candlemaking | Only real source on massage and lotion candles (maker side): IFRA 5A, fragrance load, wick and overheating, "people need to learn how to use it". |
| r/bathandbodyworks | Mass-market candle culture. Many headache threads, "warmer fixed my headaches" testimonials, sale-price anchoring ($10 to $15). |
| r/migraine | The "avoids candles" segment. Scent triggers vary by person, regifting, beeswax tolerance. |
| r/nontoxic | Paraffin and fragrance fear, beeswax price shock, the "perfect vs good enough" mindset. |
| r/SkincareAddiction | Dry and cracked hands, overnight hand cream plus gloves, greasiness complaints, luxury hand cream. |
| r/nursing | Hands constantly in water and sanitizer. Strong loyalty to O'Keeffe's Working Hands and a "before bed + gloves" ritual. |
| r/eczema | Night hand coverage: gloves slide off, socks scrape off ointment. |
| r/Nails | Cuticle oil routines, cuticle healing as self-care and habit replacement, shame about hands. |
| r/ADHD | Revenge bedtime procrastination, forgetting to blow out candles, the "fixed end point" activity insight. |
| r/sleep, r/insomnia | Wind-down routines, phone-out-of-bedroom, "convince your brain the day is over". |
| r/selfcare | Low-effort, non-performative evening rituals. Lamp, candle, lotion, tea. |
| r/Anxiety | The nightly anxious spiral. |
| r/Mommit, r/Parenting, r/beyondthebump | The "hour after bedtime" as precious me-time, kids and candles, VOC worries with newborns. |
| r/ZeroWaste | Lotion bars (DIY and bought): greasy, waxy, "my skin isn't warm enough". |
| r/GiftIdeas | Candles seen as a generic or low-effort gift. Self-care gifts under $40. |
| r/BuyItForLife | Little interest in candle warmers ("wtf is a candle warmer?"). |

---

## 1. Desires, and what satisfying them means emotionally (31 quotes)

**Closing the day and the ritual itself**
1. "for me it's mostly the ritual tbh. lighting one doesn't magically relax me, but it does make my room feel less chaotic and kinda tells my brain the day is over." ([r/Candles](https://www.reddit.com/r/Candles/comments/1t0esny/do_candles_really_help_you_unwind_or_is_it_just/))
2. "Try to consider, like, wind-down routine isnot about making yourself sleepy, it is about convincing your brain that the day is over. That is more important." ([r/sleep](https://www.reddit.com/r/sleep/comments/1uv2db0/what_is_your_wind_down_routine_when_does_it_start/))
3. "It's about the whole relaxing ambience it creates plus the ritual of reaching for the matches and lighting the candle." ([r/Candles](https://www.reddit.com/r/Candles/comments/1t0esny/do_candles_really_help_you_unwind_or_is_it_just/))
4. "Around 9 I turn off the big lights and just use a lamp. Phone goes on the charger in the kitchen, not next to the bed. I make a mug of herbal tea (usually something minty) and read a few pages of whatever book I'm on." ([r/selfcare](https://www.reddit.com/r/selfcare/comments/1wyx8j4/the_boring_little_evening_routine_that_actually/))
5. "The lamp thing is the real hidden gem, that transition from overhead lighting to something softer changes the whole room dynamic" ([r/selfcare](https://www.reddit.com/r/selfcare/comments/1wyx8j4/the_boring_little_evening_routine_that_actually/))
6. "Don't want to commit to a whole routine- take a shower with the lights off and light candle. Instant bliss." ([r/selfcare](https://www.reddit.com/r/selfcare/comments/1ul2wak/whats_a_selfcare_habit_that_actually_feels/))
7. "I'm trying to figure out what self-care looks like when you're tired, mentally fried, and don't want to commit to a whole routine." ([r/selfcare](https://www.reddit.com/r/selfcare/comments/1ul2wak/whats_a_selfcare_habit_that_actually_feels/))
8. "A lot of routines end up feeling like another task list: skincare, supplements, stretching, journaling, sleep routine, water intake. Useful, yes, but not always calming." ([r/selfcare](https://www.reddit.com/r/selfcare/comments/1urf1r3/whats_one_selfcare_habit_that_actually_calms_your/))
9. "I never make plans for Monday eve it's my reset time." ([r/selfcare](https://www.reddit.com/r/selfcare/comments/1ul2wak/whats_a_selfcare_habit_that_actually_feels/))
10. "My candles and lotions 😭 I love smells I can't do the "no smell is the best smell" most non-toxic people recommend. I love taking a shower and getting out to put on some smell good lotion, putting candle under my candle lamp, and reading a book." ([r/nontoxic](https://www.reddit.com/r/nontoxic/comments/1wb2gkf/the_one_thing_you_struggle_to_swap/))

**Taking back the hour after bedtime (revenge bedtime procrastination, parents)**

11. "I've recently learned this behavior is called "revenge bedtime procrastination," where people sacrifice sleep to reclaim personal time lost to demanding schedules." ([r/ADHD](https://www.reddit.com/r/ADHD/comments/1ip680q/how_do_you_keep_your_revenge_bedtime/))
12. "...not because I'm not tired, but because going to sleep means facing another day at a job I despise." ([r/ADHD](https://www.reddit.com/r/ADHD/comments/1ip680q/how_do_you_keep_your_revenge_bedtime/))
13. "So recently I've started giving myself an activity that i really enjoy with an end point when I get in from work." ([r/ADHD](https://www.reddit.com/r/ADHD/comments/1ip680q/how_do_you_keep_your_revenge_bedtime/))
14. "It sounds incredibly silly, but I will ask myself "if tomorrow me could take to me right now, what would she ask? What does she need from you?" And most of the time it is get some rest." ([r/ADHD](https://www.reddit.com/r/ADHD/comments/1ip680q/how_do_you_keep_your_revenge_bedtime/))
15. "The time when they sleep and I don't is precious, I'm not going to waste it on cleaning." ([r/Parenting](https://www.reddit.com/r/Parenting/comments/1oa9hc4/other_than_cleaning_what_do_you_do_in_your_free/))
16. "I would exist without checking a baby monitor or listening for suspicious thuds" ([r/Mommit](https://www.reddit.com/r/Mommit/comments/venbp2/whats_your_mom_daydream/))
17. "I just want a beautiful, deep, big tub to soak in while I watch TV and eat chocolate alone in peace." ([r/Mommit](https://www.reddit.com/r/Mommit/comments/venbp2/whats_your_mom_daydream/))

**Hands: dignity, not just moisture**

18. "I am so self conscious of my hands. They are so gross looking and they itch and hurt and I'm sick of it. ... Yesterday a coworker asked about them and I had an anxiety attack in the bathroom. I just want to go back to having normal healthy skin." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1d19yjy/misc_im_so_tired_of_itchy_sore_cracking_dry/))
19. "So dry, cracked, red, scaly. Patients comment on them to me honestly 😭." ([r/nursing](https://www.reddit.com/r/nursing/comments/1sdjc5z/dry_hand_tips/))
20. "I've been insecure about my hands my entire life because of this and I've had a lot of people ask/comment what's wrong with them." ([r/Nails](https://www.reddit.com/r/Nails/comments/1fphko4/i_promise_your_cuticles_will_heal_with_time_and/))
21. "Replaced self destructive behavior with self care on my nails." ([r/Nails](https://www.reddit.com/r/Nails/comments/1fphko4/i_promise_your_cuticles_will_heal_with_time_and/))
22. "The brush is still super satisfying to do (✨dopamine✨) so it actually works to replace the habit for me." ([r/Nails](https://www.reddit.com/r/Nails/comments/1fphko4/i_promise_your_cuticles_will_heal_with_time_and/))
23. "Like some magic cream that makes hands luxuriously soft." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1hljc70/product_question_best_luxury_hand_cream/))
24. "Yuuuuuup. I slather it on before bed, don cotton gloves, and wake up silky soft and hydrated." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))

**The warm-balm idea, and safety as peace of mind**

25. "Personally, I think the idea is absolutely amazing, a candle that isn't just an ordinary candle, but one you can actually use for real benefits." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1ura47i/massage_candles_skincare_candles/))
26. "But I personally love the idea of lotion or massage candles, even if it's just for my own use, because the warmth of it feels wonderful especially with chronic pain." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1r3n94e/massage_candle/))
27. "I really want to get a candle warmer so I can finally be able to buy candles and not worry about setting the fire alarm off in my bedroom" ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
28. "I like the peace of mind of not having a lit flame with smoke in a small apartment with pets." ([r/Candles](https://www.reddit.com/r/Candles/comments/1awjjp9/whats_the_hype_around_candle_warmers/))
29. "Plus, no soot and no fear of "Did I forget to blow the candle out?"" ([r/Candles](https://www.reddit.com/r/Candles/comments/1pnlwr2/candle_warmers_vs_burning/))
30. "I barely buy big expensive candles for myself, but you better believe I love receiving them as gifts. Particularly if they're in a fancy jar that can serve as decor even after the candle has burned down." ([r/GiftIdeas](https://www.reddit.com/r/GiftIdeas/comments/1vn7zkd/selfcare_gift_under_40_that_actually_gets_used/))
31. "a good candle with the right scent just hits, i've got one on my desk rn that i light almost every evening" ([r/GiftIdeas](https://www.reddit.com/r/GiftIdeas/comments/1vn7zkd/selfcare_gift_under_40_that_actually_gets_used/))

**What satisfying these desires means emotionally:**
- Permission to stop: a signal that the day is over.
- Control over a small window of time that belongs to them.
- Relief from shame about their hands.
- Safety they don't have to monitor.
- Comfort that takes no extra effort.

People keep separating "performative" self-care from things that genuinely calm them, and they want the second kind.

---

## 2. Failed attempts (24 quotes)

**Hands**
1. "I have been trying the following and they have all helped slightly but haven't significantly reduced the issue" ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1d19yjy/misc_im_so_tired_of_itchy_sore_cracking_dry/))
2. "on days when my hands are particularly bad O'Keefe's makes my hands sting too 🥲 sometimes it straight up burns and I have to wash it off because it makes the problem so much worse." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1d19yjy/misc_im_so_tired_of_itchy_sore_cracking_dry/))
3. "One of the problems is that I apparently rip them off in the middle of the night 😅 and wake up the next morning wondering where tf the gloves went lol" ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1d19yjy/misc_im_so_tired_of_itchy_sore_cracking_dry/))
4. "Using socks as recommended by the doctor is not really working out for me (they either slide off in the middle of the night even with hairties around the wrists or completely scrape off my glob of medicine and aquaphor)." ([r/eczema](https://www.reddit.com/r/eczema/comments/1wi0ci4/covering_hand_eczema_night/))
5. "I use cotton gloves, but the cream soaks in too much. And if I use the same gloves for a couple of nights, they feel gross." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1lczt3e/routine_help_silk_gloves_over_hand_cream/))
6. "I've tried a lot of things over the years and nothing has made a huge difference - O'keeffe's did not do it..." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1qvpwj4/routine_help_hand_and_cuticle_dry_burning_and/))
7. "I bought their retinol and regular hand cream...and I hate them both. They absorb like water - moisturizes for a hot minute then it's as if it just disappears" ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1hljc70/product_question_best_luxury_hand_cream/))
8. "The bath and body works hand creams I have on hand aren't doing the job for me - I still have nasty raspy lizard hands." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
9. "FWIW I felt the Bath and Body lotions/creams did absolutely nothing for me. They smell nice but that's about it." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
10. "lotion/cuticle oil night& day, but I miss ONE time of lotion and they look like this." (title, [r/Nails](https://www.reddit.com/r/Nails/comments/14tic32/please_help_posted_here_before_my_cuticles_still/))
11. "Rubber gloves just fling water everywhere, so I don't use them." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1olthz3/product_request_searching_for_a_good_nongreasy/))

**Lotion bars, the closest existing format to a solid balm**

12. "It's overall very greasy and leaves waxy pills/flakes everywhere. Also it rubs off white on clothing. My only option is to use it before bed and hope it doesn't mess up my sheets." ([r/ZeroWaste](https://www.reddit.com/r/ZeroWaste/comments/f32bl9/ethique_lotion_bar_overall_greasy_and_waxy_flakes/))
13. "My skin isn't warm enough for them to work. If I go to the effort to heat them up first they are fine but I don't have the stamina." ([r/ZeroWaste](https://www.reddit.com/r/ZeroWaste/comments/1bnsakb/experience_with_lotion_bars/))
14. "I've spent way too much money on trying to find the best lotion bar, so I too would love to know!" ([r/ZeroWaste](https://www.reddit.com/r/ZeroWaste/comments/1bnsakb/experience_with_lotion_bars/))
15. "the oils just sit on my skin and don't absorb. Then I don't have hours to sit around and let them absorb, so the oils get on my clothes" ([r/ZeroWaste](https://www.reddit.com/r/ZeroWaste/comments/1bnsakb/experience_with_lotion_bars/))

**Candles and warmers**

16. "I can let a candle stay lit for 4, 5, 6+ hours on the first melt and it will still never reach the sides, they ALWAYS tunnel." ([r/Candles](https://www.reddit.com/r/Candles/comments/1rlz6k4/candles_tunnel_no_matter_what/))
17. "Scents that gave me headaches while burning still give me headaches when used with a warmer." ([r/bathandbodyworks](https://www.reddit.com/r/bathandbodyworks/comments/1j5vn8j/less_headaches_with_candle_warmer_than_burning/))
18. "Never had a problem when I was burning it, but when I put it under the warmer I got the most atrocious headache, and I NEVER get headaches." ([r/bathandbodyworks](https://www.reddit.com/r/bathandbodyworks/comments/1j5vn8j/less_headaches_with_candle_warmer_than_burning/))
19. "I just bought from etsy (voltive & a pillar) & neither burned well & I always have problems when I buy from Etsy." ([r/Candles](https://www.reddit.com/r/Candles/comments/1q9xwzt/seeking_good_beeswax_candle_companies/))

**DIY massage candles (makers)**

20. "the problem is when i pour the blend on skin its cools down rapidly and the melted wax blend becomes waxy…" ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1bj70fo/massage_candles/))
21. "I make massage candles and the wax that's used to rub on the body ends up smelling burnt." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1cr73r1/massage_candle_smells_burnt_help/))

**Wind-down and sleep**

22. "I've tried different night routines, that lasted about four days lol" ([r/selfcare](https://www.reddit.com/r/selfcare/comments/1wyx8j4/the_boring_little_evening_routine_that_actually/))
23. "I've tried sleeping pills and overworking out, even HIIT, I was in sport before so I worked out and put my body in extreme pressure on daily basis. But nothing effects this!! NOTHING!!!" ([r/ADHD](https://www.reddit.com/r/ADHD/comments/1lkgtzm/revenge_bedtime_procrastination/))
24. "I still use my phone lol cuz what else am I gonna do? I have a short attention span and don't enjoy reading books." ([r/sleep](https://www.reddit.com/r/sleep/comments/o00lki/has_anyone_been_able_to_consistently_hit_their/))

---

## 3. Success stories (12 quotes)

1. "Anyways I gave it a try and my life changed. Within like 2 short weeks my hands completely healed." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
2. "I put on working hands once a day before bed and that pretty well keeps dry hands away even with frequent hand washing at work." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
3. "Pic 1 & 2 are before, pic 3 is after 2 weeks of oiling, and pic 4 is 6 weeks of oiling. I chewed and picked my fingers for about 30 years" ([r/Nails](https://www.reddit.com/r/Nails/comments/1fphko4/i_promise_your_cuticles_will_heal_with_time_and/))
4. "Just got them yesterday, and tried them last night. They are GREAT! They don't absorb the hand cream and don't let it ooze through. They keep it on my hands but aren't hot. Best $20 in skincare that I've spent in ages!" ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1lczt3e/routine_help_silk_gloves_over_hand_cream/))
5. "I received a candle melting lamp for Christmas and quickly noticed candles that previously caused head aches no longer made me sick!" ([r/bathandbodyworks](https://www.reddit.com/r/bathandbodyworks/comments/1hn8k1y/no_headaches_after_switching_to_candle_melter/))
6. "It was the burning of the wicks causing them. Since getting a warmer no more headaches. I might sneeze a little but that's it." ([r/bathandbodyworks](https://www.reddit.com/r/bathandbodyworks/comments/1j5vn8j/less_headaches_with_candle_warmer_than_burning/))
7. "I was already told about how to handle tunneling, which was to leave the candle lit for 4 hours, but sometimes it still does it unevenly. This way makes sure it doesn't happen ever & I love that!" ([r/Candles](https://www.reddit.com/r/Candles/comments/1qy8gka/candle_warmer_lamps_are_goated/))
8. "I got one for my bathroom because my bf left a candle lit one night when he fell asleep and I discovered it the next morning. Immediately, I was like "that was our freebie from the universe. Let's not press our luck."" ([r/Candles](https://www.reddit.com/r/Candles/comments/1akuxw8/i_fell_victim_to_the_trend/))
9. "I used to lie awake for an hour, but now I get drowsy just going through the steps." ([r/sleep](https://www.reddit.com/r/sleep/comments/1kpgxry/i_created_a_winddown_routine_before_bed_its/))
10. "Not having a phone/ipad in bed did have a HUGE impact on me hitting my sleep goals and getting better sleep." ([r/sleep](https://www.reddit.com/r/sleep/comments/o00lki/has_anyone_been_able_to_consistently_hit_their/))
11. "I make massage candles and people love them! They dont sell as fast as my regular candles, but there is definitely a market for them. Lots of repeat customers, as its kind of a niche product." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1r3n94e/massage_candle/))
12. "Massage candles are totally a thing! I make them myself and they sell really well. Yes, they are super moisturizing and feel great on the skin." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1ura47i/massage_candles_skincare_candles/))

---

## 4. Disappointments and frustrations (13 quotes)

1. "Why do people always buy candles when they don't know what to get people??!" ([r/migraine](https://www.reddit.com/r/migraine/comments/190isph/just_staring_at_all_the_candles_i_got_as/))
2. "I feel high maintenance asking folks not to burn them, then wind up regretting not saying something. Sigh." ([r/migraine](https://www.reddit.com/r/migraine/comments/1hlrvvf/scented_candles_do_others_struggle_with_them/))
3. "I love candles so much, that being said walking into a candle store/aisle is a 89% of a migraine." ([r/migraine](https://www.reddit.com/r/migraine/comments/1hlrvvf/scented_candles_do_others_struggle_with_them/))
4. "I fell asleep, burning a five wick wax candle and woke up to my room, smoky and covered in soot. My poor dog 😭😭😭" ([r/Candles](https://www.reddit.com/r/Candles/comments/1o9yvqj/this_is_your_reminder_to_not_fall_asleep_while/))
5. "My white comforter was grey, my fan was black, any bit of dust in the room was black, baseboards, air purifier filter was black" ([r/Candles](https://www.reddit.com/r/Candles/comments/1o9yvqj/this_is_your_reminder_to_not_fall_asleep_while/))
6. "...ended up having to do a deep cleaning of the walls and ceilings because they were COVERED in a thin layer of soot." ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
7. "I can handle some scented candles but it is limited. Even with the ones I can stand, if I light them I get very headachy and nauseated ... So, I just buy candles but never burn them. LOL" ([r/Candles](https://www.reddit.com/r/Candles/comments/1o3ctuh/my_mom_cant_stand_the_scent_of_burning_candles/))
8. "OH MY GOD You're supposed to dump the layer of wax?????!!!!! No wonder why my candles stopped smelling" ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
9. "I had one about 20yrs ago but lost interest when I had to replace expensive bulbs" ([r/Candles](https://www.reddit.com/r/Candles/comments/1awjjp9/whats_the_hype_around_candle_warmers/))
10. "Winter. I loved the scent cold but every time it was lit I had the worst migraine." ([r/bathandbodyworks](https://www.reddit.com/r/bathandbodyworks/comments/tp3j0z/does_anyone_have_a_candle_scent_they_like_but/))
11. "It's a sick joke that to keep your hands clean you have to destroy your skin 😔 I hate when they first start to get dry and my hands start to get that weird papery feeling to them" ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1vl7gv7/review_do_people_ever_talk_about_okeefes_working/))
12. "Aquaphor helps me a lot. But I only use it before before bed because in the day I'd leave a trail of petroleum slime everywhere like a snail." ([r/eczema](https://www.reddit.com/r/eczema/comments/1rghfae/great_trick_for_stupid_cotton_gloves_with_hand/))
13. "I just spent a lot of money with that Bluecorn company & the EO smelled so strong ... It was way too strong for me" ([r/Candles](https://www.reddit.com/r/Candles/comments/1q9xwzt/seeking_good_beeswax_candle_companies/))

---

## 5. Questions people ask before buying (12 quotes)

1. "Are massage candles practical?" ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1ura47i/massage_candles_skincare_candles/))
2. "What's a massage candle??" ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1fnwa54/massage_candle/))
3. "Can someone explain to me why people prefer a candle warmer over burning them?" ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
4. "theyre quite expensive but im also annoyed by all the soot caused by my candles. i like the atmosphere they create but the fire also makes me nervous. they seem like a safer alternative, but the way they're presented online makes them seem too good to be true. do they have any downsides?" ([r/Candles](https://www.reddit.com/r/Candles/comments/1pnlwr2/candle_warmers_vs_burning/))
5. "Does this still produce a glow or is it more like a lamp? One of my favorite parts of candles is the glow" ([r/Candles](https://www.reddit.com/r/Candles/comments/1hzyz1n/do_you_use_a_candle_warmer_or_prefer_lighting/))
6. "I suffer from headaches when lighting candles and was wondering if a candle warmer would help with this issue?" ([r/bathandbodyworks](https://www.reddit.com/r/bathandbodyworks/comments/1j5vn8j/less_headaches_with_candle_warmer_than_burning/))
7. "Do I dump out however much wax melted? How many times can I warm a candle??" ([r/Candles](https://www.reddit.com/r/Candles/comments/1qy8gka/candle_warmer_lamps_are_goated/))
8. "I am wondering how much the wax type matters, or what options are safe 'enough'." ([r/nontoxic](https://www.reddit.com/r/nontoxic/comments/1xegiso/unscented_candles_whats_the_consensus_on_whats/))
9. "Can anyone tell me if you've had any bad effects of burning candles around newborns?" ([r/beyondthebump](https://www.reddit.com/r/beyondthebump/comments/7a5c8i/candles_and_newborns/))
10. "Obviously there's no flame or smoke but not sure if there are VOCs or anything given off in the scent that would irritate little noses or lungs?" ([r/beyondthebump](https://www.reddit.com/r/beyondthebump/comments/2ya41e/wax_meltscandle_warmersprobably_a_dumb_question/))
11. "Would silk gloves be better? I don't understand whether the silk would keep the cream on my hands or soak it up." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1lczt3e/routine_help_silk_gloves_over_hand_cream/))
12. "I'm wondering if this (expensive for me) candle is burning as it should." ([r/Candles](https://www.reddit.com/r/Candles/comments/1qcbqmu/first_time_nice_candle_user_is_this_a_correct/))

---

## 6. Objections and hesitations (16 quotes)

**About a candle you put on your skin**
1. "I would be scared of the candle burning me on my skin when I want to apply it" ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1ura47i/massage_candles_skincare_candles/))
2. "It sounds cool but from a skincare perspective it is pretty dumb." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1ura47i/massage_candles_skincare_candles/))
3. "Oooh! I have an even better idea! What if instead of a candle, it's a moisturizing bar with actual ingredients that are good for skin and where there's no fire involved?" ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1ura47i/massage_candles_skincare_candles/))
4. "I'd say there's a good reason sex shops stopped selling them a while ago and maybe you should find out what that was before you try" ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1ura47i/massage_candles_skincare_candles/))
5. "It's a massage candle. The melted wax is supposed to go on skin. Lilies are known for causing rashes." ([r/Candles](https://www.reddit.com/r/Candles/comments/1j3orel/how_to_get_pollen_out_of_massage_candle/))
6. "Lotions normally have a 2% fragrance load so the problem with massage candles is if you use 8% to give the candle a nice hot throw, the skin is left smelling awful/overpowered because it's 4x the amount you would put in a lotion." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1r70o86/urgent_massage_oil_candles/))
7. "I know that some were not made with proper low melt waxes or skin safe fragrances, so people could get burnt from the wax, or get a rash because the fragrance oils were skin safe [sic]." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1fnwa54/massage_candle/))
8. "These other reps are telling customers that they can use the wax from the candles as lotion. Or massage oil. I'm all against this because it's soy wax, and has fragrance oils etc in it." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/23eukj/wax_as_lotion/))

**About scent, toxicity and warmers**

9. "Theres no such thing as a universally "migraine safe" scent" ([r/migraine](https://www.reddit.com/r/migraine/comments/1ox5fdm/candleslotions_that_are_safe_for_migraines/))
10. "Breathing in burnt particles is never going to be "non toxic"." ([r/nontoxic](https://www.reddit.com/r/nontoxic/comments/1xegiso/unscented_candles_whats_the_consensus_on_whats/))
11. "it isn't the burning of the candle that causes reactions, it's the ingredients so using a melter won't change the reaction." ([r/Candles](https://www.reddit.com/r/Candles/comments/1awjjp9/whats_the_hype_around_candle_warmers/))
12. "I can't imagine melting candles for fragrance by using electric device, sorry. Candles are made for burning them." ([r/Candles](https://www.reddit.com/r/Candles/comments/1hzyz1n/do_you_use_a_candle_warmer_or_prefer_lighting/))
13. "Scented lotions are a no go! The scents have alcohol in them and actually irritate and dry your hands more." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
14. "personally, as someone with sensory issues, I've never liked how greasy it stays on the hands." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1vl7gv7/review_do_people_ever_talk_about_okeefes_working/))
15. "I've found many "pet safe" candle companies but none seem to actually be cat safe, they just basically are paraffin free." ([r/Candles](https://www.reddit.com/r/Candles/comments/1juw542/cat_safe_options/))
16. "We had to ask people closer to us to stop getting us candles because we barely use them and they are piling up." ([r/GiftIdeas](https://www.reddit.com/r/GiftIdeas/comments/1pe71x7/how_bad_are_mugs_and_candles_as_gifts/))

---

## 7. How people describe their "holy grail" (10 quotes)

1. "Working hands is the only right answer. Whatever they put in that stuff, it works miracles." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
2. "Working Hands is the shit. I put that on every night after my shower when I crawl into bed. It's the only thing I trust." ([r/nursing](https://www.reddit.com/r/nursing/comments/zle8y3/best_hand_cream_you_guys_use_for_severely_dry/))
3. "goldbond: healing hand cream or the normal healing cream. YOULL NEVER stop using this once you start" ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
4. "The only hand cream I've tried which heals them almost overnight is called Duke Cannon Bloody Knuckles Hand Repair Balm." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1hljc70/product_question_best_luxury_hand_cream/))
5. "The packaging isn't fancy so people sleep on it but it does the job with no fuss and isn't expensive." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1vl7gv7/review_do_people_ever_talk_about_okeefes_working/))
6. "Try one. You wont be disappointed. You won't go back. I shook my head when my partner bought hers, now I want one." ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
7. "Dude I love mine!! I never have to buy candles again. My favorite ones just last forever! It's fantastic!" ([r/Candles](https://www.reddit.com/r/Candles/comments/1akuxw8/i_fell_victim_to_the_trend/))
8. "Cleanest, most pleasant burn I've experienced from a beeswax candle." ([r/nontoxic](https://www.reddit.com/r/nontoxic/comments/1xegiso/unscented_candles_whats_the_consensus_on_whats/))
9. "Like it's not cozy, or fresh but kinda powdery cold but warm it smells like dreamy. Not sweet at all." ([r/Candles](https://www.reddit.com/r/Candles/comments/1v6c4hn/been_falling_asleep_really_well_to_this_candle/))
10. "All naturally made and don't burn with soot. The only candles i can burn now!" ([r/migraine](https://www.reddit.com/r/migraine/comments/1nzp56m/mild_smelling_candle_brands/))

**What these have in common:**
- Exclusivity: "the only thing I trust" / "the only right answer".
- Speed of results: "almost overnight", "2 short weeks".
- No fuss.
- Lasting a long time: "last forever".
- Repeated nightly use tied to getting into bed.

---

## 8. How people decide (10 quotes)

1. "it's overpriced when you aren't willing to pay the asking price for it. there are two perspectives to value. price and percieved quality." ([r/Candles](https://www.reddit.com/r/Candles/comments/151nmxi/when_does_a_candle_become_overpriced/))
2. "I've definitely had things where the presentation, packaging and whole first experience make the purchase feel special, but obviously that novelty only works once." ([r/Candles](https://www.reddit.com/r/Candles/comments/1wq5a5i/what_makes_a_luxury_home_fragrance_purchase/))
3. "My customers enjoy how long the candles last and how good the hot throw is." ([r/Candles](https://www.reddit.com/r/Candles/comments/1wq5a5i/what_makes_a_luxury_home_fragrance_purchase/))
4. "I learned I was willing to shell out for something higher quality that lasted me longer and didn't cause headaches. I also tend to like milder scents that aren't overtop" ([r/Candles](https://www.reddit.com/r/Candles/comments/1qzhbib/recommended_candle_brands_for_sensitivities/))
5. "Generally speaking, higher-end candles are more compatible with respiratory issues." ([r/Candles](https://www.reddit.com/r/Candles/comments/1qzhbib/recommended_candle_brands_for_sensitivities/))
6. "If I had a really high end candle I'd definitely use the warmer over burning it." ([r/Candles](https://www.reddit.com/r/Candles/comments/1pnlwr2/candle_warmers_vs_burning/))
7. "I'm actually considering finally treating myself to a Diptique candle since it will last much longer with the lamp." ([r/Candles](https://www.reddit.com/r/Candles/comments/1akuxw8/i_fell_victim_to_the_trend/))
8. "I would stay clear of scented items unless you see her using a specific scent, then you know she can tolerate it." ([r/migraine](https://www.reddit.com/r/migraine/comments/1ox5fdm/candleslotions_that_are_safe_for_migraines/))
9. "PF Candle Co I think has a throw meter on their site." ([r/Candles](https://www.reddit.com/r/Candles/comments/1o3ctuh/my_mom_cant_stand_the_scent_of_burning_candles/))
10. "I'm trying to evaluate an distinguish between 'perfect' and kind of 'good enough', if that makes sense." ([r/nontoxic](https://www.reddit.com/r/nontoxic/comments/1xegiso/unscented_candles_whats_the_consensus_on_whats/))

---

## 9. Comparisons with alternatives (12 quotes)

1. "I prefer them because a candle I can get 4-5 "burns" out of, I can get 20+ warming sessions out of." ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
2. "I've switched back to burning. The lamp definitely lets the candle throw more, but it's using up the fragrance oil, whereas the strength stay consistent if I let a candle burn on its own." ([r/Candles](https://www.reddit.com/r/Candles/comments/1hzyz1n/do_you_use_a_candle_warmer_or_prefer_lighting/))
3. "I love burning, I love that little fire, the ambiance it provides, the memories it sparks. Fire is amazing." ([r/Candles](https://www.reddit.com/r/Candles/comments/1pnlwr2/candle_warmers_vs_burning/))
4. "Scented wax will release the same amount of scent when the wax is heated to a certain temperature, whether it is by wick or by warmer." ([r/Candles](https://www.reddit.com/r/Candles/comments/1awjjp9/whats_the_hype_around_candle_warmers/))
5. "Use Fragranced cubes and a warmer! All the great fragrance and No Soot or Smoke! ... you can get 10 different scents for less cost than a large candle :)" ([r/Candles](https://www.reddit.com/r/Candles/comments/1o3ctuh/my_mom_cant_stand_the_scent_of_burning_candles/))
6. "you can try simmering some spices and fruit peels/slices on a pot on the stove, like cinnamon sticks, clove pieces, orange peels, etc." ([r/Candles](https://www.reddit.com/r/Candles/comments/1o3ctuh/my_mom_cant_stand_the_scent_of_burning_candles/))
7. "The good (?) news is that, even though I'll burn some fancy-ish coconut, apricot, etc wax when I can afford it, nothing seems to have a throw like paraffin. 😅" ([r/Candles](https://www.reddit.com/r/Candles/comments/1hxzri5/are_bath_and_body_work_candles_toxic/))
8. "You can find beeswax candles, and they will last. The trade-off is they are more money up front and they don't throw as well. BBW candles do throw!" ([r/Candles](https://www.reddit.com/r/Candles/comments/1kgbpo3/bath_and_body_overpriced/))
9. "Vaseline doesn't absorb. It costs and makes a barrier. Add a lotion with hyaluronic acid under the Vaseline. It's magic." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
10. "I've found that using a balm or salve (oil/beeswax based rather than emulsified like a lotion) like tiger balm or bag balm makes a difference." ([r/Nails](https://www.reddit.com/r/Nails/comments/14tic32/please_help_posted_here_before_my_cuticles_still/))
11. "Eucerin standard formula, one of the ONLY lotions I've found that doesn't it feel like I dipped my hands in olive oil." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
12. "actually, paraffin wax is perfectly safe ... it's just all these soy-wax companies and candlemakers that spread misinformation about wax types, because soy sounds "natural" and it is good for their sales" ([r/Candles](https://www.reddit.com/r/Candles/comments/uwgdc3/any_candles_that_are_healthy_or_at_least_non/))

---

## 10. DIY approaches (10 quotes + 1)

1. "I actually make my own with beeswax, shea butter, cocoa butter, jojoba oil, and some infused olive oil. Also sleeping in socks has helped me in the winter ... It's like an overnight deep conditioning mask for your hands." ([r/Nails](https://www.reddit.com/r/Nails/comments/14tic32/please_help_posted_here_before_my_cuticles_still/))
2. "I made some, and I love the way the bars make my skin feel, I have dry skin. I hate the way my hands get oily." ([r/ZeroWaste](https://www.reddit.com/r/ZeroWaste/comments/1bnsakb/experience_with_lotion_bars/))
3. "I just made my own with mango butter, avocado oil, and beeswax" ([r/ZeroWaste](https://www.reddit.com/r/ZeroWaste/comments/1bnsakb/experience_with_lotion_bars/))
4. "4 tbsp organic cocoa butter (52g) 2 tbsp pure refined organic shea butter (27g) 1 and a half tsp safflower oil (19g) 1 tbsp (7g) or 1 ½ tbsp (10g) tapioca starch 35 drops of vanilla fragrance oil" ([r/ZeroWaste](https://www.reddit.com/r/ZeroWaste/comments/q5vf18/diy_vanilla_nongreasy_lotion_bar/))
5. "I'm trying to use as few ingredients as possible while still making a candle that not only looks pretty and smells good, but also helps with dry or cracked skin." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1icjnhj/new_to_making_massage_candles_looking_for_advice/))
6. "I would start from mixing 5% shea butter, 5% coconut oil, 2% essential oils and 88% soy wax." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1icjnhj/new_to_making_massage_candles_looking_for_advice/))
7. "I'm also on a mission to create lotion-candles, or candles that double as a decent hand balm or oil..." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1i5b0ls/new_to_soybased_lotion_candles/))
8. "I render beef tallow and make hand lotion from that. Best I've tried." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))
9. "I made my own beeswax candles. Easy and cheaper than buying them." ([r/nontoxic](https://www.reddit.com/r/nontoxic/comments/1xegiso/unscented_candles_whats_the_consensus_on_whats/))
10. "My advice if you love this it may be cheaper for you to find an online small business retailer to provide you with a safe product." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1volqo9/coconut_massage_candle/))

**Gloves as a DIY "occlusion" hack (very common):** "buy some cotton gloves. before bed, put on a generous layer of vanicream. then cover with aquaphor/vaseline. then put on the gloves and sleep. will you look like mickey mouse at night? yes. will your hands be sufficiently moisturized all winter? also yes." ([r/nursing](https://www.reddit.com/r/nursing/comments/17zilsw/my_hands_are_disgustingly_dry_what_hand/))

---

## 11. Novice vs. expert terminology

**Novice (confusion about the category):**
- "What does the throw mean?" ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
- "Hi question, what is a lighter throw? What does that mean? I'm new to home fragrances" ([r/Candles](https://www.reddit.com/r/Candles/comments/1o3ctuh/my_mom_cant_stand_the_scent_of_burning_candles/))
- "A message candle? Like hidden message in a candle made out of beads?" ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1fnwa54/massage_candle/))
- "Is a candle warmer a heat lamp? Like in the same family as the type for reptiles?" ([r/Candles](https://www.reddit.com/r/Candles/comments/1hzyz1n/do_you_use_a_candle_warmer_or_prefer_lighting/))
- "wtf is a candle warmer?" ([r/BuyItForLife](https://www.reddit.com/r/BuyItForLife/comments/1wnv2fi/bifl_candle_warmer_if_thats_a_thing/))

**Expert (makers and enthusiasts):**
- "they're classified as IFRA category 5A: Body lotion products applied to the body using the hands (palms), primarily leave on. You're essentially making a lotion bar, not a candle." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1ura47i/massage_candles_skincare_candles/))
- "The soft wax and liquids get hot fast and will smell burn-y if overwicked." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1cr73r1/massage_candle_smells_burnt_help/))
- "Wax has memory" and "1 hour per 1 inch across" ([r/Candles](https://www.reddit.com/r/Candles/comments/1qcbqmu/first_time_nice_candle_user_is_this_a_correct/))
- "Coconut wax likes to hang on the sides till the burn is half way down." ([r/Candles](https://www.reddit.com/r/Candles/comments/1qcbqmu/first_time_nice_candle_user_is_this_a_correct/))
- "Keeping burns under 3–4 hours is actually the golden rule for preventing mushrooming wicks" ([r/Candles](https://www.reddit.com/r/Candles/comments/1v6c4hn/been_falling_asleep_really_well_to_this_candle/))
- "Lanolin adds moisture instead of just sealing" ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1vl7gv7/review_do_people_ever_talk_about_okeefes_working/))
- "I find lotions and creams with 10+% urea are most effective for me." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1hljc70/product_question_best_luxury_hand_cream/))

**Plain-language translation that worked:** "Think "candle that fills my entire house" vs. "i have to walk right up to it to smell it"." ([r/Candles](https://www.reddit.com/r/Candles/comments/1o3ctuh/my_mom_cant_stand_the_scent_of_burning_candles/))

**Vocabulary to use in copy:**
- "Hot throw / cold throw" and "tunneling" are mainstream in r/Candles.
- "Candle lamp" and "candle warmer lamp" are what buyers call the device.
- "Massage candle" is understood mainly as sensual or couples. "Lotion candle" is a maker term.
- Hand-care users say "slather", "before bed", "gloves", "greasy", "absorbs", "sting", "cracked knuckles", "cuticles". Nobody said "night-time hand balm" unprompted.

---

## 12. Price and value (14 quotes)

1. "Because when I buy a 60 dollar candle, I prefer not to light my money on fire." ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
2. "I love luxury candles and they're expensive so sometimes I use a candle warmer instead." ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
3. "I think they give life to a candle that you had maybe given up on. ... I'm getting something out of this after I paid for it!!" ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
4. "I love the candles at Barnes & Noble but the prices are obscene.$28 for a small candle? Nope!" ([r/Candles](https://www.reddit.com/r/Candles/comments/1j0mdpo/forget_yankee_where_does_one_buy_good_quality/))
5. "Their prices largely match Yankee's (~$1.50/oz)." ([r/Candles](https://www.reddit.com/r/Candles/comments/1j0mdpo/forget_yankee_where_does_one_buy_good_quality/))
6. "they shouldn't be charging more than 3 times their cost of goods sold. So, if their cost was $10, normally it would retail for $30." ([r/Candles](https://www.reddit.com/r/Candles/comments/151nmxi/when_does_a_candle_become_overpriced/))
7. "I never pay over $12.95 so I don't feel cheated at all." ([r/Candles](https://www.reddit.com/r/Candles/comments/1kgbpo3/bath_and_body_overpriced/))
8. "The three wick candles take me at least 10 burns for them to be all used up. That's hours of burn time for me, so $13 is well worth it in my opinion." ([r/Candles](https://www.reddit.com/r/Candles/comments/1kgbpo3/bath_and_body_overpriced/))
9. "Every gift guide I read pushes the same $80+ 'luxury' bundle, but the self-care gifts that have actually stuck around in my house are all under $40." ([r/GiftIdeas](https://www.reddit.com/r/GiftIdeas/comments/1vn7zkd/selfcare_gift_under_40_that_actually_gets_used/))
10. "Holy I looked up Diptique and why are they so expensive?!?!" ([r/Candles](https://www.reddit.com/r/Candles/comments/1akuxw8/i_fell_victim_to_the_trend/))
11. "Wow expensive….. is it worth it?" / "Absolutely the smell alone is worth the price" ([r/Candles](https://www.reddit.com/r/Candles/comments/yztlwz/just_picked_up_my_first_expensive_candle_thoughts/))
12. "I've only seen beeswax-only candles once in a store, and they were a solid 10x more expensive than the soy ones." ([r/nontoxic](https://www.reddit.com/r/nontoxic/comments/1xegiso/unscented_candles_whats_the_consensus_on_whats/))
13. "Best hand cream you guys use for severely dry working hands? Willing to pay for quality, my hands get so bad this time of year from all the hand sanitizer." (title, [r/nursing](https://www.reddit.com/r/nursing/comments/zle8y3/best_hand_cream_you_guys_use_for_severely_dry/))
14. "I've read that bee wax candles are not toxic at all for the human body, however I find them quite expensive if I were to light one everyday." ([r/Candles](https://www.reddit.com/r/Candles/comments/uwgdc3/any_candles_that_are_healthy_or_at_least_non/))

**Price anchors seen:**

| Item | Prices mentioned |
|---|---|
| Mass-market candles | BBW 3-wick on sale for $10 to $15. Yankee and Kringle about $1.50/oz. |
| "Obscene" | $28 for a small candle |
| Luxury | $60 (Diptyque-class) |
| Candle warmers | $14.99 to $30, and $19 at Costco |
| Hand care | Silk gloves "$20 best in ages". Gloves in a Bottle "expensive, but it's worth it". |

At $32 for 7 oz, Núan sits in the "luxury" band (about $4.57/oz). Buyers justify luxury through longevity, how the jar can be reused, and health. The warmer itself is pitched as the thing that "saves" an expensive candle.

---

## 13. How people describe the ideal solution (10 quotes + 9 supporting)

1. "I'm exploring the idea of creating something that's less about "smelling good" and more about actually helping you wind down at night. Something simple. Not too strong. Not artificial. Just… calming and easy to come back to." ([r/Candles](https://www.reddit.com/r/Candles/comments/1t0esny/do_candles_really_help_you_unwind_or_is_it_just/))
2. "biggest thing is it can't be too strong. if i can still smell it after leaving the room for 5 mins and coming back, it's probably too much." ([r/Candles](https://www.reddit.com/r/Candles/comments/1t0esny/do_candles_really_help_you_unwind_or_is_it_just/))
3. "Ever since I got my candle warmer, I've loved it. It provides a good amount of light, lets the candle warm evenly, and most importantly, has a timer so I don't forget about it and let it burn the house down" ([r/Candles](https://www.reddit.com/r/Candles/comments/1hzyz1n/do_you_use_a_candle_warmer_or_prefer_lighting/))
4. "I just got a candle warming lamp and I love it so much. I fall asleep so easily I and hate the smell of a blown out candle" ([r/Candles](https://www.reddit.com/r/Candles/comments/1hzyz1n/do_you_use_a_candle_warmer_or_prefer_lighting/))
5. "I'm searching for a non-greasy hand lotion or healing ointment that will help repair my cracked skin, and prevent it from cracking again." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1olthz3/product_request_searching_for_a_good_nongreasy/))
6. "I'd like to try using a more intense moisturizer over night (even if I have to wear gloves) to try and help heal my hands." ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1jov48f/product_request_overnight_hand_cream_for_dry_red/))
7. "Not just for massage, but focused on an at-home spa ritual and moisturizing the skin?" ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1ura47i/massage_candles_skincare_candles/))
8. "I really loved that the "make your own" candles were 100% soy and I could balance the strength but still have a candle with nice throw." ([r/Candles](https://www.reddit.com/r/Candles/comments/1qzhbib/recommended_candle_brands_for_sensitivities/))
9. "My wife gets migraines from candles that smell very intensely or sharply, but still is interested in finding a very light scented natural and clean candle brand." ([r/migraine](https://www.reddit.com/r/migraine/comments/1nzp56m/mild_smelling_candle_brands/))
10. "I put my pjs on in advance ... So all I have to do is brush teeth and flop in." ([r/ADHD](https://www.reddit.com/r/ADHD/comments/1ip680q/how_do_you_keep_your_revenge_bedtime/))

**Additional supporting quotes (hands at night, the gifting crossover):**
- "OKeef's Working Hands salve at night on the dresser so it's right behind bed" ([r/nursing](https://www.reddit.com/r/nursing/comments/1sdjc5z/dry_hand_tips/))
- "a good amount of lotion and wearing the gloves for 30 minutes while you're vegging out watching a show 2 or 3x a week will help!" ([r/SkincareAddiction](https://www.reddit.com/r/SkincareAddiction/comments/1d19yjy/misc_im_so_tired_of_itchy_sore_cracking_dry/))
- "I would avoid candles completely but maybe a really good winter lotion like O'Keeffe's Working Hands Night Treatment!" ([r/migraine](https://www.reddit.com/r/migraine/comments/1ox5fdm/candleslotions_that_are_safe_for_migraines/))
- "There is a reason so many people regift candles :) But, if she likes candles, maybe get a candle warmer?" ([r/migraine](https://www.reddit.com/r/migraine/comments/1ox5fdm/candleslotions_that_are_safe_for_migraines/))
- "Years ago, these were quite popular, but I don't see a whole lot offered for sale anymore." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1fnwa54/massage_candle/))
- "You just have to spend some time educating people on how they work since a lot of people assume it is just regular hot wax." ([r/candlemaking](https://www.reddit.com/r/candlemaking/comments/1r3n94e/massage_candle/))
- "If I had a candle lit I wouldn't even be able to run to the bathroom for a literal minute because I'd just envision it catching fire." ([r/Candles](https://www.reddit.com/r/Candles/comments/1awjjp9/whats_the_hype_around_candle_warmers/))
- "The candle lasts longer. I have adhd and have forgotten to blow out my candles. Keeps the soot off my walls." ([r/Candles](https://www.reddit.com/r/Candles/comments/1w25sti/why_use_a_candle_warmer/))
- "My MIL got me one for Christmas because that's what I asked for, but she picked out the ugliest one she could find and now I don't want to use it." ([r/Candles](https://www.reddit.com/r/Candles/comments/1qy8gka/candle_warmer_lamps_are_goated/))

Unique verbatim quotes in this file: about 195 across all sections.

---

## 14. Recurring success and failure patterns (13)

1. **Success: "before bed + occlusion + consistency" heals hands.**
   - The most repeated hand advice across r/nursing, r/SkincareAddiction and r/eczema is to slather a thick product at bedtime, cover it, and repeat nightly. People report results in 1 to 2 weeks.
   - Núan's Seal step maps directly onto this habit. The opening for Núan is to make that habit pleasant, not to invent a new one.

2. **Failure: gloves and socks.**
   - Gloves slide off, get ripped off in sleep, soak up the cream, feel gross, or make you "look like mickey mouse".
   - A balm that people say needs no gloves, or works within "30 minutes while you're vegging out", would remove a friction point people complain about over and over.

3. **Failure: greasy residue versus "absorbs like water".** People complain from both sides. Night use is accepted as the place where greasiness is fine: "My only option is to use it before bed". This supports positioning Núan as night-only, as the brief's "not for fast-absorbing daytime cream" already does.

4. **Failure: solid balms are too hard to use.**
   - "My skin isn't warm enough for them to work... I don't have the stamina." Lotion bars fail because they need warming.
   - A balm that is already melted when you reach for it solves exactly this. It is the strongest functional argument for the candle format that I found.

5. **Success: warmers rescue headaches, soot, tunneling and money.**
   - Candle-lamp converts are enthusiastic: "GOATed", "game changer", "won't go back".
   - Their stated reasons: no flame with kids, cats or ADHD forgetfulness; no soot; even melt and no tunneling; the candle lasts much longer; timers.

6. **Failure: warmers don't fix scent-triggered headaches.** Several users say the scent, not the flame, is the trigger, and one reports headaches only under the warmer. Claims that the lamp "solves headaches" should be careful. Low-scent options and named notes matter more.

7. **Pattern: fear of falling asleep with a flame.**
   - Many stories: waking to soot, a dog turned grey, a boyfriend falling asleep with a candle lit.
   - The "hour after bedtime" use case runs straight into this fear. The lamp's timer (and "No flame") is the answer people already reach for: "Candle warmers have sleep timers." ([r/Candles](https://www.reddit.com/r/Candles/comments/1o9yvqj/this_is_your_reminder_to_not_fall_asleep_while/))

8. **Pattern: massage candles are a maker-side niche with low buyer awareness.**
   - "What's a massage candle??" and "people just need to learn how to use it". Makers say they sell well, with "lots of repeat customers", but "not as fast as my regular candles".
   - Consumers read "massage candle" as sexual.
   - Two skeptical claims recur: that "sex shops stopped selling them", and that the product is "pretty dumb from a skincare perspective".

9. **Pattern: skin-safety skepticism among people who know the category.**
   - Experts flag IFRA 5A limits (about 2% fragrance for leave-on use), the risk of burns from wax that is too hot, and rash risk.
   - Experts are the people who answer novices' questions on Reddit, so naming "every note", stating the fragrance percentage and the melt temperature, and saying "wait 5-10 min" are credibility essentials.

10. **Pattern: paraffin fear versus "it's misinformation".**
    - r/nontoxic and many r/Candles users treat paraffin as toxic, cancer-causing or soot-producing.
    - A vocal minority says paraffin is safe and that the scent is what matters. "No paraffin" works for the anxious segment but is mocked by enthusiasts if overclaimed.

11. **Pattern: scent strength is the deciding variable for sensitive users.**
    - They ask for "milder", "not overtop", "light scented", and "throw meter" style guidance.
    - Triggers are personal: florals, vanilla, citrus and essential oils are each a trigger for someone. Núan's per-scent strength rating matches an existing behavior (PF Candle Co's throw meter).

12. **Pattern: revenge bedtime procrastination responds to rituals that have a fixed end point.**
    - Doomscrolling and bingeing fail because they have "no fixed end point". An enjoyable activity with an ending works.
    - A ritual that ends in a physical step ("blow out, rub in, go to bed") is that end point.

13. **Pattern: candles as gifts are polarizing.**
    - Seen as "low effort", "IDGAF gift", regifted, and piling up for people with migraines. Loved when it's a known favorite or a "fancy jar that can serve as decor".
    - A functional gift (hand balm, a ritual, a lamp) escapes the "generic candle" stigma.

## 15. What triggers strong emotional responses

- **Fire and fear for pets and kids.** The soot-covered dog post drew about 40 comments of alarm and relief. Cats "fighting" flames comes up constantly. Parents frame warmers as a choice made "mostly for safety".
- **Shame about visibly damaged hands.** "anxiety attack in the bathroom", "Patients comment on them", "insecure about my hands my entire life". Healing is described as relief and dignity ("glow up", "Thanks for giving me hope").
- **Feeling unheard by people who give scented gifts.** In r/migraine this shows up as anger and dark humor: tossing a mother's candle "into a culvert", "Why should I be grateful for bad gifts I didn't ask for?".
- **Discovering wasted money.** "OH MY GOD You're supposed to dump the layer of wax", "I prefer not to light my money on fire". People get indignant about $28 to $60 candles that tunnel or lose scent.
- **Stolen time.** "precious", "I'm not going to waste it on cleaning", fantasies of a cabin alone. The hour after bedtime is emotionally loaded: it is a reward and also a source of guilt (doomscrolling at 2-5am).
- **Overstated "toxic" or "natural" claims.** Debates get heated ("B R U H", "Do some research lol"). Unsupported claims draw ridicule from enthusiasts.
- **Holy-grail evangelism.** "Working hands! Working hands! Working hands!" Once something works, users recommend it with near-religious loyalty. This is word-of-mouth fuel.

## 16. Implications for Núan (brief)

- Lead with function: a balm that is already warm when you reach for it, so you don't need gloves or the stamina to warm a bar. Treat "massage candle" as a secondary term, because buyers associate it with sex shops and safety risk.
- Answer the expert objections up front: skin-safe fragrance percentage, melt temperature, the wait time, and patch-test guidance.
- Position the Lumera lamp's timer for people who fall asleep and "no flame" for homes with kids and cats. Be careful about headache claims, since scent can still trigger them.
- The $32 price needs value framing in Reddit's own terms: burn hours and number of uses, the "save your expensive candle" lamp logic, and a reusable jar. The 6,800-review claim on a brand-new store would be caught quickly by Reddit-savvy buyers.
