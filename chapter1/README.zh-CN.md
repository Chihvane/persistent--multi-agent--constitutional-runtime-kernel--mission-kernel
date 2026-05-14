---
layout: page
title: Chapter 1
---

# Chapter 1 版本地图

[English](./README.md) | [简体中文](./README.zh-CN.md)

**Agent OS 的结构性失稳：为什么长期 AI 工作需要任务所有权、权限、审计与合法关闭**

## 最终权威版本

Chapter 1 的最终发布版本是 **Publishing Package v3** 与 **Publishing Package v3-EN**，日期为 2026-05-14。

- [Final Version Map](./final-draft-v3/)
- [中文最终 PDF](./final-draft-v3/package-v3/chapter1.pdf)
- [中文最终 Markdown 源文件](./final-draft-v3/package-v3/chapter1.md)
- [英文最终 PDF](./final-draft-v3/package-v3-en/chapter1.pdf)
- [英文最终 Markdown 源文件](./final-draft-v3/package-v3-en/chapter1.md)
- [英文最终落地页](./final-draft-v3/en/)

## 发布说明

每个语言版本的 `chapter1.pdf` 都是对应文本与排版的最终权威。如果 Markdown、Substack、Hugging Face 或 GitHub Pages 版本与对应 PDF 不一致，应以 PDF 为准修正。

package README 会说明完整 Markdown 使用 pandoc div 来表达红色定义框与绿色示例框。GitHub Pages 应直接链接 final PDF，或使用能保留这些块样式的转换页面。Substack 不支持这些 div 或 custom CSS，因此文章需要手工转成 callout / blockquote，或使用展平后的 Markdown 版本。

## 归档草稿

以下早期草稿不是最终发布权威：

- [英文可读草稿](./en/readable.md)
- [英文技术草稿](./en/technical.md)
- [中文可读草稿](./zh/readable.md)
- [中文技术草稿](./zh/technical.md)

## 核心术语

- **Agent OS**：一种 single-agent operating model，其中一个 assistant 持有对话状态、选择工具、执行工作，并判断任务何时完成。
- **Constitutional Runtime**：一个受治理的执行环境，agents 在显式规则、capability、责任结构与 closure criteria 下运行。
- **Task Ownership**：运行时层面对某个工作单元责任归属的分配。
- **Legitimate Closure**：一个可验证的结束状态，系统能说明做了什么、由谁执行、基于什么 authority、使用什么 evidence、还有什么 residual risk。
