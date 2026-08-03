# Next Visit - how the product actually works

Written for the marketing side, 3 Aug 2026, from the code as deployed (app
version 1.3 line). Screenshots referenced throughout live in
`marketing/product-screens/` - every image is seeded demo data, not user data.
The one live join code that appeared in two frames is redacted in the copies
here. This is a diagnosis document, not a brochure: the last section says what
is missing or half-built, bluntly.

One vocabulary note used everywhere below: a **space** is the shared thing a
user belongs to. It is either a **couple** (two named slots) or a **crew** (a
flat member list). Almost every behavior forks on that distinction.

---

## 1 · Onboarding, step by step

There is no signup. On first launch the app signs the user in **anonymously
in the background** - no email, no password, no login screen, ever. A brand
new user goes from cold start to a working space in as little as four taps.

The sequence (`onboarding-fork.png`):

1. **Cold start** - splash (~3 to 4 seconds), then the fork screen: the
   wordmark, the question **"Who do you travel with?"**, and three choices:
   - **Us two 💕** - "The space for you and your partner"
   - **The crew ✈️** - "Plan a trip with your mates"
   - **I've got a code** - an underlined text link below the two cards
2. What happens next depends on the card:

### The couple path (Us two)

1. Tap **Us two** → name step: one field, "your first name", Continue.
2. Space is created immediately. No date, no partner details, nothing else.
3. **The invite step** - "share with your partner": the invite message with
   the link and code, one primary button (**Send to my partner** - opens the
   system share sheet, or copies to clipboard where share is unavailable).
4. After sharing (or if the share sheet is dismissed), the flow moves on: if
   no email is linked yet, a **link-email step** offers account recovery;
   it is skippable. Then the user lands on Home.

**Where the invite sits and how skippable it is:** it is step 3 of 4, after
the space exists, and it cannot hard-block - dismissing the share sheet
counts as done. There is no "are you sure you don't want to invite" moment.
A user who skips lands on an **unpaired** space (see section 2).

### The crew path (The crew)

1. Tap **The crew** (`onboarding-crew.png`) → two fields: your first name,
   name the crew. One button: **Create the crew**.
2. Crew is created. Straight to the share step (`"<crew name> is live"`):
   the join code rendered huge in the middle of the screen, primary button
   **Invite the crew** (share sheet), ghost button **Into the app →**.

The share moment is deliberately the climax of crew onboarding, and the
ghost button is the skip. Skipping leaves a crew of one.

### The code path (I've got a code)

1. Tap **I've got a code** (`onboarding-code.png`) → one input for either
   kind of code. Focusing the empty box silently reads the clipboard and
   pastes a valid code if one is there - this is the handoff from the
   "get the app" web page, which copies the code before sending someone to
   the App Store.
2. The server peeks the code and answers with what it is:
   - **Crew code** → "Joining <crew> - which one are you?" with the member
     names as chips plus "I'm new here". Picking a chip reclaims that spot
     (so a returning member never duplicates themselves); "I'm new here"
     joins as a new member after a name field.
   - **Couple code** → the slot logic: an empty partner slot is filled
     directly after a name; if both slots are filled and the name is
     ambiguous, "Which of you are you? Tap your name."
3. Joining lands straight on the space's Home, already populated with
   whatever the space has.

An invite **link** (rather than a typed code) skips the box entirely: it
lands pre-peeked on step 2. See the next section.

---

## 2 · Pairing, both sides of it

### What the inviter does and sees

The invite is a six-character code wrapped in a link:
`next-visit.app/join/<code>`. It is surfaced in four places:

- The **onboarding share step** (both paths, above) - the intended moment.
- **Home** - an invite-partner card that renders persistently on a couple
  space while the second slot is empty, and disappears forever the moment a
  partner joins.
- **Profile (You tab)** - the same offer as a card with three actions: text
  it (opens the SMS composer prefilled), share it, copy the code
  (`crew-members-invite.png` shows the crew version: the member list with
  the join code beneath).
- **Crew surfaces** - the crew card and member strip both carry an invite
  action at all times; crews are joinable forever, not just at setup.

Nothing actively re-prompts the inviter. The cards sit there; no push, no
banner, no reminder ever fires about an unfilled slot. (Flagged in section
9 - this is passive by design but probably too passive.)

