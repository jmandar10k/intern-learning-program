# Task 2 (medium): RAG over the university IT help docs

**Time box:** ≈ 1.5 days. **Skills shown:** chunking, embeddings and retrieval, evaluation of
retrieval quality.

## Context

The fictional **Northbridge University** IT desk answers the same questions every day. They
want an assistant that answers from the official help articles, cites its sources, and says
"I don't know" when the articles do not cover a question.

- Articles: [data/docs/](data/docs/) (14 short Markdown files).
- Evaluation set: [data/eval_set.json](data/eval_set.json): 20 questions; for each, the
  relevant article(s), whether it is answerable from the docs, and a short phrase a correct
  answer must contain.
- Offline model stubs: [starter/llm_stubs.py](starter/llm_stubs.py) (`HashEmbedder`, `StubLLM`).
  See [starter/README.md](starter/README.md). You may write your own retrieval components
  (BM25, vector search, rerankers); LangChain is allowed but not required.

## What to do

1. **Build the pipeline**: load → chunk → embed/index → retrieve → (rerank) → prompt → answer
   with citations.
2. **Evaluate retrieval separately from generation**:
   - recall@k and MRR (document level) on the answerable questions;
   - compare **at least two configurations** (e.g. chunk sizes, dense vs BM25 vs hybrid) in a
     table, and justify your final choice.
3. **Evaluate answers**: share of answerable questions whose answer contains the expected
   phrase and cites a relevant article; share of unanswerable questions where the system
   abstains.
4. **Analyse failures**: for every question your final system gets wrong, explain whether
   retrieval or generation failed, and why.

## Deliver

`task2/` as described in [submission-guidelines.md](../submission-guidelines.md), including
`outputs/retrieval_comparison.md` (or `.csv`) and `outputs/answers.json`.

## Acceptance criteria

See [acceptance-criteria.md](acceptance-criteria.md).
