# Week 4 task scoring sheet

Score each task against its `acceptance-criteria.md`. Use the 1–4 scale from the
[evaluation rubric](../00-charter/evaluation-rubric.md).

| Score | Meaning for a task |
|---|---|
| 4 | All **Must** items met, most **Should** items met, work shows insight beyond the brief |
| 3 | All **Must** items met (minor gaps in Should) |
| 2 | Most Must items met; one or two significant gaps, honestly identified |
| 1 | Several Must items missing, or the task does not run |

| Field | Value |
|---|---|
| Intern | |
| Scorer | |
| Second reviewer | |
| Date | |
| Commit scored | |

## Task 1 (easy): gym churn

| Item | Met? (Y/N/partial) | Evidence / note |
|---|---|---|
| M1 runs end to end | | |
| M2 duplicates, plan labels | | |
| M3 impossible/missing values | | |
| M4 no post-outcome features | | |
| M5 preprocessing fit on train only | | |
| M6 dummy baseline | | |
| M7 CV for selection, test once | | |
| M8 minority-class metric | | |
| M9 plausible ROC-AUC (0.70–0.90) | | |
| M10 3 findings + 1 statistical test | | |
| Should items met (S1–S5) | | |

**Task 1 score (1–4):** ___

## Task 2 (medium): RAG

| Item | Met? | Evidence / note |
|---|---|---|
| M1 runs, answers 20 questions | | |
| M2 chunking documented, full coverage | | |
| M3 retrieval evaluated separately | | |
| M4 ≥ 2 configurations compared | | |
| M5 recall@3 ≥ 0.90, MRR ≥ 0.75 | | |
| M6 ≥ 13/17 correct answers with citation | | |
| M7 abstains on 3/3 unanswerable | | |
| M8 failure analysis per miss | | |
| Should items met (S1–S5) | | |

**Task 2 score (1–4):** ___

## Task 3 (hard): expense claims

| Item | Met? | Evidence / note |
|---|---|---|
| M1 runs, 14 claims | | |
| M2 agent loop or LangGraph, with tools | | |
| M3 all 14 decisions + rule ids correct (__ / 14) | | |
| M4 guardrails hold (incl. mentor's adversarial cases) | | |
| M5 decisions logged | | |
| M6 tests incl. ≥ 3 adversarial cases | | |
| M7 failure analysis ≥ 5 modes | | |
| M8 design note | | |
| Should items met (S1–S5) | | |

**Task 3 score (1–4):** ___

## Summary

| Task | Score | Meets acceptance (all Must)? |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

Tasks meeting acceptance: ___ / 3 (go rule: at least 2; Task 3 may be partial if design note
and failure analysis are sound; see [go-no-go-criteria.md](../00-charter/go-no-go-criteria.md)).

GenAI disclosures present and specific in all three tasks? Y / N. Notes:
