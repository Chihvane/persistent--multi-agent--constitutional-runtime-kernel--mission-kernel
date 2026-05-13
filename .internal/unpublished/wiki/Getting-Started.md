# Getting Started

`constitutional_runtime` studies how long-running AI work can be governed by a
runtime instead of being left to a single agent loop.

## Reading Order

1. Read the repository [README](../README.md) for the public mission and file map.
2. Read the [Series Outline](../.internal/unpublished/series/outline.md) to understand the chapter plan.
3. Read [Chapter 1](./Chapter-1.md), then the canonical PDF for the language you
   prefer.
4. Read the [Whitepaper Outline](../.internal/unpublished/whitepaper/outline.md) for the technical arc.
5. Use the [Glossary](../glossary.md) when terms become dense.

## Local Setup

No private environment is required to read or build the public docs.

```bash
make -f .internal/engineering/Makefile check
```

For local GitHub Pages preview:

```bash
ruby --version  # use Ruby 3.x; see .internal/engineering/site/.ruby-version
bundle install
bundle exec jekyll serve
```

The public environment template is `.internal/engineering/site/.env.example`. It contains only non-secret
publication metadata. Do not place real service credentials in committed files.

## What Is Canonical

For Chapter 1, the matching PDF is the final authority for both text and layout:

- Chinese: `chapter1/final-draft-v3/package-v3/chapter1.pdf`
- English: `chapter1/final-draft-v3/package-v3-en/chapter1.pdf`

If a web, Substack, or Hugging Face edition differs from the PDF, correct the
platform edition against the PDF.
