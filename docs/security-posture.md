# Security Posture

## Scope

This is a public documentation-led architecture playbook. It must be safe for
full public review and must not contain client names, employer material, internal
process diagrams, private meeting notes, real system inventories, or confidential
operating-model details.

## Current Controls

- GitHub Actions CI uses read-only repository contents permission.
- CodeQL scans the Python validation script.
- OpenSSF Scorecard runs on the public repository and uploads SARIF results.
- Dependabot version updates are configured for GitHub Actions.
- The repository validator checks required docs, Mermaid diagrams, and local links.
- Security reporting instructions are documented in `SECURITY.md`.

## Public Documentation Boundary

Architecture documents can leak sensitive information even when they contain no
code. Before committing, review every document, diagram, and template for:

- client, employer, supplier, or stakeholder names;
- real system names, internal URLs, ticket IDs, and platform identifiers;
- security-control gaps copied from a real organisation;
- non-public operating procedures or escalation routes;
- meeting notes, action owners, or incident details;
- screenshots or diagrams copied from internal tools.

## GitHub Settings To Keep Enabled

These controls live in GitHub repository settings rather than source files:

- secret scanning and push protection;
- Dependabot alerts and Dependabot security updates;
- branch protection or repository rulesets for `main`;
- required CI checks before merging;
- blocked force pushes and branch deletion;
- default workflow token permission set to read-only.

## Residual Risk

This repository does not implement a production platform and does not prove
security architecture delivery. Its main public risk is information leakage
through narrative documents and diagrams. Treat all committed examples as
synthetic, generic, and intentionally non-client.