When someone joins, the inviter's app updates live (the space document is
subscribed): the partner's name and photo appear, the invite cards vanish.
As of the current release branch, that moment also triggers the App Store
rating prompt on the inviter's device - the join is the strongest "this
product worked" signal the app has.

### What the invited person receives and sees

They receive a message like *"Join me on Next Visit ✨ Tap to join our
space: next-visit.app/join/ABC123 - code ABC123 if it asks."*

**If the app is installed** (iPhone): the link is a Universal Link - iOS
opens the app directly into the join flow. No code typing.

**If the app is not installed** - the common case, and as of 3 Aug the same
on every platform: the link opens a page that already knows what it is
inviting them to. The space is resolved on the server before the page is
sent, so the first thing painted is real - "Em is counting down to Tokyo."
with "23 sleeps." beneath it, or "Em made a space for the two of you." when
there is no trip yet, or for a crew "Euro Summer leaves in 41 sleeps." with
"Charlie, Jess and 3 others are in." One action: **Join Em** / **Join the
crew**. On an iPhone there is also a small second line offering the app.

Tapping Join runs the join in the browser and they are in the space. No
install, no account, no App Store. That is true on iPhone now too: until
3 Aug an iPhone invitee was diverted to the App Store first, on the
reasoning that a Safari join would create an anonymous account the
installed app never sees and orphan the pairing. That turned out to be
false, and is now checked on a schedule rather than assumed: a browser
join is reclaimed by the post-install account, by name or by answering
"which of you are you?", with the inviter untouched.

Once someone is actually in a space on the web, an iPhone gets **one**
toast, once ever: "For the full Next Visit experience, get the iPhone app."
with a Download action. Nothing else asks. Android and desktop never see
it, because there is no app to send them to.

Two consequences worth carrying into copy. "Join without installing
anything" is now true everywhere, so it no longer needs the iOS asterisk.
And the couple-versus-crew wording bug is gone by construction rather than
by timing - the old page guessed couple, then corrected to crew only if a
background lookup won the race, so crew invitees were regularly greeted as
though joining a romance. Nothing client-side guesses any more.

**The screenshot is out of date.** `join-link-invited-view.png` still shows
the old "You're invited / Download on the App Store" interstitial - it was
captured before this changed. Treat the words above as the truth until the
next capture run replaces the frame.

After joining: they land on the space's Home. For a couple, both phones now
show the same countdown, and every shared surface (Us, Memories) is live
for both. For a crew, they appear in the member list.

### Unpaired versus paired, screen by screen (couples)

| Screen | Unpaired (partner never joined) | Paired |
| --- | --- | --- |
| Home | Full countdown + trips work solo. Persistent invite card. Hero subtitle falls back to "with your partner 💕" | Partner name/photo in the hero; invite card gone |
| Us | Renders, but it is a duet page: song, streaks, mood, poke, presence all show a single-sided or empty state | The actual shared-rituals page |
| Memories | Fully usable solo | Same, but both partners' uploads appear |
| You (Profile) | Invite card + "Joining your partner instead?" recovery entry | Partner line, anniversary stats, quiet "wrong person joined?" link |
| Together (Plus) | Games render but every one of them is built for two - solo they are dead weight | The live premium hub |

Nothing ever locks an unpaired user out; the app just gets emptier the more
shared the surface is.

---

## 3 · Every screen, where it lives, and what needs a partner

### Navigation

Four bottom tabs plus a centre FAB, swipeable left-right:

- **Couples:** Home · Us · Memories · You, FAB = add a memory/trip.
- **Crews:** Home · **Plan** · Memories · You - crews swap Us (couple
  rituals) for Plan (the web planner entry) at the same position.

Everything else hangs off those four.

### The screen inventory

