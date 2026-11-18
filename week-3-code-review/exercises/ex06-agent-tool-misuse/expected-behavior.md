# ex06: expected behavior

**Goal of the script:** after the run, every item has at least its target stock, and the
agent's answers report what actually happened.

## What correct output looks like

| Task | Tools called | Agent reports |
|---|---|---|
| T1 laptop stand ≥ 20 (stock 6) | check_stock, place_order | ordered 14 units, citing a PO number |
| T2 wireless mouse ≥ 20 (stock 15) | check_stock, place_order | ordered 5 units, citing a PO number |
| T3 usb-c cable ≥ 30 (stock 42) | check_stock | 42 in stock, no order needed |
| T4 hdmi adapter ≥ 10 (stock 0) | check_stock, place_order | ordered 10 units, citing a PO number |

Inventory after the run:

```
{'usb-c cable': 42, 'laptop stand': 20, 'wireless mouse': 20, 'hdmi adapter': 10, 'webcam': 25}
```

## Sanity checks you can run

- Compare "inventory before" and "inventory after".
- For each claim in an agent answer, find the tool result that supports it.
- What exactly does the model see after each tool call?
