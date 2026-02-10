# Course 08 – Run Requirements

Use this as the single reference for **how to run** Course 08 notebooks and code.

**TensorFlow vs PyTorch:** Most notebooks use **TensorFlow/Keras**. Unit 3 (e.g. BERT, some transformers) and a few others use **PyTorch**. Install both for full coverage (see Dependencies below).

---

## Python

- **Version:** Python 3.8+ (3.10 or 3.11 recommended).
- **Check:** `python --version`

---

## Dependencies

Course 08 uses the **root AI Diploma `requirements.txt`** when present. For Course 08 specifically you need at least:

```bash
pip install numpy matplotlib
pip install tensorflow   # or tensorflow-cpu
pip install torch torchvision   # for PyTorch examples
pip install scikit-learn
pip install fastapi uvicorn     # Unit 5 deployment
pip install onnx onnxruntime    # Unit 5 ONNX
```

For transformers/NLP (Unit 3):

```bash
pip install transformers datasets
```

For reinforcement learning (Unit 4, notebook `03_reinforcement_learning_...`):

```bash
pip install gymnasium
```

*(That notebook uses **gymnasium** only; the old `gym` package is not used there.)*

**Optional:** If a root `requirements.txt` exists at the AI Diploma folder, run:

```bash
pip install -r requirements.txt
```

---

## GPU (recommended)

- **Local:** NVIDIA GPU with CUDA; install `tensorflow` / `torch` with GPU support.
- **Free cloud:** Use **Google Colab** (see `DOCS/COLAB_SETUP.md`). Enable GPU: Runtime → Change runtime type → GPU.

---

## Verifying setup

```python
import numpy as np
import tensorflow as tf
print("TensorFlow:", tf.__version__)
# Optional:
import torch
print("PyTorch:", torch.__version__)
```

---

## Where curriculum details live

- **Course overview and units:** `README.md` (this course folder).
- **Slide ↔ notebook mapping:** `DOCS/EXAMPLES_ORDER.md`.
- **Institution slides (if used):** See `DOCS/INSTITUTION_SLIDES_COMPATIBILITY.md`.  
If `../DETAILED_UNIT_DESCRIPTIONS.md` or `COURSE_MAP.md` are not in your repo, use `README.md` and `DOCS/EXAMPLES_ORDER.md` as the source of truth.

---

## Common errors

| If you see… | Do this |
|-------------|--------|
| **CUDA out of memory** | Reduce batch size (e.g. 32 → 16), use a smaller model or subset of data, or enable GPU and restart runtime (Colab: Runtime → Restart). |
| **ModuleNotFoundError** (e.g. `No module named 'tensorflow'`) | Install dependencies: `pip install -r requirements.txt` or `pip install tensorflow torch` (see Dependencies above). |
| **charset_normalizer / md__mypyc** (TensorFlow import fails) | Run `pip install --upgrade charset-normalizer requests`, then restart the kernel. See `DOCS/COLAB_SETUP.md` (Troubleshooting). |
| **Training very slow** | Enable GPU (Colab: Runtime → Change runtime type → GPU). On CPU, use fewer epochs or a smaller data subset. |

---

**Last updated:** 2025-02-07
