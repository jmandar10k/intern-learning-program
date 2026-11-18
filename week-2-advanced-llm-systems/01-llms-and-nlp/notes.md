# 01 LLMs and NLP

Level: advanced. Time: ≈ 1 day.
Links: [study-materials.md](../study-materials.md#01-llms-and-nlp).

## After this topic you can

- Explain the transformer at the level of tokens → embeddings → attention layers → next-token
  distribution, and say what that implies for model behavior.
- Explain subword tokenization (BPE) and its practical consequences (cost, context limits, odd
  behavior on numbers and rare words).
- Use embeddings for similarity, and explain cosine similarity and normalization.
- Write prompts that are specific, structured and testable (system instructions, few-shot
  examples, output format, delimiters).
- Explain sampling (temperature, top-p) and when to use temperature 0.
- Say when to prompt, when to use RAG and when to fine-tune.

## Concepts

### Transformers in one page

1. Text → **tokens** (subword units) → integer ids.
2. Ids → **embedding vectors** + positional information.
3. A stack of **transformer blocks**: multi-head **self-attention** (each token builds its
   representation from a weighted mix of other tokens; weights from query·key similarity) and a
   feed-forward network, with residual connections and layer norm.
4. The final layer gives a **probability distribution over the next token**. Generation
   repeats: sample a token, append, run again.

Families: **encoder-only** (BERT-like: classification, embeddings), **decoder-only** (GPT-like:
generation), **encoder-decoder** (T5-like: translation, summarization).

Implications: the model predicts plausible continuations, not verified facts → hallucination.
It only "knows" its training data and the **context window** → RAG. Cost and latency scale with
tokens.

### Tokenization

- **BPE** starts from characters and repeatedly merges the most frequent adjacent pair.
  Common words become one token; rare words split into pieces.
- Consequences: token counts ≠ word counts; numbers split oddly (arithmetic is unreliable);
  non-English text often costs more tokens; prompts have hard token limits.

### Embeddings

- A dense vector representing meaning; similar texts → nearby vectors.
- **Cosine similarity** = dot product of L2-normalized vectors. If vectors are normalized,
  ranking by cosine, dot product and L2 distance is equivalent; if not, they differ.
- Sentence embeddings (bi-encoders) are used for retrieval; cross-encoders score a pair jointly
  and are used for reranking.
- Our offline `HashEmbedder` only captures word overlap. A real embedding model would match
  "refund" with "money back".

### Prompting

- Be explicit: role, task, constraints, output format (e.g. JSON schema), what to do when unsure
  ("say you don't know").
- Separate instructions from data with delimiters; never let user/retrieved text masquerade as
  instructions (prompt injection, topic 05).
- **Few-shot** examples steer format and edge cases. **Chain-of-thought** / "think step by step"
  helps reasoning tasks; ask for the reasoning separately from the final answer.
- Prompts are code: version them, template them, test them. A template variable that is never
  substituted produces fluent output that ignores the input.

### Sampling

- **Temperature** rescales logits: `softmax(logits / T)`. T→0 = greedy and deterministic; higher T =
  more diverse and more errors. Use T=0 (or low) for extraction, classification, tool calls and
  evaluation; higher for brainstorming.
- **Top-p** samples from the smallest set of tokens with cumulative probability ≥ p.

### Prompt vs RAG vs fine-tune

| Need | Use |
|---|---|
| Different behavior/format, small task | Prompting (+ few-shot) |
| Up-to-date or private knowledge, citations | RAG |
| Consistent style/format at scale, a narrow task, smaller/cheaper model | Fine-tuning (e.g. LoRA / parameter-efficient methods) |
| New knowledge | Usually RAG, not fine-tuning |

## Exercises

| File | What it shows |
|---|---|
| `exercises/ex01_tokens_embeddings.py` | A tiny BPE trainer; cosine vs dot vs L2 with and without normalization; the limits of a hashing embedder |
| `exercises/ex02_prompting_sampling.py` | Prompt templates, few-shot, "I don't know" behavior, temperature as softmax scaling, determinism |

## Common mistakes

- Treating fluent output as correct.
- Comparing unnormalized embeddings with dot product and calling it cosine.
- Using high temperature for extraction or evaluation.
- Fine-tuning to add facts that change weekly.
