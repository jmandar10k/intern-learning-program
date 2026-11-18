# Week 2 study materials

**Rule:** each topic has **1 core** resource (do it) and **up to 2 optional** deep dives. Level
for this week: **advanced**. Read the topic's `notes.md` first.

All links were found and checked by web search on **2026-11-18**. See
[resources/link-verification-log.md](../resources/link-verification-log.md). Papers are linked
from their official source (arXiv), never copied into the repo.

## 01 LLMs and NLP

| Role | Resource | Level | Time | Watch/read this part | Why |
|---|---|---|---|---|---|
| Core | [Hugging Face: LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) | Advanced | ≈3 h | Chapter 1 (Transformer models) and Chapter 2 (tokenizers, models); skim Chapter 6 (tokenizers library) | Practical, current, free; afterwards you can explain tokenization, encoder/decoder models and how a model turns text into vectors. |
| Optional | [Jay Alammar: The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | Advanced | ≈1 h | Whole post | The clearest visual explanation of self-attention and multi-head attention. |
| Optional | [Vaswani et al. (2017): Attention Is All You Need (arXiv)](https://arxiv.org/abs/1706.03762) | Advanced | ≈1.5 h | Sections 1–3 and Figure 1; skip training details | The landmark paper; read after the Illustrated Transformer. |

## 02 RAG and retrieval

| Role | Resource | Level | Time | Watch/read this part | Why |
|---|---|---|---|---|---|
| Core | [LangChain docs: Retrieval](https://docs.langchain.com/oss/python/langchain/retrieval) | Advanced | ≈1.5 h | "Building blocks" (loaders, text splitters, embeddings, vector stores, retrievers) and the RAG architectures section | Maps every RAG component to code; afterwards you can design a retrieve-then-generate pipeline. |
| Optional | [DeepLearning.AI: Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/) | Advanced | ≈2 h | All video lessons; the RAG triad lesson is the priority | Advanced retrieval (sentence-window, auto-merging) and the RAG triad for evaluation. |
| Optional | [Lewis et al. (2020): Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (arXiv)](https://arxiv.org/abs/2005.11401) | Advanced | ≈1 h | Abstract, Sections 1–2 | The paper that named RAG; useful context for why retrieval reduces hallucination. |

## 03 Agents, tool calling and workflows

| Role | Resource | Level | Time | Watch/read this part | Why |
|---|---|---|---|---|---|
| Core | [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) | Advanced | ≈1 h | Whole post incl. appendix on tool design | Afterwards you can tell workflows from agents, pick a pattern (chaining, routing, orchestrator-workers, evaluator-optimizer) and justify when not to build an agent. |
| Optional | [Lilian Weng: LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) | Advanced | ≈1.5 h | "Agent System Overview", "Planning" (incl. ReAct, Reflexion), "Memory", "Tool Use" | Survey of planning, memory and tool-use techniques with references. |

## 04 LangChain and LangGraph

| Role | Resource | Level | Time | Watch/read this part | Why |
|---|---|---|---|---|---|
| Core | [LangGraph docs: Quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) | Advanced | ≈1.5 h | Graph API version | Afterwards you can define state, nodes, edges and conditional edges and run a graph. |
| Optional | [LangGraph docs: Graph API how-to](https://docs.langchain.com/oss/python/langgraph/use-graph-api) | Advanced | ≈1 h | State and reducers; control flow (conditional edges) | Reducers (`operator.add`, `add_messages`) are a common source of silent state bugs. |
| Optional | [DeepLearning.AI: AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/) | Advanced | ≈1.75 h | Lessons on building an agent from scratch and with LangGraph; persistence | Builds an agent by hand first, then in LangGraph. Some code may need updates for current versions. |

## 05 Evaluation and responsible GenAI

| Role | Resource | Level | Time | Watch/read this part | Why |
|---|---|---|---|---|---|
| Core | [Hugging Face (OpenEvals): The LLM Evaluation Guidebook](https://huggingface.co/spaces/OpenEvals/evaluation-guidebook) | Advanced | ≈2 h | Basics, automatic benchmarks, LLM-as-a-judge, troubleshooting | Practical guidance from the team behind the Open LLM Leaderboard; afterwards you can design an eval and know its blind spots. |
| Optional | [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/) | Advanced | ≈1 h | LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM06 Excessive Agency, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation | The standard checklist of LLM application risks with mitigations. |
