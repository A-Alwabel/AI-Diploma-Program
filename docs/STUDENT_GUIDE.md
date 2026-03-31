# Complete Student Guide | دليل الطالب الشامل
## Your Complete Guide to the AI Diploma Program

**Welcome to the AI Diploma Program!** This guide will help you navigate the entire program successfully.

---

## 🚀 Getting Started | البدء

### Step 1: Understand the Program Structure

**Program Overview:**
- **12 Courses** + Graduation Project
- **9 Months** total duration
- **944 Hours** of training (368 theory + 576 practical)
- **75 Course Learning Outcomes (CLOs)**

**Quick Navigation:**
1. Read **[QUICK_REFERENCE_GUIDE.md](QUICK_REFERENCE_GUIDE.md)** - One-page overview
2. Review **[TEACHING_TIMELINE.md](TIMELINE/TEACHING_TIMELINE.md)** - Complete schedule
3. Check **[GPU_REQUIREMENTS_SUMMARY.md](GPU_REQUIREMENTS_SUMMARY.md)** - GPU needs

### Step 2: Choose Your Starting Course

**If you're a complete beginner:**
- Start with **Course 01: Introduction to AI**
- Follow the course sequence (01 → 02 → 03...)

**If you have Python experience:**
- You can start with **Course 02: Python for AI**
- Review Course 01 materials if needed

**If you have ML experience:**
- You can start with **Course 04: ML Algorithms**
- Ensure you have prerequisites from Courses 01-03

### Step 3: Course Setup

**For each course:**
1. Navigate to course directory (e.g., `Course 01/`)
2. **Read `START_HERE.md` FIRST** - Critical setup instructions
3. Read `README.md` - Course overview
4. Follow installation steps
5. Begin with Unit 1

**Note for Students:** The `TEMPLATES/` folder is for instructors only.  
You should follow course units and notebooks, not templates.

---

## 📚 Course Progression | تقدم الدورات

### Semester 1 (Foundation)
```
Course 01: Introduction to AI
    ↓
Course 02: Python for AI
    ↓
Course 03: Mathematics & Probability
    ↓
Course 04: ML Algorithms
    ↓
Course 05: Scalable Data Science
    ↓
Course 06: AI Ethics
```

### Semester 2 (Advanced)
```
Course 07: Natural Language Processing
    ↓
Course 08: Deep Learning
    ↓
Course 09: Reinforcement Learning
    ↓
Course 10: Generative AI
    ↓
Course 11: Deploying AI Models
    ↓
Course 12: Graduation Project
```

**Important:** Each course builds on previous ones. Don't skip courses!

---

## 🖥️ Hardware Requirements | متطلبات الأجهزة

### Required for All Courses:
- **Computer:** Any modern computer (Windows, macOS, or Linux)
- **Python:** 3.8+ (3.10 or 3.11 recommended)
- **RAM:** 8GB minimum (16GB recommended)
- **Storage:** 10GB+ free space
- **Internet:** For downloading libraries and datasets

### GPU Requirements:

**✅ Course 05 (Scalable Data Science):**
- GPU required for cuDF/RAPIDS features
- **Solution:** Use Google Colab (free GPU) - See `Course 05/DOCS/COLAB_SETUP.md`

**⚠️ Course 08 (Deep Learning):**
- GPU strongly recommended (10-100x faster training)
- **Solution:** Use Google Colab (free GPU) - See `Course 08/DOCS/COLAB_SETUP.md`

**⚠️ Course 10 (Generative AI):**
- GPU strongly recommended (training very slow on CPU)
- **Solution:** Use Google Colab (free GPU) - See `Course 10/DOCS/COLAB_SETUP.md`

**❌ Other Courses (01-04, 06-07, 09, 11-12):**
- No GPU needed - work perfectly on CPU

**See [GPU_REQUIREMENTS_SUMMARY.md](GPU_REQUIREMENTS_SUMMARY.md) for details.**

---

## 🛠️ Setup Instructions | تعليمات الإعداد

### Quick Setup (All Courses):

