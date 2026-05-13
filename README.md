# constitutional_runtime

> 一个面向持久化多智能体运行时的公开世界观、概念系统、系列文章与技术白皮书仓库。

**系列:** *From Single-Agent OS to Constitutional Runtime: Why I Rebuilt My AI System*

**仓库角色:** 世界观、概念词汇、技术白皮书、公开文章、图表、引用证据与发布包

**实现状态:** 本仓库不是实现源码仓库

**公开边界:** 概念可以公开；私有源码、私有 prompt、内部日志、凭证与运行痕迹不在本仓库公开

仓库名：

`persistent--multi-agent--constitutional-runtime-kernel--mission-kernel`

## 一句话论点

长期运行的 AI 工作，不能只靠给单个 agent 更多记忆、更多工具或更大的上下文窗口来变得可靠。它需要一个受治理的运行时，使 **mission ownership、authority relations、evidence gates、state transitions、audit receipts 与 lawful closure** 成为显式的运行时对象。

## 一句话定义

**Constitutional Runtime 是一种用于持久化多智能体任务执行的受治理运行时架构。它将 capability 与 ownership、role 与 authority、memory 与 evidence、local completion 与 lawful closure 分开。**

它的目的不是制造“更多 agent”，而是让长期 AI 工作持续保存：

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

## 这个仓库是什么

这是 `constitutional_runtime` 的公开概念与白皮书主仓库。

它用于发展和发布：

- 项目的核心世界观
- Constitutional Runtime、Constitutional Kernel、Mission Kernel 的概念词汇
- 技术白皮书路线
- 中英文公开章节
- 图表与 Mermaid 源文件
- 引用证据索引
- GitHub Pages、GitHub Wiki、Substack、Hugging Face 发布包
- 公开发布与仓库卫生配置

它不包含：

- 实现源码
- 私有运行时状态
- 内部 prompt 或日志
- credentials、API keys、tokens、签名材料
- 未公开运行痕迹
- 敏感用户数据

当本仓库讨论实现时，只讨论公开架构、概念、不变量与研究方向；它不会镜像私有源码树。

## 从内部世界观到公开工程语言

项目内部使用 command-chain、lineage、doctrine 这类隐喻来帮助理解大型多智能体系统的组织关系。本公开仓库将这些隐喻翻译为中性的工程语言。

公开链条是：

```text
constitutional power
-> typed authority role
-> runtime-bound participant
```

被禁止的链条是：

```text
persona shell
-> perceived role
-> assumed authority
```

这个区分非常关键。一个被命名或有风格的参与者，可以帮助人理解它的功能，但它不是 authority 的来源。在公开写作中，每个参与者都应被描述为中性的工程角色。

推荐的公开术语：

| Internal function | Public engineering term |
|---|---|
| final operator-facing authority | Root Owner / Assignment Authority |
| task distribution and sequencing | Routing Coordinator |
| synthesis and interpretation | Synthesis Node |
| uncertainty-preserving reconnaissance | Recon Node |
| embedded review and discipline interruption | Embedded Audit Node |
| pre-task signal holding | Threshold Holder |
| tool / provider / channel access | Capability Gateway |
| evidence qualification | Evidence Gate |
| lawful task termination | Closure Authority |
| execution participant | Execution Actor |

内部世界观可以作为 mnemonic，但公开架构由 typed roles、authority relations、receipts、validators 与 evidence gates 治理。

## 为什么需要这个项目

大多数 agent 系统已经具备有用的能力：

- memory
- tool use
- workflow execution
- sub-agent delegation
- background execution
- provider routing
- channel and gateway integration

这些能力很重要，但它们并不会自动回答长期 AI 工作中的治理问题：

```text
Who owns this mission?
Who requested it?
Who has authority to change it?
Who is only supporting?
Which memory item is admissible evidence?
Which tool call was authorized?
What state changed?
Who audited the change?
When is the mission lawfully closed?
```

本项目认为，严肃的持久化 AI 工作需要一个能显式回答这些问题的运行时。目标不是“更多 agent”。目标是让长期工作具备可追责性。

## 核心区分

```text
Capability is can.
Authority is may.

Memory is recall.
Evidence is admissibility.

Done is local completion.
Closure is lawful mission termination.
```

在这个框架里：

- **Capability** 指参与者、工具、通道或模型能够执行某个动作。
- **Authority** 指该动作在当前 mission 与治理上下文中被允许。
- **Memory** 指被保存或回忆的信息。
- **Evidence** 指带有来源、范围和准入状态、可用于当前判断的信息。
- **Done** 指某个局部动作看起来完成了。
- **Closure** 指 mission 生命周期在证据、receipt、残余风险说明与验收依据下被合法终止。

