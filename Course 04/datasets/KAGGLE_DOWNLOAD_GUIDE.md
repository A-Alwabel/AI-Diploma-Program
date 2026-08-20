# Kaggle Dataset Download Guide

**Note**: Currently we have **2 confirmed Kaggle datasets**. If other required datasets are also available on Kaggle, they will be added here for easier download from one platform.

---

## ✅ Confirmed Kaggle Datasets (5 Found!)

**Status**: 2 downloaded + 3 additional found on Kaggle = **5 total Kaggle datasets!**

### 1. Credit Card Fraud Detection (European Data)

**Kaggle Dataset Page**:  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

**Dataset ID**: `mlg-ulb/creditcardfraud`

**Direct Download (requires authentication)**:  
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/download

**Dataset Details**:
- **Name**: Credit Card Fraud Detection
- **Size**: ~145 MB
- **Files**: `creditcard.csv`
- **Used For**: Financial Investigations, Terrorism Financing, Counter-Espionage, Admin/Tech Crimes
- **Rows**: ~284,807 transactions
- **Features**: 30 features + 1 target (Class: 0=Normal, 1=Fraud)

---

### 2. US-Accidents Dataset

**Kaggle Dataset Page**:  
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

**Dataset ID**: `sobhanmoosavi/us-accidents`

**Direct Download (requires authentication)**:  
https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents/download

**Dataset Details**:
- **Name**: US Accidents (2016 - 2023)
- **Size**: ~300+ MB (large dataset)
- **Files**: `US_Accidents_March23.csv` (or latest version)
- **Used For**: Traffic Management
- **Rows**: ~4.5+ million records
- **Features**: 47 columns (location, weather, severity, etc.)

---

### 3. Global Terrorism Database (GTD) ✅ FOUND!

**Kaggle URL**: https://www.kaggle.com/datasets/START-UMD/gtd  
**Dataset ID**: `START-UMD/gtd`  
**Status**: ✅ **Available on Kaggle!**  
**Used For**: Terrorism & Financing  
**Download**: Same as other Kaggle datasets (manual or API)

---

### 4. US Border Crossing Data ✅ FOUND!

**Kaggle URL**: https://www.kaggle.com/datasets/akhilv11/us-border-crossing-data  
**Dataset ID**: `akhilv11/us-border-crossing-data`  
**Status**: ✅ **Available on Kaggle!**  
**Used For**: Border Security  
**Download**: Same as other Kaggle datasets (manual or API)

---

### 5. 911 Calls / Emergency Response ✅ FOUND!

**Kaggle URL**: https://www.kaggle.com/datasets/mchirico/montcoalert  
**Dataset ID**: `mchirico/montcoalert`  
**Status**: ✅ **Available on Kaggle!**  
**Used For**: Emergency Response  
**Description**: Montgomery County 911 emergency calls  
**Download**: Same as other Kaggle datasets (manual or API)

---

## 🔍 Still Need to Check (2)

### 3. Global Terrorism Database (GTD)

**Current Source**: START, University of Maryland  
**Kaggle Status**: ⚠️ **CHECK KAGGLE**  
**Search**: "global terrorism database" or "GTD" on Kaggle  
**Used For**: Terrorism & Financing

**If on Kaggle**: Add URL here

---

### 4. UNSW-NB15 (Cybersecurity)

**Current Source**: UNSW Canberra, Australia  
**Kaggle Status**: ⚠️ **CHECK KAGGLE**  
**Search**: "UNSW-NB15" on Kaggle  
**Used For**: Cyber Threats, Communication Threats

**If on Kaggle**: Add URL here

---

### 5. CICIDS2017 (Cybersecurity)

**Current Source**: Canadian Institute for Cybersecurity  
**Kaggle Status**: ⚠️ **CHECK KAGGLE**  
**Search**: "CICIDS2017" on Kaggle  
**Used For**: Cyber Threats, Communication Threats

**If on Kaggle**: Add URL here

---

### 6. 911 Calls (Emergency Response)

**Current Source**: data.gov (Montgomery County, Seattle)  
**Kaggle Status**: ⚠️ **CHECK KAGGLE**  
**Search**: "911 calls" or "emergency calls" on Kaggle  
**Used For**: Emergency Response

**If on Kaggle**: Add URL here

---

### 7. Border Crossing Data

**Current Source**: data.gov, BTS, CBP  
**Kaggle Status**: ⚠️ **CHECK KAGGLE**  
**Search**: "border crossing" or "immigration" on Kaggle  
**Used For**: Border Security

**If on Kaggle**: Add URL here

---

## 📥 Download Methods

### Method 1: Manual Download via Web Browser (EASIEST)

#### Step 1: Create Kaggle Account
1. Go to: https://www.kaggle.com/account/register
2. Sign up with email (free account)
3. Verify your email

#### Step 2: Download Confirmed Datasets

