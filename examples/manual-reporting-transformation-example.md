# Manual Reporting Transformation Example

## Purpose

This walkthrough shows how the playbook could be applied to a generic manual reporting process. It is a fictional, non-client example designed to demonstrate architecture thinking. It does not describe a real organisation, client, employer, official process, or protected dataset.

## Scenario

A service team produces a monthly management pack from an operational tracker. The tracker is maintained by several people and exported into spreadsheets before the report is created.

The team wants the management pack to answer:

- how much work is open;
- how many items are overdue;
- which service areas have the largest backlog;
- which high-priority items need escalation;
- whether closed items have enough evidence for review;
- which data-quality issues weaken trust in the report.

The current reporting routine works, but it depends heavily on manual effort and individual knowledge.

## Current state

| Area | Current behaviour | Problem created |
| --- | --- | --- |
| Source data | Operational tracker exported monthly | No formal source-to-output map |
| KPI definitions | Open, overdue, and high-priority items defined in old spreadsheet formulas | Definitions are hard to review |
| Data preparation | Analyst cleans dates, statuses, owners, and evidence fields manually | Corrections are not consistently logged |
| Exception tracking | Issues are highlighted in spreadsheet tabs | No controlled owner, severity, or closure route |
| Dashboard/report pack | Management pack is refreshed manually | Users cannot always tell whether data is ready |
| Review meeting | Actions are discussed and captured separately | Decisions do not always feed back into source corrections |
| Handover | Process known by one main report owner | High continuity risk |

## Step 1: Frame the reporting requirement

The reporting requirement is written as a decision-support need:

| Requirement item | Example entry |
| --- | --- |
| Decision supported | Monthly review of workload, overdue items, evidence gaps, and escalation priorities |
| Audience | Service manager, reporting lead, assurance lead, action owners |
| Reporting cadence | Monthly management review with pre-review data-quality check |
| Output required | Management pack or dashboard with KPI summary, quality caveats, and exception detail |
| Required action | Agree owners and due dates for high-risk overdue items and data-quality exceptions |

This prevents the build from starting with visuals before the management question is clear.

## Step 2: Build the source-to-output map

The team maps each output back to the source fields needed to produce it.

| Output | Source fields | Control needed | Owner |
| --- | --- | --- | --- |
| Open item count | `record_id`, `status` | Accepted status values | Report owner |
| Overdue item count | `record_id`, `status`, `due_date` | Required due date for active records | Reporting assurance owner |
| High-priority overdue items | `record_id`, `priority`, `status`, `due_date`, `owner_role` | Owner required for high-priority overdue records | Decision owner |
| Evidence gap count | `record_id`, `status`, `closure_evidence` | Closed records must have evidence where required | Assurance lead |
| Backlog by service area | `record_id`, `service_area`, `status` | Service area required and valid | Data owner |

The source-to-output map makes it clear which data fields matter and where checks are needed.

## Step 3: Define KPI rules

Example KPI definitions are documented before the report is rebuilt.

| KPI | Definition | Caveat |
| --- | --- | --- |
| Open items | Count of records where status is `Open` or `In Progress` | Excludes paused and cancelled records |
| Overdue active items | Count of open or in-progress records where due date is before report date | Records missing due date are shown as data-quality exceptions |
| High-priority overdue items | Count of high or critical priority active records past due date | Priority definitions must be maintained consistently |
| Closed missing evidence | Count of closed records where closure evidence is blank or marked missing | Evidence sufficiency is not validated automatically |

This reduces definition drift across reports and review meetings.

## Step 4: Add data-quality controls

The quality controls are placed before the management output is published.

| Rule ID | Rule | Severity | Recommended action |
| --- | --- | --- | --- |
| DQ-001 | Active records must have an owner role | High for high-priority overdue records | Assign owner before review |
| DQ-002 | Active records must have a due date | Medium to high depending on priority | Add due date or caveat overdue KPI |
| DQ-003 | Status must match agreed list | Medium | Correct source status or update reference list |
| DQ-004 | Closed records must have closure evidence where required | Medium | Add evidence or flag for assurance review |
| DQ-005 | Duplicate record IDs are not allowed | High | Resolve duplicate before publishing totals |

The output does not need to be perfect before review, but its limitations must be visible.

## Step 5: Create an exception register

Instead of leaving issues in comments or spreadsheet colours, exceptions are recorded consistently.

| Exception field | Example value |
| --- | --- |
| Exception ID | EX-0001 |
| Record ID | REC-0142 |
| Rule ID | DQ-001 |
| Severity | High |
| Issue | High-priority overdue record has no owner |
| Recommended action | Assign owner before management review |
| Action owner | Service manager |
| Due date | Before next review pack |
| Status | Open |

This makes exception ownership and closure visible.

## Step 6: Define the review rhythm

The management review is redesigned as a small cycle:

| Timing | Activity |
| --- | --- |
| Five working days before review | Source owner confirms extract is available |
| Four working days before review | Reporting owner refreshes model and runs quality checks |
| Three working days before review | Assurance owner reviews high-severity exceptions |
| One working day before review | Report owner publishes pack with caveats |
| Review meeting | Decision owner agrees actions, owners, and due dates |
| After review | Action log updated; recurring issues reviewed for rule or source fixes |

The review rhythm turns reporting from a pack-production exercise into a decision process.

## Step 7: Define escalation

| Trigger | Escalation |
| --- | --- |
| Source extract missing | Report owner escalates to data owner |
| High-priority overdue item has no owner | Decision owner assigns owner in review |
| KPI definition disputed | KPI owner confirms definition before next publication |
| Quality issue repeats for two cycles | Reporting assurance owner reviews root cause with source owner |
| Manual correction repeats | Analytics owner converts correction into documented transformation or source fix |

Escalation is kept simple so it can be used without a large governance process.

## Step 8: Prepare handover

The handover pack includes:

- reporting purpose and audience;
- source-to-output map;
- KPI dictionary;
- quality rule catalogue;
- refresh checklist;
- exception register structure;
- review rhythm;
- escalation route;
- known limitations;
- change log.

The goal is that another reporting owner could pick up the process without relying on the previous owner’s memory.

## Expected target-state improvement

| Current issue | Target-state improvement |
| --- | --- |
| Spreadsheet logic is hidden | KPI definitions and transformations are documented |
| Exceptions are informal | Exception register records rule, severity, owner, and action |
| Review rhythm is unclear | Reporting cycle has pre-review checks and post-review follow-up |
| Dashboard trust is low | Outputs include readiness checks and caveats |
| Handover is fragile | Handover pack explains route, owners, checks, and failure points |

## Limits of the example

- This is not client work.
- The example does not use real source data.
- The example does not claim a platform deployment.
- The walkthrough demonstrates architecture application, not a full technical implementation.
- A real organisation would need discovery, security review, data profiling, stakeholder agreement, and tool-specific design.
