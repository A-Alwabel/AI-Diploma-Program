# Google Colab Setup Guide for Deep Learning
## Using GPU-Accelerated Notebooks on Google Colab

**For students without NVIDIA GPU:** Use Google Colab for free GPU access!

---

## 🚀 Quick Start

### Step 1: Open Notebook in Colab

1. **Go to Google Colab:** https://colab.research.google.com/
2. **Upload notebook:**
   - Click "File" → "Upload notebook"
   - Select the notebook file (e.g., `03_perceptron_mlp_tensorflow_pytorch_setup.ipynb`)
   - Or use "File" → "Open notebook" → "GitHub" and paste repository URL

### Step 2: Enable GPU

1. **Click:** "Runtime" → "Change runtime type"
2. **Set:**
   - Hardware accelerator: **GPU** (T4 or better)
   - Runtime type: **Python 3**
3. **Click:** "Save"

### Step 3: Install Libraries (Auto-installed in Colab)

**Colab already includes TensorFlow and PyTorch with GPU support!**

The setup cell will:
- Detect Colab environment
- Install/update TensorFlow and PyTorch if needed
- Verify GPU access

**Just run the Colab setup cell at the beginning of the notebook!**

### Step 4: Verify GPU Access

```python
# Verify GPU is available
import torch
import tensorflow as tf

# PyTorch
if torch.cuda.is_available():
    print(f"✅ PyTorch GPU: {torch.cuda.get_device_name(0)}")
else:
    print("⚠️  PyTorch GPU not available")

# TensorFlow
if tf.config.list_physical_devices('GPU'):
    print(f"✅ TensorFlow GPU: Available")
else:
    print("⚠️  TensorFlow GPU not available")
```

---

## 📚 Notebooks That Benefit from GPU

These notebooks work much better with GPU:

1. **`03_perceptron_mlp_tensorflow_pytorch_setup.ipynb`** - TensorFlow/PyTorch setup
2. **`06_gpt_text_generation.ipynb`** - GPT text generation (transformers)
3. **All CNN notebooks** - Image classification training
4. **All RNN notebooks** - Sequence modeling training
5. **All Transformer notebooks** - Attention mechanisms training

---

## 💡 Tips

### Free GPU Limits
- **Free tier:** ~12 hours/day of GPU usage
- **Colab Pro:** More GPU hours, better GPUs (T4, V100, A100)
- **Solution:** Save your work frequently!

### Best Practices
1. **Enable GPU before installing libraries** - Saves time
2. **Restart runtime after installation** - Ensures libraries load correctly
3. **Save notebooks to Google Drive** - Don't lose your work
4. **Download trained models** - Save checkpoints locally
5. **Use smaller models for testing** - Faster iteration

### Troubleshooting

**Problem:** "CUDA out of memory"
- **Solution:** Reduce batch size, use smaller models, or restart runtime

**Problem:** "Training is very slow"
- **Solution:** Check that GPU is enabled (Runtime → Change runtime type → GPU)

**Problem:** "TensorFlow/PyTorch not detecting GPU"
- **Solution:** Restart runtime after enabling GPU

**Problem (local/Anaconda):** `AttributeError: partially initialized module 'charset_normalizer' has no attribute 'md__mypyc'` when running `import tensorflow as tf`
- **Cause:** Broken or incompatible `charset_normalizer` (used by `requests`, which TensorFlow uses).
- **Fix:** In a terminal (with the same environment active), run:
  ```bash
  pip install --upgrade charset-normalizer requests
  ```
  Then **restart the Jupyter kernel** (Kernel → Restart) and run the imports cell again.
- **Note:** Course 08 notebooks that use TensorFlow catch this error and print the fix; if you see that message, run the command above and restart the kernel.

---

## 🔗 Alternative: Kaggle Notebooks

**Kaggle also provides free GPU:**
1. Go to: https://www.kaggle.com/
2. Create new notebook
3. Enable GPU: Settings → Accelerator → GPU
4. Install libraries using pip

---

## ✅ Quick Checklist

- [ ] Opened notebook in Google Colab
- [ ] Enabled GPU (Runtime → Change runtime type → GPU)
- [ ] Ran Colab setup cell
- [ ] Restarted runtime
- [ ] Verified GPU access
- [ ] Ready to train deep learning models!

---

**Last Updated:** January 2025  
**Status:** Ready for use
