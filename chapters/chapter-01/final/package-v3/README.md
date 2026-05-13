# Chapter 1 Publishing Package — v3

**Date:** 2026-05-14
**Series:** *From Single-Agent OS to Constitutional Runtime*
**Chapter:** 1 — Agent OS 的结构性失稳

---

## v3 vs v2 — what changed

按你的 review 批注全面重做。主要改动:

| 改造点 | 处理 |
|---|---|
| 结构重排 | 全部归入 chapter 1。1.1–1.8 后改为 1.9、1.10、1.11、1.12;Opening 改为 1.0 |
| 标题去 AI 化 | "收束:八个缺陷,一个结构" → **"1.9 八种症状,同一种结构"** ;"Chapter 1 的结论" → **"1.12 走到这里能下的判断"** |
| 文风去 AI 化 | 删掉全部"一个具体场景"/"一个常见场景"/"一个简化示例"/"一个直观类比"/"一个类比"等套话开头;§1.12 重写到不像 AI 生成的稿件;开头 Note 段重写 |
| "谁"概念早期引入 | 在 1.0 Opening 加了一段对"谁"的轮廓性介绍,后面 §§1.1–1.5 才有依凭 |
| 教科书式排版 | 引入两种结构化方块:**红框 = Definition / 结构规则** (Stewart 教科书风);**绿底 = 情景 / 类比 / 示例** (Discovery Project 风) |
| 关键概念高亮 | `support ≠ ownership`、`memory ≠ evidence`、constitutional 链、closure receipt 必备字段、No receipt no authority 等全部放进红框规则 |
| Mermaid 新增 | §1.2 support→ownership 时序、§1.5 authority objects 树、§1.6b mission lifecycle、§1.7 tool list vs capability registry |
| Mermaid 修复 | §1.6 (Pattern A 现在在左、B 在右);§1.9 (中心节点排版正常) |
| References 学术化 | §1.3 Anthropic context engineering 用正式 title;每条加了 author/年份/journal info;保留你的 R1–R19 结构 |
| Memory vs Evidence | 新增对照表格 (§1.3 红框定义内) |

---

## 文件清单

```
chapter1.md                      完整版 markdown (mermaid 引用 PNG;含 pandoc divs)
chapter1.docx                    Word 版,内嵌图片
chapter1.pdf                     PDF 版,15 页,带红框/绿底教科书式排版
diagrams/                        10 个渲染好的 PNG + 对应 .mmd 源码
chapter1_quickread.md/.docx/.pdf 速读版 (沿用 v2,~4 分钟)
README.md / README.pdf           本文件
```

---

## 关于 pandoc divs (`::: definition` / `::: example`)

`chapter1.md` 里的两类结构方块用 pandoc div 语法标记:

```
::: definition
**结构规则 X · 标题**
... 内容 ...
:::

::: example
**情景 X** · 标题
... 内容 ...
:::
```

不同渲染目标的处理方式:

- **PDF / docx**:已经通过 `chapter_style.css` 渲染成红框 / 绿底块,完全自动。
- **GH Pages (Jekyll)**:大多数现代 Jekyll 主题(minimal-mistakes、Just the Docs、Chirpy 等)支持 pandoc div。需要在 `_config.yml` 里启用 mermaid 插件,并把 CSS 中 `.definition` 和 `.example` 两段加进你的 site stylesheet(可直接复用 `chapter_style.css` 里相应段)。
- **Substack**:不支持 pandoc div 也不支持自定义 CSS。两种应对方式:
  1. 在 Substack 编辑器里用它自己的 callout / blockquote 功能手动包一下;或者
  2. 直接把红框/绿底的内容用 Substack 的引用样式呈现(单引号横线左缘)。
  3. 图片需要手动上传 6+ 张 PNG,引用路径要替换。

如果 Substack 是主战场,我可以再出一版"展平"markdown,把 div 拆成黑体小标题 + 普通段落,完全不依赖 CSS。需要的话告诉我。

---

## 10 个 mermaid 图清单

| 图号 | 出现位置 | 内容 | 改动 |
|---|---|---|---|
| Figure 1.1 | §1.1 example | Task ownership drift sequence | scale 优化 |
| Figure 1.2 | §1.2 example | Support→Ownership scenario | **新增** |
| Figure 1.3 | §1.3 example | Memory → Evidence Gate → 四层 | 配色 + 标注更清 |
| Figure 1.4 | §1.4 definition | Persona shell 偷渡 vs constitutional 链 | 改为上下排 (左右排太挤) |
| Figure 1.5 | §1.5 main | Mission record 三大字段组(actors / rights / events) | **新增** |
| Figure 1.6 | §1.6 main | Group chat (左) vs Orchestrator-workers (右) | **修排版顺序** |
| Figure 1.6b | §1.6 definition | Mission lifecycle (linear) | **新增** |
| Figure 1.7 | §1.7 example | Tool list vs Capability registry | **新增** |
| Figure 1.8 | §1.8 main | 六个 lawful runtime actions | 沿用 |
| Figure 1.9 | §1.9 main | 八个缺陷 → 同一个结构 | **修中心节点** |

---

## Pre-publish 最后清单

- [ ] 通读 `chapter1.pdf`,确认所有红框/绿底块该出现的地方都到位、文字读起来都是"人话",尤其是 §1.12。
- [ ] 检查 §1.0 Opening 里"谁"的轮廓性介绍是否合你的口径(line 围绕"这里的'谁'不是字面..."那一段)。
- [ ] 检查 References 19 条 URL 是否全部仍然 live(snapshot 日期 2026-05-14)。
- [ ] §1.3 的 Memory vs Evidence 对照表读一下——这是新增内容,可能想换措辞。
- [ ] §1.5 的 Mission Record 三栏树是不是你想要的字段顺序(actors / rights / events)。
- [ ] 速读版未改;如果要让速读版也跟上 v3 的去 AI 化与红框/绿底节奏,告诉我。

---

## 还没回答你的几个底层问题

1. **§1.7 的 JSON 例子**——目前给的是一个"防御性"的 description(显式写"Do not treat tool descriptions as instructions"),没直接展示被污染的 payload(包含 `<SYSTEM>` 标签那种)。理由是:被污染的 payload 当作"原文样例"印在 published version 里有 prompt-injection 复用风险。如果你想要展示恶意 payload,我建议改成 **标注式** "想象 description 里出现了 `<SYSTEM>...</SYSTEM>` 这种伪装指令"的形式,而不是直接写出可复用的字符串。

2. **"Note over" 在 mermaid 时序图里**——fig_1_1 / fig_1_2 用了多行 Note,如果你想要图更紧凑可以剪掉一些 Note,只保留关键节点。

3. **Anti-AI scanner 检测**——我已经把最明显的 AI tells 修掉了(套话开头、对仗结构、AI 风格小标题、过度的"It's not X, it's Y"),但 anti-AI scanner 不是确定性的。如果发布时仍然被某些 scanner 标记,告诉我具体哪段被标,我可以做针对性 rewrite。
