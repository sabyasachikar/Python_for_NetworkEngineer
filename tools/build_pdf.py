"""
build_pdf.py

Assemble the finished chapters into a single, styled PDF with the diagrams
embedded, a table of contents, page numbers, and a running header.

Usage:
    python tools/build_pdf.py

Output:
    Python_for_Network_Engineers.pdf  (in the repo root)

This is the Phase 5 assembler. It picks up whichever chapters are listed in
CHAPTERS below, so as more chapters are written they just get added to the list.
"""

import re
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter
from weasyprint import HTML

REPO = Path(__file__).resolve().parents[1]
CHAPTERS_DIR = REPO / "docs" / "chapters"
DIAGRAMS_DIR = REPO / "docs" / "diagrams"

# Chapters to include, in order. Add new chapter files here as they are written.
CHAPTERS = [
    "chapter00_prerequisites.md",
    "chapter01_why_python.md",
    "chapter02_first_programs.md",
]

BOOK_TITLE = "Python for Network Engineers"
BOOK_SUBTITLE = "From Python Fundamentals to Real-World Network Automation"
YEAR = "2026"
VERSION = "Version 0.1 (in development)"


def md_to_html(text):
    md = markdown.Markdown(
        extensions=["fenced_code", "tables", "sane_lists", "codehilite"],
        extension_configs={"codehilite": {"guess_lang": False, "noclasses": False}},
    )
    return md.convert(text)


def inline_svgs(html):
    """Replace <p><img src=.../x.svg></p> with the inline SVG wrapped in a figure."""
    pattern = re.compile(r'<p>\s*<img[^>]*src="[^"]*/([^"/]+\.svg)"[^>]*>\s*</p>')

    def repl(m):
        name = m.group(1)
        svg_path = DIAGRAMS_DIR / name
        svg = svg_path.read_text(encoding="utf-8")
        # strip the XML declaration if present
        svg = re.sub(r"<\?xml[^>]*\?>", "", svg).strip()
        return f'<div class="figure">{svg}</div>'

    return pattern.sub(repl, html)


def add_heading_ids(chapter_html, cnum, toc_entries):
    """Give h1/h2 unique ids and collect them for the table of contents."""
    counter = {"n": 0}

    def repl(m):
        level = int(m.group(1))
        inner = m.group(2)
        counter["n"] += 1
        hid = f"c{cnum}-{counter['n']}"
        text = re.sub(r"<[^>]+>", "", inner).strip()
        if level in (1, 2):
            toc_entries.append((level, text, hid))
        return f'<h{level} id="{hid}">{inner}</h{level}>'

    return re.sub(r"<h([12])>(.*?)</h\1>", repl, chapter_html, flags=re.S)


