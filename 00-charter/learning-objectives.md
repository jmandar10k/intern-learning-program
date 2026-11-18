# Learning objectives

Shared with the intern on Day 1. These are the outcomes you will be evaluated against.
How they are scored is in [evaluation-rubric.md](evaluation-rubric.md).

## Overall objectives

By the end of Week 4 you should be able to:

1. **Build and evaluate ML models correctly**: clean and explore data, choose a model and a
   metric that fit the problem, and avoid leakage and other evaluation traps.
2. **Build LLM systems that hold up**: design a RAG pipeline, a tool-calling agent or a
   LangGraph workflow, and measure whether it works rather than assume it does.
3. **Review code for silent failures**: find bugs that raise no error, explain them with
   theory, fix them, and add a check that stops them coming back.
4. **Use GenAI responsibly**: get real value from AI assistants while verifying their output,
   disclosing their use and protecting data.
5. **Speak the domain basics**: hold an informed conversation about returns, strategies,
   backtests and risk metrics, the context of later finance-related projects.
6. **Work as a contributor**: communicate progress, ask good questions, unblock yourself, and
   document and demo your work clearly.

## Per-week objectives

### Week 1: foundations (intermediate)

After Week 1 you can:

- Write idiomatic, typed, tested Python using classes, generators, decorators and context managers,
  and package it as an installable module.
- Load, clean, join, aggregate and visualize tabular data with pandas, numpy, matplotlib and
  seaborn, and reconcile your totals with the raw data.
- Explain distributions, sampling, hypothesis tests, p-values, confidence intervals, correlation
  and common biases, and apply them to a small dataset.
- Train and compare regression, tree, ensemble and clustering models with a correct train/test
  protocol, choose metrics suited to the problem, and spot data leakage.

### Week 2: advanced LLM systems (advanced)

After Week 2 you can:

- Explain transformers, tokenization, embeddings and prompting at a level that lets you predict
  how a model will behave, and say when fine-tuning is or is not appropriate.
- Build a retrieval pipeline (chunking, embedding, vector search, hybrid search, reranking) and
  evaluate it with retrieval metrics such as recall@k and MRR.
- Explain ReAct, function calling, planning, memory and guardrails, and implement a tool-calling
  loop that handles tool results and errors correctly.
- Build chains and graphs with LangChain and LangGraph, including typed state, reducers and
  conditional edges.
- Evaluate LLM output (reference-based, rubric, LLM-as-judge), detect hallucination, and apply
  safety and privacy practices.

### Week 3: domain primer and code review (apply)

After Week 3 you can:

- Explain the finance basics in the primer (returns, strategies, backtesting, performance and
  risk metrics, common pitfalls) in plain language.
- Review unfamiliar code that runs cleanly but is wrong, find the bug from the output and theory,
  explain its root cause, fix it and verify the fix.
- Write a clear review: symptom, root cause, the theory that explains it, fix, verification.

### Week 4: practical assessment

By the end of Week 4 you have:

- Delivered three working tasks (easy, medium, hard) that meet their acceptance criteria.
- Shown your judgment in a design note and a failure-case analysis.
- Demoed your work and answered technical questions about your choices.

## How progress is checked

| When | How | Template |
|---|---|---|
| End of Weeks 1, 2, 3 | Weekly check-in (30–45 min) | [assessment/weekly-checkin-template.md](../assessment/weekly-checkin-template.md) |
| Weeks 1, 2 | Self-check quiz (ungraded, discussed at the check-in) | `self-check-quiz.md` in each week |
| Week 3 | Review submissions for each exercise | [review-submission-template.md](../week-3-code-review/review-submission-template.md) |
| Week 4 | Three tasks, demo with Q&A, four-week review | [week-4-assessment/](../week-4-assessment/) |
