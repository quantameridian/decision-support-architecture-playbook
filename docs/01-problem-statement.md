# Problem Statement

## Architecture problem

Decision-support reporting often fails because the reporting artefact is treated as the system. A dashboard, spreadsheet, or management pack may exist, but the architecture around it is incomplete.

The missing architecture usually sits between operational data and management action:

- source systems are not clearly mapped to report outputs;
- KPI definitions are not agreed or version controlled;
- report ownership is based on habit rather than explicit roles;
- data-quality checks are informal or performed too late;
- manual adjustments are not recorded in a controlled way;
- dashboard users do not know which numbers are reliable enough for decisions;
- review meetings do not consistently convert findings into owned actions;
- handover depends on individual memory rather than documented process.

The result is a reporting environment that can produce numbers but cannot always explain, defend, or improve them.

## Why this matters

Poor reporting architecture creates operational risk. It can lead to:

- duplicated reporting effort;
- inconsistent KPI results across teams;
- slow reporting cycles;
- weak confidence in dashboards;
- unresolved data-quality issues;
- decisions based on unclear assumptions;
- loss of knowledge when report owners change roles.

The problem is not only technical. It is also architectural and operational: data routes, definitions, controls, ownership, review cadence, and handover all need to work together.

## Intended decision-support outcome

A controlled decision-support system should make it clear:

- which source data feeds each output;
- what each KPI means and how it is calculated;
- who owns the data, KPI definition, report, and action follow-up;
- which data-quality checks run before reporting;
- what limitations apply to the output;
- how decisions and actions are captured after review;
- how another person could maintain the system.

This playbook frames those components so they can be discussed, designed, and handed over.

## Demonstrated capability

This repository is intended to demonstrate that the author can:

- frame a reporting architecture problem clearly;
- separate symptoms from root design issues;
- design source-to-output structures;
- define where controls should sit;
- connect KPI definitions to ownership and review routines;
- describe an operating model around reporting;
- produce documentation that supports stakeholder review and handover.

## Boundaries of this problem statement

This document does not claim to describe a real organisation or client. It does not use protected or internal workplace material. It provides a generic but commercially realistic architecture scenario that can be adapted later with safe sample structures.

The problem statement also does not solve the technical implementation by itself. The remaining playbook sections define the current state, target state, source-to-output map, control model, KPI dictionary, operating model, implementation roadmap, and handover pack.
