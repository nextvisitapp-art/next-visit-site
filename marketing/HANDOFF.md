# Marketing handoff log

The running record of marketing decisions: what was decided, what shipped, what
the numbers said, and what is open.

## Who does what (current, 1 Aug 2026)

- **Cowork** - strategy and the thinking behind it, concepts, hooks, the
  calendar, and the still sets. Charlie works there directly.
- **Claude Code** - video (Remotion templates in `marketing/reel/`, footage cuts
  via the `video-editing` skill), plus infrastructure: screenshot capture,
  committing assets, `results.csv`, analytics, and the weekly results pass.
- **Claude Design** - no longer in the loop as of 1 Aug 2026. Entries 1 to 24
  are largely addressed to Design; **read them as history, not as live
  instructions or open questions.** Nothing in this log is waiting on Design.

## How to use it

1. **Read this file at the start of every marketing session.** Top entry first.
2. **Reply by appending a new dated entry at the top** - newest above oldest.
   Never edit someone else's entry; add yours.
3. Head each entry `## YYYY-MM-DD - <who>` and say what you decided, what you
   shipped, and what you need from anyone else.
4. Only once we know what to produce does Charlie get pulled in - and then with
   a specific ask: review this cut, film these three shots, confirm this
   setting. Not an open question.
5. House rule: **no em dashes anywhere in this project.** Hyphens only.
6. **Old entries live in `HANDOFF-ARCHIVE.md`** - moved there verbatim when
   this file gets heavy, never edited. History is there; this file is the
   working set.

---

## 2026-09-07 - Claude Code (43)

**Positioning update landed in the pipeline.** Decided 6 Sep: the one-line
positioning is now "For the people you have to fly to see." The product stays
focused on long-distance couples; the marketing frame widens to long-distance
friends and family. Two changes shipped, both in the couples repo, nothing else
touched (App Store title, subtitle, keywords, onboarding flow, relationship-mode
logic and every core feature are as they were).

**1. Crew is now Mates in the app.** Every user-facing string - onboarding fork,
the member card and Home strip, Your Spaces, Plus pitches, digest pushes, join
errors - reworded toward the relationship ("the mates you have to fly to see")
rather than the party size ("the whole crew"). Existing Crew spaces carry over
as Mates with no migration; stored fields and analytics identifiers are
unchanged, so the funnel report and dashboard keep working. **Still says Crew and
is NOT mine to change without a decision:** the landing page (`index.html` nav
item "Crews", the `#crews` section, meta description), `premium.html`,
`support.html`, the legal pages, and the go planner's save-to-app card ("Plan it
with the crew"). Cowork owns the copy; say the word and I will do the sweep in
one pass, or leave it until the site is next rewritten for the new positioning.

**2. Content lane in the posted log.** `marketing/reels/POSTED.md` and
`results.csv` now carry a `lane` column, `couples` or `friends`. All four
existing posts are backfilled `couples`. The reel-factory "posted" action takes
the lane as a workflow input (default couples) and refuses any other value.
Rules recorded in `RESULTS.md`: friends-lane posts use the existing six-second
Series 01 format only, no new formats; the weekly pass reports each lane
separately (views, watch-through, saves, reach) so they compare like for like
when paid ads start. Note the log lives at `marketing/reels/POSTED.md` in the
couples repo - the brief called it `claude_posted-log.md`, which does not exist
in any repo or in Drive; if that is a Cowork-side file it needs the same column.

**Nothing needed from Charlie** unless he wants the site sweep above.

## 2026-08-10 - Claude Code (42)

**Nothing posted between 3 and 10 August. Zero posts in seven days, against
three finished videos sitting on the branch ready to go.** The last thing
that went out was video 03 on 2 August. Throughput is the metric that
matters most at this stage, and this week it was nil - that is the finding,
and it is not a creative problem.

**A fourth post existed and was never logged.** Video 03 went out 2 August
and never reached `results.csv` or `POSTED.md`, so the 3 Aug pass reported
three posts when four had gone out. Both are corrected now (couples PR
#517) from the hub's own MARKETING.md table: 474 views, avg watch 4s, 24%
watched, skip rate 69.2%, 0 saves. That is the second week running that the
log under-reported throughput, and the second week the missing rows had to
be reconstructed from someone else's document.

**Saves per 100 views, every post to date:**

| Post | Date | Views | Saves / 100 views |
| --- | --- | ---: | --- |
| dayzero-nofaces | 27 Jul | 1,086 | 0.00 |
| planner-stopsaying | 29 Jul | 295 | 0.00 |
| ninetabs-static | 31 Jul | 215 | _saves still not in the export_ |
| video-03-surprise | 2 Aug | 474 | 0.00 |

**Funnel, run today.** Activation, 30 days: 53 spaces, 117 events. Created a
countdown 1, then shared it 0, someone joined 0, end to end 0%. Raw events:
81 app_open, 15 member_joined, 13 invite_opened, 7 countdown_shared, 1
countdown_created, 7 excluded for having no space_id. Invite funnel: 1 sent,
10 opened, 2 joins, 1 attributed install. Retention: 1 of 35 couple creators
active on D1, everything else zero.

- **The script's own conclusion is wrong and should be softened.** It prints
  "most people who make a countdown never share it - that is a product
  problem", off `countdown_created = 1`. One space is not "most people", and
  7 share events actually fired in the window from spaces whose creation
  predates instrumentation. The sequential funnel is n=1; the raw counts say
  people are sharing. Worth gating that line on a minimum n before it gets
  quoted as a product finding.
- **Last week's open question about the analytics pipe is answered.** 117
  events across 53 spaces. The pipe works. A deliberate test event is no
  longer needed.

**Traffic: still unavailable.** The programmatic Web Analytics API is
plan-blocked and answers not_found by design; retried once, same answer. No
site numbers again this week.

**Missing inputs, stated rather than skipped:** site traffic (above); the
per-platform split and saves for video 03; saves for ninetabs-static, open
since 3 Aug; and `set-03-crew-bookings` in Drive, which still holds POST.md
and none of its 17 frames, unchanged in ten days. Stills are Charlie's in
Cowork now, so that set is his to fill or drop - nothing is waiting on
anyone else.

**What the numbers suggest trying next.** Four posts is far below the 20 to
30 where analysis is allowed to steer. **No trend is being called and no
format is being killed** - nothing has failed twice running. One scheduling
suggestion, which is not a creative judgement: videos 04, 05 and 06 are all
built and unposted. The predictor calibrated on Friday and the brief's own
frame-zero rule agree that **06 has the strongest opening** (hook 47, peak
at frame zero) and **04 the weakest** (hook 37, peak at 4s), yet 04 is the
one marked ready to post. Posting 06 first costs nothing and tests the
frame-zero rule on the metric the brief cares about. 05 still needs the
proposal-disclosure decision.

**The one ask.** Open Instagram and TikTok insights for **video-03-surprise
(2 Aug)** and paste the per-platform views and saves, plus the saves figure
for **ninetabs-static (31 Jul)**. Those are the only numbers keeping the
results log incomplete.

**Audit of the Higgsfield MCP connector - what a session can and cannot
drive.** Charlie asked what Claude Code can actually do with the new
Higgsfield subscription before deciding what to learn himself. Verified
against the live connector, read-only, no credits spent. Written in a
parallel session to entries 39 and 40, so it overlaps them in places and
corrects one thing they imply (see the jsDelivr note below).

- **Account is on Ultra with a healthy credit balance.** The full model
  catalogue is open: Veo 3.1, Kling 3.0 (multi-shot, motion transfer, 4K),
  Seedance 2.0 (the reel's model - reference-driven identity, native audio
  including spoken lines, up to 4K and 15s), FLUX 3 Video (up to 20s, video
  continuation for chained shots), Minimax, Wan 2.7, Higgsfield Cinema
  Studio 3.0. Images: Soul 2, Nano Banana Pro, plus trainable reusable
  characters from 5-20 photos. Audio: TTS with voice cloning. Post tools:
  4K upscale, reframe, outpaint, background removal, lipsync, deflicker.
  Up to 12 generations can run in parallel per call, and `get_cost`
  preflights the credit cost of any of them without submitting a job.
- **Bundled multi-step workflows** load like skills: faceless narrated
  videos 30s to 10+ min (script, voiceover and captions included), five
  UGC ad flows, thumbnail production, brand kits. Full pipelines, not
  single prompts.
- **Assembly runs in Higgsfield's own cloud sandbox** (ffmpeg, Whisper,
  ImageMagick preinstalled, open internet). Verified: it downloads
  generated clips, can cut/concat/overlay, and uploads finished pieces
  back to Higgsfield storage. Generate, assemble, publish - end to end
  with no one's laptop involved.
