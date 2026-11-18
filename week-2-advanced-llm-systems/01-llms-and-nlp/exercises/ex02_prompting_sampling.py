"""Week 2 / 01 LLMs and NLP / Exercise 2: prompting and sampling.

Run:  python ex02_prompting_sampling.py
"""
from __future__ import annotations

import string
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_stubs import StubLLM  # noqa: E402

QA_TEMPLATE = string.Template(
    "You are a support assistant. Answer ONLY from the context. "
    "If the answer is not in the context, say you don't know.\n"
    "Context: $context\n"
    "Question: $question\n"
)

CONTEXT = (
    "Orders can be cancelled free of charge until the courier is assigned. "
    "Late deliveries of more than 30 minutes receive an automatic 10% credit. "
    "Refunds for missing items are issued within 3 business days."
)


def softmax(logits: np.ndarray, temperature: float) -> np.ndarray:
    z = logits / max(temperature, 1e-6)
    z = z - z.max()
    p = np.exp(z)
    return p / p.sum()


def main() -> None:
    llm = StubLLM(seed=1)
    for q in [
        "How long do refunds for missing items take?",
        "Can I cancel my order before the courier is assigned?",
        "Do you deliver to other cities?",
    ]:
        prompt = QA_TEMPLATE.substitute(context=CONTEXT, question=q)  # substitute() raises on missing vars
        print(f"Q: {q}\nA: {llm.complete(prompt)}\n")

    # Few-shot classification prompt (format steering).
    for review in ["Courier was fast and friendly, thanks!", "Food arrived cold and an item was missing"]:
        print(f"sentiment({review!r}) = {llm.complete('Classify sentiment: ' + review)}")

    # Temperature: same logits, different distributions.
    logits = np.array([3.0, 2.0, 1.0, 0.2])
    for t in [0.1, 0.7, 1.0, 2.0]:
        print(f"T={t:<4} probs={np.round(softmax(logits, t), 3)}")

    # Determinism: temperature 0 is repeatable; >0 varies with the seed.
    prompt = QA_TEMPLATE.substitute(context=CONTEXT, question="What happens with late deliveries and refunds?")
    print("\nT=0 three runs  :", {StubLLM(seed=s).complete(prompt, 0.0)[:40] for s in range(3)})
    print("T=1.0 three runs:", {StubLLM(seed=s).complete(prompt, 1.0)[:40] for s in range(3)})
    print(
        "\nYour turn:\n"
        "  1. Use Template.safe_substitute with a misspelled variable ($questoin). What does the\n"
        "     model receive, and why is the output still fluent?\n"
        "  2. Rewrite QA_TEMPLATE to require a JSON output {\"answer\": str, \"source_sentence\": str}.\n"
        "  3. Which tasks in this program should always run at temperature 0? Why?"
    )


if __name__ == "__main__":
    main()
