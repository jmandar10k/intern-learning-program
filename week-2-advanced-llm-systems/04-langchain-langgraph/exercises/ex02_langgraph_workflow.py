"""Week 2 / 04 LangGraph / Exercise 2: typed state, reducers and conditional edges.

A support-ticket workflow: classify -> (refund | delivery | escalate) -> draft -> review -> END
Needs: langgraph (runs offline).
Run:  python ex02_langgraph_workflow.py
"""
from __future__ import annotations

import operator
from typing import Annotated, TypedDict

from langgraph.graph import END, START, StateGraph


class TicketState(TypedDict):
    ticket: str
    category: str
    notes: Annotated[list[str], operator.add]  # reducer: node outputs are APPENDED
    draft: str
    approved: bool
    attempts: int


def classify(state: TicketState) -> dict:
    t = state["ticket"].lower()
    category = "refund" if "refund" in t or "charged" in t else "delivery" if "late" in t else "other"
    return {"category": category, "notes": [f"classified as {category}"]}


def handle_refund(state: TicketState) -> dict:
    return {"notes": ["checked refund policy: missing items refunded within 3 business days"]}


def handle_delivery(state: TicketState) -> dict:
    return {"notes": ["checked late policy: >30 min late gives 10% credit"]}


def escalate(state: TicketState) -> dict:
    return {"notes": ["escalated to a human agent"]}


def draft_reply(state: TicketState) -> dict:
    facts = "; ".join(state["notes"][1:])
    return {"draft": f"Thanks for reaching out. {facts}.", "attempts": state.get("attempts", 0) + 1}


def review(state: TicketState) -> dict:
    ok = "policy" in state["draft"] or "human" in state["draft"]
    return {"approved": ok, "notes": [f"review attempt {state['attempts']}: {'approved' if ok else 'rejected'}"]}


def route_by_category(state: TicketState) -> str:
    return {"refund": "handle_refund", "delivery": "handle_delivery"}.get(state["category"], "escalate")


def after_review(state: TicketState) -> str:
    return END if state["approved"] or state["attempts"] >= 2 else "draft_reply"


def build():
    g = StateGraph(TicketState)
    for name, fn in [
        ("classify", classify), ("handle_refund", handle_refund), ("handle_delivery", handle_delivery),
        ("escalate", escalate), ("draft_reply", draft_reply), ("review", review),
    ]:
        g.add_node(name, fn)
    g.add_edge(START, "classify")
    g.add_conditional_edges("classify", route_by_category, ["handle_refund", "handle_delivery", "escalate"])
    for n in ["handle_refund", "handle_delivery", "escalate"]:
        g.add_edge(n, "draft_reply")
    g.add_edge("draft_reply", "review")
    g.add_conditional_edges("review", after_review, ["draft_reply", END])
    return g.compile()


def main() -> None:
    app = build()
    for ticket in [
        "I was charged but two items were missing, I want a refund",
        "My order was 45 minutes late",
        "Can you recommend a recipe?",
    ]:
        final = app.invoke({"ticket": ticket, "notes": [], "attempts": 0, "draft": "", "category": "", "approved": False})
        print(f"\nTICKET: {ticket}\n  category={final['category']} approved={final['approved']} attempts={final['attempts']}")
        for n in final["notes"]:
            print("   -", n)
        print("  reply:", final["draft"])

    print("\nstep-by-step stream for one ticket:")
    for update in app.stream({"ticket": "my order was late", "notes": [], "attempts": 0, "draft": "", "category": "", "approved": False}, stream_mode="updates"):
        print("  ", list(update.keys())[0], "->", list(update.values())[0])
    print(
        "\nYour turn:\n"
        "  1. Remove the Annotated reducer from `notes` (plain list[str]). Re-run. Which notes\n"
        "     survive and why? Would anything raise an error?\n"
        "  2. Add a 'sentiment' node that runs before classify and adds a note.\n"
        "  3. Draw the graph: print(app.get_graph().draw_mermaid())"
    )


if __name__ == "__main__":
    main()
