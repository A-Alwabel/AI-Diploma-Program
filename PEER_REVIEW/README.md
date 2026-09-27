# Peer review — the protocol

Three times in this diploma you will be handed another student's work and asked to say, in
writing, what is wrong with it and what to change. **The review you write is graded.** The work
you receive reviews on is not re-graded because of them — what you do with them is up to you.

This page is the whole protocol: what you submit, what you receive, what you must write, how
long it takes, and why the review is the thing that carries the mark. The form itself is in
[`review_form.md`](review_form.md). Read both before round 1.

---

## 🔗 Where this fits

**Builds on:** `../TOOLING/examples/02_git_for_one_and_for_two.ipynb` — you cannot review what
you cannot check out, and the second half of that lesson (*branch → push → review → merge*) is the
loop this protocol runs. Round 3 also assumes `../TOOLING/examples/06_handing_over_a_repository.ipynb`:
you cannot review work you cannot run.

**Used in:** three rounds, placed where the work is —

| Round | Week | Course | What is reviewed | Why this artefact |
|------:|-----:|--------|------------------|-------------------|
| 1 | 14 | Course 05, sessions 56–57 | One module of another team's **Course 04 ML pipeline** (the team project, already submitted) — the module that matches the role you held in your own team | It is the first thing in the programme large enough to hide a real defect (a scaler fitted before the split, a metric that answers a different question, a test set touched twice). You have just built the same thing on a different dataset, so you know where to look. |
| 2 | 20 | Course 07, sessions 78–79 | Another student's written **Course 07 case-study analysis** (two of them) | Arguments are the artefact this diploma's evidence is strongest on, and they are where fluent, confident and wrong is hardest to see. Two reviews per student, so disagreement between reviewers is something you will meet. |
| 3 | 34 | Course 12, sessions 135–136 | Another student's **graduation-project repository** at the point where gate 3 (implementation) is about to be graded | Clone it, install it, run the one command the README promises, compare the result with the stated one. This is the handover lesson run for real, on work that matters to the person who wrote it — and it happens *before* the instructor grades gate 3, so the author can still act on it. |

**Not the same thing as:** the confidential *peer evaluation* form you fill in about your own
teammates at the end of a group project. That rates people. This reviews work. The two never mix.

---

## Why the review is what gets graded

Three reasons, each one checkable.

**1. Judging someone else's work is what a junior is paid to do in year one.** At Google, code
review is required for every commit, and the study that measured it (Sadowski et al., 2018 —
12 interviews, a survey of 44 developers, review logs for 9 million changes) reports that the
median developer *reviews* 4 changes a week and spends a median 2.6 hours a week doing it; that
new team members "are explicitly added as reviewers since they have not yet built up
reviewing/editing history"; and that *education* is one of the four things developers say review
is for. Nobody waits until you are senior to ask you what is wrong with a diff.

**2. In 2026 the diff is often written by a model, and the job is to catch it being wrong.** In the
Stack Overflow 2025 survey, 84% of developers use or plan to use AI tools; more of them actively
distrust the accuracy of those tools (46%) than trust it (33%); the single most-cited frustration is
"AI solutions that are almost right, but not quite" (66%); 45.2% say debugging AI-generated code is
more time-consuming; and when they do not trust an AI answer, 75.3% ask a person. That person is
doing exactly what this form asks of you: read it, run it, say what is wrong, say what to change.

**3. The grade is the part the evidence supports.** The best meta-analysis of peer assessment
(Double, McGrane & Hopfenbeck, 2020; 54 studies, 141 effect sizes) found that being assessed by
peers improved university students' performance slightly *more* than being assessed by the
teacher (g = 0.31 vs 0.28), and that when the peer feedback **carried a grade**, the effect at
university level was g = 0.55 — nearly double the overall figure. The evidence does not say what
to grade. We grade the review, because the reviewer is the one doing the harder thinking, and
because a review nobody grades is a review nobody writes carefully.

---

## What you submit (as the author)

Nothing new. The artefact of the round is work you have already handed in, or are about to:

- **Round 1:** your team's Course 04 pipeline repository, at the commit you submitted. The
  reviewer checks out that commit, so nothing you do afterwards changes what they see.
- **Round 2:** your Course 07 case-study analysis, due at the **start** of session 78 (not the end).
- **Round 3:** your graduation-project repository, tagged `gate3-review` before session 135 starts.
  The README must state one command and one expected result — the handover lesson's contract.