## 五个核心分离

### 1. Capability 不等于 Ownership

一个参与者可能可以搜索、写作、运行代码、调用 provider 或访问 gateway。但这不意味着它 owns the mission。

```text
Capability says: what can this node do?
Ownership asks: who has authority to change this mission?
```

### 2. Role 不等于 Authority

一个参与者可以被标记为 reviewer、researcher、router 或 executor。但标签不授予 authority。

```text
Role helps humans read the system.
Authority controls what the runtime may accept.
```

### 3. Collaboration 不等于 Organization

许多 agents 在同一个地方发言，并不等于组织已经形成。真正的组织知道谁进入 mission、为什么进入、带着什么 authority、处于什么 phase、留下了什么 receipt。

```text
Global chat records who said what.
A governed mission records who had authority to do what.
```

### 4. Memory 不等于 Evidence

被记住的内容不自动成为 admissible evidence。

```text
Memory is recall.
Evidence is admissibility.
```

一个 memory item 需要 source、time、scope、type、confidence、validation 与 authority，才可以影响 canonical state。

### 5. Done 不等于 Closure

一个局部执行步骤可以 done，但 mission 仍然 open。

```text
Done is local completion.
Closure is lawful mission termination.
```

Closure 需要 accepted evidence、state-delta receipts、unresolved-issue handling、audit status 与 closure authority。

## 世界观

`constitutional_runtime` 将 agents 视为受治理的行动者，而不是操作系统本身。

围绕 agent 的运行时必须保存：

- sovereignty：谁拥有最终权威
- mandate：每个行动者负责什么
- relation：某个行动者是在 owner、support、audit、route，还是 advise
- capability：哪些工具与通道可以在作用域内使用
- evidence：什么可以用于当前判断
- state：当前 canonical state 是什么
- audit：发生了什么、基于什么 authority、结果是什么
- closure：工作何时可以合法停止

这个世界观本质上是 anti-drift 的：

- support is not ownership
- recommendation is not assignment
- routing is not sovereignty
- audit is not seizure
- persona is not law
- memory is not evidence
- tool access is not permission
- activity is not progress
- completion is not closure

项目使用 command、mission、doctrine、runtime-law 这类语言作为设计语言。重点不是角色扮演，而是让 authority、responsibility 与 closure 变得清晰、可检查、可追责。

## 三条裁决主脊

### CR: Constitutional Runtime

Constitutional Runtime 是 current-truth 与 lawful-transition 的表面。

它区分：

```text
canonical state
side evidence
projection
archive
readiness
closure
```

CR 应该阻止系统在无法证明“当前自己处于何处”时继续行动。

### CK: Constitutional Kernel

Constitutional Kernel 是 authority-law 层。

它定义类型化的 authority relations，例如：

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

CK 决定某个行动者是否可以执行 state-changing action，某次 handoff 是否真的转移 ownership，以及某个被声称的 authority 是否合法。

### MK: Mission Kernel

Mission Kernel 将用户意图转化为受治理的 mission lifecycle objects。

一个最小 lifecycle 可以表达为：

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

MK 保存 conversation turn 与 mission 之间的区别。

## 八轴架构

更大的架构由八条工程轴组成。

| Axis | Name | Runtime question |
|---|---|---|
| CR | Constitutional Runtime | 当前合法真相是什么，系统能否合法前进？ |
| CK | Constitutional Kernel | 谁有 authority 做什么？ |
| MK | Mission Kernel | 一个请求如何变成受治理的 mission？ |
| AG | Agent Dimension | 哪些运行时参与者可以承载类型化角色？ |
| CP | Capability / Ingress-Egress Plane | 哪些工具、通道、gateway 与 provider 可以在作用域内使用？ |
| SM | State / Memory / Evidence Plane | 什么是 memory，什么是 evidence，什么是 canonical state？ |
| DG | Anti-Drift / Audit / Governance Plane | drift 如何被发现、阻止与记录？ |
| EP | Engineering Process / Delivery Plane | 工作、证据、return package 与 handoff 如何可复现？ |

这些轴不是 personality。它们是工程责任。

三条轴是裁决主脊：

```text
CR = current truth and lawful transition
CK = executable authority law
MK = governed mission lifecycle
```

五条轴是支撑平面：

```text
AG = runtime participants
CP = bounded capabilities and ingress / egress
SM = memory, state, evidence, and receipts
DG = anti-drift, audit, honest stop, validation
EP = engineering delivery, handoff, return bundles
```

