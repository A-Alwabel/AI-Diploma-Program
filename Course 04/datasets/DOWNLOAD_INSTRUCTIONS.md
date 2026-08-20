# Dataset Download Instructions

This document provides instructions for downloading all datasets used in Course 04 notebooks.

---

## ✅ Direct Download (Already Done)

These datasets are downloaded automatically or available via direct URL:

1. **Crime Statistics** (`crime_statistics.csv`) ✅
   - Source: GitHub (selva86/datasets) - USArrests dataset
   - Status: ✅ **VERIFIED WORKING** - Available in `datasets/raw/`
   - URL: `https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv`
   - **Dataset**: US State-level crime statistics (State, Murder, Assault, UrbanPop, Rape)
   - **Note**: Using USArrests as verified alternative (original datasciencedojo URL returned 404)
   - **Use**: Internal Intelligence, Internal Security

2. **Titanic Dataset** (`titanic.csv`)
   - Source: GitHub (datasciencedojo/datasets)
   - Status: ✅ Available in `datasets/raw/`
   - URL: `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`

---

## 📥 Manual Download Required

### 3. Credit Card Fraud Detection (European Data)

**Source**: Kaggle  
**URL**: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud  
**Used For**: Financial Investigations, Terrorism Financing, Counter-Espionage, Admin/Tech Crimes

**Download Steps**:
1. Create a free Kaggle account: https://www.kaggle.com/account/register
2. Go to the dataset page: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
3. Click "Download" button
4. Extract the ZIP file
5. Copy `creditcard.csv` to `Course 04/datasets/raw/creditcard_fraud.csv`

**Alternative (Kaggle API)**:
```bash
# Install Kaggle API: pip install kaggle
# Set up API credentials (see Kaggle account settings)
kaggle datasets download -d mlg-ulb/creditcardfraud -p datasets/raw/
unzip datasets/raw/creditcardfraud.zip -d datasets/raw/
mv datasets/raw/creditcard.csv datasets/raw/creditcard_fraud.csv
```

---

### 4. US-Accidents Dataset

**Source**: Kaggle  
**URL**: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents  
**Used For**: Traffic Management

**Download Steps**:
1. Go to: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents
2. Click "Download" button
3. Extract the ZIP file
4. Copy `US_Accidents_March23.csv` to `Course 04/datasets/raw/us_accidents.csv`

**Alternative (Kaggle API)**:
```bash
kaggle datasets download -d sobhanmoosavi/us-accidents -p datasets/raw/
unzip datasets/raw/us-accidents.zip -d datasets/raw/
# Rename to us_accidents.csv if needed
```

---

### 5. Global Terrorism Database (GTD)

**Source**: START, University of Maryland  
**URL**: https://www.start.umd.edu/gtd/  
**Used For**: Terrorism & Financing

**Download Steps**:
1. Go to: https://www.start.umd.edu/gtd/
2. Click "Download GTD" (free registration required for educational use)
3. Register/login with your email
4. Download the dataset (Excel or CSV format)
5. If Excel, convert to CSV or use pandas to read Excel
6. Save as `Course 04/datasets/raw/global_terrorism_database.csv`

**Note**: GTD is updated regularly. Use the most recent version available.

---

### 6. UNSW-NB15 (Australia - Cybersecurity)

**Source**: UNSW Canberra, Australia  
**URL**: https://research.unsw.edu.au/projects/unsw-nb15-dataset  
**Used For**: Cyber Threats, Communication Threats, Counter-Espionage

**Download Steps**:
1. Go to: https://research.unsw.edu.au/projects/unsw-nb15-dataset
2. Follow the download instructions on the website
3. Download the dataset files (may require registration)
4. Extract and process according to UNSW documentation
5. Combine/process CSV files as needed
6. Save main dataset as `Course 04/datasets/raw/runsw_nb15.csv`

**Alternative Sources**:
- Also available on Kaggle: https://www.kaggle.com/datasets/mrwellsdavid/unsw-nb15
- Direct download link (if available): Check UNSW website for latest links

---

### 7. CICIDS2017 (Canada - Cybersecurity)

**Source**: Canadian Institute for Cybersecurity  
**URL**: https://www.unb.ca/cic/datasets/ids-2017.html  
**Used For**: Cyber Threats, Communication Threats

