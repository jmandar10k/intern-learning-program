# ex02: expected behavior

**Goal of the script:** decide whether the escalation predictor is good enough to deploy.
The business priority is to **catch escalations** (≈ 5% of tickets) early.

## What correct output looks like

- The evaluation reports, at minimum: precision, recall and F1 **for the escalated class**,
  macro-F1, PR-AUC and a confusion matrix, **next to a baseline that never flags a ticket**.
- That baseline has accuracy ≈ 0.95 and recall 0.0 on escalations.
- A useful model on this data reaches **recall on escalations ≥ 0.60** with precision ≥ 0.15
  on the test set, and a PR-AUC around 0.4–0.5 (≈ 8× the base rate).
- The release gate is expressed in metrics that describe escalations, and the printed numbers
  justify its PASS/FAIL.

## Sanity checks you can run

- How many escalations are in the test set, and how many did the model catch?
- Would a model that predicts "not escalated" for every ticket pass the current gate?
- Does each printed metric measure what its label says?
