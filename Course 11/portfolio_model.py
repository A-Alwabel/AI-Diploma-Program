"""Portfolio-model contract for AIAT 125 — Deploying AI Models (Course 11).

WHAT: one tiny library that lets every Course 11 notebook deploy *the student's own*
trained model instead of a toy that the deployment course trained for itself.

WHY: deployment is the last mile of a model's life. If Course 11 trains its own
throwaway classifier in every notebook, students never experience the real job —
receiving somebody else's artifact, reading its contract, and getting it online.
So Course 11 consumes an artifact produced in AIAT 114 (Course 04) or
AIAT 122 (Course 08). See PORTFOLIO_MODEL.md for the student-facing guide.

THE CONTRACT — a portfolio directory holding exactly two things:

    <portfolio>/
    ├── model.joblib          the artifact  (or model.onnx / model_scripted.pt)
    └── model_card.json       the metadata that makes the artifact servable

`model_card.json` must contain:

    name            str   short slug, e.g. "fraud-rf"
    source_course   str   "AIAT 114" or "AIAT 122"
    framework       str   "sklearn" | "onnx" | "torchscript"
    artifact        str   filename of the model file, relative to the card
    task            str   "classification" (Course 11's serving lessons need
                          predict_proba; see PORTFOLIO_MODEL.md)
    feature_names   list  input columns, IN THE ORDER THE MODEL EXPECTS THEM
    class_names     list  human-readable label per class index
    sample_input    list  one real feature row — the request body every lesson
                          uses to smoke-test the endpoint
    sample_batch    list  up to 20 real held-out rows — the "golden set"
    sample_batch_predictions
                    list  the class index the model returned for each golden row
                          AT EXPORT TIME. Replay them through any serving stack
                          and every answer must still match, or the stack is
                          distorting your model.
    metric          dict  {"name","value","split"} — the honest held-out score

Where is the portfolio directory? `$AI_DIPLOMA_PORTFOLIO` if set, else
`~/ai-diploma-portfolio`.

No portfolio model yet? `load_portfolio_model()` builds the NAMED FALLBACK
`wdbc-baseline` — a logistic-regression pipeline on the real Wisconsin
Diagnostic Breast Cancer study that ships inside scikit-learn, so it works
offline, on any machine, with no download. The card records
`"is_fallback": true` and every notebook says so out loud.
"""

from __future__ import annotations

import json
import os
import re
from datetime import date
from pathlib import Path

__all__ = [
    "ENV_VAR", "DEFAULT_DIR", "FALLBACK_NAME", "CARD_NAME", "REQUIRED_CARD_KEYS",
    "GOLDEN_BATCH_SIZE", "portfolio_dir", "build_fallback",
    "export_portfolio_model", "load_portfolio_model", "schema_fields", "describe",
]

ENV_VAR = "AI_DIPLOMA_PORTFOLIO"
DEFAULT_DIR = Path.home() / "ai-diploma-portfolio"
CARD_NAME = "model_card.json"
FALLBACK_NAME = "wdbc-baseline"

REQUIRED_CARD_KEYS = (
    "name", "source_course", "framework", "artifact", "task",
    "feature_names", "class_names", "sample_input", "sample_batch",
    "sample_batch_predictions", "metric",
)

GOLDEN_BATCH_SIZE = 20


# --------------------------------------------------------------------------- #
# Where the portfolio lives
# --------------------------------------------------------------------------- #
def portfolio_dir() -> Path:
    """Resolve the portfolio directory ($AI_DIPLOMA_PORTFOLIO or ~/ai-diploma-portfolio)."""
    raw = os.environ.get(ENV_VAR)
    return Path(raw).expanduser() if raw else DEFAULT_DIR


# --------------------------------------------------------------------------- #
# Adapters — so an ONNX or TorchScript artifact answers the same two calls
# as a scikit-learn estimator: .predict(X) and .predict_proba(X)
# --------------------------------------------------------------------------- #
class _OnnxClassifier:
    """Wrap an ONNX Runtime session so it looks like a scikit-learn classifier."""

    def __init__(self, path: Path):
        import numpy as np
        import onnxruntime as ort
        self._np = np
        self.session = ort.InferenceSession(str(path), providers=["CPUExecutionProvider"])
        self.input_name = self.session.get_inputs()[0].name

    def _raw(self, X):
        np = self._np
        arr = np.asarray(X, dtype=np.float32)
        return np.asarray(self.session.run(None, {self.input_name: arr})[0])

    def predict_proba(self, X):
        np = self._np
        out = self._raw(X)
        # Logits -> probabilities via a numerically stable softmax.
        shifted = out - out.max(axis=1, keepdims=True)
        exp = np.exp(shifted)
        return exp / exp.sum(axis=1, keepdims=True)

    def predict(self, X):
        return self.predict_proba(X).argmax(axis=1)


