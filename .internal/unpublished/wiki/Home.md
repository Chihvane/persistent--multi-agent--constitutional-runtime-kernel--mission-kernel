# constitutional_runtime Wiki

Welcome to the public wiki for `constitutional_runtime`.

This repository is the public mission, article, and whitepaper home for a
governed multi-agent runtime project. The private implementation repository is
kept separate. This wiki explains how to read the public material, how the
runtime concepts fit together, and how to publish the public documentation
without leaking private implementation details.

## Start Here

- [Getting Started](./Getting-Started.md)
- [Core Architecture](./Architecture.md)
- [Chapter 1](./Chapter-1.md)
- [Citation Evidence](./Citation-Evidence.md)
- [Publishing Guide](./Publishing.md)
- [Public Release Checklist](./Public-Release-Checklist.md)

## Canonical Public Artifacts

- Series outline: `.internal/unpublished/series/outline.md`
- Chapter 1 final map: `chapter1/final-draft-v3/`
- Chinese Chapter 1 PDF: `chapter1/final-draft-v3/package-v3/chapter1.pdf`
- English Chapter 1 PDF: `chapter1/final-draft-v3/package-v3-en/chapter1.pdf`
- Whitepaper outline: `.internal/unpublished/whitepaper/outline.md`
- Public repository policy: `.internal/repository/policy/repo-policy.md`

## Public Boundary

Allowed in this public repository:

- essays, whitepaper drafts, and mission notes
- final PDF, Markdown, and DOCX release packages
- generated platform editions for GitHub Pages, Hugging Face, and Substack
- diagrams, Mermaid sources, citation indexes, and public evidence manifests
- public technical notes that do not reveal private implementation details

Not allowed:

- private implementation source code
- credentials, API keys, access tokens, or signing keys
- private prompts, internal logs, unpublished traces, or sensitive user data
- raw third-party PDFs or web snapshots unless redistribution rights are clear

Run `make -f .internal/engineering/Makefile check` before pushing public changes.
