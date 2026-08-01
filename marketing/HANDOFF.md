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
