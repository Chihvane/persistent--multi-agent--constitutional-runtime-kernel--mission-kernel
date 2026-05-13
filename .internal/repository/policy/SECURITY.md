# Security Policy

This repository is a public documentation and publication repository. It should
not contain private implementation code, credentials, private prompts, internal
logs, unpublished operational traces, or sensitive user data.

## Supported Scope

Security reports for this repository should focus on:

- accidental disclosure of private implementation details
- committed credentials or signing material
- sensitive operational logs or private prompts
- unsafe public publishing configuration
- misleading links that could route readers to untrusted artifacts

Implementation vulnerabilities in private source code are out of scope for this
public repository.

## Reporting

Do not post sensitive disclosure details in a public issue.

Use GitHub's private vulnerability reporting flow if it is enabled for the
repository. If it is not enabled, contact the maintainers privately through the
GitHub account or organization that owns the repository.

## Maintainer Response

Maintainers should remove or rotate exposed sensitive material, document the
public-facing correction, and run:

```bash
make -f .internal/engineering/Makefile check
```