## 核心运行流

受治理任务不应直接进入 execution。它应先通过 mission lifecycle。

```text
1. Root Owner input / root request
2. Task Feed captures raw request
3. CR checks current truth and no-touch boundaries
4. MK creates mission_envelope
5. CK evaluates authority relations
6. MK selects route, company path, or temporary council
7. CP binds eligible runtime endpoints / tools
8. AG participants execute authorized mission slices
9. SM records evidence, receipts, and state deltas
10. DG validates anti-drift and honest-stop conditions
11. MK evaluates closure conditions
12. CR updates canonical state only if lawful transition is admissible
13. EP packages evidence, audit, delivery, and handoff artifacts
```

这不是普通 agent loop。它更接近：

```text
truth-state machine
+ authority adjudication layer
+ mission lifecycle layer
+ execution substrate
+ evidence ledger
+ audit / delivery pipeline
```

## 八轴分工

### CR: Current Truth Runtime

CR 维护系统的当前合法表面：

```text
canonical state
truth gateway
truth floor
front-door read order
lawful transition gate
evidence admission
state promotion / non-promotion receipt
honest-stop basis
```

CR 不是 memory store、dashboard、archive、workflow engine 或 gateway。它询问：什么是 current，什么只是 side evidence，什么只是 projection，什么是 historical archive，什么 transition 是 lawful，需要什么 receipt。

### CK: Authority Kernel

CK 是 executable authority law。它不是 persona manager、role prompt、style guide 或 ethics slogan。

CK 询问：谁是 owner，谁只是 support，谁可以 route，谁可以 audit，谁可以 escalate，谁可以写 state delta，谁可以 close，某个 requested act 是否被授权，适用哪个 invariant，需要什么 receipt。

核心 invariants 包括：

```text
support_no_ownership
routing_no_sovereignty
audit_no_seizure
threshold_holding_no_activation
persona_not_law_source
owner_change_requires_receipt
readiness_not_closure
memory_not_evidence
done_not_closure
```

### MK: Mission Lifecycle Kernel

MK 不是普通 task queue。

Task queue 问：

```text
What tasks exist?
Who is assigned?
What is the status?
```

Mission Kernel 问：

```text
What is the mission?
Who requested it?
Who owns it?
Who can change it?
Who is support only?
What route is lawful?
What evidence is required?
What state delta is expected?
Which audit conditions apply?
When can it close?
```

### AG: Agent Dimension

AG 表示 runtime-bound participants。participant 不是 law source，而是在 mission 内承载 typed role 的有边界执行表面。

核心规则：

```text
agent_id != persona
typed_role != authority
runtime_binding != ownership
authority_relation is still adjudicated by CK
```

### CP: Capability / Ingress-Egress Plane

CP 管理内部和外部 capability exposure，包括 gateway、tool registry、provider routing、MCP / adapter surfaces、sandbox policy、channel ingress、egress control、capability manifests 与 capability invocation receipts。

核心规则：

```text
Gateway is ingress / egress.
Gateway is not sovereign center.
Tool access is capability.
Tool access is not mission permission.
```

每一次有意义的 capability invocation 都应绑定 mission、actor、typed role、capability、authority basis、input/output reference、side-effect scope 与 receipt。

### SM: State / Memory / Evidence Plane

SM 分离 recall 与 admissibility。它维护 memory item、evidence item、evidence admissibility record、state snapshot receipt、state delta proposal、state delta receipt、non-promotion receipt、projection record、archive record 与 receipt ledger。

核心规则：

```text
remembered content can enter context;
only admitted evidence can affect judgment;
only authorized state_delta_receipt can alter canonical state.
```

### DG: Anti-Drift / Audit / Governance Plane

DG 是监督治理平面，用于发现并记录 semantic drift、reasoning drift、context drift、coordination drift、authority drift、evidence drift、temporal drift、receipt drift 与 closure drift。

DG 不是全知监督者。它是 runtime audit and validation plane。

### EP: Engineering Process / Delivery Plane

EP 将内部运行时工作转化为可复现的外部 artifacts，例如 return bundle、publication package、handoff pack、manifest、source/evidence snapshot index、validation report、CI attestation、unresolved issue list 与 next-thread continuity notes。

EP 本身不改变 truth。它携带 proof，但不成为 proof。

核心规则：

```text
delivery package transports evidence;
CR decides current truth;
CK decides authority;
MK decides mission closure.
```

## 概念对象模型

