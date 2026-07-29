# Next Visit - site repo

## Marketing sessions start here

**Read `marketing/HANDOFF.md` before doing any marketing work**, every session,
without being asked. It is the shared log between Claude Code and Claude Design
and it carries the current strategy, the ownership split and the open
questions.

**Reply by appending a new dated entry at the top** (`## YYYY-MM-DD - <who>`).
Newest above oldest. Never edit an existing entry.

Strategy gets settled in that file between Code and Design. Charlie is pulled in
only once there is something concrete: review this cut, film these three shots,
confirm this setting. Not open-ended questions.

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
