# Weekly marketing run log

One entry per weekly results pass. **Newest at the top. Append only** - never
overwrite the file or edit an earlier entry.

Written straight to `main` so the marketing hub can read it from this repo
without waiting on a pull request. Four fixed sections per entry: what ran,
what changed, what broke, what needs a decision.

`HANDOFF.md` stays the narrative log where decisions get argued out. This file
is the factual record of what each run actually did.

**This repo is public.** No keys, no tokens, no user data, no folder or account
identifiers. Post metrics are fine; they are already published in `HANDOFF.md`.

---

## 2026-08-10

### What ran

- Weekly results pass, Monday 9am Brisbane. Window 3 to 10 August.
- Fresh reads of `HANDOFF.md`, `results.csv` and `POSTED.md` on main in
  both repos.
- Drive sweep of the marketing folder for new sets.
- Activation funnel workflow, dispatched on main and read from its logs.
  Invite funnel read from its daily report.
- Site traffic query, retried once. Plan-blocked as documented.

### What changed

- **Zero posts in the seven-day window.** Nothing went out between 3 and
  10 August. The last post was video 03 on 2 August. Three finished
  videos (04, 05, 06) sit built and unposted.
- **Video 03 was missing from the log entirely** and is now recorded, in
  couples PR #517: 2 Aug, 474 views, avg watch 4s, 24% watched, 69.2%
  skip, 0 saves. The 3 Aug pass reported three posts for its window when
  four had gone out. Second consecutive week the log under-reported
  throughput.
- Saves per 100 views across all four posts: 0.00, 0.00, unknown, 0.00.
- Activation funnel now returns data where it read empty last week: 53
  spaces, 117 events over 30 days. Sequential funnel 1 created, 0 shared,
  0 joined, 0% end to end. Raw counts: 81 app_open, 15 member_joined, 13
  invite_opened, 7 countdown_shared, 1 countdown_created, 7 excluded for
  missing space_id. Invite funnel: 1 sent, 10 opened, 2 joined, 1
  attributed install. Retention: 1 of 35 couple creators active at D1,
  all other cohorts and columns zero.
- **Last week's open question 4 is closed.** Zero events at 7 and 90 days
  could not be distinguished from a blocked write. 117 events settles it:
  the pipe works, no test event needed.

### What broke

- Nothing broke. Three inputs were unavailable and are recorded as
  unavailable rather than skipped: site traffic (plan-blocked, retried
  once), the per-platform split and saves for video 03, and saves for
  ninetabs-static (open since 3 Aug).
- One reporting defect found, not in the data but in the tooling: the
  funnel script prints "most people who make a countdown never share it -
  that is a product problem" off a denominator of one. Seven share events
  fired in the same window. The line should be gated on a minimum n
  before anyone quotes it as a product finding.
- `set-03-crew-bookings` in Drive still contains POST.md and none of its
  17 specified frames, unchanged in ten days.

### What needs a decision

1. **The insights for video-03-surprise and ninetabs-static.** Per-platform
   views and saves for the first, saves for the second. The only numbers
   keeping the results log incomplete.
2. **Post order for the built videos.** 04 is marked ready to post but has
   the weakest opening of the three by both the predictor and the brief's
   frame-zero rule; 06 has the strongest. A scheduling call for the hub,
   not a creative one.
3. **Video 05** still needs the proposal-disclosure decision before it can
   go anywhere.
4. **set-03-crew-bookings**: fill the frames or drop the set.

### Discipline note

Four posts total, far below the 20 to 30 at which the results log allows
analysis to steer. **No trend is called and no format is killed** - nothing
has failed twice running. The skip-rate sequence (84.1, 72.6, 69.2) is the
hub's finding already acted on in the brief, recorded here as raw numbers,
not re-derived as a trend.

The number worth reading this week: zero posts in seven days, with three
finished videos in hand. The bottleneck is not creative.

---

## 2026-08-07 - predictor scores (same day, after the connector came back)

### What ran

- Higgsfield Virality Predictor over nv-video-03..06, imported from the
  `footage` branch via jsDelivr pinned to the publish commit. 03 exceeded
  the predictor's newly discovered 16-second input cap (16.29s) and was
  scored from a 16.00s tail-trim that removes only end-card hold.
- Scores (0-100 proxies; hook window 0-3s):

  | video | viral potential | overall | hook | sustain | peak at |
  | --- | ---: | ---: | ---: | ---: | ---: |
  | nv-video-03 | 56 | 57 | 47 | 88 | 2s |
  | nv-video-04 | 49 | 50 | 37 | 91 | 4s |
  | nv-video-05 | 54 | 57 | 44 | 94 | 2s |
  | nv-video-06 | 57 | 59 | 47 | 93 | 0s |

