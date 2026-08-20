# AI Diploma - Setup Guide

Complete environment setup for the AI Diploma program.

**Last Updated:** 2026-08

---

## Prerequisites

### System Requirements

- **Operating System:** Windows 10+, macOS, or Linux (Ubuntu 20.04+)
- **Python:** a recent Python 3 (the reference environment uses Python 3.14 for
  the main venv and Python 3.13 for the TensorFlow environment)
- **RAM:** 8 GB minimum (16 GB recommended for deep learning)
- **Storage:** at least 10 GB free
- **GPU:** optional — see [GPU_REQUIREMENTS_SUMMARY.md](GPU_REQUIREMENTS_SUMMARY.md)

### Required Knowledge

- Basic command line / terminal usage
- No programming experience needed for Course 01

---

## Installation Steps

### Step 1: Install Python

**Windows:**

1. Download Python 3 from [python.org](https://www.python.org/downloads/)
2. Run the installer and check "Add Python to PATH"
3. Verify: open Command Prompt and run `python --version`

**macOS:**

```bash
brew install python
python3 --version
```

**Linux:**

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

### Step 2: Create the virtual environment

From the repository root:

```bash
cd "/path/to/AI Diploma"
python3 -m venv .venv

# Activate it:
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

### Step 3: Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip check
```

### Step 4: Register the Jupyter kernel

```bash
python -m ipykernel install --user --name ai-diploma --display-name "AI Diploma"
```

All notebooks except the TensorFlow ones (see below) use this `ai-diploma` kernel.

### Step 5: Smoke test

Confirm the core libraries import:

```bash
python -c "import numpy, pandas, sklearn, matplotlib; print('Core libs OK')"
```

Then run one real notebook end-to-end:

```bash
jupyter lab "Course 01/unit1-ai-foundations/examples/01_ai_introduction.ipynb"
```

Select the **AI Diploma** kernel and run all cells. If it completes without
errors, your environment is ready.

---

## The TensorFlow environment ("tfenv")

TensorFlow does not publish a wheel for the main venv's Python version, so the
TensorFlow/Keras notebooks in **Course 01** and **Course 08** use a second,
separate environment on **Python 3.13** registered as the `tfenv` kernel:

```bash
# Requires a Python 3.13 interpreter installed on your system
python3.13 -m venv ~/venvs/ai-diploma-tf
source ~/venvs/ai-diploma-tf/bin/activate
pip install --upgrade pip
pip install tensorflow ipykernel numpy pandas matplotlib scikit-learn
python -m ipykernel install --user --name tfenv --display-name "Python (tfenv-TF)"
deactivate
```

When a notebook imports `tensorflow`, switch its kernel to **Python (tfenv-TF)**
(Jupyter: Kernel → Change Kernel). All other notebooks stay on `ai-diploma`.

---

## Course-Specific Notes

Most courses need nothing beyond `requirements.txt`. Exceptions and extras:

### Course 01 and Course 08 (TensorFlow notebooks)

- Use the `tfenv` kernel described above for notebooks that import TensorFlow.
- PyTorch notebooks in Course 08 run on the main `ai-diploma` kernel.

### Course 05: Scalable Data Science

- Dask and Plotly are already in `requirements.txt`.
- The cuDF/RAPIDS notebooks need an NVIDIA GPU — use Google Colab
  (see `Course 05/DOCS/COLAB_SETUP.md`). All of them have a pandas CPU fallback.

### Course 07: Natural Language Processing

- NLTK and spaCy are in `requirements.txt`; download their models once:

```bash
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt')"
```

### Course 09: Reinforcement Learning

- Uses `gymnasium[classic-control]` (already in `requirements.txt`), plus
  pygame and imageio for rendering. No Atari extras are required.

### Course 11: Deploying AI Models

- FastAPI, Flask, MLflow, ONNX, and boto3 are in `requirements.txt`.
- Docker is optional and installed separately: [docker.com](https://www.docker.com/)
- Cloud labs: see `Course 11/DOCS/CLOUD_CREDENTIALS_SETUP.md`.

---

## Verify Installation

Run this quick check (TensorFlow is intentionally not included — it lives in
`tfenv`):

```python
import sys
print("Python:", sys.version)

libraries = [
    "numpy", "pandas", "matplotlib", "seaborn", "sklearn",
    "torch", "transformers", "nltk", "spacy",
    "plotly", "gymnasium", "flask", "fastapi", "shap", "lime", "mlflow",
]

missing = []
for lib in libraries:
    try:
        __import__(lib)
        print("OK  ", lib)
    except ImportError:
        print("MISS", lib)
        missing.append(lib)

print("\nAll good!" if not missing else f"\nMissing: {', '.join(missing)}")
```

---

## Troubleshooting

**`pip` not found** — use `python -m pip` (or `pip3`).

**Permission errors** — make sure the virtual environment is activated; never
use `sudo pip`.

**Import errors inside notebooks** — the notebook is probably on the wrong
kernel. Select **AI Diploma** (or **Python (tfenv-TF)** for TensorFlow
notebooks) via Kernel → Change Kernel, then re-run.

**`No module named tensorflow`** — you are on the `ai-diploma` kernel; switch
to `tfenv` (see above).

For everything else, see [TROUBLESHOOTING_GUIDE.md](TROUBLESHOOTING_GUIDE.md).

---

## Next Steps

1. Complete the smoke test above
2. Open `Course 01/START_HERE.md` and follow it
3. Work through each course in order (01 → 12)
4. Track your progress with each course's `STUDENT_PROGRESS_CHECKLIST.md`
