# KPI Dictionary

## Definition Policy

Each KPI starts with the decision it supports, then states grain, time basis, formula, exclusions, quality dependencies, owner and interpretation. A report label is not a definition. Material semantic changes require approval and a decision record when they alter architecture or business meaning.

## Current Backlog

| Field | Definition |
| --- | --- |
| Decision | Where does unresolved work require capacity or priority action? |
| Owner | Head of Service Performance role |
| Grain | Distinct work item |
| Formula | Count items whose current status is Open, In Progress or Paused |
| Time basis | Current state at the report cut off |
| Exclusions | Cancelled and Closed |
| Quality dependencies | Stable item ID and valid status |
| June 2026 result | 16 |

This is not a historical series. A historical backlog measure reconstructs items opened but not closed at each past cut off. Presenting current status against old dates would create a false trend.

## Overdue Active Items

| Field | Definition |
| --- | --- |
| Decision | Which active records require immediate owner attention? |
| Owner | Service Operations Owner role |
| Grain | Distinct work item |
| Formula | Count Open or In Progress items with due date before the report date |
| Time basis | Due date compared with fixed report cut off |
| Exclusions | Paused, Closed and Cancelled records; records without due date are disclosed separately |
| Quality dependencies | Valid status, due date and report cut off |
| June 2026 result | 14 |

Missing due dates do not make an item on time. They enter the data readiness issue count.

## SLA Met Rate

| Field | Definition |
| --- | --- |
| Decision | Is completed work meeting the service commitment? |
| Owner | KPI Owner role |
| Grain | Eligible closed work item |
| Numerator | Eligible items closed on or before due date |
| Denominator | Closed items with due date, closure date and a target effective on opened date |
| Time basis | Closure period |
| Exclusions | Items without valid SLA inputs; excluded count remains visible |
| Quality dependencies | Opened, due and closed dates plus effective target match |
| June 2026 result | 9 of 13, or 69.2% |

The comparison target is the average target rate across eligible items, weighted once per item. The June result is below the 82.1% weighted target. Calendar days are used unless a later approved definition introduces working day rules.

## Data Readiness Rate

| Field | Definition |
| --- | --- |
| Decision | Is the record set reliable enough for review, and where is remediation required? |
| Owner | Reporting Assurance Owner role |
| Grain | Distinct work item |
| Formula | 1 minus records with at least one material issue divided by total records |
| Material issue | Missing owner, missing due date, missing target, or missing required closure evidence |
| Time basis | Current report cycle |
| Exclusions | None from denominator |
| June 2026 result | 25 of 32 ready, or 78.1% |

A record with several issues counts once in the rate but produces separate exception details where action differs. Evidence marked `Not required` is not treated as missing solely because the link is blank.

## Guardrails

| Guardrail | Why it is shown |
| --- | --- |
| Missing owner count | Prevents workload metrics from hiding unassigned responsibility |
| Missing due date count | Prevents overdue performance from appearing better through absent dates |
| Target coverage rate | Shows whether the SLA denominator represents the expected population |
| Closed missing evidence count | Shows whether completion can be substantiated |
| High priority overdue count | Prevents an improving average from hiding severe individual exposure |

## Approval And Change

The KPI Owner approves meaning; the Source Owner confirms field semantics; the Analytics Engineering Owner confirms transformation; the BI Owner confirms semantic implementation; and the Decision Owner confirms that interpretation supports the forum.

A definition change records old and new behaviour, affected history, reason, owner, effective date, test result and whether historical values are restated. Reports must not silently mix definition versions in one trend.
