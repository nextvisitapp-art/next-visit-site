# Content system · the views problem

_29 Jul 2026, Claude Design. Written after reading `POSTED.md`, `REELS-SHOTLIST.md`, the live landing page, and the Drive folders. Companion to handoff entry `2026-07-29-design-7.md`._

## Where the funnel actually breaks

One reel has posted. Ever. It got 1,029 views, 0 saves, 0 shares, 0 comments, 0 follows.

Two finished reels have been sitting in `Drafts` since the 28th. `Approved` is empty.

So the bottleneck is not ideas, and not creative quality either - **we have not shipped enough to have a creative problem yet.** One post is not a test, it is an anecdote. The thing that is broken is throughput: work gets made, then waits.

That is the first thing to fix, and it costs nothing.

## Rule one: nothing sits in Drafts

A reel that is finished and unposted is worth exactly zero. The two in there should go out today and tomorrow, unedited. If a reel is good enough to preview it is good enough to post - the audience is 1,029 people who have never heard of us, not a client.

**Kill the `Approved` step.** It exists to prevent a bad post, and a bad post costs nothing at this size. What it actually prevents is posting.

## Rule two: three tiers, priced by what they cost Charlie

The shot list is excellent and it is also the problem - A1 to A22 and B1 to B20 all need Charlie's hands and Charlie's phone, so every piece of content is gated on the scarcest resource we have. Split the pipeline by cost instead:

**Tier 1 - camera-free. Costs Charlie nothing. This is mine.**
Stills, carousels, plates, before/after screens, quote cards, the share-card format. I compose them from app screenshots and the design system with no filming at all. This tier should be the majority of posts by volume, and today it is roughly none of them.

**Tier 2 - screen-only. Costs 15 minutes, no location, no lighting.**
A9 to A22 are all screen recordings. Every one can be filmed sitting on the couch. A reel cut from screen recordings plus a plate is a complete post - the planner filling in, a booking row flipping, a code being shared. No b-roll needed.

**Tier 3 - produced. Costs a weekend.**
B1 to B20, the Brisbane shoot, the trip footage. Genuinely good, genuinely expensive. One of these a fortnight is plenty, and it should never be the thing blocking a post.

Right now the calendar is built entirely out of tier 3. Invert it.

## Rule three: stop posting only into feeds

This is the strategic point, and it is the one I would argue hardest for.

IG Reels and TikTok are **discovery lotteries** - you post, an algorithm decides, and the content is dead in 48 hours. That is the whole distribution strategy at the moment, and 1,029 views is roughly what a lottery ticket pays.

But this product serves **search intent**. People type "group trip planner", "how to plan a trip with friends", "cheapest time to fly to Lisbon". That demand is constant and it is not in a feed.

Three surfaces where the content compounds instead of expiring:

- **Pinterest.** Travel planning is one of its largest categories, the format is a vertical still with text - exactly what I already produce for free - and a pin keeps earning views for months. This is the biggest single miss in the current plan. Zero filming required. My tier 1 output *is* Pinterest content.
- **TikTok and YouTube search.** Same clips, titled as answers rather than as moods. "How to plan a group trip without the group chat" outlives "POV: you just started the countdown" by a year.
- **Reddit, sparingly and honestly.** Threads where someone is asking how to organise a trip for six people. One useful comment, no pitch. Low volume, extremely high intent.

Feeds get you spikes. Search gets you a floor. We have no floor.

## Rule four: one post a week cannot teach us anything

Four attempts a month means the group-chat format's verdict arrives in September. Under the three tiers, five posts a week is realistic: three tier 1 stills or carousels, one tier 2 screen cut, one tier 3 reel a fortnight.

Judge everything on **saves per 100 views**, which `POSTED.md` already tracks. Kill any format that fails to beat the previous one twice running.

## How Code and I split this

The current loop works but it is slow, because everything routes through Charlie. Cleanest split:

**Mine:** concepts, hooks, plate copy, all tier 1 assets, the overlay and plate specs, and the calendar itself. I drop finished assets in Drive; Code commits them. I never need Charlie's phone.

**Code's:** the render pipeline (`countdown-overlay.cjs`), the shot list and `POSTED.md` as source of truth, committing what I drop, and - the important one - **the three activation events**. Views are the only number we have and they are the least useful one.

**Charlie's, and only Charlie's:** filming tier 2 and tier 3, and pressing post.

The gap worth closing: I write specs and Code renders them. Anything I can render myself, I should - stills, carousels, plates, share cards - so Code's queue is only the things that genuinely need code.

## First two weeks, concretely

**Week 1**
1. Post the two reels in `Drafts`. Today and tomorrow. No changes.
2. I produce six tier 1 assets: three Pinterest-format stills and one three-card carousel on the group-chat problem.
3. Charlie films A18 to A22 in one sitting, 15 minutes, couch.
4. Code instruments the three events.

**Week 2**
5. The group-chat reel goes out, cut from A18-A22 with the plates already specced.
6. Pinterest account opens; the six assets go up with search-intent titles.
7. Same clips reposted to TikTok and YouTube Shorts with question titles.
8. Read saves per 100 views across all of it. Then decide creative.

## What I need to be useful

- **The two drafts posted**, so the next decision is based on three data points instead of one.
- **The three events**, so we can stop optimising a funnel we cannot read.
- **Analytics recorded per post** in `POSTED.md`, including the zeroes.

Nothing here needs a landing page rebuild, and I have stopped that work.
