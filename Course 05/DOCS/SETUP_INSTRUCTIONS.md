# Setup Instructions
## AIAT 115 - Scalable Data Science

This guide covers **local installation** and **troubleshooting**. For **Google Colab** (free GPU), see [COLAB_SETUP.md](COLAB_SETUP.md).

---

## 1. Prerequisites

- **Python 3.8+** (3.10 or 3.11 recommended)
- **pip** (usually included with Python)

Check your version:
```bash
python --version
```

---

## 2. Virtual environment

This course uses the **repository root virtual environment** (`.venv`) shared by all courses, exposed in Jupyter as the **"ai-diploma"** kernel.

```bash
# From the repository root:
python -m venv .venv

# Activate
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Register the Jupyter kernel (once)
python -m ipykernel install --user --name ai-diploma
```

---

## 3. Install dependencies

**From the Course 05 directory:**
```bash
pip install -r ../requirements.txt
```

**From the repository root:** use `requirements.txt` (no `../`).

---

## 4. Verify installation

```bash
pip check
```

You should see no broken dependencies. Try:

```python
import pandas, numpy, matplotlib, seaborn, sklearn
print("OK")
```

---

## 5. GPU (optional)

- **Without GPU:** All notebooks work with pandas (CPU). No extra setup.
- **With NVIDIA GPU:** See [COLAB_SETUP.md](COLAB_SETUP.md) for RAPIDS, or install locally:
  ```bash
  conda install -c rapidsai -c conda-forge cudf cuml
  ```

---

## 6. Run notebooks

1. Start Jupyter from the repository root: `jupyter notebook` or `jupyter lab`
2. Open `unit1-introduction/examples/01_data_science_intro.ipynb`
3. Select the **ai-diploma** kernel (Kernel -> Change Kernel)

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `No module named 'X'` | Run `pip install -r ../requirements.txt` (from Course 05) or `pip install -r requirements.txt` (from repo root) |
| Python too old | Install 3.10+ from [python.org](https://www.python.org/downloads/) |
| Conflicts | Use a virtual environment (Step 2) |
| Colab / GPU | See [COLAB_SETUP.md](COLAB_SETUP.md) |

---

**See also:** [COLAB_SETUP.md](COLAB_SETUP.md) for Google Colab and GPU setup.