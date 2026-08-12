# Reviewer Guide

## Ten Minute Path

1. Read the [executive brief](00-executive-brief.md) for the decision and conditions.
2. Inspect the [architecture catalogue](../catalogue/architecture.yaml) for the structured model.
3. Open the [container](../diagrams/container-view.mmd) and [trust boundary](../diagrams/trust-boundaries.mmd) views.
4. Read the three records in the [decision log](../decisions/README.md).
5. Inspect the filled [pilot release evidence](../examples/pilot-release-evidence.md).
6. Read the [assurance review](../examples/architecture-assurance-review.md), especially the material gaps.
7. Check the generated [traceability evidence](validation-report.md).

## Challenge The Design

A serious review should ask:

- Can every requirement be accepted with observable evidence?
- Do component responsibilities overlap or leave an unowned failure?
- Does every interface cross a justified boundary with an explicit protection?
- Can a successful technical run still publish unsuitable business data?
- What happens to an authenticated identity with no service area mapping?
- Can one reporting cycle be reconstructed after the original analyst leaves?
- Are recovery and performance claims proven, or only stated?
- Which decision would need to change if latency, volume or sensitivity changes?

## What The Evidence Supports

The repository supports review of problem framing, logical service design, requirement traceability, interface definition, data quality control, KPI governance, trust analysis, operating ownership, risk treatment, decision history and release evidence design.

It does not support claims about a deployed platform, live users, organisation approval, production resilience, cost, penetration testing or regulatory compliance. The synthetic status is part of the design boundary, not a footnote.

## Reproduce The Checks

```bash
make install
make qa
```

The expected result is a parsed catalogue with complete references, nine covered requirements, all Mermaid files accepted by Mermaid, valid local links, passing regression tests and no generated evidence diff.
