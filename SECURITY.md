# Security Policy

## Supported Scope

This repository contains documentation, YAML, Mermaid and validation scripts for a synthetic architecture case. It does not process production data or provide a deployed service.

Security fixes are supported on the default branch. Public examples must remain synthetic and must not contain real client, employee, supplier or operational information.

## Report A Problem

Do not open a public issue for a suspected secret, private architecture detail or exploitable workflow problem. Use [GitHub private vulnerability reporting](https://github.com/quantameridian/decision-support-architecture-playbook/security/advisories/new), or contact the repository owner through the GitHub profile.

Include the affected file or workflow, reproduction detail, likely impact and a safe remediation suggestion. Do not include a live credential or sensitive source record in the report.

## Data Boundary

Do not submit real system names, internal URLs, tenant identifiers, account IDs, credentials, network routes, incident records, meeting notes or copied organisation diagrams. The validator checks common local path and secret patterns, but human review remains necessary because sensitive context can appear as ordinary prose.
