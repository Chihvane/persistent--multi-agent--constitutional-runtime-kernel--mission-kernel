#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "chapters/chapter-01/final/package-v3"
SOURCE_MD = SOURCE_DIR / "chapter1.md"
SOURCE_PDF = SOURCE_DIR / "chapter1.pdf"
SOURCE_DIAGRAMS = SOURCE_DIR / "diagrams"

GITHUB_PAGE = ROOT / "chapters/chapter-01/final/github-pages.md"
HF_DIR = ROOT / "publishing/chapter-01/hugging-face"
SUBSTACK_DIR = ROOT / "publishing/chapter-01/substack"
MANIFEST = ROOT / "publishing/chapter-01/conversion-manifest.md"

DIV_OPEN_RE = re.compile(r"^:{3,}\s*(definition|example)\s*$")
DIV_CLOSE_RE = re.compile(r"^:{3,}\s*$")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_source() -> str:
    return SOURCE_MD.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def copy_diagrams(target: Path) -> None:
    assets = target / "assets"
    assets.mkdir(parents=True, exist_ok=True)
    for image in SOURCE_DIAGRAMS.glob("*.png"):
        shutil.copy2(image, assets / image.name)


def convert_images(text: str, prefix: str) -> str:
    return text.replace("](diagrams/", f"]({prefix}")


def convert_github(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        m = DIV_OPEN_RE.match(line)
        if m:
            kind = m.group(1)
            label = "Definition / Structure Rule" if kind == "definition" else "Scenario / Example"
            lines.append(f'<div class="chapter-callout chapter-{kind}" markdown="1">')
            lines.append(f'<div class="chapter-callout-label">{label}</div>')
            continue
        if DIV_CLOSE_RE.match(line):
            lines.append("</div>")
            continue
        lines.append(line)

    body = "\n".join(lines)
    body = convert_images(body, "./package-v3/diagrams/")
    return f"""---
layout: page
title: Chapter 1 GitHub Pages Edition
permalink: /chapters/chapter-01/final/github-pages/
---

> Canonical final artifact: [chapter1.pdf](./package-v3/chapter1.pdf). This GitHub Pages edition is generated from the Chapter 1 final v3 source package and preserves the final PDF text, diagrams, and definition/example blocks for web reading.

{body}
"""


def flatten_for_plain_markdown(text: str, image_mode: str) -> str:
    output: list[str] = []
    current_block: str | None = None

    for line in text.splitlines():
        m = DIV_OPEN_RE.match(line)
        if m:
            current_block = m.group(1)
            output.append("")
            output.append("---")
            output.append(
                "**Definition / Structure Rule**"
                if current_block == "definition"
                else "**Scenario / Example**"
            )
            output.append("")
            continue

        if DIV_CLOSE_RE.match(line):
            output.append("")
            output.append("---")
            output.append("")
            current_block = None
            continue

        img = IMAGE_RE.match(line.strip())
        if img:
            alt, path = img.groups()
            filename = Path(path).name
            if image_mode == "substack":
                output.append(f"[Figure upload: `{filename}`]")
                output.append("")
                output.append(f"Caption: {alt}")
                output.append("")
                output.append(f"Source image file: `assets/{filename}`")
            else:
                output.append(f"![{alt}](assets/{filename})")
            continue

        output.append(line)

    return "\n".join(output)


def convert_substack(text: str) -> str:
    return flatten_for_plain_markdown(text, "substack")


def convert_hugging_face(text: str) -> str:
    body = flatten_for_plain_markdown(text, "hugging-face")
    return f"""---
title: From Single-Agent OS to Constitutional Runtime - Chapter 1
tags:
- ai-agents
- multi-agent-systems
- agent-governance
- constitutional-runtime
- long-horizon-ai
---

{body}
"""


def substack_readme() -> str:
    return """# Substack Publishing Package

Use `chapter1.substack.md` as the paste source for Substack.

## Files

- `chapter1.substack.md`: full Chapter 1 article, flattened for Substack
- `chapter1.pdf`: canonical final PDF for text and layout verification
- `assets/*.png`: figure images to upload manually at each figure marker

## Notes

Substack does not preserve pandoc div blocks or custom CSS. The conversion replaces PDF red/green boxes with plain Markdown separators and visible labels:

- `Definition / Structure Rule`
- `Scenario / Example`

At each `[Figure upload: ...]` marker, upload the matching PNG from `assets/`.

"""


def hugging_face_notes() -> str:
    return """# Hugging Face Publishing Notes

Use `README.md` as the Hugging Face project or Space README.

## Files

- `README.md`: full Chapter 1 article with Hugging Face-friendly front matter
- `chapter1.pdf`: canonical final PDF for faithful layout and final text
- `assets/*.png`: figure images referenced by the README

The README uses ordinary relative Markdown image links, so keep the `assets/` directory next to `README.md` when uploading.

"""


def make_manifest() -> str:
    pdf_hash = sha256(SOURCE_PDF)
    md_hash = sha256(SOURCE_MD)
    images = sorted(SOURCE_DIAGRAMS.glob("*.png"))
    return f"""# Chapter 1 Platform Conversion Manifest

Generated platform editions for Chapter 1 final v3.

## Canonical Source

- Canonical final PDF: `chapters/chapter-01/final/package-v3/chapter1.pdf`
- Source Markdown from the same package: `chapters/chapter-01/final/package-v3/chapter1.md`
- PDF SHA-256: `{pdf_hash}`
- Markdown SHA-256: `{md_hash}`
- Diagrams copied: {len(images)}

## Generated Outputs

- GitHub Pages: `chapters/chapter-01/final/github-pages.md`
- Substack: `publishing/chapter-01/substack/chapter1.substack.md`
- Substack notes: `publishing/chapter-01/substack/README.md`
- Hugging Face: `publishing/chapter-01/hugging-face/README.md`
- Hugging Face notes: `publishing/chapter-01/hugging-face/PUBLISHING_NOTES.md`

## Conversion Rules

- `chapter1.pdf` remains the final authority for layout and text.
- The conversion uses the final package Markdown instead of direct PDF text extraction because direct PDF extraction can introduce line-break, table, image, and punctuation loss.
- GitHub Pages keeps definition/example blocks as styled HTML containers.
- Substack flattens definition/example blocks into plain Markdown because Substack does not preserve custom CSS or pandoc divs.
- Hugging Face uses README-friendly Markdown with relative image assets.
- All ten diagram PNGs are preserved for Substack and Hugging Face packages.

"""


def main() -> None:
    source = read_source()

    write(GITHUB_PAGE, convert_github(source))

    SUBSTACK_DIR.mkdir(parents=True, exist_ok=True)
    copy_diagrams(SUBSTACK_DIR)
    write(SUBSTACK_DIR / "chapter1.substack.md", convert_substack(source))
    write(SUBSTACK_DIR / "README.md", substack_readme())
    shutil.copy2(SOURCE_PDF, SUBSTACK_DIR / "chapter1.pdf")

    HF_DIR.mkdir(parents=True, exist_ok=True)
    copy_diagrams(HF_DIR)
    write(HF_DIR / "README.md", convert_hugging_face(source))
    write(HF_DIR / "PUBLISHING_NOTES.md", hugging_face_notes())
    shutil.copy2(SOURCE_PDF, HF_DIR / "chapter1.pdf")

    write(MANIFEST, make_manifest())


if __name__ == "__main__":
    main()
