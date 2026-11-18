"""Escalation predictor: flag support tickets likely to be escalated to engineering.

Escalations are expensive; the support lead wants to catch them early so a senior agent can
take over. The release gate for this model is: accuracy >= 0.90 and F1 >= 0.90.

Run:  python main.py
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

DATA = Path(__file__).parent / "data" / "tickets.csv"
FEATURES = ["words", "previous_escalations", "hours_open", "sentiment_score", "is_enterprise"]


def main() -> None:
    df = pd.read_csv(DATA)
    df["is_enterprise"] = (df["plan"] == "enterprise").astype(int)
    X, y = df[FEATURES], df["escalated"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7, stratify=y)

    model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)
    f1 = f1_score(y_test, pred, average="micro")
    print(f"tickets: {len(df)}  test tickets: {len(y_test)}")
    print(f"accuracy        : {acc:.3f}")
    print(f"F1 (escalations): {f1:.3f}")
    gate = acc >= 0.90 and f1 >= 0.90
    print(f"release gate    : {'PASS - ready to deploy' if gate else 'FAIL'}")


if __name__ == "__main__":
    main()
