# Public Release Checklist

Use this checklist before making the repository public and before every launch
push.

## Repository Boundary

- The implementation source repository remains private.
- No private implementation source code is committed here.
- No credentials, API keys, access tokens, signing keys, private prompts,
  internal logs, or sensitive user data are committed.
- Raw third-party PDFs or web snapshots are excluded unless redistribution rights
  are explicit.
- `.env` files, cache directories, build outputs, and editor swap files are
  ignored.

## Required Public Files

- `README.md`
- `README.en.md`
- `README.zh-CN.md`
- `.github/workflows/pages.yml`
- `.github/workflows/public-check.yml`
- `.github/pull_request_template.md`
- `.github/ISSUE_TEMPLATE/docs_issue.yml`
- `.github/CONTRIBUTING.md`
- `.github/SECURITY.md`
- `.github/SUPPORT.md`
- `.github/CODEOWNERS`
- `.internal/repository/legal/LICENSE.md`
- `.internal/repository/policy/CONTRIBUTING.md`
- `.internal/repository/policy/SECURITY.md`
- `.internal/repository/policy/SUPPORT.md`
- `.internal/repository/policy/PUBLIC_RELEASE.md`
- `.internal/engineering/site/.env.example`
- `.internal/repository/policy/repo-policy.md`
- `.internal/engineering/site/_config.yml`
- `.internal/engineering/github/workflows/pages.yml`
- `.internal/engineering/github/workflows/public-check.yml`
- `.internal/engineering/github/pull_request_template.md`
- `.internal/engineering/github/ISSUE_TEMPLATE/docs_issue.yml`
- `.internal/unpublished/wiki/Home.md`
- `.internal/unpublished/wiki/_Sidebar.md`

## Chapter 1 Launch

- Chinese canonical PDF exists.
- English canonical PDF exists.
- GitHub Pages editions are generated.
- Substack paste editions are generated.
- Hugging Face README packages are generated.
- Conversion manifests exist for both language editions.
- Citation evidence index and reference manifest are present.

## GitHub Settings

- Default branch is `main`.
- Repository visibility is public only after `make -f .internal/engineering/Makefile check` passes.
- GitHub Pages source is GitHub Actions.
- Branch protection requires the public-readiness check before merging.
- Issues and pull requests use the active bilingual templates in `.github/`.
- Wiki is enabled only after the source files in `.internal/unpublished/wiki/` have been reviewed.

## Final Gate

```bash
make -f .internal/engineering/Makefile check
git status --short
```

Review the staged diff manually before pushing.
