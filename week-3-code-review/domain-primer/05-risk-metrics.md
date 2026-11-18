# 05 Risk metrics

Return alone is half the story. Two strategies with 10% CAGR are not equal if one fell 50% on the
way.

## Volatility

The standard deviation of returns. Annualize daily volatility with the square root of time
(assuming roughly independent returns):

```
σ_annual = σ_daily × √252
```

**Example.** Daily σ = 1% → annual σ ≈ 1% × 15.87 = **15.9%**.

## Sharpe ratio

Excess return per unit of total volatility:

```
Sharpe = (R_p − R_f) / σ_p        (all annualized)
```

**Example.** Annual return 12%, risk-free rate 4%, volatility 16% → (12 − 4)/16 = **0.50**.

Notes: compute from **periodic** excess returns and annualize (multiply the daily Sharpe by √252).
Sharpe treats upside and downside volatility the same and assumes roughly normal returns.
There is no universal "good" threshold. Compare like with like.

## Sortino ratio

Like Sharpe, but divides by **downside deviation** (volatility of negative returns only), so
upside volatility is not penalized.

**Example.** Same 8% excess return, downside deviation 10% → Sortino = **0.80**.

## Maximum drawdown (MDD)

The largest peak-to-trough fall of the equity curve, before a new peak.

**Worked example.** Equity: 100, 120, 90, 110, 130, 104.

| Peak | Trough | Drawdown |
|---|---|---|
| 120 | 90 | (90 − 120)/120 = −25% |
| 130 | 104 | (104 − 130)/130 = −20% |

**MDD = 25%.** Compute it from the running maximum: `dd_t = equity_t / max(equity_0..t) − 1`.
Note that a 25% loss needs a +33% gain to recover. MDD says nothing about how long recovery took
(drawdown **duration**) or how often drawdowns occur.

## Calmar ratio

```
Calmar = CAGR / |MDD|
```

**Example.** CAGR 10%, MDD 25% → **0.40**.

## Value at Risk (VaR), briefly

"With 95% confidence, the one-day loss will not exceed X." Two simple ways:

- **Historical:** the 5th percentile of past daily returns.
- **Parametric (normal):** 1.645 × σ_daily × position value (zero mean assumed).
  Example: 1,000,000 position, σ_daily = 1% → VaR₉₅ ≈ **16,450**.

VaR says nothing about how bad losses are **beyond** the threshold, and real returns have
**fat tails**: extreme days happen more often than a normal distribution predicts.

## Risk-adjusted return

Comparing strategies by return per unit of risk (Sharpe, Sortino, Calmar) instead of raw return.
A lower-return strategy with much smaller drawdowns can be the better one, especially if it can
be scaled with leverage.

## Key takeaways

1. Annualize volatility with √252, returns with compounding.
2. Sharpe uses total volatility; Sortino only downside; Calmar uses drawdown.
3. Always look at max drawdown; it is what people actually experience.
