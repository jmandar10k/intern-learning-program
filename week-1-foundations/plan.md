# Week 1 plan: foundations (learn, intermediate)

Purely study. Each topic has a `notes.md`, small runnable exercises, and curated links in
[study-materials.md](study-materials.md). The examples use the
[reference problem](reference-problem-statement.md).

**Objectives:** see the Week 1 section of
[00-charter/learning-objectives.md](../00-charter/learning-objectives.md).

## Schedule

| Day | Morning (≈3 h) | Afternoon (≈3.5 h) |
|---|---|---|
| 1 | Read [00-charter/](../00-charter/), [environment setup](../resources/environment-setup.md), [reference problem](reference-problem-statement.md) | [01 Python advanced](01-python-advanced/notes.md): notes + core link |
| 2 | 01 Python advanced: exercises (`python -m pytest` must pass) | [02 Data analysis and viz](02-data-analysis-viz/notes.md): notes + core link |
| 3 | 02 Data analysis and viz: exercises | [03 Statistics](03-statistics/notes.md): notes, core link, exercises |
| 4 | [04 ML algorithms and evaluation](04-ml-algorithms-evaluation/notes.md): notes + core link | 04 exercises |
| 5 | Catch up, optional links, [self-check quiz](self-check-quiz.md) | **Week 1 check-in** (30–45 min) |

## Running the exercises

```bash
cd week-1-foundations/01-python-advanced/exercises
python ex01_oop_generators.py
python -m pytest -q
```

Every script runs offline in seconds and generates its own synthetic data with a fixed seed.
Each script ends with a **Your turn** list; do those modifications and keep notes in
[progress-log/week-1-log.md](../progress-log/week-1-log.md).

## Week 1 check-in (Day 5)

Run by the mentor with [assessment/weekly-checkin-template.md](../assessment/weekly-checkin-template.md).
Focus: **concept clarity, learning pace, questions raised.** Bring:

- Your quiz answers (ungraded).
- One concept you found hard and how you worked through it.
- Your questions list.
