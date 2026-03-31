# Course Navigation Guide | دليل التنقل بين الدورات
## How Courses Connect and Build on Each Other

**Last Updated:** January 2025

---

## 🗺️ Course Dependency Map | خريطة تبعيات الدورات

```
┌─────────────────────────────────────────────────────────────┐
│                    FOUNDATION LEVEL                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Course 01: Introduction to AI                             │
│  └─> No prerequisites                                      │
│      └─> Provides: AI concepts, search algorithms          │
│                                                             │
│  Course 02: Python for AI                                   │
│  └─> Needs: Course 01 (AI concepts)                        │
│      └─> Provides: Python skills, algorithms               │
│                                                             │
│  Course 03: Mathematics & Probability                       │
│  └─> Needs: Course 02 (Python basics)                       │
│      └─> Provides: Math foundations for ML                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    MACHINE LEARNING LEVEL                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Course 04: ML Algorithms                                   │
│  └─> Needs: Courses 01-03                                   │
│      └─> Provides: ML algorithms, model building            │
│                                                             │
│  Course 05: Scalable Data Science                           │
│  └─> Needs: Course 04 (ML basics)                           │
│      └─> Provides: Data processing, visualization           │
│                                                             │
│  Course 06: AI Ethics                                       │
│  └─> Needs: Courses 01-05 (AI/ML knowledge)                │
│      └─> Provides: Ethical frameworks, bias detection      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    ADVANCED AI LEVEL                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Course 07: Natural Language Processing                     │
│  └─> Needs: Courses 01-06                                   │
│      └─> Provides: NLP, text processing, transformers      │
│                                                             │
│  Course 08: Deep Learning                                   │
│  └─> Needs: Courses 01-07 (especially 04, 07)             │
│      └─> Provides: Neural networks, CNNs, RNNs              │
│                                                             │
│  Course 09: Reinforcement Learning                          │
│  └─> Needs: Courses 01-08 (especially 08)                  │
│      └─> Provides: RL algorithms, Q-learning, DQN            │
│                                                             │
│  Course 10: Generative AI                                   │
│  └─> Needs: Courses 01-09 (especially 08)                 │
│      └─> Provides: GANs, VAEs, Stable Diffusion             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT & PROJECT                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Course 11: Deploying AI Models                             │
│  └─> Needs: Courses 01-10 (all previous knowledge)        │
│      └─> Provides: Deployment, MLOps, cloud platforms       │
│                                                             │
│  Course 12: Graduation Project                              │
│  └─> Needs: ALL courses (01-11)                           │
│      └─> Capstone: Apply everything learned                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔗 Key Dependencies | التبعيات الرئيسية

### Course 01 → Course 02
**Connection:** AI concepts → Python implementation
- Course 01 teaches AI theory
- Course 02 implements AI algorithms in Python

### Course 02 → Course 03
**Connection:** Python skills → Mathematical foundations
- Course 02 provides Python programming
- Course 03 uses Python for mathematical computations

### Course 03 → Course 04
**Connection:** Math foundations → ML algorithms
- Course 03 provides linear algebra, calculus, probability
- Course 04 uses these for ML algorithms

### Course 04 → Course 05
**Connection:** ML basics → Data science
- Course 04 teaches ML algorithms
- Course 05 applies ML to data science workflows

### Course 04 → Course 08
**Connection:** ML basics → Deep learning
- Course 04 provides ML foundation
- Course 08 extends to deep neural networks

### Course 07 → Course 08
**Connection:** NLP → Deep learning for NLP
- Course 07 introduces NLP concepts
- Course 08 uses deep learning for NLP (RNNs, Transformers)

### Course 08 → Course 09
**Connection:** Deep learning → Deep RL
- Course 08 provides neural network knowledge
- Course 09 uses deep learning for RL (DQN, Actor-Critic)

### Course 08 → Course 10
**Connection:** Deep learning → Generative models
- Course 08 provides neural network foundations
- Course 10 uses deep learning for generation (GANs, VAEs)

### All Courses → Course 11
**Connection:** All knowledge → Deployment
- Course 11 requires knowledge from all previous courses
- Applies everything to production deployment

### All Courses → Course 12
**Connection:** Complete program → Capstone project
- Course 12 is the graduation project
- Requires all knowledge from Courses 01-11

---

## 📚 Skill Progression | تطور المهارات

### Semester 1 Skills:

**After Course 01:**
- ✅ Understand AI concepts
- ✅ Know search algorithms
- ✅ Understand knowledge representation

**After Course 02:**
- ✅ Python programming for AI
- ✅ Implement algorithms
- ✅ Work with data structures

**After Course 03:**
- ✅ Mathematical foundations
- ✅ Linear algebra, calculus, probability
- ✅ Ready for ML algorithms

**After Course 04:**
- ✅ Build ML models
- ✅ Regression, classification, clustering
- ✅ Model evaluation

**After Course 05:**
- ✅ Data science workflows
- ✅ Data processing, visualization
- ✅ Scalable data science

**After Course 06:**
- ✅ AI ethics understanding
- ✅ Bias detection
- ✅ Responsible AI development

### Semester 2 Skills:

**After Course 07:**
- ✅ Natural language processing
- ✅ Text processing, embeddings
- ✅ NLP applications

**After Course 08:**
- ✅ Deep learning
- ✅ CNNs, RNNs, Transformers
- ✅ Neural network training

**After Course 09:**
- ✅ Reinforcement learning
- ✅ Q-learning, Deep RL
- ✅ RL applications

**After Course 10:**
- ✅ Generative AI
- ✅ GANs, VAEs, Diffusion models
- ✅ Content generation

**After Course 11:**
- ✅ Model deployment
- ✅ MLOps, cloud platforms
- ✅ Production systems

**After Course 12:**
- ✅ Complete AI project
- ✅ End-to-end implementation
- ✅ Professional portfolio

---

## 🎯 Learning Paths | مسارات التعلم

### Path 1: Complete Beginner
```
Course 01 → Course 02 → Course 03 → Course 04 → Course 05 → Course 06
    ↓
