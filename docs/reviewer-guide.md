# Reviewer Guide

This guide is for an external reviewer who wants to understand the architecture evidence quickly. The repo should be judged as a public playbook with synthetic examples, not as proof of live client delivery.

## What To Review First

1. [docs/00-executive-brief.md](00-executive-brief.md) for the short framing.
2. [docs/04-source-to-output-map.md](04-source-to-output-map.md) for lineage and control placement.
3. [docs/05-data-quality-controls.md](05-data-quality-controls.md) for data quality gate design.
4. [docs/07-operating-model.md](07-operating-model.md) for roles, cadence, escalation, change control, and handover.
5. [docs/11-security-architecture.md](11-security-architecture.md) for classification, access, auditability, and public and private boundaries.
6. [examples/architecture-decision-record-example.md](../examples/architecture-decision-record-example.md) for a filled ADR with tradeoffs.
7. [docs/commercial-review-scorecard.md](commercial-review-scorecard.md) for the plain assessment of the repo.
8. [examples/manual-reporting-transformation-example.md](../examples/manual-reporting-transformation-example.md) for the applied synthetic walkthrough.

## What This Repository Proves

| Skill | Evidence |
| --- | --- |
| Reporting architecture | Current state, target state, source to output, and lifecycle documents |
| Operating model design | Roles, ownership, review cadence, escalation, change control, and handover docs |
| Decision support thinking | Links reporting outputs to review forums, action ownership, and feedback loops |
| Security architecture thinking | Classification, access boundaries, audit evidence, and regulated environment considerations are documented |
| Tradeoff documentation | Filled ADR example shows context, options, decision, consequences, and acceptance criteria |
| Stakeholder documentation | Templates for requirements, KPI definitions, quality rules, reviews, and ADRs |
| Public repo hygiene | CI, docs validator, CodeQL, OpenSSF Scorecard, and public document security posture are present |

## Portfolio Reading

The strongest evidence is the route from problem framing to controlled decision support. Read the problem statement, then move through target state, source to output mapping, quality controls, KPI dictionary, operating model, and the filled ADR example. That path is what makes the repo useful for architecture and decision support roles.

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
- Are source to output controls placed before management review?
- Does the roadmap sequence discovery, controls, build, and handover realistically?
- Is the public document boundary clear enough to avoid leaking real organisation details?

## Current Limitations

- Documentation artifact, not a production implementation.
- Synthetic examples only.
- No real platform deployment or organisation specific discovery.
- Strongest when reviewed with the Python, dbt, and Power BI repos.

## Strongest Interview Angle

Use this repo to discuss how you would move a reporting process from informal spreadsheet work to a controlled decision support model: source to output mapping, KPI ownership, quality gates, review cadence, security boundaries, and handover.
