# Course 08 – Run Requirements

Use this as the single reference for **how to run** Course 08 notebooks and code.

**Framework:** All notebooks use **PyTorch**. TensorFlow is no longer required. Install PyTorch for full coverage (see Dependencies below).

---

## Python

- **Version:** Python 3.8+ (3.10 or 3.11 recommended).
- **Check:** `python --version`

---

## Dependencies

Course 08 uses the **root AI Diploma `requirements.txt`** when present. For Course 08 specifically you need at least:

```bash
pip install numpy matplotlib
pip install torch torchvision   # PyTorch (all notebooks)
pip install scikit-learn
pip install fastapi uvicorn     # Unit 5 deployment
pip install onnx onnxruntime    # Unit 5 ONNX
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

- **Local:** NVIDIA GPU with CUDA; install `torch` with GPU support.
- **Free cloud:** Use **Google Colab** (see `DOCS/COLAB_SETUP.md`). Enable GPU: Runtime → Change runtime type → GPU.

---

## Verifying setup

```python
import numpy as np
import torch
print("PyTorch:", torch.__version__)
import torchvision
print("torchvision:", torchvision.__version__)
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
| **ModuleNotFoundError** (e.g. `No module named 'torch'`) | Install dependencies: `pip install torch torchvision` (see Dependencies above). |
| **Kernel crash on macOS** | This course requires PyTorch only. Avoid installing TensorFlow on macOS Python 3.9. Run `pip uninstall tensorflow` if installed. |
| **Training very slow** | Enable GPU (Colab: Runtime → Change runtime type → GPU). On CPU, use fewer epochs or a smaller data subset. |

---

**Last updated:** 2025-02-07
