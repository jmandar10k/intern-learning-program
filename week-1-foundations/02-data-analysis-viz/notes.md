# 02 Data analysis and visualization

Level: intermediate. Time: ≈ 1 day.
Links: [study-materials.md](../study-materials.md#02-data-analysis-and-visualization).

## After this topic you can

- Load, inspect and clean a dataset with pandas and numpy (types, missing values, duplicates,
  outliers).
- Join tables safely and check that the join did what you intended.
- Aggregate with `groupby`, pivot and reshape, and reconcile aggregates with raw totals.
- Run a structured EDA and choose the right plot for the question.
- Explain why a preprocessing choice (e.g. filling NaN with 0) can silently change conclusions.

## Concepts

### numpy essentials

- Vectorize: operate on whole arrays, not Python loops.
- Broadcasting rules: shapes align from the right; size-1 dimensions stretch.
- `np.nan` propagates: `np.mean([1, np.nan]) → nan`; use `np.nanmean` deliberately.
- Use `np.random.default_rng(seed)` for reproducible randomness.

### pandas workflow

1. **Inspect:** `df.shape`, `df.dtypes`, `df.head()`, `df.describe(include="all")`,
   `df.isna().mean()`, `df.duplicated().sum()`.
2. **Fix types:** categories, datetimes, booleans. Wrong dtypes cause wrong sorting and joins.
3. **Missing values:** understand *why* they are missing before choosing to drop, impute
   (median/mode/model) or flag (`is_missing` column). Filling with 0 is only right when 0 is the
   true value.
4. **Outliers:** detect with IQR or domain rules; decide clip, drop or keep, and document it.
5. **Joins:** `pd.merge(..., on=key, how=..., validate="many_to_one", indicator=True)`.
   `validate` raises if the key is not unique where you expect; `indicator` shows unmatched rows.
   A many-to-many join silently multiplies rows and inflates totals.
6. **Aggregate:** `groupby(...).agg(...)` with named aggregations; `pivot_table`; `melt`.
7. **Reconcile:** totals after cleaning/joining should match the raw data (or differ by an amount
   you can explain). This single habit catches most silent data bugs.

### EDA checklist

- Target distribution and base rate (here: late rate ≈ 24%).
- Univariate: histograms/boxplots for numerics, counts for categoricals.
- Bivariate with target: late rate by zone, hour, rain; delivery time vs distance.
- Missingness patterns: is missingness itself related to the target?
- Write down three findings and one question after EDA.

### Choosing a plot

| Question | Plot |
|---|---|
| Distribution of one numeric | Histogram / KDE (`sns.histplot`), boxplot |
| Compare a numeric across groups | Boxplot / violin / bar of means with CI (`sns.barplot`) |
| Relationship of two numerics | Scatter (`sns.scatterplot`), with trend (`sns.regplot`) |
| Rate by two categoricals | Heatmap of a pivot table |
| Change over time | Line plot |

Good plots: labelled axes with units, a title that states the finding, no 3D, no unnecessary
colors.

## Exercises

| File | What it shows |
|---|---|
| `exercises/ex01_cleaning_joins.py` | Inspection, missing values, outliers, a safe join with `validate`, reconciliation checks, the NaN→0 trap |
| `exercises/ex02_eda_plots.py` | EDA and plots saved to `exercises/plots/` (no display needed) |

## Common mistakes

- `fillna(0)` on a column where 0 is a real, meaningful value (distance, price).
- Joining on a non-unique key and not noticing the row count changed.
- `groupby` on the wrong column, or averaging averages instead of re-computing from totals.
- Reading conclusions off a plot without checking the group sizes.
