# Case Study 01: Zillow Offers
## Choosing a model that decides which houses to buy

**Course:** Course 04 — AIAT 114, Machine Learning Algorithms and Applications
**Type:** Case-study analysis (official assessment instrument)
**Points:** 100, scaled to 10 of the course's 100
**Effort:** one hour. 10 min reading · 15 min collecting numbers from your own notebook runs · 30 min writing · 5 min checking
**Length:** 1,200–1,500 words. Individual work.

---

## 1. The situation

### What happened

Zillow's *Zestimate* is a house-price regression model. For years it was advice printed on a web
page. In 2018 Zillow began trading on it: **Zillow Offers** made algorithmic cash offers on homes,
bought them, repaired them and resold them. The prediction stopped being advice and became the
purchase price.

On **2 November 2021** Zillow announced it was winding the business down. From the company's own
third-quarter results release that day:

| Fact | Figure |
|---|---|
| Homes segment income (loss) before income taxes, Q3 2021 | **$(421.6) million** |
| Inventory write-down, Q3 2021 | **~$304 million** — homes bought "at higher prices than the company's current estimates of future selling prices" |
| Additional losses expected in Q4 2021 | **$240–265 million** |
| Workforce reduction announced | **approximately 25%** |

CEO Rich Barton's stated reason: *"We've determined the unpredictability in forecasting home prices
far exceeds what we anticipated."*

### The part that is not in the headline

The model was not stupid, and this is the whole reason the case is worth your hour. Zillow bought a
house when its estimate was **high relative to the seller's asking price**. That rule does not
sample houses at random. It selects, systematically, the houses where the model erred *upward*.

A model can have an excellent average error and a terrible error on the subset it chose. Average
performance is measured on data somebody else selected; deployed performance is measured on data
**the model selected for you**. Nothing in R², MAE, or a cross-validation score can see that
difference, because none of them know what you are going to do with the number.

**Source:** Zillow Group, Inc., *Zillow Group Reports Third-Quarter 2021 Financial Results & Shares
Plan to Wind Down Zillow Offers Operations*, 2 November 2021 (filed as an exhibit to Form 8-K, SEC
EDGAR, accession 0001617640-21-000085). All four figures and the quotation above are from that
release.

---

## 2. The decision you must make

You are the ML lead at a Saudi property platform. Your board has read about Zillow and wants the
opposite outcome from the same idea: an **instant-offer** product that quotes a cash price on a
listed home within 60 seconds.

You have the platform's own historical listing and transaction data. You have 90 days. The board
wants one recommendation from you, in writing, and they will act on it.

**Choose exactly one and defend it:**

- **A — Ship an automated buying model.** You must state the decision rule, the metric that gates
  it, and the number at which the system refuses to bid.
- **B — Ship the estimate as advice only.** A human makes every purchase decision. You must say
  what the human contributes that the model does not, and what evidence you have for that claim.
- **C — Do not ship.** You must say who pays for that, and what specific measurement would change
  your mind.

There is no correct option. There are defensible arguments and indefensible ones, and the
difference is whether you brought numbers.

---

## 3. Evidence you must bring from this course

Your analysis must cite **at least three** of the following by notebook filename, with the number
from **your own run** (they will differ slightly from the figures quoted here, and where they do,
report yours). An analysis that argues from principle alone cannot pass Section 1 or Section 5.

| Notebook | What it gives you |
|---|---|
| `unit1-regression-algorithms/examples/04_linear_regression.ipynb` | A fitted, plotted, respectable-looking model with **R² = 0.0033** and **MAE $95.87** on a target whose mean is **$84.96**. A regression model always returns a number, and it looks identical when it is right and when it is worthless. |
| `unit1-regression-algorithms/examples/05_polynomial_regression.ipynb` | Degree 10: **train R² 0.9548, test R² −6.1214**. The model that fits history best is often the one most wrong about next week. |
| `unit1-regression-algorithms/examples/06_ridge_lasso_regression.ipynb` | The best Ridge setting was the smallest α tried — "regularize as little as possible". At α = 100 Lasso keeps 1 of 29 features and R² collapses from **0.893 to 0.066**, silently. |
| `unit2-regression-model-evaluation/examples/01_cross_validation.ipynb` | One split reports **R² = 0.1095**; ten splits of the same data with the same model report **0.0402 to 0.1259**, mean **0.0836**. If you report the first number you reported the split, not the model. |
| `unit2-regression-model-evaluation/examples/02_bias_variance_learning_curves.ipynb` | Degree 1 (train MSE 1936.53 / val 2161.84) and degree 15 (292.33 / 42429.78) need **opposite** interventions. One number cannot tell them apart; a learning curve can. |
| `unit3-classification/examples/01_logistic_regression.ipynb` | Buy / don't-buy is a **threshold**, and a threshold is a price on two kinds of error. `class_weight='balanced'` left recall at 0.50 and dropped precision from 0.50 to 0.14 — three false alarms became eighteen, and nothing about the model changed. |
| `unit5-model-selection/examples/01_grid_search.ipynb` | **540 cross-validated fits all reported 100%.** A single `groupby` found the leak that made every one of them meaningless. Search optimises a number; it cannot audit it. |
| `unit2-regression-model-evaluation/enrichment/E10_conformal_prediction_in_twenty_lines.ipynb` | A point estimate cannot support a bid. An interval can. Also the Epic Sepsis Model: vendor-reported AUC 0.76–0.83, externally measured **0.63**, alerting on **18%** of hospitalizations at a positive predictive value of **12%**. |

