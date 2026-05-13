# Contributing

Thanks for helping improve the public documentation.

This repository is public-facing. Keep contributions scoped to essays, release
packages, public diagrams, citation indexes, publishing formats, and whitepaper
drafts.

## Before Opening a Pull Request

Run:

```bash
make -f .internal/engineering/Makefile check
```

For Chapter 1 platform edits, regenerate the platform formats when the source
Markdown changes:

```bash
.internal/engineering/scripts/build_chapter1_platform_formats.py
```

## Public Boundary

Do not contribute:

- private implementation source code
- credentials, API keys, access tokens, signing keys, or local `.env` files
- private prompts, internal logs, unpublished traces, or sensitive user data
- raw third-party PDFs or snapshots without clear redistribution permission

## Evidence Updates

If you change a cited claim, update the citation evidence index in the same
pull request or explain why no evidence update is needed.

## Pull Request Expectations

- Explain what public surface changed.
- Note whether canonical PDFs, platform packages, or citation indexes changed.
- Include screenshots only when they help review rendered pages.
- Keep unrelated formatting churn out of the pull request.
