# Chapter 1 Platform Publishing Package

This directory contains generated platform-specific editions of Chapter 1.

Canonical source:

- `chapters/chapter-01/final/package-v3/chapter1.pdf`

Chinese generated outputs:

- [GitHub Pages edition](../../chapters/chapter-01/final/github-pages.md)
- [Substack package](./substack/)
- [Hugging Face package](./hugging-face/)
- [Conversion manifest](./conversion-manifest.md)

English generated outputs:

- [GitHub Pages edition](../../chapters/chapter-01/final/en/github-pages.md)
- [Substack package](./en/substack/)
- [Hugging Face package](./en/hugging-face/)
- [Conversion manifest](./en/conversion-manifest.md)

## Rules

- The final PDF remains the authority for both text and layout.
- The platform editions are generated from the final v3 package Markdown because direct PDF text extraction would introduce line breaks, table loss, and image loss.
- If a platform version diverges from the matching `chapter1.pdf`, correct the platform version against the PDF.

## Regenerate

Run:

```bash
scripts/build_chapter1_platform_formats.py
```
