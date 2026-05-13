---
layout: page
title: Public Release Setup
---

# Public Release Setup

This file records the configuration and environment expected before the
repository is made public.

## Repository Identity

- Repository slug:
  `Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel`
- Default branch: `main`
- Intended visibility: `public`
- Public site: GitHub Pages through GitHub Actions
- Private boundary: implementation/source repository remains separate

## Local Environment

No private runtime environment is required for this public documentation
repository.

Optional local preview:

```bash
ruby --version  # use Ruby 3.x; see .internal/engineering/site/.ruby-version
bundle install
bundle exec jekyll serve
```

Public metadata can be copied from `.internal/engineering/site/.env.example` into a local `.env` file if a
script needs it. Real service credentials must stay outside the repository.

## GitHub Settings

Set these after the repository is pushed:

- General -> Features: enable Issues and Wiki if they are part of the launch.
- Pages -> Build and deployment: select GitHub Actions.
- Actions -> General: allow GitHub Actions for this repository.
- Branches -> Branch protection: require the public-readiness workflow before
  merging to `main`.
- Pull requests: require at least one manual review for public release changes.

## Required Workflows

- `.internal/engineering/github/workflows/public-check.yml`: runs `make -f .internal/engineering/Makefile check` on pushes and pull
  requests.
- `.internal/engineering/github/workflows/pages.yml`: builds and deploys GitHub Pages.

## Launch Environment Variables

The committed `.internal/engineering/site/.env.example` contains only non-secret public metadata:

- public repository slug
- public site URL
- canonical Chapter 1 artifact paths
- optional public Hugging Face and Substack destination URLs

Do not commit real service credentials or local machine paths.

## Public Launch Gate

Run:

```bash
make -f .internal/engineering/Makefile check
git status --short
```

Then manually review the diff for:

- private implementation details
- sensitive operational history
- source files that should remain private
- raw third-party materials without redistribution rights
- broken links in README, wiki source, and platform packages

## First-Day Launch Order

1. Push the public documentation repository.
2. Confirm the public-readiness workflow passes.
3. Enable GitHub Pages through Actions.
4. Publish the GitHub Wiki from `.internal/unpublished/wiki/`.
5. Publish the Hugging Face package.
6. Publish the Substack article.
7. Link all public surfaces back to the GitHub Pages landing page.
