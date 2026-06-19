# Implementation Roadmap

## Purpose

This roadmap shows how a team could move from manual reporting to a controlled decision-support reporting process. It is generic and non-client. It supports the walkthrough in `examples/manual-reporting-transformation-example.md`.

## Roadmap principles

- Start by clarifying the decision, not the dashboard layout.
- Make source-to-output flow visible before changing tools.
- Define KPI ownership before formal publication.
- Put data-quality checks before management review.
- Use small implementation stages so risk is visible.
- Maintain handover material from the beginning.

## Stage 1: Discovery and reporting problem framing

| Area | Detail |
| --- | --- |
| Objective | Understand the current reporting process and the decisions it should support |
| Key activities | Interview report users, inspect current packs, list recurring questions, identify manual steps |
| Outputs | Problem statement, current-state summary, initial stakeholder list |
| Acceptance criteria | The management question, audience, cadence, and pain points are documented |
| Main risk | Jumping into dashboard rebuild before agreeing the decision process |

## Stage 2: Source and KPI inventory

| Area | Detail |
| --- | --- |
| Objective | Identify source data, key fields, KPI definitions, and ownership gaps |
| Key activities | Map source fields, document KPI formulas, identify source owner and KPI owner |
| Outputs | Source-to-output draft, KPI definition drafts, ownership gaps |
| Acceptance criteria | Each headline KPI has a source route, formula, owner, and caveat |
| Main risk | Treating old spreadsheet formulas as approved definitions without review |

## Stage 3: Quality control design

| Area | Detail |
| --- | --- |
| Objective | Define checks that show whether the report is ready for management use |
| Key activities | Define required field checks, ownership checks, duplicate checks, evidence checks, target coverage checks |
| Outputs | Data-quality rule catalogue, exception register structure, readiness states |
| Acceptance criteria | High-severity exceptions have escalation route and owner |
| Main risk | Creating checks that find issues but do not route them to action |

## Stage 4: Reporting model and output redesign

| Area | Detail |
| --- | --- |
| Objective | Move repeatable logic out of unmanaged spreadsheets and into a documented reporting route |
| Key activities | Define transformation rules, model grain, semantic measures, and report sections |
| Outputs | Reporting model design, KPI summary, exception detail, caveats section |
| Acceptance criteria | A reviewer can trace each headline KPI back to source fields and definitions |
| Main risk | Recreating the old spreadsheet in a new tool without improving control |

## Stage 5: Pilot review cycle

| Area | Detail |
| --- | --- |
| Objective | Test the target process with one reporting cycle before formalising it |
| Key activities | Run refresh, apply checks, publish draft output, hold review, capture actions |
| Outputs | Pilot pack, exception register, action log, review notes |
| Acceptance criteria | Review forum agrees whether outputs are usable and what needs correction |
| Main risk | Treating pilot results as final before quality and ownership issues are resolved |

## Stage 6: Operating model and escalation

| Area | Detail |
| --- | --- |
| Objective | Confirm who owns source data, KPI definitions, controls, publication, and follow-up |
| Key activities | Assign owners, define review rhythm, agree escalation triggers, document change process |
| Outputs | Ownership matrix, review calendar, escalation path, change log process |
| Acceptance criteria | Each recurring activity has an accountable role and review cadence |
| Main risk | Leaving ownership implicit because the first build appears to work |

## Stage 7: Handover and publication readiness

| Area | Detail |
| --- | --- |
| Objective | Make the reporting process maintainable by another owner |
| Key activities | Complete handover pack, test refresh checklist, review known issues, confirm limitations |
| Outputs | Handover pack, runbook, failure-point guide, public-readiness or internal-readiness checklist |
| Acceptance criteria | A new report owner can explain the route, refresh process, caveats, and escalation path |
| Main risk | Finishing the build without leaving enough operational documentation |

## Stage gates

| Gate | Question | Proceed when |
| --- | --- | --- |
| Gate 1 | Is the decision supported by the report clear? | Audience, decision, cadence, and output type are agreed |
| Gate 2 | Are KPI definitions agreed? | Headline KPIs have formula, owner, grain, and caveats |
| Gate 3 | Is the source-to-output route visible? | Key fields, transformations, and outputs are mapped |
| Gate 4 | Are quality controls usable? | Exceptions have severity, owner, action, and escalation |
| Gate 5 | Did the pilot support a real review rhythm? | Review produced actions and identified improvements |
| Gate 6 | Is handover good enough? | Runbook, owners, known issues, and failure points are documented |

## Example timeline

| Week | Focus |
| --- | --- |
| 1 | Discovery and current-state mapping |
| 2 | Source inventory and KPI definition |
| 3 | Quality controls and exception register design |
| 4 | Reporting model and output redesign |
| 5 | Pilot review cycle |
| 6 | Operating model, handover, and readiness review |

The timeline is illustrative. A real implementation would scale with data complexity, stakeholder availability, platform constraints, and governance requirements.

## Definition of done

The target process is ready for handover when:

- the source-to-output map is complete enough to review;
- KPI definitions are approved by named roles;
- quality controls run before publication;
- exceptions have owners and due dates;
- the review forum records decisions and actions;
- limitations are visible in the output;
- a handover pack exists and has been reviewed.
