# Week 4 plan: practical assessment

Three tasks of increasing difficulty, a demo with Q&A, then the formal go/no-go review.
Everything you need is in this folder. All data is synthetic and offline; no API keys.

**Objectives:** see the Week 4 section of
[00-charter/learning-objectives.md](../00-charter/learning-objectives.md).
**How the decision is made:** [00-charter/go-no-go-criteria.md](../00-charter/go-no-go-criteria.md).

## Schedule

| Day | Task | Time box |
|---|---|---|
| 16 | [Task 1 (easy)](task-1-easy/brief.md): churn-style tabular data: preprocessing, analysis, baseline model with proper evaluation | ≈ 1 day |
| 17 | [Task 2 (medium)](task-2-medium/brief.md): RAG pipeline over a document set, with retrieval evaluation | ≈ 1.5 days |
| 18 | Task 2 (finish, morning) → [Task 3 (hard)](task-3-hard/brief.md) (start) | |
| 19 | Task 3: tool-calling agent or LangGraph workflow with guardrails, failure-case analysis, design note | ≈ 2 days total |
| 20 | Morning: **demo with Q&A** (45–60 min). Afternoon: **four-week go/no-go review** | |

Time boxes are guidance. If you run over on one task, stop at a working, documented state and
move on. A working, honest, partial Task 3 beats a polished Task 2 and no Task 3.

## Rules

- Work individually. You may ask the mentor clarifying questions about the briefs (log them in
  [progress-log/week-4-log.md](../progress-log/week-4-log.md)); you may not ask for solutions.
- Commit early and often. Your commit history is part of the evidence.
- Each task must run from a clean checkout with the commands in your README.
- Do not modify the provided data files or acceptance criteria.

## Allowed resources

- Everything in this repository (notes, exercises, your Week 3 reviews).
- Official documentation (Python, pandas, scikit-learn, LangChain, LangGraph…), books, papers.
- Web search.
- **GenAI tools, with disclosure** in each task's README (see the
  [GenAI usage policy](../00-charter/genai-usage-policy.md)). You must be able to explain every
  line in the demo. Asking a GenAI tool for a full solution and lightly editing it is not
  acceptable and is easy to spot in Q&A.

## Deliverables

Follow [submission-guidelines.md](submission-guidelines.md): repo layout, README per task,
and the demo format.

## How you are scored

Each task is scored against its `acceptance-criteria.md` with
[assessment/task-scoring-sheet.md](../assessment/task-scoring-sheet.md). The demo uses
[assessment/final-demo-qa-guide.md](../assessment/final-demo-qa-guide.md). Together with the
evidence from Weeks 1–3, they feed the rubric and the
[four-week review](../assessment/four-week-review-template.md).
