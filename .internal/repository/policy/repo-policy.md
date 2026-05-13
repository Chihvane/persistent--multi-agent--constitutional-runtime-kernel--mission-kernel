# Public Repository Policy

This repository is public-facing by design.

Allowed content:

- essays
- whitepaper drafts
- diagrams
- glossary entries
- architecture explanations
- sanitized examples
- publication metadata
- GitHub Wiki source pages
- public publishing configuration and templates

Do not add:

- private source code from the implementation repository
- credentials, API keys, tokens, or secrets
- internal logs
- private prompts or unpublished operational traces
- sensitive user data
- unpublished implementation details that should remain private

Before publishing, run:

```bash
make -f .internal/engineering/Makefile check
```

Public launch setup lives in:

- [PUBLIC_RELEASE.md](./PUBLIC_RELEASE.md)
- [Public Release Checklist](../../unpublished/wiki/Public-Release-Checklist.md)
