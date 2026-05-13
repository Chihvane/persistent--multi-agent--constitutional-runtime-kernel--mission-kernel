# Publishing

The first public release targets three surfaces:

- GitHub Pages
- Hugging Face
- Substack

## GitHub Pages

GitHub Pages is the canonical public source surface for the repository.

Required setup:

- repository visibility: public
- Pages source: GitHub Actions
- workflow: `.internal/engineering/github/workflows/pages.yml`
- landing page: `index.md`
- site config: `.internal/engineering/site/_config.yml`

Run:

```bash
make -f .internal/engineering/Makefile check
```

Then push to `main` and verify the `Deploy GitHub Pages` workflow.

## Hugging Face

Use the generated Hugging Face package as the project discovery surface:

- Chinese: `.internal/unpublished/publishing/chapter-01/hugging-face/`
- English: `.internal/unpublished/publishing/chapter-01/en/hugging-face/`

Each package includes a README, figure assets, publishing notes, and the matching
canonical PDF.

## Substack

Use the flattened Substack paste editions:

- Chinese: `.internal/unpublished/publishing/chapter-01/substack/chapter1.substack.md`
- English: `.internal/unpublished/publishing/chapter-01/en/substack/chapter1.substack.md`

Substack does not preserve custom CSS or pandoc div blocks. Upload the figure
PNGs manually and compare the final post against the matching PDF.

## Wiki

The version-controlled wiki source is in `.internal/unpublished/wiki/`. Publish it to GitHub Wiki
using `.internal/unpublished/publishing/wiki-sync.md`.
