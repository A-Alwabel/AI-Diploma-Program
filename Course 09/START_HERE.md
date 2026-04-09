# Start Here

This course is part of Semester 2 of the AI Diploma Program.

## Student Quick Start

1. Read `README.md`
2. Set up the environment
3. Start `unit1-rl-fundamentals/`
4. Follow the numbered notebooks in order
5. Complete the exercise, then the quiz

## Environment Setup

Recommended:

- Python 3.10 or 3.11
- Jupyter Notebook or JupyterLab
- A clean virtual environment

Install the core packages:

```bash
pip install numpy matplotlib
pip install torch torchvision
pip install gymnasium[classic_control]
pip install scikit-learn
```

If you prefer a hosted environment, Google Colab is acceptable for most notebooks.

## Verify Your Setup

```python
import torch
import gymnasium
import numpy

print("PyTorch:", torch.__version__)
print("Gymnasium:", gymnasium.__version__)
print("NumPy:", numpy.__version__)
```

## Before You Begin

You should already be comfortable with:

- Python basics
- Probability and statistics fundamentals
- Machine learning basics
- Neural network basics from Course 08

## Recommended Learning Path

1. Read `README.md`
2. Read the `README.md` inside the current unit
3. Complete the numbered example notebooks in order
4. Complete the unit exercise notebook
5. Review the unit solution notebook after attempting the exercise
6. Take the unit quiz
7. Update `STUDENT_PROGRESS_CHECKLIST.md`

## Important Guidance

### Which notebooks should students follow?

Follow the **numbered notebooks first** (`01`, `02`, `03`, ...).

Some units also contain long descriptive notebook filenames that overlap with
the numbered versions.

Use this rule:

- The **required student path** is the numbered notebooks only.
- Long descriptive notebook filenames are supplemental/reference materials.
- Ignore those long filenames unless your instructor explicitly assigns them.

### What if a notebook is confusing?

If a notebook is not clear:

1. Re-read the unit `README.md`
2. Review the previous notebook in the same unit
3. Check `../docs/TROUBLESHOOTING_GUIDE.md` for environment issues
4. Ask your instructor before skipping the topic

## Supporting Documents

- `../docs/SETUP_GUIDE.md`
- `../docs/TROUBLESHOOTING_GUIDE.md`
- `../docs/COURSE_MAP.md`

## Progress Tracking

Use `STUDENT_PROGRESS_CHECKLIST.md` to track your progress across all five units,
the project, and the final exam.

## Start Now

Open `unit1-rl-fundamentals/README.md` and begin with the first numbered notebook.
