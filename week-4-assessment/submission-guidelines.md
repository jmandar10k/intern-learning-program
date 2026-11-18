# Submission guidelines

## Repository layout

Submit one repository (or one branch) named `week4-<your-name>`:

```
week4-<your-name>/
├── README.md                 # overview, how to run everything, GenAI disclosure summary
├── requirements.txt          # pinned versions you used
├── task1/
│   ├── README.md             # approach, findings, results, limitations, GenAI disclosure
│   ├── src/ or *.py / *.ipynb
│   ├── tests/                # at least a few meaningful tests or sanity checks
│   └── outputs/              # plots, metrics.json
├── task2/
│   ├── README.md
│   ├── src/ ...
│   ├── tests/
│   └── outputs/              # retrieval comparison table, sample answers
└── task3/
    ├── README.md
    ├── design-note.md        # 1–2 pages
    ├── failure-analysis.md
    ├── src/ ...
    ├── tests/
    └── outputs/              # decisions log
```

Notebooks are fine for exploration, but the final pipeline for each task must run as a script
(`python task1/run.py`), so results are reproducible.

## Each task README must contain

1. **How to run** (exact commands, expected runtime).
2. **Approach**: what you built and why (key decisions and alternatives you rejected).
3. **Results**: the numbers the acceptance criteria ask for, with how you computed them.
4. **Verification**: how you know it is correct (tests, sanity checks, reconciliations).
5. **Limitations and next steps**: be honest; known weaknesses cost far less than hidden ones.
6. **GenAI disclosure** (template in the
   [GenAI usage policy](../00-charter/genai-usage-policy.md)).

## Code expectations

- Readable names, small functions, type hints on public functions.
- Fixed random seeds; no hard-coded absolute paths.
- No network calls, no API keys. Use the offline stubs provided in each task's `starter/`.
- Tests run with `python -m pytest`.

## Demo format (Day 20 morning, 45–60 min)

| Part | Time | Content |
|---|---|---|
| Overview | 5 min | What you built across the three tasks; one slide or README section is enough |
| Task 1 | 8 min | Key findings, evaluation protocol, how you avoided leakage |
| Task 2 | 10 min | Pipeline, retrieval comparison, one success and one failure case |
| Task 3 | 12 min | Live run, guardrails, design note highlights, failure analysis |
| Q&A | 15–25 min | Technical questions on your choices; see the demo guide |

Show running code, not only slides. Be ready to change a parameter live and explain the effect.

## Deadline

Push your final commit by **Day 19, 18:00**. Commits after the deadline are not considered.
