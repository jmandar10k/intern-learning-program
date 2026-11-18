"""Week 1 / 03 Statistics / Exercise 1: inference on the late rate.

Question: are orders more likely to be late when it rains?
Run:  python ex01_inference.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from freshcart_data import make_orders  # noqa: E402

rng = np.random.default_rng(0)


def two_proportion_ztest(x1: int, n1: int, x2: int, n2: int) -> tuple[float, float]:
    p1, p2 = x1 / n1, x2 / n2
    p = (x1 + x2) / (n1 + n2)
    se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    z = (p1 - p2) / se
    return z, 2 * (1 - stats.norm.cdf(abs(z)))


def permutation_test(a: np.ndarray, b: np.ndarray, n_perm: int = 5000) -> float:
    observed = a.mean() - b.mean()
    pooled = np.concatenate([a, b])
    count = 0
    for _ in range(n_perm):
        rng.shuffle(pooled)
        diff = pooled[: len(a)].mean() - pooled[len(a):].mean()
        count += abs(diff) >= abs(observed)
    return (count + 1) / (n_perm + 1)


def bootstrap_ci(a: np.ndarray, b: np.ndarray, n_boot: int = 5000) -> tuple[float, float]:
    diffs = [rng.choice(a, len(a)).mean() - rng.choice(b, len(b)).mean() for _ in range(n_boot)]
    return tuple(np.percentile(diffs, [2.5, 97.5]))  # type: ignore[return-value]


def main() -> None:
    df = make_orders(n=2000, with_noise=False)
    rain = df.loc[df["rain"], "late"].to_numpy()
    dry = df.loc[~df["rain"], "late"].to_numpy()
    print(f"late rate rain={rain.mean():.3f} (n={len(rain)})  dry={dry.mean():.3f} (n={len(dry)})")
    print(f"effect size (difference): {rain.mean() - dry.mean():+.3f}")

    z, p = two_proportion_ztest(rain.sum(), len(rain), dry.sum(), len(dry))
    print(f"two-proportion z-test: z={z:.2f}, p={p:.2e}")
    table = [[rain.sum(), len(rain) - rain.sum()], [dry.sum(), len(dry) - dry.sum()]]
    chi2, p_chi, *_ = stats.chi2_contingency(table)
    print(f"chi-square: chi2={chi2:.2f}, p={p_chi:.2e}")
    print(f"permutation test p ~ {permutation_test(rain, dry):.4f}")
    lo, hi = bootstrap_ci(rain, dry)
    print(f"bootstrap 95% CI of the difference: [{lo:+.3f}, {hi:+.3f}]")

    # CLT: means of a skewed variable are approximately normal.
    minutes = df["delivery_minutes"].to_numpy()
    means = np.array([rng.choice(minutes, 50).mean() for _ in range(3000)])
    print(
        f"\nCLT: skew of raw minutes={stats.skew(minutes):.2f}, skew of sample means (n=50)="
        f"{stats.skew(means):.2f}; SE observed={means.std():.2f} vs sigma/sqrt(n)={minutes.std() / np.sqrt(50):.2f}"
    )

    # Multiple comparisons: test 20 random "features" with no real effect.
    false_hits = 0
    for _ in range(20):
        noise = rng.random(len(df)) < 0.5
        _, p_noise = two_proportion_ztest(
            df.loc[noise, "late"].sum(), noise.sum(), df.loc[~noise, "late"].sum(), (~noise).sum()
        )
        false_hits += p_noise < 0.05
    print(f"\n20 tests on pure noise -> {false_hits} 'significant' at 0.05 (expected ~1)")
    print(
        "\nYour turn:\n"
        "  1. Is the late rate different on weekends (weekday >= 5)? Report effect + CI + p.\n"
        "  2. Use Welch's t-test (stats.ttest_ind(equal_var=False)) on delivery_minutes rain vs dry.\n"
        "  3. Re-run the noise test with Bonferroni correction (alpha / 20). How many hits now?"
    )


if __name__ == "__main__":
    main()
