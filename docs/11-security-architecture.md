# Security Architecture

## Security Context

The reporting model contains operational record detail classified as `Official` for this synthetic case. It excludes special category data and direct personal contact details. The main security objectives are to preserve report integrity, restrict detail by service area, retain decision evidence and recover without relying on personal files or credentials.

The [trust boundary view](../diagrams/trust-boundaries.mmd) separates source, controlled data, processing, reporting, consumption and governance zones. An arrow identifies a data or identity flow, not automatic trust.

## Protected Assets

| Asset | Security need |
| --- | --- |
| Source extract | Confidentiality, integrity, provenance and controlled retention |
| KPI definitions | Integrity, approval history and availability |
| Reporting mart | Integrity, least privilege and recoverability |
| Service area mapping | Confidentiality, integrity and prompt revocation |
| Management report | Availability, correct access and version identity |
| Readiness and approval evidence | Integrity, attribution and 13 month retention |
| Decision and action record | Integrity, attribution and controlled change history |

## Threat Analysis

| Threat | Boundary or asset | Effect | Primary treatment | Residual concern |
| --- | --- | --- | --- | --- |
| Forged or substituted extract | `INT-01`, Landing Store | False management result | Service identity, checksum and immutable receipt | Compromised source can still supply plausible bad data |
| Unapproved data correction | Quality Gate or mart | Lost lineage and biased result | Source correction route, atomic load and evidence | Emergency business correction needs a governed process |
| KPI logic changed without approval | Semantic Model | Trend and decision inconsistency | Versioned definition, release review and ADR | Reviewer may approve without understanding impact |
| User sees another service area | `INT-05`, report detail | Confidentiality breach | Identity filtering, deny unmapped users and negative tests | Export and downstream reuse need platform testing |
| Privileged service identity is abused | Processing and reporting zones | Broad data compromise | Separate managed identities and least privilege | Platform role design is not selected here |
| Quality or access failure is not detected | Evidence and monitoring | Unsafe publication continues | Observability Service, readiness gate, test evidence and alert ownership | Alert fatigue and incomplete logs require operational review |
| Evidence is changed or deleted | Evidence Store | Audit and recovery failure | Append only write, retention and quarterly sample | Legal hold and immutable storage product are not selected |
| Report service is unavailable | Consumption zone | Missed decision deadline | Recovery target and continuity output | No live resilience test exists |

## Access Model

Users authenticate through the Identity Provider. Managed group membership maps a user to one or more service areas. The Semantic Model applies the mapping to detailed records and returns no detail for an unmapped identity. [ADR-003](../decisions/ADR-003-semantic-model-access.md) records why visual filters and report copies were rejected.

Direct mart access is restricted to service identities and approved support roles. Report access does not imply mart access. Export, subscription, sharing and downstream analysis settings are part of the release review because they can bypass the expected user journey.

## Privileged Operation

- Service identities are non personal and scoped to one responsibility.
- Landing read, mart write, semantic refresh and evidence write use separate permissions.
- Production configuration changes require peer review and version history.
- Break glass access is time limited, logged and reviewed after use.
- Secrets are stored outside source and documentation.
- Access membership and unused privilege are reviewed quarterly.

## Detection And Response

Security relevant events include failed authentication, denied detail queries, role changes, unusual export, repeated readiness override attempts, source checksum mismatch and evidence deletion attempts. Alert ownership and response time are set during platform design.

A suspected integrity or confidentiality incident blocks normal publication until the Security Owner and Service Owner establish scope. Recovery uses known accepted evidence, followed by access and KPI verification before a new approval.

## Assurance Boundary

This threat analysis establishes context and candidate treatments. It is not a penetration test, privacy assessment or formal accreditation. Platform selection must add product specific attack paths, logging coverage, data location, supplier access, patching, vulnerability management and incident integration.
