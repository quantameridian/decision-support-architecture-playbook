# Repository Security Posture

## Scope

The repository publishes a synthetic architecture case. Its largest direct risk is disclosure through apparently harmless prose, diagrams, filenames or copied examples. No production secrets are required to run the checks.

## Source Controls

- GitHub workflow permissions default to read only contents.
- Action dependencies are pinned to full commit hashes.
- CodeQL analyses the Python validator.
- OpenSSF Scorecard runs on the default branch and uploads SARIF.
- Dependabot covers GitHub Actions, npm and Python dependencies.
- The validator rejects common credential markers, local user paths and retired internal review files.
- Mermaid and YAML are parsed rather than accepted by filename.
- Generated traceability evidence must match the catalogue in CI.

## Content Review

Before publication, inspect documents and diagrams for real organisation names, internal systems, network routes, tenant identifiers, ticket numbers, security gaps, personal details, meeting records and copied operating procedures. Automated matching cannot recognise every sensitive inference.

## Repository Settings

Keep secret scanning, push protection, Dependabot alerts and security updates enabled. Protect `main` with required CI and CodeQL checks, blocked force pushes and review before merge. Keep the default workflow token read only.

## Residual Risk

Pinned dependencies and scanning reduce common repository risk but do not make a public document set non sensitive. The synthetic case should be reviewed as if every committed line will be indexed permanently. The logical security design in [Security Architecture](11-security-architecture.md) is not evidence of a deployed control.