If the artefact is not there when the session starts, your reviewer reviews its absence: the
form's reproduction block records "not available at `<commit/tag>` at `<time>`" and the rest of
their review is written about whatever partial state exists. That review is still graded. Yours is
not excused.

## What you receive (as the author)

At the start of the second session of each round: the completed review form(s) — one in rounds 1
and 3, two in round 2 — with the reviewer's name on them. Reviews are signed, because that is how
it works in a job, and because the reviewer is accountable for every finding. The text of a review
never names you or addresses you; the form forbids it.

You then write a **response**, one line per finding:

- **Accept** — what changed, and where (a cell or a line, same convention as the form).
- **Reject** — why, with a location or a number. "I disagree" is not a rejection.
- **Cannot reproduce** — what you ran, what it printed.

The response is required and is not graded. What *is* graded is the artefact: a finding marked
*blocks* that is neither fixed nor rejected with evidence will cost you on the artefact's own
rubric — in round 3, on gate 3; in round 2, on the case-study analysis (the revised version is the
one marked); in round 1, only if you use your one resubmission. In round 1 the honest statement is
that the review cannot change a mark already given: act on it in the Course 05 pipeline you are
building the same week, which has the same shape and the same places to go wrong.

---

## What you must write (as the reviewer)

One completed [`review_form.md`](review_form.md) per artefact assigned to you. The form has four
parts and every part is required:

| Part | What it demands | What it will not accept |
|------|-----------------|-------------------------|
| **A — Reproduction** | What you ran, the exact last line it printed, the loader's data line, how long it took | "Ran fine" |
| **B — Findings** (2 to 5) | For each: a **location**, what you **observed** there, what it does to a **number, claim or decision**, and the **change** with its expected output | A finding missing any of the four slots; "consider improving…" |
| **C — Checks** (2 or more) | Things you verified and found to hold: a location, a number or claim in the work, and the thing **outside the work** you compared it with — a value recomputed by a different method, a documented fact, a stated requirement, or the work's own typed claim in another cell (form rule R10) | "The code is clean"; "the imports work"; "my run matches the saved output" (that is Part A, not a check); "the figure matches its own legend" |
| **D — Decision** | accept / accept after changes / needs another round, and the number of the one finding that matters most | A decision that contradicts your own findings |

Two rules bind every sentence: **nothing about a person** (no "you", no name, no "the author"),
and **no adjective of quality without a location and an observation next to it**. Nine more
rules (R2–R10 in the form) fix what a finding must contain, what its severity may be, and what
counts as a check. The form shows, with a real notebook from this repository, what passes and what
is struck.

The reason for the second rule is measured. Wisniewski, Zierer & Hattie (2020; 435 studies, 994
effect sizes, more than 61,000 people) found feedback carrying high information about the task
and the process had an effect of d = 0.99, corrective feedback d = 0.46, and reinforcement or
punishment d = 0.24 — and the paper restates, on the authority of the 2007 framework it evaluates,
that self-directed feedback (praise about the person) is the least effective level of all. (One of
the authors wrote that framework; weigh that.) "Great work" costs the reader something and buys
them nothing. A location and an observation buy them the defect.

**"No findings" is not the safe answer.** The form lets a reviewer say nothing is wrong only behind
four or more checks against things the work did not compute, together covering every metric and
every figure (R7 and R10). Say it about work that turns out to carry a defect — one your instructor
knew about when the round was set, or one another reviewer found and showed live — and the review
is marked as the review of someone who did not find it: the parts of the mark that pay for findings
pay nothing, the decision "accept" is marked as false, and no amount of careful checking elsewhere
makes that up. It is the worst outcome the rubric holds for a reviewer — below a review of two
cosmetic findings, because that reviewer at least found something. Say it about work that is
genuinely sound, with the checks to show for it, and it is marked as the right answer, fully. The
mark follows whether the work had a defect, not whether the review was comfortable to write. The
only safe move is to look until you are sure — and a review that has only compared the work with
itself has not looked.

**How many reviews.** Round 1: one (the matching module of the team next in the ring). Round 2:
two (two analyses, assigned by your instructor from the roster, never adjacent). Round 3: one
(the repository next in the ring).

**How long.** The review is written **in class**, in the first session of the round: 90 minutes for
a notebook or repository, 40 minutes for each written analysis. 300–600 words. Not more — a
five-finding review that is right is worth more than a twelve-finding review that is padding, and
the form caps findings at five for that reason.

