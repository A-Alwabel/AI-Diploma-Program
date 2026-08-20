# Quick Download Guide - Cybersecurity Datasets

---

## 🚀 Quick Download - CICIDS2017 (Automated)

### Using Hugging Face Datasets Library:

```python
from datasets import load_dataset

# Download CICIDS2017
ds = load_dataset("c01dsnap/CIC-IDS2017")

# Convert to pandas DataFrame and save
df = ds['train'].to_pandas()  # or use the available split
df.to_csv('datasets/raw/cicids2017.csv', index=False)
```

### Or Use the Script:

```bash
cd "Course 04/datasets"
python download_cybersecurity_datasets.py
```

**Prerequisites**:
```bash
pip install datasets huggingface_hub
```

---

## 📥 Quick Download - UNSW-NB15 (Manual)

**Not available on Hugging Face** - Download manually:

1. **Best Option: Zenodo** (CSV format)
   - URL: https://zenodo.org/doi/10.5281/zenodo.10140548
   - Download CSV files
   - Combine if multiple parts
   - Save as: `datasets/raw/unsw_nb15.csv`

2. **Alternative: Official UNSW**
   - URL: https://research.unsw.edu.au/projects/unsw-nb15-dataset
   - Download CSV files
   - Save as: `datasets/raw/unsw_nb15.csv`

---

## ✅ After Download

Both files should be in: `Course 04/datasets/raw/`
- `cicids2017.csv`
- `unsw_nb15.csv`

---

**Last Updated**: Current Session
