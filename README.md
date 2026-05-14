# constitutional_runtime

[English](./README.en.md) | [简体中文](./README.zh-CN.md)

[![Public Readiness](https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel/actions/workflows/public-check.yml/badge.svg)](https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel/actions/workflows/public-check.yml)
[![Deploy GitHub Pages](https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel/actions/workflows/pages.yml/badge.svg)](https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel/actions/workflows/pages.yml)

> Public mission, essays, diagrams, evidence indexes, and whitepaper drafts for a governed persistent multi-agent runtime.
>
> 面向受治理的持久化多智能体运行时的公开世界观、文章、图表、证据索引与白皮书草稿仓库。

## Choose A Language

| Language | Entry |
|---|---|
| English | [README.en.md](./README.en.md) |
| 简体中文 | [README.zh-CN.md](./README.zh-CN.md) |

## What This Repository Is

This is the public documentation and publication home for `constitutional_runtime`.

It argues that long-running AI work cannot become reliable only by giving one agent more memory, more tools, or a larger context window. It needs a governed runtime where mission ownership, authority relations, evidence gates, audit receipts, state transitions, and lawful closure are explicit runtime objects.

本仓库不是实现源码仓库。它公开的是概念、文章、白皮书路线、图表、引用证据与发布包；私有源码、私有 prompt、内部日志、凭证和运行痕迹不在这里公开。

## Start Reading

- [English overview](./README.en.md)
- [中文总览](./README.zh-CN.md)
- [Chapter 1 version map](./chapter1/)
- [Chapter 1 Chinese final PDF](./chapter1/final-draft-v3/package-v3/chapter1.pdf)
- [Chapter 1 English final PDF](./chapter1/final-draft-v3/package-v3-en/chapter1.pdf)
- [Citation evidence index](./chapter1/references/citation-evidence-index.md)
- [Wiki source](./.internal/unpublished/wiki/Home.md)
- [Public release setup](./.internal/repository/policy/PUBLIC_RELEASE.md)

## Public GitHub Configuration

The repository now includes active GitHub-facing configuration in `.github/`:

- bilingual issue template for documentation, citation, and publishing problems
- bilingual pull request template
- public readiness workflow
- GitHub Pages deployment workflow
- CODEOWNERS
- community health entry points for contributing, security, and support

Authoring and policy copies remain under `.internal/` so release checks can keep the public boundary explicit.

## Canonical Rule

For Chapter 1, each language edition's PDF is the final authority for both text and layout. If Markdown, GitHub Pages, Substack, Hugging Face, or Wiki editions diverge from the matching PDF, correct the platform edition against the PDF.

## Repository Boundary

Allowed here:

- public essays and whitepaper drafts
- final release packages
- diagrams and Mermaid sources
- citation indexes and source-evidence manifests
- public publishing configuration and templates

Not allowed here:

- private implementation source code
- credentials, API keys, tokens, or signing material
- private prompts, logs, traces, or sensitive user data
- raw third-party PDFs or snapshots without clear redistribution rights

Run the public readiness check before publishing:

```bash
make -f .internal/engineering/Makefile check
```
