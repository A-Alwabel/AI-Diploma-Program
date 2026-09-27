# The review form

One form per artefact. Copy the template in §2 into a file called `REVIEW_<your-initials>.md`
next to the work (or into the pull-request description if the work is a branch), fill every
slot, and run your own text against the rules in §3 before you hand it in. §4 and §5 show a
strong review and a weak review written on the same real notebook from this repository, with
every struck sentence explained.

**The form has no field for general comments.** That is deliberate. Every sentence you write
must sit next to a location in the work and an observation made there. If you find yourself
wanting to write something that has no location, it is not a review; it is an opinion, and this
form has no slot for it.

---

## 1. How to name a location

A location is precise enough that a stranger opens the work and is looking at the right thing in
under ten seconds. Use the shape that fits the artefact:

| Artefact | Location shape | Example |
|----------|----------------|---------|
| Notebook cell | `<path> › "<section heading above it>" › cell starting "<its first line>"` | `examples/01_cross_validation.ipynb › "Step 1: Prepare Data for Modeling" › cell starting "# Prepare features (X) and target (y)"` |
| A line inside a cell | the cell, then `› line "<the line, verbatim>"` | `… › line "X_scaled = scaler.fit_transform(X)"` |
| A printed output | the cell, then `› output line "<the printed line, verbatim>"` | `… › output line "Mean R²: 0.0844 (8.4%) (+/- 0.0358)"` |
| A figure | the cell that draws it, then which panel / series / label | `… cell starting "# CELL: Visualise the k-fold SPLIT" › right panel, fold 3` |
| A source file | `<path>:<line>` at a named commit | `src/preprocess.py:41 @ 3f9c2a1` |
| A written document | `<file> › <section> › paragraph <n> › "<first six words of the sentence>"` | `analysis.md › 4. Evaluation › ¶2 › "Accuracy of 97% shows the model"` |

Always record the commit or tag the work was reviewed at. Work changes; the review must say what
it was looking at.

---

## 2. The template

**Length: 300–600 words.** Findings and checks only; the commentary in the worked example below is not part of a review.

```markdown
# Review of <artefact path>  @ <commit / tag>
Round: <1 | 2 | 3>   Reviewer: <name>   Date: <yyyy-mm-dd>
Environment: <kernel or Python version, OS>   Data line printed by the loader: "<paste it>"

## A. Reproduction
A1. What was run: <exact command, or "Kernel → Restart & Run All" on <file>>
A2. What happened: <one of the three>
    - ran to the end in <time>; last line printed by the last code cell: "<verbatim>"
    - stopped at <location>; last line of the traceback: "<verbatim>"
    - ran to the end, but <location> printed "<mine>" where the saved output says "<theirs>"
A3. The claim, in one sentence, in my own words: <what this work says it has done — no adjectives>

## B. Findings  (2 to 5; at most one cosmetic finding counts toward the two)
### B1
Location:   <one of the shapes in §1>
Observed:   <what is there — quote the line, paste the number, name the figure and what it shows>
Affects:    <which RESULT this changes and how — a metric, a figure, a conclusion or a decision;
             never a print line, comment or heading (R8)>
Change:     <the exact edit or check> → expected after the change: <output / number / line>
Severity:   <blocks | weakens | cosmetic — fixed by what "Affects" names, see R9>
### B2
(same five slots)

## C. Checks  (2 or more — things verified and found to hold, each against something outside the work: R10)
C1. Location: <…>  Compared: <X, in the work> with <Y, from outside it — one of the four kinds in R10>  Result: <they agree / they differ by …>
C2. …

## D. Decision
<accept | accept after changes | needs another round>   The one finding that matters most: B<n>
```

**Severity means exactly this:**

- **blocks** — a number, claim or decision in the work is wrong or unsupported. The work should not
  be accepted until it is fixed or the claim is withdrawn.
- **weakens** — the printed numbers happen to hold, but the method that produced them is deficient,
  or a claim is stronger than the evidence under it. Fix before the pattern is copied.
- **cosmetic** — the work is correct; the change makes it easier to read, run or maintain.

---

## 3. The rules — a sentence that breaks one is struck, and a struck sentence does not exist

