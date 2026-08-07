# Render scripts - reference implementation

The marketing hub's scripts, handed over 6 Aug 2026. They built videos 03 to
06 and are the reference for the render pipeline, the design tokens in code,
and the beat structure. Production (Claude Code) owns and runs them; the
mapping, worked out from docstrings, timestamps and beat sums:

| script | video | length | note |
| --- | --- | ---: | --- |
| reel4.py | 03 v1 | 16.3s | superseded by reel5 |
| reel5.py | 03 final | 16.3s | as posted 2 Aug |
| reel6.py | 04 v1 | 17.1s | superseded |
| reel7.py | 04 v2 | - | superseded by reel10 |
| reel10.py | 04 final | 11.9s | the 11.9s rebuild |
| reel11.py | 05 final | 10.7s | ring size |
| reel12.py | 06 final | 9.2s | docstring stale, content is 06 |
| pfp.py | - | - | profile picture options |

They expect /home/claude/nv with fonts/ (@fontsource), clips2/ (from the
footage branch) and img/. They render PNG frames only; encoding to h264 is a
separate ffmpeg pass. See marketing/MARKETING.md for the format spec; that
file is the hub's and does not get edited here.
