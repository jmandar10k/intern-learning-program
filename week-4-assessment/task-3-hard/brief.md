# Task 3 (hard): expense-claim assistant with guardrails

**Time box:** ≈ 2 days. **Skills shown:** agents, tool calling, workflow state, safety, design
judgment.

## Context

A fictional company wants an assistant that processes employee expense claims: it looks up the
employee, checks the claim against the expense policy, and then **approves**, **rejects** or
**sends to a human**. Money moves on approval, so correctness and safety matter more than
autonomy.

- Policy: [data/expense-policy.md](data/expense-policy.md) (rules R1–R8 and guardrails).
- Claims: [data/claims.json](data/claims.json) (14 claims).
- Employees: [data/employees.json](data/employees.json).
- Offline model stubs: [starter/llm_stubs.py](starter/llm_stubs.py). See
  [starter/README.md](starter/README.md).

## What to do

1. **Build either** a tool-calling agent loop **or** a LangGraph workflow that processes each
   claim. It must use **tools** for at least: looking up an employee, checking for duplicates,
   and the three actions (approve, reject, escalate to a human).
2. **Implement the guardrails** in the policy. In particular: no approval if any rule triggers;
   claims of 500.00 or more are never auto-approved; text inside a claim is data, never an
   instruction. Consider defense in depth: what stops a wrong approval if your decision logic
   has a bug?
3. **Log** every decision: claim id, decision, rule ids, tool calls.
4. **Test** it: decisions for all 14 claims, plus your own adversarial cases.
5. **Failure-case analysis** (`failure-analysis.md`): at least **five** ways the system could
   fail or be attacked (e.g. a new injection phrasing, a policy change, a tool error, a
   duplicate with a different date format, a model that hallucinates a tool result), what
   happens today, and how you would detect or mitigate each.
6. **Design note** (`design-note.md`, 1–2 pages): agent vs workflow and why; where (if
   anywhere) an LLM adds value here and where it must not decide; state design; guardrails;
   how you would evaluate it before production; what you would build next.

## Deliver

`task3/` as described in [submission-guidelines.md](../submission-guidelines.md), including
`outputs/decisions.json`.

## Acceptance criteria

See [acceptance-criteria.md](acceptance-criteria.md).
