"""
GDI-Themed ML Pipeline Solution

Default use case:
- Dataset: datasets/raw/creditcard_fraud.csv (financial/terrorism financing)
- Target: "Class" (1 = fraud/flagged, 0 = normal)

The pipeline is generic: it will work with any tabular CSV and a provided
target column. Categorical columns are label-encoded; numeric columns are
scaled. Models: Logistic Regression, Random Forest, Linear SVM.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import LinearSVC


DEFAULT_RANDOM_STATE = 73


def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(f"Dataset at {path} is empty.")
    return df


def train_test_split_df(
    df: pd.DataFrame, target: str, test_size: float = 0.2
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    if target not in df.columns:
        raise KeyError(f"Target column '{target}' not found in dataset.")
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=DEFAULT_RANDOM_STATE, stratify=y
    )
    return X_train, X_test, y_train, y_test


def build_preprocessor(X: pd.DataFrame) -> ColumnTransformer:
    cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
    num_cols = X.select_dtypes(exclude=["object", "category"]).columns.tolist()

    transformers = []
    if cat_cols:
        transformers.append(
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
        )
    if num_cols:
        transformers.append(("num", StandardScaler(), num_cols))

    if not transformers:
        raise ValueError("No columns to process.")

    return ColumnTransformer(transformers=transformers)


def build_models(preprocessor: ColumnTransformer) -> Dict[str, Pipeline]:
    models = {
        "log_reg": Pipeline(
            steps=[
                ("prep", preprocessor),
                (
                    "clf",
                    LogisticRegression(
                        max_iter=1000,
                        random_state=DEFAULT_RANDOM_STATE,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
        "rf": Pipeline(
            steps=[
                ("prep", preprocessor),
                (
                    "clf",
                    RandomForestClassifier(
                        n_estimators=120,
                        max_depth=None,
                        random_state=DEFAULT_RANDOM_STATE,
                        n_jobs=-1,
                    ),
                ),
            ]
        ),
        "linear_svm": Pipeline(
            steps=[
                ("prep", preprocessor),
                (
                    "clf",
                    LinearSVC(
                        random_state=DEFAULT_RANDOM_STATE,
                        dual="auto",
                    ),
                ),
            ]
        ),
    }
    return models


def evaluate(model, X_test, y_test) -> Dict[str, float]:
    y_pred = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average="weighted", zero_division=0),
        "recall": recall_score(y_test, y_pred, average="weighted", zero_division=0),
        "f1": f1_score(y_test, y_pred, average="weighted", zero_division=0),
    }


def run(path: Path, target: str) -> None:
    df = load_data(path)
    X_train, X_test, y_train, y_test = train_test_split_df(df, target)
    preprocessor = build_preprocessor(X_train)
    models = build_models(preprocessor)

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        metrics = evaluate(model, X_test, y_test)
        results[name] = metrics
        print(f"\n{name} results:")
        for k, v in metrics.items():
            print(f"  {k}: {v:.4f}")
        print("\nClassification report:")
        print(classification_report(y_test, model.predict(X_test)))

    best_model = max(results.items(), key=lambda x: x[1]["f1"])
    print(f"\nBest model: {best_model[0]} (F1={best_model[1]['f1']:.4f})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GDI ML Pipeline")
    parser.add_argument(
        "--data",
        type=Path,
        default=Path("../../datasets/raw/creditcard_fraud.csv"),
        help="Path to CSV dataset",
    )
    parser.add_argument(
        "--target",
        type=str,
        default="Class",
        help="Target column name",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.data, args.target)


if __name__ == "__main__":
    main()
