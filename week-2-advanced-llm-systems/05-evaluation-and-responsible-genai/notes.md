# 05 Evaluation and responsible GenAI

Level: advanced. Time: ≈ half a day.
Links: [study-materials.md](../study-materials.md#05-evaluation-and-responsible-genai).

## After this topic you can

- Design an evaluation for an LLM feature: test set, metrics, baseline, acceptance threshold.
- Use reference-based metrics (exact match, token F1), rubric/LLM-as-judge scoring, and
  groundedness checks, and know the blind spots of each.
- Detect and reduce hallucination.
- Apply safety and privacy basics: prompt injection, sensitive data, excessive agency, output
  handling (OWASP LLM Top 10).
- Verify AI-generated code and text before you rely on it (see the
  [GenAI usage policy](../../00-charter/genai-usage-policy.md)).

## Concepts

### Why evaluate

LLM output is fluent whether or not it is right. Without an eval set you cannot tell whether a
prompt or retrieval change helped. Treat evals as tests: versioned, re-run on every change.

### Building an eval

1. **Collect** 30–100 realistic inputs, including edge cases and adversarial ones.
2. **Label** expected outputs or acceptance rules.
3. **Choose metrics** that match the task:

| Task | Metrics |
|---|---|
| Extraction / short answers | Exact match, token F1 |
| Classification / routing | Accuracy, per-class precision/recall, confusion matrix |
| Retrieval | recall@k, MRR |
| Open-ended answers | Rubric scores (human or LLM-as-judge), groundedness, answer relevance |
| Agents | Task success, correct tool sequence, number of steps, policy violations |

4. **Baseline** and **threshold**: what score ships?
5. **Look at failures**, not just averages.

### LLM-as-judge

Useful at scale, but judges are biased (position, verbosity, self-preference) and can be fooled.
Use a precise rubric, low temperature, and calibrate against a sample of human labels.

### Hallucination

- **Intrinsic:** contradicts the provided context. **Extrinsic:** adds unsupported claims.
- Reduce with RAG, "answer only from context / say you don't know" instructions, citations, low
  temperature, and **groundedness checks** (is every answer sentence supported by a retrieved
  passage?).

### Safety and privacy

| Risk (OWASP LLM 2025) | What it looks like | Mitigation |
|---|---|---|
| LLM01 Prompt injection | "Ignore previous instructions…" in user input or in a retrieved document | Separate instructions from data, limit tool permissions, detect and filter, never let output trigger privileged actions directly |
| LLM02 Sensitive information disclosure | PII, keys or internal data in prompts, logs or outputs | Redact before sending, minimize data, access control |
| LLM05 Improper output handling | Model output passed to a shell, SQL or HTML unchecked | Validate and escape like any untrusted input |
| LLM06 Excessive agency | Agent has more tools/permissions than needed | Least privilege, human approval for risky actions |
| LLM08 Vector and embedding weaknesses | Poisoned or unauthorized documents in the index | Access-controlled retrieval, source validation |
| LLM09 Misinformation | Confident wrong answers relied upon | Grounding, citations, human review where stakes are high |

### Verifying AI output (your own use)

Run it, test it, check claims against primary sources, and be able to explain it. That is
"GenAI judgment" in the [evaluation rubric](../../00-charter/evaluation-rubric.md).

## Exercises

| File | What it shows |
|---|---|
| `exercises/ex01_eval_harness.py` | Exact match, token F1, a groundedness check and a rubric judge over a small eval set; comparing two prompt variants |
| `exercises/ex02_guardrails.py` | PII redaction before sending text to a model, prompt-injection detection in retrieved documents, output validation |

## Common mistakes

- Evaluating on five hand-picked examples.
- Reporting an average that hides a category with 0% success.
- Trusting an LLM judge without checking it against humans.
- Logging raw prompts that contain personal data.