**Tools.** Use anything you like to *understand* the work, including a language model. Every finding
must be one **you reproduced on your own machine and can show live in two minutes**. Four reviewers
per round are chosen at random and asked to do exactly that, in front of the class. A finding that
cannot be shown scores zero and the review is read as if it were absent.

---

## How the two sessions run

**Session 1 — calibrate, then review.** Your instructor puts one artefact on the screen and the
whole class reviews it together — three findings, argued from locations, and a first look at how
each would be marked (35 minutes in round 1; 20 in rounds 2 and 3, because by then you know the
form). Then you check out your assigned artefact and write your review. In round 1 the last 25
minutes are a swap: you strike, in pencil, every sentence of a neighbour's form that the rules
forbid, and they do the same to yours; you submit after the strikes are fixed. In round 2 the unit's
CORE notebook still runs live in the same session, shortened, before the reviews are written.

**Session 2 — respond, fix, verify.** Authors read their reviews and write responses. Authors fix
their top finding, re-run, commit. Reviewer and author then sit together for the reviewer to
verify the fix live. The session ends with three findings from the round — one strong, one weak,
one where two reviewers disagreed — put on the screen anonymised and marked aloud.

## 💬 Discuss

Held in the last fifteen minutes of session 2. There is no single right answer to any of these.

1. Two reviewers disagreed on the same cell: one wrote *blocks*, one wrote *cosmetic*. The
   instructor ran it. Who was right — and can both reviews still score well? Argue it from the form.
2. In round 1 the scaler was fitted on all rows before cross-validation, the notebook's own
   *Where this breaks* section says not to do that, and the mean R² did not move at all when it
   was fixed (the form's strong example). Is that a defect? What would you write in the severity
   slot, and what would make you change it?
3. A review names a real defect and proposes a change that would make the number worse. Which
   part of the rubric does the reviewer lose, and which do they keep?
4. Reviews here are signed. Some teams review blind. What does each one cost, in this room, with
   these twenty people? What would you choose for round 2, and what would make you switch?
5. A review of the form's own example notebook with zero findings and eight checks — my run against
   the saved output, the legend against the caption — once passed every rule the form had. What did
   each of those checks prove? What would a check that could have caught the scaler leak have
   compared, and with what?

---

## ⚠️ Where this breaks

- **The evidence is about grades and essays, mostly not about code.** Double et al.'s 54 studies
  are largely quasi-experimental (whole classes assigned to conditions, not individuals);
  geography was never tested as a moderator, so there is no evidence either way about how this
  transfers to a Saudi cohort; and the only computer-science example the published summary
  offers is 9th-grade Scratch. Two of these three rounds are on code. In a small way, you are
  outside the evidence, and you should know it.
- **Peer review propagates errors as readily as it catches them.** A reviewer who is wrong with
  confidence can push an author to break something that worked. That is why the form demands a
  reproduction, why the change slot demands an expected output, and why the author's *reject with
  evidence* is a legitimate response, not insubordination.
- **A rubber stamp is worse than no review.** It manufactures a record of scrutiny that did not
  happen. Bacchelli & Bird's study of review at Microsoft found that what teams *expect* from review
  (finding defects) and what they mostly *get* (understanding the code, spreading knowledge) are
  not the same thing. The rubric pays for a real defect found; it pays nothing for "approve". The
  form was defeated once by exactly this, dressed up: zero findings and eight checks, each comparing
  the work with itself, on a notebook with two real defects. That is why R10 says which checks
  count, and why "no findings" on flawed work is now the worst mark a reviewer can get, not the
  safest.
- **Twenty people who know each other.** Signed reviews between friends drift soft. The form
  makes softness structurally expensive — a finding without a location does not exist — and the
  grade is on the findings. If round 1 still comes back cosmetic, round 2 goes blind. That is a
  decision your instructor will make on the evidence of round 1, not in advance.

---

*Sources used above, each where it is cited:* Sadowski, Söderberg, Church, Sipko & Bacchelli (2018),
*Modern Code Review: A Case Study at Google*, ICSE-SEIP · Stack Overflow Developer Survey 2025, AI
section · Double, McGrane & Hopfenbeck (2020), *Educational Psychology Review* 32:481–509 ·
Wisniewski, Zierer & Hattie (2020), *Frontiers in Psychology* 10:3087 · Bacchelli & Bird (2013),
*Expectations, Outcomes, and Challenges of Modern Code Review*, ICSE — as cited in the git lesson.
