# Environment setup

Everything in this program runs **offline** on a laptop. No API keys, no GPU, no data
subscriptions.

## Python version

**Python 3.11** (3.10–3.12 should work). The program was built and verified with
Python 3.11.9.

```bash
python --version
```

## Create a virtual environment

```bash
# from the repository root
python -m venv .venv

# activate
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows (PowerShell or cmd)

python -m pip install --upgrade pip
pip install -r requirements.txt
```

## What gets installed

[requirements.txt](../requirements.txt) at the repository root:

| Package | Used for |
|---|---|
| numpy, pandas, scipy | Data handling, statistics (Weeks 1, 3, 4) |
| scikit-learn | ML models and evaluation (Weeks 1, 3, 4) |
| matplotlib, seaborn | Plots (Week 1, Week 4 Task 1) |
| pytest | Tests (all weeks) |
| langchain-core, langgraph | Week 2 topic 04, Week 3 ex07, Week 4 Task 3 (all offline) |

Versions verified when building the program: numpy 2.4.4, pandas 2.2.3, scipy 1.17.0,
scikit-learn 1.8.0, matplotlib 3.10.9, langchain-core 1.2.4, langgraph 1.0.5.

Each Week 3 exercise also has its own small `requirements.txt` listing only what it needs.

## Check your setup

```bash
python -c "import numpy, pandas, scipy, sklearn, matplotlib, seaborn, langgraph, langchain_core; print('ok')"
cd week-1-foundations/01-python-advanced/exercises && python -m pytest -q
```

## LLMs and embeddings

All LLM and embedding calls use deterministic offline stubs:

- Week 2: [week-2-advanced-llm-systems/llm_stubs.py](../week-2-advanced-llm-systems/llm_stubs.py)
- Week 3: each exercise contains its own small stub
- Week 4: `starter/llm_stubs.py` in Tasks 2 and 3

If you later get approved access to a hosted model, keep the stub interface and swap the
implementation, and follow the [GenAI usage policy](../00-charter/genai-usage-policy.md) for
what data may be sent.

## Editor

Any editor works. Recommended: VS Code with the Python extension; enable a formatter and a
linter (e.g. ruff) and run `mypy` on the Week 1 typing exercise.

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError` | The virtual environment is not active, or `pip install -r requirements.txt` was not run |
| Plots do not appear | Exercises save plots to files (`plots/`); no display is needed |
| Unicode errors in a Windows console | Run `set PYTHONIOENCODING=utf-8` (cmd) or `$env:PYTHONIOENCODING="utf-8"` (PowerShell) |
