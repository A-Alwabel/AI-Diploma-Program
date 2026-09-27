# Case Study 01: The metric was hit and the goal was missed
## Reading the Netflix Prize before you write your own success criterion

**Course:** Course 12 — AIAT 126, Graduation Project
**Type:** Case-study analysis (official assessment instrument). **In this course it carries no separate mark:** the analysis is marked inside **gate 1** (proposal — criteria 1.2 and 1.6) and **gate 5** (final report — criteria 5.3 and 5.4). `PROJECT_GUIDELINES.md` has the gate weights.
**When:** read in Unit 1, before the proposal is due (end of week 2); revisited in Unit 5 when you write the report's Discussion.
**Effort:** one hour. 10 min reading · 15 min collecting numbers from your own notebook runs · 30 min writing · 5 min checking
**Length:** 600–900 words, submitted as the **Risk assessment** section of your proposal, and revised into the **Discussion** of your report. Team projects submit one analysis, signed by every member.

---

## 1. The situation

### What happened

In October 2006 Netflix offered **$1,000,000** to the first team to improve its rating-prediction
algorithm, Cinematch, by 10% on root-mean-square error. Cinematch scored 0.9514 on the quiz set.
Thousands of teams competed for three years.

| Fact | Figure |
|---|---|
| Prize awarded | **21 September 2009**, to *BellKor's Pragmatic Chaos*, for a **10.06%** improvement (RMSE 0.8567) |
| The winning solution | an ensemble blending **hundreds** of predictive models |
| What Netflix did with it | never put it into production |
| Netflix's own reason, 2012 | *"the additional accuracy gains that we measured did not seem to justify the engineering effort needed to bring them into a production environment"* |
| What did ship | two components of an earlier prize entry — an SVD and a restricted Boltzmann machine |
| What had changed by 2009 | Netflix had become a streaming company; predicting a five-star rating for a DVD arriving in three days was no longer the thing the business needed |
| The sequel | cancelled in March 2010 after a privacy lawsuit and FTC concern — the anonymised ratings had been re-identified |

### The part that is not in the headline

The objective was perfectly well defined, publicly announced, independently measured and met.
The goal — a recommender that made the business better — was missed, because the objective had
been written down in 2006 for a business that no longer existed in 2009, and because nobody had
priced the engineering that turns a number into a product.

This course puts three more cases beside it in
`unit1-project-planning/examples/01_project_proposal_literature_review.ipynb`: Zillow Offers, whose
pricing model met its metric and lost $304.4 million in a quarter; Google Flu Trends, which predicted
more than double the CDC's flu rate after the assumption under its objective expired; and MD
Anderson's Oncology Expert Advisor, contracted at $2.4 million for six months and audited at
$62.1 million and no clinical use four years later. Different industries, one pattern: **the goal
that was written down and the goal that mattered were not the same goal.** Your proposal is where
that gap closes, or does not.

**Sources:** Amatriain, X. & Basilico, J., *Netflix Recommendations: Beyond the 5 Stars (Part 1)*,
Netflix Technology Blog, April 2012 (the "engineering effort" sentence, the SVD/RBM detail and the
streaming shift); the Netflix Prize rules and results as summarised on the competition's record
(October 2006 launch, $1 million, 10% target, Cinematch 0.9514, 21 September 2009 award, 10.06%,
RMSE 0.8567, March 2010 cancellation). The Zillow, Google Flu and MD Anderson figures are sourced
in the notebook named above.

---

## 2. The decision you must make

This case is about **your** project. You do not choose between vendors; you choose how the
sentence "the project succeeded" will be written at gate 1, so that it can be tested at gate 4 and
defended at gate 6.

**Choose exactly one form for your success criterion and defend it:**

- **A — One offline metric with a threshold.** "F1 ≥ 0.80 on the held-out test set." You must say
  what the threshold is worth to the person who uses your system, and what would make you refuse to
  ship even if you hit it.
- **B — An offline metric plus a "worth it" test.** The metric, *and* the baseline it must beat by
  a stated margin, *and* the rule for stopping: the gain per day of work below which you stop
  tuning and start evaluating. You must put numbers on all three.
