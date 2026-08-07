#!/usr/bin/env python3
"""Video 05: the ring size. First of the 'things you can't ask without ruining
it' series. One product truth: Little Things. No b-roll at all - the whole
video is one screen recording, because the screen IS the story."""
import asyncio, base64, pathlib, shutil, subprocess
from playwright.async_api import async_playwright

ROOT = pathlib.Path("/home/claude/nv")
FONTS = ROOT / "fonts/node_modules/@fontsource"
CLIPS = ROOT / "clips2"
BUILD = ROOT / "build19v"
OUT = BUILD / "out"
if BUILD.exists():
    shutil.rmtree(BUILD)
OUT.mkdir(parents=True)

FPS = 24
XF = 0.30
SRC = "lt"          # ScreenRecording_08-04-2026 09-46-44_1, 886x1920, 34.07s
PW = 720            # panel width; 886x1920 source scales to 720x1560

# (in-point, duration) - every beat is the same recording, different moment
BEATS = [
    (14.60, 3.20),   # his tab: the maybe-don't. "Saturday of a match"
    (28.20, 3.40),   # her tab: no surprise parties, lilies, no speeches
    (30.40, 2.60),   # hold, end card lands here. Do NOT go past 33.0:
                     # the recording ends on the iOS control centre.
]
DUR = sum(b[1] for b in BEATS)
NF = int(round(DUR * FPS))

starts, counts = [], []
acc = 0
for _, dur in BEATS:
    starts.append(acc)
    counts.append(int(round(dur * FPS)))
    acc += counts[-1]
XFN = int(round(XF * FPS))

for bi, (tin, dur) in enumerate(BEATS):
    d = BUILD / f"a{bi}"
    d.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "ffmpeg", "-v", "error", "-noautorotate",
        "-ss", str(max(0, tin - XF)), "-i", str(CLIPS / f"{SRC}.mp4"),
        "-frames:v", str(counts[bi] + XFN + 2), "-vf", f"fps={FPS},scale={PW}:-2",
        str(d / "f%04d.jpg"), "-q:v", "2", "-y"
    ], check=True)
print("extracted", NF, "frames", round(DUR, 2), "s")

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
WORDMARK = "".join(f'<span class="flap"><i>{c}</i><u></u><b></b><s></s></span>'
                   for c in "NEXTVISIT")
B = [s / FPS for s in starts]

HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>
{FONT_CSS}
:root{{--navy:#0e2240;--cream:#fbe8de;--cream3:#eccab4;--pink:#ec4079;--tile:#06122a}}
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}}
html,body{{width:1080px;height:1920px;overflow:hidden;background:#05111f}}
#navy{{position:absolute;inset:0;background:
 radial-gradient(120% 70% at 50% -10%,#17335c 0,transparent 60%),
 radial-gradient(90% 50% at 100% 105%,#0b1c36 0,transparent 65%),var(--navy)}}
/* the recording sits in the lower two thirds so the type has clean navy above.
   Full bleed would put the headline over the app's own header. */
#ph{{position:absolute;left:50%;top:470px;width:{PW}px;height:1450px;
 transform:translateX(-50%) scale(1);border-radius:38px;overflow:hidden;
 box-shadow:0 56px 120px rgba(3,10,22,.85),0 0 0 1px rgba(251,232,222,.13);
 -webkit-mask-image:linear-gradient(to bottom,#000 0,#000 84%,transparent 100%)}}
#ph img{{position:absolute;left:0;top:0;display:block;width:{PW}px}}
#appB{{opacity:0}}
#scrimb{{position:absolute;left:0;right:0;bottom:0;height:900px;opacity:0;
 background:linear-gradient(0deg,rgba(5,17,31,.92) 0%,rgba(5,17,31,.55) 55%,rgba(5,17,31,0) 100%)}}
.plate{{position:absolute;left:96px;right:96px;top:190px;opacity:0}}
.eyebrow{{font-family:'DM Mono',monospace;font-weight:500;font-size:26px;letter-spacing:.24em;
 text-transform:uppercase;color:var(--cream3);opacity:.78;margin-bottom:26px}}
h1{{font-family:'Fraunces',serif;font-weight:600;color:var(--cream);
 font-size:96px;line-height:1.08;letter-spacing:-.015em;
 text-shadow:0 2px 34px rgba(4,12,26,.55)}}
h1 em{{font-style:italic;color:var(--pink)}}
h1.lg{{font-size:112px}}
h1.md{{font-size:82px}}
#end{{position:absolute;left:0;right:0;bottom:170px;text-align:center;opacity:0}}
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
 text-transform:uppercase;color:var(--cream);opacity:.66;margin-top:32px}}
.appicon{{width:126px;height:126px;border-radius:28.2px;overflow:hidden;display:flex;
 margin:0 auto 30px;box-shadow:0 5px 16px rgba(0,0,0,.35),inset 0 0 0 1px rgba(251,232,222,.05)}}
.half{{position:relative;width:63px;height:126px;background:var(--tile);overflow:hidden}}
.half i{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
 font-family:'Space Grotesk',sans-serif;font-weight:700;font-style:normal;
 font-size:78.1px;line-height:1;letter-spacing:-.01em}}
