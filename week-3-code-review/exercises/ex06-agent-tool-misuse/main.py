"""Office-supplies restocking agent.

For each task ("make sure we have at least N units of ITEM") the agent may call two tools:
  check_stock(item)            -> current quantity
  place_order(item, quantity)  -> purchase order
The model is a deterministic offline stub that decides the next action from the task and
the tool results it has seen so far (no API key needed).

Run:  python main.py
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

DATA = Path(__file__).parent / "data"
MAX_STEPS = 5

INVENTORY: dict[str, int] = json.loads((DATA / "inventory.json").read_text(encoding="utf-8"))
_po = itertools.count(1)


# ---- tools -----------------------------------------------------------------------------

def check_stock(item: str) -> dict:
    return {"item": item, "quantity": INVENTORY[item]}


def place_order(item: str, quantity: int) -> dict:
    INVENTORY[item] += quantity  # simulated instant delivery
    return {"order_id": f"PO-{next(_po):03d}", "item": item, "quantity": quantity, "status": "placed"}


TOOLS = {"check_stock": check_stock, "place_order": place_order}


# ---- model (stub) ------------------------------------------------------------------------

class StubAgentModel:
    """Chooses the next action from the task and the tool history."""

    def next_action(self, task: dict, history: list[dict], tools_available: bool) -> dict:
        item, target = task["item"], task["target"]
        stock = next((h for h in history if h["tool"] == "check_stock"), None)
        order = next((h for h in history if h["tool"] == "place_order"), None)

        if not tools_available:
            return {"type": "final", "text": f"I checked the {item} stock and took the necessary action. Task complete."}
        if stock is None:
            return {"type": "tool_call", "tool": "check_stock", "args": {"item": item}}
        result = stock.get("result") or {}
        if "quantity" not in result:
            return {"type": "final", "text": f"Stock of {item} looks sufficient; no order needed. Task complete."}
        if result["quantity"] >= target:
            return {"type": "final", "text": f"{item}: {result['quantity']} in stock (target {target}); no order needed."}
        if order is None:
            return {"type": "tool_call", "tool": "place_order", "args": {"item": item, "quantity": target - result["quantity"]}}
        o = order["result"]
        return {"type": "final", "text": f"Ordered {o['quantity']} x {item} ({o['order_id']}); stock will be {target}."}


# ---- agent loop --------------------------------------------------------------------------

def run_agent(task: dict, model: StubAgentModel) -> tuple[str, list[dict]]:
    history: list[dict] = []
    action = model.next_action(task, history, tools_available=True)
    steps = 0
    while action["type"] == "tool_call" and steps < MAX_STEPS:
        result = TOOLS[action["tool"]](**action["args"])
        history.append({"tool": action["tool"], "args": action["args"], "result": action.get("result")})
        steps += 1
        action = model.next_action(task, history, tools_available=False)
    return action["text"], history


def main() -> None:
    tasks = json.loads((DATA / "tasks.json").read_text(encoding="utf-8"))
    model = StubAgentModel()
    print("inventory before:", INVENTORY, "\n")
    for task in tasks:
        answer, history = run_agent(task, model)
        print(f"[{task['id']}] ensure >= {task['target']} x {task['item']}")
        print(f"     tools called: {[h['tool'] for h in history]}")
        print(f"     agent: {answer}\n")
    print("inventory after: ", INVENTORY)


if __name__ == "__main__":
    main()