白皮书路线正在走向类型化 runtime contracts。计划中的公开对象词汇包括：

| Object | Purpose |
|---|---|
| `mission_envelope` | 捕获用户意图、scope、owner、acceptance criteria 与初始 authority context。 |
| `authority_relation` | 记录行动者是在 own、support、audit、route、consult、escalate，还是持有 threshold authority。 |
| `authority_decision_receipt` | 说明某个动作为何被允许、拒绝、升级或延迟。 |
| `routing_decision` | 说明某个 mission 或 subtask 为什么被路由给特定参与者或群体。 |
| `capability_binding_receipt` | 将工具、provider、channel 或 workspace 以 scoped permission 绑定到 mission。 |
| `capability_invocation_receipt` | 记录某次具体工具或 gateway 使用及其 authority context。 |
| `evidence_item` | 表示带有 source、provenance、scope、freshness 与 admissibility status 的信息。 |
| `evidence_admissibility_record` | 说明 memory 或产物为什么可以成为当前 evidence。 |
| `state_delta_receipt` | 记录一次被授权的 canonical state 变更。 |
| `audit_receipt` | 记录 review、validation、rejection、dissent 或 acceptance。 |
| `honest_stop_receipt` | 记录系统因 evidence、authority、capability 或 closure 条件不足而合法停止。 |
| `closure_receipt` | 记录带有 evidence、checks、residual risk 与 acceptance basis 的合法 mission termination。 |
| `return_bundle` | 将 outputs、evidence、receipts 与 next-step guidance 打包用于 review 或 handoff。 |
| `handoff_pack` | 以 scope、owner、evidence、risk 与 open questions 转移有边界的工作。 |

最强设计原则是：

```text
Every state-changing act must leave a receipt.
Every refusal to change state should also leave a receipt.
```

## Mission-Centered Organization

基本治理单位不是 agent，而是 mission。

```text
Agent is not the unit of governance.
Mission is the unit of governance.
Agent is a runtime participant inside a governed mission.
```

这不改变用户界面。用户仍然可以自然对话。

```text
User-facing interface remains conversational.
Runtime-facing representation becomes mission-centered.
```

系统应该在 execution 前将自然语言输入编译为 typed mission object。

## Company Routes 与 Temporary Councils

不是每个任务都需要 temporary council。

已知、低风险、领域明确的任务，可以走稳定 company route 或普通 execution chain。当 mission 跨领域、模糊、高风险、audit-sensitive，或需要多个 authority checks 时，temporary council 才合适。

| Mission type | Recommended route |
|---|---|
| Known domain, clear owner, low risk | company_route / standard execution path |
| Unclear request, missing evidence | recon_or_hold_route |
| Cross-domain task | routed multi-participant path |
| High-risk state change | embedded_audit_route |
| Conflicting evidence or authority ambiguity | temporary_council |
| Closure-sensitive task | closure_authority_review |

Temporary councils 是 mission-scoped。它们为一个 mission 形成，并在 closure 或 honest stop 后解散。

## Truth Surfaces

这个世界观将 present-tense truth 与周边上下文分开。

| Surface class | Public meaning |
|---|---|
| Sovereign truth | 当前权威 front door，系统可据此判断 present-tense state。 |
| Canonical acceptance | 可以承载 acceptance、rejection、closure 或 floor movement 的表面。 |
| Bounded projection | 真实 artifact 或 proposal，但尚未被提升为 current truth。 |
| Helper surface | 支持 routing、explanation 或 visibility，但不定义 truth。 |
| Mirror | 兼容或反射表面，不得高于 canonical front door。 |
| Archive | 为 provenance 保存的历史 evidence，不是当前 authority。 |

重要规则很简单：

```text
Do not start from the loudest artifact.
Start from the lawful current truth.
```

## Root Owner 原则

Root Owner 是概念系统中最高的显式人类 authority。

Root Owner authority 不是不可见的 bypass。合法 override 必须是显式、可审计、有作用域、有边界的。它应声明：

- target
- scope
- reason
- audit references
- emitted evidence
- action class

Root Owner instruction 可以为 request category、mission pause、mission redirect 或 mission termination 提供依据。它不会自动改写 constitutional law，不会自动 retarget sovereign bindings，不会自动授权 destructive mutation，也不会把 override authority 转移给其他行动者。

## Chapter 1 Final

**Chapter 1:** Agent OS 的结构性失稳 / Structural Instability in Agent OS

**Subtitle:** Why long-running AI work needs task ownership, authority, audit, and lawful closure

**Date:** 2026-05-14

