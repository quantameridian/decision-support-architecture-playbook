# Operating Model

## Accountabilities

| Role | Accountable for | Cannot delegate without record |
| --- | --- | --- |
| Decision Owner | Forum decision, priority and acceptance of material caveats | Publication against a blocker |
| Service Owner | End to end service health, recovery and evidence retention | RTO, RPO and operating risk acceptance |
| Information Owner | Classification, permitted fields and retention | Sensitive field approval |
| Source Owner | Source meaning, quality and delivery | Correction of authoritative records |
| Platform Owner | Controlled receipt, runtime platform and service identities | Platform release and privileged runtime access |
| KPI Owner | Definition, target and interpretation | Semantic approval |
| Reporting Assurance Owner | Quality rules, severity and readiness | Readiness outcome |
| Analytics Engineering Owner | Reporting mart, lineage and data contracts | Transformation release |
| BI Owner | Semantic model, report performance and access rule implementation | Model release evidence |
| Security Owner | Threat treatment and access assurance | Security exception acceptance |
| Identity Owner | Authentication integration, group lifecycle and revocation | Identity policy and group control |
| Report Owner | Cycle coordination, publication and caveat display | Named report version approval |

## RACI

`A` is accountable, `R` performs the work, `C` is consulted and `I` is informed.

| Activity | Decision | Service | Source | KPI | Assurance | Engineering | BI | Security | Report |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Confirm source contract | I | C | A/R | C | C | C | I | C | I |
| Approve KPI definition | C | I | C | A | C | R | R | I | I |
| Run quality gate | I | I | C | C | A | R | I | I | I |
| Decide readiness | C | I | C | C | A/R | I | I | C | C |
| Approve publication | I | C | I | C | C | I | R | I | A |
| Accept material caveat | A | C | C | C | R | I | I | C | C |
| Grant detail access | I | C | I | I | I | I | R | A | I |
| Run recovery exercise | I | A | C | I | C | R | R | C | C |
| Record decisions and actions | A | I | I | I | I | I | I | I | R |

## Monthly Cycle

| Time | Activity | Exit evidence |
| --- | --- | --- |
| Prior month | Confirm material definition, source and access changes | Approved change record or no change statement |
| First working day | Receive source and validate provenance | `EVD-01` |
| First to second working day | Run controls, correct source and issue readiness | `EVD-02`, `EVD-03` |
| Second working day | Refresh model, run access and performance checks | `EVD-05`, `EVD-11` |
| Third working day before 09:00 | Approve and publish named report version | `EVD-07` |
| Review forum | Agree decisions, actions, owners and dates | `EVD-08` |
| After review | Route corrections and update control backlog | Updated action register |

## Failure And Escalation

| Failure | First response | Escalation time |
| --- | --- | --- |
| Extract not received | Platform Owner checks transfer; Source Owner confirms availability | By 12:00 on first working day |
| Quality blocker | Assurance Owner rejects release and routes exceptions | Immediately after gate result |
| Mart or model refresh failure | Engineering or BI Owner retries from last accepted evidence | Escalate to Service Owner after one hour |
| Access test failure | Security Owner blocks release of detail | Immediate |
| Report unavailable at deadline | Service Owner invokes approved continuity output | Before publication deadline |
| Action remains overdue | Decision Owner reviews priority and accountability | Next forum or sooner for high impact action |

## Change Control

Routine changes include corrected source values, non semantic report wording and owner substitutions within an approved role. Material changes include grain, key, KPI meaning, source authority, trust boundary, access scope, retention, recovery target or component responsibility.

Material changes need impact analysis against requirements, risks, controls and evidence. Accepted ADRs are not edited to make history look cleaner; a new record supersedes the old decision.

## Service Review

Quarterly service review samples one retained cycle, exercises recovery, reviews access membership, checks recurring caveats, reassesses residual risks and confirms that owners can still perform the runbook. Production approval would also need cost, capacity, support and incident evidence that this logical design does not yet provide.
