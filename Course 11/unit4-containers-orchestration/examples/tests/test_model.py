import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def _train():
    iris = load_iris()
    X_tr, X_te, y_tr, y_te = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    clf = RandomForestClassifier(n_estimators=50, random_state=42).fit(X_tr, y_tr)
    return clf, X_te, y_te


def test_predict_returns_one_label_per_row():
    clf, X_te, _ = _train()
    preds = clf.predict(X_te)
    assert len(preds) == len(X_te)


def test_predictions_are_valid_classes():
    clf, X_te, _ = _train()
    assert set(clf.predict(X_te)).issubset({0, 1, 2})


def test_accuracy_is_reasonable():
    clf, X_te, y_te = _train()
    assert accuracy_score(y_te, clf.predict(X_te)) > 0.8
