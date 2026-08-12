# Problem Statement

## Service Context

The synthetic Operations Review Service supports a monthly management forum. Operational teams maintain work records with status, priority, owner, dates, targets and closure evidence. The forum needs a dependable view of workload, timeliness, SLA performance and record readiness.

The current route grew around a workbook and meeting deadline. It can produce a pack, but it does not operate as a controlled service.

## Current Failure Modes

| Failure mode | Operational effect | Architecture cause |
| --- | --- | --- |
| Extract arrives late or without provenance | Review is delayed or uses stale data | No receipt contract, checksum or freshness evidence |
| Workbook contains corrections and KPI formulas | Results are difficult to reproduce | Source, transformation and presentation concerns are mixed |
| KPI definitions vary by report owner | Meeting time is spent reconciling numbers | No governed semantic definition or decision history |
| Quality issues sit in comments and email | Material defects can survive publication | No severity based readiness gate or exception workflow |
| Detailed records are shared through report copies | Access drifts and revocation is unclear | Security depends on distribution rather than an identity rule |
| Decisions are recorded separately from the report | Actions lose context and ownership | The review outcome is outside the reporting lifecycle |
| Recovery depends on the analyst who built the workbook | Service continuity is fragile | No retained cycle evidence or tested runbook |

## Required Outcome

The target service must preserve a clear route from management question to source evidence and from review finding to owned action. It must make quality risk visible, apply access at the governed data layer and retain enough evidence to reconstruct what was published and why.

The design must also remain replaceable. The selected source, orchestration, storage and reporting products can change without discarding requirements, controls, interfaces or decision history.

## Success Measures

Success is not defined as “a dashboard exists”. A successful pilot proves that:

- the monthly output reaches the forum on time with documented freshness;
- headline measures reconcile to approved definitions;
- a material quality failure stops publication;
- an accepted caveat is visible, owned and expires;
- an unmapped identity receives no detailed records;
- every agreed action has an owner, due date and success evidence;
- another operator can recover and run the service from maintained records.

The complete acceptance statements are in [requirements and traceability](12-requirements-and-traceability.md).
