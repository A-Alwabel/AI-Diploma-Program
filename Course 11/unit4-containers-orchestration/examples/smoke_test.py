"""Smoke test for the deployed iris-api endpoint.

Runs after deployment in CI/CD.
Sends 3 known-good requests and asserts 200 OK responses.

Usage:
    python smoke_test.py [--url http://your-endpoint]

Exit codes:
    0 = all checks pass
    1 = at least one check failed
"""
import sys
import argparse

try:
    import requests
except ImportError:
    print("[SKIP] requests library not installed. Run: pip install requests")
    sys.exit(0)

parser = argparse.ArgumentParser()
parser.add_argument("--url", default="http://localhost:8000",
                    help="Base URL of the deployed API")
args = parser.parse_args()

BASE_URL = args.url

# Three representative Iris samples (one per class)
TEST_CASES = [
    {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2},  # setosa
    {"sepal_length": 6.4, "sepal_width": 3.2, "petal_length": 4.5, "petal_width": 1.5},  # versicolor
    {"sepal_length": 7.7, "sepal_width": 3.0, "petal_length": 6.1, "petal_width": 2.3},  # virginica
]

EXPECTED_PREDICTIONS = ["setosa", "versicolor", "virginica"]

print(f"=== Smoke Test against {BASE_URL} ===")

# Check health endpoint first
try:
    r = requests.get(f"{BASE_URL}/health", timeout=5)
    r.raise_for_status()
    print(f"[PASS] /health returned: {r.json()}")
except Exception as e:
    print(f"[FAIL] /health check failed: {e}")
    sys.exit(1)

# Check predict endpoint with test cases
all_passed = True
for i, (payload, expected) in enumerate(zip(TEST_CASES, EXPECTED_PREDICTIONS)):
    try:
        r = requests.post(f"{BASE_URL}/predict", json=payload, timeout=5)
        assert r.status_code == 200, f"Status {r.status_code}"
        body = r.json()
        assert "prediction" in body, "Missing 'prediction' key"
        assert body["prediction"] == expected, (
            f"Expected {expected}, got {body['prediction']}"
        )
        print(f"[PASS] Case {i+1}: {payload} -> {body['prediction']} "
              f"(confidence={body.get('confidence', '?')})")
    except Exception as e:
        print(f"[FAIL] Case {i+1}: {e}")
        all_passed = False

if all_passed:
    print("\nAll smoke tests passed. Deployment is healthy.")
    sys.exit(0)
else:
    print("\nSmoke test failed. CI/CD should trigger rollback.")
    sys.exit(1)
