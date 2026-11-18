# Data dictionary

## order_lines.csv

One row per product line in an order.

| Column | Meaning |
|---|---|
| `order_id` | Order (an order has 1–4 lines) |
| `customer_id` | Customer who placed the order |
| `product_id` | Product |
| `quantity` | Units |
| `unit_price` | Price charged per unit. Blank for lines recorded during a point-of-sale outage; those sales did happen, at the product's list price |

## customers.csv

Export from the CRM.

| Column | Meaning |
|---|---|
| `customer_id` | Customer |
| `region` | Region |
| `is_current` | 1 for the customer's current record. The CRM keeps the previous record (0) when a customer moves region |

## products.csv

| Column | Meaning |
|---|---|
| `product_id` | Product |
| `category` | `books`, `games`, `music`, `stationery` |
| `list_price` | List price |