R1–R3 and R6 survived the first draft unchanged. R4, R5, R7 and R8 were tightened and R9 was added
after the draft was attacked with the laziest reviews that would still pass it. R5 and R7 were then
tightened a second time and R10 was added after a review with zero findings and eight checks — every
one a comparison of the work with itself — passed R1–R9 and declared defect-free the very notebook §4
is written on (§5.1). The instructor's rubric records exactly what got through and what stopped it.

| # | Rule | Struck | Survives |
|---|------|--------|----------|
| R1 | **No person is the subject of any sentence.** No "you", "your", the author's name, "the author", "the team", "he", "she". | *You forgot to scale after the split.* | *`… › line "X_scaled = scaler.fit_transform(X)"` fits the scaler on all 1,994 rows before any split.* |
| R2 | **A finding has all five slots.** Location, observed, affects, change, severity. A finding missing one is not a finding. | *Cell 11: the scaling should be in a pipeline.* (no observed, no affects, no expected output) | see B1 in §4 |
| R3 | **No adjective of quality without a location and an observation beside it.** good · great · clear · clean · nice · excellent · well done · well written · poor · bad · sloppy · confusing · messy | *The notebook is very well explained.* | *The markdown cell "What to see in the bar chart above" promises a mean of 0.0844 and a ±1 std band of 0.0179 spanning roughly 0.067 to 0.102; the figure's legend prints "Mean R²: 0.0844" and "±1 Std: 0.0179" and the band is drawn from about 0.067 to 0.102. They agree.* |
| R4 | **A change ends with an expected output, or an exact replacement line.** An expected output is a number, a range, an exact line, a figure property, or the word "unchanged". A *direction* — "higher R²", "better", "faster" — is not an expected output. "consider", "maybe", "could improve", "should be better" are not changes. | *Consider adding error handling.* | *Replace `cross_val_score(model_kfold, X_scaled, y, …)` with `cross_val_score(make_pipeline(StandardScaler(), LinearRegression()), X, y, …)` → expected: `Mean R²: 0.0844` unchanged, and the cell no longer contradicts "⚠️ Where this breaks".* |
| R5 | **A check compares two things of different kinds, and one of them comes from outside the work.** A printed number with a typed claim; a value recomputed by a different method with the printed one; a README promise with what actually ran. The same number printed in two places is one thing. The work compared with itself — the reviewer's run beside the saved output, a figure beside the legend the same cell formatted from the same array, an array printed in one cell and plotted in another — is reproduction, which A2 already records, and is not a check (R10 lists what counts). "The imports work" compares nothing. | *Checked the imports and they work.* · *My run printed "Test R²: 0.1095"; the saved output says 0.1095. Agree.* | *Compared the printed "Mean R²: 0.0836 ± 0.0289" with the ten split R² values printed above it, summed by hand: 0.8361 / 10 = 0.0836. Agree.* |
| R6 | **Nothing is quoted from a saved output that was not re-run.** Part A comes first, and every number in Part B or C is one that appeared on the reviewer's own screen. Four reviewers per round show one finding live. | *(a number copied from the author's saved output on a notebook the reviewer never ran)* | *(the same number, after A2 records the run)* |
| R7 | **At least two findings, at least one of them `blocks` or `weakens`.** At most one `cosmetic` finding counts toward the two. A reviewer who genuinely finds no defect writes **four or more checks that count under R10** in Part C that *together touch every reported metric and every figure* in the work — a check touches a metric only when the number compared is the metric's value, not its label, heading or parameters, and four checks on the same number touch nothing — and that is the only way "nothing wrong" is allowed to be said. It is said at the reviewer's own risk: if the work turns out to carry a defect, a review with no findings is marked as the review of someone who did not find it (the README says what that costs). | *Two cosmetic findings and "Approve".* · *Zero findings and eight checks of the reviewer's run against the saved output.* | *One `weakens` finding plus one cosmetic; or zero findings plus five R10 checks covering every printed metric and every figure.* |
| R8 | **"Affects" names a result.** A result is a metric, a figure, a stated conclusion, or a decision the work makes (which model, which threshold, which feature). A print statement, a status line ("✅ Libraries imported successfully!"), a comment or a heading is not a result. "This could cause problems later" names nothing. | *This might cause issues in production.* | *Affects the line "Best Model by R²: Ridge (α=10)": the margin over the runner-up is 0.000008 against a fold spread of 0.0179.* |
| R9 | **Severity is fixed by what is affected, not chosen.** A finding whose location is a comment, a print statement, a variable name, an import, a docstring, or formatting is `cosmetic` by definition, whatever the reviewer would like to call it. `weakens` and `blocks` are reserved for findings whose "Affects" slot names a result (R8). | *Severity: weakens* on a finding about a comment. | *Severity: cosmetic* on the same finding — and it still counts, once, toward the minimum of two. |
| R10 | **A check counts only against something the work did not compute.** The test: if the code were wrong, would the thing compared against still be right? A hand sum, a documented rule, a stated requirement and a typed claim would; the saved output, a legend formatted from the array it labels, and a second print of the same array would not. The four kinds that count and the three that do not are listed under this table, each with an example from the notebook in §4. At least two of Part C's checks must count; under R7's escape, all four or more must. A comparison of the work with itself may be written, and counts toward nothing. | *C1: my run printed "Test R²: 0.1095"; the saved output says 0.1095. Agree.* (eight of these passed R1–R9 and tested nothing) | *Compared the printed "Mean R²: 0.0844" with the five fold values above it, added by hand: 0.4222 / 5 = 0.0844. Agree.* |

