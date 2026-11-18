# 02 Trading strategy basics

## What a strategy is

A **trading strategy** is a precise, repeatable set of rules that decides **when to enter**, **when to
exit**, **which direction** and **how much**. "Buy when it looks cheap" is not a strategy; "buy when
the 20-day average closes above the 50-day average, sell when it closes below" is.

| Component | Question it answers |
|---|---|
| **Signal** | Is there an opportunity now? (a value computed from data, e.g. an indicator crossing a threshold) |
| **Entry rule** | When exactly do I open a position? (e.g. at the next bar's open after the signal) |
| **Exit rule** | When do I close it? (opposite signal, stop loss, take profit, time limit) |
| **Direction** | **Long** (profit if price rises) or **short** (borrow and sell; profit if price falls) |
| **Position sizing** | How much capital or how many units? |

## Position sizing

A common rule: **risk a fixed fraction of capital per trade**.

**Worked example.** Capital 100,000. Risk 1% per trade = 1,000. Entry at 50.00, stop loss at 48.00
→ risk per share 2.00. Position = 1,000 / 2.00 = **500 shares** (25,000 of exposure). If the stop
is hit, the loss is about 1,000 (plus costs and slippage).

## Stop loss and take profit

- **Stop loss:** exit if price moves against you by a set amount; caps the loss per trade.
- **Take profit:** exit when a profit target is reached.
- In fast markets the fill can be worse than the stop price (**slippage**, file 03).

## Common strategy types

| Type | Idea | Typical signal |
|---|---|---|
| **Trend-following** | Trends persist; ride them | Moving-average crossover |
| **Mean reversion** | Prices revert to an average after extremes | Price far below/above a band; RSI extreme |
| **Momentum** | Recent winners keep winning for a while | Rank assets by past N-month return |
| **Breakout** | A move beyond a range starts a new trend | Close above the N-day high |

## Indicators

Indicators are functions of past prices. They summarize, they do not predict.

| Indicator | Definition | Reads as |
|---|---|---|
| **SMA(n)** | Average of the last n closes | Smoothed trend |
| **EMA(n)** | Weighted average with more weight on recent closes; α = 2/(n+1) | Faster-reacting trend |
| **RSI(14)** | 100 − 100/(1 + RS), RS = average gain / average loss over 14 periods | 0–100; > 70 "overbought", < 30 "oversold" (conventions, not laws) |
| **MACD** | EMA(12) − EMA(26); signal line = EMA(9) of MACD | Trend momentum; crossovers of MACD and its signal line |
| **Bollinger Bands** | SMA(20) ± 2 × standard deviation of the last 20 closes | Volatility envelope; touches of the bands |

**Worked SMA example.** Closes: 10, 11, 12, 13, 14. SMA(3) on the last bar = (12+13+14)/3 = **13**.
On bar 3 (the first bar with 3 values) it is (10+11+12)/3 = 11. Earlier bars have **no** SMA(3):
filling them with something else invents data.

**Timing matters.** An indicator computed with today's close can only drive a trade **after** the
close (e.g. at the next open). Trading at today's close on a signal computed from today's close
is subtly optimistic; trading at today's open on it is look-ahead bias.

## Key takeaways

1. A strategy is precise rules: signal, entry, exit, direction, size.
2. Size positions by risk, not by conviction.
3. Indicators use only past data; when the signal is known decides when you can trade.
