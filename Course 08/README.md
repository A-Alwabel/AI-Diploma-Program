# AIAT 122 - Deep Learning

## 🚀 NEW STUDENTS: START HERE!

**👉 If you're a new student, read `START_HERE.md` FIRST!**

**👩‍🏫 Instructors:** First time teaching? See **`DOCS/TEACHING_GUIDE.md`** then **`DOCS/INSTRUCTOR_RUNBOOK.md`**.

---

**✅ Official Path:** Follow the unit folders in order (Unit 1 → Unit 5).

**📚 Source of truth for what to study:** **This README** + **`DOCS/EXAMPLES_ORDER.md`** define unit content and notebook order. If your repo has `../DETAILED_UNIT_DESCRIPTIONS.md`, it aligns with these; otherwise this README + EXAMPLES_ORDER are the curriculum.

**Unit ↔ Folder Mapping (aligned with Detailed Unit Descriptions):**

| Detailed Unit | Folder | Topic |
|---------------|--------|-------|
| Unit 1 | `unit1-deep-learning-basics/` | Introduction to Deep Learning and Neural Networks |
| Unit 2 | `unit2-cnns/` | Convolutional Neural Networks (CNNs) for Computer Vision |
| Unit 3 | `unit3-rnns-transformers/` | Recurrent Neural Networks (RNNs) and Transformers for Sequential Data |
| Unit 4 | `unit4-advanced-dl/` | Advanced Deep Learning Techniques (GANs, VAEs, RL, transfer learning, ethics) |
| Unit 5 | `unit5-deployment/` | Model Optimization and Deployment |

**📌 Which notebook covers which topic?** Each example notebook has a **📌 Covers slide(s):** line in its first cell (which lecture slide it matches). For the full map (slide ↔ topic ↔ notebook), see **`DOCS/EXAMPLES_ORDER.md`**. That way you always know what you’re learning and won’t get confused.

**📌 Theory → Practical:** Lecture slides (theory) are **directly applied** in the example notebooks: each notebook states which slide(s) it covers, includes a short **Theory (short)** recap, then **Step 1, Step 2, …** code so you see the concept in practice. Do each notebook **after** the corresponding slide(s) so theory and practice stay connected.

**📌 Notebook order:** Do examples in **file order** (01 → 02 → 03 …) as listed in each unit's README. Slide numbers in the doc are references to lecture slides, not the sequence to follow.

**❓ "Dr, it's not connected" / ordering confusion?**  
Always follow **notebook file number order** (01, then 02, then 03, …) in each unit. **Slide numbers** (e.g. 08, 01, 02) are only **topic IDs**—they do **not** tell you which notebook to do first. So: first notebook in the unit is always **01_…**, second is **02_…**, and so on. Optional notebooks (e.g. 07, 08 in Unit 1) are clearly marked; do them after the core numbered sequence. If you follow 01 → 02 → 03 …, theory and practice stay connected.

## Course Overview

This course provides comprehensive training in Deep Learning using TensorFlow and PyTorch. Students will learn to build, train, and deploy deep neural networks for various applications.

**Course Code:** AIAT 122  
**Language:** English
**Credit Hours:** 3  
**Lecture Hours:** 2  
**Practical Hours:** 2  
**Total Hours:** 96 (32 theoretical + 64 practical)

**Unit Breakdown:**
- Unit 1: 6 theoretical + 12 practical = 18 hours
- Unit 2: 6 theoretical + 13 practical = 19 hours
- Unit 3: 6 theoretical + 13 practical = 19 hours
- Unit 4: 7 theoretical + 13 practical = 20 hours
- Unit 5: 7 theoretical + 13 practical = 20 hours


---

## Prerequisites

**What you need:** You only need **this repository** (clone or download) and the **root `requirements.txt`** at the AI Diploma folder. No other files or external data are required—notebooks download datasets (e.g. MNIST) automatically when you run them. **Libraries:** Most notebooks use **TensorFlow/Keras**; some (e.g. Unit 3 BERT/transformers) use **PyTorch**. Install both for full coverage (see `DOCS/REQUIREMENTS_COURSE_08.md`).

**Python Version**: Python 3.8+ required (3.10 or 3.11 recommended)

**Knowledge**: Students should have:
- Completion of Courses 01-06 (Semester 1)
- Strong understanding of machine learning
- Familiarity with neural networks basics

**Hardware**: 
- **GPU strongly recommended** for training deep learning models (10-100x faster)
- **Use Google Colab for free GPU access!** (See `DOCS/COLAB_SETUP.md`)
- CPU works but training will be very slow

**Notebooks without slides?** You can follow the **notebook order** in each unit README even if you don't have the institution slides; each notebook has enough theory to proceed. Unit 5 has no slides—use its examples in file order.

**If a notebook isn't clear?** Some parts are harder (e.g. backprop, attention, optimization). See **`DOCS/WHEN_A_NOTEBOOK_IS_NOT_CLEAR.md`** for what to do: pinpoint which part, use the notebook's Theory and Steps, and how to ask your instructor so they can help quickly.

---

## Course Learning Outcomes (CLOs)

**The detailed objectives of the training program are: For the trainee to be able to:**

**CLO1:** Explain basic concepts of deep learning, including the structure and performance of neural networks, backpropagation algorithm, and optimization techniques.

**CLO2:** Develop and implement deep learning architectures such as Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Transformers.

**CLO3:** Build and deploy deep learning models to solve real-world problems, including tasks in image recognition (such as classification and object detection).

**CLO4:** Optimize deep learning models by applying techniques such as hyperparameter tuning (grid search, random search) and regularization (dropout, batch normalization).

**CLO5:** Critically evaluate ethical issues related to deep learning, including biases in datasets, fairness in model predictions, and interpretability.

---

## 📁 Course Structure

```
Course 08/
│
├── README.md
├── START_HERE.md
├── STUDENT_PROGRESS_CHECKLIST.md
│
├── unit1-deep-learning-basics/      📚 Unit 1: Deep Learning Basics
├── unit2-cnns/                      📚 Unit 2: CNNs for Images
├── unit3-rnns-transformers/         📚 Unit 3: RNNs and Transformers
├── unit4-advanced-dl/               📚 Unit 4: Advanced DL (GANs, VAEs, RL, transfer, ethics)
├── unit5-deployment/                📚 Unit 5: Deploying Deep Learning Models
│
├── PROJECTS/
├── QUIZZES/
└── DOCS/                    (includes COLAB_SETUP.md, EXAMPLES_ORDER.md, PHASES_TO_10_TEACHING_PLAN.md)
```

---

**Created for**: AIAT 122 - Deep Learning  
**Last Updated:** 2025-12-10

