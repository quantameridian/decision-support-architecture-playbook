# Risk Register And Limitations

## Architecture Risks

| ID | Risk | Inherent view | Treatment | Residual | Owner |
| --- | --- | --- | --- | --- | --- |
| `RSK-01` | Late or incomplete source delays review | Medium likelihood, high impact | Provenance check and readiness gate | Medium | Source Owner |
| `RSK-02` | Unapproved KPI change creates inconsistent decisions | Medium likelihood, high impact | Versioned definitions, approval and ADR process | Low | KPI Owner |
| `RSK-03` | Unauthorised user sees service area detail | Low likelihood, high impact | Identity filtering, deny by default and access tests | Low | Security Owner |
| `RSK-04` | Quality failure is hidden by successful publication | Medium likelihood, high impact | Quality gate, explicit readiness and approval evidence | Medium | Reporting Assurance Owner |
| `RSK-05` | Service cannot be reconstructed after loss or owner turnover | Medium likelihood, medium impact | Evidence retention, recovery exercise and maintained runbook | Low | Service Owner |
| `RSK-06` | Pilot design fails at production volume | Medium likelihood, medium impact | Representative volume and performance test | Medium | BI Owner |
| `RSK-07` | Review finding does not become a complete owned action | Medium likelihood, high impact | Action owner, due date and success evidence check | Low | Decision Owner |
| `RSK-08` | Reporting model contains data not needed for the decision | Medium likelihood, high impact | Approved field inventory and excluded field rejection | Low | Information Owner |
| `RSK-09` | Output excludes keyboard or assistive technology users | Medium likelihood, high impact | WCAG review and equivalent tabular route | Medium | Report Owner |
| `RSK-10` | Material stage failure remains undetected until deadline | Medium likelihood, high impact | Health events and exercised alert routes | Low | Service Owner |

Residual ratings are design judgements for the synthetic case. A real risk owner would set likelihood, impact and acceptance against organisational criteria.

## Risk Decisions

Medium residual risk is not the same as accepted production risk. `RSK-01`, `RSK-04`, `RSK-06` and `RSK-09` remain pilot concerns because source behaviour, waiver use, scale and accessibility need observed evidence. The Decision Owner cannot accept security or information risk on behalf of the Security Owner or Information Owner.

## Known Design Gaps

- No physical platform, region, network route or tenant is selected.
- No production volume, concurrency profile or cost estimate exists.
- Recovery and performance targets are specified but not exercised.
- Accessibility and alert targets are specified but not exercised.
- No live identity provider, group lifecycle or export control has been tested.
- No formal privacy assessment, threat workshop or penetration test has run.
- The design does not address cross region resilience, legal hold or records disposal tooling.
- The synthetic monthly process does not prove daily or real time operation.

## Evidence Limits

The validation suite proves catalogue consistency, reference coverage, document links and Mermaid syntax. It does not prove that an architecture is correct, that controls operate, or that a selected product supports the design.

The [pilot release evidence](../examples/pilot-release-evidence.md) is deliberately filled, but remains an example. Its purpose is to make evidence expectations reviewable before implementation.

## Review Triggers

Reassess the design when source authority, reporting cadence, volume, sensitivity, user population, identity provider, retention, recovery target or decision forum changes. Each trigger can alter component boundaries, risks and acceptance evidence even if the report visuals remain unchanged.
