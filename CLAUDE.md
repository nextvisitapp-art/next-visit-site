# Next Visit - site repo

## Marketing sessions start here

**Read `marketing/HANDOFF.md` before doing any marketing work**, every session,
without being asked. It is the running log of marketing decisions and it carries
the current strategy, the ownership split and the open questions.

**Reply by appending a new dated entry at the top** (`## YYYY-MM-DD - <who>`).
Newest above oldest. Never edit an existing entry.

### The weekly pass also writes `marketing/WEEKLY.md`

Every weekly results pass appends an entry to **`marketing/WEEKLY.md`**, and
that one is **committed straight to `main`** so the marketing hub can read it
from this repo without waiting on a pull request. Newest at the top, append
only. Four fixed sections: what ran, what changed, what broke, what needs a
decision.

`HANDOFF.md` is the narrative log where decisions get argued out; `WEEKLY.md`
is the factual record of what each run did. Both get written, and the weekly
pass is not finished until `WEEKLY.md` is on `main`.

Keep it clean for a public repo: metrics and findings yes, keys, tokens,
account or folder identifiers and user data no.

### Who does what (current, 1 Aug 2026)

- **Cowork** - strategy and the thinking behind it, concepts, hooks, the
  calendar, and the still sets. Charlie works there directly.
- **Claude Code (you)** - video. Programmatic reels via `marketing/reel/`
  (Remotion) and footage-led cuts via the `video-editing` skill (ffmpeg).
  Plus the infrastructure: app screenshot capture, committing assets,
  `results.csv`, analytics, and the weekly results pass.
- **Claude Design** - no longer in the loop. Do not address entries to it, wait
  on it, or route concepts through it unless Charlie says otherwise. Older
  entries in the log are addressed to Design; read them as history.

Charlie is pulled in only once there is something concrete: review this cut,
film these three shots, confirm this setting. Not open-ended questions.

## Design system

The full design system lives in `../next-visit-couples/CLAUDE.md` and applies
here too: tokens not hex codes, pink only for the single most important thing on
a screen, Fraunces / Inter / DM Mono in their three roles, locked brand marks.

**No em dashes anywhere in this project.** Copy, code, comments, commit
messages, PR text. Hyphens only.

## Repo shape

Static site, no build step. `index.html` plus `premium.html`, `privacy.html`,
`terms.html`, `support.html`, sharing `nv-site.css` and `nv-site.js`.
`tokens/` and `brand/` are copies of the couples-repo originals - keep them in
sync rather than editing them here. Hosted on Vercel; pushing to `main` deploys.
