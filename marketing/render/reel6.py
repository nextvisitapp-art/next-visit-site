#!/usr/bin/env python3
"""Video 04: the trip you get to keep. One product truth: memories. The only
pillar that lives after the trip rather than before it. Two app beats back to
back because the feature needs showing, not describing."""
import asyncio, base64, pathlib, shutil, subprocess
from playwright.async_api import async_playwright

ROOT = pathlib.Path("/home/claude/nv")
FONTS = ROOT / "fonts/node_modules/@fontsource"
IMG = ROOT / "img"
CLIPS = ROOT / "clips2"
BUILD = ROOT / "build6v"
OUT = BUILD / "out"
if BUILD.exists():
    shutil.rmtree(BUILD)
OUT.mkdir(parents=True)

FPS = 24
XF = 0.30

# (clip, in-point, duration, push-direction). None = an app beat on navy.
BEATS = [
    ("trip-trip-13", 5.00, 2.50,  1),   # the trip at full volume
    ("IMG_1709",     8.60, 2.20, -1),   # the room, empty and quiet
    (None,           0.00, 2.90,  0),   # app: the map of every trip
    (None,           0.00, 3.00,  0),   # app: the song attached to one
    ("trip-trip-08", 2.20, 2.20,  1),   # rainforest
    ("IMG_1730",     2.20, 3.20,  1),   # the bridge and the river, end card
]
DUR = sum(b[2] for b in BEATS)
NF = int(round(DUR * FPS))

starts, counts = [], []
acc = 0
for _, _, dur, _ in BEATS:
    starts.append(acc)
    counts.append(int(round(dur * FPS)))
    acc += counts[-1]
XFN = int(round(XF * FPS))

for bi, (clip, tin, dur, _) in enumerate(BEATS):
    d = BUILD / f"b{bi}"
    d.mkdir(parents=True, exist_ok=True)
    if clip is None:
        continue
    n = counts[bi] + XFN + 2
    # -noautorotate: the mirror baked rotation into the pixels but left a
    # spurious rotation=-90 flag in the container.
    subprocess.run([
        "ffmpeg", "-v", "error", "-noautorotate",
        "-ss", str(max(0, tin - XF)), "-i", str(CLIPS / f"{clip}.mp4"),
        "-frames:v", str(n), "-vf",
        f"fps={FPS},scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
        str(d / "f%04d.jpg"), "-q:v", "2", "-y"
    ], check=True)
print("beats extracted, total frames", NF, "dur", round(DUR, 2))

b64 = lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
face = lambda f, p, w, st="normal": (
    f"@font-face{{font-family:'{f}';font-style:{st};font-weight:{w};"
    f"src:url(data:font/woff2;base64,{b64(p)}) format('woff2');}}")
FONT_CSS = "".join([
    face("Fraunces", FONTS/"fraunces/files/fraunces-latin-600-normal.woff2", 600),
    face("Fraunces", FONTS/"fraunces/files/fraunces-latin-600-italic.woff2", 600, "italic"),
    face("DM Mono", FONTS/"dm-mono/files/dm-mono-latin-500-normal.woff2", 500),
    face("Space Grotesk", FONTS/"space-grotesk/files/space-grotesk-latin-700-normal.woff2", 700),
])
CARD_MAP = f"data:image/jpeg;base64,{b64(IMG/'card-map.jpg')}"
CARD_SONG = f"data:image/jpeg;base64,{b64(IMG/'card-song.jpg')}"
CARD_PHOTOS = f"data:image/jpeg;base64,{b64(IMG/'card-photos.jpg')}"
WORDMARK = "".join(f'<span class="flap"><i>{c}</i><u></u><b></b><s></s></span>'
                   for c in "NEXTVISIT")

B = [s / FPS for s in starts]
APP_IN = B[2]
APP_MID = B[3]
APP_OUT = (starts[3] + counts[3]) / FPS

HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>
{FONT_CSS}
:root{{--navy:#0e2240;--cream:#fbe8de;--cream3:#eccab4;--pink:#ec4079;--tile:#06122a}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#05111f}}
.bgw{{position:absolute;inset:0;overflow:hidden}}
.bgw img{{position:absolute;left:50%;top:50%;width:1080px;height:1920px;object-fit:cover;
 transform:translate(-50%,-50%) scale(1);
 filter:saturate(1.10) contrast(1.05) brightness(1.02)}}
#tint{{position:absolute;inset:0;background:#0e2240;opacity:.10;mix-blend-mode:soft-light}}
#vig{{position:absolute;inset:0;pointer-events:none;
 background:radial-gradient(120% 78% at 50% 46%, transparent 52%, rgba(4,12,26,.42) 100%)}}
#navy{{position:absolute;inset:0;opacity:0;background:
 radial-gradient(120% 70% at 50% -10%,#17335c 0,transparent 60%),
 radial-gradient(90% 50% at 100% 105%,#0b1c36 0,transparent 65%),var(--navy)}}
#scrim{{position:absolute;left:0;right:0;top:0;height:920px;opacity:0;
 background:linear-gradient(180deg,rgba(5,17,31,.76) 0%,rgba(5,17,31,.46) 55%,rgba(5,17,31,0) 100%)}}
#scrimb{{position:absolute;left:0;right:0;bottom:0;height:860px;opacity:0;
 background:linear-gradient(0deg,rgba(5,17,31,.80) 0%,rgba(5,17,31,.42) 60%,rgba(5,17,31,0) 100%)}}
.plate{{position:absolute;left:96px;right:96px;top:300px;opacity:0}}
.eyebrow{{font-family:'DM Mono',monospace;font-weight:500;font-size:26px;letter-spacing:.24em;
 text-transform:uppercase;color:var(--cream3);opacity:.75;margin-bottom:30px}}
h1{{font-family:'Fraunces',serif;font-weight:600;color:var(--cream);
 font-size:104px;line-height:1.08;letter-spacing:-.015em;
 text-shadow:0 2px 34px rgba(4,12,26,.55)}}
h1 em{{font-style:italic;color:var(--pink)}}
h1.sm{{font-size:88px}}
.card{{position:absolute;left:50%;opacity:0;
 transform:translateX(-50%) scale(1);border-radius:24px;overflow:hidden;
 box-shadow:0 46px 110px rgba(3,10,22,.8),0 0 0 1px rgba(251,232,222,.10)}}
.card img{{display:block;width:100%}}
#cardMap{{top:760px;width:912px}}
#cardSong{{top:700px;width:900px}}
#cardPhotos{{top:1188px;width:900px}}
#end{{position:absolute;left:0;right:0;bottom:225px;text-align:center;opacity:0}}
.mark{{display:inline-flex;gap:7px}}
.flap{{position:relative;width:78px;height:105px;background:var(--tile);
 border-radius:5.5px;overflow:hidden;flex-shrink:0;
 box-shadow:inset 0 0 0 1px rgba(251,232,222,.07),0 1px 0 rgba(0,0,0,.45)}}
.flap i{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
 font-family:'Space Grotesk',sans-serif;font-weight:700;font-style:normal;
 font-size:69px;line-height:1;letter-spacing:-.01em;color:var(--cream)}}
.flap u{{position:absolute;left:0;right:0;top:50%;height:1px;background:rgba(0,0,0,.6)}}
.flap b{{position:absolute;left:0;right:0;top:0;height:50%;
 background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,0))}}
.flap s{{position:absolute;left:0;right:0;top:50%;bottom:0;
 background:linear-gradient(180deg,rgba(0,0,0,.05),rgba(0,0,0,.20))}}
.url{{font-family:'DM Mono',monospace;font-weight:500;font-size:31px;letter-spacing:.14em;
 text-transform:uppercase;color:var(--cream);opacity:.66;margin-top:34px}}
.appicon{{width:132px;height:132px;border-radius:29.53px;overflow:hidden;display:flex;
 margin:0 auto 34px;box-shadow:0 5px 16px rgba(0,0,0,.35),inset 0 0 0 1px rgba(251,232,222,.05)}}
.half{{position:relative;width:66px;height:132px;background:var(--tile);overflow:hidden}}
.half i{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
 font-family:'Space Grotesk',sans-serif;font-weight:700;font-style:normal;
 font-size:81.84px;line-height:1;letter-spacing:-.01em}}
