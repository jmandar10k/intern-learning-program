# Week 3: silent-bug code review

Each exercise in [exercises/](exercises/) is a small, realistic program that **runs end to end
with no error, no exception and no warning that points at the problem, yet produces wrong
output.** Your job is what a good reviewer does on a real team: notice that the results cannot
be right, find out why, explain it with theory from Weeks 1–2, fix it, and make sure it cannot
silently come back.

## The exercises

| Exercise | Area | Domain |
|---|---|---|
| [ex01-data-leakage](exercises/ex01-data-leakage/) | ML evaluation | Subscription churn |
| [ex02-metric-misuse](exercises/ex02-metric-misuse/) | Statistics, evaluation | Support-ticket escalation |
| [ex03-preprocessing-bug](exercises/ex03-preprocessing-bug/) | Data analysis | Online-store sales report |
| [ex04-rag-retrieval-flaw](exercises/ex04-rag-retrieval-flaw/) | RAG | Note-taking app help center |
| [ex05-prompt-chain-flaw](exercises/ex05-prompt-chain-flaw/) | LLMs, NLP | Product review replies |
| [ex06-agent-tool-misuse](exercises/ex06-agent-tool-misuse/) | Agents, tool calling | Office-supplies restocking |
| [ex07-langgraph-state-bug](exercises/ex07-langgraph-state-bug/) | LangGraph | Document publishing workflow |

Each folder contains:

- `main.py`: the program under review.
- `data/`: small synthetic data (and, for some, a data dictionary).
- `requirements.txt`: what it needs (all offline; LLMs and embeddings are deterministic stubs).
- `expected-behavior.md`: what correct output looks like. **This is your only hint.**

## How to work

1. Read `expected-behavior.md`, then run `python main.py` from inside the exercise folder.
2. Compare the output with the expected behavior. Write down every symptom.
3. Form a hypothesis, then **prove it** with a small experiment (print, assert, minimal change).
4. Fix the code. Re-run and compare with `expected-behavior.md` again.
5. Add a test or sanity check that would have caught the bug.
6. Write it up with [review-submission-template.md](review-submission-template.md).

Use [review-checklist.md](review-checklist.md) to make sure you looked everywhere.

## Rules

- **Some exercises contain more than one bug**: typically one obvious and one subtle. Fixing
  the first symptom you see is not necessarily the end. Keep going until the output matches
  `expected-behavior.md` for the right reason.
- Do not rewrite the program from scratch. Make the smallest correct fix, as you would in a
  real review.
- Do not change the data files or `expected-behavior.md`.
- Commit your fixed code in a branch or a copy (`exNN-.../fixed/`), and your write-up as
  `exNN-.../review.md`.
- **GenAI is allowed, but must be disclosed** in each submission (see the
  [GenAI usage policy](../00-charter/genai-usage-policy.md)). You must reproduce and explain
  every finding yourself; an unverified AI explanation scores zero for that bug.

## How it is scored

For each bug: **found** it, **explained** why it is wrong (with the Week 1–2 concept), **fixed**
it correctly, and **added a test or sanity check** that prevents it from recurring. Depth
(finding the subtle bugs) and clear reasoning count more than speed. Scores feed the
"Technical quality" and "Learning" dimensions of the
[evaluation rubric](../00-charter/evaluation-rubric.md).