def build():
    toc_entries = []
    chapter_html_parts = []

    for i, fname in enumerate(CHAPTERS):
        raw = (CHAPTERS_DIR / fname).read_text(encoding="utf-8")
        html = md_to_html(raw)
        html = inline_svgs(html)
        html = add_heading_ids(html, i, toc_entries)
        chapter_html_parts.append(f'<section class="chapter">{html}</section>')

    # table of contents
    toc_items = []
    for level, text, hid in toc_entries:
        cls = "toc-l1" if level == 1 else "toc-l2"
        toc_items.append(f'<li class="{cls}"><a href="#{hid}">{text}</a></li>')
    toc_html = (
        '<section class="frontmatter toc">'
        '<div class="section-title">Contents</div>'
        f'<ul class="toc-list">{"".join(toc_items)}</ul>'
        "</section>"
    )

    cover_html = f"""
    <section class="cover">
      <div class="cover-rule"></div>
      <div class="cover-title">{BOOK_TITLE}</div>
      <div class="cover-subtitle">{BOOK_SUBTITLE}</div>
      <div class="cover-tag">Study Guide &nbsp;&middot;&nbsp; Hands-on Lab Manual &nbsp;&middot;&nbsp; Reference &nbsp;&middot;&nbsp; Practice Workbook</div>
      <div class="cover-rule"></div>
      <div class="cover-meta">
        <div>{VERSION}</div>
        <div>Author: (your name)</div>
        <div>Organization: (your organization)</div>
        <div>{YEAR}</div>
      </div>
    </section>
    """

    about_html = """
    <section class="frontmatter">
      <div class="section-title">About This Guide</div>
      <p>This guide teaches a network engineer how to use Python to automate real
      network work, starting from the absolute basics and building up to
      production-quality automation tools. It is designed to serve four purposes at
      once: a study guide you read, a hands-on lab manual you work through, a
      reference you come back to, and a practice workbook with exercises and
      solutions.</p>

      <div class="sub">Who this is for</div>
      <p>Network engineers with or without any programming background. If you know
      what a VLAN, an interface, and a BGP neighbor are, and you can use a device
      command line, the networking side is covered. This course supplies the Python.</p>

      <div class="sub">How to use it</div>
      <p>Do Chapter 0 first to set up your environment. Then work through the
      chapters in order. Read the concept, study the code walkthrough, then do the
      lab with your own hands. Try each exercise and challenge before opening its
      solution. The solutions are stored separately for exactly that reason.</p>

      <div class="sub">Lab environment</div>
      <p>Labs are tiered so you are never blocked by a lack of hardware. Many early
      labs run on mock data with no devices at all. Later labs use free sandboxes,
      containers, or emulators, and each lab tells you what it needs.</p>
    </section>
    """

    pygments_css = HtmlFormatter(style="default").get_style_defs(".codehilite")

    css = r"""
    @page {
      size: A4;
      margin: 22mm 18mm 20mm 18mm;
      @top-center { content: "Python for Network Engineers"; font-size: 8.5pt; color: #9aa4b2; }
      @bottom-right { content: counter(page); font-size: 9pt; color: #7a8494; }
      @bottom-left { content: "From Python Fundamentals to Real-World Network Automation"; font-size: 7.5pt; color: #b8c0cc; }
    }
    @page :first {
      @top-center { content: normal; }
      @bottom-right { content: normal; }
      @bottom-left { content: normal; }
    }

    html { font-family: "DejaVu Sans", "Helvetica", "Arial", sans-serif; font-size: 10.5pt; color: #23303f; line-height: 1.5; }
    body { margin: 0; }

    /* Cover */
    .cover { height: 235mm; display: flex; flex-direction: column; justify-content: center; text-align: center; page-break-after: always; }
    .cover-rule { height: 3px; background: #1f3b57; width: 60%; margin: 18px auto; }
    .cover-title { font-size: 34pt; font-weight: 700; color: #1f3b57; letter-spacing: 0.5px; }
    .cover-subtitle { font-size: 15pt; color: #2e75b6; margin-top: 10px; }
    .cover-tag { font-size: 10.5pt; color: #52606d; margin: 22px auto; max-width: 80%; }
    .cover-meta { margin-top: 40px; font-size: 11pt; color: #3b4757; line-height: 1.9; }

    /* Front matter and TOC */
    .frontmatter { page-break-before: always; }
    .section-title { font-size: 22pt; font-weight: 700; color: #1f3b57; border-bottom: 2px solid #1f3b57; padding-bottom: 6px; margin-bottom: 16px; }
    .frontmatter .sub { font-size: 13pt; font-weight: 700; color: #2e75b6; margin-top: 16px; margin-bottom: 4px; }

    .toc-list { list-style: none; padding-left: 0; }
    .toc-list li { margin: 3px 0; }
    .toc-list a { text-decoration: none; color: #23303f; }
    .toc-l1 { font-weight: 700; color: #1f3b57; margin-top: 10px !important; }
    .toc-l1 a { color: #1f3b57; }
    .toc-l2 { padding-left: 18px; font-size: 9.7pt; color: #4a5666; }
    .toc-list a::after { content: leader('. ') target-counter(attr(href), page); font-weight: 400; color: #6b7686; }

    /* Chapters */
    .chapter { page-break-before: always; }
    h1 { font-size: 21pt; color: #1f3b57; border-bottom: 2px solid #1f3b57; padding-bottom: 6px; margin-top: 4px; }
    h2 { font-size: 15pt; color: #1f3b57; margin-top: 20px; border-bottom: 1px solid #dbe3ee; padding-bottom: 3px; }
    h3 { font-size: 12.5pt; color: #2e75b6; margin-top: 14px; }
    p { margin: 8px 0; }

    a { color: #2e75b6; }

    /* Inline and block code */
    code { font-family: "DejaVu Sans Mono", monospace; font-size: 9pt; background: #eef1f5; padding: 1px 4px; border-radius: 3px; color: #b83b5e; }
    pre { background: #f6f8fa; border: 1px solid #e3e8ee; border-left: 4px solid #2e75b6; border-radius: 4px; padding: 10px 12px; font-size: 8.7pt; line-height: 1.4; white-space: pre-wrap; word-wrap: break-word; overflow-wrap: break-word; }
    pre code { background: none; color: inherit; padding: 0; font-size: 8.7pt; }
    .codehilite { background: #f6f8fa; border: 1px solid #e3e8ee; border-left: 4px solid #2e75b6; border-radius: 4px; margin: 10px 0; }
    .codehilite pre { border: none; border-left: none; margin: 0; background: none; }

    /* Tables */
    table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 9.3pt; }
    th, td { border: 1px solid #cdd6e0; padding: 6px 9px; text-align: left; vertical-align: top; }
    th { background: #eef3f8; color: #1f3b57; }

    /* Blockquote callouts */
    blockquote { margin: 12px 0; padding: 8px 14px; background: #f4f7fb; border-left: 4px solid #2e8b7f; color: #33475b; }
    blockquote p { margin: 4px 0; }

    /* Figures */
    .figure { margin: 14px 0; text-align: center; page-break-inside: avoid; }
    .figure svg { width: 100%; height: auto; max-height: 155mm; }
    em { color: #52606d; }

    ul, ol { margin: 8px 0; padding-left: 22px; }
    li { margin: 3px 0; }
    """ + pygments_css

    full_html = f"""<!DOCTYPE html>
    <html><head><meta charset="utf-8"><title>{BOOK_TITLE}</title></head>
    <body>
    {cover_html}
    {about_html}
    {toc_html}
    {''.join(chapter_html_parts)}
    </body></html>"""

    out = REPO / "Python_for_Network_Engineers.pdf"
    HTML(string=full_html, base_url=str(REPO)).write_pdf(str(out), stylesheets=[__import__("weasyprint").CSS(string=css)])
    print("Wrote", out)


if __name__ == "__main__":
    build()
