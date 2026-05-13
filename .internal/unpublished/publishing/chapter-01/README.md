# Chapter 1 Platform Publishing Package

This directory contains generated platform-specific editions of Chapter 1.

<sub>Chihvane Xiang</sub>

Canonical source:

- `chapter1/final-draft-v3/package-v3/chapter1.pdf`

Chinese generated outputs:

- [GitHub Pages edition](../../chapter1/final-draft-v3/github-pages.md)
- [Substack package](./substack/)
- [Hugging Face package](./hugging-face/)
- [Conversion manifest](./conversion-manifest.md)

English generated outputs:

- [GitHub Pages edition](../../chapter1/final-draft-v3/en/github-pages.md)
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
.internal/engineering/scripts/build_chapter1_platform_formats.py
```
