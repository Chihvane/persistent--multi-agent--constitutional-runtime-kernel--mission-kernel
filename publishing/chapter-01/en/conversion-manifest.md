# Chapter 1 Platform Conversion Manifest (English)

Generated platform editions for Chapter 1 final v3 (English).

## Canonical Source

- Canonical final PDF: `chapters/chapter-01/final/package-v3-en/chapter1.pdf`
- Source Markdown from the same package: `chapters/chapter-01/final/package-v3-en/chapter1.md`
- PDF SHA-256: `e4e240c77c1e876a477797ee5ac0283ab35a1fa98e0fae1adc6398b55f2b67f7`
- Markdown SHA-256: `d0cbf7dbc1a4093b0835272b04d0a2376d885237ca1dbaff6244efb88306a97f`
- Diagrams copied: 10

## Generated Outputs

- GitHub Pages: `chapters/chapter-01/final/en/github-pages.md`
- Substack: `publishing/chapter-01/en/substack/chapter1.substack.md`
- Substack notes: `publishing/chapter-01/en/substack/README.md`
- Hugging Face: `publishing/chapter-01/en/hugging-face/README.md`
- Hugging Face notes: `publishing/chapter-01/en/hugging-face/PUBLISHING_NOTES.md`

## Conversion Rules

- `chapter1.pdf` remains the final authority for layout and text.
- The conversion uses the final package Markdown instead of direct PDF text extraction because direct PDF extraction can introduce line-break, table, image, and punctuation loss.
- GitHub Pages keeps definition/example blocks as styled HTML containers.
- Substack flattens definition/example blocks into plain Markdown because Substack does not preserve custom CSS or pandoc divs; original block titles are retained.
- Hugging Face uses README-friendly Markdown with relative image assets and small caption lines.
- All ten diagram PNGs are preserved for Substack and Hugging Face packages.
- Generated text editions include the subtle author signature: Chihvane Xiang.

<sub>Chihvane Xiang</sub>