class _TorchScriptClassifier:
    """Wrap a TorchScript module so it looks like a scikit-learn classifier."""

    def __init__(self, path: Path):
        import numpy as np
        import torch
        self._np, self._torch = np, torch
        self.module = torch.jit.load(str(path))
        self.module.eval()

    def predict_proba(self, X):
        torch, np = self._torch, self._np
        with torch.no_grad():
            out = self.module(torch.tensor(np.asarray(X, dtype=np.float32)))
            return torch.softmax(out, dim=1).numpy()

    def predict(self, X):
        return self.predict_proba(X).argmax(axis=1)


def _load_artifact(card: dict, base: Path):
    """Load the model file named by the card, using the right loader for its framework."""
    path = base / card["artifact"]
    if not path.exists():
        raise FileNotFoundError(
            f"model_card.json points at '{card['artifact']}' but {path} does not exist."
        )
    framework = card["framework"]
    if framework == "sklearn":
        import joblib
        return joblib.load(path)
    if framework == "onnx":
        return _OnnxClassifier(path)
    if framework == "torchscript":
        return _TorchScriptClassifier(path)
    raise ValueError(
        f"Unknown framework '{framework}'. Use 'sklearn', 'onnx', or 'torchscript'."
    )


# --------------------------------------------------------------------------- #
# The named fallback: wdbc-baseline
# --------------------------------------------------------------------------- #
def build_fallback(dest: Path | None = None) -> tuple[object, dict]:
    """Train and export the NAMED FALLBACK `wdbc-baseline`, then return (model, card).

    Real data, no download: the Wisconsin Diagnostic Breast Cancer study
    (569 biopsies, 30 features) ships inside scikit-learn. This is what a
    student without a portfolio model deploys, so the deployment lessons still
    have a genuine artifact with a genuine held-out score.
    """
    import joblib
    from sklearn.datasets import load_breast_cancer
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    base = Path(dest) if dest else portfolio_dir()
    base.mkdir(parents=True, exist_ok=True)

    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42, stratify=data.target
    )
    # Scaler + logistic regression in ONE Pipeline: the scaler must travel with
    # the model, otherwise the server scales inputs differently from training.
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=10_000, random_state=42)),
    ]).fit(X_train, y_train)

    accuracy = float(accuracy_score(y_test, model.predict(X_test)))
    joblib.dump(model, base / "model.joblib")

    # Pick the smoke-test row deliberately: of the held-out rows the model gets
    # RIGHT, take the one whose confidence is the median. A maximally confident
    # row would make every lesson print "100.0%" and teach students nothing
    # about reading a probability.
    proba = model.predict_proba(X_test)
    correct = proba.argmax(axis=1) == y_test
    confidence = proba.max(axis=1)
    candidates = confidence.argsort()[correct[confidence.argsort()]]
    sample_idx = int(candidates[len(candidates) // 2])

    card = {
        "name": FALLBACK_NAME,
        "owner": "course fallback (not a student model)",
        "source_course": "AIAT 125 fallback",
        "source_notebook": "Course 11/portfolio_model.py :: build_fallback()",
        "framework": "sklearn",
        "artifact": "model.joblib",
        "task": "classification",
        "feature_names": [str(n) for n in data.feature_names],
        "class_names": [str(n) for n in data.target_names],
        "sample_input": [float(v) for v in X_test[sample_idx]],
        "sample_batch": [[float(v) for v in row] for row in X_test[:GOLDEN_BATCH_SIZE]],
        "sample_batch_predictions": [int(i) for i in
                                     model.predict(X_test[:GOLDEN_BATCH_SIZE])],
        "metric": {"name": "accuracy", "value": round(accuracy, 4),
                   "split": "held-out 20% (random_state=42, stratified)"},
        "created": date.today().isoformat(),
        "is_fallback": True,
    }
    (base / CARD_NAME).write_text(json.dumps(card, indent=2) + "\n")
    return model, card


def _drop_duplicate_feature_names(estimator, feature_names):
    """Remove sklearn's own `feature_names_in_` once the card records the same names.

    Fitting on a DataFrame stamps the column names into the estimator. At serving
    time the request arrives as a plain list of floats, and sklearn then warns on
    EVERY prediction that the feature names went missing. Two copies of one
    contract is one copy too many: the card owns the feature order from here, so
    the duplicate inside the artifact goes away and inference stays quiet.
    """
    targets = [estimator]
    if hasattr(estimator, "steps"):
        targets += [step for _, step in estimator.steps]
    for obj in targets:
        stamped = obj.__dict__.get("feature_names_in_")
        if stamped is None:
            continue
        stamped = [str(n) for n in stamped]
        if stamped != [str(n) for n in feature_names]:
            raise ValueError(
                "The model was fitted on columns "
                f"{stamped[:5]}{'...' if len(stamped) > 5 else ''} but you passed "
                f"feature_names={list(feature_names)[:5]}"
                f"{'...' if len(feature_names) > 5 else ''}. Serving would feed the "
                "model its features in the wrong order. Fix the order, then export again."
            )
        del obj.__dict__["feature_names_in_"]
    return estimator


# --------------------------------------------------------------------------- #
# The one call an AIAT 114 / AIAT 122 student makes to hand a model to Course 11
# --------------------------------------------------------------------------- #
def export_portfolio_model(
    source,
    *,
    X_test,
    y_test,
    feature_names,
    class_names,
    name,
    source_course,
    source_notebook="",
    framework="sklearn",
    metric_name="accuracy",
    dest=None,
    owner="",
):
    """Write a Course 11 portfolio model: the artifact plus a complete model card.

    Add three lines to the end of the AIAT 114 or AIAT 122 notebook that produced
    your best model, and Course 11 can deploy it. See PORTFOLIO_MODEL.md.

    Parameters
    ----------
    source : a FITTED estimator when framework="sklearn"; otherwise the PATH to a
        file you already exported (`.onnx` from `torch.onnx.export`, or a
        TorchScript `.pt` from `torch.jit.script(model).save(...)`).
    X_test, y_test : the HELD-OUT split. The score written into the card is
        measured here, so it is the number you would defend in a review.
    feature_names : the input columns, in the order the model consumes them.
    class_names : human-readable label for each class index.
    framework : "sklearn" | "onnx" | "torchscript".

    Returns the card it wrote.
    """
    import numpy as np

    base = Path(dest).expanduser() if dest else portfolio_dir()
    base.mkdir(parents=True, exist_ok=True)

    X_test = np.asarray(X_test, dtype=float)
    y_test = np.asarray(y_test)
    feature_names = [str(n) for n in feature_names]
    class_names = [str(n) for n in class_names]

    if X_test.shape[1] != len(feature_names):
        raise ValueError(
            f"X_test has {X_test.shape[1]} columns but you passed "
            f"{len(feature_names)} feature_names. The card's feature order is "
            "the API contract - it has to be exactly right."
        )

    # --- put the artifact in the portfolio directory -----------------------
    if framework == "sklearn":
        import copy
        import joblib
        artifact = "model.joblib"
        # Deep-copy first: exporting must never mutate the model still live in
        # the student's notebook.
        estimator = _drop_duplicate_feature_names(copy.deepcopy(source), feature_names)
        joblib.dump(estimator, base / artifact)
        model = joblib.load(base / artifact)
    elif framework in ("onnx", "torchscript"):
        import shutil
        src = Path(source).expanduser()
        artifact = "model.onnx" if framework == "onnx" else "model_scripted.pt"
        if src.resolve() != (base / artifact).resolve():
            shutil.copy2(src, base / artifact)
        model = _load_artifact({"artifact": artifact, "framework": framework}, base)
    else:
        raise ValueError(f"framework must be 'sklearn', 'onnx' or 'torchscript', not {framework!r}")

    # --- score and golden batch, measured from the artifact ON DISK --------
    # WHY from the artifact and not from the in-memory model: if serialization
    # lost something, we want to find out here, not in production.
    predictions = np.asarray(model.predict(X_test)).astype(int).ravel()
    accuracy = float((predictions == y_test.astype(int)).mean())

    batch = X_test[:GOLDEN_BATCH_SIZE]
    batch_predictions = np.asarray(model.predict(batch)).astype(int).ravel()

    # Smoke-test row: a correctly classified row at median confidence, so lessons
    # print a realistic probability instead of a saturated 1.00.
    if hasattr(model, "predict_proba"):
        proba = np.asarray(model.predict_proba(X_test))
        correct = proba.argmax(axis=1) == y_test.astype(int)
        order = proba.max(axis=1).argsort()
        candidates = order[correct[order]]
        sample_idx = int(candidates[len(candidates) // 2]) if len(candidates) else 0
    else:
        sample_idx = 0

    card = {
        "name": name,
        "owner": owner,
        "source_course": source_course,
        "source_notebook": source_notebook,
        "framework": framework,
        "artifact": artifact,
        "task": "classification",
        "feature_names": feature_names,
        "class_names": class_names,
        "sample_input": [float(v) for v in X_test[sample_idx]],
        "sample_batch": [[float(v) for v in row] for row in batch],
        "sample_batch_predictions": [int(i) for i in batch_predictions],
        "metric": {"name": metric_name, "value": round(accuracy, 4),
                   "split": f"held-out set of {len(y_test)} rows supplied at export"},
        "created": date.today().isoformat(),
        "is_fallback": False,
    }
    (base / CARD_NAME).write_text(json.dumps(card, indent=2) + "\n")
    print(f"Exported '{name}' to {base}")
    print(f"  {artifact} + {CARD_NAME}   |   {metric_name} = {accuracy:.4f} on {len(y_test)} held-out rows")
    return card


# --------------------------------------------------------------------------- #
# The one call every Course 11 notebook makes
# --------------------------------------------------------------------------- #
def load_portfolio_model(verbose: bool = True) -> tuple[object, dict]:
    """Return (model, card) for the student's portfolio model, or the named fallback.

    Never raises for the ordinary "I haven't exported one yet" case — it builds
    `wdbc-baseline` instead and says so, so every Course 11 notebook runs for
    everyone on the first try.
    """
    base = portfolio_dir()
    card_path = base / CARD_NAME

    if card_path.exists():
        card = json.loads(card_path.read_text())
        missing = [k for k in REQUIRED_CARD_KEYS if k not in card]
        if missing:
            raise KeyError(
                f"{card_path} is missing required key(s): {missing}. "
                "See Course 11/PORTFOLIO_MODEL.md for the full card schema."
            )
        model = _load_artifact(card, base)
    else:
        if verbose:
            print("No portfolio model found at", base)
            print("-> Building the NAMED FALLBACK 'wdbc-baseline' so this lesson can run.")
        model, card = build_fallback(base)

    if verbose:
        print(describe(card, base))
    return model, card


def describe(card: dict, base: Path | None = None) -> str:
    """One honest paragraph naming the model being deployed and where it came from."""
    base = base or portfolio_dir()
    metric = card.get("metric", {})
    header = (
        f"FALLBACK MODEL '{card['name']}' — this is NOT your model."
        if card.get("is_fallback")
        else f"YOUR PORTFOLIO MODEL '{card['name']}' from {card['source_course']}."
    )
    lines = [
        header,
        f"  directory   : {base}",
        f"  artifact    : {card['artifact']}  ({card['framework']})",
        f"  task        : {card['task']}  ->  {len(card['class_names'])} classes "
        f"{card['class_names']}",
        f"  features    : {len(card['feature_names'])} "
        f"(first three: {card['feature_names'][:3]})",
        f"  {metric.get('name', 'score')}    : {metric.get('value')} on {metric.get('split')}",
    ]
    if card.get("is_fallback"):
        lines.append(
            "  Export your own model from AIAT 114 or AIAT 122 and re-run: "
            "see Course 11/PORTFOLIO_MODEL.md"
        )
    return "\n".join(lines)


def schema_fields(card: dict) -> list[tuple[str, str]]:
    """Turn `feature_names` into (python_identifier, original_name) pairs.

    Real feature names contain spaces, dots and slashes ("mean radius"), which
    cannot be Pydantic field names — so the API slugifies them, and the card
    keeps the mapping back to the training columns.
    """
    pairs, seen = [], {}
    for original in card["feature_names"]:
        field = re.sub(r"\W+", "_", str(original).strip().lower()).strip("_")
        if not field or field[0].isdigit():
            field = f"f_{field}"
        if field in seen:
            raise ValueError(
                f"Feature names {seen[field]!r} and {str(original)!r} both become the "
                f"API field '{field}'. Rename one of them in your training data and "
                "re-export — an API cannot have two fields with the same name."
            )
        seen[field] = str(original)
        pairs.append((field, str(original)))
    return pairs
