#!/usr/bin/env python3
"""Profile picture options for @twonightsaway. Four marks, rendered at 1024
square, then a contact sheet showing each at the sizes the platforms actually
display: 40px in a comment row, 80px in a feed, 160px on the profile page.

The test is 40px. Anything that dies at 40px is not a profile picture."""
import asyncio, base64, pathlib, shutil, subprocess
from playwright.async_api import async_playwright

ROOT = pathlib.Path("/home/claude/nv")
FONTS = ROOT / "fonts/node_modules/@fontsource"
OUT = ROOT / "pfp"
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

b64 = lambda p: base64.b64encode(pathlib.Path(p).read_bytes()).decode()
face = lambda f, p, w, st="normal": (
    f"@font-face{{font-family:'{f}';font-style:{st};font-weight:{w};"
    f"src:url(data:font/woff2;base64,{b64(p)}) format('woff2');}}")
FONT_CSS = "".join([
    face("Fraunces", FONTS/"fraunces/files/fraunces-latin-600-normal.woff2", 600),
    face("Fraunces", FONTS/"fraunces/files/fraunces-latin-600-italic.woff2", 600, "italic"),
    face("DM Mono", FONTS/"dm-mono/files/dm-mono-latin-500-normal.woff2", 500),
])

# Same navy and cream as Next Visit. Not the logo, but the same air, so that
# when someone finds the app later it does not feel like a different company.
BG = ("radial-gradient(115% 75% at 50% -12%,#1a3a68 0,transparent 62%),"
      "radial-gradient(85% 55% at 100% 108%,#0b1c36 0,transparent 66%),#0e2240")

CRESCENT = """
<svg class="moon" viewBox="0 0 100 100">
  <defs><mask id="mk%d">
    <rect width="100" height="100" fill="#000"/>
    <circle cx="50" cy="50" r="46" fill="#fff"/>
    <circle cx="72" cy="38" r="40" fill="#000"/>
  </mask></defs>
  <rect width="100" height="100" fill="%s" mask="url(#mk%d)"/>
</svg>"""

OPTIONS = {
"a-two": f"""
<div class="wrap">
  <div class="big">2</div>
  <div class="sub">NIGHTS AWAY</div>
</div>
<style>
.wrap{{display:flex;flex-direction:column;align-items:center;justify-content:center;
 height:100%;transform:translateY(-14px)}}
.big{{font-family:Fraunces;font-weight:600;font-size:620px;line-height:.78;
 color:#fbe8de;letter-spacing:-.02em}}
.sub{{font-family:'DM Mono';font-weight:500;font-size:76px;letter-spacing:.30em;
 color:#eccab4;margin-top:52px;text-indent:.30em}}
</style>""",

"b-moons": f"""
<div class="wrap">
  {CRESCENT % (1, '#fbe8de', 1)}
  {CRESCENT % (2, '#ec4079', 2)}
</div>
<style>
.wrap{{display:flex;align-items:center;justify-content:center;gap:66px;height:100%}}
.moon{{width:330px;height:330px;display:block}}
</style>""",

"c-stack": f"""
<div class="wrap">
  <div class="l">TWO</div><div class="l">NIGHTS</div><div class="l em">away</div>
</div>
<style>
.wrap{{display:flex;flex-direction:column;align-items:center;justify-content:center;
 height:100%;gap:6px}}
.l{{font-family:Fraunces;font-weight:600;font-size:210px;line-height:1.0;
 color:#fbe8de;letter-spacing:-.015em}}
.em{{font-style:italic;color:#ec4079}}
</style>""",

"d-moon-two": f"""
<div class="wrap">
  {CRESCENT % (3, '#fbe8de', 3)}
  <div class="big">2</div>
</div>
<style>
.wrap{{display:flex;align-items:center;justify-content:center;gap:40px;height:100%;
 transform:translateY(-8px)}}
.moon{{width:300px;height:300px;display:block;margin-top:36px}}
.big{{font-family:Fraunces;font-weight:600;font-size:560px;line-height:.78;
 color:#fbe8de;letter-spacing:-.02em}}
</style>""",
}

SHELL = """<!doctype html><html><head><meta charset="utf-8"><style>
%s
*{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased}
html,body{width:1024px;height:1024px;overflow:hidden}
body{background:%s}
</style></head><body>%s</body></html>"""


async def main():
    async with async_playwright() as p:
        br = await p.chromium.launch()
        pg = await br.new_page(viewport={"width": 1024, "height": 1024},
                               device_scale_factor=1)
        for name, body in OPTIONS.items():
            await pg.set_content(SHELL % (FONT_CSS, BG, body))
            await pg.evaluate("document.fonts.ready")
            await pg.wait_for_timeout(160)
            await pg.screenshot(path=str(OUT / f"{name}.png"))
            print("rendered", name)
        await br.close()

asyncio.run(main())

# Circle-crop each one the way the platforms will, then build the sheet.
for f in sorted(OUT.glob("*.png")):
    subprocess.run([
        "convert", str(f), "-alpha", "on",
        "(", "+clone", "-alpha", "extract", "-draw",
        "fill black polygon 0,0 0,1024 8,0 fill white circle 512,512 512,0",
        ")", "-alpha", "off", "-compose", "CopyOpacity", "-composite",
        str(OUT / f"c-{f.stem}.png")
    ], check=True)

rows = []
for f in sorted(OUT.glob("c-*.png")):
    tiles = []
    for size in (40, 80, 160):
        t = OUT / f"t{size}-{f.stem}.png"
        subprocess.run(["convert", str(f), "-resize", f"{size}x{size}",
                        "-background", "#1c1c1e", "-gravity", "center",
                        "-extent", "200x200", "-flatten", str(t)], check=True)
        tiles.append(str(t))
    row = OUT / f"row-{f.stem}.png"
    subprocess.run(["convert"] + tiles + ["+append", str(row)], check=True)
    rows.append(str(row))

subprocess.run(["convert"] + rows + ["-append",
                "-bordercolor", "#1c1c1e", "-border", "20",
                str(OUT / "sizes.png")], check=True)

subprocess.run(["convert"] + [str(OUT / f"c-{n}.png") for n in OPTIONS] +
               ["-resize", "420x420", "-background", "#1c1c1e", "-gravity",
                "center", "-extent", "460x460", "+append",
                str(OUT / "all.png")], check=True)
print("sheets done")
