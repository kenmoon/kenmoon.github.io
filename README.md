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
- **DNS cutover** (when Ken approves the preview):
  1. Add a `CNAME` file containing `www.kenmoon.net` (do NOT add before cutover —
     it breaks the github.io preview URL).
  2. In the domain's DNS (currently managed at Wix): point `www` CNAME to
     `kenmoon.github.io`, and apex A records to GitHub Pages IPs
     (185.199.108.153 / .109. / .110. / .111.).
  3. In repo Settings → Pages: set custom domain `www.kenmoon.net`, enable
     Enforce HTTPS once the certificate provisions.
  4. Verify, then cancel the Wix site subscription (keep the domain registration).
