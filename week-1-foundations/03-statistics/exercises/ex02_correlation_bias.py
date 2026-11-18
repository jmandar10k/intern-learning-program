"""Week 1 / 03 Statistics / Exercise 2: correlation, confounding, Simpson's paradox.

Run:  python ex02_correlation_bias.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from freshcart_data import make_orders  # noqa: E402


def main() -> None:
    df = make_orders(n=2000, with_noise=False)

    r, _ = stats.pearsonr(df["distance_km"], df["delivery_minutes"])
    rho, _ = stats.spearmanr(df["distance_km"], df["delivery_minutes"])
    print(f"distance vs minutes: Pearson r={r:.3f}, Spearman rho={rho:.3f}")

    # One extreme outlier can move Pearson a lot, Spearman much less.
    x = df["distance_km"].to_numpy()[:100].copy()
    y = df["delivery_minutes"].to_numpy()[:100].copy()
    x2, y2 = np.append(x, 60.0), np.append(y, 5.0)
    print(
        f"first 100 rows: Pearson {stats.pearsonr(x, y)[0]:.3f} -> with one outlier {stats.pearsonr(x2, y2)[0]:.3f}; "
        f"Spearman {stats.spearmanr(x, y)[0]:.3f} -> {stats.spearmanr(x2, y2)[0]:.3f}"
    )

    # Simpson's paradox with a confounder (synthetic, built to show the effect).
    # Two couriers, two kinds of route. Courier B takes mostly hard routes.
    rows = (
        [("A", "easy", 1)] * 10 + [("A", "easy", 0)] * 90
        + [("A", "hard", 1)] * 8 + [("A", "hard", 0)] * 12
        + [("B", "easy", 1)] * 1 + [("B", "easy", 0)] * 19
        + [("B", "hard", 1)] * 30 + [("B", "hard", 0)] * 70
    )
    s = pd.DataFrame(rows, columns=["courier", "route", "late"])
    print("\nSimpson's paradox:")
    print("late rate by courier (pooled):\n", s.groupby("courier")["late"].mean().round(3))
    print("late rate by courier within route type:\n", s.pivot_table(index="route", columns="courier", values="late").round(3))
    print("-> B looks worse pooled, but is better on BOTH easy and hard routes. Route type confounds.")

    print(
        "\nYour turn:\n"
        "  1. Compute the correlation between courier_load and delivery_minutes overall and\n"
        "     within peak / off-peak hours separately. What does that tell you?\n"
        "  2. List two biases that could affect a real version of this dataset and how you\n"
        "     would detect them."
    )


if __name__ == "__main__":
    main()
