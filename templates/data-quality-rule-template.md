# Data Quality Rule Template

Use this template to define a data-quality rule before it is added to a validation script, reporting model, or manual assurance checklist.

## 1. Rule Identity

| Field | Detail |
| --- | --- |
| Rule ID |  |
| Rule name |  |
| Rule owner |  |
| Source owner |  |
| Date created |  |
| Review frequency | Each refresh / weekly / monthly / quarterly |
| Rule status | Draft / active / retired |

## 2. Business Purpose

| Question | Detail |
| --- | --- |
| What reporting risk does this rule control? |  |
| Which KPI or output is affected? |  |
| What decision could be weakened if this rule fails? |  |
| Is this rule a blocker or a caveat? | Blocker / caveat / warning |

## 3. Source and Fields

| Field | Detail |
| --- | --- |
| Source table/file |  |
| Source grain |  |
| Key field |  |
| Field(s) checked |  |
| Reference list or lookup |  |

## 4. Rule Logic

```text
Rule logic:

```

Examples:

- Required field is not blank for active records.
- Status value must be one of the agreed reference values.
- Closed records must have closure evidence.
- High-risk overdue records must have an action owner.

## 5. Severity and Routing

| Severity level | Use when | Action |
| --- | --- | --- |
| High | Issue affects headline reporting or high-risk follow-up | Escalate before formal publication |
| Medium | Issue affects a subset of records or requires caveat | Publish with caveat if accepted |
| Low | Issue should be corrected but does not affect interpretation materially | Log and correct in normal cycle |

| Routing item | Detail |
| --- | --- |
| Exception owner |  |
| Escalation route |  |
| Expected resolution time |  |
| Closure evidence required |  |

## 6. Exception Output

| Exception field | Value or rule |
| --- | --- |
| Rule ID |  |
| Record ID |  |
| Field |  |
| Issue description |  |
| Recommended action |  |
| Severity |  |
| Owner |  |
| Due date |  |

## 7. Testing and Review

| Check | Status |
| --- | --- |
| Rule tested on sample data | Not started / passed / failed |
| False positives reviewed | Not started / passed / failed |
| Business owner reviewed wording | Not started / passed / failed |
| Rule added to control catalogue | Not started / complete |
| Next review date set | Yes / No |

## 8. Change Log

| Date | Change | Owner | Reason |
| --- | --- | --- | --- |
|  |  |  |  |