Chapter 1 final release 有两个 canonical language editions。每个语言版本中，PDF 是文本与排版的最终权威。

| Edition | Canonical PDF | Web Edition | Platform Package |
|---|---|---|---|
| Chinese | [chapter1.pdf](./chapter1/final-draft-v3/package-v3/chapter1.pdf) | [GitHub Pages Markdown](./chapter1/final-draft-v3/github-pages.md) | [Publishing package](./.internal/unpublished/publishing/chapter-01/) |
| English | [chapter1.pdf](./chapter1/final-draft-v3/package-v3-en/chapter1.pdf) | [GitHub Pages Markdown](./chapter1/final-draft-v3/en/github-pages.md) | [Publishing package](./.internal/unpublished/publishing/chapter-01/en/) |

Source packages:

- [Chinese final package](./chapter1/final-draft-v3/package-v3/)
- [English final package](./chapter1/final-draft-v3/package-v3-en/)
- [Chapter 1 reference evidence](./chapter1/references/)

Chapter 1 将结构性失稳归纳为八类 failure modes：

| Failure mode | Runtime interpretation |
|---|---|
| Task ownership drift | 系统继续运行，但不再保存谁真正 owns the mission。 |
| Support becomes ownership | 辅助工作悄悄变成方向控制。 |
| Memory becomes evidence | 被回忆的内容被当成当前 admissible evidence。 |
| Persona becomes authority | 角色语言被误认为 runtime power。 |
| Delegation becomes authorization | handoff 被误认为 permission transfer。 |
| Global chat becomes context pollution | 多个行动者发言，但 authority boundaries 没有被保存。 |
| Tool calling becomes capability governance | 拥有工具被误认为拥有 scoped permission。 |
| Done becomes closure | 局部完成被误认为 lawful mission termination。 |

## 阅读顺序

推荐阅读顺序：

1. [Series Outline](./.internal/unpublished/series/outline.md)
2. [Chapter 1 Version Map](./chapter1/)
3. [Chapter 1 Final v3](./chapter1/final-draft-v3/)
4. [Chapter 1 Reference Evidence](./chapter1/references/)
5. [Whitepaper Outline](./.internal/unpublished/whitepaper/outline.md)
6. [Glossary](./.internal/repository/concepts/glossary.md)
7. [Wiki Home](./.internal/unpublished/wiki/Home.md)

## 发布输出

本仓库已包含首发所需的生成版发布格式。

### GitHub Pages

- [Chinese GitHub Pages edition](./chapter1/final-draft-v3/github-pages.md)
- [English GitHub Pages edition](./chapter1/final-draft-v3/en/github-pages.md)
- Shared styling: [.internal/engineering/assets/main.scss](./.internal/engineering/assets/main.scss)

### GitHub Wiki

GitHub Wiki 源稿保存在 [.internal/unpublished/wiki/](./.internal/unpublished/wiki/)，便于发布前 review。

Start pages:

- [Wiki Home](./.internal/unpublished/wiki/Home.md)
- [Wiki Sidebar](./.internal/unpublished/wiki/_Sidebar.md)
- [Public Release Checklist](./.internal/unpublished/wiki/Public-Release-Checklist.md)
- [Wiki Sync Guide](./.internal/unpublished/publishing/wiki-sync.md)

GitHub 会把 wiki 页面存放在单独的 `*.wiki.git` 仓库中。只有在 `make -f .internal/engineering/Makefile check` 通过后，才应从 `.internal/unpublished/wiki/` 发布。

### Substack

- [Chinese Substack paste edition](./.internal/unpublished/publishing/chapter-01/substack/chapter1.substack.md)
- [English Substack paste edition](./.internal/unpublished/publishing/chapter-01/en/substack/chapter1.substack.md)

Substack 不保留 custom CSS 或 pandoc div blocks，所以 Substack 版本将 definition/example boxes 展平为普通 Markdown，并使用明确的 figure-upload markers。

### Hugging Face

- [Chinese Hugging Face README edition](./.internal/unpublished/publishing/chapter-01/hugging-face/README.md)
- [English Hugging Face README edition](./.internal/unpublished/publishing/chapter-01/en/hugging-face/README.md)

每个 Hugging Face package 都包含对应的 final PDF 与 figure assets。

## 引用证据

Chapter 1 有 citation evidence matrix 支撑，包含 arXiv papers、web-source extracts 与 source-to-claim mapping notes。

Public index:

- [Citation Evidence Index](./chapter1/references/citation-evidence-index.md)
- [Reference Package Manifest](./chapter1/references/reference-package-manifest.md)

