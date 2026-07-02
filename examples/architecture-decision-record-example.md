# Architecture Decision Record Example

## ADR-001: Place Data Quality Gates Before Management Reporting

| Field | Detail |
| --- | --- |
| Status | Accepted for portfolio example |
| Date | 2026-06-20 |
| Decision owner | Reporting architecture owner |
| Technical owner | Analytics engineering owner |
| Business owner | Decision support lead |

## Context

A manual reporting process is producing regular management outputs, but source
quality issues are being discovered during or after review meetings. This means
review time is spent debating the numbers instead of agreeing actions.

The reporting route needs a control point that checks ownership, required
fields, duplicate records, overdue items, target coverage, and closure evidence
before headline KPIs are published.

## Options Considered

| Option | Strength | Weakness |
| --- | --- | --- |
| Keep checks in spreadsheets | Fast to start and familiar to current users | Hard to test, easy to alter silently, weak handover |
| Build checks into BI visuals | Makes warnings visible in report | Still allows bad data into model and hides detailed exception ownership |
| Add quality gate before publication | Creates repeatable exception register before reporting | Requires owner process and acceptance rules |

## Decision

Use a quality gate before the management reporting layer. The
gate should generate an exception register, severity, recommended action, owner,
and readiness state before the report is treated as suitable for decision
support.

## Consequences

Positive consequences:

- headline KPIs are less likely to be used without caveats;
- exceptions can be assigned before management review;
- repeated source failures become visible;
- the reporting owner can distinguish ready, caveated, review required, and not ready states.

Tradeoffs:

- the reporting cycle needs time for exception review;
- business owners must accept or reject caveats explicitly;
- not all issues can be automated without discovery against the real source.

## Acceptance Criteria

- The data quality rule catalogue is documented.
- The exception register includes severity, owner action, and closure evidence.
- High severity issues have an escalation route.
- Publication decisions record whether the output was ready, caveated, or held.
- The handover pack explains how to run and review the gate.