.half u{{position:absolute;left:0;right:0;top:50%;height:1px;background:rgba(0,0,0,.6)}}
.half b{{position:absolute;left:0;right:0;top:0;height:50%;
 background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,0))}}
.half s{{position:absolute;left:0;right:0;top:50%;bottom:0;
 background:linear-gradient(180deg,rgba(0,0,0,.05),rgba(0,0,0,.20))}}
.mark .flap{{width:62px;height:83px;border-radius:4.3px}}
.mark .flap i{{font-size:54.8px}}
</style></head><body>
<div class="bgw"><img id="bgA" src=""></div>
<div class="bgw" id="wrapB" style="opacity:0"><img id="bgB" src=""></div>
<div id="tint"></div>
<div id="navy"></div>
<div id="vig"></div>
<div id="scrim"></div><div id="scrimb"></div>

<div class="plate" id="p1"><h1>You think you'll<br><em>remember it.</em></h1></div>

<div class="plate" id="p2"><h1 class="sm">You remember<br>about <em>four things.</em></h1></div>

<div class="plate" id="p3" style="top:296px"><div class="eyebrow">Our story so far</div>
  <h1 class="sm">Every trip,<br><em>pinned.</em></h1></div>
<div class="card" id="cardMap"><img src="{CARD_MAP}"></div>

<div class="plate" id="p4" style="top:296px"><div class="eyebrow">And attached to each one</div>
  <h1 class="sm">The song that<br><em>was playing.</em></h1></div>
<div class="card" id="cardSong"><img src="{CARD_SONG}"></div>
<div class="card" id="cardPhotos"><img src="{CARD_PHOTOS}"></div>

<div class="plate" id="p5"><h1 class="sm">Start it <em>before</em><br>you go.</h1></div>

<div id="end">
  <div class="appicon">
    <div class="half"><i style="color:var(--cream);transform:translateX(9.24px)">N</i><u></u><b></b><s></s></div>
    <div class="half"><i style="color:var(--pink);transform:translateX(-9.24px)">V</i><u></u><b></b><s></s></div>
  </div>
  <div class="mark">{WORDMARK}</div>
  <div class="url">Free on the App Store</div></div>