- **TikTok publishing is built in**: direct post or to-drafts, commercial
  music library, quota-aware. No account is connected yet; it needs
  authorising once.
- **Two real gaps.** (1) No music generation and no licensed-music search
  in the connector; music stays platform-native at post time or from our
  own library. (2) The Claude Code container's network policy blocked
  Higgsfield's media CDN, which is the real cause of entry 38's "I cannot
  view the pixels from this container". **Charlie fixed this on 7 Aug** by
  setting the environment's network access to Custom and allowing
  `d8j0ntlcm91z4.cloudfront.net` and `d2ol7oe51mr4n9.cloudfront.net` (with
  the default package-manager list kept). It applies to sessions started
  after the change, so a session that still cannot fetch a frame should
  check it is not an older one rather than assume the block is back.
- Also connected, untested in anger: artlist AI (gen plus voiceover, not
  the licensed music catalogue), InVideo (script-to-video), Canva.

**Getting our real footage into Higgsfield needs nobody's hands.** Proven
end to end, not theorised - clip `trip-trip-13.mp4` (47 MB, 1080x1920,
20.6s) is a confirmed video asset in Higgsfield storage, pulled straight
off the `footage` branch.

- `media_import_url` on a `raw.githubusercontent.com` link is REJECTED:
  GitHub serves `.mp4` as `application/octet-stream` and the importer
  refuses that content-type. Not a permissions problem, so do not go
  hunting for one.
- **jsDelivr works, but only under its file-size cap.** Entry 40 imported
  nv-video-03..06 that way and it was the right call - they are short
  renders. The same URL shape 403s on `trip-trip-13.mp4` at 47 MB, which
  is a size limit, not a broken mirror. Reach for jsDelivr first on a
  finished reel; expect it to fail on raw source footage.
- **The path that works at any size:** `media_upload` for a presigned URL,
  then the Higgsfield sandbox does `curl` from raw.githubusercontent and a
  `PUT` to the presigned URL in the SAME command (the sandbox is discarded
  seconds after a call returns), then `media_confirm`. Neither the 50 MB
  import cap nor the content-type check applies on that path.
- For a clip in Drive but not yet mirrored: `footage-sync.yml` in the
  couples repo has `workflow_dispatch`, and its own comments say the
  manual path is not throttled the way the schedule is. Dispatch it, wait
  the few minutes a one-clip run takes, then pull from the branch. So the
  whole chain Drive to branch to Higgsfield runs from a session.

Once a clip is in there it is a first-class input, not just storage:
`video_references` on Seedance 2.0, MiniMax H3, Wan 2.6 and Gemini Omni
(generate new footage that matches ours), Kling 3.0 motion control (drive
a character with the motion from a real clip), reframe to any aspect, 4K
upscale, background removal, scene-by-scene analysis, and the virality
predictor.

Net: proper 15-60s brand films are producible end to end from a session -
multi-shot, consistent characters, spoken lines, 4K finish, posted to
TikTok. Charlie's irreplaceable inputs are taste and approval, and real
footage. Learning the Higgsfield web UI is optional; everything the MCP
exposes can be driven from here.

---

## 2026-08-07 - Claude Code (40)

**Scores are in and the predictor passed its test. Rank order is now
trusted for triage.** Charlie re-enabled the Higgsfield connector minutes
after entry 39; all four videos imported via jsDelivr and scored.

| video | viral | overall | hook | sustain | peak at |
| --- | ---: | ---: | ---: | ---: | ---: |
| nv-video-03 | 56 | 57 | 47 | 88 | 2s |
| nv-video-04 | 49 | 50 | 37 | 91 | 4s |
| nv-video-05 | 54 | 57 | 44 | 94 | 2s |
| nv-video-06 | 57 | 59 | 47 | 93 | 0s |

- **The calibration test from the brief:** video 03 (69.2% real skip, our
  best) had to rank above planner-stopsaying (84.1% real skip, our known
  failure, scored 45/47/33 yesterday) or the tool was dead. It ranked 03
  eleven points higher on viral potential, fourteen on hook, and planner
  sits bottom of all eight scored videos on overall. Direction correct on
  the one pair with real comparative data. **Working rule upgraded: rank
  order and hook diagnostics are now trusted for triage between cuts.
  Absolute numbers still mean nothing until more per-reel retention data
  arrives.**
- The new-format four (03..06) score above the old posted set (49-57
  viral vs 42-48; hooks 37-47 vs 30-37) - the format change the brief
  codified reads as real in the predictor too, not just in the skip
  rates.
- Diagnostic worth having before the next post goes out: 04 - the one the
  slate marks ready to post - has the weakest hook of the four (37, peak
  not until 4s; the hotel pan ramps before the payoff). 06 is the
  strongest scorer and peaks at frame zero, exactly the brief's
  frame-zero-hook rule. Not my call to reorder the slate; flagging for
  the hub.
- Two predictor facts learned: it hard-rejects anything over 16s (03 at
  16.29s bounced; scored from a 16.00s tail-trim that only shaves end-card
  hold, hook window untouched), and it runs free on the current plan.
  Future cuts are 10-12s per the brief, so the cap only ever bites
  legacy-length videos.

**The brief is in, the render pipeline is proven, nv-video-03..06 are on the
branch.** The production run the hub commissioned is done end to end:

- `marketing/MARKETING.md` committed verbatim to main (c82df77). Read in
  full before producing. It governs from here; the hub owns it, I do not
  edit it.
- The eight reference scripts are at `marketing/render/` with a README
  mapping scripts to published videos (reel5 = 03, reel10 = 04,
  reel11 = 05, reel12 = 06).
- All four videos rebuilt from those scripts in a fresh environment and
  QA'd to the brief's spec: 1080x1920 at 24fps, durations 16.3 / 11.9 /
  10.7 / 9.2s matching the published lengths exactly. Frame-delta scan
  clean on all four (the one 30.4 spike in 04 is a fast handheld pan in
  the source hotel clip, checked frame by frame - continuous, not a
  glitch). Tail frames of 05 and 06 verified free of the iOS Control
  Centre; reel12's last beat ends at 33.0s in SR_08-04, 0.2s past the
  brief's 32.8s line, but the recording settles before the pull-down so
  nothing leaks into frame. Worth trimming to 32.8 if that beat is ever
  re-cut.
- Pushed to the `footage` branch as `clips/nv-video-03.mp4` through `06`
  (07384c8). Deliberately not in `manifest.json`: that file records the
  Drive mirror's state, and listing files the mirror cannot see in Drive
  would get them removed on its next run. Finished renders ride the
  branch outside the manifest; the mirror leaves non-manifest paths
  alone.

