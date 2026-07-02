# Executive Brief

## What this playbook is

This repository is a reusable architecture playbook for moving manual reporting
toward controlled decision support. It focuses on the operating model around
reporting: ownership, definitions, controls, review rhythm, escalation, and
handover.

## Reporting problem

Manual reporting can still produce regular dashboards and packs while remaining
fragile underneath. The usual failure is not only technical. It is unclear
ownership, undocumented KPI logic, weak data quality gates, informal exceptions,
and review meetings that do not feed decisions back into the source process.

## What a reviewer should inspect

1. [Source to output map](04-source-to-output-map.md) for lineage and control placement.
2. [Data quality controls](05-data-quality-controls.md) for quality gate design.
3. [KPI dictionary](06-kpi-dictionary.md) for definition ownership.
4. [Operating model](07-operating-model.md) for roles, cadence, escalation, and handover.
5. [Synthetic applied walkthrough](../examples/manual-reporting-transformation-example.md).

## Portfolio signal

This playbook shows how I would structure the architecture around a reporting problem before choosing a tool. It is meant to demonstrate problem framing, control design, stakeholder ready documentation, and the link between data work and decisions.

## What this demonstrates

- Architecture thinking beyond dashboard visuals.
- Ability to translate messy reporting symptoms into a target operating model.
- Practical controls around source data, KPI definitions, quality exceptions,
  review forums, and action ownership.
- Documentation that can be reused in discovery and review meetings.

## What this does not prove

- It does not prove delivery for a real organisation.
- It does not include production data or platform configuration.
- It does not replace a working dbt model, Power BI report, or Python data quality engine.
- It works best as an architecture companion to the technical repos.

## Review standard

The playbook is ready for review when a reader can answer:

- What decision does the reporting support?
- Which source fields feed each output?
- Who owns source quality and KPI definitions?
- What checks run before publication?
- How are exceptions assigned, escalated, and closed?
- What must be handed over so the process survives role changes?
