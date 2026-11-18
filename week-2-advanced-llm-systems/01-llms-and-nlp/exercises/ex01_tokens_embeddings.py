"""Week 2 / 01 LLMs and NLP / Exercise 1: tokenization and embeddings.

Run:  python ex01_tokens_embeddings.py
"""
from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_stubs import HashEmbedder  # noqa: E402


def train_bpe(corpus: list[str], num_merges: int) -> list[tuple[str, str]]:
    """Minimal byte-pair encoding: repeatedly merge the most frequent adjacent symbol pair."""
    words = Counter(tuple(w) + ("</w>",) for line in corpus for w in line.lower().split())
    merges: list[tuple[str, str]] = []
    for _ in range(num_merges):
        pairs: Counter = Counter()
        for word, freq in words.items():
            for a, b in zip(word, word[1:]):
                pairs[(a, b)] += freq
        if not pairs:
            break
        best = max(pairs, key=pairs.get)
        merges.append(best)
        new_words: Counter = Counter()
        for word, freq in words.items():
            out, i = [], 0
            while i < len(word):
                if i < len(word) - 1 and (word[i], word[i + 1]) == best:
                    out.append(word[i] + word[i + 1])
                    i += 2
                else:
                    out.append(word[i])
                    i += 1
            new_words[tuple(out)] += freq
        words = new_words
    return merges


def bpe_encode(word: str, merges: list[tuple[str, str]]) -> list[str]:
    symbols = list(word.lower()) + ["</w>"]
    for a, b in merges:
        i = 0
        while i < len(symbols) - 1:
            if symbols[i] == a and symbols[i + 1] == b:
                symbols[i : i + 2] = [a + b]
            else:
                i += 1
    return symbols


def main() -> None:
    corpus = [
        "delivery delayed delivery late deliveries delayed",
        "the courier delivered the order late",
        "refund requested for late delivery",
        "delivery slot delivery window delivery time",
    ] * 5
    merges = train_bpe(corpus, num_merges=30)
    print("first 8 merges:", merges[:8])
    for w in ["delivery", "deliveries", "redelivery", "1234567"]:
        print(f"  {w!r:<14} -> {bpe_encode(w, merges)}")
    print("  common words compress to few tokens; unseen words and numbers fragment.\n")

    # Cosine vs dot vs L2: equivalent rankings only when vectors are normalized.
    rng = np.random.default_rng(0)
    q = rng.normal(size=8)
    docs = rng.normal(size=(5, 8)) * rng.uniform(0.2, 5.0, size=(5, 1))  # very different norms
    cos = docs @ q / (np.linalg.norm(docs, axis=1) * np.linalg.norm(q))
    dot = docs @ q
    l2 = np.linalg.norm(docs - q, axis=1)
    print("rank by cosine:", np.argsort(-cos), " by dot:", np.argsort(-dot), " by L2 (asc):", np.argsort(l2))
    dn = docs / np.linalg.norm(docs, axis=1, keepdims=True)
    qn = q / np.linalg.norm(q)
    print(
        "after L2-normalizing: cosine", np.argsort(-(dn @ qn)),
        " dot", np.argsort(-(dn @ qn)), " L2", np.argsort(np.linalg.norm(dn - qn, axis=1)),
    )

    emb = HashEmbedder()
    pairs = [
        ("my order arrived late", "the delivery was late"),
        ("I want a refund", "please give me my money back"),
        ("I want a refund", "refund policy for damaged items"),
    ]
    print("\nHashEmbedder cosine similarity (word overlap only):")
    for a, b in pairs:
        print(f"  {emb.embed(a) @ emb.embed(b):.2f}  {a!r} ~ {b!r}")
    print("  -> 'refund' vs 'money back' scores 0: no shared words. A real embedding model would not.")
    print(
        "\nYour turn:\n"
        "  1. Increase num_merges to 100. How does the encoding of 'redelivery' change?\n"
        "  2. Explain why a vector store that ranks by L2 distance on unnormalized vectors can\n"
        "     return different results than cosine similarity.\n"
        "  3. Add a tiny synonym map to HashEmbedder (refund ~ money back). What are the risks?"
    )


if __name__ == "__main__":
    main()