.half u{{position:absolute;left:0;right:0;top:50%;height:1px;background:rgba(0,0,0,.6)}}
.half b{{position:absolute;left:0;right:0;top:0;height:50%;
 background:linear-gradient(180deg,rgba(255,255,255,.06),rgba(255,255,255,0))}}
.half s{{position:absolute;left:0;right:0;top:50%;bottom:0;
 background:linear-gradient(180deg,rgba(0,0,0,.05),rgba(0,0,0,.20))}}
.mark .flap{{width:60px;height:80px;border-radius:4.2px}}
.mark .flap i{{font-size:53px}}
</style></head><body>
<div id="navy"></div>
<div id="ph"><img id="appA" src=""><img id="appB" src=""></div>
<div id="scrimb"></div>

<div class="plate" id="p1"><h1 class="md">Everyone has<br>one thing they'd<br><em>hate.</em></h1></div>
<div class="plate" id="p2"><div class="eyebrow">Hers</div>
  <h1 class="lg">No <em>speeches.</em></h1></div>
<div class="plate" id="p3"><h1>Neither of you<br>has to <em>guess.</em></h1></div>

<div id="end">
  <div class="appicon">
    <div class="half"><i style="color:var(--cream);transform:translateX(8.82px)">N</i><u></u><b></b><s></s></div>
    <div class="half"><i style="color:var(--pink);transform:translateX(-8.82px)">V</i><u></u><b></b><s></s></div>
  </div>
  <div class="mark">{WORDMARK}</div>
  <div class="url">Free on the App Store</div></div>

<script>
const E=i=>document.getElementById(i);
const cl=(a,b,t)=>Math.max(0,Math.min(1,(t-a)/(b-a)));
const ease=x=>1-Math.pow(1-x,3);
const ss=x=>x*x*(3-2*x);
const band=(t,a,b,f=0.4)=>Math.min(ss(cl(a,a+f,t)),1-ss(cl(b-f,b,t)));
const B=[{B[0]:.4f},{B[1]:.4f},{B[2]:.4f}];
function plate(id,t,a,b,f){{
  const o=band(t,a,b,f);
  const el=E(id);
  el.style.opacity=o;
  el.style.transform='translateY('+(22*(1-ease(cl(a,a+0.55,t)))).toFixed(1)+'px)';
  return o;
}}
window.setT=function(t){{
  // the hook is up at frame zero. Everything after 2s is borrowed time.
  plate('p1',t,-0.32,B[1]-0.04,0.30);
  plate('p2',t,B[1]+0.16,B[2]-0.02,0.26);
  plate('p3',t,B[2]+0.14,B[2]+1.70,0.26);
  const oe=ss(cl(B[2]+1.20,B[2]+2.05,t));
  E('end').style.opacity=oe;
  E('scrimb').style.opacity=oe*0.95;
  E('ph').style.transform='translateX(-50%) scale('+(1+0.022*cl(0,{DUR:.4f},t)).toFixed(4)+')';
}};
window.setApp=async function(a,b,mix){{
  const wait=[];
  const A=E('appA'), Bg=E('appB');
  if(a && A.getAttribute('src')!==a){{ A.src=a; wait.push(A.decode().catch(()=>{{}})); }}
  if(b && Bg.getAttribute('src')!==b){{ Bg.src=b; wait.push(Bg.decode().catch(()=>{{}})); }}
  Bg.style.opacity=mix;
  await Promise.all(wait);
}};
</script></body></html>"""

(BUILD / "index.html").write_text(HTML)
STARTS, COUNTS = starts, counts
AVAIL = {}


def frame_path(bi, local):
    if bi not in AVAIL:
        AVAIL[bi] = len(list((BUILD / f"a{bi}").glob("*.jpg")))
    n = max(1, min(local + XFN + 1, AVAIL[bi]))
    return f"a{bi}/f{n:04d}.jpg"


def ease_py(x):
    return x * x * (3 - 2 * x)


async def main():
    async with async_playwright() as p:
        br = await p.chromium.launch()
        pg = await br.new_page(viewport={"width": 1080, "height": 1920},
                               device_scale_factor=1)
        await pg.goto(f"file://{BUILD}/index.html")
        await pg.wait_for_timeout(1200)
        for i in range(NF):
            t = i / FPS
            bi = next(k for k in range(len(BEATS) - 1, -1, -1) if i >= STARTS[k])
            local = i - STARTS[bi]
            rem = COUNTS[bi] - local
            a = frame_path(bi, local)
            b, mix = None, 0.0
            if rem <= XFN and bi + 1 < len(BEATS):
                b = frame_path(bi + 1, local - COUNTS[bi])
                mix = round(ease_py(1 - rem / XFN), 4)
            await pg.evaluate(
                "async ([a,b,m,t]) => { await window.setApp(a||'', b||'', m); window.setT(t); }",
                [a, b or "", mix, t])
            await pg.screenshot(path=str(OUT / f"f{i:04d}.png"))
            if i % 60 == 0:
                print("frame", i, "/", NF, flush=True)
        await br.close()
    print("done", NF, "frames", round(DUR, 2), "s")


asyncio.run(main())
