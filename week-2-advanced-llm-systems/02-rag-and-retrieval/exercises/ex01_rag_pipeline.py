"""Week 2 / 02 RAG / Exercise 1: a complete offline RAG pipeline with retrieval evaluation.

Pipeline: load -> chunk (with overlap) -> embed -> vector search | BM25 -> hybrid (RRF)
          -> rerank -> prompt -> StubLLM answer.
Evaluation: recall@k and MRR on labelled queries in data/eval_queries.json.

Run:  python ex01_rag_pipeline.py
"""
from __future__ import annotations

import json
import math
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from llm_stubs import HashEmbedder, StubLLM, content_words  # noqa: E402


@dataclass
class Chunk:
    doc: str
    text: str


def load_docs(folder: Path) -> dict[str, str]:
    return {p.name: p.read_text(encoding="utf-8") for p in sorted(folder.glob("*.md"))}


def chunk_words(text: str, size: int, overlap: int) -> list[str]:
    """Fixed-size word windows with overlap. Requires 0 <= overlap < size."""
    if not 0 <= overlap < size:
        raise ValueError("overlap must be >= 0 and < size")
    words = text.split()
    step = size - overlap
    return [" ".join(words[i : i + size]) for i in range(0, max(len(words) - overlap, 1), step)]


class VectorIndex:
    def __init__(self, chunks: list[Chunk], embedder: HashEmbedder) -> None:
        self.chunks, self.embedder = chunks, embedder
        self.matrix = embedder.embed_many([c.text for c in chunks])  # rows are L2-normalized

    def search(self, query: str, k: int) -> list[tuple[int, float]]:
        scores = self.matrix @ self.embedder.embed(query)  # cosine (normalized vectors)
        top = np.argsort(-scores)[:k]  # highest similarity first
        return [(int(i), float(scores[i])) for i in top]


class BM25:
    def __init__(self, chunks: list[Chunk], k1: float = 1.5, b: float = 0.75) -> None:
        self.docs = [content_words(c.text) for c in chunks]
        self.k1, self.b = k1, b
        self.avgdl = sum(map(len, self.docs)) / len(self.docs)
        df = Counter(w for d in self.docs for w in set(d))
        n = len(self.docs)
        self.idf = {w: math.log(1 + (n - f + 0.5) / (f + 0.5)) for w, f in df.items()}

    def search(self, query: str, k: int) -> list[tuple[int, float]]:
        q = content_words(query)
        scores = []
        for i, d in enumerate(self.docs):
            tf = Counter(d)
            s = sum(
                self.idf.get(w, 0) * tf[w] * (self.k1 + 1)
                / (tf[w] + self.k1 * (1 - self.b + self.b * len(d) / self.avgdl))
                for w in q
            )
            scores.append(s)
        top = np.argsort(-np.array(scores))[:k]
        return [(int(i), scores[i]) for i in top]


def rrf(rankings: list[list[tuple[int, float]]], k: int = 60) -> list[tuple[int, float]]:
    """Reciprocal rank fusion: combine rankings without calibrating their score scales."""
    fused: Counter = Counter()
    for ranking in rankings:
        for rank, (idx, _) in enumerate(ranking):
            fused[idx] += 1.0 / (k + rank + 1)
    return fused.most_common()


def rerank(query: str, candidates: list[int], chunks: list[Chunk]) -> list[int]:
    """Stand-in for a cross-encoder: score each (query, chunk) pair jointly using
    unigram + bigram overlap. A real cross-encoder model would go here."""
    qw = content_words(query)
    qb = set(zip(qw, qw[1:]))

    def score(i: int) -> float:
        cw = content_words(chunks[i].text)
        return len(set(qw) & set(cw)) + 2 * len(qb & set(zip(cw, cw[1:])))

    return sorted(candidates, key=lambda i: -score(i))


def evaluate(name: str, retrieve, queries: list[dict], chunks: list[Chunk], k: int = 3) -> None:
    hits, rr = 0, 0.0
    for q in queries:
        docs = [chunks[i].doc for i in retrieve(q["question"])][:k]
        if q["relevant"] in docs:
            hits += 1
            rr += 1 / (docs.index(q["relevant"]) + 1)
    print(f"  {name:<22} recall@{k}={hits / len(queries):.2f}  MRR={rr / len(queries):.2f}")


def main() -> None:
    docs = load_docs(HERE / "data" / "help_center")
    queries = json.loads((HERE / "data" / "eval_queries.json").read_text(encoding="utf-8"))
    embedder, llm = HashEmbedder(), StubLLM()

    for size, overlap in [(25, 5), (60, 10), (400, 0)]:
        chunks = [Chunk(name, c) for name, text in docs.items() for c in chunk_words(text, size, overlap)]
        vec, bm25 = VectorIndex(chunks, embedder), BM25(chunks)
        print(f"\nchunk size={size} overlap={overlap} -> {len(chunks)} chunks")
        evaluate("vector", lambda q: [i for i, _ in vec.search(q, 10)], queries, chunks)
        evaluate("bm25", lambda q: [i for i, _ in bm25.search(q, 10)], queries, chunks)
        evaluate("hybrid (RRF)", lambda q: [i for i, _ in rrf([vec.search(q, 10), bm25.search(q, 10)])], queries, chunks)
        evaluate(
            "hybrid + rerank",
            lambda q: rerank(q, [i for i, _ in rrf([vec.search(q, 10), bm25.search(q, 10)])][:8], chunks),
            queries,
            chunks,
        )

    # End-to-end answer with the mid-size configuration.
    chunks = [Chunk(name, c) for name, text in docs.items() for c in chunk_words(text, 60, 10)]
    vec, bm25 = VectorIndex(chunks, embedder), BM25(chunks)
    question = "How much credit do I get when my delivery is very late?"
    ids = rerank(question, [i for i, _ in rrf([vec.search(question, 10), bm25.search(question, 10)])][:8], chunks)[:2]
    context = "\n".join(f"[{chunks[i].doc}] {chunks[i].text}" for i in ids)
    prompt = f"Answer only from the context.\nContext: {context}\nQuestion: {question}\n"
    print(f"\nQ: {question}\nretrieved: {[chunks[i].doc for i in ids]}\nA: {llm.complete(prompt)}")
    print(
        "\nYour turn:\n"
        "  1. Why does chunk size 400 (one chunk per doc) still score well here? When would it fail?\n"
        "  2. Change VectorIndex.search to use L2 distance on UN-normalized bag-of-words vectors.\n"
        "     What happens to recall, and why?\n"
        "  3. Add 'hit rate of the answer sentence' as a second metric: is the sentence that\n"
        "     contains the answer inside the retrieved chunk(s)?"
    )


if __name__ == "__main__":
    main()