**What counts as a check (R10).** One example of each, from the notebook §4 reviews.

Counts — the thing compared against is outside the work:

- **(a) A value recomputed by a different method** — by hand, or in a cell of the reviewer's own that
  does not call the same function on the same arrays. *The printed "Mean R²: 0.0844" against the
  five fold values above it added by hand, (0.1095 + 0.0616 + 0.0703 + 0.0999 + 0.0809) / 5 = 0.0844.*
- **(b) A documented fact** — a library's documented default or rule, a dataset's documented size, a
  registry entry. *The step table under the k-fold figure, "held out 399 / 399 / 399 / 399 / 398",
  against 1,994 = 5 × 398 + 4 and scikit-learn's documented rule that the first n mod k folds get one
  extra row; the loader's "crime_statistics: full file, 1,994 rows." against `"full_rows": 1994` in
  `tools/data.py`.*
- **(c) A stated requirement or learning objective** — the brief, the unit README, the notebook's own
  objectives. *The unit README's "Apply K-Fold and other cross-validation schemes" against what runs:
  `KFold(n_splits=5, shuffle=True, random_state=73)` and `LeaveOneOut()`. The notebook's own objective
  "Use k-fold and stratified cross-validation" against the code, where `StratifiedKFold` is imported
  and never called — a requirement check that fails is written up as a finding (cosmetic here: no
  result depends on it), not as a check.*
- **(d) The work's own typed claim in a different cell** — a markdown cell, a README line, a docstring:
  text a person wrote, which would stay the same if the code changed. *"What to see in the bar chart
  above" promises a mean of 0.0844 and a ±1 std band of 0.0179 spanning roughly 0.067 to 0.102; the
  figure cell draws a legend "Mean R²: 0.0844", "±1 Std: 0.0179" and a band from 0.0665 to 0.1023.*

Does not count — the work against itself, which A2 already records:

- **The reviewer's run against the saved output.** *"My run printed Test R²: 0.1095; the saved output
  says 0.1095."* That sentence belongs in A2 and nowhere else.
- **A figure against the title, legend or labels the same cell formatted from the same array.** *The
  bar chart's labels 0.110 … 0.081 against its legend "Mean R²: 0.0844" — both are `all_scores`.*
- **The same array printed in one cell and printed or plotted in another.** *The five fold values
  under "SOLUTION: Perform cross-validation" against the bar heights; the loader's "1,994 rows"
  against "Samples: 1994 communities" against the x-axis "0 … 1,993".* One number, three prints.

The test that separates the two lists: **if the code were wrong, would the thing you compared it with
still be right?** A hand sum would. A legend formatted from the wrong array would be wrong in exactly
the same way — and would agree with it perfectly.

