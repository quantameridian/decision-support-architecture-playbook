# Requirements And Traceability

## Requirement Set

| ID | Category | Commitment | Acceptance |
| --- | --- | --- | --- |
| `BR-01` | Business | Publish by 09:00 on the third working day | Timestamped publication record exists |
| `BR-02` | Business | Show workload, backlog, SLA and readiness from governed definitions | Output reconciles to approved semantic measures |
| `BR-03` | Business | Record each decision and action with owner and due date | No open action lacks owner or due date |
| `NFR-01` | Availability | Recover inside eight business hours | Timed recovery exercise passes |
| `NFR-02` | Freshness | Source is no more than 24 hours behind cut off | Receipt and source timestamps pass |
| `NFR-03` | Security | Restrict detail by service area and deny unmapped identities | Positive and negative role tests pass |
| `NFR-04` | Audit | Retain cycle evidence for 13 months | Sampled cycle can be reconstructed |
| `NFR-05` | Performance | Executive summary returns inside five seconds at pilot volume | 95th percentile test passes |
| `NFR-06` | Privacy | Exclude special category and direct contact fields | Field inventory and scan pass |
| `NFR-07` | Accessibility | Meet applicable WCAG 2.2 AA behaviour and provide a tabular route | Automated and manual review has no critical or serious issue |
| `NFR-08` | Observability | Notify the owner of material stage failure inside 15 minutes | Synthetic failure alerts pass at each material stage |

The [architecture catalogue](../catalogue/architecture.yaml) is authoritative for owners and full acceptance wording. The generated [validation evidence](validation-report.md) lists linked controls, evidence, decisions and risks for every requirement.

## Traceability Rules

- Every requirement has exactly one accountable owner and an observable acceptance statement.
- Every requirement is addressed by at least one control.
- Every control identifies one component and one evidence record.
- Every risk links to at least one control.
- Every decision links to requirements and risks, then resolves to a version controlled record.
- Component and interface identifiers used in diagrams must exist in the catalogue.

Automation checks reference completeness. A human review still decides whether the relationship is credible. Linking a weak control to a requirement does not make the requirement satisfied.

## Requirement Status

| Status | Meaning |
| --- | --- |
| Defined | Owner and acceptance are present in the catalogue |
| Designed | Component, interface and control treatment are documented |
| Pilot verified | Evidence from a representative pilot meets acceptance |
| Operationally proven | Repeated operation and recovery evidence meets the agreed period |

All eleven requirements are `Designed` in this repository. None is claimed as `Pilot verified` or `Operationally proven` because no platform is deployed.

## Architecture Review Basis

The view set follows the [C4 model](https://c4model.com/) distinction between system context and container responsibilities. Architecture decisions are kept with the service records following [GDS guidance](https://gds-way.digital.cabinet-office.gov.uk/standards/architecture-decisions.html); the lifecycle and consequence structure also draw on [AWS Prescriptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html).

Security review uses the [NCSC secure design principles](https://www.ncsc.gov.uk/collection/cyber-security-design-principles) to establish context, make compromise and disruption difficult, improve detection and reduce impact. Cross cutting review considers operations, security, reliability and performance concerns from the [Google Cloud Well Architected Framework](https://docs.cloud.google.com/architecture/framework). Accessibility uses the [W3C WCAG 2.2 standard](https://www.w3.org/WAI/standards-guidelines/wcag/). Privacy, open standards and sustainability questions draw on the [Technology Code of Practice](https://www.gov.uk/guidance/the-technology-code-of-practice). Monitoring, incident readiness and safe change questions use the [Azure operational excellence checklist](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/checklist). These references shape questions and evidence; they do not certify the design or select a supplier.
