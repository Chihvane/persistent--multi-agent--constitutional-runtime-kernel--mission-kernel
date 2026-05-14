# Contributing / 贡献指南

[English](#english) | [简体中文](#简体中文)

## English

Thanks for helping improve the public documentation.

This repository is public-facing. Keep contributions scoped to essays, release packages, public diagrams, citation indexes, publishing formats, and whitepaper drafts.

### Before Opening a Pull Request

Run:

```bash
make -f .internal/engineering/Makefile check
```

For Chapter 1 platform edits, regenerate the platform formats when the source Markdown changes:

```bash
.internal/engineering/scripts/build_chapter1_platform_formats.py
```

### Public Boundary

Do not contribute:

- private implementation source code
- credentials, API keys, access tokens, signing keys, or local `.env` files
- private prompts, internal logs, unpublished traces, or sensitive user data
- raw third-party PDFs or snapshots without clear redistribution permission

### Pull Request Expectations

- Explain what public surface changed.
- Note whether canonical PDFs, platform packages, or citation indexes changed.
- Include screenshots only when they help review rendered pages.
- Keep unrelated formatting churn out of the pull request.

## 简体中文

感谢你帮助改进公开文档。

本仓库面向公开发布。贡献范围应限制在文章、发布包、公开图表、引用索引、平台发布格式与白皮书草稿内。

### 提交 Pull Request 前

运行：

```bash
make -f .internal/engineering/Makefile check
```

如果修改了 Chapter 1 的平台版本，并且源 Markdown 发生变化，请重新生成平台格式：

```bash
.internal/engineering/scripts/build_chapter1_platform_formats.py
```

### 公开边界

请不要贡献：

- 私有实现源码
- credentials、API keys、access tokens、signing keys 或本地 `.env` 文件
- 私有 prompts、内部日志、未公开 traces 或敏感用户数据
- 没有明确再分发许可的第三方 PDF 或网页快照

### Pull Request 期望

- 说明改动了哪个公开表面。
- 说明 canonical PDFs、platform packages 或 citation indexes 是否变化。
- 只有在有助于审阅渲染页面时才加入截图。
- 避免把无关的格式化噪声混入 PR。
