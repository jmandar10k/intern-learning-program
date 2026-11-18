"""Synthetic FreshCart data generator shared by the Week 1 exercises.

Deterministic (fixed seed), offline, small. See reference-problem-statement.md.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

ZONES = ["north", "south", "east", "west"]


def make_orders(n: int = 2000, seed: int = 7, with_noise: bool = True) -> pd.DataFrame:
    """Return a DataFrame of synthetic FreshCart orders.

    with_noise=True injects missing values and a few outliers for cleaning practice.
    """
    rng = np.random.default_rng(seed)
    zone = rng.choice(ZONES, size=n, p=[0.3, 0.25, 0.25, 0.2])
    store_id = rng.integers(1, 9, size=n)
    hour = rng.integers(8, 22, size=n)
    weekday = rng.integers(0, 7, size=n)
    items = rng.poisson(12, size=n) + 1
    basket_value = np.round(items * rng.normal(4.5, 1.0, size=n).clip(1.5), 2)
    zone_dist = {"north": 3.0, "south": 4.5, "east": 2.5, "west": 5.5}
    distance_km = np.round(
        np.array([zone_dist[z] for z in zone]) * rng.lognormal(0, 0.35, size=n), 2
    )
    peak = ((hour >= 17) & (hour <= 19)).astype(int)
    courier_load = rng.poisson(1.0 + 1.5 * peak)
    rain = rng.random(n) < 0.22

    minutes = (
        12
        + 4.2 * distance_km
        + 3.0 * courier_load
        + 6.0 * rain
        + 0.25 * items
        + 4.0 * peak
        + rng.normal(0, 5, size=n)
    )
    delivery_minutes = np.round(minutes.clip(8), 1)
    late = (delivery_minutes > 45).astype(int)

    df = pd.DataFrame(
        {
            "order_id": np.arange(1, n + 1),
            "zone": zone,
            "store_id": store_id,
            "hour": hour,
            "weekday": weekday,
            "items": items,
            "basket_value": basket_value,
            "distance_km": distance_km,
            "courier_load": courier_load,
            "rain": rain,
            "delivery_minutes": delivery_minutes,
            "late": late,
        }
    )
    if with_noise:
        miss = rng.random(n) < 0.03
        df.loc[miss, "distance_km"] = np.nan
        miss2 = rng.random(n) < 0.02
        df.loc[miss2, "basket_value"] = np.nan
        outliers = rng.choice(n, size=5, replace=False)
        df.loc[outliers, "items"] = df.loc[outliers, "items"] * 20
    return df


def make_stores(seed: int = 7) -> pd.DataFrame:
    """Store metadata used for join exercises."""
    rng = np.random.default_rng(seed + 1)
    return pd.DataFrame(
        {
            "store_id": np.arange(1, 9),
            "store_name": [f"Store-{i}" for i in range(1, 9)],
            "store_size": rng.choice(["small", "medium", "large"], size=8),
            "opened_year": rng.integers(2015, 2025, size=8),
        }
    )


if __name__ == "__main__":
    print(make_orders().head())
    print(make_stores())
