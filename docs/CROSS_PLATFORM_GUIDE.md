# Cross-Platform Compatibility Guide

The AI Diploma program works on **Windows, macOS, and Linux**. This guide
covers the differences that matter.

**Last Updated:** 2026-08

---

## Compatibility Features

### Line endings

- All text files use LF (Unix-style) line endings, enforced by `.gitattributes`
- Works correctly on all operating systems

### Path handling

- Notebooks use relative paths and `pathlib`/`os.path.join()`
- No hardcoded absolute paths like `/Users/...` or `C:\...`

### Python

- Use a recent Python 3 (see [SETUP_GUIDE.md](SETUP_GUIDE.md) for the
  reference versions, including the separate Python 3.13 `tfenv` environment
  for TensorFlow notebooks)
- Works with CPython from python.org, Homebrew, or your distro's packages

### OS-specific files (ignored by git)

- `.DS_Store` (macOS), `Thumbs.db` (Windows)
- `.venv/`, `venv/`, `__pycache__/`

---

## Setup per Operating System

The steps are the same everywhere; only activation differs.

### Windows

```cmd
cd "C:\path\to\AI Diploma"
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### macOS

```bash
brew install python            # or download from python.org
cd "/path/to/AI Diploma"
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Linux

```bash
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
cd "/path/to/AI Diploma"
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Then register the kernel on every platform:

```bash
python -m ipykernel install --user --name ai-diploma --display-name "AI Diploma"
```

---

## Directory Names with Spaces

Every course directory has a space in its name (`Course 01` … `Course 12`), and
the repository root may too (`AI Diploma`). Always quote paths:

**Windows:**

```cmd
cd "Course 04"
```

**macOS/Linux:**

```bash
cd "Course 04"
# or
cd Course\ 04
```

---

## Common Issues and Solutions

### Module not found

```bash
# Activate the venv first, then:
pip install -r requirements.txt
```

### Permission denied (Linux/macOS)

- Never use `sudo pip` — activate the virtual environment instead

### Path not found (Windows)

- Quote paths containing spaces
- In Python code, prefer `pathlib.Path()` or `os.path.join()`

### Git line-ending warnings

Handled by `.gitattributes`. If warnings persist:

```bash
git config core.autocrlf input   # macOS/Linux
git config core.autocrlf true    # Windows
```

---

## Cross-Platform Code Patterns

### Good: portable paths

```python
from pathlib import Path
data_path = Path("data") / "dataset.csv"
```

### Bad: platform-specific paths

```python
data_path = "/Users/username/data/dataset.csv"        # macOS only
data_path = "C:\\Users\\username\\data\\dataset.csv"  # Windows only
```

---

## Testing Your Setup

### Test 1: Python version

```bash
python --version    # Windows
python3 --version   # macOS/Linux
```

### Test 2: Import key libraries

```bash
python -c "import numpy, pandas, matplotlib, sklearn; print('All libraries OK')"
```

### Test 3: Run the smoke-test notebook

Open `Course 01/unit1-ai-foundations/examples/01_ai_introduction.ipynb` in
Jupyter on the **AI Diploma** kernel and run all cells.

---

## Configuration Files

- **`.gitattributes`** — consistent line endings across platforms
- **`.gitignore`** — excludes OS-specific and environment files
- **`requirements.txt`** — the student environment baseline (all platforms)

---

## Additional Resources

- [Python venv tutorial](https://docs.python.org/3/tutorial/venv.html)
- [pathlib documentation](https://docs.python.org/3/library/pathlib.html)
- [SETUP_GUIDE.md](SETUP_GUIDE.md) — full environment setup, including `tfenv`