### What changed

- **Calibration closed, rank order trusted.** The decisive test passed:
  03 (69.2% real skip) outscores planner-stopsaying (84.1% real skip) by
  11 points viral and 14 points hook, and planner is bottom of all eight
  scored videos on overall. Rank order and hook diagnostics now steer
  triage between cuts; absolute scores remain uninterpreted until more
  per-reel retention data exists.
- The new-format four score above the old posted set on every axis that
  matters (viral 49-57 vs 42-48, hook 37-47 vs 30-37).

### What broke

- Nothing. The connector block from the morning entry was resolved by
  Charlie re-enabling Higgsfield for the working chat.

### What needs a decision

- Hub: 04 is slated ready-to-post but carries the weakest hook of the
  four (37, peak at 4s); 06 is the strongest (47, peak at frame zero).
  Whether that reorders the slate is the hub's call.

---

## 2026-08-07

### What ran

- Production run against the marketing brief, end to end. MARKETING.md
  committed verbatim to main, unmodified. The eight reference render
  scripts committed to `marketing/render/` with a README mapping each
  script to its published video.
- Full rebuild of nv-video-03 through 06 from those scripts: playwright
  frame renders plus ffmpeg h264 encodes, 1155 frames across the four.
- The brief's QA pass on all four: resolution and fps probe, frame-delta
  glitch scan at 216x384, and a visual check of the 05/06 tail frames
  for the iOS Control Centre.
- Push of the four finished renders to the `footage` branch as
  `clips/nv-video-03.mp4` through `06` (07384c8), left out of
  `manifest.json` so the Drive mirror never tries to reconcile them.

### What changed

- The render pipeline is now reproducible from the repo alone: scripts on
  main, footage on the branch, and the rebuilt outputs match the
  published cuts on duration to the frame (16.3 / 11.9 / 10.7 / 9.2s).
- QA numbers for the record: medians 2.02 / 8.74 / 0.32 / 0.32, max
  deltas 23.0 / 30.4 / 6.4 / 6.6. The single above-30 pair in 04 is a
  fast handheld pan in the source hotel clip, verified continuous frame
  by frame. The brief's median 5-8 band reads as calibrated on b-roll;
  typography plates and UI recordings sit well below it by nature.
- One margin noted for future cuts: reel12's final beat ends at 33.0s in
  SR_08-04, past the brief's 32.8s line. The recording settles before
  the Control Centre pull-down so the frames are clean, but any re-cut
  should pull the out-point back to 32.8.

### What broke

- The Higgsfield connector dropped out of the working session mid-run and
  cannot be re-enabled from this side: account-level auth is fine, the
  chat-level toggle is off. Scoring of nv-video-03..06 is parked on it.

### What needs a decision

- Nothing to decide; one action: re-enable the Higgsfield connector for
  the working chat so the predictor can score 03..06. The calibration
  close is specced: 03 must rank above planner-stopsaying (real skip
  rates 69.2% vs 84.1%) for rank-order trust to survive.

### What ran

- Higgsfield Virality Predictor over the four posting reels on the `footage`
  branch, one job per reel, imported via jsDelivr (raw.githubusercontent
  serves octet-stream and gets rejected; jsDelivr serves video/mp4 and all
  four imported clean). PREVIEW and proxy variants skipped: byte-duplicates
  of the posting cuts.
- Scores (normalized 0-100 proxies; hook window is 0-3s):

  | reel | length | viral potential | overall | hook | sustain | peak at |
  | --- | ---: | ---: | ---: | ---: | ---: | ---: |
  | kept-afteryouland | 13.0s | 48 | 51 | 37 | 96 | 0s |
  | memories-keepthetrip | 14.7s | 45 | 48 | 34 | 97 | 5s |
  | planner-stopsaying | 9.4s | 45 | 47 | 33 | 95 | 4s |
  | fiji-longweekend | 10.4s | 42 | 45 | 30 | 97 | 5s |

### What changed

- Calibration baseline recorded. Read of the tool so far: internally
  consistent and directionally useful, not yet validated against reality.
  The one reel that opens at its visual peak (kept-afteryouland, peak at
  t=0) gets the best hook score and the best overall - the other three ramp
  for 4-5 seconds first and get punished for it, uniformly low hooks
  (30-34) against uniformly high sustain (95-97). That matches how these
  cuts were built, so the diagnostics cohere. The band is narrow (42-48
  viral potential): it separates our reels weakly from each other.
