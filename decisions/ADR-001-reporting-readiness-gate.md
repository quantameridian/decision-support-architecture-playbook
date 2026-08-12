# ADR-001: Gate Management Reporting On Explicit Data Readiness

| Field | Value |
| --- | --- |
| Status | Accepted for scenario |
| Date | 2026-08-12 |
| Owner | Reporting Assurance Owner |
| Decision roles | Report Owner, KPI Owner, Decision Owner |
| Requirements | `BR-01`, `BR-02`, `NFR-04` |
| Risks | `RSK-01`, `RSK-04` |

## Context

A successful technical refresh does not prove that an output is suitable for a management decision. The source can arrive late, mandatory fields can be absent, or a high impact exception can remain unresolved while every pipeline step reports success.

The service needs a separate readiness decision that can stop publication or allow a named owner to accept a visible caveat. That decision must be recoverable from evidence after the meeting.

## Options

| Option | Benefit | Cost and risk |
| --- | --- | --- |
| Publish whenever refresh succeeds | Fast and simple | Hides business quality failures and confuses technical success with assurance |
| Block on every failed rule | Strong consistency | A low impact defect can prevent a time critical review |
| Apply severity based readiness | Distinguishes blocker, caveat and warning outcomes | Requires agreed rules, ownership and recorded judgement |

## Decision

The Quality Gate will assign every run one of three outcomes:

- `Ready`: no unresolved blocker and the quality summary is complete.
- `Ready with caveat`: no blocker remains, but an accountable owner has accepted a documented limitation for this cycle.
- `Not ready`: a blocker remains or the source evidence is incomplete.

Only the first two outcomes can reach publication. A caveat needs an owner, expiry date, affected KPI and recorded rationale. The quality result, exception set, approval and published report version are retained together.

## Consequences

The design makes management risk visible and gives the Report Owner a defensible release decision. It also introduces an operational dependency: quality severity, approval authority and escalation times must be maintained, not left to analyst judgement.

The gate can delay publication. That is intentional for material defects, but repeated delays should trigger source remediation rather than permanent waiver use.

## Verification

- A synthetic blocking failure produces `Not ready` and no publication approval.
- A medium issue cannot produce `Ready with caveat` without owner, rationale and expiry date.
- A clean run links source receipt, quality result, approval and report version.
- A sampled cycle can be reconstructed from the Evidence Store.

## Review Triggers

Review this decision when publication frequency changes, quality severity changes, a caveat is repeatedly renewed, or regulation requires a stricter release rule.
