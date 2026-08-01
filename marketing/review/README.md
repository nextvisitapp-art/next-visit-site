# Review sheets

Contact sheets from the reel pipeline. Every rendered video gets one: 20 evenly
spaced frames from the finished cut, each labelled with its timecode, as a
single JPEG named to match the render. The footage index sheet lives here too.

| File | What it is |
| --- | --- |
| `reel-<name>.jpg` | The finished cut, 20 frames, timecoded. One per render. |
| `reel-<name>-still.jpg` | The 1080x1350 feed still that ships with that cut. |
| `footage-index.jpg` | One labelled frame per clip in the Drive Footage root. |
| `probe-contactsheet.jpg` | The raw source at 2 fps, before any cut is made. |

## Why this exists

The marketing hub can clone a repo but cannot pull binaries out of Drive, so a
video sitting in `Footage/Drafts` cannot be reviewed before it posts. The sheet
is the reviewable artefact. It lives here, in git, where anyone can read it.

That applies just as much to the footage index. Every raw clip in Drive is
called `IMG_1234.MOV`, so "the palm tree shot" cannot be picked by name - the
index sheet is the only way to name a clip by what is in it. A sheet in Drive
would be a sheet neither side of the handoff could look at.

The render sheet is also the only step in the pipeline that looks at **the
pixels that actually shipped**. Everything else - the EDL, the durations, the
plate timings - checks intent. That distinction is not theoretical: the first
Fiji cut opened on half a second of airport terminal because keyframe seeking
landed the in-point early, the assembled length was still exactly right, and no
duration or frame-count check caught it. The sheet did, immediately.

## How they get here

`marketing/_render/reel-cut.mjs` in the couples repo writes the sheets, and
`reel-cut.yml` uploads them as the run artefact `reel-<mode>`. Videos go to
Drive, sheets go to the artefact. Whoever ran the job pulls the artefact down
and commits the JPEGs here unchanged, keeping the filenames.

Sheets are **not** uploaded to Drive, on purpose. One destination, no drift, and
nothing lands somewhere it cannot be read.

## Reading one

Frames run left to right, four across, five down. The yellow timecode on each
frame is its position in the finished cut, not in the source footage.

Check, in this order:

1. **The first frame.** It is the entire first impression and the place a seek
   error shows up.
2. **Every shot boundary.** A frame containing the tail of the previous shot
   means an in-point crossed a scene change.
3. **The plates.** Legible, clear of any UI they sit over, and present for the
   frames they should be.
4. **The last frame.** The end mark should be on it, and nothing retired -
   there is an old white end card with a pink heart in some sources that must
   never appear.
