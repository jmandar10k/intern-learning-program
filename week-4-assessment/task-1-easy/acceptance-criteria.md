# Task 1 acceptance criteria

A task **meets** acceptance when every **must** item is satisfied. **Should** items raise the
score. Scored with [assessment/task-scoring-sheet.md](../../assessment/task-scoring-sheet.md).

## Must

| # | Criterion | How it is checked |
|---|---|---|
| M1 | The pipeline runs end to end from a clean checkout with one documented command. | Mentor runs it |
| M2 | Exact duplicate rows are removed (there are 40), and inconsistent `plan` labels are normalized to 3 values. | Cleaning log / code |
| M3 | Impossible values (e.g. `age` = 999) and missing values are handled with a documented, justified strategy. | README |
| M4 | No feature uses information recorded after the extraction date or after the outcome. | Code review |
| M5 | All fitted preprocessing (imputation, scaling, encoding) is fitted on training data only (e.g. inside a `Pipeline`). | Code review |
| M6 | A dummy baseline is reported next to at least one real model. | Output |
| M7 | Model selection uses cross-validation on the training set; the test set is used once at the end. | Code review |
| M8 | Reported test metrics include ROC-AUC **and** a metric suited to the minority class (PR-AUC, or precision/recall/F1 for churners). | `outputs/metrics.json` |
| M9 | The honest test ROC-AUC is plausible for this data, **between 0.70 and 0.90**. A value above 0.95 indicates leakage. | `outputs/metrics.json` |
| M10 | At least three EDA findings, one with a statistical test (test named, effect size, p-value or CI). | README |

## Should

| # | Criterion |
|---|---|
| S1 | Features engineered from domain reasoning (e.g. change in visit frequency, tenure), with a short justification. |
| S2 | A threshold or "top-N to contact" recommendation tied to precision/recall. |
| S3 | Tests or asserts for the cleaning steps (e.g. no duplicates, valid plan values, row counts). |
| S4 | A short limitations section (sample size, synthetic data, what you would do with more time). |
| S5 | Clear plots with titles that state the finding. |
