# Reviewer Guide

## What To Review First

1. [docs/00-executive-brief.md](00-executive-brief.md) for the short commercial framing.
2. [docs/04-source-to-output-map.md](04-source-to-output-map.md) for lineage and control placement.
3. [docs/05-data-quality-controls.md](05-data-quality-controls.md) for data-quality gate design.
4. [docs/07-operating-model.md](07-operating-model.md) for roles, cadence, escalation, change control, and handover.
5. [examples/manual-reporting-transformation-example.md](../examples/manual-reporting-transformation-example.md) for the applied synthetic walkthrough.

## What This Repository Proves

| Skill | Evidence |
| --- | --- |
| Reporting architecture | Current-state, target-state, source-to-output, and lifecycle documents |
| Operating-model design | Roles, ownership, review cadence, escalation, change control, and handover docs |
| Decision-support thinking | Links reporting outputs to review forums, action ownership, and feedback loops |
| Stakeholder documentation | Templates for requirements, KPI definitions, quality rules, reviews, and ADRs |
| Public repo hygiene | CI, docs validator, CodeQL, OpenSSF Scorecard, and public-document security posture are present |

## Fast Local Review

```bash
make qa
```

Expected result:

- required markdown assets exist;
- Mermaid diagrams are present and parse as diagram-like source;
- local markdown links are checked;
- validation report is regenerated.

## Good Reviewer Questions

- Does the playbook explain the decision the reporting process supports?
- Are KPI ownership and quality responsibilities explicit?
- Are source-to-output controls placed before management review?
- Does the roadmap sequence discovery, controls, build, and handover realistically?
- Is the public-document boundary strong enough to avoid leaking real organisation details?

## Current Limitations

- Documentation-led artifact, not a production implementation.
- Synthetic examples only.
- No real platform deployment, security architecture, or organisation-specific discovery.
- Strongest when reviewed with the Python, dbt, and Power BI repos.