raw reference PDF corpus 默认不提交到仓库。这样可以保持公开仓库干净，也避免对第三方 PDF 或网页快照的再分发权利产生歧义。

## 仓库地图

```text
.
├── README.md
├── chapter1/
│   ├── README.md
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
    │   ├── Makefile
    │   ├── assets/
    │   ├── github/
    │   │   ├── workflows/
    │   │   ├── ISSUE_TEMPLATE/
    │   │   ├── pull_request_template.md
    │   │   └── CODEOWNERS
    │   ├── scripts/
    │   └── site/
    ├── repository/
    │   ├── concepts/
    │   ├── legal/
    │   └── policy/
    ├── unpublished/
    │   ├── publishing/
    │   ├── series/
    │   ├── whitepaper/
    │   └── wiki/
    └── local/
```

根层只保留公开入口。`.internal/engineering/` 保存工程与发布自动化，`.internal/unpublished/` 保存未发表材料，`.internal/repository/` 保存仓库治理、许可与概念辅助文件，`.internal/local/` 只放本地缓存并被忽略。

## 如何使用本仓库

### 阅读

把本仓库作为 `constitutional_runtime` 的公开概念地图。

从这里开始：

```text
.internal/unpublished/series/outline.md
chapter1/final-draft-v3/
.internal/unpublished/whitepaper/outline.md
.internal/repository/concepts/glossary.md
.internal/unpublished/wiki/Home.md
```

### 发布

使用生成好的平台发布包：

```text
.internal/unpublished/publishing/chapter-01/
.internal/unpublished/publishing/chapter-01/en/
```

### 验证引用

使用：

```text
chapter1/references/citation-evidence-index.md
chapter1/references/reference-package-manifest.md
```

### 重新生成平台格式

```bash
./.internal/engineering/scripts/build_chapter1_platform_formats.py
```

### 检查公开仓库卫生

```bash
make -f .internal/engineering/Makefile check
```

它会运行：

```bash
./.internal/engineering/scripts/check_public_repo.sh
```

### 本地预览 GitHub Pages

本地 Jekyll 预览使用 Ruby 3.x：

```bash
ruby --version  # use Ruby 3.x; see .internal/engineering/site/.ruby-version
cd .internal/engineering/site
bundle install
bundle exec jekyll serve
```

隐藏后的 workflow 配置保存在 `.internal/engineering/github/workflows/`；如需重新启用 GitHub Actions，需要在发布前把对应文件同步回 `.github/workflows/`。

## 公开发布设置

公开发布配置记录在 [.internal/repository/policy/PUBLIC_RELEASE.md](./.internal/repository/policy/PUBLIC_RELEASE.md)。

Required local/public files include:

- [Environment metadata template](./.internal/engineering/site/.env.example)
- [License](./.internal/repository/legal/LICENSE.md)
- [Contribution guide](./.internal/repository/policy/CONTRIBUTING.md)
- [Security policy](./.internal/repository/policy/SECURITY.md)
- [Support policy](./.internal/repository/policy/SUPPORT.md)
- [Citation metadata](./.internal/repository/legal/CITATION.cff)
- [Public readiness workflow](./.internal/engineering/github/workflows/public-check.yml)

going public 需要：

- repository visibility 被有意设置
- GitHub Pages source 设置为 GitHub Actions
- public-readiness workflow 通过
- Wiki source 在发布到 GitHub Wiki 前经过 review
- 没有 private implementation source、credentials、prompts、logs 或 traces

## 公开仓库政策

允许放在这里：

- essays and publishing drafts
- final PDF/Markdown/DOCX release packages
- diagrams and Mermaid sources
- citation indexes and manifests
- glossary entries and concept explanations
- whitepaper outlines and public technical notes
- GitHub Wiki source pages
- public publishing configuration and templates

不要加入：

- private implementation source code
- credentials, API keys, tokens, or secrets
- private prompts or internal logs
- unpublished operational traces
- sensitive user data
- raw third-party PDFs or snapshots without clear redistribution rights

发布或 push 前运行：

```bash
make -f .internal/engineering/Makefile check
```

## 当前状态

- Chapter 1 Chinese final package: complete
- Chapter 1 English final package: complete
- GitHub Pages editions: generated
- Substack paste editions: generated
- Hugging Face README editions: generated
- GitHub Wiki source: drafted
- Chapter 1 reference evidence index: complete
- Full whitepaper: outline stage
- Chapters 2-8: planned

## 项目成熟度声明

本公开仓库不应宣称 full runtime 已经完成。

