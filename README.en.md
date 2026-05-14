# constitutional_runtime

[English](./README.en.md) | [简体中文](./README.zh-CN.md)

[![Public Readiness](https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel/actions/workflows/public-check.yml/badge.svg)](https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel/actions/workflows/public-check.yml)
[![Deploy GitHub Pages](https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel/actions/workflows/pages.yml/badge.svg)](https://github.com/Chihvane/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel/actions/workflows/pages.yml)

> A public worldview, concept system, article series, diagrams, evidence index, and whitepaper repository for governed persistent multi-agent runtime architecture.

**Series:** *From Single-Agent OS to Constitutional Runtime: Why I Rebuilt My AI System*

**Repository role:** worldview, concept vocabulary, technical whitepaper, public articles, diagrams, citation evidence, and publication packages.

**Implementation status:** this is not a public implementation-source repository.

**Public boundary:** concepts can be public; private source code, private prompts, internal logs, credentials, and operational traces are not published here.

Repository slug:

```text
persistent--multi-agent--constitutional-runtime-kernel--mission-kernel
```

## One-Sentence Thesis

Long-running AI work cannot become reliable only by giving a single agent more memory, more tools, or a larger context window. It needs a governed runtime where **mission ownership, authority relations, evidence gates, state transitions, audit receipts, and lawful closure** become explicit runtime objects.

## One-Sentence Definition

**Constitutional Runtime is a governed runtime architecture for persistent multi-agent task execution. It separates capability from ownership, role from authority, memory from evidence, and local completion from lawful closure.**

Its goal is not to create "more agents." Its goal is to preserve, across long-running work:

```text
who owns the mission
who may change it
who is only supporting
which memory is admissible evidence
which capability invocation is authorized
which state change is valid
which audit condition blocks progress
when a mission is lawfully closed
```

## What This Repository Contains

This repository develops and publishes:

- the core worldview for `constitutional_runtime`
- vocabulary for Constitutional Runtime, Constitutional Kernel, and Mission Kernel
- technical whitepaper direction
- public chapters in Chinese and English
- diagrams and Mermaid source files
- citation evidence indexes
- GitHub Pages, GitHub Wiki, Substack, and Hugging Face publication packages
- public release and repository hygiene configuration

It does not contain:

- implementation source code
- private runtime state
- internal prompts or logs
- credentials, API keys, tokens, or signing material
- unpublished operational traces
- sensitive user data

When this repository discusses implementation, it discusses public architecture, concepts, invariants, and research direction. It does not mirror the private source tree.

## Core Distinctions

```text
Capability is can.
Authority is may.

Memory is recall.
Evidence is admissibility.

Done is local completion.
Closure is lawful mission termination.
```

In this frame:

- **Capability** means a participant, tool, channel, or model can perform an action.
- **Authority** means the action is permitted in the current mission and governance context.
- **Memory** means information has been saved or recalled.
- **Evidence** means information has source, scope, admissibility status, and can be used for the current judgment.
- **Done** means a local action appears complete.
- **Closure** means a mission lifecycle has been lawfully terminated with evidence, receipts, residual-risk notes, and acceptance basis.

## Three Adjudicating Spines

### CR: Constitutional Runtime

Constitutional Runtime is the surface of current truth and lawful transition. It separates:

```text
canonical state
side evidence
projection
archive
readiness
closure
```

CR should prevent the system from continuing when it cannot prove where it currently stands.

### CK: Constitutional Kernel

Constitutional Kernel is the authority-law layer. It defines typed authority relations such as:

```text
ownership
support
consult
audit
routing
escalation
threshold holding
state-change authority
closure authority
```

CK decides whether an actor may perform a state-changing action, whether a handoff actually transfers ownership, and whether a claimed authority is lawful.

### MK: Mission Kernel

Mission Kernel turns user intent into governed mission lifecycle objects. A minimal lifecycle can be expressed as:

```text
raw_request
-> mission_envelope
-> authority_relation_check
-> routing_decision
-> participant selection
-> capability_binding
-> execution_receipt
-> evidence_admission
-> audit_receipt
-> state_delta_receipt
-> closure_receipt or honest_stop
```

MK preserves the difference between a conversation turn and a governed mission.

## Eight-Axis Architecture

| Axis | Name | Runtime question |
|---|---|---|
| CR | Constitutional Runtime | What is the current lawful truth, and may the system move forward? |
| CK | Constitutional Kernel | Who has authority to do what? |
| MK | Mission Kernel | How does a request become a governed mission? |
| AG | Agent Dimension | Which runtime participants can carry typed roles? |
| CP | Capability / Ingress-Egress Plane | Which tools, channels, gateways, and providers may be used within scope? |
| SM | State / Memory / Evidence Plane | What is memory, what is evidence, and what is canonical state? |
| DG | Anti-Drift / Audit / Governance Plane | How are drift, audit failures, and honest-stop conditions detected and recorded? |
| EP | Engineering Process / Delivery Plane | How are work, evidence, return packages, and handoffs made reproducible? |

The three adjudicating spines are:

```text
CR = current truth and lawful transition
CK = executable authority law
MK = governed mission lifecycle
```

The five supporting planes are:

```text
AG = runtime participants
CP = bounded capabilities and ingress / egress
SM = memory, state, evidence, and receipts
DG = anti-drift, audit, honest stop, validation
EP = engineering delivery, handoff, return bundles
```

## Mission-Centered Organization

The basic unit of governance is not the agent. It is the mission.

```text
Agent is not the unit of governance.
Mission is the unit of governance.
Agent is a runtime participant inside a governed mission.
```

This does not require the user interface to stop being conversational.

```text
User-facing interface remains conversational.
Runtime-facing representation becomes mission-centered.
```

The system should compile natural-language input into a typed mission object before execution.

## Chapter 1 Final

**Chapter 1:** Structural Instability in Agent OS

**Subtitle:** Why long-running AI work needs task ownership, authority, audit, and lawful closure

**Date:** 2026-05-14

Chapter 1 has two canonical language editions. In each edition, the PDF is the final authority for text and layout.

| Edition | Canonical PDF | Web Edition | Package |
|---|---|---|---|
| Chinese | [chapter1.pdf](./chapter1/final-draft-v3/package-v3/chapter1.pdf) | [GitHub Pages Markdown](./chapter1/final-draft-v3/github-pages.md) | [Publishing package](./chapter1/final-draft-v3/package-v3/) |
| English | [chapter1.pdf](./chapter1/final-draft-v3/package-v3-en/chapter1.pdf) | [GitHub Pages Markdown](./chapter1/final-draft-v3/en/github-pages.md) | [Publishing package](./chapter1/final-draft-v3/package-v3-en/) |

Chapter 1 frames structural instability through eight failure modes:

| Failure mode | Runtime interpretation |
|---|---|
| Task ownership drift | The system keeps running but no longer preserves who owns the mission. |
| Support becomes ownership | Support work quietly turns into direction control. |
| Memory becomes evidence | Recalled content is treated as admissible current evidence. |
| Persona becomes authority | Role language is mistaken for runtime power. |
| Delegation becomes authorization | Handoff is mistaken for permission transfer. |
| Global chat becomes context pollution | Multiple actors speak without preserved authority boundaries. |
| Tool calling becomes capability governance | Tool access is mistaken for scoped permission. |
| Done becomes closure | Local completion is mistaken for lawful mission termination. |

## Reading Order

Recommended path:

1. [Language gateway](./README.md)
2. [Chapter 1 Version Map](./chapter1/)
3. [Chapter 1 Final v3](./chapter1/final-draft-v3/)
4. [Chapter 1 Reference Evidence](./chapter1/references/)
5. [Series Outline](./.internal/unpublished/series/outline.md)
6. [Whitepaper Outline](./.internal/unpublished/whitepaper/outline.md)
7. [Wiki Home](./.internal/unpublished/wiki/Home.md)

## Public GitHub Configuration

This repository uses the same public-facing conventions readers expect from active open repositories:

- root README language switch: [English](./README.en.md) / [简体中文](./README.zh-CN.md)
- active GitHub issue template: [.github/ISSUE_TEMPLATE/docs_issue.yml](./.github/ISSUE_TEMPLATE/docs_issue.yml)
- active pull request template: [.github/pull_request_template.md](./.github/pull_request_template.md)
- active public readiness workflow: [.github/workflows/public-check.yml](./.github/workflows/public-check.yml)
- active GitHub Pages workflow: [.github/workflows/pages.yml](./.github/workflows/pages.yml)
- CODEOWNERS: [.github/CODEOWNERS](./.github/CODEOWNERS)
- public release setup: [.internal/repository/policy/PUBLIC_RELEASE.md](./.internal/repository/policy/PUBLIC_RELEASE.md)

Run the public readiness check before publishing or opening release-oriented pull requests:

```bash
make -f .internal/engineering/Makefile check
```

## Repository Map

```text
.
├── README.md
├── README.en.md
├── README.zh-CN.md
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   ├── pull_request_template.md
│   └── CODEOWNERS
├── chapter1/
│   ├── README.md
│   ├── README.zh-CN.md
│   ├── final-draft-v3/
│   │   ├── package-v3/
│   │   ├── package-v3-en/
│   │   ├── github-pages.md
│   │   └── en/
│   ├── references/
│   ├── en/
│   └── zh/
└── .internal/
    ├── engineering/
    ├── repository/
    ├── unpublished/
    └── local/
```

The root level is the public entry. `.github/` contains active GitHub configuration. `.internal/engineering/` contains engineering and publication automation. `.internal/unpublished/` contains unpublished source material. `.internal/repository/` contains governance, legal, and concept-support files. `.internal/local/` is for ignored local cache only.

## Public Policy

Allowed here:

- essays and publishing drafts
- final PDF, Markdown, and DOCX release packages
- diagrams and Mermaid sources
- citation indexes and manifests
- glossary entries and concept explanations
- whitepaper outlines and public technical notes
- GitHub Wiki source pages
- public publishing configuration and templates

Do not add:

- private implementation source code
- credentials, API keys, tokens, or secrets
- private prompts or internal logs
- unpublished operational traces
- sensitive user data
- raw third-party PDFs or snapshots without clear redistribution rights

## Project Maturity

This repository should not claim that a full runtime is already complete.

Careful public wording:

```text
The project proposes and documents a governed runtime architecture for persistent multi-agent task execution.
It has a mature conceptual frame around CR, CK, and MK.
It treats authority relations, mission lifecycle, evidence admission, audit, and closure as explicit runtime objects.
Some source-side components may exist as scaffolds or executable research surfaces.
The system still requires controlled taskflow tests, schema hardening, runtime validation, and public evidence packaging before v1.0 claims.
```

Short version:

```text
Not a finished v1.0 product.
Not a public source-code release.
Not a generic agent framework.
Not a roleplay/persona project.
A public architecture, article, and whitepaper repository for a governed persistent multi-agent runtime.
```

## Minimal Glossary

| Term | Meaning |
|---|---|
| Agent OS | A single-agent operating model where one assistant manages intent, planning, tools, execution, memory, and closure through a conversational loop. |
| Constitutional Runtime | A governed runtime layer that preserves current truth, evidence gates, authority boundaries, audit receipts, state transitions, and lawful closure. |
| Constitutional Kernel | The authority-law layer that decides who has authority to do what. |
| Mission Kernel | The lifecycle layer that turns requests into governed mission objects. |
| Mission | A task object with owner, authority, route, evidence, state-delta expectations, required receipts, and closure conditions. |
| Root Owner | The highest explicit human authority in the concept system. |
| Scoped Capability | A permission grant bounded by actor, mission, artifact, tool, action, environment, and time. |
| Evidence Gate | The process through which memory or produced information becomes admissible evidence for current mission judgment. |
| State Delta | A recorded and authorized change to canonical system state. |
| Audit Receipt | A record of review, validation, rejection, dissent, or acceptance. |
| Closure Receipt | A verifiable record that a mission has been lawfully closed. |
| Honest Stop | A lawful runtime outcome where the system refuses to continue because evidence, authority, state, or closure conditions are insufficient. |

## License / Reuse

Reuse terms are recorded in [.internal/repository/legal/LICENSE.md](./.internal/repository/legal/LICENSE.md). Until broader reuse rights are explicitly granted, treat this repository as public documentation and whitepaper draft material. When citing the project, cite Chapter 1's canonical PDFs or GitHub Pages editions.