---

## 4. Analysis questions

These have no single right answer. Answer all five inside the five sections in §5 — the mapping is
in the table there.

**Q1 — The selection problem.** Explain, in language a non-technical board member will follow, how
a model with a good MAE across all houses can have a bad MAE **on the houses it chose to buy**.
Then propose a measurement: using data you actually have, how would you estimate the size of that
gap *before* spending anything? (Hint: you can apply the buying rule retrospectively to sold homes
and score the model only on the ones the rule would have selected.)

**Q2 — From a number to an offer.** Your model returns 1,420,000 SAR. Write the decision rule that
turns that into an offer or a refusal to bid. Now suppose the model's honest 90% prediction interval
is ±35% (`E10`). Does your rule survive? If it does not, is the correct response a better model, a
narrower product, or no product?

**Q3 — Which diagnostic would have caught it.** Barton's sentence blames *unpredictability*, not a
bug. Go through the diagnostics in Units 1 and 2 and sort them into two lists: those that would have
warned Zillow before deployment, and those that would have stayed green the entire way. Name at
least one in the second list and say why it was structurally blind.

**Q4 — Your recommendation and its price.** Commit to A, B or C from §2. Then argue the strongest
case *against* your own choice, and say what it would cost the business if you are wrong. If you
chose B, state what evidence you have that a human appraiser beats the model — and if you have none,
say so and say how you would get it.

**Q5 — Turning riyals into a metric.** Your board will tolerate an expected loss of at most
X riyals per home purchased. Convert that ceiling into a threshold on a metric from this course, and
explain why R² cannot carry it. Choose X yourself and defend the choice.

---

## 5. What you submit

One document, five sections, marked out of 100.

| Section | Points | Feeds from |
|---|---:|---|
| 1. Problem analysis | 20 | Q1, Q3 |
| 2. Solution design | 25 | Q2 |
| 3. Implementation plan | 25 | Q2, Q4 |
| 4. Evaluation | 15 | Q5, Q1 |
| 5. Recommendations, limits and ethics | 15 | Q4 |

### What a strong answer contains

This is a description of **properties**, not of content. Two students can recommend opposite things
and both score full marks.

- **A constraint the brief did not state.** The brief gives you 90 days, historical platform data
  and a 60-second quote. A strong Section 1 names something else that binds — regulatory, financial,
  data-availability, or organisational — and says how it was inferred.
- **Success defined as a number with a target**, never as "high accuracy". A metric, a threshold,
  and a sentence saying what happens when the threshold is missed.
- **An alternative considered and rejected, with the reason.** A design that names only what it
  chose has not been designed.
- **A baseline that appears before the real model in the plan.** For this problem the baseline is
  cheap and it is not zero: last sale price adjusted by a regional index, or the median price per
  square metre in the district. If your plan cannot beat that, it has no product in it.
- **Something that happens after deployment.** A monitor, a retraining trigger, a rollback, and the
  named person who receives the alert.
- **Two limitations that would genuinely make your proposal fail**, and what you would do about
  each. "More data would help" is true of every project ever written and earns nothing.
- **Who is affected who never uses the system** — the seller who accepts a low automated offer, the
  district whose prices your bidding moves, the appraiser whose job the product replaces.
- **At least two references to this course's own material**, by filename, with your own numbers.

### Rules

- Submit markdown or PDF. Code is optional; if you include a snippet it must match your written
  design.
- Over the word count by more than 25% loses marks. Length is not the deliverable.
- If you used an AI assistant, declare it in one line at the end: which tool, for what. Declared
  assistance is permitted. You will be asked to walk through your Section 3 plan aloud.

---

## 6. Sources

- Zillow Group, Inc., *Zillow Group Reports Third-Quarter 2021 Financial Results & Shares Plan to
  Wind Down Zillow Offers Operations*, 2 November 2021. Filed as an exhibit to Form 8-K, SEC EDGAR.
- Wong, A., Otles, E., Donnelly, J. P., et al., "External Validation of a Widely Implemented
  Proprietary Sepsis Prediction Model in Hospitalized Patients", *JAMA Internal Medicine*, 2021.
  doi:10.1001/jamainternmed.2021.2626 (the Epic figures in `E10`).
- Kaufman, S., Rosset, S., Perlich, C. & Stitelman, O., "Leakage in Data Mining: Formulation,
  Detection, and Avoidance", *ACM TKDD* 6(4), 2012 (the leakage result in `01_grid_search`).

**For:** Course 04 — AIAT 114
