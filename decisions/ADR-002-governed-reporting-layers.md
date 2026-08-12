# ADR-002: Separate Governed Reporting Layers From Source Extracts

| Field | Value |
| --- | --- |
| Status | Accepted for scenario |
| Date | 2026-08-12 |
| Owner | Analytics Engineering Owner |
| Decision roles | Source Owner, Platform Owner, BI Owner, Service Owner |
| Requirements | `BR-02`, `NFR-01`, `NFR-02` |
| Risks | `RSK-01`, `RSK-05`, `RSK-06` |

## Context

The current process mixes source receipt, correction, KPI logic and presentation in one workbook. That makes a rerun difficult, weakens lineage and leaves report behaviour dependent on local files.

The target service needs a route that preserves what arrived, separates rejected records from accepted reporting data and gives the semantic model a stable contract.

## Options

| Option | Benefit | Cost and risk |
| --- | --- | --- |
| Continue with a controlled workbook | Low initial cost and familiar operation | Limited automated control, concurrency and recovery evidence |
| Query the source system directly from the report | Fewer stored copies | Couples management reporting to source availability and exposes source schema changes at consumption time |
| Use landing, quality, mart and semantic layers | Clear ownership, replay and test points | More components to operate and reconcile |

## Decision

Use four governed layers between source and report:

1. The Controlled Landing Store retains the received extract and provenance.
2. The Quality Gate validates the extract and issues readiness evidence.
3. The Reporting Mart publishes accepted facts and dimensions at declared grains.
4. The Semantic Model owns measures, date behaviour and report access rules.

Interfaces use replaceable formats and explicit contracts. Source corrections happen in the source system where possible. A controlled transformation can correct representation, but it must not silently invent a business fact.

## Consequences

The service gains repeatability, clearer failure isolation and a practical recovery route. A historical extract can be replayed without asking the source owner to recreate it.

The design has more operational surface than a workbook. Monitoring must distinguish receipt failure, quality rejection, mart load failure, model refresh failure and report availability. Reconciliation checks are required at each material boundary.

## Verification

- Every interface in `catalogue/architecture.yaml` identifies direction, mode, format, cadence and protection.
- A rejected quality run cannot update the published mart.
- A prior accepted extract can be replayed into a clean reporting environment.
- Fact and dimension row counts reconcile through the mart and semantic model.

## Review Triggers

Review this decision when source access changes, data volume exceeds the pilot baseline, latency moves below daily batch, or the organisation adopts a governed shared data product that can replace one of the layers.
