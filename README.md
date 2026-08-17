# kenmoon.net — personal academic site

Static site for Ken Moon, served by GitHub Pages from `kenmoon/kenmoon.github.io`.
No build system, no dependencies: hand-written HTML/CSS plus one generator script.

## Files

- `index.html` — home page (bio + contact). Edited by hand.
- `papers.json` — the paper list, the single source of truth for the publications page.
  Sections → papers, each with `title`, `authors`, optional `venue` (published work),
  `status` (revision/review status), and `url` (DOI or SSRN).
- `build.py` — regenerates `publications.html` from `papers.json` (stdlib only).
- `publications.html` — GENERATED. Do not edit by hand; edit `papers.json` and rebuild.
- `style.css` — all styling.
- `assets/` — CV PDF and photo live here when added.

## Updating the paper list

1. Edit `papers.json` (statuses come from the current CV).
2. `python3 build.py`
3. Commit and push both `papers.json` and `publications.html`.

## Pending items

- **CV PDF**: Ken posts only PDF CVs and reviews/censors before posting. When he
  produces the approved PDF, save it as `assets/CV_KenMoon.pdf` and uncomment the CV
  link in the `<nav>` of BOTH `index.html` and the `PAGE` template in `build.py`,
  then rebuild.
- **Photo**: optional; drop into `assets/` and add to `index.html` header.
- **kenmoon.net handling** (updated 2026-08-17): kenmoon.github.io is the intended
  LONG-TERM address; kenmoon.net exists only so old documents/links resolve until
  the domain lapses (registration expires 2027-06-06, renewal to be cancelled).
  Wix offers no plain HTTP forwarding, so INTERIM setup = GitHub Pages custom
  domain: Wix DNS apex A records → GitHub Pages IPs, `www` CNAME →
  kenmoon.github.io, and the `CNAME` file here containing `kenmoon.net`. While
  this is active, github.io 301s to kenmoon.net — expected. **Before the domain
  dies (calendar reminder 2027-04-26): delete the `CNAME` file and clear the
  custom domain in repo Settings → Pages**, restoring direct github.io serving.
