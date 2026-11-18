# 06 Common pitfalls

Almost every impressive backtest that fails in practice falls into one of these traps. Most are
ML evaluation mistakes you already know, in a finance setting.

| Pitfall | What it is | ML equivalent | Example | Defense |
|---|---|---|---|---|
| **Look-ahead bias** | Using information not available at decision time | Data leakage | Trading at today's open on a signal computed from today's close; using restated earnings on their original date | Strict time indexing; shift signals by one bar; point-in-time data |
| **Survivorship bias** | Testing only on assets that still exist today | Selection bias | Backtesting on today's index members ignores companies that went bankrupt or were removed | Survivorship-free datasets with delisted assets |
| **Overfitting / curve fitting** | Tuning parameters until the past looks great | Overfitting | 12 parameters tuned on 3 years of data; a 20/50 crossover beats 21/50 by a wide margin | Few parameters; out-of-sample and walk-forward tests; parameter stability checks |
| **Data snooping** | Testing many ideas on the same data and keeping the winner | Multiple comparisons / p-hacking | Trying 500 indicator combinations and reporting the best | Hold out data you never look at; adjust for the number of trials; prefer ideas with a reason |
| **Ignoring costs** | No commission, spread or slippage | Unrealistic evaluation | A high-frequency strategy with a tiny per-trade edge | Model costs conservatively; test sensitivity to cost |
| **Small sample size** | Too few trades or too short a period to conclude anything | Low statistical power | 12 trades, 75% win rate | Report the number of trades; bootstrap confidence intervals; test across regimes |

## A quick sanity checklist for any backtest you see

1. Is every signal computed only from data available before the trade?
2. Does the asset universe include assets that later disappeared?
3. How many parameter combinations or ideas were tried?
4. Are results shown out-of-sample?
5. Are costs included? What happens if they double?
6. How many trades? Over how many years and market conditions?
7. Is the equity curve too smooth to be true?

## Key takeaways

1. If it looks too good, look for leakage first.
2. The number of things you tried is part of the result.
3. Costs and sample size turn many "edges" into noise.
