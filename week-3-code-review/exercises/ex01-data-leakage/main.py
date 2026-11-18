"""Churn model: predict which subscription customers will cancel next month.

The retention team wants a ranked list of at-risk customers so they can contact them
BEFORE they decide to leave. This script trains a baseline model and reports its quality.

Run:  python main.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATA = Path(__file__).parent / "data" / "customers.csv"
TARGET = "churned"


def load() -> pd.DataFrame:
    df = pd.read_csv(DATA)
    return df


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    features = df.drop(columns=["customer_id", TARGET])
    features = pd.get_dummies(features, columns=["region", "contract"], drop_first=True, dtype=float)
    return features


def main() -> None:
    df = load()
    X = build_features(df)
    y = df[TARGET]

    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.25, random_state=42, stratify=y
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    proba = model.predict_proba(X_test)[:, 1]
    print(f"rows: {len(df)}  churn rate: {y.mean():.3f}")
    print(f"test accuracy: {accuracy_score(y_test, proba >= 0.5):.3f}")
    print(f"test ROC-AUC : {roc_auc_score(y_test, proba):.3f}")

    coefs = pd.Series(model.coef_[0], index=X.columns).sort_values(key=abs, ascending=False)
    print("\ntop drivers (standardized coefficients):")
    print(coefs.head(5).round(3).to_string())

    top = df.loc[X_test.index].assign(risk=proba).sort_values("risk", ascending=False)
    print("\nhighest-risk customers to contact:")
    print(top[["customer_id", "contract", "tenure_months", "risk"]].head(5).to_string(index=False))


if __name__ == "__main__":
    main()
