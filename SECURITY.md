# Security Policy

## Scope

This repository contains educational Python programs and coursework artifacts. Security reports are welcome for vulnerabilities in the repository itself, its scripts, or its automation.

## Reporting a vulnerability

Please do not publish exploitable details in a public issue. Use GitHub's private vulnerability reporting feature when it is enabled for this repository, or contact the repository owner through the email address listed on the GitHub profile.

Include the affected file, impact, reproduction steps, and a suggested mitigation where possible. Do not include real credentials, private data, or secrets in a report.

## Supported versions

Only the latest version on the default branch is actively maintained.

## Security practices

- Keep dependencies minimal; the teaching programs currently use the Python standard library.
- Never commit API keys, passwords, tokens, private keys, or local `.env` files.
- Review third-party GitHub Actions and pin actions to trusted releases.
- CI jobs should use the least permissions required.
