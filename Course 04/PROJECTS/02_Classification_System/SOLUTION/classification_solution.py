"""
GDI-Themed Multi-Class Classification Solution

Default use cases:
- Emergency Response: datasets/raw/montgomery_911_calls.csv (target: "category")
- Cyber Threats: datasets/raw/unsw_nb15.csv subset (target: "label")

Handles generic tabular data with categorical + numeric features, using
StandardScaler + OneHotEncoder. Models: Logistic Regression, Random Forest,
Linear SVM. Includes class-weight support for imbalance.
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


def train_val_test_split(
    df: pd.DataFrame,
    target: str,
    test_size: float = 0.2,
    val_size: float = 0.2,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.Series, pd.Series, pd.Series]:
    if target not in df.columns:
        raise KeyError(f"Target column '{target}' not found in dataset.")
    X = df.drop(columns=[target])
    y = df[target]
    X_train, X_holdout, y_train, y_holdout = train_test_split(
        X, y, test_size=test_size, random_state=DEFAULT_RANDOM_STATE, stratify=y
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_holdout, y_holdout, test_size=0.5, random_state=DEFAULT_RANDOM_STATE, stratify=y_holdout
    )
    return X_train, X_val, X_test, y_train, y_val, y_test


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
                        class_weight="balanced",
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
                        n_estimators=140,
                        max_depth=None,
                        random_state=DEFAULT_RANDOM_STATE,
                        n_jobs=-1,
                        class_weight="balanced_subsample",
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
    X_train, X_val, X_test, y_train, y_val, y_test = train_val_test_split(df, target)
    preprocessor = build_preprocessor(X_train)
    models = build_models(preprocessor)

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        # Quick val check to avoid overfitting signals
        val_metrics = evaluate(model, X_val, y_val)
        test_metrics = evaluate(model, X_test, y_test)
        results[name] = {"val": val_metrics, "test": test_metrics}
        print(f"\n{name} (val): {val_metrics}")
        print(f"{name} (test): {test_metrics}")
        print("\nClassification report (test):")
        print(classification_report(y_test, model.predict(X_test)))

    best_model = max(results.items(), key=lambda x: x[1]["test"]["f1"])
    print(f"\nBest model: {best_model[0]} (Test F1={best_model[1]['test']['f1']:.4f})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GDI Multi-Class Classification")
    parser.add_argument(
        "--data",
        type=Path,
        default=Path("../../datasets/raw/montgomery_911_calls.csv"),
        help="Path to CSV dataset",
    )
    parser.add_argument(
        "--target",
        type=str,
        default="category",
        help="Target column name",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.data, args.target)


if __name__ == "__main__":
    main()
