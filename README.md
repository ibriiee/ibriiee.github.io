# ibriiee.github.io — Ibrahim Naeem

`PERSONAL SITE · REV 02 · 2026-08-02`

Two pages, one free GitHub Pages site, no build step and no dependencies. System fonts only
(Palatino serif, Segoe UI sans, Consolas mono). Both pages work opened straight from disk.

| URL | Page | Audience | Job |
|---|---|---|---|
| `ibriiee.github.io` | `index.html` | Clients, partners, buyers | Get hired for outcomes, sell products |
| `ibriiee.github.io/profile.html` | `profile.html` | Recruiters, HR, hiring panels | Get shortlisted |

`profile.html` is fully self-contained: the headshot is embedded as base64, so the single file can
be sent over WhatsApp or email and still works offline, with no broken images.

## Files

```
index.html          the founder site
profile.html        the interactive recruiter profile (self-contained, WhatsApp-safe)
assets/headshot.jpg used by index.html
assets/og-image.jpg social card for index.html
assets/og-profile.jpg social card for profile.html
```

Master copy of the profile lives at `Job Hunt/Interactive Profile/Ibrahim's Profile.html`. Edit
there first (its rules are in that folder's `DESIGN-BRIEF.md`), then copy over `profile.html` here.

## Deploy

Already live. To push a change:

```bash
git add -A && git commit -m "Update site" && git push
```

GitHub Pages rebuilds in about a minute. Settings are already correct: repo
`ibriiee/ibriiee.github.io`, branch `main`, folder `/`.

## Updating

Edit the file, bump the `REV` stamp in the hero top-right and the footer, commit, push. Social
cards regenerate from `scripts/make_og.py` if the headline ever changes.

## What is on index.html

Hero with accreditation badge → stat strip (12+ yrs, 140+ delegations, 60 chauffeurs, 753 tests) →
**Ventures** (Fluencer Hive, Kaza Umri, Mizan, Burrak Express) → **Systems** (Auto Pilot Events OS,
Brain + Abdullah, data science, content engine) → **The Floor** (filterable 18-entry timeline) →
**On Record** (facts table) → contact.

Interactions: scroll progress bar, scroll-spy nav, animated counters, reveal on scroll, filterable
timeline, 3D tilt cards, magnetic buttons, live Asia/Dubai clock, copy-email-to-clipboard, dark and
light themes persisted in `localStorage`, and a real mobile menu. All guarded by
`prefers-reduced-motion` and `pointer: fine`.

## House rules

- Every figure is record-verified against `Job Hunt/PROFILE.md`. Nothing is invented or estimated.
- No em-dashes in visible prose. En-dash only inside a date range like 2020–21.
- One accent colour, gold `#d4af37`. Gold text darkens to `#7d6410` on the light theme so every
  text pair clears WCAG AA at 4.5:1.
- No testimonials, client logos, or revenue figures. None are recorded and none get invented.

## Deliberately left out

- Revenue for Fluencer Hive and Burrak Express. Not recorded, so the page states the facts without
  numbers rather than estimating.
- Analytics, cookie banner, newsletter, blog.
