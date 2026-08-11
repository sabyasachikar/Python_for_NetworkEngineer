# Publishing the book as a free online site

The book is set up to publish as a website with MkDocs and the Material theme. The
chapters and diagrams you already have become a searchable, mobile-friendly site.

## Preview it on your own machine first

From the project folder, with your virtual environment active:

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

Open the address it prints (usually http://127.0.0.1:8000) in your browser. The site
reloads as you edit, so you can watch changes live. Press Ctrl+C to stop.

## Publish to GitHub Pages

There are two ways. Pick one.

### Option A: automatic (recommended)

This repository includes a GitHub Actions workflow at
`.github/workflows/deploy-docs.yml`. Once your code is on GitHub:

1. Push to the `main` branch (you already do this with `git push`).
2. In your GitHub repository, open Settings, then Pages, and set the source to the
   `gh-pages` branch (the workflow creates it on the first run).
3. Every push to `main` from then on rebuilds and republishes the site
   automatically.

Your site will be at `https://YOUR-USERNAME.github.io/python-for-network-engineers/`.

### Option B: manual

Run this once from your machine whenever you want to publish:

```bash
mkdocs gh-deploy
```

That builds the site and pushes it to the `gh-pages` branch for you. Then set
Settings, Pages, source to `gh-pages` as above.

## Adding new chapters

When a new chapter file is added under `docs/chapters/`, add one line to the `nav`
section of `mkdocs.yml` pointing at it. That is the only step. The diagrams referenced
by the chapter are picked up automatically.

## A note on naming and ownership

The content is original, so you are free to publish it. Update the author and
copyright placeholders in `mkdocs.yml` and `README.md` with your name. Keep the paid
video course and the reference book as background only, never pasted in, so your
published work stays cleanly your own.
