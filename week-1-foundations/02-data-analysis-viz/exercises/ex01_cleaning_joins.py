"""Week 1 / 02 Data analysis / Exercise 1: cleaning, joins, reconciliation.

Run:  python ex01_cleaning_joins.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from freshcart_data import make_orders, make_stores  # noqa: E402


def inspect(df: pd.DataFrame) -> None:
    print("shape:", df.shape)
    print("missing share per column:\n", df.isna().mean().round(3)[lambda s: s > 0])
    print("duplicates:", df.duplicated().sum())


def clean(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["zone"] = out["zone"].astype("category")
    # Missing distance: impute with the zone median and keep a flag (missingness may be informative).
    out["distance_missing"] = out["distance_km"].isna()
    out["distance_km"] = out.groupby("zone", observed=True)["distance_km"].transform(
        lambda s: s.fillna(s.median())
    )
    # Missing basket value: impute from items × median price per item.
    price_per_item = (out["basket_value"] / out["items"]).median()
    out["basket_value"] = out["basket_value"].fillna(out["items"] * price_per_item)
    # Outliers in items: clip to the 99th percentile (documented decision).
    cap = out["items"].quantile(0.99)
    out["items_clipped"] = out["items"] > cap
    out["items"] = out["items"].clip(upper=cap)
    return out


def main() -> None:
    raw = make_orders(n=2000)
    stores = make_stores()
    inspect(raw)

    df = clean(raw)
    joined = pd.merge(df, stores, on="store_id", how="left", validate="many_to_one", indicator=True)
    assert len(joined) == len(df), "join changed the row count"
    assert (joined["_merge"] == "both").all(), "some orders have no store"

    # Reconcile: per-zone order counts and late counts must add up to the raw totals.
    by_zone = joined.groupby("zone", observed=True).agg(orders=("order_id", "count"), late=("late", "sum"))
    assert by_zone["orders"].sum() == len(raw)
    assert by_zone["late"].sum() == raw["late"].sum()
    by_zone["late_rate"] = by_zone["late"] / by_zone["orders"]
    print("\nlate rate by zone (reconciled):\n", by_zone.round(3))

    # The NaN -> 0 trap: same data, two "cleaning" choices, different conclusions.
    wrong = raw.copy()
    wrong["distance_km"] = wrong["distance_km"].fillna(0)
    print(
        "\nmean distance, zone-median impute: "
        f"{df['distance_km'].mean():.3f} km  vs  fillna(0): {wrong['distance_km'].mean():.3f} km"
    )
    print("orders with distance 0 after fillna(0):", int((wrong["distance_km"] == 0).sum()))

    # Weighted vs unweighted average: averaging per-zone rates is NOT the overall rate.
    print(
        f"\noverall late rate {raw['late'].mean():.3f}  vs  mean of zone rates "
        f"{by_zone['late_rate'].mean():.3f}  <- not the same"
    )
    pivot = joined.pivot_table(index="zone", columns="store_size", values="late", aggfunc="mean", observed=True)
    print("\nlate rate by zone x store size:\n", pivot.round(2))
    print(
        "\nYour turn:\n"
        "  1. Build a stores table with a duplicated store_id and re-run the merge. What does\n"
        "     validate= do? What would happen without it?\n"
        "  2. Compute late rate by hour; which hours stand out? Is the group size large enough?\n"
        "  3. Replace the clip with IQR-based outlier detection and compare counts."
    )
    np.testing.assert_allclose(by_zone["orders"].sum(), 2000)


if __name__ == "__main__":
    main()
