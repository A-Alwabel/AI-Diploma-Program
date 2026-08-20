# Troubleshooting Guide

Common issues and solutions across all courses.

**Last Updated:** 2026-08

---

## Installation Issues

### "No module named 'X'"

```
ModuleNotFoundError: No module named 'pandas'
```

1. **Check the virtual environment is active**

   ```bash
   source .venv/bin/activate      # macOS/Linux
   .venv\Scripts\activate         # Windows
   ```

2. **Install the requirements**

   ```bash
   pip install -r requirements.txt
   ```

3. **Verify**

   ```bash
   python -c "import pandas; print('pandas OK')"
   ```

### "No module named 'tensorflow'"

This is expected on the main `ai-diploma` kernel — TensorFlow lives in the
separate **tfenv** environment (Python 3.13). Switch the notebook's kernel to
**Python (tfenv-TF)**: Kernel → Change Kernel. See
[SETUP_GUIDE.md](SETUP_GUIDE.md) for how to create the tfenv environment.

### Dependency conflicts

```
ERROR: pip's dependency resolver does not currently take into account...
```

1. Use a fresh virtual environment (never install into the system Python)
2. Re-install from the baseline: `pip install -r requirements.txt`
3. Check: `pip check`

---

## Notebook Issues

### Notebook won't run / kernel dies

1. **Check the kernel** — select **AI Diploma** (or **Python (tfenv-TF)** for
   TensorFlow notebooks in Courses 01 and 08)
2. **Restart the kernel** — Kernel → Restart
3. **Run cells in order** from the top (Shift+Enter); later cells depend on
   earlier ones
4. **Clear and restart** — Kernel → Restart & Clear Output, then run again

### Notebook is slow

1. Reduce dataset size while experimenting
2. For Courses 05/08/10, use Google Colab with a GPU
   (each has `DOCS/COLAB_SETUP.md`)
3. Prefer vectorized NumPy/pandas operations over Python loops

### Code looks right but errors anyway

1. Check for missing colons, parentheses, or wrong indentation
2. Verify variables are defined — run the earlier cells first
3. Confirm imports at the top of the notebook actually succeeded

---

## GPU Issues

### "CUDA out of memory"

1. Reduce the batch size (e.g. 64 → 16 or 8)
2. Clear GPU memory:

   ```python
   import torch
   torch.cuda.empty_cache()
   ```

3. Use a smaller model
4. Restart the runtime/kernel

### GPU not detected

1. **Colab:** Runtime → Change runtime type → GPU
2. Verify access:

   ```python
   import torch
   print(torch.cuda.is_available())
   ```

3. **Local:** check drivers with `nvidia-smi`; install the CUDA-enabled build
   of your framework

### RAPIDS/cuDF installation fails (Course 05)

1. **Use Google Colab** — see `Course 05/DOCS/COLAB_SETUP.md`
2. RAPIDS requires specific CUDA versions: <https://rapids.ai/>
3. All Course 05 cuDF notebooks have a pandas (CPU) fallback — you can complete
   the course without a GPU

---

## Data Issues

### "File not found"

1. Check your working directory:

   ```python
   import os
   print(os.getcwd())
   print(os.listdir('.'))
   ```

2. Notebook paths are relative to the notebook's own folder — launch Jupyter
   from the repository root and open the notebook in place
3. Some notebooks download data on first run — check the setup cell

### Memory errors with large datasets

1. Load in chunks:

   ```python
   chunks = pd.read_csv('large_file.csv', chunksize=10_000)
   df = pd.concat(chunks, ignore_index=True)
   ```

2. Course 05 covers Dask for out-of-core dataframes — see
   `Course 05/unit5-scaling/examples/02_dask_distributed.ipynb`

---

## Course-Specific Issues

### Course 01 and Course 08 (TensorFlow notebooks)

- **"No module named tensorflow"** → switch to the `tfenv` kernel (see above)
- **Training very slow (Course 08)** → use Colab with GPU:
  `Course 08/DOCS/COLAB_SETUP.md`

### Course 05 (Scalable Data Science)

- **cuDF not available** → use Colab (`Course 05/DOCS/COLAB_SETUP.md`) or the
  pandas fallback built into every cuDF notebook
- **PySpark issues** → PySpark needs Java; the notebook's setup cell explains

### Course 09 (Reinforcement Learning)

- **Rendering fails** → the environments use `gymnasium[classic-control]` with
  pygame; re-run `pip install -r requirements.txt`

### Course 10 (Generative AI)

- **GAN/VAE training extremely slow on CPU** → use Colab with GPU:
  `Course 10/DOCS/COLAB_SETUP.md`
- **Out of memory** → smaller model, lower image resolution, smaller batch

### Course 11 (Deploying AI Models)

- **Docker labs** → Docker is installed separately from Python; the course
  marks Docker steps as optional where a local alternative exists
- **Cloud labs** → credentials setup in `Course 11/DOCS/CLOUD_CREDENTIALS_SETUP.md`

---

## Colab-Specific Issues

### Session disconnected

1. Save frequently (File → Save) and download important outputs
2. Mount Google Drive to persist work
3. Runtime → Reconnect, then re-run the setup cells

### GPU quota exceeded

1. Free tier resets daily — wait and retry
2. Switch to CPU temporarily for non-training cells
3. Colab Pro offers more GPU time if you need it

---

## System-Specific Issues

### Windows

- **`pip` not found** → use `python -m pip`
- **Permission denied** → activate the venv; avoid installing system-wide
- **Paths with spaces** → quote them: `cd "Course 04"`

### macOS

- **`python` not found** → use `python3`
- **SSL certificate errors** → run
  `/Applications/Python 3.x/Install Certificates.command`

### Linux

- **Permission denied** → use a virtual environment; never `sudo pip`

---

## Learning Issues

### "I don't understand the notebook"

1. Check the unit README and course prerequisites
2. Re-run the earlier numbered examples in the unit — they build up to it
3. Follow the sequence: units 1 → 5, examples 01 → NN

### "The exercise is too difficult"

1. Re-study the unit's examples and modify them first
2. Break the exercise into the smallest possible steps
3. Attempt it fully, then compare with the solution **when your instructor
   releases it**
4. Ask your instructor or study group — see
   [COMMUNITY_RESOURCES.md](COMMUNITY_RESOURCES.md)

---

## Before Reporting an Issue

- [ ] Read the relevant section of this guide
- [ ] Verified the virtual environment is active
- [ ] Verified the correct kernel (`ai-diploma` / `tfenv`)
- [ ] Ran `pip check`
- [ ] Restarted the kernel and ran cells from the top
- [ ] Checked file paths and working directory

---

## Additional Resources

- [SETUP_GUIDE.md](SETUP_GUIDE.md) — environment and kernels
- [STUDENT_GUIDE.md](STUDENT_GUIDE.md) — how to work through the program
- [GPU_REQUIREMENTS_SUMMARY.md](GPU_REQUIREMENTS_SUMMARY.md) — GPU and Colab
- Python docs: <https://docs.python.org/> · pandas: <https://pandas.pydata.org/docs/> · NumPy: <https://numpy.org/doc/>
