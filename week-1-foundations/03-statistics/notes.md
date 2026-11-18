# 03 Statistics

Level: intermediate. Time: ≈ half a day to 1 day.
Links: [study-materials.md](../study-materials.md#03-statistics).

## After this topic you can

- Describe a distribution (center, spread, skew, tails) and pick a suitable summary.
- Explain sampling, the sampling distribution and the central limit theorem in your own words.
- Run and interpret a hypothesis test (two-proportion z-test, t-test, chi-square, permutation test).
- State correctly what a p-value and a 95% confidence interval mean, and what they don't.
- Compute and interpret Pearson and Spearman correlation, and explain why correlation ≠ causation.
- Name the common sampling and analysis biases and spot them in a dataset.

## Concepts

### Distributions

- **Normal:** symmetric, defined by mean and SD; many sums/averages are approximately normal.
- **Binomial / Bernoulli:** counts of successes (late or not).
- **Poisson:** counts per interval (orders per hour, courier load).
- **Log-normal / right-skewed:** durations, prices, distances. Use the median and IQR, or log-transform.
- **Heavy tails:** extreme values more likely than the normal predicts; the mean becomes unstable.
  (You will see this again in the finance primer: returns have fat tails.)

### Sampling and the CLT

- A statistic computed on a sample (e.g. the late rate) varies from sample to sample. Its
  distribution is the **sampling distribution**; its SD is the **standard error**.
- CLT: the mean of n independent draws is approximately normal for large n, whatever the
  population shape, with SE = σ/√n. Precision improves with √n, not n.
- **Bootstrap:** resample your data with replacement many times to estimate the SE or a CI of any
  statistic without a formula.

### Hypothesis testing

1. State H₀ (no difference) and H₁.
2. Choose a test that matches the data: proportions → two-proportion z-test or chi-square;
   means → Welch's t-test; no distributional assumptions → permutation test.
3. Compute the p-value: **the probability of data at least this extreme if H₀ were true.**
4. Report the **effect size and its CI**, not only the p-value.

A p-value is **not** the probability that H₀ is true, and a "non-significant" result is not proof
of no effect. With huge samples, trivial effects become "significant"; with small samples, real
effects are missed (low power). Running many tests and reporting the significant ones
(**p-hacking / multiple comparisons**) produces false discoveries. Correct with Bonferroni or
control the false discovery rate. (Finance primer: "data snooping".)

### Confidence intervals

A 95% CI is produced by a procedure that captures the true value in 95% of repeated samples. It
is not a 95% probability that the true value lies in this specific interval (frequentist view).

### Correlation

- **Pearson** measures linear association; sensitive to outliers.
- **Spearman** is rank-based and captures monotonic association; robust to outliers.
- Correlation ≠ causation: confounders (rain increases both courier load and delivery time),
  reverse causation, selection effects.
- Anscombe's quartet: the same correlation, very different data. Always plot.

### Bias

| Bias | Example in FreshCart |
|---|---|
| Selection bias | Analysing only orders that were not cancelled; the latest orders were cancelled more |
| Survivorship bias | Studying only couriers still employed; the slowest ones left |
| Measurement bias | Couriers mark "delivered" before reaching the door |
| Confounding | Rain raises both load and delay; load looks more harmful than it is |
| Simpson's paradox | A trend that appears in every zone reverses when zones are pooled |
| Look-ahead / leakage | Using information not available at decision time (Week 3, finance primer) |

## Exercises

| File | What it shows |
|---|---|
| `exercises/ex01_inference.py` | Rain vs late rate: z-test, chi-square, permutation test, bootstrap CI; CLT simulation; multiple-testing demo |
| `exercises/ex02_correlation_bias.py` | Pearson vs Spearman, outlier effect, confounding by rain, Simpson's paradox |

## Common mistakes

- Reporting "p < 0.05" without the effect size.
- Using a t-test on heavily skewed small samples without checking.
- Testing many slices and reporting the one that "worked".
- Concluding causation from observational correlation.