<script>
const E=i=>document.getElementById(i);
const cl=(a,b,t)=>Math.max(0,Math.min(1,(t-a)/(b-a)));
const ease=x=>1-Math.pow(1-x,3);
const ss=x=>x*x*(3-2*x);
const band=(t,a,b,f=0.4)=>Math.min(ss(cl(a,a+f,t)),1-ss(cl(b-f,b,t)));
const B=[{B[0]:.4f},{B[1]:.4f},{B[2]:.4f},{B[3]:.4f},{B[4]:.4f},{B[5]:.4f}];
const APP_IN={APP_IN:.4f}, APP_MID={APP_MID:.4f}, APP_OUT={APP_OUT:.4f};
function plate(id,t,a,b,f){{
  const o=band(t,a,b,f);
  const el=E(id);
  el.style.opacity=o;
  el.style.transform='translateY('+(24*(1-ease(cl(a,a+0.60,t)))).toFixed(1)+'px)';
  return o;
}}
window.setT=function(t){{
  // one continuous navy block across both app beats, the cards cross-dissolve
  // inside it. Cutting back to footage between them would make the feature
  // read as two things instead of one.
  const app=band(t,APP_IN,APP_OUT,0.32);
  E('navy').style.opacity=app;

  const cm=band(t,APP_IN+0.10,APP_MID+0.16,0.30);
  E('cardMap').style.opacity=cm;
  E('cardMap').style.transform='translateX(-50%) scale('+(1+0.035*cl(APP_IN,APP_MID,t)).toFixed(4)+')';
  const cs=band(t,APP_MID+0.06,APP_OUT-0.02,0.30);
  E('cardSong').style.opacity=cs;
  E('cardPhotos').style.opacity=band(t,APP_MID+0.42,APP_OUT-0.02,0.30);
  E('cardSong').style.transform='translateX(-50%) scale('+(1+0.03*cl(APP_MID,APP_OUT,t)).toFixed(4)+')';

  const o1=plate('p1',t,B[0]-0.35,B[1]-0.24,0.34);
  const o2=plate('p2',t,B[1]-0.14,APP_IN+0.26,0.30);
  const o3=plate('p3',t,APP_IN+0.24,APP_MID-0.06,0.30);
  const o4=plate('p4',t,APP_MID+0.20,APP_OUT+0.24,0.30);
  const o5=plate('p5',t,B[4]-0.14,B[5]+0.10,0.32);

  E('scrim').style.opacity=Math.max(o1,o2,o5*0.95)*0.94;

  const oe=ss(cl(B[5]+0.55,B[5]+1.45,t));
  E('end').style.opacity=oe;
  E('scrimb').style.opacity=Math.max(oe*0.92,o5*0.30);
}};
window.setBG=async function(a,b,mix,sa,sb){{
  const wait=[];
  const A=E('bgA'), Bg=E('bgB');
  if(a && A.getAttribute('src')!==a){{ A.src=a; wait.push(A.decode().catch(()=>{{}})); }}
  A.style.transform='translate(-50%,-50%) scale('+sa+')';
  E('wrapB').style.opacity=mix;
  if(b && Bg.getAttribute('src')!==b){{ Bg.src=b; wait.push(Bg.decode().catch(()=>{{}})); }}
  if(b) Bg.style.transform='translate(-50%,-50%) scale('+sb+')';
  await Promise.all(wait);
}};
</script></body></html>"""

(BUILD / "index.html").write_text(HTML)

STARTS, COUNTS = starts, counts


def ease_py(x):
    return x * x * (3 - 2 * x)


def beat_for(i):
    for bi in range(len(BEATS)):
        if STARTS[bi] <= i < STARTS[bi] + COUNTS[bi]:
            return bi
    return len(BEATS) - 1


AVAIL = {}


def src_for(bi, local):
    if BEATS[bi][0] is None:
        return None, 1.0
    if bi not in AVAIL:
        AVAIL[bi] = len(list((BUILD / f"b{bi}").glob("*.jpg")))
    n = local + XFN + 1
    if n > AVAIL[bi]:
        n = AVAIL[bi]
    if n < 1:
        n = 1
    push = BEATS[bi][3]
    p = local / max(1, COUNTS[bi] - 1)
    scale = 1.03 + 0.055 * (p if push > 0 else (1 - p))
    return f"b{bi}/f{n:04d}.jpg", round(scale, 4)


PRE = XFN + 6


async def main():
    async with async_playwright() as p:
        br = await p.chromium.launch()
        pg = await br.new_page(viewport={"width": 1080, "height": 1920},
                               device_scale_factor=1)
        await pg.goto(f"file://{BUILD}/index.html")
        await pg.wait_for_timeout(1400)
        for i in range(NF):
            t = i / FPS
            bi = beat_for(i)
            local = i - STARTS[bi]
            rem = COUNTS[bi] - local
            a, sa = src_for(bi, local)
            b, sb, mix = None, 1.0, 0.0

            if BEATS[bi][0] is None:
                # An app beat holds whatever frame was underneath. Before the
                # navy lifts, quietly move the base layer onto the next shot's
                # pre-roll so the footage is already running when it appears.
                if rem <= PRE and bi + 1 < len(BEATS) and BEATS[bi + 1][0] is not None:
                    a, sa = src_for(bi + 1, local - COUNTS[bi])
            elif rem <= XFN and bi + 1 < len(BEATS) and BEATS[bi + 1][0] is not None:
                b, sb = src_for(bi + 1, local - COUNTS[bi])
                mix = round(ease_py(1 - rem / XFN), 4)

            await pg.evaluate(
                "async ([a,b,m,sa,sb,t]) => { await window.setBG(a||'', b||'', m, sa, sb); window.setT(t); }",
                [a or "", b or "", mix, sa, sb, t])
            await pg.screenshot(path=str(OUT / f"f{i:04d}.png"))
            if i % 60 == 0:
                print("frame", i, "/", NF, flush=True)
        await br.close()
    print("done", NF, "frames", round(DUR, 2), "s")


asyncio.run(main())
