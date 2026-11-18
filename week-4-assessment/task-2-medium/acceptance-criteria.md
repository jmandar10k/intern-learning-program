# Task 2 acceptance criteria

## Must

| # | Criterion | How it is checked |
|---|---|---|
| M1 | The pipeline runs offline end to end with one documented command and answers all 20 questions in `eval_set.json`. | Mentor runs it |
| M2 | Chunking is documented (unit, size, overlap) and covers all text; overlap < size. | Code / README |
| M3 | Retrieval is evaluated **separately** from generation, with recall@k and MRR at document level on the 17 answerable questions. | `outputs/retrieval_comparison.*` |
| M4 | At least **two** retrieval configurations are compared in one table, and the final choice is justified. | Output + README |
| M5 | Final configuration reaches **recall@3 ≥ 0.90** and **MRR ≥ 0.75** on the answerable questions. | Output (mentor re-runs) |
| M6 | Answers cite their source article(s). At least **13 of 17** answerable questions are answered with the expected phrase and a relevant citation. | `outputs/answers.json` |
| M7 | The system abstains ("I don't know…") on **all 3** unanswerable questions. | `outputs/answers.json` |
| M8 | Every wrong or missed question has a short failure analysis: retrieval vs generation, and why. | README |

## Should

| # | Criterion |
|---|---|
| S1 | Hybrid retrieval (dense + BM25, e.g. reciprocal rank fusion) or a reranking step, with its effect measured. |
| S2 | The abstention rule is principled (e.g. a score threshold tuned on the eval set, with the trade-off discussed) rather than hard-coded per question. |
| S3 | Tests for chunking (coverage, overlap) and for the metric functions (a hand-computed MRR example). |
| S4 | Discussion of the stub embedder's limits (word overlap only) and what would change with a real embedding model. |
| S5 | Prompt treats retrieved text as data (instructions/delimiters), with a note on prompt injection via documents. |
