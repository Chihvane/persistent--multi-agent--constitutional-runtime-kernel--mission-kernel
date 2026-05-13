# Chapter 1 v3 Publishing Guide

Source package:

`chapters/chapter-01/final/package-v3/`

Canonical artifact:

`chapters/chapter-01/final/package-v3/chapter1.pdf`

The package README states that this PDF is the 15-page final layout with red definition boxes and green example blocks. Treat it as the final authority for both format and text.

## GitHub Pages

Recommended first launch:

1. Publish the Chapter 1 landing page at `chapters/chapter-01/final/`.
2. Link directly to `chapter1.pdf` as the canonical final artifact.
3. Link to `chapter1.md` as the full Markdown source, but do not treat the Markdown rendering as authoritative unless the pandoc div blocks are converted or styled correctly.
4. Keep the package README visible so readers can inspect the release notes.

Important rendering note:

The full Markdown uses pandoc div syntax for:

- `definition` blocks: red definition / structure-rule boxes
- `example` blocks: green scenario / analogy / example boxes

The Markdown also references pre-rendered PNG figures under `diagrams/`, so GitHub Pages does not need to render Mermaid at launch.

## Hugging Face

Recommended first launch:

1. Use `publishing/hugging-face-readme.md` as the short project README base.
2. Add links to the GitHub Pages landing page and `chapter1.pdf`.
3. Use the short project summary, not the full `chapter1.md`, as the Hugging Face profile surface.
4. Keep the source repository private; this public repository is the mission and documentation repository.

## Substack

Substack does not support pandoc divs or custom CSS.

Recommended first launch:

1. Use `chapter1.pdf` as the final text reference.
2. Paste from `chapter1.md`, but manually convert `definition` and `example` blocks into Substack callouts or blockquotes.
3. Upload the figure PNGs manually from `diagrams/`.
4. Replace local image paths such as `diagrams/fig_1_1.png` with Substack-hosted images.
5. Do not publish `chapter1_quickread.md` as the canonical v3 article unless it is refreshed against the v3 PDF; the package README says the quick-read edition still follows v2.

## Pre-Publish Checklist From Package README

- Read `chapter1.pdf` end to end and confirm red/green blocks render correctly.
- Pay special attention to section `1.12`.
- Check whether the `1.0 Opening` explanation of "who" matches your intended framing.
- Verify the 19 reference URLs before public launch.
- Review the Chapter 1 reference evidence package and confirm every cited reference is backed by the matrix.
- Review the `Memory vs Evidence` table in section `1.3`.
- Review the Mission Record field order in section `1.5`.
- Decide whether the quick-read version should be refreshed before being promoted.

Reference evidence:

- [Chapter 1 Reference Evidence](../chapters/chapter-01/references/)
- [Citation Evidence Index](../chapters/chapter-01/references/citation-evidence-index.md)

Generated platform formats:

- [GitHub Pages edition](../chapters/chapter-01/final/github-pages.md)
- [Substack package](./chapter-01/substack/)
- [Hugging Face package](./chapter-01/hugging-face/)
- [Conversion manifest](./chapter-01/conversion-manifest.md)

## Publication Decision

For launch day, publish in this order:

1. GitHub Pages landing page plus final PDF.
2. Hugging Face short project README linking back to GitHub Pages.
3. Substack article prepared from the final Markdown and checked against the final PDF.
