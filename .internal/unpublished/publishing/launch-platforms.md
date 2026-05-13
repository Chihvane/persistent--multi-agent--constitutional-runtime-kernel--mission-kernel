# Launch Platforms

Initial publication platforms:

- GitHub Pages
- GitHub Wiki
- Hugging Face
- Substack

## GitHub Pages

Use this repository as the canonical public source. GitHub Pages can render the Markdown structure directly through Jekyll.

Recommended launch path:

1. Publish the repository as a public docs repository.
2. Enable GitHub Pages from the main branch root.
3. Use `index.md` as the site landing page.
4. Use `chapter1/final-draft-v3/` as the Chapter 1 launch page.
5. Link `chapter1.pdf` as the canonical final artifact.

## GitHub Wiki

Use the wiki as the orientation layer for readers who want a guided map rather
than a file tree.

Recommended launch path:

1. Review `.internal/unpublished/wiki/`.
2. Run `make -f .internal/engineering/Makefile check`.
3. Enable Wiki in repository settings.
4. Publish the wiki source using `.internal/unpublished/publishing/wiki-sync.md`.
5. Keep the wiki focused on public mission, reading order, architecture concepts,
   citation evidence, and release checklists.

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
2. Confirm the public-readiness workflow passes.
3. Enable GitHub Pages.
4. Publish the GitHub Wiki.
5. Publish Chapter 1 final v3 landing page and PDF.
6. Publish the Hugging Face project summary linking to GitHub Pages.
7. Publish the Substack version prepared from the final v3 text.
