# Case Study 01: Mathematical Modeling
## Reviewing a risk model whose numbers are too good

**Course:** Course 03 – AIAT 113 (Mathematics and Probability for Machine Learning)
**Type:** Case Study Analysis
**Points:** 100 (scaled to 10 of the course's 100 marks)
**Set:** session 28 · **Due:** session 32
**Length:** 1,200–1,500 words. Code optional; if you include any, it is evidence, not a separate mark.
**Time budget:** about one hour — 15 minutes reading and re-running one cell in one notebook, 45 minutes writing.

---

## 1. The situation

This is a documented case, and this course teaches it in
`unit4-dimensionality-reduction/examples/03_feature_selection.ipynb`.

In the late 1990s, microarray studies began reporting classifiers that separated cancer from healthy tissue
at **near-zero error** — from a few thousand genes and a few dozen patients. In **2002 Christophe Ambroise
and Geoffrey McLachlan** published *"Selection bias in gene extraction on the basis of microarray
gene-expression data"* in *PNAS* (99(10)). The flaw they found was in the procedure, not in the biology.

The studies chose which genes to use by scoring all of them against the **entire** dataset, and only then ran
cross-validation on the classifier. By that point the held-out samples had already influenced which genes
existed at all. The reported error rate was biased downward. An honest estimate requires the gene selection
to be repeated **inside every cross-validation fold** — and when it is, the error rates go up.

Read the shape of that failure carefully, because it is the reason this brief exists: **the mistake produces
good news.** There is no crash, no warning, and the number that comes out is the number you wanted.

**Your own course notebook commits this error on purpose, where you can see it.** In
`03_feature_selection.ipynb`, `f_classif(X, y)` scores all ten features using every row, the top five are
chosen, and only then does `cross_val_score` split the data. That notebook's limits section also records the
honest comparison it printed: 5-fold accuracy with **all ten** features **0.933**, with the **top five**
**0.914** — a difference of **−0.019**. Selecting the "best" features made the model worse.

Four more results from this course belong beside it:

- **Summary statistics do not determine the picture.** Anscombe (1973) published four datasets sharing the
  same mean, variance, correlation, regression line y = 3.00 + 0.500x and R² = 0.67, and looking nothing like
  each other. See `unit3-optimization/examples/03_statistical_measures.ipynb`.
- **Near-duplicate columns break the arithmetic silently.** Longley (1967) ran one ordinary regression —
  16 observations, 6 predictors — through the statistical packages of the day and they disagreed, some in the
  leading digit, because the predictors moved together. See
  `unit1-linear-algebra/examples/05_determinants_inverse_matrices.ipynb`, which builds a matrix with
  determinant −0.0002 and inverse entries near 20,000, and prints no error.
- **"Nearest" can stop meaning anything.** Beyer, Goldstein, Ramakrishnan and Shaft (1999) showed that under
  broad conditions, as dimensions grow, the distance to the nearest neighbour converges toward the distance to
  the farthest. See `unit4-dimensionality-reduction/examples/02_curse_dimensionality.ipynb`.
- **A significant result is not a true one.** The Open Science Collaboration (2015, *Science*) repeated 100
  psychology studies; of the 97 that had reported a statistically significant effect, **36%** produced a
  significant result on replication. See `unit5-probability/examples/07_hypothesis_testing_procedures.ipynb`.

**Sources.** Ambroise and McLachlan, *PNAS* 99(10), 2002 · Anscombe, *The American Statistician*, 1973 ·
Longley, *Journal of the American Statistical Association* 62(319), 819–841, 1967 · Beyer, Goldstein,
Ramakrishnan and Shaft, *When Is "Nearest Neighbor" Meaningful?*, ICDT, 1999 · Open Science Collaboration,
*Estimating the reproducibility of psychological science*, *Science*, 2015 · Hoekstra, Morey, Rouder and
Wagenmakers, *Robust misinterpretation of confidence intervals*, *Psychonomic Bulletin & Review*, 2014.

---

## 2. The decision you have to make

You work in the risk team of a lender. A colleague has built a **default-risk score** and hands you the
report the day before it goes to the credit committee. It says:

- **900 applicants** in the historical file, **4,100 candidate variables** assembled from application forms,
  bureau data and transaction summaries;
- the 40 strongest variables were selected by scoring every variable against the outcome across the full
  file, then a logistic model was fitted on those 40;
- **10-fold cross-validated accuracy 0.94**; **R² = 0.87** on the continuous loss-given-default model that
  accompanies it;
- **no residual plot**, no confusion matrix, no baseline;
- four of the 40 selected variables are, on inspection, three measurements of the same quantity plus its
  twelve-month moving average;
- one variable is a neighbourhood-level index the vendor documents as "an area affluence score";
- the report's final line: *"We are 95% confident that portfolio loss will be between 2.1% and 3.4%."*

The committee chair has asked you one question: **sign it off, send it back with required changes, or reject
the approach.** If your answer is anything other than "reject", you must also specify the corrected
evaluation protocol and the plan to redo the work.

There is no correct answer. All three verdicts can score full marks. What is marked is whether your reasoning
would survive the committee.

---

## 3. The evidence you must bring

Your analysis must **cite at least three of this course's own notebooks by filename**, and quote a specific
number or result from each. An analysis with no course evidence cannot pass the middle of the mark range.

| Question you have to answer | Where the course already answered it |
|---|---|
| Why is 0.94 not an estimate of anything? | `unit4/03_feature_selection.ipynb` — the Ambroise–McLachlan error, and the notebook's own admission that it commits it |
| Does selecting features even help? | `unit4/03_feature_selection.ipynb` — all ten features 0.933, top five 0.914, difference −0.019 |
| What is R² = 0.87 worth without a plot? | `unit3/03_statistical_measures.ipynb` — Anscombe's four datasets, one R² |
| What do four near-duplicate columns do? | `unit1/05_determinants_inverse_matrices.ipynb` — determinant −0.0002, inverse entries near 20,000, no error message |
| Is a 4,100-column distance meaningful? | `unit4/02_curse_dimensionality.ipynb` — nearest and farthest neighbour converge |
| Should I trust the selected variables' p-values? | `unit4/03_feature_selection.ipynb` — with 569 samples, p = 8.47 × 10⁻⁹⁶ means "not exactly zero" and nothing more |
| What does that final sentence actually claim? | `unit5/08_pvalues_confidence_intervals.ipynb` — 120 researchers were given six statements about a 95% interval, all six false, and endorsed more than three on average |
| How wide is the fold-to-fold spread? | `unit5/02_statistical_inference.ipynb` — building an interval around a cross-validated mean |
| Can a column encode an assumption rather than a measurement? | `unit3/04_regression_real_datasets.ipynb` — why this course does not use the Boston housing data, and what its `B` column was |
| What does dropping to a handful of components cost? | `unit4/01_pca_implementation.ipynb` — what a principal component is and is not |

> Paths in the table are abbreviated. `unit4/03_feature_selection.ipynb` means
> `unit4-dimensionality-reduction/examples/03_feature_selection.ipynb`; the unit folder names are in the
> course README.

---

## 4. What you submit

Five sections, in this order.

**1. Problem analysis.** What is actually wrong, stated in one sentence the committee chair would understand?
Which of the report's numbers can be believed and which cannot, and why? Name at least one problem the brief
above does not point at. Say what "good enough to lend on" would mean as a measurable criterion.

**2. Solution design.** Specify the corrected modelling and evaluation protocol: where selection sits
relative to the split, what the outer estimate is, how you handle 4,100 columns against 900 rows, and what
you do about the collinear group. Name one alternative you considered and rejected — a simpler model, a
smaller variable set, more data, or not modelling this at all.

**3. Implementation plan.** Five to eight ordered steps someone could start on Monday. Include a **baseline**
before the model — what does the lender's current rule-of-thumb score, on the same protocol? Include the
diagnostics you would require before anything is shown to the committee again, and the checks that would run
every quarter after it is live.

**4. Evaluation.** Which numbers you would require and why, including why accuracy is the wrong headline for
this problem. State the uncertainty you would report and the **exact sentence** in which you would report it.
Say what you would measure besides model quality.

**5. Recommendation, limits and ethics.** Your verdict in one sentence. Then two limitations of your **own**
corrected protocol that would genuinely make it fail, with a response to each. Then: the model decides who
gets credit. Say what the "area affluence score" is doing in the model, and what you would need to know
before allowing it.

---

## 5. Analysis questions

Answer these inside your five sections; do not answer them as a separate list. None has a single right
answer, and two students who disagree can both be right.

1. **The reported 0.94 is biased upward and you cannot say by how much.** Argue for the direction and rough
   size of the correction using measured numbers from a named notebook — and then say clearly why you cannot
   give the committee an exact corrected figure without rerunning the work. Which of those two statements is
   harder to say out loud in a committee, and why does it matter that you say it?

2. **R² = 0.87, no residual plot.** Describe two genuinely different datasets that could produce that number,
   and say which single diagnostic you would demand first. Then answer the harder question: when the
   corrected protocol returns a lower R², what exactly has got worse? Be precise, because the committee will
   hear "the model got worse" and act on it.

3. **Four of the forty variables measure the same quantity.** The p-values on all four are tiny. What does
   the condition number of the design matrix tell you that the p-values cannot? Would you drop three of the
   four, combine them, or keep them and change the fitting method? Defend the choice you make, including its
   cost.

4. **"We are 95% confident that portfolio loss will be between 2.1% and 3.4%."** Rewrite that sentence so it
   is correct. Then say what changes for the committee when they read your version instead — and what a
   member who wanted the original sentence is actually asking for.

5. **One column is an "area affluence score".** With 4,100 columns you cannot read them all. Describe a
   procedure you would actually run to find the columns that encode an assumption about people rather than a
   measurement of them — before `fit()`, not after deployment. Say what your procedure would miss.

---

## 6. What a strong answer contains

This is not a list of the right answers. It is what the marker is looking for.

- **The selection-bias diagnosis, stated precisely.** Not "there might be overfitting" but *which* step saw
  *which* rows, and what that does to the number.
- **A problem the brief did not point at.** There is more than one. Finding one is worth more than any
  technique you can name.
- **A baseline.** The lender already scores applicants somehow. A corrected protocol that compares the new
  model to nothing has repeated the mistake in a new costume.
- **An alternative considered and rejected**, with the reason — including "fewer variables and a model the
  committee can read".
- **Named course evidence.** Three notebooks, three specific numbers, used to carry an argument rather than
  decorate one.
- **A correctly worded uncertainty statement.** One sentence, and it is the sentence the whole report is
  judged on outside this room.
- **Two limitations of your own proposal** that would genuinely sink it, each with a response. "More data
  would help" is true of every project ever written and earns nothing.
- **A named consequence for a real applicant** when the score is wrong, in the direction it is most often
  wrong.

"There are no ethical concerns" is not an available answer on a brief about who gets credit.

---

## Submission

- Markdown or PDF, 1,200–1,500 words. Code snippets, if any, go in an appendix outside the word count.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared use is
  permitted; you will be asked to talk through your section 3 aloud.
- Submit by session 32.

---

**For:** Course 03 – AIAT 113 · Mathematics and Probability for Machine Learning
