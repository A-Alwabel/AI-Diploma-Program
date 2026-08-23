# WHAT: write the training script into app/ — it saves model/iris_rf.joblib.
# WHY: the container will COPY this folder, so the model must be created inside
# app/ first; read the docstring's note about relative paths carefully.
"""Train a RandomForest on Iris and save it.

This script lives inside app/ and is meant to run from there (or at /app
inside the container, since the Dockerfile sets WORKDIR /app). Because the
working directory is app/, the relative path "model/iris_rf.joblib" below is
the SAME file as "app/model/iris_rf.joblib" seen from the repo root, and
"/app/model/iris_rf.joblib" inside the container.

Run from the app/ directory:  python model_train.py
"""
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

acc = accuracy_score(y_test, clf.predict(X_test))
print(f"Test accuracy: {acc:.2%}")

os.makedirs('model', exist_ok=True)
joblib.dump(clf, 'model/iris_rf.joblib')   # == app/model/iris_rf.joblib from repo root
print("Model saved to model/iris_rf.joblib")