Course 07 → Course 08 → Course 09 → Course 10 → Course 11 → Course 12
```

### Path 2: Python Experience
```
Review Course 01 → Course 02 → Course 03 → Course 04 → Course 05 → Course 06
    ↓
Course 07 → Course 08 → Course 09 → Course 10 → Course 11 → Course 12
```

### Path 3: ML Experience
```
Review Courses 01-03 → Course 04 → Course 05 → Course 06
    ↓
Course 07 → Course 08 → Course 09 → Course 10 → Course 11 → Course 12
```

---

## ⚠️ Important Notes | ملاحظات مهمة

### Don't Skip Courses:
- Each course builds on previous ones
- Skipping will create knowledge gaps
- You'll struggle in later courses

### Complete Units in Order:
- Units within courses are sequential
- Later units use concepts from earlier units
- Don't jump ahead

### Prerequisites Matter:
- Check prerequisites before starting each course
- Review previous courses if needed
- Ensure you have required knowledge

---

## 🔄 Review Recommendations | توصيات المراجعة

### Before Starting Course 04:
- Review Course 03 (Mathematics)
- Ensure you understand linear algebra and probability

### Before Starting Course 08:
- Review Course 04 (ML Algorithms)
- Review Course 07 (NLP) if available
- Understand neural network basics

### Before Starting Course 10:
- Review Course 08 (Deep Learning)
- Understand CNNs, RNNs, Transformers
- Know how to train neural networks

### Before Starting Course 11:
- Review all previous courses
- Understand model training and evaluation
- Know deployment concepts

### Before Starting Course 12:
- Review entire program
- Understand all concepts
- Be ready for independent project

---

## 📊 Course Connections Matrix | مصفوفة اتصالات الدورات

| Course | Depends On | Used By | Key Concepts |
|--------|------------|---------|--------------|
| **01** | None | 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12 | AI foundations |
| **02** | 01 | 03, 04, 05, 06, 07, 08, 09, 10, 11, 12 | Python skills |
| **03** | 02 | 04, 05, 08, 09, 10, 11, 12 | Math foundations |
| **04** | 01-03 | 05, 06, 07, 08, 09, 10, 11, 12 | ML algorithms |
| **05** | 04 | 06, 07, 08, 09, 10, 11, 12 | Data science |
| **06** | 01-05 | 07, 08, 09, 10, 11, 12 | AI ethics |
| **07** | 01-06 | 08, 09, 10, 11, 12 | NLP |
| **08** | 01-07 | 09, 10, 11, 12 | Deep learning |
| **09** | 01-08 | 10, 11, 12 | Reinforcement learning |
| **10** | 01-09 | 11, 12 | Generative AI |
| **11** | 01-10 | 12 | Deployment |
| **12** | 01-11 | None | Capstone project |

---

## 💡 Tips for Navigation | نصائح للتنقل

1. **Follow the Sequence**
   - Complete courses in order (01 → 12)
   - Don't skip ahead

2. **Review When Needed**
   - Review previous courses if you're stuck
   - Check prerequisites regularly

3. **Track Your Progress**
   - Use progress checklists
   - Know where you are in the program

4. **Understand Connections**
   - See how courses build on each other
   - Understand why order matters

5. **Ask Questions**
   - If you don't understand connections
   - Consult course documentation
   - Ask instructors/peers

---

**Last Updated:** January 2025  
**Status:** Complete Navigation Guide
