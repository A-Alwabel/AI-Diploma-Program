# 🚀 AI Diploma Curriculum - Setup Guide

Complete setup instructions for the AI Diploma curriculum.

---

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python Version**: Python 3.8 or higher
- **RAM**: Minimum 8GB (16GB recommended for deep learning)
- **Storage**: At least 10GB free space
- **GPU**: Optional but recommended for deep learning courses (NVIDIA GPU with CUDA support)

### Required Knowledge
- Basic Python programming
- Command line/terminal usage
- Basic understanding of machine learning concepts (for advanced courses)

---

## 🔧 Installation Steps

### Step 1: Install Python

**Windows:**
1. Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. Run installer, check "Add Python to PATH"
3. Verify: Open Command Prompt, type `python --version`

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python@3.10

# Or download from python.org
# Verify installation
python3 --version
```

**Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```cmd
python -m venv ai_diploma_env
ai_diploma_env\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv ai_diploma_env
source ai_diploma_env/bin/activate
```

### Step 3: Install Dependencies

```bash
# Navigate to project directory
cd "/path/to/AI Diploma"

# Upgrade pip
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt

# Verify installation
pip check
```

**Quick validate:** Run a minimal check to confirm core libs work:
```bash
python -c "import numpy, pandas, sklearn; print('✅ Core libs OK')"
```
Optional: run one notebook (e.g. `Course 01/unit1-ai-foundations/examples/01_ai_introduction.ipynb`) to confirm Jupyter + deps.

### Step 4: Install Jupyter Notebook

```bash
pip install jupyter notebook ipykernel

# Add kernel to Jupyter
python -m ipykernel install --user --name=ai_diploma_env
```

### Step 5: Install Additional Course-Specific Tools

**For Course 05 (Data Science with GPU):**
```bash
# Optional: NVIDIA RAPIDS (requires NVIDIA GPU)
# Follow instructions at: https://rapids.ai/start.html
```

**For Course 08 (Deep Learning):**
```bash
# TensorFlow GPU support (if you have NVIDIA GPU)
# Note: TensorFlow 2.x includes GPU support automatically
# Just install tensorflow (already in requirements.txt)
# Make sure you have CUDA and cuDNN installed for GPU support
# See: https://www.tensorflow.org/install/gpu

# PyTorch GPU (if you have NVIDIA GPU)
# Visit: https://pytorch.org/get-started/locally/
```

**For Course 09 (Reinforcement Learning):**
```bash
pip install gym[atari] stable-baselines3
```

**For Course 10 (Generative AI):**
```bash
# OpenAI API (requires API key)
pip install openai

# Hugging Face Transformers
pip install transformers accelerate
```

---

## 📚 Course-Specific Setup

### Course 01: Introduction to AI
- **Required**: NumPy, basic Python libraries
- **Setup**: `pip install numpy matplotlib`

### Course 02: Python for AI
- **Required**: NumPy, Pandas, scikit-learn
- **Setup**: Already in requirements.txt

### Course 03: Mathematics & Probability ✅
- **Required**: NumPy, SciPy, Matplotlib
- **Setup**: Core libraries included

### Course 04: Machine Learning
- **Required**: scikit-learn, Pandas, NumPy
- **Setup**: Core libraries included

### Course 05: Data Science
- **Required**: Pandas, NumPy, Matplotlib, Seaborn, Plotly
- **Optional**: cuDF (GPU acceleration)
- **Setup**: Core libraries included

### Course 06: AI Ethics
- **Required**: scikit-learn, SHAP, LIME
- **Setup**: `pip install shap lime`

### Course 07: Natural Language Processing
- **Required**: NLTK, spaCy, Transformers
- **Setup**: 
```bash
pip install nltk spacy transformers
python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('punkt')"
```

### Course 08: Deep Learning
- **Required**: TensorFlow/Keras, PyTorch
- **Setup**: Core libraries included

### Course 09: Reinforcement Learning
- **Required**: OpenAI Gym, Stable-Baselines3
- **Setup**: Core libraries included

### Course 10: Generative AI
- **Required**: Transformers, OpenAI API (optional)
- **Setup**: Core libraries included

### Course 11: Deploying AI Models
- **Required**: Flask, FastAPI, Docker (optional)
- **Setup**: Core libraries included

### Course 12: Graduation Project
- **Required**: All previous course libraries
- **Setup**: Use requirements.txt

---

## 🧪 Verify Installation

Run this verification script:

```python
# verify_installation.py
import sys

libraries = [
    'numpy', 'pandas', 'matplotlib', 'seaborn', 'sklearn',
    'tensorflow', 'torch', 'transformers', 'nltk', 'spacy',
    'plotly', 'gym', 'flask', 'fastapi', 'shap', 'lime'
]

print("Python version:", sys.version)
print("\nChecking libraries...")

missing = []
for lib in libraries:
    try:
        __import__(lib)
        print(f"✅ {lib}")
    except ImportError:
        print(f"❌ {lib} - MISSING")
        missing.append(lib)

if missing:
    print(f"\n⚠️  Missing libraries: {', '.join(missing)}")
    print("Install with: pip install " + " ".join(missing))
else:
    print("\n✅ All core libraries installed successfully!")
```

---

## 🐳 Docker Setup (Alternative)

If you prefer Docker:

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

Build and run:
```bash
docker build -t ai-diploma .
docker run -p 8888:8888 -v $(pwd):/app ai-diploma
```

---

## 🔍 Troubleshooting

### Common Issues

**Issue**: `pip` command not found
- **Solution**: Use `pip3` instead, or ensure Python is in PATH

**Issue**: Permission denied errors
- **Solution**: Use `pip install --user` or activate virtual environment

**Issue**: CUDA/GPU not working
- **Solution**: Install CUDA toolkit separately, verify GPU drivers

**Issue**: Import errors in notebooks
- **Solution**: Ensure kernel is using correct environment: `python -m ipykernel install --user --name=ai_diploma_env`

**Issue**: Memory errors with large datasets
- **Solution**: Use smaller datasets, enable GPU, or increase system RAM

**Issue**: Some notebooks fail (missing packages, syntax)
- **Solution**: Run `pip check` and quick-validate (Step 3). See [artifacts/NOTEBOOK_TRIAGE.md](artifacts/NOTEBOOK_TRIAGE.md) for env vs code triage and optional/advanced markers.

---

## 📖 Next Steps

1. ✅ Complete setup verification
2. 📚 Read `START_HERE.md` in each course directory
3. 📝 Review `MASTER_NOTEBOOK_INDEX.md` for navigation
4. 🎯 Start with Course 01, Unit 1
5. 📊 Track progress using course checklists

---

## 🆘 Getting Help

- Check course-specific README files
- Review notebook documentation
- Consult `DETAILED_UNIT_DESCRIPTIONS.md` for course structure
- Check `MASTER_NOTEBOOK_INDEX.md` for notebook locations

---

**Last Updated**: Session completion date
**Status**: Ready for use
