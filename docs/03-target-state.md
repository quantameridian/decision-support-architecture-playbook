# Target State

## System Context

The Operations Review Service receives owned operational records and approved KPI definitions. It gives service managers a governed output and sends review decisions into a controlled action register. Authentication and service area claims come from the organisation identity provider.

See the [system context diagram](../diagrams/system-context.mmd) for the actor and system boundary.

## Component View

The [container view](../diagrams/container-view.mmd) shows the ten logical components. They are responsibilities, not product selections.

| Component | Architectural responsibility | Failure isolated |
| --- | --- | --- |
| `CMP-01` Operational Work System | Own business records and daily extract | Source availability or field meaning |
| `CMP-02` Controlled Landing Store | Preserve receipt, checksum and timestamps | Transfer and provenance |
| `CMP-03` Quality Gate | Validate data and issue readiness | Business quality and release status |
| `CMP-04` Reporting Mart | Publish tested facts and dimensions | Transformation and data contract |
| `CMP-05` Semantic Model | Govern measures, date rules and service area access | KPI semantics and model policy |
| `CMP-06` Management Report | Present performance and visible caveats | User experience and report availability |
| `CMP-07` Decision and Action Register | Record decisions, actions and due dates | Review follow through |
| `CMP-08` Evidence Store | Retain cycle and recovery evidence | Audit and service continuity |
| `CMP-09` Identity Provider | Authenticate users and supply group claims | Identity and access lifecycle |
| `CMP-10` Observability Service | Receive health events and route material failures | Detection and accountable response |

## Service Behaviour

The [reporting cycle sequence](../diagrams/reporting-cycle-sequence.mmd) separates three outcomes:

- `Ready` permits publication.
- `Ready with caveat` permits publication only with a named owner, rationale, affected output and expiry.
- `Not ready` prevents publication until the blocker is corrected or the decision owner follows an approved contingency.

The gate decision is defined in [ADR-001](../decisions/ADR-001-reporting-readiness-gate.md). It prevents a green pipeline run from concealing unsuitable business data.

## Design Qualities

| Quality | Design response |
| --- | --- |
| Replaceability | Interfaces declare mode and format; product names are not embedded in the logical design |
| Reliability | Immutable receipts, atomic mart publication and retained evidence support replay and recovery |
| Security | Trust zones, managed identities, least privilege and semantic access filtering limit exposure |
| Auditability | Source, quality, approval, publication and decision records share a reporting cycle identity |
| Operability | Failure stages, owners, escalation and recovery evidence are explicit |
| Performance | A measurable render target is set, but remains a pilot acceptance item |
| Accessibility | Applicable WCAG 2.2 AA checks and an equivalent tabular route are release requirements |
| Observability | Receipt, quality, load, model and report stages emit restricted health events |

## Deliberate Limits

This design does not select a cloud, database, orchestration service or reporting product. It also does not define physical network routes, capacity sizing or cost. Those choices require organisational constraints, forecast volumes, existing platform standards and security review.

The [assurance review](../examples/architecture-assurance-review.md) therefore recommends a controlled pilot, not production approval.
