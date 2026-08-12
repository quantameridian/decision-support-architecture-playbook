# Service Operation And Handover

## Daily Refresh Runbook

1. Confirm the scheduled extract arrived inside the source contract window.
2. Verify checksum, source timestamp, receipt timestamp and contract version.
3. Run the Quality Gate and review blocker, caveat and warning counts.
4. Stop if the result is `Not ready`; route each blocker to its owner.
5. Load accepted data into the Reporting Mart atomically.
6. Refresh the Semantic Model and reconcile fact, dimension and KPI results.
7. Run access and performance checks required for the release type.
8. Record the readiness result and any accepted caveat.
9. Approve and publish the named report version.
10. Store cycle evidence under one reporting cycle ID.

## Recovery Runbook

| Step | Action | Evidence |
| --- | --- | --- |
| 1 | Declare the failed stage and affected cycle | Incident timestamp and owner |
| 2 | Preserve failed logs and inputs | Evidence references |
| 3 | Select the last accepted receipt or corrected replacement | Checksum and acceptance record |
| 4 | Rebuild quality, mart and model layers in order | Stage results and reconciliations |
| 5 | Run access, KPI and report smoke checks | Test result |
| 6 | Publish only after a new readiness and approval decision | New report version |
| 7 | Compare elapsed recovery with eight business hour RTO | Recovery exercise result |
| 8 | Record cause, impact and preventive action | Incident review |

The proposed RPO is 24 hours. If a failure would lose more accepted data, the Service Owner must stop normal recovery and obtain a risk decision before publication.

## Continuity Output

If the normal report cannot meet the forum deadline, the Service Owner can invoke a preapproved continuity output containing the last accepted results, clear age, known incident, affected decisions and next update time. It must not be presented as current data.

## Monitoring

| Signal | Alert condition | Owner |
| --- | --- | --- |
| Source receipt | Missing or more than 24 hours behind cut off | Platform Owner |
| Quality gate | Any blocker or incomplete check set | Reporting Assurance Owner |
| Mart load | Rejected atomic load or count mismatch | Analytics Engineering Owner |
| Model refresh | Failure or KPI reconciliation mismatch | BI Owner |
| Access test | Any denied case returns detail | Security Owner |
| Publication | No approved version by deadline | Report Owner and Service Owner |
| Action register | Material action lacks owner or due date | Decision Owner |
| Evidence retention | Sampled cycle cannot be reconstructed | Service Owner |
| Stage failure alert | Accountable owner is not notified inside 15 minutes | Platform Owner and Service Owner |

## Handover Contents

Handover includes the architecture catalogue, current ADRs, source contract, data model, KPI definitions, quality rules, access mapping ownership, runbooks, monitoring routes, evidence location, open risks, recent incidents, support contacts by role and current action backlog.

## Handover Test

An operator who did not build the service completes one refresh and one recovery exercise from maintained documentation. The test fails when the operator needs an undocumented path, personal credential, local file or verbal definition. Findings enter the service backlog before handover acceptance.

## Removal And Role Change

Handover includes revocation. Departing owners lose privileged access, scheduled identities remain non personal, group membership is reviewed and local copies are removed under the organisation records policy. A replacement owner accepts the open risks and recurring duties explicitly.
