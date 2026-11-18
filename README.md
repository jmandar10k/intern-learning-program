# Intern Learning Program

A structured four-week onboarding and training program for a newly joined intern working on
ML, LLM and agentic systems. It covers the four mandated areas:

1. **Context:** a neutral reference problem in Week 1 and a finance domain primer in Week 3.
2. **Technology and tools:** Python, data, statistics, ML, LLMs, RAG, agents, LangChain and
   LangGraph, plus effective and responsible GenAI use.
3. **Guided hands-on work:** small exercises in Weeks 1–2, silent-bug code review in Week 3,
   and a three-task practical assessment in Week 4.
4. **Feedback and assessment:** weekly check-ins, a progress log, and a formal go/no-go review
   at the end of Week 4.

> **Start here (intern):** read everything in [00-charter/](00-charter/) on Day 1. It tells you
> what you will learn, how you are evaluated and what decides continuation after Week 4.

## Four-week timeline

| Week | Theme | Mode | Main folder | Ends with |
|---|---|---|---|---|
| 1 | Foundations: advanced Python, data analysis and visualization, statistics, ML algorithms and evaluation | Learn (intermediate) | [week-1-foundations/](week-1-foundations/) | Self-check quiz, weekly check-in |
| 2 | Advanced LLM systems: LLMs and NLP, RAG, agents and tool calling, LangChain and LangGraph, evaluation and responsible GenAI | Learn (advanced) | [week-2-advanced-llm-systems/](week-2-advanced-llm-systems/) | Self-check quiz, weekly check-in |
| 3 | Day 1: finance domain primer. Days 2–5: silent-bug code review | Apply | [week-3-code-review/](week-3-code-review/) | Review submission, weekly check-in |
| 4 | Practical assessment (easy, medium, hard), demo with Q&A, go/no-go review | Assess | [week-4-assessment/](week-4-assessment/) | Four-week review (go/no-go) |

The day-by-day schedule is in [00-charter/program-calendar.md](00-charter/program-calendar.md).

```
Week 1 ──► Week 2 ──► Week 3 ─────────────────────► Week 4
LEARN      LEARN      Day 1 primer │ Days 2-5 review   Tasks 1-3 ─► Demo + Q&A ─► Go/no-go
 └ check-in └ check-in              └ check-in
```

## How to use this repo

**Intern**

1. Set up your environment: [resources/environment-setup.md](resources/environment-setup.md).
2. Read [00-charter/](00-charter/), including the
   [GenAI usage policy](00-charter/genai-usage-policy.md).
3. Each week, open that week's `plan.md` and follow it day by day.
4. Keep notes in [progress-log/](progress-log/) (your section of `week-N-log.md`).
5. Use [resources/glossary.md](resources/glossary.md) and
   [resources/reading-list.md](resources/reading-list.md) as references.

**Mentor**

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) for how to update content and log feedback.
2. Run check-ins with [assessment/weekly-checkin-template.md](assessment/weekly-checkin-template.md).
3. Score Week 4 with [assessment/task-scoring-sheet.md](assessment/task-scoring-sheet.md) and
   decide with [assessment/four-week-review-template.md](assessment/four-week-review-template.md).

## Repository layout

| Path | Contents |
|---|---|
| [00-charter/](00-charter/) | Learning objectives, evaluation rubric, go/no-go criteria, calendar, GenAI policy |
| [week-1-foundations/](week-1-foundations/) | Notes, runnable exercises, curated links, reference problem, quiz |
| [week-2-advanced-llm-systems/](week-2-advanced-llm-systems/) | Notes, runnable exercises (offline stubs), curated links, quiz |
| [week-3-code-review/](week-3-code-review/) | Finance domain primer (Day 1) and seven silent-bug review exercises |
| [week-4-assessment/](week-4-assessment/) | Three practical tasks with briefs, data and acceptance criteria |
| [assessment/](assessment/) | Check-in template, scoring sheet, demo Q&A guide, four-week review |
| [progress-log/](progress-log/) | Weekly logs: intern notes, mentor feedback, action items |
| [resources/](resources/) | Glossary, reading list, environment setup, link-verification log |

## Ground rules

- **Offline and free.** All code runs on small synthetic data. No API keys, no network calls,
  no data subscriptions. LLMs and embeddings are deterministic stubs.
- **GenAI is allowed, with disclosure and verification.** See
  [00-charter/genai-usage-policy.md](00-charter/genai-usage-policy.md).
- **Evaluation is about learning, not volume.** The go/no-go decision rests on demonstrated
  learning, initiative and readiness to contribute, not on how much routine work was done.

## Study links

Each topic has **1 core + up to 2 optional** resources, with time estimates and level tags, in
each week's `study-materials.md`. Every link was found and checked by web search.

**Links last verified: 2026-11-18.** Re-check quarterly; the log is
[resources/link-verification-log.md](resources/link-verification-log.md).
