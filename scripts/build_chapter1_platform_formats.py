#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import html
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUTHOR = "Chihvane Xiang"

DIV_OPEN_RE = re.compile(r"^:{3,}\s*(definition|example)\s*$")
DIV_CLOSE_RE = re.compile(r"^:{3,}\s*$")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


@dataclass(frozen=True)
class Edition:
    slug: str
    label: str
    source_dir: Path
    github_page: Path
    github_title: str
    github_permalink: str
    github_pdf_link: str
    github_diagram_prefix: str
    substack_dir: Path
    hugging_face_dir: Path
    manifest: Path
    hf_title: str

    @property
    def source_md(self) -> Path:
        return self.source_dir / "chapter1.md"

    @property
    def source_pdf(self) -> Path:
        return self.source_dir / "chapter1.pdf"

    @property
    def source_diagrams(self) -> Path:
        return self.source_dir / "diagrams"


EDITIONS = [
    Edition(
        slug="zh",
        label="Chinese",
        source_dir=ROOT / "chapters/chapter-01/final/package-v3",
        github_page=ROOT / "chapters/chapter-01/final/github-pages.md",
        github_title="Chapter 1 GitHub Pages Edition",
        github_permalink="/chapters/chapter-01/final/github-pages/",
        github_pdf_link="../package-v3/chapter1.pdf",
        github_diagram_prefix="../package-v3/diagrams/",
        substack_dir=ROOT / "publishing/chapter-01/substack",
        hugging_face_dir=ROOT / "publishing/chapter-01/hugging-face",
        manifest=ROOT / "publishing/chapter-01/conversion-manifest.md",
        hf_title="From Single-Agent OS to Constitutional Runtime - Chapter 1",
    ),
    Edition(
        slug="en",
        label="English",
        source_dir=ROOT / "chapters/chapter-01/final/package-v3-en",
        github_page=ROOT / "chapters/chapter-01/final/en/github-pages.md",
        github_title="Chapter 1 English GitHub Pages Edition",
        github_permalink="/chapters/chapter-01/final/en/github-pages/",
        github_pdf_link="../../package-v3-en/chapter1.pdf",
        github_diagram_prefix="../../package-v3-en/diagrams/",
        substack_dir=ROOT / "publishing/chapter-01/en/substack",
        hugging_face_dir=ROOT / "publishing/chapter-01/en/hugging-face",
        manifest=ROOT / "publishing/chapter-01/en/conversion-manifest.md",
        hf_title="From Single-Agent OS to Constitutional Runtime - Chapter 1 English",
    ),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read_source(edition: Edition) -> str:
    return edition.source_md.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def copy_diagrams(edition: Edition, target: Path) -> None:
    assets = target / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    for image in edition.source_diagrams.glob("*.png"):
        shutil.copy2(image, assets / image.name)


def convert_images(text: str, prefix: str) -> str:
    return text.replace("](diagrams/", f"]({prefix}")


def insert_article_signature(text: str, signature: str) -> str:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if line.startswith("### Chapter 1"):
            return "\n".join(lines[: index + 1] + ["", signature] + lines[index + 1 :])
    return f"{signature}\n\n{text}"


def signature_footer() -> str:
    return f"<sub>{AUTHOR}</sub>"


def convert_github_figures(text: str, edition: Edition) -> str:
    def repl(match: re.Match[str]) -> str:
        alt, path = match.groups()
        filename = Path(path).name
        src = f"{edition.github_diagram_prefix}{filename}"
        escaped_alt = html.escape(alt, quote=True)
        caption = html.escape(alt)
        return (
            f'<figure class="chapter-figure">\n'
            f'  <img src="{src}" alt="{escaped_alt}" loading="lazy">\n'
            f'  <figcaption>{caption}</figcaption>\n'
            f'</figure>'
        )

    return IMAGE_RE.sub(repl, text)


def convert_github(text: str, edition: Edition) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        m = DIV_OPEN_RE.match(line)
        if m:
            kind = m.group(1)
            lines.append(f'<div class="chapter-callout chapter-{kind}" markdown="1">')
            continue
        if DIV_CLOSE_RE.match(line):
            lines.append("</div>")
            continue
        lines.append(line)

    body = "\n".join(lines)
    body = convert_github_figures(body, edition)
    return f"""---
layout: page
title: {edition.github_title}
author: {AUTHOR}
permalink: {edition.github_permalink}
---

<article class="chapter-page chapter-page-{edition.slug}" markdown="1">

<p class="chapter-canonical">Canonical final artifact: <a href="{edition.github_pdf_link}">chapter1.pdf</a>. This {edition.label} GitHub Pages edition is generated from the Chapter 1 final v3 source package and preserves the final PDF text, diagrams, and definition/example blocks for web reading.</p>
<p class="chapter-signature">{AUTHOR}</p>

{body}

</article>
"""


def flatten_for_plain_markdown(text: str, image_mode: str) -> str:
    output: list[str] = []

    for line in text.splitlines():
        m = DIV_OPEN_RE.match(line)
        if m:
            output.append("")
            output.append("---")
            output.append("")
            continue

        if DIV_CLOSE_RE.match(line):
            output.append("")
            output.append("---")
            output.append("")
            continue

        img = IMAGE_RE.match(line.strip())
        if img:
            alt, path = img.groups()
            filename = Path(path).name
            if image_mode == "substack":
                output.append(f"[Figure upload: `{filename}`]")
                output.append("")
                output.append(f"_Caption: {alt}_")
                output.append("")
                output.append(f"_Source image file: `assets/{filename}`_")
            else:
                output.append(f"![{alt}](assets/{filename})")
                output.append("")
                output.append(f"<sub>{html.escape(alt)}</sub>")
            continue

        output.append(line)

    return "\n".join(output)


def convert_substack(text: str) -> str:
    body = flatten_for_plain_markdown(text, "substack")
    return insert_article_signature(body, f"_{AUTHOR}_")


def convert_hugging_face(text: str, edition: Edition) -> str:
    body = flatten_for_plain_markdown(text, "hugging-face")
    body = insert_article_signature(body, f'<p align="right"><sub>{AUTHOR}</sub></p>')
    return f"""---
title: {edition.hf_title}
author: {AUTHOR}
tags:
- ai-agents
- multi-agent-systems
- agent-governance
- constitutional-runtime
- long-horizon-ai
---

{body}
"""


def substack_readme(edition: Edition) -> str:
    return f"""# Substack Publishing Package ({edition.label})

Use `chapter1.substack.md` as the paste source for Substack.

## Files

- `chapter1.substack.md`: full Chapter 1 article, flattened for Substack
- `chapter1.pdf`: canonical final PDF for text and layout verification
- `assets/*.png`: figure images to upload manually at each figure marker

## Notes

Substack does not preserve pandoc div blocks or custom CSS. The conversion flattens PDF red/green boxes into plain Markdown separators and keeps each original box title as the visible label.

- The subtle author signature appears under the chapter subtitle.
- Figure upload markers include the source filename and caption.
- Do not paste the GitHub Pages HTML callout wrappers into Substack.

At each `[Figure upload: ...]` marker, upload the matching PNG from `assets/`.

{signature_footer()}
"""


def hugging_face_notes(edition: Edition) -> str:
    return f"""# Hugging Face Publishing Notes ({edition.label})

Use `README.md` as the Hugging Face project or Space README.

## Files

- `README.md`: full Chapter 1 article with Hugging Face-friendly front matter
- `chapter1.pdf`: canonical final PDF for faithful layout and final text
- `assets/*.png`: figure images referenced by the README

## Format

- The README front matter includes `author: {AUTHOR}`.
- The subtle author signature appears under the chapter subtitle.
- Definition/example boxes are flattened with ordinary Markdown separators and original box titles.
- Figures use relative Markdown image links plus a small caption line.
- Keep the `assets/` directory next to `README.md` when uploading.

{signature_footer()}

"""


def make_manifest(edition: Edition) -> str:
    pdf_hash = sha256(edition.source_pdf)
    md_hash = sha256(edition.source_md)
    images = sorted(edition.source_diagrams.glob("*.png"))
    return f"""# Chapter 1 Platform Conversion Manifest ({edition.label})

Generated platform editions for Chapter 1 final v3 ({edition.label}).

## Canonical Source

- Canonical final PDF: `{rel(edition.source_pdf)}`
- Source Markdown from the same package: `{rel(edition.source_md)}`
- PDF SHA-256: `{pdf_hash}`
- Markdown SHA-256: `{md_hash}`
- Diagrams copied: {len(images)}

## Generated Outputs

- GitHub Pages: `{rel(edition.github_page)}`
- Substack: `{rel(edition.substack_dir / "chapter1.substack.md")}`
- Substack notes: `{rel(edition.substack_dir / "README.md")}`
- Hugging Face: `{rel(edition.hugging_face_dir / "README.md")}`
- Hugging Face notes: `{rel(edition.hugging_face_dir / "PUBLISHING_NOTES.md")}`

## Conversion Rules

- `chapter1.pdf` remains the final authority for layout and text.
- The conversion uses the final package Markdown instead of direct PDF text extraction because direct PDF extraction can introduce line-break, table, image, and punctuation loss.
- GitHub Pages keeps definition/example blocks as styled HTML containers.
- Substack flattens definition/example blocks into plain Markdown because Substack does not preserve custom CSS or pandoc divs; original block titles are retained.
- Hugging Face uses README-friendly Markdown with relative image assets and small caption lines.
- All ten diagram PNGs are preserved for Substack and Hugging Face packages.
- Generated text editions include the subtle author signature: {AUTHOR}.

{signature_footer()}
"""


def build_edition(edition: Edition) -> None:
    if not edition.source_md.exists():
        return

    source = read_source(edition)

    write(edition.github_page, convert_github(source, edition))

    edition.substack_dir.mkdir(parents=True, exist_ok=True)
    copy_diagrams(edition, edition.substack_dir)
    write(edition.substack_dir / "chapter1.substack.md", convert_substack(source))
    write(edition.substack_dir / "README.md", substack_readme(edition))
    shutil.copy2(edition.source_pdf, edition.substack_dir / "chapter1.pdf")

    edition.hugging_face_dir.mkdir(parents=True, exist_ok=True)
    copy_diagrams(edition, edition.hugging_face_dir)
    write(edition.hugging_face_dir / "README.md", convert_hugging_face(source, edition))
    write(edition.hugging_face_dir / "PUBLISHING_NOTES.md", hugging_face_notes(edition))
    shutil.copy2(edition.source_pdf, edition.hugging_face_dir / "chapter1.pdf")

    write(edition.manifest, make_manifest(edition))


def main() -> None:
    for edition in EDITIONS:
        build_edition(edition)


if __name__ == "__main__":
    main()
