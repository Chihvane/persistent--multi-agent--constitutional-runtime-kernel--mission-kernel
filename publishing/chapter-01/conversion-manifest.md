# Chapter 1 Platform Conversion Manifest

Generated platform editions for Chapter 1 final v3.

## Canonical Source

- Canonical final PDF: `chapters/chapter-01/final/package-v3/chapter1.pdf`
- Source Markdown from the same package: `chapters/chapter-01/final/package-v3/chapter1.md`
- PDF SHA-256: `a5f6f08f61bcc2444b442b84f14ae100cb6bb86c6b679675f23288d6fe5fde3c`
- Markdown SHA-256: `8a6666a66ad69f9e639ef1bb9f89d7594fe9a540a61ea2ac267647b11aaf45fa`
- Diagrams copied: 10

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

