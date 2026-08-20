# AI Diploma - Student Handbook

Practical habits and workflows for getting the most out of the program.
For program structure and setup, see [STUDENT_GUIDE.md](STUDENT_GUIDE.md) and
[SETUP_GUIDE.md](SETUP_GUIDE.md).

**Last Updated:** 2026-08

---

## Getting Started

### Step 1: Set up your environment

1. Follow [SETUP_GUIDE.md](SETUP_GUIDE.md) end to end
2. Run the smoke test (Course 01's first notebook) on the `ai-diploma` kernel
3. Note the separate `tfenv` kernel for TensorFlow notebooks (Courses 01 and 08)

### Step 2: Understand the structure

- **Courses:** 12 courses (AIAT 111–126), two semesters, taken in order
- **Units:** each course has 5 units (`unit1-…` to `unit5-…`)
- **Examples:** numbered notebooks (`01_…`, `02_…`, …) in each unit's `examples/`
- **Exercises:** practice work in each unit's `exercises/`
- **Quizzes:** per unit, plus a course-level `QUIZZES/` folder
- **Assessments:** the course exam in `ASSESSMENTS/`
- **Templates:** `docs/TEMPLATES/` is instructor-only — not part of your path

### Step 3: Follow the one numbered path

```
START_HERE.md → examples 01 → NN → exercise → quiz → next unit … → assessment
```

There is exactly one path per course, and `START_HERE.md` spells it out.
**Solutions and answer keys are released by your instructor** — they are not in
this repository, so complete each exercise and quiz on your own first.

---

## How to Use the Notebooks

### Typical notebook structure

1. **Learning objectives** — what you will be able to do
2. **Prerequisites** — what you should already know
3. **Concepts** — explanation with visuals
4. **Code examples** — complete, runnable implementations
5. **Summary** — key takeaways

### Best practices

1. **Read first** — objectives and prerequisites before any code
2. **Run sequentially** — execute cells top to bottom; don't jump around
3. **Check the kernel** — `ai-diploma` for most notebooks; `tfenv` for
   TensorFlow notebooks in Courses 01 and 08
4. **Experiment** — change parameters and inputs to test your understanding
5. **Take notes** — add your own markdown cells and observations
6. **Revisit** — re-run earlier notebooks when a later topic depends on them

---

## Learning Tips

### If you are new to programming

- Start at Course 01, Unit 1, notebook 01 — the path assumes nothing
- Do not skip prerequisites; the numbering exists for a reason
- Type code out rather than copy-pasting when practicing

### If you have some experience

- Still follow the path, but move faster through familiar material
- Focus on the exercises — they reveal what you actually know
- Extend the examples: add a metric, try another dataset, break and fix things

### For everyone

- **Quizzes are checkpoints**, not obstacles — take each unit quiz before
  moving on, and revisit the unit if it goes badly
- **Assessments are rehearsals** for real-world work; treat them seriously
- Compare your exercise attempts with the instructor-released solutions when
  they arrive, and study the differences

---

## Tracking Progress

Each course has a `STUDENT_PROGRESS_CHECKLIST.md`:

- Mark completed examples and exercises
- Record quiz results
- Note what you want to revisit

Self-assessment questions after each unit:

- Can you explain the concept in your own words?
- Can you implement it without looking at the example?
- Can you apply it to a new problem?

---

## Getting Help

### Resources, in order

1. **The unit README** and the notebook's own explanation cells
2. **The course `START_HERE.md` and `README.md`**
3. **[TROUBLESHOOTING_GUIDE.md](TROUBLESHOOTING_GUIDE.md)** for environment and
   error issues
4. **Your instructor and peers** — see
   [COMMUNITY_RESOURCES.md](COMMUNITY_RESOURCES.md)

### Common issues

- **Import errors** → wrong kernel or missing install; see
  [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Notebook won't run** → restart the kernel and run cells from the top
- **Concept unclear** → re-run the previous numbered examples in that unit

---

## Time Management

- **Daily practice:** 1–2 hours of hands-on work beats passive reading
- **Weekly rhythm:** finish the unit you started; review before starting the next
- **Review sessions:** once a week, skim your notes and re-run one old notebook
- **Before quizzes:** redo the unit's exercise from scratch

---

## Graduation Project (Course 12)

- Choose a problem you care about and can finish with the skills from
  Courses 01–11
- Follow `Course 12/PROJECT_GUIDELINES.md` and the Course 12 `START_HERE.md`
- Phases: planning → data → development → evaluation → documentation and
  presentation
- Reuse your own completed notebooks from earlier courses as building blocks —
  this is why keeping your modified notebooks matters

---

## Final Notes

- **Persistence** — learning AI takes time; steady beats fast
- **Honesty** — do the work before looking at released solutions
- **Portfolio** — your completed exercises and project are your portfolio
- **Community** — help others; explaining a concept is the best way to learn it

Good luck with your AI Diploma journey!
