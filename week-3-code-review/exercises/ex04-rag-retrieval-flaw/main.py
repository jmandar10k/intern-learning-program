"""Help-center assistant for "CloudNote", a note-taking app.

Retrieval-augmented QA over the help articles in data/docs/. Embeddings and the answer
model are deterministic offline stubs (no API key needed).

Run:  python main.py
"""
from __future__ import annotations

import json
import re
import zlib
from pathlib import Path

import numpy as np

DATA = Path(__file__).parent / "data"
CHUNK_SIZE = 25     # words per chunk
CHUNK_OVERLAP = 10  # words shared between neighbouring chunks
TOP_K = 3

STOP = set("a an the is are be to of in on for and or with by at from as it its this that what which how when do does can i my your you".split())


def words(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z0-9]+", text.lower()) if w not in STOP]


class Embedder:
    """Stub embedding model: hashed bag of words, L2-normalised."""

    def __init__(self, dim: int = 512) -> None:
        self.dim = dim

    def embed(self, text: str) -> np.ndarray:
        v = np.zeros(self.dim)
        for w in words(text):
            v[zlib.crc32(w.encode()) % self.dim] += 1.0
        n = np.linalg.norm(v)
        return v / n if n else v


class AnswerModel:
    """Stub LLM: answers with the context sentence that best matches the question."""

    def answer(self, question: str, context: list[str]) -> str:
        q = set(words(question))
        sentences = [s.strip() for c in context for s in re.split(r"(?<=[.!?])\s+", c) if s.strip()]
        if not sentences:
            return "No information found."
        return max(sentences, key=lambda s: len(q & set(words(s))))


def chunk(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    tokens = text.split()
    step = size + overlap
    return [" ".join(tokens[i : i + size]) for i in range(0, len(tokens), step)]


class Index:
    def __init__(self, embedder: Embedder) -> None:
        self.embedder = embedder
        self.chunks: list[tuple[str, str]] = []  # (source, text)
        self.vectors = np.zeros((0, embedder.dim))

    def add(self, source: str, text: str) -> None:
        for c in chunk(text):
            self.chunks.append((source, c))
        self.vectors = np.vstack([self.embedder.embed(t) for _, t in self.chunks])

    def search(self, query: str, k: int = TOP_K) -> list[tuple[str, str]]:
        scores = self.vectors @ self.embedder.embed(query)  # cosine similarity
        nearest = np.argsort(scores)[:k]  # nearest chunks first
        return [self.chunks[i] for i in nearest]


def main() -> None:
    index = Index(Embedder())
    for path in sorted((DATA / "docs").glob("*.md")):
        index.add(path.name, path.read_text(encoding="utf-8"))
    print(f"indexed {len(index.chunks)} chunks from {len(list((DATA / 'docs').glob('*.md')))} articles\n")

    model = AnswerModel()
    for item in json.loads((DATA / "eval_queries.json").read_text(encoding="utf-8")):
        hits = index.search(item["question"])
        answer = model.answer(item["question"], [t for _, t in hits])
        print(f"Q: {item['question']}")
        print(f"   sources: {[s for s, _ in hits]}")
        print(f"   A: {answer}\n")


if __name__ == "__main__":
    main()
