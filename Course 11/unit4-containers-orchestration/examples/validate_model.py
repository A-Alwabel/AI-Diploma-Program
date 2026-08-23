# WHAT: write validate_model.py — the accuracy + latency gate as a standalone script.
# WHY: a gate must be a script, not a notebook: CI runs it headless and its
# sys.exit code decides whether the Docker build ever happens.
"""Model validation gate for CI/CD.

Checks:
  1. Test-set accuracy >= ACCURACY_THRESHOLD
  2. p95 inference latency < LATENCY_P95_MS

Exit codes:
  0 = all checks pass  (CI proceeds to build)
  1 = at least one check failed  (CI blocks deployment)
"""
import sys
import time
import numpy as np
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

ACCURACY_THRESHOLD = 0.90   # 90% minimum test accuracy
LATENCY_P95_MS     = 100.0  # 100ms maximum p95 latency
N_LATENCY_SAMPLES  = 200    # number of predictions for latency measurement
MODEL_PATH         = "app/model/iris_rf.joblib"


# Gate 1: holdout accuracy against the fixed threshold.
def check_accuracy(model, X_test, y_test):
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    status = "PASS" if acc >= ACCURACY_THRESHOLD else "FAIL"
    print(f"[{status}] Accuracy: {acc:.4f} (threshold: {ACCURACY_THRESHOLD})")
    return acc >= ACCURACY_THRESHOLD


# Gate 2: p95 of single-sample predictions against the latency budget.
def check_latency(model, X_test):
    samples = X_test[:N_LATENCY_SAMPLES]
    latencies = []
    for row in samples:
        t0 = time.perf_counter()
        model.predict([row])
        latencies.append((time.perf_counter() - t0) * 1000)  # ms
    p95 = float(np.percentile(latencies, 95))
    status = "PASS" if p95 < LATENCY_P95_MS else "FAIL"
    print(f"[{status}] p95 latency: {p95:.2f}ms (threshold: {LATENCY_P95_MS}ms)")
    return p95 < LATENCY_P95_MS


# Load artifact, run both gates, and exit 0 (pass) or 1 (block deploy).
def main():
    print("=== Model Validation Gate ===")

    # Load model
    try:
        model = joblib.load(MODEL_PATH)
        print(f"Loaded model from {MODEL_PATH}")
    except FileNotFoundError:
        print(f"[FAIL] Model not found at {MODEL_PATH}")
        sys.exit(1)

    # Load test data (same split used during training)
    iris = load_iris()
    X, y = iris.data, iris.target
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Run checks
    accuracy_ok = check_accuracy(model, X_test, y_test)
    latency_ok  = check_latency(model, X_test)

    if accuracy_ok and latency_ok:
        print("\nAll checks passed. Model is approved for deployment.")
        sys.exit(0)
    else:
        print("\nOne or more checks failed. Deployment blocked.")
        sys.exit(1)


if __name__ == "__main__":
    main()
