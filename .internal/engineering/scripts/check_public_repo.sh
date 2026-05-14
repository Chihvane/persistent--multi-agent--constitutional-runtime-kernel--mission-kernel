#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

echo "Checking public documentation repository readiness..."

failures=0

fail() {
  echo "ERROR: $*"
  failures=1
}

require_file() {
  if [[ ! -f "$1" ]]; then
    fail "Missing required file: $1"
  fi
}

required_files=(
  README.md
  README.en.md
  README.zh-CN.md
  .github/workflows/pages.yml
  .github/workflows/public-check.yml
  .github/pull_request_template.md
  .github/ISSUE_TEMPLATE/config.yml
  .github/ISSUE_TEMPLATE/docs_issue.yml
  .github/CONTRIBUTING.md
  .github/SECURITY.md
  .github/SUPPORT.md
  .github/CODEOWNERS
  .internal/repository/legal/LICENSE.md
  .internal/repository/policy/CONTRIBUTING.md
  .internal/repository/policy/SECURITY.md
  .internal/repository/policy/SUPPORT.md
  .internal/repository/legal/CITATION.cff
  .internal/repository/policy/PUBLIC_RELEASE.md
  .internal/engineering/site/.env.example
  .internal/repository/policy/repo-policy.md
  .internal/repository/concepts/glossary.md
  .internal/engineering/site/_config.yml
  .internal/engineering/site/Gemfile
  .internal/engineering/site/.ruby-version
  .internal/engineering/github/workflows/pages.yml
  .internal/engineering/github/workflows/public-check.yml
  .internal/engineering/github/pull_request_template.md
  .internal/engineering/github/ISSUE_TEMPLATE/config.yml
  .internal/engineering/github/ISSUE_TEMPLATE/docs_issue.yml
  .internal/engineering/github/CODEOWNERS
  .internal/unpublished/wiki/Home.md
  .internal/unpublished/wiki/_Sidebar.md
  .internal/unpublished/wiki/Getting-Started.md
  .internal/unpublished/wiki/Architecture.md
  .internal/unpublished/wiki/Chapter-1.md
  .internal/unpublished/wiki/Citation-Evidence.md
  .internal/unpublished/wiki/Publishing.md
  .internal/unpublished/wiki/Public-Release-Checklist.md
  .internal/unpublished/wiki/Roadmap.md
  .internal/unpublished/wiki/FAQ.md
  .internal/unpublished/publishing/wiki-sync.md
)

for file in "${required_files[@]}"; do
  require_file "$file"
done

required_artifacts=(
  chapter1/final-draft-v3/package-v3/chapter1.pdf
  chapter1/final-draft-v3/package-v3-en/chapter1.pdf
  chapter1/final-draft-v3/github-pages.md
  chapter1/final-draft-v3/en/github-pages.md
  .internal/unpublished/publishing/chapter-01/substack/chapter1.substack.md
  .internal/unpublished/publishing/chapter-01/en/substack/chapter1.substack.md
  .internal/unpublished/publishing/chapter-01/hugging-face/README.md
  .internal/unpublished/publishing/chapter-01/en/hugging-face/README.md
  .internal/unpublished/publishing/chapter-01/conversion-manifest.md
  .internal/unpublished/publishing/chapter-01/en/conversion-manifest.md
  chapter1/references/citation-evidence-index.md
  chapter1/references/reference-package-manifest.md
)

for file in "${required_artifacts[@]}"; do
  require_file "$file"
done

unexpected_root_entries=()
while IFS= read -r entry; do
  name="${entry#./}"
  case "$name" in
    .git|.gitignore|.internal|README.md|README.en.md|README.zh-CN.md|.github|chapter1)
      ;;
    *)
      unexpected_root_entries+=("$name")
      ;;
  esac
done < <(find . -mindepth 1 -maxdepth 1 -print)

if ((${#unexpected_root_entries[@]} > 0)); then
  printf '%s\n' "${unexpected_root_entries[@]}"
  fail "Unexpected root-level entries found. Keep root visible topology to README language entries, .github/, chapter1/, and hidden internals."
fi

forbidden_tracked=()
while IFS= read -r path; do
  case "$path" in
    .internal/engineering/site/.env.example)
      ;;
    .env|.env.*|*/.env|*/.env.*|.DS_Store|*/.DS_Store|*.swp|*.swo|*.log|.bundle/*|*/.bundle/*|vendor/bundle/*|*/vendor/bundle/*|.cache/*|*/.cache/*|.playwright-mcp/*|*/.playwright-mcp/*|_site/*|*/_site/*|chapter1_reference_matrix.zip|chapter1-EN.zip|chapter1_publishing_package_v3_en.zip)
      forbidden_tracked+=("$path")
      ;;
  esac
done < <(git ls-files)

if ((${#forbidden_tracked[@]} > 0)); then
  printf '%s\n' "${forbidden_tracked[@]}"
  fail "Forbidden local/private artifact is tracked."
fi

scan_files=()
while IFS= read -r path; do
  case "$path" in
    .internal/engineering/scripts/check_public_repo.sh|*.pdf|*.docx|*.png)
      ;;
    *)
      scan_files+=("$path")
      ;;
  esac
done < <(git ls-files --cached --others --exclude-standard)

secret_pattern='(AKIA[0-9A-Z]{16}|gh[pousr]_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{20,}|-----BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY-----|[A-Za-z0-9_]*(API_KEY|ACCESS_TOKEN|AUTH_TOKEN|SECRET|PASSWORD)[A-Za-z0-9_]*[[:space:]]*=[[:space:]]*["'"'"']?[A-Za-z0-9_./+=:@-]{8,})'

if ((${#scan_files[@]} > 0)); then
  if rg -n --hidden --no-messages "$secret_pattern" "${scan_files[@]}"; then
    fail "Potential credential-like value found. Review before publishing."
  fi
fi

if ! rg -q '!.internal/engineering/site/.env.example' .gitignore; then
  fail ".gitignore must allow the public .internal/engineering/site/.env.example template."
fi

if ! rg -q 'actions/deploy-pages@v4' .internal/engineering/github/workflows/pages.yml; then
  fail "GitHub Pages workflow must deploy with actions/deploy-pages@v4."
fi

if ! rg -q 'actions/deploy-pages@v4' .github/workflows/pages.yml; then
  fail "Active GitHub Pages workflow must deploy with actions/deploy-pages@v4."
fi

if ! rg -q 'make -f .internal/engineering/Makefile check' .internal/engineering/github/workflows/public-check.yml; then
  fail "Public readiness workflow must run make -f .internal/engineering/Makefile check."
fi

if ! rg -q 'make -f .internal/engineering/Makefile check' .github/workflows/public-check.yml; then
  fail "Active public readiness workflow must run make -f .internal/engineering/Makefile check."
fi

if ! rg -q 'baseurl: "/persistent--multi-agent--constitutional-runtime-kernel--mission-kernel"' .internal/engineering/site/_config.yml; then
  fail ".internal/engineering/site/_config.yml must set the GitHub Pages project baseurl."
fi

if ! rg -q 'README.en.md' README.md || ! rg -q 'README.zh-CN.md' README.md; then
  fail "README.md must expose English and Simplified Chinese language entries."
fi

if ! rg -q '.internal/unpublished/wiki/Home.md' README.md; then
  fail "README.md must link to the wiki source."
fi

if ! rg -q '.internal/repository/policy/PUBLIC_RELEASE.md' README.md; then
  fail "README.md must link to public release setup."
fi

if ((failures > 0)); then
  echo "Public readiness check failed."
  exit 1
fi

echo "OK: public documentation repository is ready for publication review."
