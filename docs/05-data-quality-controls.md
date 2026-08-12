# Data Quality And Release Controls

## Control Objective

The service must prevent a technically successful run from publishing data that is materially unsuitable for a management decision. It must also avoid blocking a time critical review for a disclosed low impact defect.

[ADR-001](../decisions/ADR-001-reporting-readiness-gate.md) therefore defines three release outcomes: `Ready`, `Ready with caveat` and `Not ready`.

## Control Catalogue

| ID | Control | Type | Owner | Evidence |
| --- | --- | --- | --- | --- |
| `CTL-01` | Record extract checksum and timestamps | Preventive | Platform Owner | `EVD-01` receipt record |
| `CTL-02` | Validate schema, keys, references and dates | Preventive | Reporting Assurance Owner | `EVD-02` quality result |
| `CTL-03` | Issue explicit reporting readiness | Preventive | Reporting Assurance Owner | `EVD-03` readiness decision |
| `CTL-04` | Version and approve measures | Preventive | KPI Owner | `EVD-04` definition version |
| `CTL-05` | Filter detail by identity and service area | Preventive | Security Owner | `EVD-05` access test |
| `CTL-06` | Review fields against excluded data classes | Preventive | Information Owner | `EVD-06` field review |
| `CTL-07` | Approve a named report version before release | Preventive | Report Owner | `EVD-07` publication approval |
| `CTL-08` | Check decision and action completeness | Detective | Decision Owner | `EVD-08` review record check |
| `CTL-09` | Sample retained cycle evidence | Detective | Service Owner | `EVD-09` quarterly sample |
| `CTL-10` | Exercise refresh recovery | Corrective | Service Owner | `EVD-10` recovery record |
| `CTL-11` | Measure report render time | Detective | BI Owner | `EVD-11` performance result |

## Readiness Policy

| Outcome | Minimum condition | Publication |
| --- | --- | --- |
| Ready | All checks ran, no blocker remains and evidence is complete | Permitted |
| Ready with caveat | No blocker remains; each material caveat has owner, impact, rationale and expiry | Permitted with visible caveat |
| Not ready | A blocker remains, checks did not complete or provenance is missing | Prohibited |

The Decision Owner can invoke a documented continuity report when the normal service is unavailable. That is a separate contingency output, not a way to relabel failed data as ready.

## Pilot Rules

| Rule | Condition | Severity | Route |
| --- | --- | --- | --- |
| DQ-001 Source receipt | Extract absent or checksum unavailable | Blocker | Platform Owner and Source Owner |
| DQ-002 Stable key | Work item ID missing or duplicated | Blocker | Source Owner |
| DQ-003 Reference integrity | Status, priority or service area is unknown | Blocker | Source Owner and KPI Owner |
| DQ-004 Required ownership | Active item has no owner | Caveat | Service Area Owner |
| DQ-005 Timeliness input | Active item has no due date | Caveat | Source Owner |
| DQ-006 Target coverage | SLA item has no effective target | Caveat | KPI Owner |
| DQ-007 Closure evidence | Closed item requiring evidence has no link | Caveat | Service Area Owner |
| DQ-008 Prohibited field | Excluded personal or special category field enters the mart | Blocker | Information Owner and Security Owner |

Severity is not inferred from row count alone. One prohibited field can be a blocker, while several missing optional notes may be warnings. The rule owner must define the decision risk and false positive treatment before activation.

## Exception Lifecycle

Every exception records cycle ID, rule ID, record ID, severity, affected output, owner, due date, status and closure evidence. A caveat also records acceptance rationale and expiry. Closing an exception requires source correction, an approved rule change or documented evidence that the result was a false positive.

Repeated waivers are treated as a control design problem. Three consecutive caveats for the same cause trigger review by the Reporting Assurance Owner and Service Owner.

## Test Evidence

The pilot must include clean, boundary and failure fixtures. At minimum, it should prove duplicate key rejection, unknown reference rejection, missing owner caveat, prohibited field rejection and a clean run. The release evidence example shows the intended [cycle record](../examples/pilot-release-evidence.md), but no runtime is claimed here.
