# B-roll clips

Trimmed b-roll for the marketing hub. 1080x1920, H.264, crf 20, muted, six
seconds maximum, original filename as the basename.

The hub reads git and cannot pull a binary out of Drive, so this is the only
route that actually delivers footage to it. Cut by `MODE=clips` in
`marketing/_render/reel-cut.mjs` in the couples repo, from
`marketing/_render/clips.manifest.json`.

## What is here

| File | Shot | Length |
| --- | --- | --- |
| `IMG_9402.mp4` | Sunset over the water, gold cloud, distant shoreline | 5.86s |
| `IMG_1725.mp4` | River, open water, city across the far bank | 3.77s |
| `IMG_1727.mp4` | City skyline from the bridge | 4.73s |
| `IMG_1728.mp4` | Two people walking away with suitcases | 3.63s |
| `IMG_0054.mp4` | Travelator, suitcase, from behind | 4.13s |
| `IMG_9541.mp4` | Qantas terminal exterior | 0.80s |
| `IMG_9548.mp4` | Plane and boarding stairs on the tarmac | 1.63s |
| `trip-trip-10.mp4` | Golf at sunset with cattle | 6.00s |

Only `trip-trip-10` hit the six second cap. Everything else was already
shorter, and `IMG_9541` at 0.80s is short enough to be hard to use.

Trims are taken from the **centre** of the source: the head of a handheld clip
is usually the camera settling and the tail is it being lowered.

## This folder is public

`next-visit-site` is a public repo and git history is permanent. A clip
committed here is published for good - deleting it later does not unpublish it,
because the blob stays reachable by commit SHA. Vercel also serves this repo, so
these files are fetchable from the live domain as well.

So the rule is **no identifiable faces**, and it is enforced on the pixels, not
on a label. Every trim gets a 12-frame face sheet at 2 fps and is checked frame
by frame before it lands here. The clips mode deliberately cannot publish: it
writes to a private outbox in the couples repo, outside the token branch that
delivers sheets, so no configuration turns it into an automatic route here.

### Checked and excluded, 1 Aug 2026

- **`IMG_1720`** (coffee van) - two staff on camera with faces clearly
  identifiable from 0.0s to about 2.4s, and the business name fully legible.
- **`IMG_1722`** (farmers market) - the foreground is only a hand and produce,
  but a row of shoppers runs across the top of every single frame and several
  are front-on and identifiable.

Both were on the requested list. The index sheet showed one frame each and
neither of those frames gave them away, which is the whole reason the check
looks at the trim rather than a thumbnail.

`IMG_1724`, `IMG_1727` and `IMG_1728` each match **two different Drive files** -
a name is not an id in that folder. Both takes were trimmed and checked; the
duplicates were frame-for-frame identical, so the larger file was kept and the
alternates were not published.

## Where the Fiji footage is

There is none in the Drive Footage root. Every frame of Fiji lives inside the
finished edit and nowhere else, which is why none of it appears above. See
`../footage-index.jpg` and HANDOFF entry 28.
