"""Week 1 / 04 ML / Exercise 2: data leakage and clustering.

Run:  python ex02_leakage_clustering.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, silhouette_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from freshcart_data import make_orders  # noqa: E402


def target_leakage() -> None:
    df = make_orders(n=3000, with_noise=False)
    honest = ["distance_km", "courier_load", "items", "hour"]
    leaky = honest + ["delivery_minutes"]  # known only AFTER delivery
    for name, cols in [("honest features", honest), ("with delivery_minutes", leaky)]:
        X_tr, X_te, y_tr, y_te = train_test_split(df[cols], df["late"], test_size=0.3, random_state=0, stratify=df["late"])
        model = Pipeline([("s", StandardScaler()), ("m", LogisticRegression(max_iter=2000))]).fit(X_tr, y_tr)
        print(f"  {name:<24} test ROC-AUC = {roc_auc_score(y_te, model.predict_proba(X_te)[:, 1]):.3f}")
    print("  -> near-perfect score = a red flag, not a success.")


def selection_leakage() -> None:
    """Feature selection on the full dataset before CV: the classic contamination."""
    rng = np.random.default_rng(0)
    X = rng.normal(size=(200, 5000))  # pure noise
    y = rng.integers(0, 2, size=200)  # random labels: true AUC is 0.5

    X_sel = SelectKBest(f_classif, k=20).fit_transform(X, y)  # WRONG: saw all labels
    wrong = cross_val_score(LogisticRegression(max_iter=1000), X_sel, y, cv=5, scoring="roc_auc").mean()

    right_pipe = Pipeline([("sel", SelectKBest(f_classif, k=20)), ("m", LogisticRegression(max_iter=1000))])
    right = cross_val_score(right_pipe, X, y, cv=5, scoring="roc_auc").mean()
    print(f"  select-then-CV (leaky) AUC = {wrong:.3f}   pipeline CV (correct) AUC = {right:.3f}")
    print("  -> on pure noise, the leaky protocol 'finds' signal.")


def clustering() -> None:
    df = make_orders(n=2000, with_noise=False)
    X = StandardScaler().fit_transform(df[["distance_km", "items", "basket_value", "courier_load"]])
    print("  k  silhouette")
    for k in range(2, 7):
        labels = KMeans(n_clusters=k, n_init=10, random_state=0).fit_predict(X)
        print(f"  {k}  {silhouette_score(X, labels):.3f}")


def main() -> None:
    print("1) Target leakage")
    target_leakage()
    print("\n2) Preprocessing / feature-selection leakage")
    selection_leakage()
    print("\n3) k-means delivery profiles")
    clustering()
    print(
        "\nYour turn:\n"
        "  1. Show scaler leakage: fit StandardScaler on all rows before the split, compare\n"
        "     with a pipeline. Why is the difference small here but large in other cases?\n"
        "  2. Pick k for k-means, describe each cluster in one line (use cluster means on\n"
        "     unscaled columns)."
    )


if __name__ == "__main__":
    main()
