# 04 Performance metrics

How much did the strategy make, and how did it make it?

## Return metrics

**Total return** = final equity / initial equity − 1.

**CAGR** (compound annual growth rate): the constant yearly rate that gives the same total.

```
CAGR = (final / initial)^(1 / years) − 1
```

**Worked example.** 10,000 → 16,105.10 over 5 years. 16,105.10 / 10,000 = 1.61051.
1.61051^(1/5) = 1.10 → **CAGR = 10%**. (Total return is 61.05%, not 50%: compounding.)

**Annualized return from daily returns** with N trading days (≈ 252 per year):

```
annualized = (1 + total_return)^(252 / N) − 1
```

Annualizing a short period amplifies noise: +5% in one month annualizes to ≈ +80%, which says
little about a full year.

## Trade-level metrics

**Worked example.** Ten closed trades (profit/loss in currency):

```
+200, −100, +150, −80, −120, +300, −50, −90, +100, −60
```

| Metric | Formula | Value |
|---|---|---|
| Number of trades | count | 10 |
| Wins / losses | count > 0 / < 0 | 4 / 6 |
| **Win rate** | wins / trades | 40% |
| Gross profit | sum of wins | 750 |
| Gross loss | sum of losses (absolute) | 500 |
| **Profit factor** | gross profit / gross loss | 1.50 |
| **Average win** | gross profit / wins | 187.50 |
| **Average loss** | gross loss / losses | 83.33 |
| **Expectancy** (per trade) | win rate × avg win − loss rate × avg loss | 0.4 × 187.50 − 0.6 × 83.33 = **25.00** |
| Net profit | sum | 250 (= 10 × 25.00 ✓) |

Observations:

- A **40% win rate can be profitable** when average wins are larger than average losses.
- **Profit factor > 1** means profitable before whatever costs are not yet included.
- **Number of trades** matters: 10 trades is far too few to trust any of these numbers
  (file 06, small samples). Think of each metric as an estimate with a wide confidence interval.

## Key takeaways

1. Use CAGR to compare different period lengths; never sum yearly returns.
2. Win rate alone means nothing without average win and loss.
3. Always report the number of trades next to the metrics.
