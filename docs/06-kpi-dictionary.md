# KPI Dictionary

## Purpose

A KPI dictionary defines the measures used in a reporting system before those measures appear in a dashboard, management pack, or review meeting.

In a weak reporting process, KPI logic often sits in spreadsheet formulas, presentation notes, or individual memory. Two people can use the same KPI name and mean different things. One report may count paused records as open, while another excludes them. One review may use due date for overdue reporting, while another uses review date.

The dictionary prevents that drift by making each KPI explicit:

- what the KPI means;
- what decision it supports;
- which source fields it depends on;
- what one row represents at the point of calculation;
- who owns the definition;
- how often it refreshes;
- how to interpret movement;
- what quality issues can weaken trust in the number.

The aim is not to make a long catalogue for its own sake. The aim is to make KPI logic reviewable, testable, and maintainable.

## How KPI Definitions Prevent Inconsistent Reporting

KPI definitions reduce reporting disputes by fixing the calculation rules before the output is built.

| Reporting problem | Dictionary control |
| --- | --- |
| Same KPI name used with different filters | Record the inclusion and exclusion rules |
| Manual reporting owner changes formula between cycles | Record the approved calculation and change history |
| Report users challenge why a record is counted | Record grain, source fields, and caveats |
| Targets are applied inconsistently | Record target owner, threshold, and target source |
| Data-quality issues are hidden in headline metrics | Record known quality risks and readiness checks |
| KPI is refreshed without a clear cut-off | Record refresh cadence, cut-off assumption, and owner |

A good KPI dictionary is also useful when moving between tools. The same definition can guide a SQL mart, a Power BI semantic model, a spreadsheet prototype, or a manual review pack.

## Recommended Dictionary Structure

Each KPI entry should include the fields below.

| Field | Purpose |
| --- | --- |
| KPI ID | Stable identifier used in documentation, tests, and review packs |
| KPI name | Plain-language name used by report users |
| Decision supported | The management question the KPI helps answer |
| Definition owner | Role accountable for the business meaning |
| Reporting owner | Role accountable for presenting and maintaining the output |
| Calculation grain | What one counted row represents before aggregation |
| Reporting grain | Level shown in the management output |
| Source dependency | Source table, tracker, extract, or field group needed |
| Calculation logic | Business-readable formula or rule |
| Inclusion rules | Records included in the calculation |
| Exclusion rules | Records deliberately excluded |
| Target or threshold | Target value, threshold, or statement that no target applies |
| Refresh cadence | How often the KPI is expected to refresh |
| Cut-off assumption | Date or time boundary used for reporting |
| Interpretation | How to read high, low, rising, or falling values |
| Quality risks | Data-quality issues that could distort the KPI |
| Limitation | What the KPI does not prove |
| Escalation route | Where definition or quality issues should go |

## Example KPI Entries

The examples below use safe synthetic operational reporting context. They are not client examples and do not describe a real organisation.

### KPI 001: Open Workload

| Field | Definition |
| --- | --- |
| KPI ID | KPI-001 |
| KPI name | Open workload |
| Decision supported | Does the current volume of unresolved work require prioritisation, resource review, or escalation? |
| Definition owner | Service performance owner |
| Reporting owner | Report owner |
| Calculation grain | One operational record |
| Reporting grain | Reporting period, service area, category, and owner group |
| Source dependency | Operational tracker: `record_id`, `status`, `service_area`, `category`, `owner_role`, `reporting_period` |
| Calculation logic | Count records where status is `Open`, `In progress`, or `On hold` at the reporting cut-off |
| Inclusion rules | Active records with a valid record ID and reportable service area |
| Exclusion rules | Records marked `Closed`, `Cancelled`, duplicate rows not selected as authoritative, and records outside the reporting scope |
| Target or threshold | No fixed target; reviewed against trend, service capacity, and agreed tolerance |
| Refresh cadence | Weekly for operational review; monthly for management pack |
| Cut-off assumption | Status as at the agreed reporting cut-off date |
| Interpretation | Rising workload may indicate higher demand, slower throughput, unresolved blockers, or wider capture of work |
| Quality risks | Invalid statuses, duplicate IDs, missing service area, unclear ownership, late source updates |
| Limitation | Does not explain why workload changed without supporting flow, closure, and category measures |
| Escalation route | Definition issue to service performance owner; data issue to source data owner |

### KPI 002: Overdue Action Rate

