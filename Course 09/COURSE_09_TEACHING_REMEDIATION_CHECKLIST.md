# Course 09 Teaching Remediation Checklist

## Goal

Upgrade `Course 09` so every student-facing lesson explains:
- what each concept is
- why it is used
- when it appears in the RL learning path
- how it differs from nearby concepts
- how to read the code and outputs
- what questions students are likely to ask

## Working Rule

Move one checklist item at a time. Do not skip ahead.

## Phase 1: Full Course Audit

- [x] Audit all unit `README.md` files against the real notebook flow.
- [x] Audit all numbered example notebooks in Units 1 to 5.
- [x] Audit all exercise notebooks for prerequisite coverage gaps.
- [x] Audit all quizzes for concepts asked before being properly taught.
- [x] Audit the final exam for scope mismatches.
- [x] Create a concept-gap report for the whole course.
- [x] Prioritize gaps by classroom risk: critical, medium, low.

## Phase 2: Teaching Standard Definition

- [x] Define a fixed teaching template for every student-facing notebook.
- [x] Require `Lesson Brief` and `Closing Takeaway` in every lesson.
- [x] Require a plain-language explanation for every new RL concept.
- [x] Require a "why this matters" explanation before math or code.
- [x] Require a "common mistakes" section for likely confusions.
- [x] Require step-by-step code comments where students may get lost.
- [x] Require a short interpretation of outputs after plots/tables/results.
- [x] Require a mini FAQ or expected student questions where needed.

## Phase 3: Unit 1 Remediation

- [x] Strengthen explanations for MDP basics, Markov property, policy, value,
  reward, transitions, and terminal states.
- [x] Add clearer explanation of Bellman thinking before policy/value algorithms.
- [x] Explain policy evaluation, policy improvement, policy iteration, and
  value iteration in plain language.
- [x] Clarify discount factor `gamma` with intuition and examples.
- [x] Align Unit 1 quizzes with what is explicitly taught.
- [ ] Verify Unit 1 exercise can be solved from the taught material only.

## Phase 4: Unit 2 Remediation

- [x] Explain why model-free RL is needed after dynamic programming.
- [x] Deepen Monte Carlo explanation: what it is, why it works, and where it fails.
- [x] Deepen TD learning explanation and contrast it with Monte Carlo.
- [x] Clarify Q-learning vs SARSA with intuitive and algorithmic comparisons.
- [x] Explain bootstrapping, on-policy, and off-policy in student-friendly language.
- [ ] Align Unit 2 quiz and exercise with explicit notebook coverage.

## Phase 5: Unit 3 Remediation

- [x] Strengthen DQN explanation beyond implementation steps.
- [x] Explain replay buffer, target network, and instability problems clearly.
- [x] Clarify policy gradients and Actor-Critic with intuition before code.
- [x] Explain PPO objectives and why PPO is more stable than naive policy gradients.
- [x] Review DDPG scope and either add proper student-facing coverage or reduce
  claims in docs and assessments.
- [ ] Align Unit 3 quiz, exercise, and README with real student-facing materials.

## Phase 6: Unit 4 Remediation

- [x] Clarify exploration vs exploitation beyond epsilon-greedy.
- [x] Explain Boltzmann, UCB, Thompson Sampling, and adaptive exploration in
  plain language.
- [x] Review whether intrinsic motivation, RND, and Bayesian-style exploration
  are truly taught or only claimed.
- [x] Add or revise materials so documented coverage matches real coverage.
- [x] Ensure comparison notebooks explain when each exploration strategy is preferred.
- [ ] Align Unit 4 quiz and exercise with actual taught content.

## Phase 7: Unit 5 Remediation

- [x] Make applications notebooks explain the RL framing before jumping to examples.
- [x] Review whether meta-learning and few-shot RL are really taught at
  student level.
- [x] Review whether ethics, safety, and fairness are really taught at student level.
- [x] Add or revise advanced-topic coverage so docs do not overpromise.
- [x] Ensure applications connect back to the earlier RL foundations.
- [x] Align Unit 5 quiz, exercise, project prep, and exam coverage with real materials.

## Phase 8: Course-Level Assessment Alignment

- [x] Audit all quizzes question-by-question against actual notebook teaching.
- [x] Remove questions that assume untaught terminology.
- [x] Add questions that better test conceptual understanding, not
  memorization only.
- [x] Audit `ASSESSMENTS/Final_Exam.md` for fairness and scope alignment.
- [x] Ensure no student-facing assessment depends on instructor-only material.

## Phase 9: Student Support Improvements

- [x] Improve `DOCS/GLOSSARY.md` so key RL terms are short and teachable.
- [x] Improve `DOCS/ALGORITHM_CHEAT_SHEET.md` so it supports class explanation.
- [x] Improve `DOCS/FINAL_REVIEW_GUIDE.md` around concept relationships and
  confusion points.
- [x] Add course-wide concept cross-links where students commonly forget connections.

## Phase 10: Verification

- [ ] Open and review each updated notebook for structure consistency.
- [ ] Run or sanity-check updated notebooks one by one.
- [ ] Check that each exercise is solvable from the revised examples.
- [x] Recheck quizzes and exam after notebook revisions.
- [x] Do a final pass for duplication, weak prompts, and shallow explanations.

## Phase 11: Cleanup

- [ ] Normalize tone and structure across all student-facing notebooks.
- [x] Remove misleading scope claims from docs.
- [x] Confirm instructor-only materials remain separated.
- [x] Write a final summary of what changed and why.
