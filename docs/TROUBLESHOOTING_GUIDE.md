# Troubleshooting Guide | دليل حل المشاكل
## Common Issues and Solutions Across All Courses

**Last Updated:** January 2025

---

## 🔧 Installation Issues | مشاكل التثبيت

### Problem: "No module named 'X'"

**Symptoms:**
```
ModuleNotFoundError: No module named 'pandas'
ImportError: No module named 'numpy'
```

**Solutions:**

1. **Check Virtual Environment**
   ```bash
   # Make sure virtual environment is activated
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

2. **Install Missing Library**
   ```bash
   pip install pandas numpy matplotlib seaborn
   # Or install all at once:
   pip install -r requirements.txt
   ```

3. **Verify Installation**
   ```bash
   pip list | grep pandas
   python -c "import pandas; print('✅ pandas installed')"
   ```

---

### Problem: "Python version too old"

**Symptoms:**
```
Python 3.7 or older
SyntaxError: invalid syntax (on newer Python features)
```

**Solutions:**

1. **Install Python 3.10 or 3.11**
   - Download from: https://www.python.org/downloads/
   - Check "Add Python to PATH" during installation

2. **Verify Version**
   ```bash
   python --version
   # Should show: Python 3.10.x or 3.11.x
   ```

3. **Update pip**
   ```bash
   python -m pip install --upgrade pip
   ```

---

### Problem: "Libraries conflict with each other"

**Symptoms:**
```
ERROR: pip's dependency resolver does not currently take into account...
Conflicting dependencies
```

**Solutions:**

1. **Use Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. **Update All Libraries**
   ```bash
   pip install --upgrade pip
   pip install --upgrade pandas numpy matplotlib seaborn scikit-learn
   ```

3. **Check for Conflicts**
   ```bash
   pip check
   ```

---

## 📓 Notebook Issues | مشاكل الدفاتر

### Problem: "Notebook won't run"

**Symptoms:**
- Cells don't execute
- Kernel keeps restarting
- "Kernel died" error

**Solutions:**

1. **Restart Kernel**
   - Jupyter: Kernel → Restart
   - Colab: Runtime → Restart runtime

2. **Check Python Kernel**
   - Make sure Python 3 kernel is selected
   - Jupyter: Kernel → Change kernel → Python 3

3. **Run Cells in Order**
   - Start from the first cell
   - Run cells sequentially (Shift+Enter)

4. **Clear Output and Restart**
   - Cell → All Output → Clear
   - Kernel → Restart & Clear Output

---

### Problem: "Notebook is slow"

**Symptoms:**
- Cells take very long to execute
- System becomes unresponsive

**Solutions:**

1. **Check Dataset Size**
   - Use smaller datasets for testing
   - Reduce number of rows/columns

2. **Enable GPU (if applicable)**
   - Course 05/08/10: Use Google Colab with GPU
   - See course-specific Colab setup guides

3. **Optimize Code**
   - Use vectorized operations (NumPy/Pandas)
   - Avoid loops when possible
   - Use appropriate data types

---

### Problem: "Notebook shows errors but code looks correct"

**Solutions:**

1. **Check for Syntax Errors**
   - Look for missing colons, parentheses, quotes
   - Check indentation

2. **Verify Variable Names**
   - Check for typos in variable names
   - Ensure variables are defined before use

3. **Check Import Statements**
   - Verify all imports are at the top
   - Check library names are correct

---

## 🖥️ GPU Issues | مشاكل GPU

### Problem: "CUDA out of memory"

**Symptoms:**
```
RuntimeError: CUDA out of memory
```

**Solutions:**

1. **Reduce Batch Size**
   ```python
   # Change from:
   batch_size = 64
   # To:
   batch_size = 16  # or 8, or 4
   ```

2. **Clear GPU Memory**
   ```python
   import torch
   torch.cuda.empty_cache()
   ```

3. **Use Smaller Models**
   - Use smaller model architectures
   - Reduce model complexity

4. **Restart Runtime**
   - Colab: Runtime → Restart runtime
   - Local: Restart Python kernel

---

### Problem: "GPU not detected"

**Symptoms:**
- Code runs on CPU instead of GPU
- No speedup from GPU

**Solutions:**

1. **Check GPU is Enabled (Colab)**
   - Runtime → Change runtime type → GPU
   - Verify: Runtime → Change runtime type shows "GPU"

2. **Verify GPU Access**
   ```python
   import torch
   print(torch.cuda.is_available())  # Should be True
   print(torch.cuda.get_device_name(0))  # Should show GPU name
   ```

3. **Install GPU Libraries**
   - Colab: Run Colab setup cell
   - Local: Install CUDA and GPU libraries

4. **Check CUDA Version**
   ```bash
   nvidia-smi  # Check CUDA version
   ```

---

### Problem: "RAPIDS/cuDF installation fails"

**Solutions:**

1. **Use Google Colab** (Recommended)
   - Colab has pre-configured GPU environment
   - Run Colab setup cell in notebook

2. **Check CUDA Compatibility**
   - RAPIDS requires specific CUDA versions
   - See: https://rapids.ai/start.html

3. **Install via Conda** (Local)
   ```bash
   conda install -c rapidsai -c conda-forge cudf cuml
   ```

---

## 📊 Data Issues | مشاكل البيانات

### Problem: "File not found" or "Dataset not found"

**Solutions:**

1. **Check File Path**
   ```python
   import os
   print(os.getcwd())  # Check current directory
   print(os.listdir('.'))  # List files in current directory
   ```

2. **Use Correct Path**
   ```python
   # Relative path:
   df = pd.read_csv('data/sample_data.csv')
   # Absolute path:
   df = pd.read_csv('/full/path/to/data.csv')
   ```

3. **Download Dataset**
   - Check if dataset needs to be downloaded
   - Follow dataset download instructions in notebook

---

### Problem: "Memory error when loading large dataset"

**Solutions:**

1. **Load Data in Chunks**
   ```python
   # Instead of:
   df = pd.read_csv('large_file.csv')
   # Use:
   chunk_list = []
   for chunk in pd.read_csv('large_file.csv', chunksize=10000):
       chunk_list.append(chunk)
   df = pd.concat(chunk_list, ignore_index=True)
   ```

2. **Use Dask or PySpark**
   - Course 05: Use Dask for large datasets
   - See: `Course 05/unit5-scaling/examples/14_dask_distributed.ipynb`

3. **Use GPU (if available)**
   - Course 05: Use cuDF for GPU-accelerated loading
   - See: `Course 05/unit2-cleaning/examples/07_cudf_import_export_gpu.ipynb`

---

## 🔗 Course-Specific Issues | مشاكل خاصة بالدورات

### Course 05 (Scalable Data Science):

**Problem:** "cuDF not available"
- **Solution:** Use Google Colab - See `Course 05/DOCS/COLAB_SETUP.md`
- **Alternative:** Use pandas (CPU) - all notebooks have fallbacks

**Problem:** "Dask/PySpark not working"
- **Solution:** Install Dask: `pip install dask`
- **Note:** PySpark requires Java - see notebook for setup

---

### Course 08 (Deep Learning):

**Problem:** "TensorFlow/PyTorch training very slow"
- **Solution:** Use Google Colab with GPU - See `Course 08/DOCS/COLAB_SETUP.md`
- **Note:** Training on CPU is 10-100x slower

**Problem:** "Model training fails"
- **Solution:** 
  1. Reduce batch size
  2. Use smaller model
  3. Check GPU memory

---

### Course 10 (Generative AI):

**Problem:** "GAN/VAE training extremely slow"
- **Solution:** Use Google Colab with GPU - See `Course 10/DOCS/COLAB_SETUP.md`
- **Warning:** Training on CPU can take days/weeks

**Problem:** "Stable Diffusion out of memory"
- **Solution:**
  1. Use smaller model
  2. Reduce image resolution
  3. Use Colab Pro (more GPU memory)

---

## 🌐 Colab-Specific Issues | مشاكل خاصة بـ Colab

### Problem: "Colab session disconnected"

**Solutions:**

1. **Save Work Frequently**
   - File → Save
   - Download important outputs

2. **Use Google Drive**
   - Mount Google Drive
   - Save notebooks to Drive

3. **Reconnect**
   - Runtime → Reconnect
   - Re-run setup cells

---

### Problem: "Colab GPU quota exceeded"

**Solutions:**

1. **Wait for Reset**
   - Free tier: Resets daily (~12 hours/day)
   - Check: Runtime → Change runtime type → GPU availability

2. **Use CPU Temporarily**
   - Switch to CPU runtime
   - Continue learning (slower but functional)

3. **Consider Colab Pro**
   - More GPU hours
   - Better GPUs (T4, V100, A100)

---

## 💻 System-Specific Issues | مشاكل خاصة بالنظام

### Windows:

**Problem:** "pip command not found"
- **Solution:** Use `python -m pip` instead of `pip`
- **Or:** Add Python to PATH during installation

**Problem:** "Permission denied"
- **Solution:** Run terminal as Administrator
- **Or:** Use `--user` flag: `pip install --user package_name`

---

### macOS:

**Problem:** "Command not found: python"
- **Solution:** Use `python3` instead of `python`
- **Or:** Create alias: `alias python=python3`

**Problem:** "SSL certificate errors"
- **Solution:**
  ```bash
  /Applications/Python\ 3.x/Install\ Certificates.command
  ```

---

### Linux:

**Problem:** "Permission denied"
- **Solution:** Use `sudo` or install with `--user` flag
- **Better:** Use virtual environment (no sudo needed)

---

## 📚 Learning Issues | مشاكل التعلم

### Problem: "I don't understand the notebook"

**Solutions:**

1. **Check Prerequisites**
   - Review course README for prerequisites
   - Complete previous courses/units if needed

2. **Read Documentation**
   - Read unit README files
   - Review course documentation

3. **Follow Sequence**
   - Complete units in order (1 → 5)
   - Don't skip ahead

4. **Practice Basics**
   - Review Python basics
   - Practice with simple examples first

---

### Problem: "Exercises are too difficult"

**Solutions:**

1. **Review Examples**
   - Re-read example notebooks
   - Understand code step-by-step

2. **Start Simple**
   - Modify examples first
   - Build up to exercises gradually

3. **Check Solutions**
   - Review solutions after attempting
   - Learn from solution approaches

4. **Ask for Help**
   - Consult course documentation
   - Ask instructors/peers

---

## ✅ Verification Checklist | قائمة التحقق

### Before Reporting Issues:

- [ ] Read this troubleshooting guide
- [ ] Checked course-specific documentation
- [ ] Verified Python version (3.8+)
- [ ] Verified libraries are installed
- [ ] Tried restarting kernel/runtime
- [ ] Checked for syntax errors
- [ ] Verified file paths are correct
- [ ] Checked GPU is enabled (if needed)

---

## 🔗 Additional Resources | موارد إضافية

### Documentation:
- **Course-Specific:** Each course has `START_HERE.md` and `README.md`
- **Setup Guide:** `SETUP_GUIDE.md`
- **Student Guide:** `STUDENT_GUIDE.md`
- **GPU Guide:** `GPU_REQUIREMENTS_SUMMARY.md`

### Online Resources:
- **Python Docs:** https://docs.python.org/
- **Pandas Docs:** https://pandas.pydata.org/docs/
- **NumPy Docs:** https://numpy.org/doc/
- **Colab Help:** https://colab.research.google.com/notebooks/intro.ipynb

---

## 🆘 Still Need Help? | لا تزال تحتاج مساعدة؟

1. **Check Course Documentation**
   - Read `START_HERE.md` in course directory
   - Review `README.md` for course-specific help

2. **Review Examples**
   - Re-read example notebooks
   - Check for similar code patterns

3. **Search Documentation**
   - Use search in documentation files
   - Check troubleshooting sections

4. **Contact Support**
   - Consult with instructors
   - Ask peers in study groups
   - Check course forums (if available)

---

**Last Updated:** January 2025  
**Status:** Comprehensive Troubleshooting Guide
