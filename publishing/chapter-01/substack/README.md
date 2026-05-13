# Substack Publishing Package

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

