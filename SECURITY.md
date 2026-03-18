# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x     | ✅ Yes     |

Only the latest release receives security fixes. Upgrade before reporting.

## Reporting a Vulnerability

**Do not open a public GitHub issue for security vulnerabilities.**

Report security issues by emailing: **security@sciwizard.dev** (or open a private GitHub security advisory at `Security → Report a vulnerability`).

Include:

- A clear description of the issue and its potential impact
- Steps to reproduce or a minimal proof-of-concept
- Affected versions
- Any suggested fix, if you have one

## Response Timeline

| Step | Target |
|------|--------|
| Acknowledgement | Within 48 hours |
| Triage & severity assessment | Within 5 business days |
| Fix or mitigation released | Within 30 days for critical, 90 days for moderate |
| Public disclosure | After fix is released |

## Scope

This policy covers:

- The `sciwizard` Python package
- The plugin loading mechanism (arbitrary code execution via untrusted plugins is by design — users should only load plugins from sources they trust)

Out of scope: third-party dependencies (report those to their respective maintainers).
