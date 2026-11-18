"""Week 1 / 02 Data analysis / Exercise 2: EDA and visualization.

Run:  python ex02_eda_plots.py      (plots are written to ./plots/)
"""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # no display needed
import matplotlib.pyplot as plt  # noqa: E402
import seaborn as sns  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from freshcart_data import make_orders  # noqa: E402

OUT = Path(__file__).parent / "plots"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    df = make_orders(n=2000, with_noise=False)
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(df["delivery_minutes"], bins=40, ax=ax)
    ax.axvline(45, color="red", linestyle="--", label="late threshold (45 min)")
    ax.set(title="Delivery time is right-skewed; ~24% exceed 45 min", xlabel="minutes", ylabel="orders")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "01_delivery_minutes_hist.png", dpi=120)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=df, x="zone", y="late", errorbar=("ci", 95), ax=ax)
    ax.set(title="Late rate by zone (95% CI)", ylabel="late rate")
    fig.tight_layout()
    fig.savefig(OUT / "02_late_rate_by_zone.png", dpi=120)

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=df, x="distance_km", y="delivery_minutes", hue="rain", alpha=0.4, s=12, ax=ax)
    ax.set(title="Delivery time grows with distance; rain shifts it up", xlabel="distance (km)", ylabel="minutes")
    fig.tight_layout()
    fig.savefig(OUT / "03_distance_vs_minutes.png", dpi=120)

    pivot = df.pivot_table(index="zone", columns="hour", values="late", aggfunc="mean")
    fig, ax = plt.subplots(figsize=(9, 3.5))
    sns.heatmap(pivot, cmap="Reds", vmin=0, vmax=1, ax=ax)
    ax.set(title="Late rate by zone and hour: evening peak in west and south")
    fig.tight_layout()
    fig.savefig(OUT / "04_zone_hour_heatmap.png", dpi=120)
    plt.close("all")

    print("Saved plots:", sorted(p.name for p in OUT.glob("*.png")))
    print("late rate:", round(df["late"].mean(), 3))
    print(
        "\nYour turn:\n"
        "  1. Write three findings and one open question from these plots in your progress log.\n"
        "  2. Add a plot of late rate vs courier_load. Which plot type did you choose and why?\n"
        "  3. Each heatmap cell has how many orders? Add annotations or mask cells with < 20 orders."
    )


if __name__ == "__main__":
    main()