- **C — An outcome measured with real users.** A task completed faster, an error caught, a
  decision changed — measured in a small trial. You must state the sample size, what it will cost
  you in calendar weeks, and what you will do if the trial cannot run.

There is no correct option. There are defensible arguments and indefensible ones, and the
difference is whether you brought numbers — from this course, and from your own project.

---

## 3. Evidence you must bring from this course

Your analysis must cite **at least three** of the following by notebook filename, with the number
from **your own run** (they will differ slightly from the figures quoted here, and where they do,
report yours). Where your own project already has numbers, put them beside the course's.

| Notebook | What it gives you |
|---|---|
| `unit1-project-planning/examples/01_project_proposal_literature_review.ipynb` | MD Anderson: $2.4 million and six months contracted; $39.2 million to IBM after 12 extensions; $62.1 million to all external firms; **25.9×** the cost and **8.0×** the schedule, with no clinical use. The 14-week template plans **0 weeks** for gate 2 (10 points) and 57.1% of the calendar for gate 3 (35.3% of the marks). The storyboard: every week the data phase overruns comes out of the *last* milestone. |
| `unit3-model-development/examples/02_model_training_hyperparameter_optimization.ipynb` | Majority class 0.6145 → default forest **0.8045** (+0.1899). Then **540 fits** of grid search: cross-validated F1 +0.0282, validation accuracy **−0.0112** — 17× smaller than the baseline gain, and in the wrong direction. All 108 configurations sit within 0.0355 of each other; 2 of 4 winners sit at the edge of their grid. |
| `unit4-evaluation-optimization/examples/01_model_evaluation_optimization.ipynb` | Validation F1: logistic 0.7176, forest 0.7612, SVM **0.7903**. Threshold tuning bought +0.0125 on a plateau where 77 of 181 cut-offs sit within 0.03 of the peak. On the untouched test set: F1 **0.7302**, accuracy 0.8101 — a gap of −0.0823 from validation — with a 95% bootstrap interval on F1 of **0.6346–0.8102 (±8.8 points)** from 179 rows. Epic's sepsis model: vendor AUC 0.76–0.83, external 0.63, 1,709 of 2,552 patients missed. |
| `unit2-system-design-architecture/examples/01_system_design_architecture.ipynb` | The decision matrix, weights fixed before scoring, put its top two candidates at **4.85 against 4.70** — 0.15 on a five-point scale, which is no gap at all. Design-time evidence on validation: logistic 0.8034, tree 0.8146. The diagram checker refused to draw an arrow to an undeclared component. |
| `unit4-evaluation-optimization/enrichment/E2_one_success_isnt_reliability.ipynb` | Six steps with a mean reliability of **93%** finish correctly **64%** of the time. Ten successes out of ten gives a Wilson interval of **[0.722, 1.000]**. A published pass@1 of 0.6536 next to a pass^20 of 0.2525 is **1,247×** what independence predicts — a system that owns some tasks and cannot do others, averaged into one number that describes neither. |

---

## 4. Analysis questions

These have no single right answer. Answer all five; the mapping to the proposal and the report is
in §5.

**Q1 — The goal that was written down.** Netflix, Zillow, Google Flu and Watson each had a written
objective that was met or measurable, and a real goal that was missed. Write your project's
objective exactly as it stands in your proposal draft. Under it, write the goal behind it in one
sentence a non-specialist would use. Then name the specific way the two can diverge for *your*
project — the assumption that can expire, the metric that can be hit by a useless model.

**Q2 — The worth-it line.** Netflix refused hundreds of models' worth of accuracy. Using
`02_model_training_hyperparameter_optimization` (540 fits bought −0.0112 on validation) and
`01_model_evaluation_optimization` (a +0.0125 plateau), write the rule for your project: the gain
per day of work below which you stop tuning. Then answer the question a client asks instead: what
does 0.01 of your metric *do* for the person using your system? If you cannot answer it, say what
that tells you about the metric.

