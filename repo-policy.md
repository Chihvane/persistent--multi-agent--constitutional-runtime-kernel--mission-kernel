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

Do not add:

- private source code from the implementation repository
- credentials, API keys, tokens, or secrets
- internal logs
- private prompts or unpublished operational traces
- sensitive user data
- unpublished implementation details that should remain private

Before publishing, run:

```bash
make check
```

