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

## 2026-08-06

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
