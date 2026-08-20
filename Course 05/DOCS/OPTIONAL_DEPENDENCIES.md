# Optional Dependencies Guide | دليل التبعيات الاختيارية

## Overview | نظرة عامة

Some Course 05 notebooks require **optional dependencies** that provide GPU acceleration or distributed computing capabilities. These are **not required** for the core learning objectives, but enhance the learning experience when available.

بعض دفاتر Course 05 تتطلب **تبعيات اختيارية** توفر تسريع GPU أو قدرات الحوسبة الموزعة. هذه **ليست مطلوبة** لأهداف التعلم الأساسية، لكنها تعزز تجربة التعلم عند توفرها.

---

## GPU-Accelerated Notebooks | دفاتر GPU

### Notebooks Requiring GPU Support:
1. **`03_cudf_introduction.ipynb`** - Introduction to cuDF (GPU-accelerated DataFrames)
2. **`13_cpu_vs_gpu_ml.ipynb`** - CPU vs GPU Machine Learning comparison

### What You Need:
- **NVIDIA GPU** with CUDA support
- **cuDF** library (GPU-accelerated pandas)
- **cuML** library (GPU-accelerated scikit-learn)

### Installation Options:

#### Option 1: Google Colab (Recommended for Students)
1. Open notebook in Google Colab
2. Go to **Runtime → Change runtime type**
3. Select **GPU** as hardware accelerator
4. Run the notebook - dependencies are pre-installed!

#### Option 2: Local Installation (Advanced)
```bash
# Using conda (recommended)
conda install -c rapidsai -c conda-forge cudf cuml

# Or using pip (may have compatibility issues)
pip install cudf-cu11 cuml-cu11
```

### What Happens Without GPU?
- Notebooks will show a **clear error message** explaining the requirement
- You can still **read and understand** the concepts
- The code examples demonstrate the **same operations** but with GPU acceleration
- **Alternative**: Use regular pandas/sklearn for CPU-based learning

---

## Distributed Computing Notebooks | دفاتر الحوسبة الموزعة

### Notebooks Requiring Spark:
1. **`15_pyspark_distributed.ipynb`** - Distributed Data Processing with PySpark

### What You Need:
- **Apache Spark** installation
- **PySpark** Python library

### Installation Options:

#### Option 1: Google Colab (Recommended for Students)
1. Open notebook in Google Colab
2. Install PySpark in first cell:
   ```python
   !pip install pyspark
   ```
3. Restart runtime and run the notebook

#### Option 2: Local Installation
```bash
# Install PySpark
pip install pyspark

# Note: Spark requires Java JDK
# macOS: brew install openjdk
# Linux: sudo apt-get install openjdk-11-jdk
# Windows: Download from Oracle
```

#### Option 3: Cloud Platforms (Production)
- **Databricks** - Managed Spark platform
- **AWS EMR** - Amazon Elastic MapReduce
- **Google Cloud Dataproc** - Managed Spark/Hadoop

### What Happens Without Spark?
- Notebook will show a **clear error message** explaining the requirement
- You can still **read and understand** distributed computing concepts
- **Alternative**: Use Dask (covered in Example 14) for similar distributed computing concepts

---

## Error Handling | معالجة الأخطاء

All notebooks with optional dependencies include **graceful error handling**:

```python
try:
    import cudf
    # ... GPU code ...
except ImportError:
    print("⚠️  cuDF not available. This notebook requires GPU support.")
    print("   Install with: conda install -c rapidsai -c conda-forge cudf")
    print("   Or use Google Colab with GPU runtime.")
    raise
```

This ensures:
- ✅ **Clear error messages** when dependencies are missing
- ✅ **Helpful installation instructions**
- ✅ **No confusing stack traces** for students
- ✅ **Graceful failure** that doesn't break the learning flow

---

## Learning Path Recommendations | توصيات مسار التعلم

### For Students Without GPU/Spark Access:

1. **Read the notebooks** - Understand the concepts and code structure
2. **Focus on the learning objectives** - The core concepts don't require GPU/Spark
3. **Use alternatives**:
   - For GPU notebooks: Use regular pandas/sklearn (CPU-based)
   - For Spark notebooks: Use Dask (covered in Example 14)
4. **Try cloud platforms**:
   - Google Colab (free GPU access)
   - Kaggle (free GPU access)
   - Databricks Community Edition (free Spark)

### For Students With GPU/Spark Access:

1. **Follow installation instructions** above
2. **Compare performance** - See the speed improvements firsthand
3. **Experiment** - Try larger datasets to see performance differences
4. **Document your findings** - Note the performance improvements

---

## Summary | الملخص

| Notebook | Dependency | Required? | Alternative |
|----------|-----------|-----------|-------------|
| `03_cudf_introduction.ipynb` | cuDF (GPU) | ❌ Optional | Use pandas |
| `13_cpu_vs_gpu_ml.ipynb` | cuML (GPU) | ❌ Optional | Use sklearn |
| `15_pyspark_distributed.ipynb` | PySpark | ❌ Optional | Use Dask |

**All notebooks are designed to work with or without these dependencies!**

---

## Questions? | أسئلة؟

If you encounter issues:
1. Check the error message - it should guide you
2. Review this document for installation options
3. Try Google Colab for easiest access
4. Contact your instructor for assistance
