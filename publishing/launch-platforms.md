# Launch Platforms

Initial publication platforms:

- GitHub Pages
- Hugging Face
- Substack

## GitHub Pages

Use this repository as the canonical public source. GitHub Pages can render the Markdown structure directly through Jekyll.

Recommended launch path:

1. Publish the repository as a public docs repository.
2. Enable GitHub Pages from the main branch root.
3. Use `index.md` as the site landing page.
4. Use `chapters/chapter-01/final/` as the Chapter 1 launch page.
5. Link `chapter1.pdf` as the canonical final artifact.

## Hugging Face

Use Hugging Face as the AI-community discovery surface.

Recommended options:

- create a project/model/dataset profile README that links back to the GitHub Pages site
- publish a short project-facing summary that links to Chapter 1 final v3
- link the final PDF for readers who want the complete text and formatting

## Substack

Use Substack for serialized narrative distribution.

Recommended approach:

- prepare the post from `chapter1.md`, checked against `chapter1.pdf`
- manually convert pandoc div blocks into Substack callouts or blockquotes
- upload the diagram PNG files manually
- close the post with a pointer to the GitHub Pages final v3 landing page

## Launch Order

Suggested first-day order:

1. Push the public documentation repository.
2. Enable GitHub Pages.
3. Publish Chapter 1 final v3 landing page and PDF.
4. Publish the Hugging Face project summary linking to GitHub Pages.
5. Publish the Substack version prepared from the final v3 text.