**Blocked: the predictor scoring of 03..06.** The Higgsfield connector is
authenticated at the account level but toggled off for the working chat, so
the tools are not loadable from my side. Charlie: enable Higgsfield in the
chat's connector settings and say go. The decisive calibration test is
specced and waiting: video 03 (69.2% skip in the wild) must rank above
planner-stopsaying (84.1% skip, scored 45/47/33 yesterday) or the
predictor's rank-order trust is dead per the brief's own rule.

**First Higgsfield-produced reel, ready for Charlie's review.** In the
Higgsfield account: a 10s vertical cut, working name nv-reel-countdown-
stopsaying. Built on the proven line - the opening frame carries
Stop saying "we should go somewhere." as painted text over a couple from
behind at a golden-hour headland, subtle live-photo motion, light deepening
toward dusk. No AI faces (couple from behind, matching our real-footage
look), no AI-drawn logo (the marks are locked).

**It is the first cut made under the calibrated predictor, and it ranks
first of the five scored:** viral potential 59 against the 42-48 band of
the four existing reels, hook 41 against 30-37, sustain 100. The hook
lesson from calibration - open at the peak - was applied literally, and the
model rewarded exactly that. Engagement also RISES to its peak at the final
second, which is the right shape for loop plays. Per the working rule,
trust the rank, not the absolute numbers.

**Before posting, Charlie must check** (I cannot view the pixels from this
container): the headline text is spelled exactly right and stays crisp
through the motion, and the scene reads as us. If it passes: it is 720p -
say the word and it gets a 2K upscale first. It is silent by design - add
platform-native music at post time.

Brief status: MARKETING.md and the render scripts still have not arrived;
this cut deliberately stays on hub-approved copy and the countdown concept
rather than inventing new strategy.

---

## 2026-08-04 - Claude Code (37)

**Onboarding no longer strands anyone, and the whole web funnel is green.**
Three fixes from Charlie's own testing this morning, all live and all
covered by the production suite (run 30902816353, four jobs green):

- **Email sign-in is on the fork.** It only existed behind "Us two", so a
  crew user with a linked email had no discoverable way back into their
  spaces on a new phone. "Been here before? Sign in with email" now sits on
  the fork itself and opens the email step directly - and sign-in restores
  every space on the account, crew and couple alike.
- **The couple chooser has a Back.** Tapping "Us two" by mistake was a dead
  end; it now returns to the fork.
- **The go handoff card's App Store line** was a browser-default blue link
  on the pink card. Styled to match the footnote it lives in.

**Proven end to end on production, permanently:** plan a trip on go with no
account, tap Save, onboard - the trip saves itself into the brand-new space
and the just-saved banner greets you. The URL parks under onboarding and
completes after; nobody has to "come back".

One note for copy: the notification prompt Charlie saw on web is real, not
an app leak - web push genuinely delivers to desktop and Android browsers,
and iOS Safari never sees the prompt because there it truly is unsupported.

---

## 2026-08-04 - Claude Code (36)

**Web-first is now real on every surface, not just parked capability.**
Charlie is about to share Next Visit with a mixed-platform group (family
chat, mostly Android), which made the gap concrete: the hello page's primary
element was the App Store badge, and an Android visitor was implicitly told
this is not for them.

**What changed, all live:**

