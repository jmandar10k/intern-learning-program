"""Week 2 / 03 Agents / Exercise 1: a function-calling agent loop with guardrails.

Run:  python ex01_tool_calling_agent.py
"""
from __future__ import annotations

import ast
import operator
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from llm_stubs import StubLLM, ToolCall, tool_result_message  # noqa: E402

ORDERS = {"FC-1001": {"status": "out for delivery", "eta_min": 12}, "FC-1002": {"status": "delivered", "eta_min": 0}}

# --- Tools ------------------------------------------------------------------------------

_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}


def calculator(expression: str) -> float:
    """Safe arithmetic: parses the expression, never eval()s it."""

    def ev(node: ast.AST) -> float:
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return float(node.value)
        if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](ev(node.left), ev(node.right))
        raise ValueError("unsupported expression")

    return ev(ast.parse(expression, mode="eval").body)


def order_status(order_id: str) -> dict:
    if order_id not in ORDERS:
        raise KeyError(f"unknown order {order_id}")
    return ORDERS[order_id]


def issue_refund(amount: float) -> dict:
    return {"refunded": amount, "status": "ok"}


TOOLS: dict[str, dict[str, Any]] = {
    "calculator": {
        "fn": calculator,
        "description": "calculate arithmetic expression numbers sum total multiply",
        "parameters": {"expression": "string"},
    },
    "order_status": {
        "fn": order_status,
        "description": "look up order status and eta for an order id",
        "parameters": {"order_id": "string"},
    },
    "issue_refund": {
        "fn": issue_refund,
        "description": "issue refund amount money back to customer",
        "parameters": {"amount": "number"},
        "requires_approval_above": 50.0,
    },
}


def human_approves(call: ToolCall) -> bool:
    print(f"    [guardrail] human approval requested for {call.name}({call.arguments}) -> DENIED (demo)")
    return False


def execute(call: ToolCall, allowed: set[str], approve: Callable[[ToolCall], bool]) -> Any:
    if call.name not in allowed:
        return {"error": f"tool {call.name!r} not allowed for this task"}
    spec = TOOLS[call.name]
    limit = spec.get("requires_approval_above")
    if limit is not None and float(call.arguments.get("amount", 0)) > limit and not approve(call):
        return {"error": "action needs human approval and was not approved"}
    try:
        return {"result": spec["fn"](**call.arguments)}
    except Exception as exc:  # return errors to the model instead of crashing
        return {"error": f"{type(exc).__name__}: {exc}"}


def run_agent(question: str, allowed: set[str], max_steps: int = 5) -> str:
    llm = StubLLM()
    tool_specs = [{"name": n, "description": TOOLS[n]["description"], "parameters": TOOLS[n]["parameters"]} for n in allowed]
    messages: list[dict] = [{"role": "user", "content": question}]
    print(f"\nUSER: {question}")
    for step in range(1, max_steps + 1):
        response = llm.chat(messages, tools=tool_specs)
        if not response.tool_calls:
            print(f"  step {step}: FINAL -> {response.content}")
            return response.content
        for call in response.tool_calls:
            result = execute(call, allowed, human_approves)
            print(f"  step {step}: CALL {call.name}({call.arguments}) -> {result}")
            messages.append({"role": "assistant", "content": "", "tool_calls": [call]})
            messages.append(tool_result_message(call, result))  # the result MUST go back to the model
    print("  stopped: max steps reached")
    return "Stopped without a final answer."


def main() -> None:
    run_agent("What is the status of order FC-1001?", allowed={"order_status", "calculator"})
    run_agent("Calculate the total of 12.5 * 3 + 4", allowed={"calculator"})
    run_agent("What is the status and eta of order FC-9999?", allowed={"order_status"})
    run_agent("Please issue a refund of 80 money back to customer", allowed={"issue_refund"})
    run_agent("Please issue a refund of 80 money back to customer", allowed={"order_status"})
    print(
        "\nYour turn:\n"
        "  1. Comment out the line that appends the tool result. What does the agent answer now,\n"
        "     and how would you detect this bug from the trace alone?\n"
        "  2. Add a tool `delivery_fee(basket_value)` and a question that needs it AND the\n"
        "     calculator. Confirm both tools are called before the final answer.\n"
        "  3. Add a check that the final answer only mentions numbers that appear in tool results."
    )


if __name__ == "__main__":
    main()