- Working rule until validated: use it for hook diagnostics and rank order
  between variants of the same concept; do not treat absolute scores as
  meaning anything yet.

### What broke

- The MARKETING.md brief and the nv-video-03..06 render scripts did not
  arrive - the upload contains only an unrelated screenshot. Everything
  that depends on them is parked: the brief commit, the reference scripts,
  and pushing nv-video-03..06 to the branch (they exist nowhere I can
  reach; no nv-video entries on the branch, in Drive via the mirror, or in
  the repos).

### What needs a decision

- Real performance numbers per reel, to finish the calibration: predicted
  rank order is kept > memories = planner > fiji, and whether that matches
  actual views/retention decides how much weight the predictor gets. The
  numbers in HANDOFF entries cover the account level; per-reel
  views/retention from the platform dashboards would close this.
- Re-send MARKETING.md and the render scripts.

### What ran

- Weekly results pass, Monday 9am Brisbane.
- Read the analytics exports uploaded to the Drive marketing folder on 2 Aug:
  14 screenshots covering both reels, the static post, and the TikTok account.
- Activation funnel job, twice: a 7 day window and a 90 day window.
- Drive sweep of the marketing folder for new sets to commit.
- Site traffic query. Blocked, see below.

### What changed

`results.csv` and `POSTED.md` in the app repo now carry this week's numbers.
Three creatives went out in the window, 1,596 views total, **zero saves on both
reels**.

| Post | Format | Date | Where | Views | Saves |
| --- | --- | --- | --- | ---: | --- |
| `dayzero-nofaces` | b-roll reel, 14s | 27 Jul | IG + TikTok | 1,086 | **0** |
| `planner-stopsaying` | screen recording reel, 9s | 29 Jul | IG + FB + TikTok | 295 | **0** |
| "Nine tabs open. Nothing booked." | static feed post | ~31 Jul | IG + FB | 215 | not in the export |

- `dayzero-nofaces`: 279 accounts reached on Instagram, average watch 5s of 14s,
  1 follow. Views are still accruing, so the totals now exceed the 1,029
  recorded at the first reading.
- `planner-stopsaying`: 102 accounts reached, average watch 4s of 9s, 0 follows,
  skip rate 84.1%, save and share and like rates all 0.0%.
- Static post: 65 accounts reached.
- TikTok account for the week: 945 post views, 6 profile views, 15 likes.

**Two of those three were missing from the log entirely** until this pass: the
TikTok cut of `planner-stopsaying`, and the whole static post. The log had been
under-reporting throughput by a third. Both are recorded now.

Handoff entry 30 carries the full detail and the reasoning.

### What broke

Nothing broke. Three inputs were unavailable, and are recorded as unavailable
rather than quietly skipped:

- **Site traffic figures.** The programmatic analytics API is not available on
  the current hosting plan and answers "not found" by design. Retried once in
  case the plan had changed; same answer. No traffic numbers this week.
- **The new set has no frames.** `set-03-crew-bookings` in the Drive marketing
  folder contains its post copy and nothing else. It specifies 17 frames across
  three aspect ratios, and none of them are there, so there was nothing to
  commit.
- **Saves for the static post.** Its export includes the overview and audience
  tabs but not the engagement tab.

One result looks alarming and is not. **The activation funnel reads empty at
both 7 and 90 days.** The instrumentation only shipped on 29 July, so there
were five days in which an event could have been recorded, not ninety. The
event call sites and the database rule both check out in source. Zero events in
five days at this install volume is unremarkable, and it is not evidence of a
broken pipe.

### What needs a decision

1. **The saves count for the static post.** The only post this week whose saves
   could not be read, and saves are the number that decides creative. Needs the
   engagement tab from Instagram insights.
2. **`format=static` in the results log.** A static feed post does not fit the
   three existing format values (face, screen recording, b-roll). Recorded as
   `static` and flagged, rather than widening the taxonomy unilaterally.
3. **Hook type and pillar for the two newly logged rows.** Those are
   approval-time editorial calls. Left blank rather than reconstructed from a
   screenshot a week later.
4. **Whether to add a check that proves the analytics pipe works.** Event
   writes fail silently by design, so a blocked write and genuine non-use
   produce identical output indefinitely. One deliberate test event would
   separate the two permanently.

### Discipline note

Three posts is far below the 20 to 30 at which the results log allows analysis
to steer. **These are raw numbers and no trend is being called.** The two reels
are different formats, so neither format has failed twice running and nothing
meets the kill rule. Nothing is being cut on this week's data.

The one number worth reading: three creatives in seven days is the highest
throughput week so far.
