"""Review-response assistant for an outdoor-gear shop.

A three-step prompt chain per customer review:
  1. summarize the review
  2. classify sentiment (negative reviews are routed to the support queue)
  3. draft a reply to the customer
The LLM is a deterministic offline stub (no API key needed).

Run:  python main.py
"""
from __future__ import annotations

import json
import re
import zlib
from pathlib import Path

import numpy as np

DATA = Path(__file__).parent / "data" / "reviews.json"
TEMPERATURE = 0.9  # a bit of creativity makes replies sound less robotic

SUMMARY_PROMPT = "TASK: summarize\nProduct: {product}\nReview: {review_text}\n"
SENTIMENT_PROMPT = "TASK: sentiment\nReview: {review_text}\nAnswer with one word: positive or negative.\n"
REPLY_PROMPT = "TASK: reply\nProduct: {product}\nSentiment: {sentiment}\nSummary: {summary}\n"


class _KeepMissing(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"


def render(template: str, **values: str) -> str:
    """Fill a prompt template. Optional fields that are not supplied are left untouched."""
    return template.format_map(_KeepMissing(values))


class StubLLM:
    """Deterministic stand-in for a chat model."""

    NEG = ("snapped", "disappointed", "small", "loose", "stopped", "never", "broke", "leak")
    POS = ("great", "love", "excellent", "dry", "cold all day", "well")

    def generate(self, prompt: str, temperature: float = 0.0) -> str:
        task = prompt.split("\n", 1)[0]
        field = lambda name: (re.search(rf"^{name}: (.*)$", prompt, re.M) or [None, ""])[1]  # noqa: E731
        if task == "TASK: summarize":
            review = field("Review")
            if not review or review.startswith("{"):
                return f"The customer shared general feedback about the {field('Product')}."
            return "The customer says: " + review.split(". ")[0].rstrip(".").lower() + "."
        if task == "TASK: sentiment":
            text = field("Review").lower()
            label = "negative" if sum(w in text for w in self.NEG) > sum(w in text for w in self.POS) else "positive"
            rng = np.random.default_rng(zlib.crc32(prompt.encode()))
            if rng.random() < 0.5 * temperature:  # sampling noise grows with temperature
                label = "positive" if label == "negative" else "negative"
            return label
        if task == "TASK: reply":
            summary, product = field("Summary"), field("Product")
            if field("Sentiment") == "negative":
                return f"We're sorry to hear about your {product}. {summary} We'll send a replacement right away."
            return f"Thank you for the kind words about your {product}! {summary} Enjoy your next trip."
        return ""


def main() -> None:
    reviews = json.loads(DATA.read_text(encoding="utf-8"))
    llm = StubLLM()
    memory: list[str] = []
    support_queue = []

    for r in reviews:
        summary = llm.generate(render(SUMMARY_PROMPT, product=r["product"], review=r["text"]), TEMPERATURE)
        memory.append(summary)
        sentiment = llm.generate(render(SENTIMENT_PROMPT, review_text=r["text"]), TEMPERATURE)
        reply = llm.generate(render(REPLY_PROMPT, product=r["product"], sentiment=sentiment, summary=memory[0]), TEMPERATURE)
        if sentiment == "negative":
            support_queue.append(r["id"])
        print(f"[{r['id']}] {r['product']}  sentiment={sentiment}")
        print(f"     summary: {summary}")
        print(f"     reply  : {reply}\n")

    print(f"routed to support queue: {support_queue}")


if __name__ == "__main__":
    main()