Struck sentences are not penalised for existing — they are penalised for what is missing once
they are gone. A review that is all struck sentences is an empty review, and it is marked as one.

---

## 4. A strong review — on a real notebook in this repository

> **This example is deliberately over the length cap.** Every slot is filled and every rule is
> shown at work, so it runs to about 1,000 words; a real review of this artefact fits in
> 300–600 because it needs only its findings and checks, not the commentary. The cap applies
> to your review, not to this teaching copy.

The notebook is `Course 04/unit2-regression-model-evaluation/examples/01_cross_validation.ipynb`,
a CORE lesson. Every number below was produced by running it fresh on the `ai-diploma` kernel
while this page was written; if the notebook has been changed since, re-run it and the numbers,
not this page, are the truth. That sentence is itself an application of rule R6.

```markdown
# Review of Course 04/unit2-regression-model-evaluation/examples/01_cross_validation.ipynb  @ main, 2026-09-27
Round: calibration example   Reviewer: (worked example)   Date: 2026-09-27
Environment: ai-diploma kernel, macOS   Data line printed by the loader: "crime_statistics: full file, 1,994 rows."

## A. Reproduction
A1. What was run: Kernel → Restart & Run All on the file above, 44 cells.
A2. What happened: ran to the end in about 3 s; last line printed by the last code cell:
    "Example 1 Complete! ✓". Every printed number below matched the saved output.
A3. The claim, in one sentence: a single 80/20 split gives one unreliable R² (0.1095), 5-fold
    cross-validation gives a mean of 0.0844 with a fold spread that shows how far one split can
    mislead, and the same folds rank five linear models, of which Ridge (α=10) is printed as best.

## B. Findings
### B1
Location:   "Step 1: Prepare Data for Modeling" › cell starting "# Prepare features (X) and target (y)"
            › line "X_scaled = scaler.fit_transform(X)"; then consumed by "SOLUTION: Perform
            cross-validation" › line "cv_scores_mse = cross_val_score(model_kfold, X_scaled, y,"
            and by the tournament cell starting "# CELL: Tournament".
Observed:   The scaler is fitted on all 1,994 rows, before KFold ever runs, so every test fold was
            standardised with a mean and std that included its own rows. Two lines above, the
            cell's own comment says "For test data, use only .transform() (don't refit!)". The
            notebook's closing section "⚠️ Where this breaks" says, verbatim: "Scale or select
            features *before* the split and the test information is inside every single fold.
            Put the preprocessing in a `Pipeline` and pass the pipeline to `cross_val_score`." The
            notebook does the thing its own last section forbids.
Affects:    The printed numbers, as it happens, not at all: with the scaler inside a Pipeline and
            the same KFold(5, shuffle=True, random_state=73), LinearRegression mean R² is 0.0844
            either way (an affine rescaling of the features cannot change an OLS fit); Ridge α=10
            moves by +0.000018 and Lasso α=1 by −0.000170. On the 50-row USArrests file with
            Lasso α=1 the gap is 0.4682 vs 0.4672. What it affects is the METHOD the lesson
            demonstrates, which is the one students copy into a pipeline with Lasso, KNN or SVM
            on a small dataset — where it does move the number and always in the flattering
            direction.
Change:     In the two CV cells, replace `cross_val_score(<model>, X_scaled, y, cv=kfold, …)` with
            `cross_val_score(make_pipeline(StandardScaler(), <model>), X, y, cv=kfold, …)`
            (import `make_pipeline` from `sklearn.pipeline`); in the baseline cell, split X first
            and fit the scaler on X_train only. → expected after the change: "Mean R²: 0.0844
            (8.4%)" prints unchanged, the tournament table changes in the 5th decimal, and the
            notebook stops contradicting itself.
Severity:   weakens

### B2
Location:   cell starting "# CELL: Tournament" › output lines "Model Comparison:" table and
            "📊 Best Model by R²: Ridge (α=10)".
Observed:   Mean R² in the table: Linear 0.084430 · Ridge α=1 0.084437 · Ridge α=10 0.084445 ·
            Lasso α=0.1 0.081952 · Lasso α=1 0.005325. The printed "best" beats the runner-up by
            0.000008 and beats plain linear regression by 0.000015. The same notebook's last
            figure labels the spread of the five fold scores "±1 Std: 0.0179".
Affects:    The claim "Best Model by R²: Ridge (α=10)". A difference 1,000× smaller than the fold
            spread the notebook's preceding sections exist to demonstrate is not a ranking; it is
            noise printed with a trophy next to it. A reader leaves believing Ridge α=10 beat OLS
            on this data. It did not, in any sense the notebook's own evidence can support.
Change:     After `best_r2_idx`, compute the runner-up and print "best" only if the margin exceeds
            the standard error of the fold scores (std / √5 ≈ 0.008 here); otherwise print
            "No model is distinguishable from the others at this fold spread (margin 0.000008,
            spread 0.0179)". → expected on this data: the "not distinguishable" line, and the
            Lasso α=1 row (0.0053) still visibly last.
Severity:   weakens

### B3
Location:   "Step 2: Simple Train-Test Split (Baseline)" › cell starting "# CELL: Baseline
            evaluation" › comment line "# train_test_split(X, y, test_size=0.2, random_state=123
            # Any number works".
Observed:   The comment documents random_state=123 (twice) while the code two lines below uses
            random_state=73, and the second "random_state=123 # Any number works" is pasted
            inside the bullet that explains random_state.
Affects:    Nothing that runs. A reader reconciling the comment with the code loses a minute.
Change:     Replace both occurrences of "random_state=123  # Any number works …" in the comment
            block with "random_state=73". → expected: comment and code agree; no output changes.
Severity:   cosmetic

## C. Checks
C1. Location: "SOLUTION: Perform cross-validation" › output line "Mean R²: 0.0844 (8.4%) (+/- 0.0358)".
    Compared: the printed mean with the five fold values above it, added by hand: 0.4222 / 5 = 0.0844;
    and "+/- 0.0358" with 2 × the "Std R²: 0.0179" printed under "Scores collected from 5 folds".
    Result: they agree.  (R10 kind a — recomputed by a different method.)
C2. Location: cell starting "# CELL: Visualise the k-fold SPLIT ITSELF" › step table column "held out".
    Compared: 399 / 399 / 399 / 399 / 398 with 1,994 = 5 × 398 + 4 under scikit-learn's documented
    rule that the first n mod k folds get one extra row.  Result: they agree.  (R10 kind b.)
C3. Location: markdown "What to see in the bar chart above" vs the figure "Cross-Validation Score
    Distribution Across 5 Folds".  Compared: the typed promise — mean 0.0844, ±1 std 0.0179, band
    "roughly 0.067 to 0.102" — with the legend "Mean R²: 0.0844", "±1 Std: 0.0179" and the band drawn
    from 0.0665 to 0.1023.  Result: they agree.  (R10 kind d — the work's own claim in another cell.)
C4. Location: markdown "What to see in the two panels above" vs the cell after "# DEMONSTRATION:
    Variance Across Different Splits".  Compared: "ten blue dots", "split 3 … 0.0402; split 7 …
    0.1259", "the single split … (0.1095)" with `for seed in range(10)`, the printed step table and
    the baseline "Test R²: 0.1095"; and the ten printed split values summed by hand, 0.8361 / 10 =
    0.0836, with "Mean R²: 0.0836 ± 0.0289".  Result: they agree.  (R10 kinds d and a.)

## D. Decision
accept after changes   The one finding that matters most: B1
```

