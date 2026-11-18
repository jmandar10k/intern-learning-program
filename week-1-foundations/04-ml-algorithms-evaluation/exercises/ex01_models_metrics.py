"""Week 1 / 04 ML / Exercise 1: models, pipelines, metrics.

Predict `late` (classification) and `delivery_minutes` (regression) from features
known at dispatch time.
Run:  python ex01_models_metrics.py
"""
from __future__ import annotations

import sys
from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    classification_report,
    confusion_matrix,
    mean_absolute_error,
    r2_score,
    roc_auc_score,
)
from sklearn.model_selection import StratifiedKFold, cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from freshcart_data import make_orders  # noqa: E402

NUMERIC = ["hour", "weekday", "items", "basket_value", "distance_km", "courier_load"]
CATEGORICAL = ["zone", "rain"]
FEATURES = NUMERIC + CATEGORICAL  # NOT delivery_minutes: it is only known after delivery


def preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        [
            ("num", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), NUMERIC),
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
        ]
    )


def main() -> None:
    df = make_orders(n=3000)
    df["rain"] = df["rain"].astype(str)
    X, y = df[FEATURES], df["late"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)

    models = {
        "dummy (most frequent)": DummyClassifier(strategy="most_frequent"),
        "logistic regression": LogisticRegression(max_iter=1000),
        "decision tree (depth 4)": DecisionTreeClassifier(max_depth=4, random_state=0),
        "random forest": RandomForestClassifier(n_estimators=200, min_samples_leaf=5, random_state=0),
        "hist gradient boosting": HistGradientBoostingClassifier(random_state=0),
    }
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=0)
    print("5-fold CV on the training set (PR-AUC / average precision):")
    for name, model in models.items():
        pipe = Pipeline([("prep", preprocessor()), ("model", model)])
        scores = cross_val_score(pipe, X_tr, y_tr, cv=cv, scoring="average_precision")
        print(f"  {name:<26} {scores.mean():.3f} +/- {scores.std():.3f}")

    best = Pipeline([("prep", preprocessor()), ("model", HistGradientBoostingClassifier(random_state=0))])
    best.fit(X_tr, y_tr)
    proba = best.predict_proba(X_te)[:, 1]
    pred = (proba >= 0.5).astype(int)
    print(f"\nTest set (touched once): ROC-AUC={roc_auc_score(y_te, proba):.3f}  PR-AUC={average_precision_score(y_te, proba):.3f}")
    print("confusion matrix [[TN FP] [FN TP]]:\n", confusion_matrix(y_te, pred))
    print(classification_report(y_te, pred, digits=3))

    # Regression: delivery_minutes from the same dispatch-time features.
    yr = df["delivery_minutes"]
    Xr_tr, Xr_te, yr_tr, yr_te = train_test_split(X, yr, test_size=0.25, random_state=42)
    for name, model in {"dummy (mean)": DummyRegressor(), "linear regression": LinearRegression()}.items():
        pipe = Pipeline([("prep", preprocessor()), ("model", model)]).fit(Xr_tr, yr_tr)
        p = pipe.predict(Xr_te)
        print(f"regression {name:<18} MAE={mean_absolute_error(yr_te, p):.2f} min  R2={r2_score(yr_te, p):.3f}")

    print(
        "\nYour turn:\n"
        "  1. Operations prefers catching late orders over avoiding false alarms. Pick a\n"
        "     threshold that gives recall >= 0.8 on a validation split (not the test set).\n"
        "  2. Compare macro-F1 and micro-F1 for the dummy model. Explain the gap.\n"
        "  3. Plot a learning curve for the random forest. Over- or under-fitting?"
    )


if __name__ == "__main__":
    main()
