# constitutional_runtime

Public mission, article, and whitepaper repository for **constitutional_runtime**, a governed multi-agent runtime project.

Repository name:

`persistent--multi-agent--constitutional-runtime-kernel--mission-kernel`

This repository is the publication home for the series:

**From Single-Agent OS to Constitutional Runtime: Why I Rebuilt My AI System**

The private implementation/source repository remains separate. This public repository contains essays, release packages, diagrams, citation evidence, publishing formats, and whitepaper drafts for `constitutional_runtime`.

## What This Project Argues

Long-running AI work does not fail only because models hallucinate, forget, or misuse tools. It also fails because the surrounding runtime often lacks the governance primitives required for accountable work over time:

- task ownership
- scoped authority
- evidence gates
- audit trails
- state-delta records
- lawful closure

`constitutional_runtime` explores a shift from a single-agent operating model to a **Constitutional Runtime**: a governance layer where agents are runtime participants, not the whole operating system.

## Start Here

- [Series Outline](./series/outline.md)
- [Chapter 1 Final Version Map](./chapters/chapter-01/final/)
- [Whitepaper Outline](./whitepaper/outline.md)
- [Glossary](./glossary.md)

## Chapter 1 Final

**Chapter 1:** Agent OS 的结构性失稳 / Structural Instability in Agent OS

**Subtitle:** Why long-running AI work needs task ownership, authority, audit, and lawful closure

The final Chapter 1 release has two canonical language editions. For each language, the PDF is the final authority for both text and layout.

| Edition | Canonical PDF | Web Edition | Platform Package |
|---|---|---|---|
| Chinese | [chapter1.pdf](./chapters/chapter-01/final/package-v3/chapter1.pdf) | [GitHub Pages Markdown](./chapters/chapter-01/final/github-pages.md) | [Publishing package](./publishing/chapter-01/) |
| English | [chapter1.pdf](./chapters/chapter-01/final/package-v3-en/chapter1.pdf) | [GitHub Pages Markdown](./chapters/chapter-01/final/en/github-pages.md) | [Publishing package](./publishing/chapter-01/en/) |

Source packages:

- [Chinese final package](./chapters/chapter-01/final/package-v3/)
- [English final package](./chapters/chapter-01/final/package-v3-en/)
- [Chapter 1 reference evidence](./chapters/chapter-01/references/)

## Platform Outputs

Generated publication formats are included for first-day release.

### GitHub Pages

- [Chinese GitHub Pages edition](./chapters/chapter-01/final/github-pages.md)
- [English GitHub Pages edition](./chapters/chapter-01/final/en/github-pages.md)
- Shared styling: [assets/main.scss](./assets/main.scss)

### Substack

- [Chinese Substack paste edition](./publishing/chapter-01/substack/chapter1.substack.md)
- [English Substack paste edition](./publishing/chapter-01/en/substack/chapter1.substack.md)

Substack does not preserve custom CSS or pandoc div blocks, so the Substack editions flatten definition/example boxes into plain Markdown and use explicit figure-upload markers.

### Hugging Face

- [Chinese Hugging Face README edition](./publishing/chapter-01/hugging-face/README.md)
- [English Hugging Face README edition](./publishing/chapter-01/en/hugging-face/README.md)

Each Hugging Face package includes the matching final PDF and figure assets.

## Regenerate Platform Formats

The platform editions are generated from the final package Markdown while the final PDFs remain canonical.

```bash
scripts/build_chapter1_platform_formats.py
```

Conversion manifests:

- [Chinese conversion manifest](./publishing/chapter-01/conversion-manifest.md)
- [English conversion manifest](./publishing/chapter-01/en/conversion-manifest.md)

## Reference Evidence

Chapter 1 is backed by a citation evidence matrix containing arXiv papers, web-source extracts, and source-to-claim mapping notes.

Public index:

- [Citation Evidence Index](./chapters/chapter-01/references/citation-evidence-index.md)
- [Reference Package Manifest](./chapters/chapter-01/references/reference-package-manifest.md)

The raw reference PDF corpus is intentionally not committed by default. This keeps the public repository clean and avoids ambiguous redistribution of full paper/web snapshots.

## Repository Map

```text
.
├── chapters/
│   └── chapter-01/
│       ├── final/
│       │   ├── package-v3/       Chinese final package
│       │   ├── package-v3-en/    English final package
│       │   ├── github-pages.md   Chinese web edition
│       │   └── en/               English final landing + web edition
│       └── references/           Citation evidence index
├── publishing/
│   ├── chapter-01/               Platform packages for Chapter 1
│   ├── chapter-01-v3-guide.md    Launch guide
│   └── launch-platforms.md       Platform strategy
├── series/
│   └── outline.md
├── whitepaper/
│   ├── outline.md
│   └── 00-abstract.md
├── scripts/
│   ├── build_chapter1_platform_formats.py
│   └── check_public_repo.sh
└── assets/
    └── main.scss
```

## Public Repository Policy

Allowed here:

- essays and publishing drafts
- final PDF/Markdown/DOCX release packages
- diagrams and Mermaid sources
- citation indexes and manifests
- whitepaper outlines and public technical notes

Do not add:

- private implementation source code
- credentials, API keys, tokens, or secrets
- private prompts or internal logs
- unpublished operational traces
- sensitive user data

Before publishing or pushing:

```bash
make check
```

## Current Status

- Chapter 1 Chinese final package: complete
- Chapter 1 English final package: complete
- GitHub Pages editions: generated
- Substack paste editions: generated
- Hugging Face README editions: generated
- Chapter 1 reference evidence index: complete
- Full whitepaper: outline stage
- Chapters 2-8: planned