| Screen | Route | Reached from | Without a partner |
| --- | --- | --- | --- |
| Home (couple) | `/` | tab | Works. Emptier. (`home-couple-countdown.png`, free tier: `home-free-tier.png`) |
| Home (crew) | `/` | tab | Works with any member count (`home-crew-countdown.png`) |
| Us | `/Us` | tab (couples only) | Renders but is a duet page; mostly pointless solo (`us-shared-space.png`) |
| Memories grid / map | `/Photos` | tab | Fully solo-usable (`memories-grid.png`, `memories-map.png`) |
| Memory detail | `/memory/:id` | grid tap | Solo-usable; crews get the who-booked-what card (`memory-detail.png`, `crew-bookings.png`) |
| Add a trip / memory | `/add-memory` | FAB | Solo-usable (`add-trip-form.png`) |
| You / Profile | `/MyProfile` | tab | Solo-usable; carries invite + notification prefs + appearance + upgrade card (`profile-couple.png`) |
| Together hub | `/Together` | Home doorway (Plus couples only) | Every feature inside assumes two people (`together-hub.png`) |
| Together sub-pages | `/Together/:category` | hub | Health, dream and explore, games - all two-person (`together-health.png`, `together-dream-explore.png`, `together-surprise.png`, `together-passport.png`) |
| Bucket list | `/BucketList` | Us / tiles | Solo-usable (`bucket-list.png`) |
| Dream destinations | `/DreamDestinationsPage` | Us / tiles | Solo-usable (`dream-destinations.png`) |
| Anniversaries | `/Anniversaries` | Us | Solo-usable, couple-framed |
| Quiz | `/Quiz` | Us | Needs both partners to answer for results |
| AI date ideas | `/AIDateIdeas` | Us | Solo-usable, couple-framed |
| Postcard | `/Postcard` | notification / Us | Two-person by design |
| Little things | `/LittleThings` | Us | Couple-framed |
| Save from planner | `/save-trip` | inbound from go | n/a (transit screen, writes and redirects) |

The one-line summary for positioning: **Memories and the countdown carry a
solo user; everything with a heartbeat needs the second person.** The
product without a partner is a nice trip tracker. The product with one is
the actual product. That is why the invite funnel matters more than any
other number.

---

## 4 · Plus: what is gated, prices, where the paywall appears

