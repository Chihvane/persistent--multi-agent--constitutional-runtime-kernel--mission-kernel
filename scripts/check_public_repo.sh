#!/usr/bin/env bash
set -euo pipefail

echo "Checking public documentation repository hygiene..."

if rg -n --hidden --glob '!.git/**' --glob '!scripts/check_public_repo.sh' \
  '(OPENAI_API_KEY|ANTHROPIC_API_KEY|GITHUB_TOKEN|HF_TOKEN|PRIVATE KEY|BEGIN RSA|BEGIN OPENSSH|password\s*=|secret\s*=)' .; then
  echo "Potential secret or private credential marker found. Review before publishing."
  exit 1
fi

if rg -n --hidden --glob '!.git/**' \
  '(private source|internal log|credential|token)' . >/dev/null; then
  echo "Note: repository contains privacy-sensitive keywords. Review context before publishing."
fi

echo "OK: no obvious credential markers found."

