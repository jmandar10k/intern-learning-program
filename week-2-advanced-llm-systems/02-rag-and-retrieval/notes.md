# 02 RAG and retrieval

Level: advanced. Time: ≈ 1 day.
Links: [study-materials.md](../study-materials.md#02-rag-and-retrieval).

## After this topic you can

- Build a retrieval-augmented generation pipeline end to end and explain each stage.
- Choose a chunking strategy (size, overlap, structure-aware) and predict its effect.
- Run dense (vector), sparse (BM25) and hybrid retrieval, and add a reranker.
- Evaluate retrieval separately from generation with recall@k, precision@k and MRR, and evaluate
  generation for groundedness and answer relevance.
- Diagnose why a RAG system gives a confident wrong answer.

## Concepts

### Pipeline

```
documents → load/clean → chunk → embed → index (vector store)            [offline]
question  → (rewrite) → retrieve top-k → rerank → build prompt → LLM → answer + citations  [online]
```

Two halves fail differently: **retrieval** fails by not finding the evidence; **generation**
fails by ignoring or misusing it. Measure them separately.

### Chunking

- Too small: answers split across chunks, context lost (e.g. "it" with no referent).
- Too large: chunk embeddings are diluted; the prompt fills with irrelevant text; costs rise.
- **Overlap** keeps sentences that straddle a boundary retrievable. Overlap must be smaller
  than the size; the step is `size − overlap`.
- Prefer structure-aware splitting (headings, paragraphs, sentences) over raw character counts.
- Keep metadata (source, section, date) with each chunk for filtering and citations.

### Vector stores and similarity

- Store chunk embeddings; search by nearest neighbors (exact or approximate: HNSW, IVF).
- The similarity **must match the embedding model's training**: usually cosine. Cosine on
  normalized vectors = dot product; L2 distance gives the same ranking only if vectors are
  normalized. **Higher similarity = better, lower distance = better**: mixing these up
  reverses the ranking.

### Sparse, dense, hybrid

- **BM25** (sparse): exact term matching with term-frequency saturation and IDF. Strong on ids,
  codes, rare terms.
- **Dense**: semantic matching (synonyms, paraphrases). Weak on exact codes.
- **Hybrid**: run both and fuse, e.g. **Reciprocal Rank Fusion** `Σ 1/(k + rank)`, which needs no
  score calibration.

### Reranking

Retrieve a generous candidate set (e.g. top-20) cheaply, then rerank with a **cross-encoder**
that reads query and chunk together; pass only the top few to the LLM. Improves precision at
the top, where it matters.

### Prompting for RAG

- Instruct: answer only from context, cite sources, say "I don't know" if the context is
  insufficient.
- Put the retrieved context between clear delimiters; treat it as data, not instructions
  (prompt injection via documents is real; see topic 05).

### Evaluation

| Stage | Metric | Needs |
|---|---|---|
| Retrieval | recall@k (is a relevant chunk in the top k?), precision@k, MRR (how high is the first relevant chunk?), nDCG | Labelled query → relevant doc/chunk pairs |
| Generation | Groundedness / faithfulness (is every claim supported by the context?), answer relevance, correctness vs reference | Context + answer (+ reference) |
| Both (RAG triad) | Context relevance, groundedness, answer relevance | |

Build a small labelled eval set early (20–50 queries) and rerun it after every change.

## Exercises

| File | What it shows |
|---|---|
| `exercises/ex01_rag_pipeline.py` | Chunking with overlap, cosine vector search, BM25, RRF hybrid, rerank, recall@k and MRR across chunk sizes, an end-to-end answer |
| `exercises/data/` | A small help-center corpus and labelled eval queries |

## Common mistakes

- Evaluating only final answers, so retrieval failures look like model failures.
- Sorting distances descending (or similarities ascending).
- Overlap ≥ chunk size (infinite loop or duplicated chunks).
- Passing too many chunks "to be safe", which drowns the answer.
