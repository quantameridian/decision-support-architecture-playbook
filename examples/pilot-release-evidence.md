# Pilot Release Evidence

This is a filled synthetic evidence record for the June 2026 Operations Review Service cycle. It demonstrates the shape of a release decision. It is not a record from a real organisation or system.

## Cycle Identity

| Field | Value |
| --- | --- |
| Reporting period | June 2026 |
| Cut off | 2026-06-30 18:00 Europe/London |
| Source receipt | 2026-07-01 08:14 Europe/London |
| Report version | `ops-review-2026-06-r1` |
| Readiness outcome | Ready with caveat |
| Decision owner | Director of Operations role |

## Source And Reconciliation

| Check | Expected | Observed | Result |
| --- | ---: | ---: | --- |
| Source rows received | 32 | 32 | Pass |
| Distinct work item IDs | 32 | 32 | Pass |
| Accepted mart rows | 32 | 32 | Pass |
| Semantic model total items | 32 | 32 | Pass |
| Receipt inside 24 hour freshness target | Yes | 14 hours 14 minutes | Pass |

The receipt evidence would include the file checksum, source timestamp, receipt timestamp and service identity. This public example records values but does not contain a real file path, tenant identifier or credential.

## Quality Gate

| Control | Result | Material finding |
| --- | --- | --- |
| `CTL-02` Schema and key validation | Pass | Required columns and unique item IDs confirmed |
| `CTL-03` Reporting readiness gate | Caveat accepted | Seven records have at least one readiness issue |
| `CTL-04` Governed measure catalogue | Pass | 24 reference KPI results reconcile |
| `CTL-05` Dynamic service area access | Pass | Allowed, multi-area and denied identity cases pass |
| `CTL-06` Release field review | Pass | No excluded personal or special category fields found |

## Accepted Caveat

Seven records have at least one missing owner, due date, target match or required evidence value. The caveat affects the data readiness measure and record level follow up. It does not change the 32 item workload denominator.

| Field | Value |
| --- | --- |
| Caveat owner | Reporting Assurance Owner role |
| Affected output | Assurance Detail page and Data Readiness Rate |
| Rationale | The defect population is fully disclosed and can be assigned in the review forum |
| Expiry | Next monthly cycle |
| Required action | Source owners correct the seven records or provide an approved exception rationale |

## Published KPI Evidence

| KPI | Result | Interpretation |
| --- | ---: | --- |
| Current backlog | 16 | Unresolved queue at the fixed report date |
| Overdue active items | 14 | Material timeliness pressure requiring owner action |
| SLA met rate | 69.2% | Below the weighted target of 82.1% |
| Data readiness rate | 78.1% | Caveat remains visible and is not removed from the denominator |

## Access Tests

| Test | Expected | Result |
| --- | --- | --- |
| Mapped single area identity | Sees only its service area detail | Pass |
| Mapped two area identity | Sees the union of its two areas | Pass |
| Authenticated unmapped identity | Sees no detailed rows | Pass |
| Export of detailed table | Applies the same service area filter | Pass |

## Publication Decision

Publication is approved as `Ready with caveat`. The report must show the readiness rate and provide the seven affected records to authorised owners. The caveat cannot be rolled into the next cycle without a new decision.

## Decisions And Actions

| ID | Decision or action | Owner | Due | Success evidence |
| --- | --- | --- | --- | --- |
| DEC-2026-06-01 | Prioritise overdue high priority work before accepting new discretionary items | Decision Owner | 2026-07-03 | Updated priority review record |
| ACT-2026-06-01 | Correct or explain all seven readiness issues | Source Owners | 2026-07-10 | Clean quality result or approved exception record |
| ACT-2026-06-02 | Review SLA misses by category and priority | KPI Owner | 2026-07-08 | Signed analysis note linked to the next review |

## Evidence Boundary

This example demonstrates evidence design only. No pipeline ran, no identity provider was queried and no report was published for this repository. The figures align with the synthetic Power BI example, but this repository does not depend on that implementation.