**Q3 — The number you will defend.** Your test set will be small. Using the bootstrap in
`01_model_evaluation_optimization` (179 rows, ±8.8 points on F1) or the Wilson intervals in `E2`,
compute the interval you should expect at *your* planned test-set size. Rewrite your success
criterion so that it survives that interval — a threshold the lower bound must clear, not the point
estimate.

**Q4 — Calendar against marks.** The template plans 0 weeks for gate 2 and 57% of the calendar for
gate 3. Re-plan your 14 weeks against the 85 gate points. Then name the milestone you will cut, by
name, if the data phase overruns by two weeks — before it happens, in writing, so that week 9 is a
decision you already made.

**Q5 — The failure you write down now.** Google Flu's objective outlived its assumption. Name the
assumption under your project that could expire between the proposal and the defence, the
measurement that would tell you it has, and what you will do in week 9 if it does. This paragraph
becomes the first entry in your report's Discussion.

---

## 5. What you submit, and where it is marked

There is no separate case-study mark in AIAT 126. The analysis is a **section of your proposal**
and is marked there; it is revised into your **report's Discussion** and marked again there.

| Where it goes | Gate criterion it feeds | Questions |
|---|---|---|
| Proposal — Objectives and success criteria | 1.2 Objectives and measurable success criteria | Q1, Q3 |
| Proposal — Risk assessment | 1.6 Timeline, resources and risk assessment | Q2, Q4, Q5 |
| Report — Discussion | 5.3 Results, analysis and critical discussion | Q2, Q3 |
| Report — Ethical, legal and social considerations | 5.4 Ethical, legal and social considerations | Q5 |

### What a strong answer contains

This is a description of **properties**, not of content.

- **A success criterion the examiner could fail you on.** A metric, a threshold on its *lower
  bound*, a test-set size, and the sentence that says what happens if it is missed. "High
  accuracy" cannot be failed and therefore cannot be passed.
- **A worth-it rule with a number in it**, and the client's question answered: what one unit of
  your metric does for one user.
- **A baseline that exists before your model.** The majority class, the rule a person uses today,
  the model from AIAT 114 you are reusing. If your criterion does not name what you must beat, it
  is not a criterion.
- **An assumption named, with its expiry test.** Not "the data may be noisy" — the specific thing
  about the world your project relies on, and the measurement that would show it gone.
- **A milestone you have already agreed to cut**, named, with the reason it is the one.
- **Two limitations that would genuinely make your project fail**, written at gate 1 and checked
  at gate 5. "More data would help" earns nothing at either gate.
- **At least three references to this course's own material**, by filename, with your own numbers.

### Rules

- The proposal template (`TEMPLATES/project_proposal_template.md`) is unchanged; this analysis fills
  its risk section rather than adding a new one.
- Over 900 words by more than 25% loses marks on 1.6. Length is not the deliverable.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared
  assistance is permitted. You will be asked, at the gate-2 design review, to say your success
  criterion aloud without notes.

---

## 6. Sources

- Amatriain, X. & Basilico, J., *Netflix Recommendations: Beyond the 5 Stars (Part 1)*, Netflix
  Technology Blog, April 2012.
- The Netflix Prize record (October 2006 launch; $1,000,000; 10% over Cinematch's 0.9514;
  BellKor's Pragmatic Chaos, 21 September 2009, 10.06%, RMSE 0.8567; sequel cancelled March 2010).
- Zillow Group, *Q3 2021 results and plan to wind down Zillow Offers*, Form 8-K, 2 November 2021.
- Lazer, D., Kennedy, R., King, G. & Vespignani, A., *The Parable of Google Flu: Traps in Big Data
  Analysis*, Science 343(6176), 2014.
- University of Texas System Audit Office, *Special Review of Procurement Procedures Related to the
  M.D. Anderson Cancer Center Oncology Expert Advisor Project*, November 2016.
- Wong, A. et al., *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model
  in Hospitalized Patients*, JAMA Internal Medicine, 2021.

All six are the sources already cited in the notebooks named in §3.

**For:** Course 12 — AIAT 126