What makes this strong is not that it found a leak. It is that B1's "Affects" slot says, with
numbers, that the leak *does not move this notebook's result* — and then says precisely why it is
still a defect. A reviewer who wrote "the R² is wrong because of leakage" would have been wrong, and
the author could have proved it in one cell. Precision about severity is the whole skill.

Its checks are the kind that count. Each compares a number in the work with something the work did
not compute — a hand sum, a documented rule, a typed promise. A check that compared the saved output
with the reviewer's run, or a legend with the array it was formatted from, would have been true and
would have tested nothing (R10, and §5.1).

---

## 5. A weak review — same notebook, and what is struck

```markdown
# Review of 01_cross_validation.ipynb
Reviewer: (worked example)

## A. Reproduction
I ran the notebook and it works fine.

## B. Findings
### B1
The notebook is very well explained and the comments are clear. Good job!
### B2
Cell 11: the scaling is done well.
### B3
You should consider adding more visualizations and some error handling.
### B4
The author could improve the naming of some variables.

## C. Checks
Checked the imports and they work.

## D. Decision
Approve. Great notebook overall.
```

Line by line:

| Sentence | Rule | Why it is struck | What would have survived |
|----------|------|------------------|--------------------------|
| *I ran the notebook and it works fine.* | R6, A2 | No command, no time, no last line, no loader line. Nothing here could be checked by a third person, and nothing distinguishes a reviewer who ran it from one who did not. | A2 of §4. |
| *The notebook is very well explained and the comments are clear. Good job!* | R3, R2 | Three adjectives, no location, no observation; "Good job" is addressed to a person. As a finding it has zero of five slots. | If it is true, it belongs in Part C as a check that compares a markdown promise with a printed output — see R3's "survives" column. |
| *Cell 11: the scaling is done well.* | R3, R2 | A location and an adjective. "Done well" was, as §4 B1 shows, the one place in the notebook where the method contradicts the lesson's own warning. The reviewer looked at the right cell and said nothing about it. | §4 B1. |
| *You should consider adding more visualizations and some error handling.* | R1, R4, R8 | "You"; "consider"; no location; no number or claim affected; no expected output. This sentence could be pasted under any notebook ever written, which is the test for whether a sentence is a review. | A location where an exception can occur, what input triggers it, the line to add, and what it should print. |
| *The author could improve the naming of some variables.* | R1, R2, R4 | "The author"; "some variables" is not a location; "could improve" is not a change. | §4 B3 — one named comment line, what it says, what the code two lines below says instead, the exact replacement, and "expected: no output changes". Cosmetic, and it still has all five slots. |
| *Checked the imports and they work.* | R5, R10 | Compares nothing with nothing — and nothing outside the work. | §4 C1–C4. |
| *Approve. Great notebook overall.* | R3, R7, D | "Great" with no location. Zero surviving findings and one non-check, so R7's only escape (four R10 checks covering every printed metric and every figure) is not met. The decision has no finding to point at. | `accept after changes — B1`, with B1 existing. |

