# Cross-Platform Compatibility Guide | دليل التوافق بين المنصات

## Overview | نظرة عامة

This guide ensures the AI Diploma Program works correctly on **Windows, macOS, and Linux** systems with different Python environments.

---

## ✅ Compatibility Features | ميزات التوافق

### 1. Line Endings | نهايات الأسطر
- **All text files use LF (Unix-style) line endings**
- Configured via `.gitattributes` file
- Works correctly on all operating systems

### 2. Path Handling | التعامل مع المسارات
- **Use `pathlib` or `os.path.join()`** for file paths
- Never use hardcoded paths like `/Users/` or `C:\`
- All examples use relative paths

### 3. Python Version | إصدار Python
- **Python 3.8+ required** (3.10 or 3.11 recommended)
- Compatible with all Python distributions:
  - CPython (standard)
  - Anaconda
  - Miniconda
  - PyPy (where applicable)

### 4. OS-Specific Files | الملفات الخاصة بنظام التشغيل
- `.DS_Store` (macOS) - **ignored**
- `Thumbs.db` (Windows) - **ignored**
- `.venv/` and `venv/` - **ignored**
- `__pycache__/` - **ignored**

---

## 🛠️ Setup for Different OS | الإعداد لأنظمة مختلفة

### Windows | ويندوز

```bash
# 1. Install Python 3.10 or 3.11
# Download from python.org

# 2. Open Command Prompt or PowerShell
# Navigate to project directory
cd "C:\path\to\AI Diploma"

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment
venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt
```

**Note:** Use quotes around paths with spaces: `"Course 04"`

---

### macOS | ماك

```bash
# 1. Install Python (if not already installed)
brew install python@3.11
# OR download from python.org

# 2. Open Terminal
# Navigate to project directory
cd "/path/to/AI Diploma"

# 3. Create virtual environment
python3 -m venv venv

# 4. Activate virtual environment
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt
```

---

### Linux | لينكس

```bash
# 1. Install Python (if not already installed)
sudo apt-get update
sudo apt-get install python3.11 python3-pip python3-venv

# 2. Open Terminal
# Navigate to project directory
cd "/path/to/AI Diploma"

# 3. Create virtual environment
python3 -m venv venv

# 4. Activate virtual environment
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt
```

---

## 📁 Directory Names with Spaces | أسماء المجلدات مع المسافات

Some course directories have spaces in their names:
- `Course 04/`
- `Course 05/`
- `Course 06/`

### Windows:
```cmd
cd "Course 04"
```

### macOS/Linux:
```bash
cd "Course 04"
# OR
cd Course\ 04
```

---

## 🐍 Python Environment Best Practices | أفضل ممارسات بيئة Python

### 1. Always Use Virtual Environments
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Check Python Version
```bash
python --version
# Should be 3.8 or higher
```

---

## ⚠️ Common Issues and Solutions | المشاكل الشائعة والحلول

### Issue 1: Module Not Found
**Solution:**
```bash
# Make sure virtual environment is activated
# Reinstall requirements
pip install -r requirements.txt
```

### Issue 2: Permission Denied (Linux/macOS)
**Solution:**
```bash
# Don't use sudo with pip in virtual environment
# If needed, fix permissions:
chmod +x venv/bin/python
```

### Issue 3: Path Not Found (Windows)
**Solution:**
- Use quotes around paths with spaces
- Use forward slashes or double backslashes: `path/to/file` or `path\\to\\file`
- Better: Use `pathlib.Path()` or `os.path.join()`

### Issue 4: Line Ending Warnings (Git)
**Solution:**
- Already handled by `.gitattributes`
- If you see warnings, run:
```bash
git config core.autocrlf input  # macOS/Linux
git config core.autocrlf true   # Windows
```

---

## 🔧 Configuration Files | ملفات الإعداد

### `.gitattributes`
- Ensures consistent line endings across platforms
- Automatically handles text vs binary files

### `.gitignore`
- Excludes OS-specific files
- Prevents committing unnecessary files

### `requirements.txt`
- Lists all Python dependencies
- Works with pip on all platforms

---

## 📝 Code Examples | أمثلة الكود

### ✅ Good: Cross-Platform Path Handling
```python
from pathlib import Path

# Works on all platforms
data_path = Path("data") / "dataset.csv"
# Or
import os
data_path = os.path.join("data", "dataset.csv")
```

### ❌ Bad: Platform-Specific Paths
```python
# DON'T DO THIS:
data_path = "/Users/username/data/dataset.csv"  # macOS only
data_path = "C:\\Users\\username\\data\\dataset.csv"  # Windows only
```

### ✅ Good: Python Version Check
```python
import sys
if sys.version_info < (3, 8):
    raise RuntimeError("Python 3.8+ required")
```

---

## 🧪 Testing Your Setup | اختبار إعدادك

### Test 1: Python Version
```bash
python --version
# Should show 3.8.x, 3.9.x, 3.10.x, or 3.11.x
```

### Test 2: Import Key Libraries
```python
import numpy
import pandas
import matplotlib
import sklearn
print("All libraries imported successfully!")
```

### Test 3: Run Example Script
```bash
cd "Course 04/unit1-data-processing/examples"
python 01_data_loading_exploration.py
```

---

## 📚 Additional Resources | موارد إضافية

- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [pathlib Documentation](https://docs.python.org/3/library/pathlib.html)
- [Cross-Platform Python Guide](https://docs.python.org/3/using/windows.html)

---

## ✅ Verification Checklist | قائمة التحقق

Before starting, verify:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Can navigate to course directories
- [ ] Can run example Python scripts
- [ ] No import errors

---

**Last Updated:** 2025  
**Compatible with:** Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)

