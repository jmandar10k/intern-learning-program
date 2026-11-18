"""Monthly sales report for an online store (books, games, music, stationery).

Produces total revenue, revenue and average order value (AOV) per region, and revenue per
category. Finance uses these numbers for regional budgets.

Run:  python main.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"


def load() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    lines = pd.read_csv(DATA / "order_lines.csv")
    customers = pd.read_csv(DATA / "customers.csv")
    products = pd.read_csv(DATA / "products.csv")
    return lines, customers, products


def clean(lines: pd.DataFrame) -> pd.DataFrame:
    lines = lines.copy()
    lines["unit_price"] = lines["unit_price"].fillna(0)
    lines["quantity"] = lines["quantity"].astype(int)
    return lines


def main() -> None:
    lines, customers, products = load()
    lines = clean(lines)

    df = lines.merge(customers[["customer_id", "region"]], on="customer_id", how="left")
    df = df.merge(products[["product_id", "category"]], on="product_id", how="left")
    df["revenue"] = df["quantity"] * df["unit_price"]

    print(f"order lines: {len(lines)}   orders: {lines['order_id'].nunique()}")
    print(f"total revenue: {df['revenue'].sum():,.2f}\n")

    by_region = df.groupby("region").agg(revenue=("revenue", "sum"), orders=("order_id", "nunique"))
    by_region["aov"] = df.groupby("region")["revenue"].mean()
    print("by region:")
    print(by_region.round(2).to_string())

    print("\nrevenue by category:")
    print(df.groupby("category")["revenue"].sum().round(2).sort_values(ascending=False).to_string())


if __name__ == "__main__":
    main()
