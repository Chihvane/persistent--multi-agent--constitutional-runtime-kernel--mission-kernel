---
layout: page
title: "第一章技术版：Agent OS 的结构性失稳"
---

# 从 Single-Agent OS 到 Constitutional Runtime

## 第一章技术版

### Agent OS 的结构性失稳：为什么长期 AI 工作需要任务归属、权限、审计与合法结案

这一章定义我从 single-agent operating model 转向 constitutional multi-agent runtime 的失败模型。

核心判断是：长期 AI 工作的失败，不只是因为模型会幻觉、遗忘或错误使用工具。更深层的问题是，许多系统的 runtime substrate 缺少让工作在时间中保持可问责的治理原语。尤其是在 Single-Agent OS 里，四类本应分离的职责经常被压进同一个对话循环：

- 意图管理
- 权限管理
- 执行管理
- 结案管理

这些职责在短任务中可以保持隐式，因为短任务的上下文小、风险低、纠错快。但一旦进入长期操作，隐式结构会变成系统性风险。

## 1. 定义：Single-Agent OS

这里的 **Single-Agent OS** 指的是一种 AI 工作环境：一个主要 agent 承担大部分或全部核心职责，包括：

- 理解用户意图
- 维护任务上下文
- 制定计划
- 选择并调用工具
- 读写 artifact
- 判断何时请求权限
- 总结进度
- 宣布任务完成

这种设计的优势是协调成本极低。用户只需要自然表达目标，agent 负责把意图转换成行动。

问题出现在它被用于长期工作时。此时，agent 不再只是执行者，而会变成事实上的操作系统。但它通常并没有操作系统所需的治理结构。

## 2. 长期 AI 工作是 runtime 问题

长期 AI 工作具有普通聊天交互不具备的特征：

- 跨越许多轮对话或多个 session
- 触及多个 artifact
- 需求会变化
- 使用风险等级不同的工具
- 可能需要委托给其他 agent
- 会被中断和恢复
- 产出需要评审、发布或进入实际使用
- 必须说明剩余不确定性

这些特征把问题从“生成一个好回答”转变成“维护一个可治理的操作”。

可治理操作需要显式 runtime state。这个 state 不能只存在于模型注意力或聊天记录里。它必须被表示为系统可检查的对象和事件。

## 3. 失效模式 A：任务归属不明确

在 Single-Agent OS 中，任务往往以自然语言形式存在于对话里。agent 可能有一个内部计划，但 runtime 并不一定拥有一等公民级别的 task object：

- owner
- scope
- status
- dependencies
- evidence requirements
- acceptance criteria
- handoff history

当任务被打断、委托或恢复时，这会导致结构性不稳定。

如果没有稳定的 ownership，系统就无法可靠回答：

- 当前 work unit 由谁负责？
- 负责的 artifact 或 outcome 精确是什么？
- ownership 是否发生过转移？
- 转移时携带了哪些权限？
- 结案前必须返回哪些证据？

结果就是责任扩散。工作仍在推进，但 accountability 变得模糊。

## 4. 失效模式 B：权限扁平或隐式

许多 agent 系统把权限当成接口层问题：工具可用或不可用，用户允许或不允许。这对于简单工作流足够，但对于真实任务并不够。

Constitutional Runtime 需要更细粒度的 authority model：

- read authority
- write authority
- execute authority
- publish authority
- delete authority
- network authority
- credential authority
- delegation authority
- spending or quota authority

这些 authority 应该按任务、artifact、环境和时间进行 scope 限定。

例如，允许 agent 编辑文章草稿，不等于允许它发布文章。允许 agent 检查仓库，不等于允许它推送分支。允许 agent 生成部署方案，也不等于允许它执行部署。

当权限保持隐式时，agent 的行为就过度依赖对话解释。它可能因为不确定而放弃有用动作，也可能执行从未被真正授权的动作。

## 5. 失效模式 C：历史记录不具备审计等级

聊天记录有价值，但它不是充分的 audit trail。

一个具备审计等级的 runtime history 应该保存结构化事件，例如：

- task creation
- authority grant
- tool invocation
- artifact read
- artifact write
- decision point
- assumption recorded
- handoff
- review
- closure request
- closure acceptance or rejection

每个事件至少应该回答：

- 谁或什么 actor 执行了动作
- 使用了什么 authority
- 动作属于哪个 task
- 影响了哪些 artifact
- 使用了哪些输入证据
- 产生了什么输出
- 是否需要用户确认

这不是为了制造繁文缛节，而是为了让系统在事后可理解、可复盘、可追责。如果一个生成 artifact 出错、不安全或引发争议，runtime 必须支持重建过程。

## 6. 失效模式 D：结案非正式

在普通聊天里，assistant 的最后回答经常被视作任务完成。但对于治理型工作，这不够。

合法结案需要 closure packet：

- final artifact references
- actions taken summary
- tests or checks performed
- unresolved assumptions
- residual risks
- permission-sensitive actions taken or skipped
- user-visible consequences
- acceptance criteria status

如果没有 closure packet，“done”只是一个对话状态。assistant 停止输出了，但操作并没有以用户或 runtime 可以信任的方式关闭。

长期 AI 工作中，closure 是治理原语，而不是礼貌性总结。

## 7. 为什么模型能力不能替代治理

增强模型能力能改善很多局部行为。它可能提升规划、减少幻觉、提高代码准确率，也可能让总结更忠实。但它不能消除 runtime governance 的必要性。

原因有四个。

第一，authority 不能仅凭智能推断。模型推理能力再强，也不自动拥有行动权限。

第二，没有 provenance 的 memory 可能增加信心，而不增加 accountability。系统不仅要知道它记得什么，还要知道记忆来自哪里、是否仍然有效。

第三，tool availability 会扩大后果。更好的工具使用能力扩大了能力边界，也扩大了错误影响面。

第四，closure 位于 generation 之外。一个回答可以非常流畅，却没有满足任务验收标准。

因此，治理不能只作为 prompt instruction 存在。它必须成为 runtime semantics。

## 8. Constitutional Runtime 的初始定义

**Constitutional Runtime** 是一种执行环境：AI agents 在显式、可检查、可执行的规则下行动。

最低限度上，它应该提供：

- 具备 ownership semantics 的 task objects
- scoped capability grants
- sensitive actions 之前的 policy checks
- structured event logs
- delegation and handoff protocols
- review and escalation paths
- closure criteria and closure packets

runtime constitution 不是一份静态 policy 文档，而是一组会实际塑造 agent 行动的操作约束和能力边界。

这意味着 agent 不再是整个 operating system，而是 governed system 里的 actor。

## 9. 架构后果

这种转向带来几个直接架构结论。

Tasks 必须成为一等 runtime objects。

Permissions 应该表示为 scoped capabilities，而不是笼统的 trust mode。

Tool calls 必须绑定 task identity 和 authority context。

Memory 应该拆分为 working context、durable mission state 和 audit-grade event history。

Delegation 必须通过 typed handoff records 保留 accountability。

Closure 必须基于 evidence，而不是仅仅基于最后一段自然语言回答。

这些原则构成后续章节的基础。

## 10. 本章结论

Single-Agent OS 的失败，并不是 agency 的失败，而是 runtime structure 的失败。

长期 AI 工作需要一个能够保存意图、限制权限、暴露历史并合法关闭任务的系统。没有这些原语，即使一个 agent 非常强大，它在操作层面仍然是不稳定的。

下一步架构转向是 mission kernel：把持久用户意图与临时 agent execution 分离出来的那一层。

