# Course 08 – Run Requirements

Use this as the single reference for **how to run** Course 08 notebooks and code.

**Frameworks:** Course 08 uses **both TensorFlow/Keras and PyTorch**. Many notebooks show a concept in one or both frameworks; Unit 3 transformer notebooks use Hugging Face (PyTorch).

---

## Environment and kernels

- Use the repo root `.venv` and the **"ai-diploma"** Jupyter kernel for PyTorch notebooks.
- Notebooks that import **TensorFlow** run on the **"tfenv"** kernel — select it in Jupyter before running those notebooks.

## Python

- **Version:** Python 3.10 or 3.11 recommended.
- **Check:** `python --version`

---

## Dependencies

Install from the **root AI Diploma `requirements.txt`**:

```bash
pip install -r requirements.txt
```

For Course 08 specifically you need at least:

```bash
pip install numpy matplotlib scikit-learn
pip install torch torchvision   # PyTorch notebooks
pip install tensorflow          # TensorFlow notebooks (tfenv kernel)
pip install fastapi uvicorn     # Unit 5 deployment
pip install onnx onnxruntime    # Unit 5 ONNX
```

For reinforcement learning (Unit 4, notebook `03_reinforcement_learning_...`):

```bash
pip install gymnasium
```

*(That notebook uses **gymnasium**; the old `gym` package is not used there.)*

---

## GPU (recommended)

- **Local:** NVIDIA GPU with CUDA; install `torch` (and/or TensorFlow) with GPU support.
- **Free cloud:** Use **Google Colab** (see `COLAB_SETUP.md`). Enable GPU: Runtime → Change runtime type → GPU.

---

## Verifying setup

```python
import numpy as np
import torch
print("PyTorch:", torch.__version__)
```

On the tfenv kernel:

```python
import tensorflow as tf
print("TensorFlow:", tf.__version__)
```

---

## Where curriculum details live

- **Course overview and units:** `../README.md` (this course folder).
- **Slide ↔ notebook mapping:** `EXAMPLES_ORDER.md` (this folder); slide decks in `../PRESENTATIONS/SLIDES/`.

---

## Common errors

| If you see… | Do this |
|-------------|--------|
| **CUDA out of memory** | Reduce batch size (e.g. 32 → 16), use a smaller model or subset of data, or enable GPU and restart runtime (Colab: Runtime → Restart). |
| **ModuleNotFoundError** (e.g. `No module named 'torch'`) | Install dependencies (see Dependencies above) into the active environment. |
| **`import tensorflow` fails on the "ai-diploma" kernel** | Switch to the **"tfenv"** kernel — TensorFlow notebooks run there. |
| **charset_normalizer / md__mypyc error on TensorFlow import** | `pip install --upgrade charset-normalizer requests`, then restart the kernel (see `COLAB_SETUP.md`). |
| **Training very slow** | Enable GPU (Colab: Runtime → Change runtime type → GPU). On CPU, use fewer epochs or a smaller data subset. |
