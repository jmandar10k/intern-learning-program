# Task 1 (easy): gym membership churn

**Time box:** ≈ 1 day. **Skills shown:** Python, pandas, statistics, ML evaluation, avoiding
leakage.

## Context

A fictional chain of gyms, **PulseFit**, wants to know which members are likely to cancel next
month so the front-desk team can reach out (a free personal-training session, a plan change).
The data is an extract taken on **2025-01-01**: one row per member, with what was known on
that date, plus whether they cancelled during the following month.

Data: [data/members.csv](data/members.csv), documented in [data/README.md](data/README.md).
The data is deliberately messy.

## What to do

1. **Clean and validate** the data. Document every decision (what you changed, why, how many
   rows were affected).
2. **Explore** it. Produce at least **three findings** supported by numbers or plots, and at
   least one finding tested statistically (e.g. is churn different between payment methods?).
3. **Build a baseline model** that predicts `churned_next_month`, with a correct evaluation
   protocol:
   - only information available on the extraction date;
   - preprocessing fitted on training data only;
   - a dummy baseline and at least one real model;
   - cross-validation for model choice; a held-out test set used once;
   - metrics appropriate for the class balance.
4. **Recommend** how the front desk should use the model (e.g. how many members to contact per
   month, and what precision/recall that implies).

## Deliver

`task1/` as described in [submission-guidelines.md](../submission-guidelines.md), including
`outputs/metrics.json` with your final test metrics.

## Acceptance criteria

See [acceptance-criteria.md](acceptance-criteria.md).
