# Your Portfolio Model — the one artifact you carry through AIAT 125

In every other course you finished when the model was good. This course starts there.

AIAT 125 is about **deployment**, and deployment means taking a model that someone
already trained and getting it in front of real callers. If this course trained its
own throwaway classifier in every notebook, you would never do the actual job: receive
an artifact, read what it expects, and put it online without breaking it.

So you bring your own. One model, exported once, deployed over and over — as a Flask
API, as a FastAPI service, inside a Docker image.

> **Haven't got one yet? You are not blocked.** Every notebook that needs a model
> builds a **named fallback** — [`wdbc-baseline`](#4-the-named-fallback-wdbc-baseline) —
> and prints, in its own output, that it is serving the fallback and not your work.
> Nothing here fails because you skipped this page. It just gets less interesting.

---

## 1. The contract

A *portfolio directory* holding exactly two files:

```
~/ai-diploma-portfolio/
├── model.joblib          the artifact   (or model.onnx, or model_scripted.pt)
└── model_card.json       the contract that makes the artifact servable
```

Set `AI_DIPLOMA_PORTFOLIO` if you want it somewhere else; otherwise every notebook
looks in `~/ai-diploma-portfolio`.

### Why two files and not one

`joblib.load(path)` hands you back an object that can `.predict()` — and tells you
nothing else. It will not tell you that column 3 has to be *mean area* and not *mean
perimeter*. Feed it a scrambled row and it returns a confident, wrong answer, with no
error anywhere. The card is the machine-readable answer to *"what does this thing
expect, and what do its outputs mean?"*

You have seen a first version of this idea already: **AIAT 115 Unit 5,
`08_deployment.ipynb`** pickled a model and wrote a `model_metadata.json` next to it,
recording the features, the metrics and the model type. This course makes that pairing
mandatory and adds the parts a serving stack actually needs.

### `model_card.json`

| Key | Type | What it is |
|---|---|---|
| `name` | str | short slug, e.g. `fraud-rf` |
| `source_course` | str | `AIAT 114` or `AIAT 122` |
| `source_notebook` | str | the notebook that trained it — so you can rebuild it |
| `framework` | str | `sklearn`, `onnx`, or `torchscript` |
| `artifact` | str | the model filename, next to the card |
| `task` | str | `classification` (see [limits](#5-limits-and-edge-cases)) |
| `feature_names` | list | the input columns **in the order the model consumes them** |
| `class_names` | list | human-readable label per class index |
| `sample_input` | list | one real held-out row — the request body every lesson smoke-tests with |
| `sample_batch` | list | up to 20 real held-out rows — the **golden set** |
| `sample_batch_predictions` | list | the class index the model returned for each golden row **at export time** |
| `metric` | dict | `{"name", "value", "split"}` — your honest held-out score |
| `is_fallback` | bool | `true` only for the course fallback |

The golden set is the part people skip and regret. Replay those 20 rows through any
serving stack you build; every answer must still match `sample_batch_predictions`. The
model file has not changed, so a mismatch means **your serving code** changed the
model's mind — a scrambled feature order, a scaler left behind in the training
notebook, a float parsed as a string. Unit 2's Flask notebook runs exactly this check.

---

## 2. Exporting from AIAT 114 (Course 04) — Machine Learning Algorithms

**Be aware of what Course 04 does and does not teach.** Course 04 trains a great many
models and saves **none** of them. The only persistence code anywhere in that course is
a pair of unimplemented stubs — `save_model()` and `save_pipeline()`, both marked
`TODO: Save model using joblib.dump()` — in
`Course 04/PROJECTS/01_ML_Pipeline/Template/ml_pipeline_template.py`. There is no
notebook to copy from. This section is that missing step.

Pick the classifier you are proudest of. Good candidates, all on real data:

| Notebook | Model | Data |
|---|---|---|
| `unit3-classification/examples/05_random_forest_naive_bayes.ipynb` | `rf` (RandomForest) | real credit-card fraud, genuinely imbalanced |
| `unit3-classification/examples/02_decision_trees.ipynb` | decision tree | real Titanic passengers, with real missing values |
| `unit3-classification/examples/03_svm.ipynb` | SVM | real CICIDS2017 network traffic — already fitted with `probability=True`, which is what lets it return confidences |

(`06_ensemble_methods_bagging_boosting.ipynb` trains on `load_breast_cancer` — the very
dataset behind the course fallback. A perfectly good model, but deploying it makes your
work indistinguishable from the fallback in every notebook's output.)

Avoid `unit5-model-selection/examples/01_grid_search.ipynb` as your source: that
notebook's own "reality check" section proves its target leaks through
`State_encoded`, which is why everything there scores ~100%. A leaking model is a bad
thing to spend five units deploying.

Open your chosen notebook, run it to the end, then add **one cell**:

```python
# Export this model for AIAT 125 (Course 11).
import sys
from pathlib import Path

for _d in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    if (_d / "Course 11" / "portfolio_model.py").exists():
        sys.path.insert(0, str(_d / "Course 11"))
        break
import portfolio_model as pf

pf.export_portfolio_model(
    rf,                                   # <- your fitted estimator or Pipeline
    X_test=X_test, y_test=y_test,         # <- the HELD-OUT split, not the training one
    feature_names=feature_cols,           # <- in the order the model consumes them
    class_names=["legitimate", "fraud"],
    name="fraud-rf",
    source_course="AIAT 114",
    source_notebook="Course 04/unit3-classification/examples/05_random_forest_naive_bayes.ipynb",
)
```

That call writes both files, scores the model **from the artifact on disk** (if
serialization lost something, you find out now rather than in production), records the
golden batch, and prints what it wrote.

**Scalers and encoders must travel with the model.** If your notebook does
`StandardScaler().fit_transform(X)` and then trains on the result, the artifact you
export contains the model but *not* the scaler — and the server will feed it raw,
unscaled numbers. Wrap them together before exporting:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

model = Pipeline([("scaler", StandardScaler()), ("clf", your_classifier)]).fit(X_train, y_train)
```

Now one `joblib.dump` captures the whole path from raw input to prediction, which is
the only thing an API can honestly promise.

---

## 3. Exporting from AIAT 122 (Course 08) — Deep Learning

Course 08 Unit 5 **does** teach export, four different ways:

| Notebook | What it saves | Servable on its own? |
|---|---|---|
| `01_model_optimization.ipynb` | Keras `model.save("...keras")` | Yes, with TensorFlow installed |
| `02_tensorflow_serving.ipynb` | `torch.save(model.state_dict(), ...)` | **No** — weights only |
| `02_tensorflow_serving.ipynb` | `torch.jit.script(model).save(...)` | **Yes** — graph + weights |
| `03_onnx_conversion.ipynb` | `torch.onnx.export(...)` | **Yes** — and framework-independent |
| `06_flask_fastapi_deployment.ipynb` | `torch.save(model.state_dict(), ...)` | **No** — weights only |

Use **ONNX** (first choice) or **TorchScript**. A `state_dict` is only a dictionary of
tensors: loading it requires the exact `nn.Module` class definition to be importable in
the serving process, which means your model architecture becomes a source-code
dependency of every container you build. TorchScript and ONNX carry the computation
graph inside the file, so the server needs no model code at all.

Export the file the way `03_onnx_conversion.ipynb` teaches, then hand it over:

```python
import sys
from pathlib import Path

for _d in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    if (_d / "Course 11" / "portfolio_model.py").exists():
        sys.path.insert(0, str(_d / "Course 11"))
        break
import portfolio_model as pf

import torch
model.eval()
torch.onnx.export(model, torch.randn(1, n_features), "/tmp/my_model.onnx",
                  input_names=["features"], output_names=["logits"],
                  dynamic_axes={"features": {0: "batch"}, "logits": {0: "batch"}},
                  opset_version=17)

pf.export_portfolio_model(
    "/tmp/my_model.onnx",                 # <- the PATH, for onnx / torchscript
    framework="onnx",
    X_test=X_test, y_test=y_test,         # <- already preprocessed exactly as at training
    feature_names=[f"pixel_{i}" for i in range(64)],
    class_names=[str(i) for i in range(10)],
    name="digits-mlp",
    source_course="AIAT 122",
    source_notebook="Course 08/unit5-deployment/examples/03_onnx_conversion.ipynb",
)
```

`dynamic_axes` on the batch dimension matters: without it the exported graph accepts
exactly one row per call forever, and Unit 2's batch-inference notebook has nothing to
batch.

**Your normalisation is part of the model too.** If you trained on
`StandardScaler().fit_transform(X)`, the scaler lives in your notebook and not in the
`.onnx` file. Either fold the normalisation into the network's first layer before
exporting, or record the scaler's `mean_` and `scale_` and apply them in the serving
app — and say which you did, in `source_notebook`. A network fed raw pixels when it was
trained on standardised ones does not crash. It just answers badly.

---

## 4. The named fallback: `wdbc-baseline`

If `model_card.json` is missing, `load_portfolio_model()` trains and exports
`wdbc-baseline` in its place, then says so in every notebook that uses it:

```
FALLBACK MODEL 'wdbc-baseline' — this is NOT your model.
```

- **Data:** the Wisconsin Diagnostic Breast Cancer study — 569 real biopsies, 30
  measured features, 2 classes (`malignant` / `benign`). It ships **inside
  scikit-learn**, so it needs no download, no internet, and no dataset folder. It runs
  on any machine that can run this course.
- **Model:** `Pipeline(StandardScaler, LogisticRegression)` — the scaler travels with
  the model, exactly as section 2 insists yours should.
- **Score:** 0.9825 accuracy on a stratified held-out 20% (`random_state=42`).
- **`sample_input`:** not the first test row and not the most confident one, but a
  correctly classified row at *median* confidence — so the lessons print a realistic
  probability instead of a saturated `1.00`.

It is a real model on real data, and it is deliberately not yours. Every lesson that
loads it prints `is_fallback: true` on its own `/health` or `/model-info` endpoint,
which is also the honest answer to the question a real on-call engineer asks first:
*which model is actually running in production right now?*

---

## 5. Limits and edge cases

**"My best model is a regressor."** The serving lessons need `predict_proba`, so the
contract is classification-only for now. Course 04 Unit 3 gave you four classifiers to
choose from; export one of those. (Your regressor is still the right choice for the
AIAT 126 graduation project if that is the problem you are solving.)

**"My model has 300 features."** Fine. The request schema is generated from the card at
runtime, so the API grows the fields it needs. Unit 1 prints a ready-to-paste `curl`
for your model rather than making you type them.

**"Two of my columns become the same API field."** `mean radius` and `mean-radius` both
slugify to `mean_radius`, and the exporter refuses rather than silently dropping one.
Rename a column and export again.

**"My artifact is 400 MB."** It will still serve, but notice what Unit 4 does with it:
every Docker build copies it into the image. That is the moment the optimisation
lessons from AIAT 122 Unit 5 — quantisation, pruning, distillation — stop being
academic.

**"I want to swap models mid-course."** Export again over the top. The notebooks read
the card fresh on every run, so the next cell you execute serves the new model.

---

## 6. Which AIAT 125 lessons consume your model

| Unit | Notebook | What it does with your artifact |
|---|---|---|
| 1 | `examples/01_model_serving_api.ipynb` | Loads it, generates a Pydantic schema from the card, serves `/predict` + `/health`, prints a `curl` for your model |
| 2 | `examples/01_flask_api_deployment.ipynb` | Serves it from Flask with hand-written validation, then replays the **golden batch** to prove the HTTP layer changed nothing |
| 2 | `examples/02_fastapi_deployment.ipynb` | Serves the same artifact from FastAPI; `/model-info` reports the card, `/openapi.json` documents *your* feature names |
| 4 | `examples/01_docker_deployment.ipynb` | Stages it into a build context, bakes it into an image, and proves the app runs standalone before building |

The model is held constant across all four, which is the point: every difference you
observe between Flask, FastAPI and a container is a property of the *serving layer*,
not of the model.

The remaining AIAT 125 notebooks still use their own demo models. Units 3 and 5 are the
open front — cloud endpoints, drift detection, retraining pipelines — and they are the
next lessons to move onto your artifact.

---

## 📚 References

1. Mitchell, M., Wu, S., Zaldivar, A., et al. (2019). *Model Cards for Model Reporting*. FAT\* '19. <https://arxiv.org/abs/1810.03993>
2. Sculley, D., Holt, G., Golovin, D., et al. (2015). *Hidden Technical Debt in Machine Learning Systems*. NeurIPS 28. <https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html>
3. Breck, E., Cai, S., Nielsen, E., Salib, M., & Sculley, D. (2017). *The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction*. IEEE Big Data. <https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/>
4. Paleyes, A., Urma, R.-G., & Lawrence, N. D. (2022). *Challenges in Deploying Machine Learning: A Survey of Case Studies*. ACM Computing Surveys 55(6). <https://arxiv.org/abs/2011.09926>