谨慎的公开表述是：

```text
The project proposes and documents a governed runtime architecture for persistent multi-agent task execution.
It has a mature conceptual frame around CR, CK, and MK.
It treats authority relations, mission lifecycle, evidence admission, audit, and closure as explicit runtime objects.
Some source-side components may exist as scaffolds or executable research surfaces.
The system still requires controlled taskflow tests, schema hardening, runtime validation, and public evidence packaging before v1.0 claims.
```

简短版：

```text
Not a finished v1.0 product.
Not a public source-code release.
Not a generic agent framework.
Not a roleplay/persona project.
A public architecture, article, and whitepaper repository for a governed persistent multi-agent runtime.
```

## Chapter Map

### Published / Public

#### Chapter 1: Structural Instability in Agent OS

**Working title:** *Agent OS Structural Instability: Why Long-Horizon AI Work Needs Task Ownership, Permissions, Audit, and Legitimate Closure*

Chapter 1 是 problem frame。它解释为什么长期 single-agent work 在 task identity、authority、evidence、audit 与 closure 不是显式 runtime objects 时会发生结构性失稳。

核心 taxonomy：

```text
task ownership drift
support-to-ownership escalation
memory / evidence collapse
persona-as-authority
delegation-as-authorization
global-chat context pollution
tool capability without governance
continuation without lawful closure
```

### Chapters 2-7 Draft Roadmap

以下章节不是 final authority。标题与内部结构会随白皮书稳定而调整。

#### Chapter 2: The Problem Is Not Capability, but Organization

Chapter 2 将项目从“更强 agent”重新定位到“受治理的任务组织”。

核心 claims：

```text
Capability != Ownership
Role != Authority
Collaboration != Organization
Memory != Evidence
Done != Closure
```

预期贡献：

- 解释为什么现有 agent runtimes 是必要但不充分的
- 分离 execution substrate 与 governance substrate
- 引入 CR / CK / MK 作为 nested adjudicating layers
- 定义为什么 mission ownership、authority relations、evidence gates、state deltas 与 closure receipts 必须存在于 capability systems 之上

#### Chapter 3: Governed Persistent Multi-Agent Task System

Chapter 3 将架构展开为八轴系统。

核心 claims：

```text
CR / CK / MK are adjudicating spines.
AG / CP / SM are substrate planes.
DG / EP are supervisory and delivery planes.
```

预期贡献：

- 定义 Constitutional Persistent Multi-Agent Runtime
- 形式化八轴架构
- 解释 CR as current lawful surface
- 解释 CK as executable authority law
- 解释 MK as mission lifecycle governance
- 解释 AG / CP / SM / DG / EP 为什么对真实 execution、audit 与 delivery 必要

#### Chapter 4: Runtime Contract

**Suggested title:** *Runtime Contract: From Eight-Axis Architecture to Executable Objects*

Chapter 4 回答：

```text
What must be implemented?
Which runtime objects exist?
How do they reference each other?
Which transitions are allowed, denied, held, escalated, or closed?
What receipts prove each step?
```

#### Chapter 5: Reference Implementation / Execution Topology

Chapter 5 回答：

```text
What implementation surfaces carry the contracts?
```

预期主题：

- Root Owner interaction layer
- Task Feed / Mission Feed
- current-truth gateway
- CK authority validator
- MK routing and lifecycle engine
- AG runtime binding
- CP gateway / adapter / tool / sandbox layer
- SM evidence ledger and receipt store
- DG audit validator
- EP return bundle and handoff builder
- controlled connection to agent runtime OS, OpenClaw-style gateway, MCP, CI, and publication surfaces

这一章不应变成 library list。实现栈的重要性只在于它如何承载 runtime contracts。

#### Chapter 6: Evaluation, Drift Tests, and Audit Protocol

Chapter 6 回答：

```text
How do we know the governance layer works?
```

预期 evaluation directions：

```text
authority invariant tests
mission lifecycle replay
receipt-chain completeness
denial correctness
honest-stop correctness
evidence admission correctness
state-delta replay
closure quality
handoff continuity
drift ablation
controlled read-only taskflow tests
```

可能 metrics：

```text
owner-field completeness
support_no_ownership violation rate
expired evidence use count
persona_not_law_source pass rate
state_delta receipt coverage
closure receipt completeness
honest_stop precision
handoff continuity score
```

#### Chapter 7: Lawful Closure, Release Boundary, and v1.0 Criteria

Chapter 7 回答：

```text
When is a mission truly closed?
When is the runtime ready to claim release maturity?
What does v1.0 require?
```

