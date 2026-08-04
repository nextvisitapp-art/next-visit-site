# Footage library

Every video in the Drive `Footage` folder, subfolders included: **84 clips**,
each with a contact sheet and a transcode. 18.3 MB of sheets,
757.7 MB of video.

**This branch mirrors Drive automatically.** Add a clip to the Drive folder and
it appears here on the next run, usually within a couple of hours, without
anyone triggering anything. Nothing is hand-maintained, so do not hand-edit this file: it is
regenerated from `manifest.json` on every sync and an edit would be silently
overwritten. The one thing that is not derived from Drive is the Faces column,
which is stored separately - see below.

## Taking only what you need

The branch is a couple of hundred MB. Do not clone it whole:

```sh
git clone --filter=blob:none --sparse --branch footage \
  https://github.com/nextvisitapp-art/next-visit-site.git footage && cd footage
git sparse-checkout set index          # sheets + INDEX.md, a few MB
git sparse-checkout add clips/IMG_9402.mp4 clips/trip-trip-13.mp4
```

`--filter=blob:none` means no file contents are fetched until something asks
for them, so the size of the branch costs you nothing until you name a clip.

## What you get

- `index/<base>.jpg` - contact sheet, 3x2, sampled at 5, 25, 45, 65, 85 and 97
  percent of the clip so camera movement shows rather than one frame that
  flatters a shot that pans away. 360px tiles, source timecode burned in.
- `clips/<base>.mp4` - h264, crf 18, preset medium, yuv420p, no audio, native
  aspect ratio, longest side capped at 1920, and **not cropped to 9:16**.
  The crop window is yours per shot.
- `manifest.json` - machine-readable state, including each clip's Drive id and
  checksum. This is what makes the sync incremental.

Orientation is corrected on disk and the container carries no rotation flag, so
the file is upright everywhere without `-noautorotate`. **Native** below is the
resolution after rotation, which is the one anybody actually sees.

## This branch is public

`next-visit-site` is a public repo. The orphan branch keeps the mirror out of
`main`; it does **not** make any of it private. Anything here is published
permanently - deleting later does not unpublish while a commit referencing the
blob survives. That applies automatically to anything dropped in the Drive
folder from now on, which is the cost of the mirror being unattended.

## Do not use

- **`IMG_0048`** - Not a face problem: a political advertisement plays across the departure board for the clip's duration.
- **`IMG_0059`** - Identifiable front-on face.
- **`IMG_0063`** - Identifiable front-on face.

**This is not a subset of the FACE rows.** A clip can be unusable for reasons
that have nothing to do with faces, so check this list as well as the column.

> ### Faces
>
> `cleared` and `**FACE**` are the hub's verdicts, 29 of 84 so far.
> **`unreviewed` means nobody has looked** - it does not mean the clip is clear,
> and an unreviewed row must never be read as cleared. New clips arrive
> unreviewed by definition.
>
> Flag a clip where a face is **identifiable and front-on**. People walking away
> from camera are fine and are not flagged.
>
> **Judge a borderline frame at full resolution, not off the sheet.** At tile
> size these sheets have read the back of a head as a face, and a man looking
> straight into the lens as an ambiguous profile - both on the same batch, in
> opposite directions.
>
> Verdicts live in `marketing/_render/footage-review.json` in the couples repo,
> not in this file, precisely so a regeneration cannot wipe them.

## Clips