- **hello.next-visit.app** now leads with a pink "Open Next Visit" button to
  the web app in the hero, the nav on all five pages, and the closing card.
  The App Store is the iPhone extra ("get the app for widgets and
  notifications"), the store badges sit second, and the greyed Google Play
  "coming soon" badge finally reads coherently, because the button above it
  is the Android answer today. Steps copy no longer says an invitee "gets
  the app".
- **The one funnel break in the web-first story is fixed.** Plan a trip on
  go, tap Save to Next Visit with no account - the exact person a shared
  link brings in - and the payload used to be dropped with "come back to
  save this trip". It now survives onboarding: stashed on arrival, replayed
  automatically the moment the space exists, trip on Home with the
  just-saved banner. A new production check walks that whole funnel beside
  the reclaim and nudge ones, and reads the visit doc back as admin.
- **The iOS app-nudge toast looks like ours now.** Its Download action was
  sonner's stock near-black chip inside an otherwise on-brand toast.
  Rendered it in both themes before and after (there is a committed
  preview-toast.html harness now); the action is the brand's pink primary,
  and error toasts keep crimson actions by construction.
- **One layout bug found by looking:** the hero parallax walked the phone
  art into the new note text on mobile. It ate its clearance on any stacked
  viewport at any scroll depth, old copy included. Parallax is now desktop
  only, where the columns cannot collide.

**For copy and creative:** "works in your browser, nothing to install, any
phone" is now true AND said out loud on the landing page. Share
hello.next-visit.app when the audience is mixed-platform; next-visit.app
goes straight into onboarding when the pitch has already happened.

**Open:** whether the greyed "Google Play - coming soon" badge should stay
on the closing card at all now the browser is the Android answer - keeping
it promises a native app we may never ship. Cowork's call, it is one line
to remove.

---

## 2026-08-04 - Claude Code (35)

**New clip on the branch: a 34s walkthrough of The little things.** Charlie
recorded it on device and dropped it in the Drive folder; it is clip 84.

```
clips/ScreenRecording_08-04-2026 09-46-44_1.mp4    5.64 MB, 886x1920, 34.07s
index/ScreenRecording_08-04-2026 09-46-44_1.jpg    contact sheet
```

**Reviewed: cleared, usable.** No faces, and no real data either - it is the
Tom and Mim demo space, so every name and answer on screen is seeded. That is
worth stating plainly because a screen recording is the one kind of footage
that can carry a real name, email or join code onto a public branch, and this
one does not.

**One shot in it is already out of date.** At about 8.5s, on Tom's tab, the
Treat field reads "Convenience-sto...andwiches" - it is clipped mid-word. That
was a real bug: the short fields were plain inputs and an input cannot wrap, so
any answer past roughly forty characters was unreadable. It is fixed and live
as of tonight, every field wraps now. The recording was made before the fix.

So: the Mim half of the clip is accurate and always was, because the partner
view already wrapped. The Tom half shows a bug that no longer exists. Cut
around it, or ask Charlie for a fresh take - it is a 34 second shot.

**What the feature is, for anyone writing to it.** Each partner privately notes
what they love - ring size and style, sizes, favourites, love language, a
"maybe don't" list - and the other can read it any time with **no notification
and no viewed indicator**. That silence is the whole feature: asking someone
their ring size is what spoils the proposal. The demo space now has all
seventeen fields filled on Mim's side and twelve on Tom's, so the screen
demonstrates itself rather than showing an empty state.

**Unrelated, and it affects the still sets rather than this clip:** the app
screenshot capture is currently failing. Several frames come back byte
identical because pages are photographed before they finish drawing, and the
run is all or nothing, so `screens/` has not been rebuilt since 3 Aug 08:00.
Nothing that is already there is wrong, it is just not refreshing. Being fixed
properly rather than re-run hopefully.

---

## 2026-08-03 - Claude Code (34)

**The footage mirror is live and the whole library is on the branch.** 83 clips,
each with a contact sheet and a transcode, on the `footage` branch of this repo.
Until today it carried 25 transcodes and 82 sheets, so there are 58 new clips to
cut from, including all ten screen recordings and the trip set.

Take what you need rather than cloning it, it is 752 MB of video:

```sh
git clone --filter=blob:none --sparse --branch footage \
  https://github.com/nextvisitapp-art/next-visit-site.git footage && cd footage
git sparse-checkout set index          # every sheet + INDEX.md, about 18 MB
git sparse-checkout add clips/trip-trip-13.mp4
```

`INDEX.md` on that branch is the catalogue: duration, resolution, orientation,
the Faces column and the do-not-use list. Read it before pulling any clip.

**Two things to know about it.**

It is unattended. Anything dropped in the Drive `Footage` folder is transcoded
and published to a public branch on the next run, with no one approving it. One
clip arrived that way today and is on the branch now, listed as `unreviewed`.
`unreviewed` means nobody has looked, not that it is clear, and 55 of the 83 are
in that state. Anything with a face in it needs a look before it goes in a cut.

It is best effort on timing. GitHub runs scheduled jobs when it feels like it,
and on this account it skips about three quarters of them, so "within a couple
of hours" is the honest promise rather than a schedule. If something is needed
sooner, the workflow can be run by hand and takes about 40 minutes for a full
rebuild, a few minutes for one new clip.

Nothing is owed to anyone on this. It is here when it is useful.

---

## 2026-08-03 - Claude Code (33)

**The invite flow is on main and live.** Everything entry 32 described as
sitting in a branch is now in production, plus one addition Charlie asked for
after reading it.

What a person actually experiences now, if someone sends them an invite link
and they do not have the app:

1. The page opens already knowing what it is inviting them to - "Em is
   counting down to Tokyo." / "23 sleeps." with **Join Em**, or for a crew
   "Euro Summer leaves in 41 sleeps." / "Charlie, Jess and 3 others are in."
   with **Join the crew**. It is resolved on the server, so that is the first
   thing painted, not a spinner and not the wrong wording.
2. They tap Join and they are in the space, in their browser. No install, no
   account, no App Store. **This now includes iPhone**, which was the wall in
   front of nearly every invitee we have.
3. Once they are actually in and looking at the product, an iPhone gets one
   toast, once ever: "For the full Next Visit experience, get the iPhone app."
   with a Download action straight to the listing. It waits until they are
   past setup, never repeats, and Android and desktop never see it, because
   there is no app to send them to. Checked by a real iPhone-shaped browser:
   it appears, the action reaches the App Store, it does not come back on the
   next visit, and Android stays silent.

Charlie's framing, and it is the right one to write copy against: get people
connected and in the same space first, and the ones who like it will find the
app themselves.

### What this frees up for the words we use

- **"Join without installing anything" is now true everywhere.** It no longer
  needs an iOS asterisk. Any hook built on how fast two people can be in the
  same countdown is honest.
- **The crew-greeted-as-a-couple bug is gone by construction**, so crew
  creatives no longer risk an invitee being welcomed to a romance.
- **The site can lean on the browser** as the way in. Charlie has parked
  promoting it as a website for now, so this is capability, not a campaign.

### Two things to know before reading any funnel number

- **"Invite links opened" was wrong until today.** The event only ever fired
  on a screen a brand-new invitee never reaches, so it had been counting
  existing users tapping links and nothing else. Fixed. Rates from before
  today cannot be compared with rates after; the first clean week starts now.
- **An unfilled invite now gets chased**: one push the morning after the space
  is made, one more five days in, then silence. If join rates move next week,
  that is a candidate cause alongside the flow itself.

### One stale asset

`marketing/product-screens/join-link-invited-view.png` still shows the old
"You're invited / Download on the App Store" interstitial - it was captured
before this changed. `marketing/PRODUCT.md` says so at the point it matters.
The next capture run replaces it.

## 2026-08-03 - Claude Code (32)

**The invite flow got the four changes it needed, and the biggest one was
gated on a test rather than an opinion.**

The claim that an iPhone invitee could not be allowed to join in Safari - the
wall in front of nearly every invitee we have - rested on a plausible worry:
that a browser join creates an anonymous account the installed app never sees,
orphaning the pairing. That is a question with an answer, so it got one. A
check now round-trips it against production: join in Safari, install, come back
as a brand-new anonymous account. **11 of 11 checks pass.** The slot is
reclaimed by name, or by answering "which of you are you?", the inviter is
never disturbed, and a partner who has linked an email still cannot be
displaced by someone who merely has the code. So the wall came down.

What changes for the words we use:

1. **"Join without installing anything" is true again on iPhone.** Join is the
   primary action on every platform; the App Store is a quiet second option.
   Any campaign line about frictionless joining no longer needs an asterisk.
2. **The invite page now shows the thing before it asks for anything** -
   "Em is counting down to Tokyo. 23 sleeps." → Join Em, or "Euro Summer
   leaves in 41 sleeps. Charlie, Jess and 3 others are in." → Join the crew.
   It reads like an invitation from a person rather than an ad from a
   stranger, and it is resolved on the server, so the crew-greeted-as-a-couple
   bug is now impossible rather than merely unlikely.
3. **An unfilled invite finally gets chased**: one push the morning after the
   space is made, one more five days in, landing on the invite card ready to
   resend. Then silence forever - two is the whole budget.

One thing that matters for reading the funnel: **the "invite links opened"
number has been wrong since it shipped.** The event only ever fired on a screen
that a brand-new invitee never reaches, so it was counting existing users
tapping links and nothing else. Fixed, but it means opened-versus-joined rates
from before today cannot be compared with the ones after. The first clean week
starts now.

`marketing/PRODUCT.md` on main is updated to match. All of the above is in the
couples release branch, not yet on main, so the app in your hand still does the
old thing until it merges.

## 2026-08-03 - Claude Code (31)

**The product picture is on main: `marketing/PRODUCT.md` plus 28 named
frames in `marketing/product-screens/`.** Onboarding tap by tap, pairing
from both sides, every screen and what needs a partner, Plus gating and
prices, the planner handoff, notifications, widgets, the data model, and a
blunt gaps list. Written from the deployed code against a same-day capture
run; every claim with pixels has the frame named next to it.

Three findings from writing it that touch marketing copy directly:

1. **The iOS invite link does not join in the browser.** An iPhone invitee
   without the app gets an App Store interstitial (deliberate in code: a
   Safari join would orphan the pairing across two anonymous accounts).
   Android and desktop invitees do join in the browser. So no "they can
   join without installing anything" lines for iPhone audiences; the
   funnel report will show what that wall costs.
2. **Free couples never meet the paywall.** No Together doorway on Home,
   and `/Together` silently redirects free users to /Us (photographed in
   the set). The only doors to the purchase sheet are the Profile card and
   the storage caps.
3. **The crew interstitial greets people as couples** when its crew lookup
   loses the race to first paint. Small, fixable, flagged in the doc.

Housekeeping: the seeded demo crew's live join code was legible in two
captured frames. The public copies on main are redacted; the un-redacted
originals exist only in the private couples repo and the Drive mirror.
Low-urgency ask for Charlie: rotate that crew's invite code from the app
whenever convenient, and the next capture run picks up the new one.

Also today, ahead of the doc: the events security rules are deployed and
verified end to end (a client-path write lands, a mismatched uid is
refused), so the invite-funnel numbers start recording from today.

## 2026-08-03 - Claude Code (30)

**Weekly results pass. Three creatives went out, 1,596 views, zero saves on
everything we can measure.**

### What posted

| Post | Date | Where | Views | Saves / 100 views |
| --- | --- | --- | ---: | --- |
| `dayzero-nofaces` (reel, b-roll, 14s) | 27 Jul | IG + TikTok | 1,086 | **0.00** (0 / 1,086) |
| `planner-stopsaying` (reel, screen recording, 9s) | 29 Jul | IG + FB + TikTok | 295 | **0.00** (0 / 295) |
| "Nine tabs open. Nothing booked." (static feed post) | ~31 Jul | IG + FB | 215 | not in the export |

Read off the exports Charlie put in Drive (`Footage / Analytics exports`, 2 Aug):

- **dayzero-nofaces** - IG 378 views, 279 reached, average watch 5s of 14s, 1
  follow. Skip 72.6%, share 0.3%, like 1.4%. TikTok 708 views. Views kept
  accruing after the first reading (IG 329 to 378, TikTok 700 to 708), so the
  1,029 total in the old log is superseded.
- **planner-stopsaying** - IG 149 + Facebook 54 = 203 views, 102 reached,
  average watch 4s of 9s, 0 follows. **Save rate 0.0%, share rate 0.0%, like
  rate 0.0%, skip rate 84.1%.** TikTok 92 views under a Copenhagen caption; the
  analytics thumbnail is the "Skip the planning / Who's going?" frame, so it is
  the same creative rather than a fourth post.
- **"Nine tabs open"** - 212 IG + 3 Facebook = 215 views, 65 reached.
- TikTok account, 25 to 31 Jul: 945 post views, 6 profile views, 15 likes,
  $0.00 rewards. Audience 86% female, 14% male.

### Two of the three were not in the log

`results.csv` had `dayzero-nofaces` and one bare Instagram row for
`planner-stopsaying`. The TikTok cut of `planner-stopsaying` and the whole
"Nine tabs open" post were missing. Both are in now, with this week's numbers,
in `next-visit-couples/marketing/reels/`.

Worth naming because throughput is the metric that matters most at this stage
and the log was under-reporting it by a third.

Two things I did not fill in. `hook_type` and `pillar` are blank on the new
rows: those are editorial calls made at approval time and reconstructing them
from a screenshot is exactly what RESULTS.md says not to do. And the static
post is recorded as `format=static`, which is **a new value** not in the
RESULTS.md list (face / screen-recording / b-roll) - flagging it rather than
quietly widening the taxonomy.

### The funnel is empty, and that is not yet a finding

`funnel.yml` on main: no events in 7 days. Ran it again at 90 days: also none.
So `countdown_created`, `countdown_shared` and `member_joined` are zero for
every space.

Before anyone reads anything into that: **the instrumentation landed on 29 July**
(`b8e63a9`), five days ago. There were five days in which an event could have
been recorded, not ninety. Zero events in five days at this install volume is
unremarkable and is **not** evidence of a broken pipe.

I checked the two things that would make it one, and both are sound in source.
All three events fire from real call sites (`AddMemory.jsx`, `CrewCard.jsx`,
`CrewStrip.jsx`, `joinSpace.js`), and the `/events` rule in `firestore.rules`
permits exactly the write `analytics.js` makes. What I cannot verify from here
is whether those rules are actually deployed.

The structural problem is worth fixing before it costs a month: `analytics.js`
swallows write errors by design, so **a denied write and genuine non-use look
identical**, and the funnel prints the same line either way. One deliberate
event fired from a signed-in test space would separate them permanently. Say
the word and I will wire it.

### Site traffic: unavailable, as expected

The programmatic Web Analytics API answers `not_found` for `next-visit-site` on
this plan. Retried once in case the plan had changed; same answer. That is by
design on this account, not breakage, and I did not spend time re-diagnosing it.
No traffic figures in this entry.

### Drive sweep: one set, no frames

`Marketing assets / set-03-crew-bookings` contains a `POST.md` and nothing else.
It specs 17 frames (6 at 1080x1920, 6 at 1080x1350, 5 at 1000x1500) with
captions for TikTok photo mode, an IG carousel and a Pinterest pin written as a
search query. **None of the frames are in Drive**, so there was nothing to
commit. The `Posted` folder is empty.

### What the numbers suggest

Three posts. RESULTS.md sets the bar at roughly 20 to 30 before analysis is
allowed to steer, so **this is raw reporting and I am not calling a trend.**
Below that bar any pattern is invented.

Raw, without interpretation:

- Two reels, 1,381 views between them, **zero saves on both**.
- They are different formats (b-roll, screen recording), so neither format has
  failed twice running and **nothing meets the kill rule.** Nothing is cut.
- Skip rate was 72.6% on the 14s b-roll and 84.1% on the 9s screen recording.
  One observation each. That is not a direction.
- The static post reached 65 accounts against the reels' 279 and 102.

The one number that is a finding rather than noise: **three creatives in seven
days is the highest throughput week so far**, and the log caught two of them.

### One ask

**Paste the Instagram insights for the "Nine tabs open. Nothing booked." post,
specifically the saves count.** It is the only post this week whose saves I
could not read - the Drive export has its Overview and Audience tabs but not
Engagement - and saves are the number that decides creative.

If the Vercel dashboard figures for `next-visit-site` and `next-visit-go` are
to hand they would fill the traffic gap too, but the saves number is the one
that changes what gets made next.

---

## 2026-08-02 - Claude Code (29)

**The footage mirror runs itself now. Nobody has to ask for a sync.**

Charlie's call: the hub should never need a human to trigger the mirror. So it
is on a schedule. Every three hours a job lists the Drive `Footage` folder,
compares it against what is already on the **`footage` branch of this repo**,
and processes only what is new or changed. Put a clip in the Drive folder and
within three hours it is on the branch with a contact sheet, a transcode and a
row in `INDEX.md`. There is nothing to trigger and nothing to ask for.

The two-phase split is gone. There is no longer a pass that makes sheets and a
separate pass where somebody picks which clips get transcoded. **Every clip gets
both.** The branch is a couple of hundred MB, but the checkout is filtered, so
taking two clips costs you two clips:

```sh
git clone --filter=blob:none --sparse --branch footage \
  https://github.com/nextvisitapp-art/next-visit-site.git footage && cd footage
git sparse-checkout set index          # every sheet + INDEX.md, a few MB
git sparse-checkout add clips/IMG_9402.mp4
```

`--filter=blob:none` means no file contents transfer until something names
them. The size of the branch is not a cost you pay.

### What is on the branch today, and what lands next

82 clips, all with sheets. 25 already have transcodes. The first scheduled run
picks up the remaining 57, so within a few hours the whole library is available
as ready-to-cut video rather than a sheet you have to request against.

Encoding is unchanged and still worth restating, because it is the thing that
makes these usable: **native aspect ratio, no pre-crop to 9:16.** The crop
window is yours, per shot. Longest side 1920, crf 18, no audio.

### The Faces column still means what it said

Regenerating `INDEX.md` on every run does not touch the review verdicts - they
live in a separate file in the couples repo precisely so a regeneration cannot
wipe them. `unreviewed` still means **nobody has looked**, not "clear", and new
clips arrive unreviewed by definition. `IMG_0059` and `IMG_0063` remain
unusable on faces, `IMG_0048` remains unusable because a political ad plays
across the departure board for its full duration.

### One consequence worth naming

The mirror is unattended, and this repo is public. Anything dropped into the
Drive `Footage` folder from now on is published automatically, permanently, and
without anyone looking at it first. Deleting later does not unpublish it. That
is the trade for not having to ask for a sync, and it is fine for b-roll, but it
means the Drive folder is now a publishing surface rather than a scratch space.

Nothing is waiting on anyone.

---

## 2026-08-01 - Claude Code (28)

**Review sheets now live in git, and the first one rejected a cut.**

Charlie's call: a sheet in Drive is a sheet neither of us can look at, because
the hub can clone a repo but cannot pull a binary out of Drive. So the split is
now by what a file is for. Videos go to Drive, which is where the source lives
and where finished cuts get collected. Every JPEG the reel pipeline makes goes
to **`marketing/review/`** in this repo. That covers the render contact sheet,
the feed still, the probe sheet and the footage index.

`marketing/review/README.md` says what each file is and how to read one.

### The sheet paid for itself immediately

The first render checked under the new rule failed. `-t` sits after `-i` in the
clip render, so it caps the OUTPUT duration, and `setpts` has already stretched
the clip by then. Every held clip was being cut straight back to its native
length: the closing shot slowed to 3.00s played 1.46s, the app countdown held
to 1.60s played 0.75s. The holds did nothing.

Nothing else could have caught it. The clip list recorded the length **asked
for**, so the total, the plate windows and the end mark were all computed
against a timeline that did not exist, and the log printed 10.33s for a 7.9s
file. Every check of intent agreed with every other check of intent. In the
version that would have posted, **the end mark never drew a frame** - it was
scheduled a second and a half past the last one - and the second plate bled off
the app screen onto the boarding shot.

Fixed, and the durable part is the second item: clip lengths are now **probed,
not assumed**, and a clip that misses its target by more than 50ms fails the
run. The assembled cut is probed too and must match the plate timeline. That
kills the class of bug rather than this instance of it.

The re-render is verified frame by frame and its sheet is committed:
`reel-fiji-longweekend.jpg`.

### The footage index settles an open question

`footage-index.jpg` is one labelled frame per clip in the Drive Footage root,
so a clip called `IMG_1234.MOV` can finally be picked by what is in it.

Reading it answers something that had been running on assumption: **there are no
raw island, palm, water or boarding clips in that folder.** All the Fiji
material lives inside the single edited MOV the reel is cut from. The raw
footage is airports, Brisbane river and skyline, a farmers market, domestic gate
boarding, and a long run of concert and festival clips.

Two consequences worth carrying forward:

1. **The Fiji cut has no sunset and cannot have one.** The brief asked for the
   end mark over a sunset; the source edit's closing shot is midday water, and
   no choice of timecode changes that. The only genuinely warm-light clip in the
   whole folder is `IMG_9402.MOV`, dusk cloud over water, and it is not Fiji.
   The reel currently opens and closes on near-identical bright resort-from-the-
   water framing, which is the weakest thing about it.
2. **A Drive folder cannot deliver footage to the hub**, for exactly the reason
   a sheet in Drive cannot deliver a sheet. `~/Google Drive` on the Mac is a dead
   2020 Backup and Sync folder and nothing syncs into it, so that is not a route
   either. Recommendation: retire `_hub-footage`, keep Drive as the render
   source only (the pipeline reads it with credentials inside Actions, which
   works), and give the hub the index sheet plus small proxies of any clip it
   names. Committing 64 raw MOVs to git is not the answer.

### One thing Charlie can do in two minutes

A fine-grained PAT with `contents: write` on `next-visit-site`, saved as
`SITE_REPO_TOKEN` in `next-visit-couples`. The pipeline already checks for it
and switches by itself: with it, every run drops its sheets straight into
`marketing/review/`. Without it they land in a `review-outbox/` in the couples
repo for a session to carry across, which leaves a couple of MB of JPEG in that
repo's history per render.

Worth recording why the obvious route was not taken: the workflow does upload a
run artefact, and it is fine for a human on github.com, but a Claude Code
session cannot fetch it. GitHub serves artefact downloads from
`*.blob.core.windows.net` and this org's egress policy answers 403 to CONNECT
for that host. Git is reachable; blob storage is not.

_- Claude Code_

---

## 2026-08-01 - Claude Code (27)

Housekeeping so this file stops taxing every session that reads it:
**entries 1 to 19 are archived to `marketing/HANDOFF-ARCHIVE.md`**, verbatim
and in order, nothing edited. This file had grown to about 113KB and the
session-start rule means every marketing session pays to read all of it;
the working set is entries 20 and up, so that is what stays.

Catch-up digest for a fresh session: stills posted as photo reels are the
default format - TikTok photo mode first, IG carousel second, Pinterest as
the compounding search channel (entry 20). Design holds the creative reins
for concepts, formats and the calendar; Code is infrastructure - captures,
commits, results.csv, analytics (entry 22). Delivery is Drive plus a
POST.md per set; saves per 100 views is the verdict; the brand system is
binding; Charlie posts and films, nothing else. Production tooling now
covers both reel types: an ffmpeg video-editing skill for footage cuts and
a Remotion pipeline in `marketing/reel/` for code-rendered reels (entry 24).

Also in `.claude/skills/` in this repo: two vetted marketing skills, `cro`
(landing page conversion audits) and `seo-audit` (technical and on-page
SEO, including the search-intent discipline Pinterest needs), both from
coreyhaines31/marketingskills, MIT, evals dropped. The token-heavy
task-observer skill is removed from all four repos to cut per-session
overhead, and an App Store ASO skill went into the couples repo alongside
the app.

_- Claude Code_

---

## 2026-08-01 - Claude Code (26)

**Entry 24's open flag is closed, on evidence rather than argument.** The
question was whether animating the wordmark tile by tile makes it a variant of
a locked mark. Charlie said settle it, so I stopped reasoning about it and
rendered it.

**It is the mark.** The reel's per-tile markup at rest and `<LogoA/>` imported
from `brand/marks.jsx` render **byte-identical PNGs** (md5
`df69a65a53bfecb7107f2872a41de00e` both). The animation wrapper changes
nothing about the mark itself; it only changes how the tiles arrive. Same
`FlapChar` atom, same `round(w * 0.077)` gap, same 70/52 aspect. Nothing
redrawn, nothing restyled, CLAUDE.md 4 intact.

### The check is committed, so it stays true

A one-off verification rots the moment a template changes, so it is now a
guard rather than a note: **`npm run verify:marks`** in `marketing/reel/`
renders both and exits non-zero unless they match. Run it after touching any
template that renders the wordmark, and after any change to `brand/marks.jsx`.

I also confirmed the guard can fail, which is the part people skip: nudging
the tile gap from 0.077 to 0.09 (about 1.3% of tile width, invisible to the
eye) makes it exit 1 with a diff to compare. A check that cannot fail is
decoration.

### Why bother

The marks are the one part of the system CLAUDE.md calls locked, and
programmatic video is the first thing we have built that reassembles a mark
from its atoms rather than importing it whole. That is exactly where drift
would enter, silently, and end up on a store listing before anyone noticed.
Now it cannot ship without failing a check first.

_- Claude Code_

---

## 2026-08-01 - Claude Code (25)

**Structure change, and it supersedes the ownership split in every entry below
this one.** Charlie's call, made today.

- **Cowork owns the thinking**: marketing strategy, concepts, hooks, the
  calendar, and the still sets. He works there directly and it replaces both
  the Design creative reins from entry 22 and the strategy role I have been
  playing in this log.
- **I own video**: programmatic reels and footage-led cuts, on request, plus the
  infrastructure I already ran (capture, committing assets, `results.csv`,
  analytics, the Monday results pass).
- **Claude Design is out of the loop.** Not a criticism of the work; the routing
  simply changed. Entries 1 to 24 are addressed to Design and several ask it
  open questions. **Those questions are closed. Nothing here is waiting on
  anyone.** The header now says so, and so does `CLAUDE.md` in this repo and in
  couples, which both still described marketing as a Code plus Design split
  until today.

### Both video toolchains are verified working, not just installed

I proved these end to end in a cloud session today rather than assuming:

- **Remotion.** `CountdownReel` rendered clean: 390 frames, 1080x1920, 30fps,
  13.06s, h264. Frame checks confirm it holds the brand - navy-led, Fraunces
  headline, DM Mono eyebrows, exactly one pink moment on "Today.", marks
  imported not redrawn. Deps install in about 12 seconds; the container browser
  quirk is already handled in `remotion.config.js`.
- **ffmpeg.** Not preinstalled in a fresh cloud container. `apt-get install -y
  ffmpeg` fixes it in one step and the `video-editing` skill (trim, silence
  jump cuts, captions, overlays, speed) then works. Worth knowing so a future
  session does not read a missing binary as a broken skill.

So graphics-led motion costs a render, and footage-led cuts cost an edit. Both
are same-session turnarounds.

### What I need from a concept to return a cut

A POST.md-shaped brief: the one-line idea, the hook for frame one, the beat
list, the surfaces, and the copy. Everything else is mine. If the concept needs
a screen that does not exist in `screens/`, name the route and I will capture it
rather than compose around the gap.

### Standing measurement, unchanged

Sets and cuts land in Drive with a POST.md, I commit them to
`marketing/social/`, every post gets a `results.csv` row, saves per 100 views
stays the verdict, and the Monday pass writes the read here. Entry 5's finding
still stands and is not relitigated: countdown montages earned zero saves, so
the `CountdownReel` template is a capability demo on the brand's own gesture,
not a format recommendation.

_- Claude Code_

---

## 2026-08-01 - Claude Code (24)

Production capability shipped, logged so it is in the record: **reels can now
be rendered from code.** Charlie asked for it directly today, so I built the
pipeline rather than proposing it first.

### What exists now

- `marketing/reel/` is a Remotion project. Compositions are React: they import
  the real `brand/marks.jsx` and `tokens/tokens.css`, so brand output is exact
  by construction rather than by care. Render with `npm run render` inside the
  folder. Works in cloud sessions and on the Mac; the container browser quirk
  is handled in `remotion.config.js`.
- One template so far: `CountdownReel` (13s, 1080x1920 master, safe area per
  entry 21). Hook line, the wordmark assembling tile by tile, a 38-sleeps
  countdown, one pink moment at "Today.", end card on the icon. A test render
  went to Charlie today.
- `.claude/skills/` gained `remotion-best-practices` (the official Remotion
  rules bundle) plus a vetted `video-editing` skill (ffmpeg: trim, silence
  jump cuts, styled captions) here and in couples. That one covers footage-led
  cuts, so both halves of reel production are now tooled.

### What this is and is not

Entry 5's measurement stands: countdown montages earned zero saves, and I am
not relitigating it. This template is a capability demo on the brand's own
gesture, not a format commitment. Concepts, hooks and the calendar are yours
(entry 22). What changes for you: graphics-led motion is now roughly as cheap
as a still set. Name a concept and a POST.md-shaped brief and I can hand back
a rendered cut the same session, tokens-true, no filming, sized for the three
surfaces.

### One flag for your veto

The animated wordmark assembles NEXTVISIT from the exported `FlapChar` atom
using LogoA's exact geometry (gap = 7.7% of tile width), because per-tile
animation needs per-tile wrappers. Same atoms, same construction, nothing
redrawn or restyled. If you read that as a variant rather than the mark, say
so and I will animate the assembled `LogoA` as one block instead.

_- Claude Code_

---

## 2026-07-31 - Claude Code (23)

Production change from Charlie, logged so nobody duplicates work: **he is
making the stills himself in Cowork now.** Design - do not build sets unless
Charlie asks you directly. Entry 22's reins stand for anything he does route
to you, but set production is his and Cowork's.

The measurement machinery is production-agnostic and unchanged: sets land in
Drive with a POST.md, I commit them to marketing/social/, every post gets a
results.csv row, saves per 100 views stays the verdict, and the weekly
results pass writes the read here every Monday morning.

Analytics re-verified live today against the current production deploys:
real-browser check green on hello, hello/premium and go - script served and
pageview accepted with 200s on all three. The programmatic API stays
plan-blocked, so the Vercel dashboard remains the read surface for site
traffic.

_- Claude Code_

---

## 2026-07-31 - Claude Code (22)

Two calls from Charlie, and the second one changes your job.

**Sets 01 and 02 are deleted.** His call, his files. Do not rebuild them, do
not reference them, nothing to salvage. Blank page.

**You have the creative reins for Next Visit's marketing.** Not just the
slideshow sets - concepts, formats, channels, the calendar, the voice of the
posts. Make what you believe in, in whatever order you believe in it. My entry
21 build order is hereby a suggestion in your queue, not a commission - take
the crew-bookings story if you rate it, ignore it if you have something
better. You do not need my sign-off per set, per concept, or per channel, and
you do not need to wait for a reply to this entry before producing.

The strategy context in entries 20 and 21 still stands as information - what
measured zero, where distribution actually is, what the seeded crew makes
possible - but it is input to your judgement now, not instructions.

### The four things that stay fixed

1. **The brand system stays binding.** Tokens, locked marks, pink discipline,
   type roles, `marketing/STILLS-BRIEF.md`. It is your system - you built the
   discipline into it. If a concept genuinely needs to break a rule, propose
   the change here first (CLAUDE.md 10: the system grows on purpose). "Go
   crazy" is about ideas, not about the wordmark.
2. **Delivery stays Drive plus a `POST.md` per set** (the convention in entry
   21's delivery section). Not as a creative constraint - because work that
   cannot be posted in two minutes is the failure mode that has now killed
   three finished pieces. If it is not in Drive with a POST.md, it does not
   exist.
3. **The scoreboard stays on.** Everything posted gets a row in `results.csv`
   and saves per 100 views stays the verdict - with RESULTS.md's discipline
   that no trend is real before roughly 20 to 30 posts. Full freedom on what
   to make; no freedom on whether it gets measured.
4. **Charlie's surface stays tiny.** He posts, he films, nothing else. If a
   concept needs his hands beyond that, it lands here as one specific ask.

### What I am to you now

Infrastructure. Captures on request (name a route and I capture it rather
than you composing around a gap - today's 21-frame set, crew frames included,
is already in your folder), committing what you drop, calendar mechanics,
the results log, and analytics.

On analytics: **collection is confirmed live** - Charlie can see traffic in
the Vercel dashboard, so the make-post-measure loop is finally closed. The
programmatic API is still answering not_found (chasing it; likely an API
surface quirk rather than missing data), so until I post numbers here, site
traffic reads come from Charlie's dashboard and post performance from the
platform exports as always.

Go.

_- Claude Code_

---

## 2026-07-31 - Claude Code (21)

**You are building the slideshow sets themselves now, not just specifying them.**
Charlie's call. Cowork produced sets 01 and 02, they did not come out right, and
they never reached Drive - so there is nothing to salvage and nothing lost.
Rebuild from here. Entry 20 stands as the strategy; this is the production brief
so you never have to ask what to make next or in what shape.

The channel from here is you and me. Charlie posts and films; he does not
compose, relay or decide the queue.

### Two things changed since entry 20

**A fresh capture ran today**, so `screens/` is current against the live build
rather than the 29 Jul set. Same contract as always: `screens/manifest.json` is
the record, `s01..s21`, 1290x2796. **s19, s20 and s21 are the crew frames** from
the seeded Euro Summer - countdown, join code, and the bookings panel with two
rows booked and two not. That mixed state is the strongest single asset we have
and it did not exist a week ago.

**Analytics is instrumented but not yet readable.** The beacon is live on all
seven pages and a real Chrome run confirms Vercel accepts the pageview. The
query API still answers `not_found`, which I am still chasing. So keep judging
work on saves per 100 views from the platform exports, not on site traffic, and
do not let anyone quote a site number until I post one here.

### The three surfaces, in the order they matter

1. **TikTok photo mode.** The primary target. It gets real For You distribution
   and native music. Design for this first and the rest are crops.
2. **Instagram carousel.** Free second placement, mostly served to people who
   already follow us. Worth posting, not worth optimising for.
3. **Pinterest.** The compounding one. A pin earns for months against search
   intent, and it is still the largest miss in the plan. Every set should have a
   Pinterest cut with a search-shaped title, not a mood-shaped one.

### The build

- **Sizes.** `1080x1920` is the master (TikTok photo mode + Stories).
  `1080x1350` for the IG carousel cut. `1000x1500` for Pinterest per
  MARKETING.md 7.2. Compose the master first, then recut - do not design three
  separate things.
- **Length.** Ten frames is the ceiling and six is a perfectly good set. **Do
  not pad to ten.** A set that runs out of things to say at frame seven should
  be seven frames.
- **Frame 1 is the whole hook.** In a photo post the first frame is the entire
  first impression, exactly as the first two seconds are in a reel. Reel one
  died at 5 seconds of 14 with a hook that asked the viewer to care before it
  gave them anything. Frame 1 names a problem the viewer is already inside.
- **Safe area on the 1080x1920 master.** Keep every must-read element between
  **y=320 and y=1450**. TikTok's caption and username sit over the bottom, the
  action rail sits over the right edge below roughly y=900, so nothing that has
  to be read should land at `x>880` down there. On the 1080x1350 IG cut, 100px
  margins and keep the bottom 120px clear of type.
- **Brand.** `marketing/STILLS-BRIEF.md` is binding: navy-led, tokens only, one
  pink moment per frame, mono eyebrow above a Fraunces headline, marks imported
  never redrawn, Space Grotesk for marks only. No em dashes.

### Delivery, which is the part that has failed twice

A set that is not in Drive does not exist. You have write access, so this is
yours end to end now.

- **One folder per set** in the Drive folder, named `set-03-crew-bookings` and
  so on.
- **Frames** named `01.png`, `02.png` in post order, in a subfolder per format:
  `1080x1920/`, `1080x1350/`, `1000x1500/`. Post order is filename order, so I
  never have to guess the sequence.
- **A `POST.md` in every set folder** carrying: the one-line idea, the caption
  for each platform, hashtags, a music direction (mood and tempo, not a specific
  track - Charlie picks from the in-app library so it stays native), and the
  Pinterest title written as a search query. That file is what makes a set
  postable in two minutes instead of twenty.
- I commit whatever lands into `marketing/social/` and log it.

### The first three sets, in build order

**Set 03 - the crew bookings panel.** Source `s19`, `s20`, `s21`. The strongest
story we own and newly shootable. The arc: the group chat that never books
anything, one shared number everyone sees, the panel where two things are booked
and two are not, one tap to claim one, one code to get everyone in. This is the
same beat as reel recipe 7 in `REELS-SHOTLIST.md`, and the plate copy there is
agreed - reuse it rather than writing new lines.

**Set 04 - the memories map.** Source `s08`, `s09`, `s10`. Wanderlust plus
keeping the trip after it ends. Softer, more saveable, a different pillar so we
are not testing the same idea twice.

**Set 05 - Pinterest search intent.** Titled as an answer, not a mood. "How to
plan a group trip without the group chat" is the shape. Same frames are fine;
the title and frame 1 are what change.

### What is mine

The capture runs and the manifest, committing what you drop, the posting cadence
and `results.csv`, the analytics API, and the one screen cut a week that keeps
the App Store preview fed. If you need a frame that does not exist in `screens/`,
name the route and I will capture it rather than have you compose around a gap.

_- Claude Code_

---

## 2026-07-30 - Claude Code (20)

Charlie's proposal, in his words: photo stills posted as photo reels with music,
for most or all marketing, because it is quick, professional and it shows the
product. **I agree with the direction and I am formally moving the plan to it.**
Your entry 5 and `content-system.md` argued for this on the 29th; the only new
thing is that Charlie now wants it as the default rather than the supplement.
So this entry is the commission, plus three corrections and one problem.

### The measurement hole is closed, so we can stop guessing

Web Analytics was enabled in the Vercel dashboard for both `next-visit-site` and
`next-visit-go` and **was collecting nothing**. Neither project is Next.js, so
the dashboard's React instructions never applied and the beacon script was never
on the page. The snippet is now live on all seven pages, and a real Chrome run
confirms `POST /_vercel/insights/view` on `hello`, `hello/premium` and `go`.

Worth knowing, because it will bite anyone who tries to verify this: the Vercel
insights script refuses to send anything when `navigator.webdriver` is true or
the UA contains "Headless". Every automated check reads as zero traffic on a
perfectly healthy page. The committed workflow
(`.github/workflows/analytics-smoke.yml`, manual dispatch) defeats both halves,
so "is analytics dead" now has a one-minute answer instead of a guess.

**Do not quote a site number yet.** The beacon fires; the analytics API still
answers `not_found` for both projects, which I am still running down. When it
reads, it reads for real.

### Crews is seeded, so A18 to A22 is unblocked

"Euro Summer" now holds 5 members (Jess, Liam, Priya, Noah plus the owner), an
upcoming Barcelona trip at 38 days, two past trips with 7 photos, a six-item
plan with per-member attribution, and **a four-row bookings panel with two rows
booked and two not**. That mixed state is the A20 shot you called the one that
has to be right, and it is the thing the lead reel could not be cut without.

The seed refreshes on a re-run, so it can be re-warmed the morning of a shoot.

### The three corrections to "stills for everything"

1. **"Photo reel" means TikTok, not Instagram.** TikTok photo mode gets real For
   You distribution. Instagram has no true photo-reel format - a still set is a
   carousel, and a carousel is served mostly to people who already follow us.
   Your slideshow brief already says "not a reel" for IG and it is right. So
   stills are a TikTok-first bet with IG as the free second placement, and we
   should stop expecting IG reach from them.
2. **Pinterest is the half of this that compounds**, and it is still not open.
   A pin keeps earning for months against search intent we have no other way to
   reach. Every set we build is already Pinterest-shaped. This is the largest
   remaining miss and it needs no filming and no new work.
3. **Keep one screen cut a week.** Not because video is better - reel one says
   otherwise - but because the App Store preview needs real screen recordings
   regardless, and A18 to A22 is now the cheapest video we will ever have. One
   tier 2 cut a week, not a produced shoot.

### The problem, and it is the same problem as last time

**The two ten-frame sets are not in Drive.** Slideshow 02 has only its README
doc there; Slideshow 01 has nothing at all. The frames are on Charlie's Mac. So
you cannot see them, I cannot commit them, and they cannot be posted from
anywhere but that one machine.

That is the exact failure `content-system.md` named: work gets made, then waits.
Two finished sets and one finished reel are currently worth zero for the same
reason. **Frames land in Drive or they do not exist.**

### What I am asking you for

A standing still series rather than another one-off set, so the queue never runs
dry and Charlie never picks what to post.

- **Format:** 1080x1920 for TikTok photo mode and Stories; 1080x1350 for the IG
  carousel cut of the same idea. Ten frames is the right length; six is fine
  when the idea is smaller. Do not pad to ten.
- **Source:** `screens/` in the couples repo, currently 21 frames at
  `manifest.json` commit `f3b3ee1`, app 1.3.2 - including **s19, s20 and s21**,
  which are the crew countdown, the join code and the bookings panel from the
  seeded Euro Summer. Those three are the group-chat story and they exist now.
- **Build:** per `marketing/STILLS-BRIEF.md`. Navy-led, tokens only, one pink
  moment per frame, Fraunces headline with a mono eyebrow, marks imported not
  redrawn. Frame 1 carries the whole hook - in a photo post it is the entire
  first impression, the way the first two seconds are in a reel.
- **Delivery:** finished PNGs into the Drive folder, named for where they go. I
  commit them to `marketing/social/`. A set without frames in Drive is not a
  set.
- **Next three sets, in the order I would build them:** the crew bookings panel
  (s19-s21, the strongest thing we have and newly shootable), the memories map,
  and a search-intent Pinterest set aimed at "how to plan a group trip" rather
  than at a mood.

### What is mine

Posting cadence and the results log, the analytics API question above, and
committing whatever you drop. I am not going to ask Charlie for anything until
there is a set in Drive to post.

_- Claude Code_
