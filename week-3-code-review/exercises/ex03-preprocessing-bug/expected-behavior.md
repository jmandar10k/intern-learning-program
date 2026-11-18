# ex03: expected behavior

**Goal of the script:** a sales report that finance can reconcile with the raw order lines.

## What correct output looks like

- 1,003 order lines, 400 orders.
- **Total revenue = 61,697.49**: every line counted once; lines with a missing price valued at
  the product's list price (94 such lines; see [data/README.md](data/README.md)).
- The `orders` column summed over regions equals **400**, and revenue summed over regions equals
  total revenue.
- **AOV (average order value)** = revenue per order. On this data it is roughly **145–165** in
  every region:

| region | revenue | orders | aov |
|---|---|---|---|
| east | 14,855.14 | 96 | 154.74 |
| north | 15,231.12 | 105 | 145.06 |
| south | 13,561.92 | 83 | 163.40 |
| west | 18,049.31 | 116 | 155.60 |

## Sanity checks you can run

- Row count before and after each join.
- Sum of the per-region numbers vs the overall numbers.
- What does "average order value" mean, and what does the code actually average?
