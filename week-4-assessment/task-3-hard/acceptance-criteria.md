# Task 3 acceptance criteria

## Must

| # | Criterion | How it is checked |
|---|---|---|
| M1 | Runs offline end to end with one documented command and processes all 14 claims. | Mentor runs it |
| M2 | Implemented as a tool-calling agent loop or a LangGraph workflow, using tools for employee lookup, duplicate check and the three actions. | Code review |
| M3 | Every decision follows the policy, including rule order: **all 14 decisions and rule ids are correct.** | `outputs/decisions.json` vs mentor's expected decisions |
| M4 | Guardrails hold: nothing that triggers a rule is approved; no claim ≥ 500.00 is approved; instructions in claim text do not change behavior (the claim is flagged per R5). | Decisions + mentor's adversarial cases |
| M5 | Every decision is logged with claim id, decision, rule ids and tool calls. | `outputs/decisions.json` |
| M6 | Tests cover the 14 claims and at least **three** adversarial cases of your own. | `tests/` |
| M7 | `failure-analysis.md` covers at least **five** distinct failure or attack modes, each with current behavior and a detection/mitigation. | Document |
| M8 | `design-note.md` (1–2 pages) justifies agent vs workflow, the role of the LLM, state design, guardrails and evaluation. | Document |

> **Partial credit:** if M3/M4 are not fully met, Task 3 can still count toward a "go" when the
> design note and failure analysis are sound and the gaps are identified honestly (see
> [go-no-go-criteria.md](../../00-charter/go-no-go-criteria.md)).

## Should

| # | Criterion |
|---|---|
| S1 | Defense in depth: the approve tool (or a final check) independently refuses unsafe approvals. |
| S2 | Tool errors (e.g. unknown employee, lookup failure) are handled explicitly and never lead to approval. |
| S3 | Typed state; LangGraph reducers used deliberately (if LangGraph). |
| S4 | The LLM, if used, never makes the approve/reject decision; its output is validated. |
| S5 | Clear explanation strings for each decision that a human reviewer could act on. |
