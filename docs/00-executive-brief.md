# Executive Brief

## Decision

Approve a controlled pilot of the synthetic Operations Review Service, subject to named owners confirming the source contract and acceptance plan. Do not approve production operation until recovery, performance and platform access evidence exists.

## Business Need

Service managers currently depend on manual extracts, workbook logic and informal corrections. A monthly pack is produced, but the route from source record to management action is difficult to reconstruct. KPI disputes and quality corrections consume review time that should be used to decide priorities.

The proposed service answers three questions:

1. What work is open or overdue and needs intervention?
2. Is service performance meeting the agreed target?
3. Is the underlying evidence reliable enough for a formal decision?

## Proposed Change

The design separates the reporting route into controlled source receipt, a quality gate, a tested reporting mart, a governed semantic model and an access filtered management report. A decision and action register closes the loop. An evidence store retains the source receipt, quality result, approval, publication and review outcome for 13 months.

The architecture catalogue defines eleven requirements, ten components, fourteen interfaces, thirteen controls, thirteen evidence records, ten risks and three accepted scenario decisions.

## Key Commitments

| Commitment | Target |
| --- | --- |
| Monthly publication | 09:00 on the third working day |
| Source freshness | No more than 24 hours behind the agreed cut off |
| Recovery time | Eight business hours |
| Recovery point | 24 hours |
| Detail access | Service area scope, deny when no mapping exists |
| Evidence retention | 13 months |
| Executive page performance | Five seconds or less at the 95th percentile for pilot volume |
| Accessibility | Applicable WCAG 2.2 AA checks with an equivalent tabular route |
| Failure notification | Accountable owner notified inside 15 minutes |

## Main Risks

The largest residual risks are quality failures hidden by publication, an untested scale assumption and inaccessible report behaviour. The readiness gate controls the first by separating technical success from release approval. Scale and accessibility remain open until representative platform evidence exists.

## Pilot Exit

Production consideration requires:

- one complete reporting cycle reconstructed from retained evidence;
- blocker, caveat and clean readiness paths exercised;
- positive and negative service area access tests passed;
- recovery completed inside eight business hours;
- report performance measured at the agreed pilot and forecast volumes;
- accessibility checks completed with no critical or serious issue;
- material failure alerts reaching accountable owners inside 15 minutes;
- named service, information, source, KPI, security and report owners accepting their duties.