| Field | Definition |
| --- | --- |
| KPI ID | KPI-002 |
| KPI name | Overdue action rate |
| Decision supported | What share of active work has missed its agreed action date? |
| Definition owner | Review forum owner |
| Reporting owner | Report owner |
| Calculation grain | One active operational record with an action due date |
| Reporting grain | Reporting period, service area, owner group, and risk rating |
| Source dependency | Operational tracker: `record_id`, `status`, `action_due_date`, `risk_rating`, `action_owner` |
| Calculation logic | Overdue active records divided by active records with an action due date |
| Inclusion rules | Active records where an action due date is required |
| Exclusion rules | Closed records, cancelled records, records with accepted no-date caveat, and records outside the reporting scope |
| Target or threshold | Example threshold: less than 10 percent overdue for routine review; zero tolerance for high-risk overdue records without owner |
| Refresh cadence | Weekly for action review |
| Cut-off assumption | Due date compared with the reporting cut-off date |
| Interpretation | A higher rate points to follow-up risk; high-risk overdue records should be reviewed individually |
| Quality risks | Missing due dates, date parsing errors, stale statuses, missing action owner, unclear exception ownership |
| Limitation | Does not prove poor performance if actions were legitimately paused or awaiting external input |
| Escalation route | High-risk overdue items to decision owner; missing owner/date issues to source data owner |

### KPI 003: Reporting Readiness Exception Count

| Field | Definition |
| --- | --- |
| KPI ID | KPI-003 |
| KPI name | Reporting readiness exception count |
| Decision supported | Is the dataset clean enough to use in a formal review pack? |
| Definition owner | Reporting assurance owner |
| Reporting owner | Report owner |
| Calculation grain | One failed quality rule for one source record |
| Reporting grain | Reporting period, rule, severity, service area, and owner group |
| Source dependency | Data quality exception register: `rule_id`, `severity`, `record_id`, `field`, `issue`, `status` |
| Calculation logic | Count open quality exceptions raised before publication |
| Inclusion rules | Open exceptions that affect the reporting period or headline outputs |
| Exclusion rules | Closed exceptions, duplicate exception rows, and accepted caveats that have been approved for the cycle |
| Target or threshold | No high-severity exceptions affecting headline outputs before formal publication |
| Refresh cadence | Every reporting cycle before publication |
| Cut-off assumption | Exceptions generated from source data received at the reporting cut-off |
| Interpretation | A higher count means more caveats, correction work, or publication risk |
| Quality risks | Rule catalogue not maintained, exceptions not deduplicated, closed issues not evidenced |
| Limitation | Counts visible exceptions only; it does not detect issues that no rule has been designed to find |
| Escalation route | High-severity exceptions to reporting assurance owner and decision owner |

### KPI 004: Evidence Completion Rate

| Field | Definition |
| --- | --- |
| KPI ID | KPI-004 |
| KPI name | Evidence completion rate |
| Decision supported | Are closed or completed records supported by evidence before they are reported as resolved? |
| Definition owner | Assurance owner |
| Reporting owner | Report owner |
| Calculation grain | One record that requires evidence |
| Reporting grain | Reporting period, service area, category, and closure status |
| Source dependency | Operational tracker: `record_id`, `status`, `closure_evidence`, `evidence_link`, `closed_date` |
| Calculation logic | Records with required evidence present divided by records requiring evidence |
| Inclusion rules | Closed or completed records where the process requires evidence |
| Exclusion rules | Records where evidence is explicitly not required and the caveat is approved |
| Target or threshold | Example threshold: 95 percent for routine closure evidence; 100 percent for high-risk closures |
| Refresh cadence | Monthly for assurance review; before any closure performance pack |
| Cut-off assumption | Evidence present at the reporting cut-off |
| Interpretation | Low completion rate weakens confidence in closure reporting and may indicate process follow-up issues |
| Quality risks | Broken evidence links, inconsistent evidence naming, missing closure status, evidence recorded outside the agreed source |
| Limitation | Presence of evidence does not prove that the evidence is sufficient or has been independently reviewed |
| Escalation route | Missing evidence to source owner; repeated gaps to assurance owner |

## Ownership Rules

KPI ownership should be split clearly:

| Role | Responsibility |
| --- | --- |
| Definition owner | Approves business meaning, inclusion rules, exclusions, targets, and interpretation |
| Source data owner | Maintains the source fields needed for the KPI |
| Reporting owner | Publishes the KPI and keeps caveats visible |
| Analytics or BI owner | Implements the calculation in SQL, semantic model, report, or manual pack |
| Decision owner | Uses the KPI in review and resolves disputed definitions when they affect action |

One person may hold more than one role in a small team, but the responsibilities should still be written down.

## Change Control

KPI definitions should not change silently. A simple change record should capture:

- KPI ID and name;
- requested change;
- reason for change;
- fields, filters, or targets affected;
- expected impact on prior results;
- approval owner;
- implementation owner;
- effective reporting period;
- whether historic results will be restated.

Definition changes should be visible in the next reporting pack if they affect trend interpretation.

## Acceptance Criteria

A KPI dictionary is ready to support decision support when:

- every headline KPI has one approved definition;
- calculation grain and reporting grain are clear;
- source fields and owner roles are named;
- inclusion and exclusion rules are explicit;
- refresh cadence and cut-off assumptions are documented;
- quality risks are visible;
- limitations explain what the KPI does not prove;
- changes are recorded rather than hidden in report logic.
