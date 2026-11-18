"""Week 2 / 05 Evaluation / Exercise 1: a small eval harness.

Compares two prompt variants on the same eval set with several metrics.
Run:  python ex01_eval_harness.py
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_stubs import StubLLM, content_words, split_sentences  # noqa: E402

CONTEXT = (
    "Orders can be cancelled free of charge until a courier is assigned. "
    "After a courier is assigned, a cancellation fee of 3.00 applies. "
    "If your delivery is more than 30 minutes late you receive an automatic credit of 10% of the basket value. "
    "Refunds for missing items are issued within 3 business days. "
    "The delivery fee is free for baskets of 40.00 or more."
)

EVAL_SET = [
    {"q": "What is the cancellation fee after a courier is assigned?", "ref": "3.00", "answerable": True},
    {"q": "How much credit for a delivery more than 30 minutes late?", "ref": "10% of the basket value", "answerable": True},
    {"q": "How many business days for refunds for missing items?", "ref": "3 business days", "answerable": True},
    {"q": "Which baskets get a free delivery fee?", "ref": "40.00 or more", "answerable": True},
    {"q": "Do you deliver alcohol?", "ref": "I don't know", "answerable": False},
    {"q": "What is the phone number of support?", "ref": "I don't know", "answerable": False},
]

PROMPT_STRICT = "Answer only from the context. Say you don't know if it is not there.\nContext: {c}\nQuestion: {q}\n"
PROMPT_NO_CONTEXT = "Context: \nQuestion: {q}\n"  # a "variant" that forgot to pass the context


def normalize(s: str) -> list[str]:
    return re.findall(r"[a-z0-9.%]+", s.lower())


def exact_match(pred: str, ref: str) -> float:
    return float(" ".join(normalize(ref)) in " ".join(normalize(pred)))


def token_f1(pred: str, ref: str) -> float:
    p, r = normalize(pred), normalize(ref)
    common = sum((Counter(p) & Counter(r)).values())
    if common == 0:
        return 0.0
    precision, recall = common / len(p), common / len(r)
    return 2 * precision * recall / (precision + recall)


def grounded(pred: str, context: str) -> float:
    """Share of answer sentences whose content words are mostly found in one context sentence."""
    if "don't know" in pred.lower():
        return 1.0
    ctx = [set(content_words(s)) for s in split_sentences(context)]
    sents = split_sentences(pred)
    ok = 0
    for s in sents:
        w = set(content_words(s))
        ok += any(len(w & c) / max(len(w), 1) >= 0.7 for c in ctx)
    return ok / max(len(sents), 1)


def rubric_judge(pred: str, item: dict) -> int:
    """Stand-in for an LLM-as-judge with a 1-3 rubric:
    3 = correct and grounded, or correctly abstains; 2 = partially correct; 1 = wrong / hallucinated / wrong abstention."""
    abstained = "don't know" in pred.lower()
    if not item["answerable"]:
        return 3 if abstained else 1
    if abstained:
        return 1
    return 3 if exact_match(pred, item["ref"]) else 2 if token_f1(pred, item["ref"]) > 0.3 else 1


def run(name: str, template: str) -> None:
    llm = StubLLM()
    rows = []
    for item in EVAL_SET:
        pred = llm.complete(template.format(c=CONTEXT, q=item["q"]))
        rows.append((exact_match(pred, item["ref"]), token_f1(pred, item["ref"]), grounded(pred, CONTEXT), rubric_judge(pred, item)))
    n = len(rows)
    em, f1, gr, judge = (sum(col) / n for col in zip(*rows))
    answerable = [r for r, it in zip(rows, EVAL_SET) if it["answerable"]]
    print(
        f"{name:<18} EM={em:.2f}  F1={f1:.2f}  grounded={gr:.2f}  judge(1-3)={judge:.2f}  "
        f"EM on answerable only={sum(r[0] for r in answerable) / len(answerable):.2f}"
    )


def main() -> None:
    run("strict prompt", PROMPT_STRICT)
    run("context missing", PROMPT_NO_CONTEXT)
    print(
        "\nNote how 'grounded' stays high for the broken variant: it abstains everywhere, which is\n"
        "'safe' but useless. One metric is never enough; slice by answerable vs unanswerable.\n"
        "\nYour turn:\n"
        "  1. Add three adversarial questions (paraphrases with no word overlap). What breaks?\n"
        "  2. Make the judge stricter for partial answers. How much does the average move?\n"
        "  3. Which single number would you put in a dashboard, and which would you never show alone?"
    )


if __name__ == "__main__":
    main()
