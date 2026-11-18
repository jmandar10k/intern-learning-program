# ex01: expected behavior

**Goal of the script:** rank customers by their risk of cancelling **next month**, so the
retention team can contact them before they decide to leave.

## What correct output looks like

- The model only uses information available **before** a customer starts to cancel (see
  [data/README.md](data/README.md)).
- On this data, an honest logistic-regression baseline reaches a **test ROC-AUC of roughly
  0.68–0.80**, and a 5-fold cross-validated ROC-AUC in the same range.
- Test accuracy is only a few points above the **majority-class baseline of ≈ 0.78** (churn
  rate ≈ 0.22).
- The strongest drivers are contract type (monthly vs two-year), tenure and payment failures.
- The highest predicted risks are well below 1.0 (around 0.7–0.85). Customers who have not yet
  decided to leave cannot be predicted with near certainty.

## Sanity checks you can run

- Is any score "too good to be true" for a churn problem?
- For every feature: could the retention team know this value at the moment they would act?
- Does anything computed from the test rows influence training?
