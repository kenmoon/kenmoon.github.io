#!/usr/bin/env python3
"""Generate publications.html from papers.json. Stdlib only.

Usage: python3 build.py   (run from the repo root, then commit both files)
"""
import json
import html
from pathlib import Path

ROOT = Path(__file__).parent

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Publications &amp; Papers — Ken Moon</title>
<meta name="description" content="Publications and working papers by Ken Moon, Cornell SC Johnson College of Business.">
<link rel="stylesheet" href="style.css">
</head>
<body>

<header>
  <div class="wrap header-flex">
    <div class="header-text">
      <h1><a href="index.html">Ken Moon</a></h1>
      <p class="tagline">Associate Professor of Operations, Technology and Information Management<br>
      Cornell SC Johnson College of Business</p>
      <nav>
        <a href="index.html">Home</a>
        <a href="publications.html" class="active">Publications &amp; Papers</a>
        <a href="assets/CV_KenMoon.pdf">CV</a>
      </nav>
    </div>
    <img class="portrait" src="assets/photo.jpg" alt="Portrait of Ken Moon">
  </div>
</header>

<main>
  <div class="wrap">
{sections}
  </div>
</main>

<footer>
  <div class="wrap">&copy; 2026 Ken Moon</div>
</footer>

</body>
</html>
"""


def render_paper(p):
    title = html.escape(p["title"])
    if p.get("url"):
        title_html = f'<a href="{html.escape(p["url"])}">{title}</a>'
    else:
        title_html = title
    lines = [f'    <div class="paper">',
             f'      <p class="title">{title_html}</p>',
             f'      <p class="authors">{html.escape(p["authors"])}</p>']
    if p.get("venue"):
        lines.append(f'      <p class="venue">{html.escape(p["venue"])}</p>')
    if p.get("status"):
        lines.append(f'      <p class="venue"><span class="status">{html.escape(p["status"])}</span></p>')
    lines.append('    </div>')
    return "\n".join(lines)


def main():
    data = json.loads((ROOT / "papers.json").read_text())
    out = []
    for section in data["sections"]:
        out.append(f'    <h2>{html.escape(section["title"])}</h2>')
        out.extend(render_paper(p) for p in section["papers"])
    page = PAGE.replace("{sections}", "\n".join(out))
    (ROOT / "publications.html").write_text(page)
    n = sum(len(s["papers"]) for s in data["sections"])
    print(f"Wrote publications.html ({n} papers, {len(data['sections'])} sections)")


if __name__ == "__main__":
    main()
