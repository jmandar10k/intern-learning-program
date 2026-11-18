"""Week 2 / 03 Agents / Exercise 2: workflow patterns as plain code.

Often you do not need an agent: a fixed workflow is cheaper, faster and easier to test.
Run:  python ex02_workflow_patterns.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_stubs import StubLLM, content_words  # noqa: E402

llm = StubLLM()

KB = {
    "billing": "Refunds for missing items are issued within 3 business days. Refunds above 50.00 require a review.",
    "delivery": "If your delivery is more than 30 minutes late you receive an automatic credit of 10% of the basket value.",
    "account": "Enable two-factor authentication in Settings to protect your account.",
}
ROUTES = {
    "billing": {"refund", "charge", "money", "payment", "card"},
    "delivery": {"late", "courier", "delivery", "slot", "eta"},
    "account": {"password", "login", "account", "two-factor"},
}


def route(message: str) -> str:
    """Routing: classify, then send to a specialised handler."""
    words = set(content_words(message)) | set(message.lower().split())
    scores = {r: len(words & kw) for r, kw in ROUTES.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "human"


def chain(message: str) -> str:
    """Prompt chaining: step 1 summarize, step 2 classify sentiment, step 3 answer from KB."""
    summary = llm.complete("Summarize: " + message)
    sentiment = llm.complete("Classify sentiment: " + message)
    topic = route(message)
    if topic == "human":
        return f"[{sentiment}] escalated to a human: {summary}"
    answer = llm.complete(f"Context: {KB[topic]}\nQuestion: {message}\n")
    return f"[{sentiment}|{topic}] {answer}"


def evaluator_optimizer(draft: str, max_rounds: int = 3) -> str:
    """Evaluator-optimizer: check a draft against rules, revise until it passes."""
    rules = [
        ("must not promise a specific refund date", lambda t: "tomorrow" not in t.lower()),
        ("must be under 25 words", lambda t: len(t.split()) <= 25),
        ("must end with an offer of further help", lambda t: t.rstrip().endswith("help?")),
    ]
    for round_ in range(1, max_rounds + 1):
        failed = [name for name, ok in rules if not ok(draft)]
        print(f"  round {round_}: failed={failed}")
        if not failed:
            return draft
        if "must not promise a specific refund date" in failed:
            draft = draft.replace("tomorrow", "within 3 business days")
        if "must be under 25 words" in failed:
            draft = " ".join(draft.split()[:20]).rstrip(".,") + "."
        if "must end with an offer of further help" in failed:
            draft = draft.rstrip() + " Anything else I can help?"
    return draft


def main() -> None:
    for msg in [
        "My delivery was 40 minutes late and the courier was rude.",
        "I was charged twice, I want my money back for the refund.",
        "How do I change my password and login?",
        "What is the meaning of life?",
    ]:
        print(f"{msg!r}\n  -> {chain(msg)}")
    print("\nEvaluator-optimizer:")
    final = evaluator_optimizer(
        "We are very sorry about the missing items in your order and we will make sure that your refund arrives tomorrow without any further problems at all."
    )
    print("  final:", final)
    print(
        "\nYour turn:\n"
        "  1. Which of these would you turn into an agent, if any? Justify in two sentences.\n"
        "  2. Add a 'parallelization' step: run two independent checks and combine them."
    )


if __name__ == "__main__":
    main()
