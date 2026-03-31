# AI Diploma Program
### برنامج دبلوم الذكاء الاصطناعي

A comprehensive, hands-on AI curriculum covering Deep Learning, Reinforcement Learning, Generative AI, and Production Deployment — built with PyTorch and real-world industry examples.

---

## 📚 Courses

| # | Course | Topics |
|---|--------|--------|
| 01 | Foundations of AI | Python, math, ML basics |
| 02 | Supervised Learning | Regression, classification, evaluation |
| 03 | Unsupervised Learning | Clustering, dimensionality reduction |
| 04 | Advanced ML | Ensemble methods, feature engineering |
| 05 | NLP Fundamentals | Text processing, classical NLP |
| 06 | Applied ML Projects | End-to-end pipelines |
| 07 | Introduction to Deep Learning | Perceptrons, activation functions |
| **08** | **Deep Learning** | CNNs, RNNs, Transformers, Deployment |
| **09** | **Reinforcement Learning** | MDPs, DQN, PPO, Multi-agent RL |
| **10** | **Generative AI** | GANs, VAEs, Diffusion Models, LLMs |
| **11** | **AI Deployment & MLOps** | APIs, Docker, Cloud, CI/CD, Monitoring |
| 12 | Capstone Project | Full AI system from idea to production |

> Courses 08–11 are fully developed with examples, exercises, quizzes, and assessments.

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/A-Alwabel/AI-Diploma-Program.git
cd AI-Diploma-Program
```

### 2. Set up the environment
```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Register the Jupyter kernel
```bash
python -m ipykernel install --user --name ai-diploma --display-name "AI Diploma"
```

### 4. Launch JupyterLab
```bash
jupyter lab
```

Navigate to the course folder you want and open `START_HERE.md` first.

---

## 📁 Repository Structure

```
AI-Diploma-Program/
├── Course 08/                    # Deep Learning
│   ├── START_HERE.md             ← Start here every course
│   ├── unit1-deep-learning-basics/
│   │   ├── examples/             ← Worked examples with real-world code
│   │   └── exercises/            ← Hands-on practice (TODOs to complete)
│   ├── unit2-cnns/
│   ├── unit3-rnns-transformers/
│   ├── unit4-advanced-dl/
│   ├── unit5-deployment/
│   ├── QUIZZES/                  ← 5 unit quizzes
│   ├── ASSESSMENTS/              ← Final exam
│   └── STUDENT_PROGRESS_CHECKLIST.md
│
├── Course 09/                    # Reinforcement Learning
├── Course 10/                    # Generative AI
├── Course 11/                    # AI Deployment & MLOps
│
├── SOLUTIONS_ALL/                # Reference solutions (Courses 01–06)
├── docs/                         # Curriculum documentation
│   ├── STUDENT_GUIDE.md
│   ├── SETUP_GUIDE.md
│   ├── COURSE_MAP.md
│   ├── TROUBLESHOOTING_GUIDE.md
│   └── ...
└── requirements.txt
```

---

## 🗺️ Learning Path

Each course follows the same pattern:

```
START_HERE.md → examples/ (study) → exercises/ (practice) → QUIZZES/ → ASSESSMENTS/
```

Every example notebook includes:
- 📖 **Theory** — concept explanation with visuals
- 💻 **Code** — complete, runnable PyTorch implementation
- 🌍 **Real-World Example** — same concept applied to industry data
- 📚 **References** — papers, docs, further reading
- 📝 **Summary** — key takeaways

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Deep Learning | PyTorch, torchvision |
| RL Environments | Gymnasium (OpenAI Gym) |
| Deployment | FastAPI, ONNX, Docker |
| Experiment Tracking | MLflow |
| Visualization | Matplotlib, Seaborn |
| Data | NumPy, Pandas, Scikit-learn |

> All notebooks are tested on Python 3.9+ (macOS, Linux, Windows).

---

## 📋 Prerequisites

- Python 3.9 or higher
- Basic Python programming
- Linear algebra fundamentals (vectors, matrices)
- Calculus basics (derivatives, chain rule)

---

## 📖 Documentation

| Document | Description |
|---|---|
| [Student Guide](docs/STUDENT_GUIDE.md) | How to navigate the curriculum |
| [Setup Guide](docs/SETUP_GUIDE.md) | Detailed installation instructions |
| [Course Map](docs/COURSE_MAP.md) | Visual overview of all 12 courses |
| [Troubleshooting](docs/TROUBLESHOOTING_GUIDE.md) | Common errors and fixes |
| [GPU Requirements](docs/GPU_REQUIREMENTS_SUMMARY.md) | Hardware recommendations |
| [Community Resources](docs/COMMUNITY_RESOURCES.md) | Datasets, papers, tools |

---

## 📄 License

This curriculum is provided for educational purposes.

---

*Built with ❤️ for AI learners*
