# Risks and Limitations

## Purpose

This document records the main risks and limitations for the decision-support architecture playbook. It is deliberately honest about what a generic portfolio playbook can and cannot prove.

## Architecture risks

| Risk | Meaning | Mitigation in this playbook |
| --- | --- | --- |
| Unclear ownership | Data, KPI, report, and action ownership are not assigned clearly. | Later operating-model section should define ownership roles and review responsibilities. |
| Weak KPI definitions | Measures are used in management forums without agreed calculation logic. | KPI dictionary templates should require definition, formula, owner, caveat, and review cadence. |
| Late data-quality checks | Quality issues are found after outputs are already circulated. | Data-quality control section should place checks before management output creation. |
| Manual adjustment risk | Manual corrections are made without evidence, versioning, or approval. | Source-to-output mapping should identify manual steps and control points. |
| Dashboard-only thinking | Visuals are built without source lineage, ownership, or handover. | The playbook treats reports as part of a wider decision-support system. |
| Review without action | Management meetings discuss metrics but do not capture decisions or owners. | Reporting lifecycle should include action logging and follow-up ownership. |
| Handover failure | Reporting processes depend on individual knowledge. | Handover pack should document sources, definitions, refresh, checks, owners, and known limitations. |

## Portfolio limitations

- This is a public portfolio project, not a client delivery record.
- It does not claim that Quanta Meridian or the author has delivered this exact playbook for a client.
- It uses generic architecture patterns and must not include protected, official, internal, or copied workplace material.
- It does not include real operational data.
- It does not prove production implementation capability by itself.
- It is documentation-led and should be assessed as architecture thinking, not as a deployed platform.

## Method limitations

- A real organisation would need discovery, stakeholder interviews, source-system review, data profiling, security assessment, and governance alignment.
- The playbook cannot define final KPI ownership without a real operating context.
- The target architecture may need to change depending on existing tools, data platform maturity, reporting cadence, and risk appetite.
- Templates can support consistency, but they cannot replace review by accountable business and technical owners.

## Boundary risks

This repo should not drift into the scope of the other portfolio repositories:

- Python exception generation belongs in `operational-data-quality-engine`.
- SQL/dbt transformation modelling belongs in `analytics-engineering-service-mart`.
- Power BI semantic modelling and DAX belong in `powerbi-kpi-semantic-model`.

This playbook owns the architecture, controls, operating model, roadmap, and handover thinking around those technical layers.

## Publication limitations

Before publication, check that:

- all claims are framed as portfolio examples, not client outcomes;
- diagrams are generic and do not imply a protected system;
- templates are complete enough to be useful;
- no placeholder outline sections remain;
- no wording implies official endorsement or access to protected material;
- limitations remain visible in the README and this document.
