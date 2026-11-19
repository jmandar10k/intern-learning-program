# 01 Financial basics

## Asset classes

| Asset | One-line intro |
|---|---|
| **Stocks (equities)** | A share of ownership in a company; price moves with the company's prospects and the market. |
| **Indices** | A number tracking a basket of stocks (e.g. a broad-market index). You cannot buy an index directly; it is a benchmark. |
| **ETFs** | Exchange-traded funds: a fund (often tracking an index) that trades like a stock. |
| **Bonds** | Loans to governments or companies that pay interest. |
| **Futures** | A contract to buy or sell an asset at a set price on a future date; usually traded with margin (leverage). |
| **Options** | The right, not the obligation, to buy (call) or sell (put) at a set price before a date. |
| **FX, commodities, crypto** | Currencies, raw materials and digital assets; same return/risk concepts apply. |

## Prices as data: OHLCV bars

Market data usually arrives as **bars**, one per time interval:

| Field | Meaning |
|---|---|
| **O**pen | First traded price in the interval |
| **H**igh | Highest price |
| **L**ow | Lowest price |
| **C**lose | Last traded price in the interval |
| **V**olume | Quantity traded |

**Timeframes:** 1-minute, 1-hour, daily, weekly bars. A daily close is only known **at the end of
the day**: using it to make a decision earlier that same day is look-ahead bias (file 06).

## Returns

**Simple return** over one period:

```
r = (P_t − P_{t−1}) / P_{t−1} = P_t / P_{t−1} − 1
```

**Log return:**

```
ℓ = ln(P_t / P_{t−1})
```

### Worked example

Price goes 100 → 110 → 99.

| Step | Simple return | Log return |
|---|---|---|
| 100 → 110 | +10.00% | ln(1.10) = +0.0953 |
| 110 → 99 | −10.00% | ln(0.90) = −0.1054 |
| Sum | 0.00% (**wrong** as a total) | −0.0101 |
| True total (100 → 99) | −1.00% | exp(−0.0101) − 1 = −1.00% ✓ |

- Simple returns **compound**: total = (1.10 × 0.90) − 1 = −1%. They do **not** add.
- Log returns **add** over time, which is convenient for multi-period math.
- Simple returns **aggregate across assets** in a portfolio (weighted average); log returns do not.
- For small moves they are nearly equal (+1% simple ≈ +0.995% log).

## Adjusted vs unadjusted prices

Corporate actions change the price without changing an investor's wealth.

**Stock split (2-for-1):** each share becomes two; the price halves. Unadjusted data shows
200 → 100, a fake −50% "return". **Adjusted** prices rescale history so the series is continuous.

**Dividends:** a company pays cash per share. On the **ex-dividend date** the price typically
drops by about the dividend. Example: price 50.00, dividend 1.00 → opens near 49.00. The holder
didn't lose 2%: they received 1.00 in cash.

- **Price return** ignores dividends; **total return** includes them.
- Use **adjusted** prices for return calculations and backtests; use **unadjusted** prices when
  you need what actually traded on a given day (e.g. order sizes, price limits).
- Mixing the two in one dataset silently creates fake jumps.

## Key takeaways

1. Returns compound; summing simple returns over time is wrong.
2. A daily close is only known after the close.
3. Splits and dividends create fake moves in unadjusted data.
