# Domain primer: reading guide

**Week 3, Day 1. Study only: no exercises, no grading.** About 6 hours.

Your later projects are finance-related. This primer gives you the vocabulary and intuition to
follow conversations about trading strategies and backtests. It is introductory on purpose: no
deep quant theory, and **nothing here is trading or investment advice**.

It is kept separate from the Week 3 review exercises, which use neutral, non-finance domains.

## Reading order and time

| # | File | Time | Focus on |
|---|---|---|---|
| 1 | [01-financial-basics.md](01-financial-basics.md) | 60 min | Simple vs log returns (do the worked example by hand), adjusted prices |
| 2 | [02-trading-strategy-basics.md](02-trading-strategy-basics.md) | 60 min | What a signal is, position sizing, what each indicator measures |
| 3 | [03-backtesting-basics.md](03-backtesting-basics.md) | 60 min | In-sample vs out-of-sample, walk-forward, costs |
| 4 | [04-performance-metrics.md](04-performance-metrics.md) | 45 min | CAGR, profit factor, expectancy; compute the example yourself |
| 5 | [05-risk-metrics.md](05-risk-metrics.md) | 60 min | Volatility scaling, Sharpe vs Sortino, max drawdown |
| 6 | [06-common-pitfalls.md](06-common-pitfalls.md) | 45 min | Map each pitfall to a Week 1–2 concept |
| — | [glossary.md](glossary.md) | as needed | Look up terms while reading |
| 7 | [self-check-questions.md](self-check-questions.md) | 30 min | Answer briefly in your progress log; discussed at the Week 3 check-in |

Keep a calculator or a Python shell open and recompute every worked example.

## How this connects to what you already know

| Finance idea | Week 1–2 concept |
|---|---|
| Look-ahead bias | Data leakage |
| In-sample vs out-of-sample | Train vs test split |
| Walk-forward analysis | Time-series cross-validation |
| Overfitting a strategy | Overfitting a model; multiple comparisons |
| Survivorship bias | Selection/survivorship bias in statistics |
| Fat tails, volatility | Distributions, standard deviation |
| Sharpe ratio | Signal-to-noise; mean over standard deviation |

## Optional short explainers (verified 2026-11-18)

Read only if a concept is unclear after the primer. Keep it brief: the one-day limit matters more.

| Topic | Link |
|---|---|
| CAGR | [Corporate Finance Institute: CAGR](https://corporatefinanceinstitute.com/resources/valuation/what-is-cagr/) |
| Sharpe ratio | [Corporate Finance Institute: Sharpe Ratio](https://corporatefinanceinstitute.com/resources/wealth-management/sharpe-ratio-definition-formula/) |
| Maximum drawdown | [Corporate Finance Institute: Maximum Drawdown](https://corporatefinanceinstitute.com/resources/uncategorized/maximum-drawdown/) |
| Survivorship bias | [Corporate Finance Institute: Survivorship Bias](https://corporatefinanceinstitute.com/resources/capital_markets/survivorship-bias/) |
