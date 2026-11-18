# Week 2 plan: advanced LLM systems (learn, advanced)

Purely study, same format as Week 1, with more hands-on work. Each topic has a `notes.md` and
runnable exercises; curated links are in [study-materials.md](study-materials.md).

**Objectives:** see the Week 2 section of
[00-charter/learning-objectives.md](../00-charter/learning-objectives.md).

## No API keys needed

All exercises run **offline** with deterministic stubs in [llm_stubs.py](llm_stubs.py):

- `HashEmbedder`: a bag-of-words hashing embedder (deterministic; captures word overlap, not
  meaning).
- `StubLLM`: a rule-based "LLM" that follows a few simple conventions (answers from provided
  context, emits tool calls in a fixed format).

The stubs let you focus on the **system around the model** (retrieval, prompting, tool loops,
state, evaluation), which is where most real bugs live. If you later have approved access to a
real model, the interfaces are small enough to swap in.

## Schedule

| Day | Morning (≈3 h) | Afternoon (≈3.5 h) |
|---|---|---|
| 6 | [01 LLMs and NLP](01-llms-and-nlp/notes.md): notes + core link | 01 exercises (tokenization, embeddings, prompting) |
| 7 | [02 RAG and retrieval](02-rag-and-retrieval/notes.md): notes + core link | 02 exercises (chunking, vector + hybrid search, reranking, retrieval eval) |
| 8 | [03 Agents, tool calling and workflows](03-agents-tool-calling-workflows/notes.md): notes + core link | 03 exercises (ReAct loop, function calling, guardrails) |
| 9 | [04 LangChain and LangGraph](04-langchain-langgraph/notes.md): notes + core link | 04 exercises (LCEL-style chain, LangGraph state, reducers, conditional edges) |
| 10 | [05 Evaluation and responsible GenAI](05-evaluation-and-responsible-genai/notes.md) + exercises | [Self-check quiz](self-check-quiz.md), **Week 2 check-in** |

## Running the exercises

```bash
cd week-2-advanced-llm-systems/02-rag-and-retrieval/exercises
python ex01_rag_pipeline.py
```

Topic 04 needs `langchain-core` and `langgraph` installed (see
[resources/environment-setup.md](../resources/environment-setup.md)); they run fully offline.

## Week 2 check-in (Day 10)

Focus: **depth of understanding and links between topics.** Be ready to explain, for example,
how chunking (02) affects hallucination (05), or how LangGraph state (04) implements agent memory (03).
