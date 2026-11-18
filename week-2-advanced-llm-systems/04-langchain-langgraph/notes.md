# 04 LangChain and LangGraph

Level: advanced. Time: ≈ 1 day.
Links: [study-materials.md](../study-materials.md#04-langchain-and-langgraph).

Installed versions used to build this program: `langchain-core 1.2.x`, `langgraph 1.0.x`.
Both run fully offline in these exercises; no model provider package or API key is needed.

## After this topic you can

- Compose chains with LCEL (`prompt | model | parser`), `RunnableParallel`,
  `RunnablePassthrough` and `RunnableLambda`; use `invoke`, `batch` and `stream`.
- Use LangChain building blocks: prompt templates, documents, retrievers, tools, output parsers.
- Build a LangGraph `StateGraph`: typed state, nodes, edges, conditional edges, loops and `END`.
- Explain **reducers** and how node outputs are merged into state.
- Debug a graph by streaming per-node updates.

## Concepts

### LangChain (LCEL)

- Everything is a **Runnable** with `invoke` / `batch` / `stream`.
- `|` pipes the output of one runnable into the next.
- `RunnableParallel({...})` builds a dict from several runnables on the same input — the usual way
  to produce `{"context": ..., "question": ...}` for a RAG prompt.
- `PromptTemplate.from_template("... {question}")` infers `input_variables`. A missing variable
  raises; a variable that is present but comes from the wrong field does not. Check what you pass.
- Retrievers return `Document`s (`page_content` + `metadata`). Keep `metadata["source"]` for
  citations.
- Tools: a function + name + description + argument schema (`@tool` decorator). The model chooses;
  your code executes.

### LangGraph

- A **graph of nodes** that read and update a shared **state** (`TypedDict` or Pydantic model).
- A node returns a **partial update** (a dict with only the keys it changes).
- **Reducers** decide how an update is merged:
  - no reducer → the new value **overwrites** the old one;
  - `Annotated[list, operator.add]` → lists are **concatenated**;
  - `Annotated[list, add_messages]` → chat messages are appended/updated by id.
  Choosing the wrong one silently loses or duplicates data.
- **Edges**: `add_edge(a, b)` always goes a → b. `add_conditional_edges(a, router, [targets])`
  calls `router(state)` and goes to the returned node name. Loops are edges back to an earlier node
  with a stop condition.
- `START` and `END` mark entry and exit. `compile()` validates the graph.
- Persistence (checkpointers) gives memory across invocations and human-in-the-loop pauses.

### When to use which

| Need | Use |
|---|---|
| Linear prompt → model → parse, or simple RAG | LCEL chain |
| Branching, loops, retries, multi-step agents, human approval, persistent state | LangGraph |
| A fixed 2–3 step process | Plain Python may be simplest |

### Debugging

- `app.stream(input, stream_mode="updates")` shows what each node returned.
- `app.get_graph().draw_mermaid()` prints the graph structure.
- Assert invariants after a run (e.g. "every ticket has a classification note and a review note").

## Exercises

| File | What it shows |
|---|---|
| `exercises/ex01_langchain_chain.py` | LCEL RAG chain with a custom retriever and a stub model wrapped in `RunnableLambda` |
| `exercises/ex02_langgraph_workflow.py` | `StateGraph` with a list reducer, routing via conditional edges, a review loop, streaming |

## Common mistakes

- Forgetting a reducer on a list that several nodes append to.
- A router returning a name that is not in the target list, or a branch that always goes the same way.
- Loops without a stop condition (LangGraph enforces a recursion limit; hitting it is an error, but
  a loop that exits too early is silent).
