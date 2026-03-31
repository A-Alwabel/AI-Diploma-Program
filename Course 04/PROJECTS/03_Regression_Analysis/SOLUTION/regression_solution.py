"""
GDI-Themed Regression Solution

Default use case:
- Traffic Management: datasets/raw/us_accidents.csv (target: e.g., "Severity" or continuous proxy)
- Financial Risk: datasets/raw/creditcard_fraud.csv (use a continuous column as target)

Models: Linear, Ridge, Lasso, Polynomial (degree=2). Scaling included.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


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
        X, y, test_size=test_size, random_state=DEFAULT_RANDOM_STATE
    )
    return X_train, X_test, y_train, y_test


def build_models() -> Dict[str, Pipeline]:
    return {
        "linear": Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("reg", LinearRegression()),
            ]
        ),
        "ridge": Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("reg", Ridge(alpha=1.0, random_state=DEFAULT_RANDOM_STATE)),
            ]
        ),
        "lasso": Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("reg", Lasso(alpha=0.001, random_state=DEFAULT_RANDOM_STATE, max_iter=5000)),
            ]
        ),
        "poly_deg2": Pipeline(
            steps=[
                ("poly", PolynomialFeatures(degree=2, include_bias=False)),
                ("scaler", StandardScaler()),
                ("reg", LinearRegression()),
            ]
        ),
    }


def evaluate(model, X_test, y_test) -> Dict[str, float]:
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return {
        "mse": mse,
        "rmse": np.sqrt(mse),
        "mae": mean_absolute_error(y_test, y_pred),
        "r2": r2_score(y_test, y_pred),
    }


def run(path: Path, target: str) -> None:
    df = load_data(path)
    X_train, X_test, y_train, y_test = train_test_split_df(df, target)
    models = build_models()

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        metrics = evaluate(model, X_test, y_test)
        results[name] = metrics
        print(f"\n{name} results:")
        for k, v in metrics.items():
            print(f"  {k}: {v:.4f}")

    best_model = min(results.items(), key=lambda x: x[1]["rmse"])
    print(f"\nBest model: {best_model[0]} (RMSE={best_model[1]['rmse']:.4f})")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="GDI Regression Analysis")
    parser.add_argument(
        "--data",
        type=Path,
        default=Path("../../datasets/raw/us_accidents.csv"),
        help="Path to CSV dataset",
    )
    parser.add_argument(
        "--target",
        type=str,
        default="Severity",
        help="Target column name (continuous)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run(args.data, args.target)


if __name__ == "__main__":
    main()