**Credit Card Fraud**:
1. Go to: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
2. Click the **"Download"** button (top right)
3. Save the ZIP file
4. Extract: `creditcard.csv`
5. Copy to: `Course 04/datasets/raw/creditcard_fraud.csv`

**US-Accidents**:
1. Go to: https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents
2. Click the **"Download"** button (top right)
3. Save the ZIP file (may take a while - large file)
4. Extract: `US_Accidents_March23.csv` (or latest filename)
5. Copy to: `Course 04/datasets/raw/us_accidents.csv`

---

### Method 2: Kaggle API (AUTOMATED - Recommended for Developers)

#### Step 1: Install Kaggle API
```bash
pip install kaggle
```

#### Step 2: Get API Credentials
1. Go to: https://www.kaggle.com/settings
2. Scroll to **"API"** section
3. Click **"Create New Token"**
4. This downloads `kaggle.json` file

#### Step 3: Set Up Credentials

**Linux/Mac**:
```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

**Windows**:
```bash
mkdir C:\Users\<YourUsername>\.kaggle
move %USERPROFILE%\Downloads\kaggle.json C:\Users\<YourUsername>\.kaggle\
# Set permissions: Right-click kaggle.json → Properties → Security → Advanced
```

#### Step 4: Download Datasets via API

```bash
# Navigate to datasets directory
cd "Course 04/datasets/raw"

# Download Credit Card Fraud
kaggle datasets download -d mlg-ulb/creditcardfraud -p .
unzip creditcardfraud.zip
mv creditcard.csv creditcard_fraud.csv
rm creditcardfraud.zip

# Download US-Accidents
kaggle datasets download -d sobhanmoosavi/us-accidents -p .
unzip us-accidents.zip
# Rename if needed (check actual filename)
# mv US_Accidents_March23.csv us_accidents.csv
rm us-accidents.zip
```

---

## 📋 Quick Reference - Confirmed URLs

| Dataset | Kaggle Page URL | Dataset ID | Download Size |
|---------|----------------|------------|---------------|
| **Credit Card Fraud** | https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud | `mlg-ulb/creditcardfraud` | ~145 MB |
| **US-Accidents** | https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents | `sobhanmoosavi/us-accidents` | ~300+ MB |

---

## 🔧 Troubleshooting

### Issue: "403 Forbidden" or "Permission Denied"
**Solution**: Make sure you:
1. Have a Kaggle account
2. Are logged in
3. Have accepted the dataset's terms of use (click "I Understand and Accept" on dataset page)
4. For API: Have valid `kaggle.json` credentials

### Issue: "Dataset not found"
**Solution**: 
- Verify the dataset ID is correct
- Check if the dataset is still public
- Try accessing via web browser first

### Issue: Download is slow
**Solution**:
- Kaggle downloads can be slow for large files
- US-Accidents is ~300+ MB, be patient
- Consider downloading during off-peak hours

### Issue: "kaggle: command not found"
**Solution**: 
```bash
pip install kaggle
# Or
pip3 install kaggle
```

---

## ✅ Verification After Download

After downloading, verify the files:

```python
import pandas as pd
import os

datasets_dir = 'datasets/raw/'

files_to_check = {
    'creditcard_fraud.csv': 'Credit Card Fraud',
    'us_accidents.csv': 'US Accidents'
}

for filename, name in files_to_check.items():
    filepath = os.path.join(datasets_dir, filename)
    if os.path.exists(filepath):
        try:
            df = pd.read_csv(filepath, nrows=5)
            full_df = pd.read_csv(filepath)
            print(f"✅ {name}")
            print(f"   Rows: {full_df.shape[0]:,}")
            print(f"   Columns: {full_df.shape[1]}")
            print(f"   Size: {os.path.getsize(filepath) / (1024*1024):.1f} MB")
        except Exception as e:
            print(f"❌ {name}: Error - {e}")
    else:
        print(f"❌ {name}: File not found")
```

---

## 📝 Checklist

- [ ] Create Kaggle account
- [ ] Install Kaggle API (optional, for automated download)
- [ ] Download Credit Card Fraud dataset
- [ ] Download US-Accidents dataset
- [ ] **(Optional) Check Kaggle for other datasets** (GTD, UNSW-NB15, CICIDS2017, 911 Calls, Border Data)
- [ ] Verify files are in `datasets/raw/` directory
- [ ] Verify files can be read with pandas

---

## 🚀 Quick Start (Recommended)

**For Quick Manual Download**:
1. Create Kaggle account: https://www.kaggle.com/account/register
2. Visit dataset pages and click "Download"
3. Extract and move to `datasets/raw/`

**For Automated Download**:
1. Install Kaggle API: `pip install kaggle`
2. Set up credentials (download `kaggle.json`)
3. Use the Python script: `python download_kaggle_datasets.py`

---

**Note**: Currently **2 confirmed Kaggle datasets**. If other required datasets (GTD, UNSW-NB15, CICIDS2017, 911 Calls, Border Data) are also available on Kaggle, they can be added to this guide for easier download from one platform.

---

**Last Updated**: Current Session