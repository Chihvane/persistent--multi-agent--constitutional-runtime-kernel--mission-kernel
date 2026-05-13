# Substack Publishing Package (English)

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

<sub>Chihvane Xiang</sub>
