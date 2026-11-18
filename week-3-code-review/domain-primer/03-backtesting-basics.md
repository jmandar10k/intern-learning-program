# 03 Backtesting basics

## What backtesting is and isn't

A **backtest** simulates how a strategy's rules **would have** performed on historical data.

| It is | It isn't |
|---|---|
| A way to reject bad ideas cheaply | Proof that a strategy will make money |
| A check that rules are precise and implementable | A forecast |
| An estimate under assumptions (costs, fills, data quality) | Free of bias. Most backtests are optimistic |

## Historical simulation, step by step

For each bar, in time order:

1. Update indicators using **only data available up to that bar**.
2. Generate signals.
3. Place orders to be filled at a **later** price (e.g. next bar's open), not the price that
   created the signal.
4. Apply **costs** (commission, slippage, spread).
5. Update positions, cash and the **equity curve** (account value over time).

This is the same discipline as an ML model at prediction time: no future information.

## In-sample vs out-of-sample

- **In-sample (IS):** the period used to design and tune the strategy (≈ training data).
- **Out-of-sample (OOS):** a later period never used for design (≈ test data). Touch it once.
- A strategy that shines in-sample and fails out-of-sample is **overfit**.

## Walk-forward analysis

Repeat: tune on a window, test on the next window, roll forward.

```
|---- tune ----|- test -|
        |---- tune ----|- test -|
                |---- tune ----|- test -|
```

Concatenate the test windows to get an honest performance estimate. This is time-series
cross-validation (`TimeSeriesSplit` in scikit-learn).

## Costs

| Cost | What it is |
|---|---|
| **Commission** | Broker fee per trade (fixed or a percentage) |
| **Spread** | Difference between the buy (ask) and sell (bid) price; you pay it crossing the market |
| **Slippage** | Your fill is worse than the expected price (fast markets, large orders) |
| **Financing / borrow** | Cost of leverage or of borrowing shares to short |

**Worked example.** A strategy makes 200 round-trip trades a year with an average gross profit of
0.15% per trade. Round-trip costs (commission + spread + slippage) are 0.10%. Net per trade =
0.05%. Costs eat **two thirds** of the edge. A high-turnover strategy that ignores costs can turn
from profitable to losing.

## Capital and leverage

- **Capital:** the money the strategy starts with; returns are relative to it.
- **Leverage:** exposure / capital. With 2× leverage, a −10% move in the asset is about −20% for the
  account (before financing costs). Leverage scales returns **and** drawdowns, and can force
  liquidation.

## Key takeaways

1. A backtest is a simulation under assumptions; state them.
2. Separate in-sample and out-of-sample; prefer walk-forward.
3. Model costs realistically; they often decide whether a strategy works.
