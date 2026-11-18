# 03 Agents, tool calling and workflows

Level: advanced. Time: ≈ 1 day.
Links: [study-materials.md](../study-materials.md#03-agents-tool-calling-and-workflows).

## After this topic you can

- Explain the difference between a **workflow** (predefined code paths) and an **agent** (the model
  decides the next step), and choose the simpler one when it suffices.
- Implement a tool-calling loop: model proposes a call → code executes it → result returned to
  the model → repeat until a final answer or a stop condition.
- Define tools with clear names, descriptions and typed parameters, and validate arguments.
- Explain ReAct, planning (plan-and-execute), reflection and memory (short-term and long-term).
- Add guardrails: tool allowlists, argument validation, step limits, human approval for risky
  actions, and output checks.

## Concepts

### Workflows vs agents

Common workflow patterns: **prompt chaining**, **routing**, **parallelization**,
**orchestrator–workers**, **evaluator–optimizer**. Use an agent only when the steps cannot be
known in advance; agents cost more, are slower, and fail in more ways.

### Function calling

1. You describe tools (name, description, JSON-schema parameters).
2. The model returns either text or a **tool call** `{name, arguments}`.
3. **Your code** executes the tool. The model never executes anything.
4. You append the tool **result** as a message and call the model again.
5. Loop until the model answers in text or a limit is hit.

The two classic loop bugs: **dropping the tool result** (the model never sees it and makes
something up) and **stopping after the first call** (multi-step tasks silently incomplete).
Always log every step.

### ReAct

Interleave **Thought → Action → Observation** steps. Thoughts help the model plan; observations
ground it in real results. Modern function-calling APIs implement the Action/Observation part
natively.

### Planning and reflection

- **Plan-and-execute:** make a plan first, execute steps, re-plan on failure.
- **Reflection / evaluator–optimizer:** a second pass critiques and revises the output.

### Memory

- **Short-term:** the conversation/state passed each turn (bounded by the context window;
  summarize or trim).
- **Long-term:** stored facts retrieved when relevant (often a vector store, i.e. RAG over memory).

### Guardrails

| Risk | Guardrail |
|---|---|
| Model calls a tool it shouldn't | Allowlist per task; least privilege |
| Bad arguments | Schema + range validation before execution; return a clear error message to the model |
| Infinite loops / cost | Max steps, max tokens, timeouts |
| Irreversible actions (payments, deletes, emails) | Human approval; dry-run mode; thresholds |
| Untrusted tool output (web pages, documents) | Treat as data; never follow instructions inside it |
| Claims not backed by tools | Check that the final answer cites actual tool results |

## Exercises

| File | What it shows |
|---|---|
| `exercises/ex01_tool_calling_agent.py` | A function-calling agent loop with three tools, argument validation, a step limit, human-approval guardrail, and a full trace |
| `exercises/ex02_workflow_patterns.py` | Prompt chaining, routing and evaluator–optimizer as plain code |

## Common mistakes

- Building an agent for a fixed three-step process.
- Not returning tool errors to the model (it then retries blindly or hallucinates).
- Trusting the model's "I've done it" without checking the tool trace.