**Download Steps**:
1. Go to: https://www.unb.ca/cic/datasets/ids-2017.html
2. Click on download links for the dataset files
3. Download all CSV files (multiple files may be provided)
4. Combine or use individual files as needed
5. Save main dataset as `Course 04/datasets/raw/cicids2017.csv`

**Note**: This is a large dataset. Ensure you have sufficient disk space.

---

### 8. 911 Calls (Montgomery County, MD)

**Source**: data.gov / Montgomery County Open Data  
**Used For**: Emergency Response

**Download Steps**:
1. Go to Montgomery County Open Data Portal or data.gov
2. Search for "Fire and Rescue Service Calls" or "911 Calls"
3. Download CSV file
4. Save as `Course 04/datasets/raw/montgomery_911_calls.csv`

**Alternative (Seattle)**:
- Seattle Open Data: data.seattle.gov
- Search for "Real Time Fire 911 Calls"
- Download CSV
- Save as `Course 04/datasets/raw/seattle_911_calls.csv`

---

### 9. BTS/CBP Border Crossing Data

**Source**: Bureau of Transportation Statistics / US Customs and Border Protection  
**URLs**: 
- BTS: https://www.bts.gov/browse-statistical-products-and-data/border-crossing-data
- CBP: https://www.cbp.gov/newsroom/stats/cbp-public-data-portal  
**Used For**: Border Security

**Download Steps**:
1. **BTS Border Data**:
   - Go to: https://www.bts.gov/browse-statistical-products-and-data/border-crossing-data
   - Select "Border Crossing/Entry Data"
   - Download CSV/Excel file
   - Save as `Course 04/datasets/raw/bts_border_crossings.csv`

2. **CBP Border Data**:
   - Go to: https://www.cbp.gov/newsroom/stats/cbp-public-data-portal
   - Navigate to border statistics
   - Download available CSV/Excel files
   - Save as `Course 04/datasets/raw/cbp_border_data.csv`

---

## 📋 Download Checklist

- [x] Crime Statistics (direct URL - auto-downloaded)
- [x] Titanic (direct URL - auto-downloaded)
- [ ] Credit Card Fraud (Kaggle - manual download)
- [ ] US-Accidents (Kaggle - manual download)
- [ ] Global Terrorism Database (GTD - registration + download)
- [ ] UNSW-NB15 (UNSW website - download)
- [ ] CICIDS2017 (CIC website - download)
- [ ] 911 Calls (data.gov - download)
- [ ] BTS/CBP Border Data (data.gov - download)

---

## 🔧 Post-Download Verification

After downloading, verify each dataset:

```python
import pandas as pd
import os

datasets_dir = 'datasets/raw/'
files = {
    'crime_statistics.csv': 'Crime Statistics',
    'titanic.csv': 'Titanic',
    'creditcard_fraud.csv': 'Credit Card Fraud',
    'us_accidents.csv': 'US Accidents',
    'global_terrorism_database.csv': 'Global Terrorism Database',
    'unsw_nb15.csv': 'UNSW-NB15',
    'cicids2017.csv': 'CICIDS2017',
    'montgomery_911_calls.csv': '911 Calls',
    'bts_border_crossings.csv': 'Border Data'
}

for filename, name in files.items():
    filepath = os.path.join(datasets_dir, filename)
    if os.path.exists(filepath):
        try:
            df = pd.read_csv(filepath, nrows=5)
            print(f"✅ {name}: {len(df.columns)} columns, shape OK")
        except Exception as e:
            print(f"⚠️  {name}: Error reading - {e}")
    else:
        print(f"❌ {name}: File not found")
```

---

## 📝 Notes

1. **Kaggle Datasets**: Require free Kaggle account. Consider using Kaggle API for automated downloads.
2. **Large Datasets**: Some datasets (US-Accidents, CICIDS2017) are large. Ensure sufficient disk space.
3. **Registration**: GTD and UNSW-NB15 may require registration (free for educational use).
4. **Data Updates**: Datasets may be updated. Use most recent versions when available.
5. **Privacy**: All datasets listed are publicly available and suitable for educational use.

---

**Last Updated**: Current Session