One paid tier: **Plus, A$3.99/month** (auto-renewing subscription via the
App Store; the button shows the buyer's localised store price). A yearly
product slot exists in the billing scaffold but no yearly price is live.
"Together" appears internally as a tier name - it is the same feature set
as Plus, kept for comped and internal spaces; there is no separate purchase.

**Free tier** (the hook): countdown and unlimited upcoming trips, memories
up to **10**, photos up to **150**, videos up to **15**, the whole web
planner, basic AI.

**Plus unlocks:** photo cap **2,000**, video cap **100**, unlimited
memories, and the entire Together world - walk-together (steps mapped onto
the route to the next trip), the weekly step face-off, shared streaks, the
couple passport, the games hub (guess-where, same sky, first up, closing
distance, date-night roulette, local tourist), **surprise trips** (plan a
trip your partner sees only as a masked countdown), and the **iOS
home-screen widgets**.

**Where the paywall physically appears:**

1. The **upgrade card on the You tab** - the only always-available door.
2. The **photo/video cap wall** - hitting the free cap mid-upload offers
   "Upgrade to Plus" and opens the sheet.
3. The **memory cap** - the 11th memory on free.
4. Navigating to `/Together` on a free space does not show a paywall - it
   silently **redirects to /Us**. That behavior is photographed:
   `together-free-redirects-to-us.png` is a free user navigating to
   /Together and landing on Us. No capture of the actual purchase sheet
   exists in the set (noted in section 9).

And the fact that matters for diagnosis: **a free couple never sees the
Together doorway on Home.** Premium spaces get the doorway where free
spaces get two utility tiles, so the flagship paid surface is invisible
until after purchase. Free users meet Plus only through the Profile card or
by hitting a storage cap. Crews never see the doorway at any tier - the
Together world is couple-only.

---

## 5 · The web planner (go.next-visit.app)

Standalone, public, no auth, no install. The flow:

1. **Landing** - "Skip the planning": who is going (solo / couple / group),
   origin city, then where and when (or "surprise me" style prompts).
2. ~30 seconds of building, then **the result** (`planner-results.png`): a
   named trip page with a hero photo, the route map for multi-stop trips
   (`planner-route-map.png`), per-leg **flight links prefilled with the
   right airports and dates** (`planner-flights.png`), stays per stop, a
   **prep section** - essentials checklist, travel info, and a drafted
   leave-request email for work (`planner-prep.png`) - and **AI-picked
   activities** tailored by selectable priorities (`planner-ai-activities.png`).
   Every booking link is a real deep link the user books themselves;
   affiliate commission is disclosed on the page.
3. The page is shareable by URL - the whole trip state is encoded in it.

### How a result gets into the app

The result page ends on a handoff card: **"Don't lose this trip - plan it
together"** with the primary button **Save to Next Visit**. Tapping it
opens `next-visit.app/save-trip?...` with the whole trip in the URL. The
app (or web app) silently writes the trip and lands on Home with a
"just saved" banner and a **View trip** button. There is no import screen -
the trip just appears, hero photo and all. Editing later round-trips back
into the planner and updates the same trip rather than duplicating it.

**A user without the app** at the end of the planner: the save still works,
because next-visit.app is the full product in a browser - "Save without an
account · Add email later" is printed under the button, and it is true
(anonymous auth again). As of this week the card also carries a plain App
Store link ("Or get the Next Visit iPhone app"), and all planner pages
serve the Safari smart banner.

Inside the native app the planner opens in the app's own webview, so
"Save to Next Visit" stays in-app - the same page serves both audiences.

---

## 6 · Notifications and the widgets

### Notifications

All partner/crew pushes, delivered via the native shell (APNs) and web push
in browsers. Everything is per-toggle in **You → notifications**
(`profile-couple.png`), grouped roughly as:

- **Trips:** next-trip date set, trip countdown, reunion moments, trip
  imported from the planner, flight updates.
- **Memories:** partner added a memory, on-this-day lookbacks.
- **Shared lists:** dream destination added, bucket-list idea added, list
  updated, song set.
- **Health (Plus):** sleep recap, evening steps recap.
- **Rituals and games (mostly Plus):** daily postcard, quiz nudges and
  results, date-night roulette, food roulette, dream pin, same sky, local
  tourist quest, card decks, daily question, letters, wind-down, virtual
  dinner, pokes, mood shares, presence.

The trigger model is peer-to-peer: your partner's action fires your
notification (a memory saved, a poke sent, a quest completed). Scheduled
ones (daily postcard, daily question, recaps) fire on their own clock.

### The widgets (iOS, Plus-gated)

Four home-screen widgets ship in the app binary:

1. **Countdown** - the next trip, days to go.
2. **Send a Feeling** - one-tap ping to your partner from the home screen.
3. **Share Mood** - same mechanic, moods.
4. **Two Clocks** - both partners' local times (built for apart-couples).

Setup is the standard iOS flow: long-press the home screen → add widget →
Next Visit. The app feeds them through an App Group; opening the app while
on Plus is what arms them. On a free space the shared context is
deliberately wiped, so the widgets render their set-up placeholder rather
than data - the gate is enforced, not cosmetic.

---

## 7 · The data model in plain English

Seven things, one relationship diagram in prose:

- A **space** is the container everything else belongs to. It is a couple
  (two named partner slots, one of which may be empty) or a crew (a member
  list of names). The space owns the invite code, the anniversary, the
  chosen song, the tier (free/Plus), and counters like how many photos it
  holds.
- A **profile** is one person: first name, photo, notification toggles, and
  a pointer to the space they are currently viewing. Accounts are
  anonymous-first; an email can be linked later purely for recovery. One
  person can belong to several spaces (a couple and two crews, say) and
  switch between them; one space is their primary.
- A **visit** is a trip - past or future. Future visits are countdowns;
  past ones are memories. A visit belongs to a space and carries dates,
  destination, a hero photo, the story, an attached song, and - for
  planner-built trips - the full multi-stop route exactly as the planner
  produced it, including every booking link. Crews additionally track
  who-has-booked-what per visit.
- A **photo** (or video) belongs to a visit and a space, with the taken
  date used to place it on the right stop of a route.
- **Lists** - the bucket list and dream destinations - are per-space lists
  of ideas; dream destinations carry a city/country and feed the passport
  and dream-pin features.
- **Together data** - streaks, steps, sleep, games state, surprise trips,
  letters - is a family of per-space, per-feature records that only Plus
  spaces write.
- **Events** - the anonymous analytics trail (created/shared/joined/opened,
  and daily app-opens), per space and user id, readable only by the admin
  reporting job. No names, no content.

Deletion is cascade-by-space: deleting a space takes its visits, photos,
lists and Together data with it.

---

## 8 · What is genuinely good (so marketing sells the right thing)

- **Zero-friction entry is real.** Four taps from cold start to a working
  space, no account ever. For the invited person it holds on Android and
  desktop (full browser join, nothing installed); on an iPhone without the
  app, the link deliberately routes through the App Store first (section 2).
- **The planner is a legitimate standalone hook** - it produces something
  useful for a stranger in ~30 seconds and now hands off cleanly to both
  the web and native app.
- **The crew mechanics are stronger than the marketing implies:** name
  reclaim on rejoin, additive joins, per-trip booking coordination.
- **The Plus gate is honest** - every listed perk is actually enforced in
  code, and the caps are real. Nothing on the paywall is fake.

## 9 · Known gaps and half-built things, bluntly

1. **The paywall is nearly invisible.** Free couples never see the Together
   doorway; `/Together` silently bounces them to /Us instead of showing a
   locked preview. The only organic paths to the A$3.99 sheet are a Profile
   card and the storage caps - and on a young space nobody hits a 150-photo
   cap. If Plus conversion matters, the product currently barely asks.
2. **Analytics were dark until 3 Aug.** The events security rule existed in
   the repo but was never deployed, so every write silently bounced. Zero
   historical funnel data exists before today; the invite-funnel numbers
   start now. (Deployed and verified end-to-end today.)
3. **Nothing chases an unfilled invite.** The unpaired state is passive
   cards only - no reminder, no push, no "your space is waiting" email
   (there are no emails at all). Given the whole product thesis is the
   second person, the silence after a skipped invite is the biggest hole in
   the funnel. (Being fixed in the release branch: two pushes, the morning
   after the space is made and again five days in, landing on the invite
   card ready to resend, then silence. Two is the whole budget.)
4. **The iOS invite link converts installs, not joins - watch that step.**
   An iPhone invitee without the app cannot join in the browser; they get
   the App Store interstitial (deliberate, to keep the pairing in one
   account - section 2). So the couple-side funnel crosses the App Store:
   invite → interstitial → install → reopen the link or paste the code →
   join. Every step now emits an event, but the wall is real. And the
   interstitial's crew wording depends on a background peek winning a
   race, so crew invitees are regularly greeted as couples. If joins lag
   invites in the funnel report, this page is the first suspect. (Both are
   fixed in the release branch - see section 2.)
5. **The funnel's "links opened" step was only counting existing users.**
   The event fired on one screen that a brand-new invitee never reaches,
   because anyone without a profile is routed straight into onboarding. So
   the denominator under the join rate - the number the positioning
   question rests on - has been missing its main case since it shipped.
   Fixed in the release branch, but it means opened-versus-joined rates
   from before that fix cannot be compared with the ones after it.
6. **The rating ask never fired in practice** - it sat behind a 30-day
   gate in a category where ~96% of installs are gone by day 30, which is
   why the store shows two ratings. The success-moment rework is in the
   current release branch, not yet shipped.
7. **Crews are half a product.** They get Home, Plan, Memories, bookings -
   good - but no crew equivalent of Us, and the entire paid tier is
   couple-shaped (a comped crew landing on /Together meets partner duels
   and couple passports). Crew Plus effectively sells storage only.
8. **Recovery is fragile by design.** Anonymous-first with optional email
   means a solo user (or crew creator) who never links an email and loses
   the phone loses the space. The recovery paths that exist all assume a
   partner who still has access.
9. **Android does not exist.** The Play listing is "coming soon" on the
   site; there is scaffolding in the repo but no shipped build. Every
   invited Android partner ends at the web app - which works, but the
   asymmetry is invisible in the marketing.
10. **Quiz results, postcards and several Us modules read as couple-only**
   even on crew spaces where they are hidden - fine - but the Us page on an
   unpaired couple is close to empty and does nothing to say why. It could
   sell the pairing moment; today it just looks unfinished.
11. **No yearly price is live** despite the billing scaffold supporting it -
    monthly A$3.99 is the only SKU. At this price point a yearly SKU is
    usually the majority of subscription revenue.
12. **The screenshot set itself has three gaps:** no capture of the
    unpaired-couple Home (the persistent invite card), none of the couple
    onboarding share step (both need a throwaway space per capture run),
    and none of the A$3.99 purchase sheet. The Together frame in the set
    photographs the silent free-tier redirect to /Us (finding 1), not a
    paywall. Where the pixels are missing, sections 1-2 and 4 describe
    from code instead.

---

*Maintained by the capture and analytics pipeline owner. The screenshot set
is regenerated by the couples-repo capture workflow; this document is
hand-maintained - correct it when the product moves.*
