# Glossary: ML, LLM and tooling terms

Finance terms are in the [domain primer glossary](../week-3-code-review/domain-primer/glossary.md).

## Statistics and ML

| Term | Meaning |
|---|---|
| **Accuracy** | Share of correct predictions. Misleading on imbalanced classes |
| **Baseline** | The simplest reasonable model (e.g. always predict the majority class). Every model must beat it |
| **Bias–variance trade-off** | Simple models underfit (bias); complex models overfit (variance) |
| **Bootstrap** | Resampling with replacement to estimate uncertainty of a statistic |
| **Central limit theorem** | Means of many independent draws are approximately normal |
| **Class imbalance** | One class is much rarer than another |
| **Confidence interval** | Range from a procedure that captures the true value in a stated share of repeated samples |
| **Confounder** | A variable that influences both a cause and an effect, creating a spurious association |
| **Confusion matrix** | Table of true/false positives/negatives |
| **Cross-validation** | Repeated train/validation splits to estimate performance robustly |
| **Data leakage** | Information unavailable at prediction time influences training or evaluation |
| **Ensemble** | Combining models (bagging: random forest; boosting: gradient boosting) |
| **F1 score** | Harmonic mean of precision and recall. *Binary*: for the positive class; *macro*: unweighted mean over classes; *micro*: from global counts (= accuracy for single-label) |
| **Feature** | An input variable to a model |
| **Hypothesis test** | Procedure to judge whether data are consistent with a null hypothesis |
| **k-means** | Clustering into k groups by minimizing within-cluster distances |
| **MAE / RMSE** | Mean absolute error / root mean squared error |
| **Overfitting** | Fitting noise in the training data; poor generalization |
| **p-value** | Probability of data at least this extreme if the null hypothesis were true |
| **Pipeline** | Chained preprocessing + model fitted as one unit (prevents leakage) |
| **Precision / recall** | Of predicted positives, share correct / of actual positives, share found |
| **PR-AUC (average precision)** | Area under the precision–recall curve; informative under imbalance |
| **ROC-AUC** | Probability a random positive is ranked above a random negative |
| **Simpson's paradox** | A trend in every group reverses when groups are combined |
| **Stratification** | Preserving class proportions in splits |
| **Target leakage** | A feature derived from, or recorded after, the target |

## LLMs and NLP

| Term | Meaning |
|---|---|
| **Attention** | Mechanism letting each token weigh information from other tokens |
| **BPE** | Byte-pair encoding: subword tokenization by merging frequent pairs |
| **Chain-of-thought** | Prompting a model to reason step by step |
| **Context window** | Maximum number of tokens a model can read at once |
| **Cosine similarity** | Dot product of normalized vectors; similarity of direction |
| **Embedding** | Dense vector representation of text |
| **Few-shot prompting** | Including examples in the prompt |
| **Fine-tuning** | Further training a model on task-specific data (e.g. LoRA, parameter-efficient methods) |
| **Hallucination** | Fluent output that is unsupported or false |
| **LLM-as-judge** | Using a model to grade outputs against a rubric |
| **Prompt injection** | Untrusted text that tries to override instructions |
| **Temperature** | Sampling parameter; higher = more random |
| **Token** | Unit of text a model processes (often a subword) |
| **Top-p** | Sampling from the smallest token set with cumulative probability ≥ p |
| **Transformer** | Neural architecture based on self-attention |

## Retrieval and RAG

| Term | Meaning |
|---|---|
| **BM25** | Classic keyword ranking function (sparse retrieval) |
| **Chunking** | Splitting documents into retrievable pieces (size, overlap) |
| **Cross-encoder** | Model scoring a (query, passage) pair jointly; used for reranking |
| **Dense retrieval** | Retrieval by embedding similarity |
| **Groundedness / faithfulness** | Whether an answer is supported by the retrieved context |
| **Hybrid search** | Combining sparse and dense retrieval |
| **MRR** | Mean reciprocal rank of the first relevant result |
| **RAG** | Retrieval-augmented generation: retrieve evidence, then generate from it |
| **Recall@k** | Share of queries with a relevant item in the top k |
| **Reciprocal rank fusion (RRF)** | Combining rankings by summing 1/(k + rank) |
| **Reranking** | Re-ordering retrieved candidates with a stronger model |
| **Vector store** | Database for embeddings with nearest-neighbor search |

## Agents and workflows

| Term | Meaning |
|---|---|
| **Agent** | System where a model decides which steps/tools to use next |
| **Function / tool calling** | Model outputs a structured tool call; your code executes it |
| **Guardrail** | Check that constrains inputs, actions or outputs |
| **Human-in-the-loop** | Human approval for selected actions |
| **Memory** | Short-term (conversation/state) or long-term (stored, retrieved) information |
| **Orchestrator–workers** | Pattern where one model delegates subtasks to others |
| **ReAct** | Interleaving reasoning (thought) and acting (tool calls) with observations |
| **Workflow** | Predefined sequence of LLM and tool steps (no autonomous control flow) |

## LangChain and LangGraph

| Term | Meaning |
|---|---|
| **LCEL** | LangChain Expression Language: composing runnables with the pipe operator |
| **Runnable** | LangChain unit with `invoke`, `batch`, `stream` |
| **StateGraph** | LangGraph graph whose nodes read and update shared state |
| **Node / edge** | A step / a transition between steps |
| **Conditional edge** | Transition chosen by a router function on the state |
| **Reducer** | Function deciding how a node's update merges into state (overwrite, append, merge) |
| **Checkpointer** | Persistence for graph state across runs |

## Tooling

| Term | Meaning |
|---|---|
| **pyproject.toml** | Standard Python project/packaging configuration |
| **pytest** | Python test framework |
| **mypy** | Static type checker |
| **Virtual environment (venv)** | Isolated Python installation per project |
| **Seed** | Fixed value for reproducible randomness |