预期主题：

- done vs closure
- closure authority
- state-delta finality
- unresolved issue declaration
- rollback and reopen semantics
- public evidence package
- source / document boundary
- v1.0 release criteria
- what should remain private
- how a governed runtime becomes publishable without leaking private implementation surfaces

Chapter 7 应该通过 release discipline 收束整个公开系列。

## Roadmap

推荐的下一步公开写作顺序：

1. 稳定 Chapter 1 在 GitHub Pages、Substack、Hugging Face 上的发布版本。
2. 从 `.internal/unpublished/wiki/` 发布 GitHub Wiki orientation layer。
3. 用 Chapter 2 解释根本问题为什么是 organization，而不是 capability。
4. 用 Chapter 3 定义八轴架构。
5. 用 Chapter 4 定义 Runtime Contracts。
6. 用 Chapter 5 解释 reference implementation topology，但不暴露私有源码结构。
7. 用 Chapter 6 提出 evaluation and validation。
8. 将 technical editions 整合为完整白皮书。

## 与相邻系统的定位

本项目不需要在每个相邻系统的主战场上竞争。它提出的是一个更窄的 claim。

| Adjacent direction | What it is strong at | This project's narrower claim |
|---|---|---|
| persistent auditable single-agent runtime | memory、logs、self-observation、forensic reconstruction | multi-agent mission ownership and authority governance |
| microkernel MAS / social simulation | scale、simulation validity、dynamic agent population | operational legitimacy for real task execution |
| natural-language Agent OS | human-readable constitution and role structure | typed executable governance above natural-language interface |
| gateway / plugin-based agent OS | ingress、capability exposure、provider and channel control | gateway is not mission sovereignty |
| durable task daemon | long-running work persistence | lawful mission execution with owner、evidence、audit、closure |

## Project Motto

```text
Memory is recall.
Evidence is admissibility.

Capability is can.
Authority is may.

Done is local completion.
Closure is lawful mission termination.

Agent is not the unit of governance.
Mission is the unit of governance.
```

## 建议公开描述

描述本仓库时可以使用：

> This repository documents a governed persistent multi-agent runtime architecture. The project argues that long-running AI work needs mission ownership, typed authority relations, evidence gates, audit receipts, state-delta records, and lawful closure. It treats existing agent runtimes as execution substrates and places a Constitutional Runtime / Kernel / Mission Kernel governance layer above them.

## 最小词汇表

| Term | Meaning |
|---|---|
| Agent OS | 一个 single-agent operating model：一个 assistant 通过 conversational loop 管理 intent、planning、tools、execution、memory 与 closure。 |
| Constitutional Runtime | 维护 current truth、evidence gates、authority boundaries、audit receipts、state transitions 与 lawful closure 的受治理 runtime layer。 |
| Constitutional Kernel | 决定谁有 authority 做什么的 authority-law layer。 |
| Mission Kernel | 将 request 转化为 governed mission objects 的 lifecycle layer。 |
| Mission | 带有 owner、authority、route、evidence、state-delta expectations、required receipts 与 closure conditions 的 task object。 |
| Root Owner | 概念系统中的最高显式人类 authority。 |
| Scoped Capability | 被 actor、mission、artifact、tool、action、environment 与 time 限制的 permission grant。 |
| Evidence Gate | memory 或 produced information 成为当前 mission judgment 可采 evidence 的过程。 |
| State Delta | 对 canonical system state 的一次被记录且被授权的变更。 |
| Audit Receipt | review、validation、rejection、dissent 或 acceptance 的记录。 |
| Closure Receipt | mission 被合法关闭的可验证记录。 |
| Honest Stop | 因 evidence、authority、state 或 closure conditions 不足而拒绝继续的合法 runtime outcome。 |

## 这个仓库不是什么

本仓库不是：

- implementation repository 的公开 dump
- API reference
- finished runtime 的 deployment manual
- runtime 已经 v1.0 complete 的声明
- 泛泛的“more agents are better”论证
- roleplay/persona project
- benchmark-first agent framework
- large-scale social simulation framework

它是一个为 governed persistent multi-agent task system 服务的公开世界观、概念、文章与白皮书仓库。

## License / Reuse

复用条款见 [.internal/repository/legal/LICENSE.md](./.internal/repository/legal/LICENSE.md)。在更宽泛的复用权利被明确授予之前，请将本仓库视为公开 documentation 与 whitepaper draft。引用本项目时，请引用 Chapter 1 的 canonical PDFs 或 GitHub Pages editions。
