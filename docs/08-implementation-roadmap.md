# Delivery Roadmap

## Delivery Rule

The roadmap retires risk in evidence order. It does not begin with a dashboard build. Source meaning, KPI decisions, quality behaviour and access boundaries are resolved before presentation work can create an appearance of progress.

## Stage 1: Confirm Context

**Work**

- Name the Decision Owner, Service Owner, Information Owner, Source Owner and KPI Owner.
- Confirm management questions, review cadence and publication deadline.
- Profile source grain, keys, timestamps, reference values, volume and sensitivity.
- Agree current and forecast volume assumptions.

**Gate**

`BR-01` to `BR-03` and `NFR-01` to `NFR-08` have named owners, measurable acceptance and no unresolved contradiction. The source inventory contains no unapproved sensitive field.

## Stage 2: Prove Contracts And Controls

**Work**

- Implement immutable source receipt and provenance.
- Exercise clean, caveat and blocker quality paths.
- Approve KPI definitions and independent expected results.
- Build the exception structure and severity route.

**Gate**

A rejected run cannot update accepted reporting data. A caveat cannot pass without an owner, rationale, impact and expiry. Source, quality and expected result evidence reconcile for the synthetic cycle.

## Stage 3: Build Reporting Layers

**Work**

- Build declared fact and dimension grains in the Reporting Mart.
- Implement governed measures and date behaviour in the Semantic Model.
- Build the Management Report against the semantic contract.
- Preserve load, refresh and report version metadata.

**Gate**

Counts reconcile at every boundary. Approved KPI results match independent evidence. A schema or model contract violation fails before publication.

## Stage 4: Assure Security And Operation

**Work**

- Integrate managed identity and service area mappings.
- Run allowed, multi-area, unmapped and revoked identity tests.
- Exercise refresh recovery from retained evidence.
- Measure report performance at pilot and forecast volumes.
- Test applicable WCAG 2.2 AA behaviour and the equivalent tabular route.
- Inject failures at each material stage and verify alert timing and ownership.
- Review logging, alerts, retention and support ownership.

**Gate**

`NFR-01` and `NFR-03` to `NFR-08` have platform evidence. No high residual security or accessibility finding remains without explicit risk acceptance.

## Stage 5: Pilot The Review Cycle

**Work**

- Run the new service in parallel with the current pack for two cycles.
- Explain every material difference by definition, data correction or defect.
- Run the forum using the new decision and action record.
- Test handover with an operator who did not build the service.

**Gate**

The service publishes on time, material differences are resolved, decisions and actions are complete, recovery meets target and the independent operator completes the runbook without undocumented help.

## Cutover And Rollback

Cutover retires the old calculation route after the Decision Owner, Service Owner and KPI Owner accept the pilot evidence. The old pack can remain read only for comparison, but it cannot continue as a second source of truth.

Rollback during pilot restores the last accepted reporting version and invokes the approved continuity output. It does not overwrite failed evidence or silently return to uncontrolled calculations. A rollback records trigger, owner, affected period, restored version and corrective action.

## Production Decision

The [architecture assurance review](../examples/architecture-assurance-review.md) currently permits a controlled pilot only. A production decision still needs selected platform evidence, forecast capacity, cost, support model, recovery result, performance result, access result and organisational security approval.
