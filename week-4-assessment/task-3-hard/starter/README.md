# Starter: offline model stubs

`llm_stubs.py` is the same module used in Week 2.

| Component | Behavior |
|---|---|
| `StubLLM().chat(messages, tools)` | Function-calling interface. Proposes a call to the tool whose description best matches the last user message (each tool at most once), then answers in text using the tool results. Deterministic. |
| `StubLLM().complete(prompt)` | Extractive answers from a `Context:` block; `Summarize:` returns the first sentences. |
| `ToolCall`, `ChatResponse`, `tool_result_message` | Data structures for the tool-calling loop. |

The stub is intentionally simple. It is **not** smart enough to apply the expense policy, and
you should not need it to be: decide which parts of this task need a model at all, and explain
that choice in your design note. LangGraph (installed in the program environment) runs fully
offline.
