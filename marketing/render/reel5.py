#!/usr/bin/env python3
"""Video 03: the surprise trip. One product truth: you can plant a trip your
partner cannot see the destination of. Opens on footage and a line, never on a
UI screen, because the planner reel lost 84% of viewers in the first seconds."""
import asyncio, base64, pathlib, shutil, subprocess
from playwright.async_api import async_playwright

ROOT = pathlib.Path("/home/claude/nv")
FONTS = ROOT / "fonts/node_modules/@fontsource"
IMG = ROOT / "img"
CLIPS = ROOT / "clips2"
BUILD = ROOT / "build5v"
OUT = BUILD / "out"
if BUILD.exists():
    shutil.rmtree(BUILD)
OUT.mkdir(parents=True)

FPS = 24
XF = 0.30

# (clip, in-point, duration, push-direction)
BEATS = [
    ("IMG_0067", 1.00, 2.60,  1),   # the yellow Departures gate, walking toward it
    ("IMG_0061", 5.50, 2.70, -1),   # night flight, a city below that could be anywhere
    (None,       0.00, 3.60,  0),   # the app: the surprise card
    ("IMG_0044", 0.20, 2.20,  1),   # terminal at night under the lamp, empty
    ("IMG_0050", 0.90, 2.00, -1),   # aircraft at the gate, night
    ("IMG_9402", 1.30, 3.20,  1),   # sunset over the water, end card
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
    # -noautorotate: the phase 2 mirror baked rotation into the pixels but left a
    # spurious rotation=-90 flag in the container. Honouring it turns every clip
    # on its side. Verified upright against the phase 1 contact sheets.
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
CARD = f"data:image/jpeg;base64,{b64(IMG/'card-surprise.jpg')}"
WORDMARK = "".join(f'<span class="flap"><i>{c}</i><u></u><b></b><s></s></span>'
                   for c in "NEXTVISIT")

APP_I = 2
APP_IN, APP_OUT = starts[APP_I]/FPS, (starts[APP_I]+counts[APP_I])/FPS
B0 = starts[0]/FPS
B1 = starts[1]/FPS
B3 = starts[3]/FPS
B4 = starts[4]/FPS
B5 = starts[5]/FPS

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
#card{{position:absolute;left:50%;top:770px;width:952px;opacity:0;
 transform:translateX(-50%) scale(1);border-radius:26px;overflow:hidden;
 box-shadow:0 46px 110px rgba(3,10,22,.8),0 0 0 1px rgba(251,232,222,.10)}}
#card img{{display:block;width:100%}}
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

<div class="plate" id="p1"><div class="eyebrow">One of us knows</div>
  <h1>I know<br><em>the dates.</em></h1></div>

<div class="plate" id="p2"><h1>I don't know<br><em>the country.</em></h1></div>

<div class="plate" id="p3" style="top:296px"><div class="eyebrow">She planted it in the app</div>
  <h1 class="sm">Dates in.<br>Destination <em>hidden.</em></h1></div>
<div id="card"><img src="{CARD}"></div>

<div class="plate" id="p4"><h1 class="sm">45 sleeps of<br><em>not knowing.</em></h1></div>

<div class="plate" id="p5"><h1>Plant one<br><em>for later.</em></h1></div>

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
const B0={B0:.4f}, B1={B1:.4f}, APP_IN={APP_IN:.4f}, APP_OUT={APP_OUT:.4f},
      B3={B3:.4f}, B4={B4:.4f}, B5={B5:.4f};
function plate(id,t,a,b,f){{
  const o=band(t,a,b,f);
  const el=E(id);
  el.style.opacity=o;
  el.style.transform='translateY('+(24*(1-ease(cl(a,a+0.60,t)))).toFixed(1)+'px)';
  return o;
}}
window.setT=function(t){{
  const app=band(t,APP_IN,APP_OUT,0.32);
  E('navy').style.opacity=app;
  E('card').style.opacity=app;
  E('card').style.transform='translateX(-50%) scale('+(1+0.035*cl(APP_IN,APP_OUT,t)).toFixed(4)+')';

  // the hook is fully on screen at frame zero. 84% of the planner reel's
  // viewers skipped before any line landed.
  const o1=plate('p1',t,B0-0.35,B1-0.26,0.34);
  // The night-flight beat carries a faint face reflection in the window. Two
  // things keep it off screen: the line holds full opacity right through the
  // cut and only fades as the navy app beat rises over it, and a scrim runs
  // the whole beat independently of the text so there is never a frame of
  // bare glass.
  const o2=plate('p2',t,B1-0.16,APP_IN+0.30,0.30);
  const o3=plate('p3',t,APP_IN+0.52,APP_OUT-0.05,0.32);
  const o4=plate('p4',t,B3+0.32,B4-0.10,0.42);
  const o5=plate('p5',t,B4+0.30,B5+0.05,0.42);
  const wing=band(t,B1-0.34,APP_IN+0.16,0.28);

  E('scrim').style.opacity=Math.max(o1,o2,o4*0.95,o5*0.95,wing)*0.94;

  const oe=ss(cl(B5+0.55,B5+1.45,t));
  E('end').style.opacity=oe;
  E('scrimb').style.opacity=Math.max(oe*0.92,o5*0.30);
}};
window.setBG=async function(a,b,mix,sa,sb){{
  const wait=[];
  const A=E('bgA'), B=E('bgB');
  if(a && A.getAttribute('src')!==a){{ A.src=a; wait.push(A.decode().catch(()=>{{}})); }}
  A.style.transform='translate(-50%,-50%) scale('+sa+')';
  E('wrapB').style.opacity=mix;
  if(b && B.getAttribute('src')!==b){{ B.src=b; wait.push(B.decode().catch(()=>{{}})); }}
  if(b) B.style.transform='translate(-50%,-50%) scale('+sb+')';
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
            a, sa = src_for(bi, local)
            b, sb, mix = None, 1.0, 0.0
            rem = COUNTS[bi] - local
            if rem <= XFN and bi + 1 < len(BEATS) and BEATS[bi + 1][0] is not None:
                nb = bi + 1
                nlocal = local - COUNTS[bi]
                b, sb = src_for(nb, nlocal)
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
