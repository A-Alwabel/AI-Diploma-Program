# Cybersecurity Datasets - Download URLs

**Status**: ⚠️ These datasets are **NOT on Kaggle**, but available from original sources

---

## 📥 Download URLs

### 1. UNSW-NB15 (Cybersecurity - Network Traffic)

**❌ NOT on Kaggle** - Use original sources below

**Option 1: Official UNSW Source** (Recommended)
- **URL**: https://research.unsw.edu.au/projects/unsw-nb15-dataset
- **Description**: Official source from UNSW Canberra
- **Formats**: PCAP, BRO, Argus, CSV files
- **Status**: ✅ Available (may require registration)

**Option 2: Zenodo Repository** (Easier - CSV format)
- **URL**: https://zenodo.org/doi/10.5281/zenodo.10140548
- **Description**: CSV format, divided into parts
- **Format**: CSV (easier for ML)
- **Status**: ✅ Available

**Used For**: Cyber Threats, Communication Threats  
**Save As**: `unsw_nb15.csv` (or combine parts if multiple files)

---

### 2. CICIDS2017 (Cybersecurity - Intrusion Detection)

**❌ NOT on Kaggle** - Use original sources below

**Option 1: Official CIC Source** (Recommended)
- **URL**: https://www.unb.ca/cic/datasets/ids-2017.html
- **Description**: Official source from Canadian Institute for Cybersecurity
- **Formats**: PCAP, CSV files
- **Status**: ✅ Available (free download)

**Option 2: Hugging Face** (Easier - ML-ready format)
- **URL**: https://huggingface.co/datasets/c01dsnap/CIC-IDS2017
- **Description**: ML-ready format
- **Format**: Compatible with ML frameworks
- **Status**: ✅ Available

**Option 3: GitHub Repository**
- **URL**: https://github.com/rokibulroni/CIC-IDS-2017-Dataset
- **Description**: Pre-processed version on GitHub
- **Status**: ✅ Available

**Used For**: Cyber Threats, Communication Threats  
**Save As**: `cicids2017.csv` (or combine parts if multiple files)

---

## 📋 Download Instructions

### For UNSW-NB15:

1. **Recommended**: Use Zenodo (easier - CSV format)
   - Go to: https://zenodo.org/doi/10.5281/zenodo.10140548
   - Download CSV files
   - Combine if multiple parts
   - Save as: `Course 04/datasets/raw/unsw_nb15.csv`

2. **Alternative**: Use official UNSW source
   - Go to: https://research.unsw.edu.au/projects/unsw-nb15-dataset
   - Download CSV files
   - May require registration
   - Save as: `Course 04/datasets/raw/unsw_nb15.csv`

### For CICIDS2017:

1. **Recommended**: Use Hugging Face (easier)
   - Go to: https://huggingface.co/datasets/c01dsnap/CIC-IDS2017
   - Download dataset
   - Convert to CSV if needed
   - Save as: `Course 04/datasets/raw/cicids2017.csv`

2. **Alternative**: Use official CIC source
   - Go to: https://www.unb.ca/cic/datasets/ids-2017.html
   - Download CSV files
   - Combine if multiple parts
   - Save as: `Course 04/datasets/raw/cicids2017.csv`

---

## 📊 Summary

| Dataset | On Kaggle? | Best Download Source | URL |
|---------|------------|---------------------|-----|
| **UNSW-NB15** | ❌ No | Zenodo (CSV format) | https://zenodo.org/doi/10.5281/zenodo.10140548 |
| **CICIDS2017** | ❌ No | Hugging Face (ML-ready) | https://huggingface.co/datasets/c01dsnap/CIC-IDS2017 |

---

## ⚠️ Notes

- These datasets are **large** (several GB) - ensure sufficient disk space
- May take time to download
- Some sources may require registration (free)
- If multiple files, combine them into single CSV for notebooks

---

## ✅ After Download

Move files to: `Course 04/datasets/raw/`
- `unsw_nb15.csv`
- `cicids2017.csv`

---

**Last Updated**: Current Session
