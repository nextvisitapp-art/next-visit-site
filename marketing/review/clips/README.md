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
| `IMG_1705.mp4` | Brisbane at dusk, city lights on the river | 6.00s |
| `IMG_1725.mp4` | River, open water, city across the far bank | 3.77s |
| `IMG_1727.mp4` | City skyline from the bridge | 4.73s |
| `IMG_1728.mp4` | Two people walking away with suitcases | 3.63s |
| `IMG_1724.mp4` | Walking under trees, from behind | 2.06s |
| `IMG_0054.mp4` | Travelator, suitcase, from behind | 4.13s |
| `IMG_9541.mp4` | Qantas terminal exterior | 0.80s |
| `IMG_9547.mp4` | Qantas tail on the tarmac | 2.66s |
| `IMG_9548.mp4` | Plane and boarding stairs on the tarmac | 1.63s |
| `trip-trip-10.mp4` | Golf at sunset with cattle | 6.00s |

Only `trip-trip-10` and `IMG_1705` hit the six second cap. Everything else was
already shorter, and `IMG_9541` at 0.80s is short enough to be hard to use.

Trims are taken from the **centre** of the source: the head of a handheld clip
is usually the camera settling and the tail is it being lowered.

## This folder is public

`next-visit-site` is a public repo and git history is permanent. A clip
committed here is published for good - deleting it later does not unpublish it,
because the blob stays reachable by commit SHA. Vercel also serves this repo, so
these files are fetchable from the live domain as well.

So the rule is **no identifiable faces**, and it is enforced on the pixels, not
on a label. Every trim gets a 12-frame face sheet and is checked frame by frame
before it lands here. The clips mode deliberately cannot publish: it writes to a
private outbox in the couples repo, outside the token branch that delivers
sheets, so no configuration turns it into an automatic route here.

**Judge a borderline frame at full resolution, not off the sheet.** The sheet
was originally tiled at 270px wide, an eighth of the 1080px master, and at that
size it got two calls wrong in opposite directions on the same batch: it made
`IMG_1724` look like a face turned to camera when it is the back of a head, and
it made `IMG_9550` look like an ambiguous profile when the man is looking
straight back at the lens with his features fully resolvable. Tiles are now
405px, but the rule stands - anything close, pull the frame out of the mp4 and
look at it properly before deciding.

### Checked and excluded

- **`IMG_1720`** (coffee van, 1 Aug 2026) - two staff on camera with faces
  clearly identifiable from 0.0s to about 2.4s, and the business name fully
  legible.
- **`IMG_1722`** (farmers market, 1 Aug 2026) - the foreground is only a hand
  and produce, but a row of shoppers runs across the top of every single frame
  and several are front-on and identifiable.
- **`IMG_9550`** (boarding stairs, 2 Aug 2026) - briefed as backs of heads, and
  it mostly is, but a man in glasses is turned back toward the camera with his
  face fully resolvable through most of the trim. Only visible at full
  resolution; the sheet made it look like a profile.

All three were on the requested list. The index sheet showed one frame each and
none of those frames gave them away, which is the whole reason the check looks
at the trim rather than a thumbnail.

`IMG_1724`, `IMG_1727` and `IMG_1728` each match **two different Drive files** -
a name is not an id in that folder. Every take is trimmed and checked. The
`IMG_1727` and `IMG_1728` pairs turned out to be frame-for-frame identical, so
the larger file was kept and the alternate discarded. The **`IMG_1724` pair are
genuinely different takes**, so the alternate is not a duplicate - it is simply
unchecked and unpublished, and would need its own face check before use.

## Where the Fiji footage is

There is none in the Drive Footage root. Every frame of Fiji lives inside the
finished edit and nowhere else, which is why none of it appears above. See
`../footage-index.jpg` and HANDOFF entry 28.