After the strikes, this review contains no sentence. It is not a harsh review or a lenient review;
it is an absent one, and it is marked as absent. The author learned nothing from it, and — the
part that costs the reviewer — it is indistinguishable from the review of someone who never opened
the file.

### 5.1 A second weak review — the careful-looking one

This one passed every rule R1–R9 as first released, on the same notebook, and is why R10 exists:

```markdown
## A. Reproduction
A1. What was run: Kernel → Restart & Run All on the file above, 44 cells.
A2. What happened: ran to the end in 3 s; last line printed: "Example 1 Complete! ✓"
A3. The claim, in one sentence: one split gives R² 0.1095, five folds give mean 0.0844, and the
    folds rank five models with Ridge (α=10) first.
## B. Findings
(none)
## C. Checks
C1. Location: "Step 2" › output line "Test R²: 0.1095".  Compared: the value my run printed with the
    value in the saved output.  Result: 0.1095 in both.
C2. Location: the score-distribution figure.  Compared: the legend "0.0844" with the caption.
    Result: they agree.
C3–C8. (six more, every one "my run = saved output" or "figure = its own legend")
## D. Decision
accept
```

Nothing in it is false. Part A is complete; every check names a location and states a result; every
metric and figure is touched. And the review says nothing, because every comparison is of the work
with itself: C1 is A2 written a second time, C2 compares a legend with the array it was formatted
from, and a notebook that is consistently wrong passes all eight. This is the notebook whose §4 review
found a scaler fitted on every fold and a "best model" declared on a margin of 0.000008. Under R10
none of the eight checks count, R7's escape is unmet, and D stands on nothing. Read the last
paragraph of §5 again: this review, too, is indistinguishable from the review of someone who never
opened the file — it only took longer to write. And because the notebook does carry a defect, "no
findings" here is not a safe verdict but the worst one the reviewer could have handed in (README,
"No findings is not the safe answer").
