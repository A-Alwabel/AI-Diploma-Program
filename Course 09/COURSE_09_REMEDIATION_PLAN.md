# Course 09 Remediation Plan

## Goal

Bring `Course 09` to a classroom-ready standard where the numbered student path
teaches concepts deeply, assessments are fair, and documentation does not
overpromise beyond what students actually study.

## Guiding Principle

Fix alignment first, then deepen teaching, then add missing advanced material if
it is still needed.

## Phase 1: Assessment Fairness and Scope Repair

### Why this phase comes first

Assessments create immediate classroom pain. If a quiz asks about something the
course has not truly taught, students and instructors both lose trust in the
materials.

### Actions

- Audit and revise `QUIZZES/quiz_01.md` for any concepts that need stronger
  notebook support or clearer scope wording.
- Revise `QUIZZES/quiz_04.md` so it does not assess `RND` or count-based
  exploration unless those topics are added to the required path.
- Review quiz headers so they consistently reflect the full numbered notebook
  path for each unit.
- Recheck `ASSESSMENTS/Final_Exam.md` after quiz alignment changes.
- Expand support docs where assessment terminology is currently too thin.

### Deliverables

- Revised quiz files
- Updated support docs where required
- A short fairness note in docs if needed

## Phase 2: README and Scope Alignment

### Why this phase comes second

The course currently has several places where docs promise more than the
student-facing numbered notebooks deliver. That confuses scheduling, teaching,
and expectations.

### Actions

- Update `unit3-deep-rl/README.md` so its scope matches the numbered notebooks.
- Update `unit4-exploration-exploitation/README.md` so it no longer overclaims
  advanced exploration methods unless they are genuinely taught.
- Update `unit5-applications/README.md` so meta-learning, ethics, and advanced
  topics are described honestly at the student-path level.
- Tighten wording in top-level docs only where they amplify unit-level mismatch.

### Deliverables

- Scope-aligned unit READMEs
- Cleaner expectation-setting for instructors and students

## Phase 3: Foundation Teaching Upgrade

### Why this phase comes third

The strongest classroom return comes from making Units 1 and 2 teacher-proof.
If the foundations are deeply explained, later advanced units become much easier
to teach and much easier for students to absorb.

### Unit 1 priorities

- Clarify Bellman thinking before students see multiple update rules.
- Explain policy evaluation and policy improvement in plain language.
- Explain `gamma` with intuition, examples, and consequences.
- Make the difference between policy and value unavoidable and memorable.
- Add more “why this matters” and “common confusion” support where needed.

### Unit 2 priorities

- Clarify why model-free methods are needed after dynamic programming.
- Deepen Monte Carlo vs TD comparison.
- Explain bootstrapping clearly and repeatedly.
- Clarify Q-learning vs SARSA conceptually, not just algebraically.
- Make on-policy vs off-policy easy to explain in class.

### Deliverables

- Revised Unit 1 notebooks
- Revised Unit 2 notebooks
- Exercise and quiz rechecks for both units

## Phase 4: Advanced Unit Teaching Upgrade

### Why this phase comes fourth

Only after the foundations and scope are clean should advanced units be
deepened. Otherwise the course grows in size without becoming more teachable.

### Unit 3 priorities

- Resolve the PPO notebook mismatch by either:
  - implementing a minimal real PPO-like lesson, or
  - reframing the notebook honestly as PPO intuition plus simpler policy
    gradient training.
- Deepen explanations of replay buffer, target network, and instability.
- Make actor-critic distinctions more concrete.
- Decide whether DDPG stays as documented scope or becomes supplemental only.

### Unit 4 priorities

- Strengthen exploration strategy comparisons.
- Make the bridge from bandits to RL exploration explicit.
- Either add intrinsic-motivation / RND-level student material or reduce scope
  claims and assessments to match reality.

### Unit 5 priorities

- Strengthen RL framing in application notebooks.
- Decide whether meta-learning remains in the official student scope.
- Turn ethics and safety from light discussion prompts into clearer teaching
  blocks if they remain in scope.

### Deliverables

- Revised advanced-unit notebooks
- Aligned unit quizzes
- More honest and teachable advanced-unit scope

## Phase 5: Support Layer Upgrade

### Actions

- Improve `DOCS/GLOSSARY.md` for assessed but under-supported terms.
- Improve `DOCS/ALGORITHM_CHEAT_SHEET.md` where students need better concept
  comparisons.
- Improve `DOCS/FINAL_REVIEW_GUIDE.md` where confusion patterns keep repeating.

### Deliverables

- Stronger student rescue layer
- Better instructor quick-reference materials

## Phase 6: Verification

### Actions

- Open and structurally review every updated notebook.
- Run or sanity-check updated notebooks one by one.
- Confirm exercises are solvable from preceding examples.
- Recheck quizzes and exam after notebook changes.
- Remove duplicated weak scaffolding and misleading phrasing.

### Deliverables

- Verified, classroom-ready revised path

## Immediate Execution Order

1. Fix `quiz_04` and any related support-doc terminology.
2. Align `unit3`, `unit4`, and `unit5` READMEs with reality.
3. Deepen Unit 1 notebooks.
4. Deepen Unit 2 notebooks.
5. Revisit Unit 3 PPO and scope decisions.
6. Revisit Unit 4 advanced exploration scope.
7. Revisit Unit 5 meta-learning and ethics scope.

## Next Concrete Step

The next work item should be:

- revise the highest-risk assessment mismatch first

That means starting with:

- `QUIZZES/quiz_04.md`
- `DOCS/GLOSSARY.md`
- possibly `DOCS/ALGORITHM_CHEAT_SHEET.md`

## Success Criteria

The remediation is successful when:

- no quiz asks about a concept before it is clearly taught
- no README promises advanced content that the numbered path does not deliver
- each important notebook explains concepts, not just code
- students can answer “what is it, why is it used, and when do we use it?”
  after each lesson
- instructors can teach from the notebook without having to invent missing
  conceptual bridges live in class
