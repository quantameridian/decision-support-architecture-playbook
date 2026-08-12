# ADR-003: Enforce Service Area Access In The Semantic Model

| Field | Value |
| --- | --- |
| Status | Accepted for scenario |
| Date | 2026-08-12 |
| Owner | Security Owner |
| Decision roles | Information Owner, Identity Owner, BI Owner |
| Requirements | `NFR-03`, `NFR-06` |
| Risks | `RSK-03` |

## Context

Managers need an organisation wide summary while detailed work records must remain limited to authorised service areas. Separate report copies would duplicate logic and make revocation difficult to prove. Visual filters alone are not a security control.

## Options

| Option | Benefit | Cost and risk |
| --- | --- | --- |
| Publish separate report copies | Simple user experience | Duplicates content, increases drift and complicates revocation |
| Filter report pages by service area | Easy to configure | A presentation filter does not enforce data access |
| Apply identity based filtering in the semantic model | One governed model and central policy | Requires reliable identity mappings and explicit negative tests |

## Decision

The Semantic Model will filter detail through an approved identity to service area mapping. Unmapped identities receive no detailed rows. Access is granted through managed groups where the platform supports them, reviewed quarterly and removed through the identity lifecycle.

The reporting mart remains a restricted service layer. Semantic filtering does not make the underlying data safe for broad direct access. Special category data and direct personal contact details are excluded before data reaches the model.

## Consequences

One model can serve several service areas while keeping the rule close to the governed measures. The design avoids proliferating report copies, but it depends on accurate group membership and correct filter propagation.

Summary access and detail access must be tested separately. Export, subscription and downstream reuse settings require the same review as interactive viewing.

## Verification

- An authorised service manager can see only their mapped service area detail.
- A manager mapped to two areas sees the union and no other detail.
- An authenticated but unmapped identity sees no detail.
- Removing a group grant removes access within the agreed identity propagation time.
- Exported detail applies the same effective filter as the report view.

## Review Triggers

Review this decision when the identity provider changes, external users are introduced, report sharing changes, a new sensitivity class enters the model, or the platform cannot enforce the expected export behaviour.
