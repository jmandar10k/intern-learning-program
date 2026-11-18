# 04 ML algorithms and evaluation

Level: intermediate. Time: ≈ 1–1.5 days.
Links: [study-materials.md](../study-materials.md#04-ml-algorithms-and-evaluation).

## After this topic you can

- Train and compare linear/logistic regression, decision trees, random forests, gradient
  boosting and k-means with scikit-learn.
- Set up a correct evaluation protocol: train/validation/test split, stratification, cross-validation,
  time-based splits when order matters.
- Choose metrics that match the business question and the class balance.
- Build preprocessing inside a `Pipeline` so nothing leaks from test data into training.
- Recognize data leakage and explain why it produces suspiciously good scores.

## Concepts

### Algorithms (what, when, watch out)

| Algorithm | Use when | Watch out |
|---|---|---|
| Linear regression | Baseline for numeric targets; interpretable | Needs scaling for regularized versions; assumes linearity |
| Logistic regression | Baseline classifier; calibrated probabilities | Scale features; regularization strength `C` |
| Decision tree | Non-linear, interpretable rules | Overfits easily; limit `max_depth`, `min_samples_leaf` |
| Random forest | Strong default for tabular data | Less interpretable; impurity-based importances are biased toward high-cardinality features |
| Gradient boosting (e.g. `HistGradientBoosting*`) | Often best on tabular data | More hyperparameters; overfits with too many rounds without early stopping |
| k-means | Grouping into k compact clusters | Scale features; choose k (elbow, silhouette); assumes roughly spherical clusters |

### Bias–variance

Underfitting (high bias): train and test both poor. Overfitting (high variance): train great, test
worse. Use learning curves and validation curves to tell them apart.

### Evaluation protocol

1. **Hold out a test set first** and do not touch it until the end.
2. Use **cross-validation** on the training data for model selection and tuning.
3. **Stratify** splits for classification so class ratios are preserved.
4. If data has time order, split by time (train on the past, test on the future). A random split
   leaks the future. (Finance primer: in-sample vs out-of-sample, walk-forward.)
5. If rows are grouped (same customer many times), use `GroupKFold` so a group never appears in
   both train and test.
6. Always compare against a **dummy baseline** (`DummyClassifier`, `DummyRegressor`).

### Metrics

| Task | Metric | When |
|---|---|---|
| Classification | Accuracy | Only with balanced classes and equal error costs |
| | Precision / recall / F1 | Imbalanced classes; choose by error cost (missing a late order vs false alarm) |
| | Macro vs micro vs weighted F1 | Macro: every class counts equally (minority visible). Micro: every sample counts equally (≈ accuracy for single-label) |
| | ROC-AUC | Ranking quality, threshold-free; can look optimistic under heavy imbalance |
| | PR-AUC (average precision) | Imbalanced problems where positives matter |
| | Confusion matrix | Always look at it |
| Regression | MAE | Robust, same units as the target |
| | RMSE | Penalizes large errors more |
| | R² | Variance explained; compare to baseline |
| Clustering | Silhouette | Cohesion vs separation, no labels needed |

A 95% accuracy is meaningless if 95% of rows belong to one class: a model predicting only that
class gets it too.

### Data leakage

Leakage = information that would not be available at prediction time influences training or
evaluation. Symptoms: test scores that are suspiciously high, or much higher than production.

| Kind | Example |
|---|---|
| Target leakage | Feature computed from the target or after it (`delivery_minutes` to predict `late`) |
| Train–test contamination | Scaler, imputer, encoder or feature selector fit on all data before splitting |
| Temporal leakage | Random split on time-ordered data; future rows in training |
| Group leakage | Same entity in train and test |
| Duplicate leakage | Identical rows in both sets |

**Fix:** split first, put every fitted preprocessing step in a `Pipeline`, and fit the pipeline on
training data only. Cross-validate the whole pipeline.

## Exercises

| File | What it shows |
|---|---|
| `exercises/ex01_models_metrics.py` | Classification and regression with pipelines, dummy baselines, CV, confusion matrix, metric choice |
| `exercises/ex02_leakage_clustering.py` | Target leakage and preprocessing leakage demonstrated side by side; k-means with silhouette |

## Common mistakes

- Tuning on the test set.
- Reporting accuracy on imbalanced data.
- Calling `fit_transform` on the full dataset before splitting.
- Not comparing to a baseline.