1. **Install Python 3.8+**
   - Download from: https://www.python.org/downloads/
   - Verify: `python --version` or `python3 --version`

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Libraries**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   pip check
   python -c "import pandas, numpy, sklearn; print('✅ All libraries installed!')"
   ```

**For detailed setup:** See `SETUP_GUIDE.md` or course-specific `START_HERE.md`

---

## 📖 Learning Path | مسار التعلم

### For Each Course:

1. **Read Course README.md**
   - Understand course objectives
   - Review prerequisites
   - Check course structure

2. **Read START_HERE.md**
   - Follow setup instructions
   - Understand learning sequence
   - Review progress tracker

3. **Complete Units in Order**
   - Start with Unit 1
   - Complete all examples
   - Do exercises
   - Take quizzes

4. **Track Your Progress**
   - Use `STUDENT_PROGRESS_CHECKLIST.md`
   - Mark completed units
   - Review regularly

---

## 🆘 Troubleshooting | حل المشاكل

### Common Issues:

**Problem:** "No module named 'pandas'" or similar
- **Solution:** Install libraries: `pip install -r requirements.txt`
- **Check:** Verify virtual environment is activated

**Problem:** "Python version too old"
- **Solution:** Install Python 3.10 or 3.11
- **Verify:** `python --version` should show 3.8+

**Problem:** "Notebook won't run"
- **Solution:** 
  1. Check Python kernel is selected
  2. Restart kernel: Kernel → Restart
  3. Run cells in order

**Problem:** "GPU not working"
- **Solution:** 
  1. For Course 05/08/10: Use Google Colab (see Colab setup guides)
  2. Check GPU is enabled in Colab: Runtime → Change runtime type → GPU
  3. Verify GPU access in notebook

**Problem:** "Libraries conflict"
- **Solution:** Use virtual environment (see setup instructions)

**Problem:** "I don't understand the content"
- **Solution:**
  1. Check prerequisites in course README
  2. Review previous courses if needed
  3. Read unit README files
  4. Complete examples in order

---

## 💡 Best Practices | أفضل الممارسات

### Study Tips:

1. **Follow the Sequence**
   - Complete courses in order (01 → 12)
   - Complete units in order (1 → 5)
   - Don't skip ahead

2. **Practice Regularly**
   - Run all example notebooks
   - Complete all exercises
   - Try variations and experiments

3. **Track Your Progress**
   - Use progress checklists
   - Mark completed items
   - Review regularly

4. **Ask for Help**
   - Check troubleshooting guides
   - Review course documentation
   - Consult with instructors/peers

5. **Save Your Work**
   - Commit code regularly
   - Save notebook outputs
   - Backup important files

### Code Quality:

1. **Read Comments**
   - All notebooks have detailed comments
   - Comments explain concepts
   - Learn from code examples

2. **Experiment**
   - Modify code examples
   - Try different parameters
   - Test edge cases

3. **Document Your Learning**
   - Take notes
   - Write summaries
   - Create your own examples

---

## 📊 Progress Tracking | تتبع التقدم

### Course-Level Tracking:

Each course has:
- `STUDENT_PROGRESS_CHECKLIST.md` - Detailed checklist
- Unit-level progress tracking
- Exercise completion tracking

### Program-Level Tracking:

**Semester 1 Progress:**
- [ ] Course 01: Introduction to AI
- [ ] Course 02: Python for AI
- [ ] Course 03: Mathematics & Probability
- [ ] Course 04: ML Algorithms
- [ ] Course 05: Scalable Data Science
- [ ] Course 06: AI Ethics

**Semester 2 Progress:**
- [ ] Course 07: Natural Language Processing
- [ ] Course 08: Deep Learning
- [ ] Course 09: Reinforcement Learning
- [ ] Course 10: Generative AI
- [ ] Course 11: Deploying AI Models
- [ ] Course 12: Graduation Project

---

## 🎯 Course-Specific Guides | أدلة خاصة بالدورات

### GPU Courses (Use Colab):
- **Course 05:** `Course 05/DOCS/COLAB_SETUP.md`
- **Course 08:** `Course 08/DOCS/COLAB_SETUP.md`
- **Course 10:** `Course 10/DOCS/COLAB_SETUP.md`

### Setup Guides:
- **General Setup:** `SETUP_GUIDE.md`
- **Course-Specific:** Each course has `START_HERE.md`

### Reference Documents:
- **Quick Reference:** `QUICK_REFERENCE_GUIDE.md`
- **Complete Structure:** `COMPLETE_COURSE_STRUCTURE_AND_CLOS.md`
- **Detailed Content:** `DETAILED_UNIT_DESCRIPTIONS.md`
- **Timeline:** `TIMELINE/TEACHING_TIMELINE.md`

---

## 🔗 Quick Links | روابط سريعة

### Essential Documents:
- [QUICK_REFERENCE_GUIDE.md](QUICK_REFERENCE_GUIDE.md) - Quick overview
- [TEACHING_TIMELINE.md](TIMELINE/TEACHING_TIMELINE.md) - Complete schedule
- [GPU_REQUIREMENTS_SUMMARY.md](GPU_REQUIREMENTS_SUMMARY.md) - GPU needs
- [SETUP_GUIDE.md](SETUP_GUIDE.md) - Setup instructions

### Course Directories:
- `Course 01/` - Introduction to AI
- `Course 02/` - Python for AI
- `Course 03/` - Mathematics & Probability
- `Course 04/` - ML Algorithms
- `Course 05/` - Scalable Data Science
- `Course 06/` - AI Ethics
- `Course 07/` - Natural Language Processing
- `Course 08/` - Deep Learning
- `Course 09/` - Reinforcement Learning
- `Course 10/` - Generative AI
- `Course 11/` - Deploying AI Models
- `Course 12/` - Graduation Project

---

## ✅ Success Checklist | قائمة النجاح

### Before Starting:
- [ ] Read this guide completely
- [ ] Reviewed program structure
- [ ] Understood course progression
- [ ] Checked hardware requirements
- [ ] Set up Python environment

### During Learning:
- [ ] Following course sequence
- [ ] Completing all examples
- [ ] Doing all exercises
- [ ] Tracking progress
- [ ] Asking questions when stuck

### After Each Course:
- [ ] Completed all units
- [ ] Completed all exercises
- [ ] Taken quizzes/assessments
- [ ] Reviewed key concepts
- [ ] Ready for next course

---

## 🎓 Final Tips | نصائح نهائية

1. **Be Patient** - Learning AI takes time
2. **Practice Regularly** - Code every day
3. **Don't Skip** - Each course builds on previous
4. **Ask Questions** - Use documentation and support
5. **Track Progress** - Use checklists
6. **Experiment** - Try variations and modifications
7. **Save Work** - Commit code regularly
8. **Stay Organized** - Keep notes and summaries

---

**Last Updated:** January 2025  
**Status:** Complete Student Guide  
**For Course-Specific Help:** See individual course `START_HERE.md` files