| Clip | Duration | Native | Orientation | Faces | Files |
| --- | ---: | --- | --- | --- | --- |
| `3AC736FF-1E7C-45BE-A164-A05517C9D6F7` | 19.43s | 1920x1920 | square | unreviewed | [sheet](index/3AC736FF-1E7C-45BE-A164-A05517C9D6F7.jpg) &middot; [clip](clips/3AC736FF-1E7C-45BE-A164-A05517C9D6F7.mp4) |
| `att.tjCE2F1uk9V4LBx3xgw5KlkYa8SdpSPJzJqEbLx-UB8` | 6.07s | 720x1280 | portrait | unreviewed | [sheet](index/att.tjCE2F1uk9V4LBx3xgw5KlkYa8SdpSPJzJqEbLx-UB8.jpg) &middot; [clip](clips/att.tjCE2F1uk9V4LBx3xgw5KlkYa8SdpSPJzJqEbLx-UB8.mp4) |
| `IMG_0044` | 2.80s | 1080x1920 | portrait | cleared | [sheet](index/IMG_0044.jpg) &middot; [clip](clips/IMG_0044.mp4) |
| `IMG_0045` | 2.53s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_0045.jpg) &middot; [clip](clips/IMG_0045.mp4) |
| `IMG_0046` | 3.50s | 1080x1920 | portrait | cleared | [sheet](index/IMG_0046.jpg) &middot; [clip](clips/IMG_0046.mp4) |
| `IMG_0047` | 2.20s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_0047.jpg) &middot; [clip](clips/IMG_0047.mp4) |
| `IMG_0048` | 4.57s | 1080x1920 | portrait | cleared | [sheet](index/IMG_0048.jpg) &middot; [clip](clips/IMG_0048.mp4) &middot; do not use |
| `IMG_0050` | 3.77s | 1080x1920 | portrait | cleared | [sheet](index/IMG_0050.jpg) &middot; [clip](clips/IMG_0050.mp4) |
| `IMG_0051` | 6.63s | 1920x1080 | landscape | cleared | [sheet](index/IMG_0051.jpg) &middot; [clip](clips/IMG_0051.mp4) |
| `IMG_0052` | 4.13s | 1080x1920 | portrait | cleared | [sheet](index/IMG_0052.jpg) &middot; [clip](clips/IMG_0052.mp4) |
| `IMG_0054` | 4.13s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_0054.jpg) &middot; [clip](clips/IMG_0054.mp4) |
| `IMG_0055` | 4.63s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_0055.jpg) &middot; [clip](clips/IMG_0055.mp4) |
| `IMG_0056` | 8.03s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_0056.jpg) &middot; [clip](clips/IMG_0056.mp4) |
| `IMG_0057` | 2.83s | 1080x1920 | portrait | cleared | [sheet](index/IMG_0057.jpg) &middot; [clip](clips/IMG_0057.mp4) |
| `IMG_0058` | 2.43s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_0058.jpg) &middot; [clip](clips/IMG_0058.mp4) |
| `IMG_0059` | 2.43s | 1080x1920 | portrait | **FACE** | [sheet](index/IMG_0059.jpg) &middot; [clip](clips/IMG_0059.mp4) &middot; do not use |
| `IMG_0061` | 13.52s | 1080x1920 | portrait | cleared | [sheet](index/IMG_0061.jpg) &middot; [clip](clips/IMG_0061.mp4) |
| `IMG_0062` | 12.97s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_0062.jpg) &middot; [clip](clips/IMG_0062.mp4) |
| `IMG_0063` | 48.33s | 1080x1920 | portrait | **FACE** | [sheet](index/IMG_0063.jpg) &middot; [clip](clips/IMG_0063.mp4) &middot; do not use |
| `IMG_0064` | 3.30s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_0064.jpg) &middot; [clip](clips/IMG_0064.mp4) |
| `IMG_0066` | 3.10s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_0066.jpg) &middot; [clip](clips/IMG_0066.mp4) |
| `IMG_0067` | 12.94s | 1080x1920 | portrait | cleared | [sheet](index/IMG_0067.jpg) &middot; [clip](clips/IMG_0067.mp4) |
| `IMG_1705` | 7.81s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1705.jpg) &middot; [clip](clips/IMG_1705.mp4) |
| `IMG_1708` | 6.97s | 1080x1920 | portrait | cleared | [sheet](index/IMG_1708.jpg) &middot; [clip](clips/IMG_1708.mp4) |
| `IMG_1709` | 16.21s | 1080x1920 | portrait | cleared | [sheet](index/IMG_1709.jpg) &middot; [clip](clips/IMG_1709.mp4) |
| `IMG_1717` | 3.64s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1717.jpg) &middot; [clip](clips/IMG_1717.mp4) |
| `IMG_1718` | 2.83s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1718.jpg) &middot; [clip](clips/IMG_1718.mp4) |
| `IMG_1719` | 3.33s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1719.jpg) &middot; [clip](clips/IMG_1719.mp4) |
| `IMG_1720` | 4.73s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1720.jpg) &middot; [clip](clips/IMG_1720.mp4) |
| `IMG_1721` | 5.03s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1721.jpg) &middot; [clip](clips/IMG_1721.mp4) |
| `IMG_1722` | 2.87s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1722.jpg) &middot; [clip](clips/IMG_1722.mp4) |
| `IMG_1724` | 2.07s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1724.jpg) &middot; [clip](clips/IMG_1724.mp4) |
| `IMG_1724-2` | 2.07s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1724-2.jpg) &middot; [clip](clips/IMG_1724-2.mp4) |
| `IMG_1725` | 3.77s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1725.jpg) &middot; [clip](clips/IMG_1725.mp4) |
| `IMG_1726` | 4.90s | 1080x1920 | portrait | cleared | [sheet](index/IMG_1726.jpg) &middot; [clip](clips/IMG_1726.mp4) |
| `IMG_1727` | 4.74s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1727.jpg) &middot; [clip](clips/IMG_1727.mp4) |
| `IMG_1727-2` | 4.74s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1727-2.jpg) &middot; [clip](clips/IMG_1727-2.mp4) |
| `IMG_1728` | 3.63s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1728.jpg) &middot; [clip](clips/IMG_1728.mp4) |
| `IMG_1728-2` | 3.63s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1728-2.jpg) &middot; [clip](clips/IMG_1728-2.mp4) |
| `IMG_1730` | 5.90s | 1080x1920 | portrait | cleared | [sheet](index/IMG_1730.jpg) &middot; [clip](clips/IMG_1730.mp4) |
| `IMG_1804` | 10.91s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_1804.jpg) &middot; [clip](clips/IMG_1804.mp4) |
| `IMG_9402` | 5.87s | 1080x1920 | portrait | cleared | [sheet](index/IMG_9402.jpg) &middot; [clip](clips/IMG_9402.mp4) |
| `IMG_9540` | 1.13s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_9540.jpg) &middot; [clip](clips/IMG_9540.mp4) |
| `IMG_9541` | 0.80s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_9541.jpg) &middot; [clip](clips/IMG_9541.mp4) |
| `IMG_9542` | 2.27s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_9542.jpg) &middot; [clip](clips/IMG_9542.mp4) |
| `IMG_9544` | 1.60s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_9544.jpg) &middot; [clip](clips/IMG_9544.mp4) |
| `IMG_9547` | 2.67s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_9547.jpg) &middot; [clip](clips/IMG_9547.mp4) |
| `IMG_9548` | 1.63s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_9548.jpg) &middot; [clip](clips/IMG_9548.mp4) |
| `IMG_9550` | 3.80s | 1080x1920 | portrait | unreviewed | [sheet](index/IMG_9550.jpg) &middot; [clip](clips/IMG_9550.mp4) |
| `reel-fiji-longweekend` | 10.37s | 1080x1920 | portrait | unreviewed | [sheet](index/reel-fiji-longweekend.jpg) &middot; [clip](clips/reel-fiji-longweekend.mp4) |
| `reel-fiji-longweekend-proxy` | 10.37s | 540x960 | portrait | unreviewed | [sheet](index/reel-fiji-longweekend-proxy.jpg) &middot; [clip](clips/reel-fiji-longweekend-proxy.mp4) |
| `reel-kept-afteryouland` | 13.03s | 1080x1920 | portrait | unreviewed | [sheet](index/reel-kept-afteryouland.jpg) &middot; [clip](clips/reel-kept-afteryouland.mp4) |
| `reel-kept-afteryouland-PREVIEW-not-for-posting` | 13.03s | 1080x1920 | portrait | unreviewed | [sheet](index/reel-kept-afteryouland-PREVIEW-not-for-posting.jpg) &middot; [clip](clips/reel-kept-afteryouland-PREVIEW-not-for-posting.mp4) |
| `reel-memories-keepthetrip` | 14.67s | 1080x1920 | portrait | unreviewed | [sheet](index/reel-memories-keepthetrip.jpg) &middot; [clip](clips/reel-memories-keepthetrip.mp4) |
| `reel-planner-stopsaying` | 9.43s | 1080x1920 | portrait | unreviewed | [sheet](index/reel-planner-stopsaying.jpg) &middot; [clip](clips/reel-planner-stopsaying.mp4) |
| `reel-planner-stopsaying-PREVIEW-not-for-posting` | 9.43s | 1080x1920 | portrait | unreviewed | [sheet](index/reel-planner-stopsaying-PREVIEW-not-for-posting.jpg) &middot; [clip](clips/reel-planner-stopsaying-PREVIEW-not-for-posting.mp4) |
| `ScreenRecording_07-19-2026 11-28-13_1` | 4.16s | 1180x2388 | portrait | cleared | [sheet](index/ScreenRecording_07-19-2026%2011-28-13_1.jpg) &middot; [clip](clips/ScreenRecording_07-19-2026%2011-28-13_1.mp4) |
| `ScreenRecording_07-19-2026 11-39-45_1` | 11.62s | 1180x2394 | portrait | cleared | [sheet](index/ScreenRecording_07-19-2026%2011-39-45_1.jpg) &middot; [clip](clips/ScreenRecording_07-19-2026%2011-39-45_1.mp4) |
| `ScreenRecording_07-19-2026 11-41-06_1` | 16.04s | 1180x2414 | portrait | cleared | [sheet](index/ScreenRecording_07-19-2026%2011-41-06_1.jpg) &middot; [clip](clips/ScreenRecording_07-19-2026%2011-41-06_1.mp4) |
| `ScreenRecording_07-19-2026 11-48-19_1` | 10.77s | 1180x2386 | portrait | cleared | [sheet](index/ScreenRecording_07-19-2026%2011-48-19_1.jpg) &middot; [clip](clips/ScreenRecording_07-19-2026%2011-48-19_1.mp4) |
| `ScreenRecording_07-19-2026 11-50-16_1` | 13.05s | 1180x2390 | portrait | cleared | [sheet](index/ScreenRecording_07-19-2026%2011-50-16_1.jpg) &middot; [clip](clips/ScreenRecording_07-19-2026%2011-50-16_1.mp4) |
| `ScreenRecording_07-19-2026 12-12-56_1` | 10.55s | 1180x2398 | portrait | cleared | [sheet](index/ScreenRecording_07-19-2026%2012-12-56_1.jpg) &middot; [clip](clips/ScreenRecording_07-19-2026%2012-12-56_1.mp4) |
| `ScreenRecording_07-19-2026 12-15-16_1` | 2.85s | 1180x2376 | portrait | cleared | [sheet](index/ScreenRecording_07-19-2026%2012-15-16_1.jpg) &middot; [clip](clips/ScreenRecording_07-19-2026%2012-15-16_1.mp4) |
| `ScreenRecording_07-19-2026 12-16-47_1` | 1.55s | 1180x2016 | portrait | cleared | [sheet](index/ScreenRecording_07-19-2026%2012-16-47_1.jpg) &middot; [clip](clips/ScreenRecording_07-19-2026%2012-16-47_1.mp4) |
| `ScreenRecording_07-19-2026 12-18-48_1` | 1.81s | 1180x2002 | portrait | cleared | [sheet](index/ScreenRecording_07-19-2026%2012-18-48_1.jpg) &middot; [clip](clips/ScreenRecording_07-19-2026%2012-18-48_1.mp4) |
| `ScreenRecording_07-26-2026 22-12-48_1` | 4.72s | 1180x2392 | portrait | cleared | [sheet](index/ScreenRecording_07-26-2026%2022-12-48_1.jpg) &middot; [clip](clips/ScreenRecording_07-26-2026%2022-12-48_1.mp4) |
| `ScreenRecording_08-04-2026 09-46-44_1` | 34.07s | 886x1920 | portrait | cleared | [sheet](index/ScreenRecording_08-04-2026%2009-46-44_1.jpg) &middot; [clip](clips/ScreenRecording_08-04-2026%2009-46-44_1.mp4) |
| `trip-trip-01` | 15.37s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-01.jpg) &middot; [clip](clips/trip-trip-01.mp4) |
| `trip-trip-02` | 16.22s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-02.jpg) &middot; [clip](clips/trip-trip-02.mp4) |
| `trip-trip-03` | 9.33s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-03.jpg) &middot; [clip](clips/trip-trip-03.mp4) |
| `trip-trip-04` | 6.53s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-04.jpg) &middot; [clip](clips/trip-trip-04.mp4) |
| `trip-trip-05` | 9.33s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-05.jpg) &middot; [clip](clips/trip-trip-05.mp4) |
| `trip-trip-06` | 6.70s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-06.jpg) &middot; [clip](clips/trip-trip-06.mp4) |
| `trip-trip-07` | 9.33s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-07.jpg) &middot; [clip](clips/trip-trip-07.mp4) |
| `trip-trip-08` | 9.37s | 1080x1920 | portrait | cleared | [sheet](index/trip-trip-08.jpg) &middot; [clip](clips/trip-trip-08.mp4) |
| `trip-trip-09` | 8.83s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-09.jpg) &middot; [clip](clips/trip-trip-09.mp4) |
| `trip-trip-10` | 8.21s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-10.jpg) &middot; [clip](clips/trip-trip-10.mp4) |
| `trip-trip-11` | 7.47s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-11.jpg) &middot; [clip](clips/trip-trip-11.mp4) |
| `trip-trip-12` | 8.10s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-12.jpg) &middot; [clip](clips/trip-trip-12.mp4) |
| `trip-trip-13` | 20.63s | 1080x1920 | portrait | cleared | [sheet](index/trip-trip-13.jpg) &middot; [clip](clips/trip-trip-13.mp4) |
| `trip-trip-14` | 9.22s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-14.jpg) &middot; [clip](clips/trip-trip-14.mp4) |
| `trip-trip-15` | 7.53s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-15.jpg) &middot; [clip](clips/trip-trip-15.mp4) |
| `trip-trip-16` | 6.97s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-trip-16.jpg) &middot; [clip](clips/trip-trip-16.mp4) |
| `trip-unsorted-01` | 8.10s | 1080x1920 | portrait | unreviewed | [sheet](index/trip-unsorted-01.jpg) &middot; [clip](clips/trip-unsorted-01.mp4) |

## Renamed for collisions

Drive lets two files share a name and this library has several such pairs. At
least one - `IMG_1724` - is **two different takes rather than copies**, so
overwriting would silently drop footage. The first occurrence keeps the plain
basename and the rest take a numeric suffix. Numbering is assigned across the
whole library in a fixed order on every run, so a name never depends on which
files happened to be new.

| Mirrored as | Source | Folder |
| --- | --- | --- |
| `IMG_1724-2` | `IMG_1724.MOV` | root |
| `IMG_1727-2` | `IMG_1727.MOV` | root |
| `IMG_1728-2` | `IMG_1728.MOV` | root |
