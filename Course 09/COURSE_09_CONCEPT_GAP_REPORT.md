# Course 09 Concept Gap Report

## Purpose

This report summarizes the teaching and alignment gaps found in `Course 09`.

The focus is not only whether content exists, but whether the required student
path explains each concept deeply enough for classroom delivery:

- what the concept is
- why it is used
- when it appears in the RL learning path
- how it differs from nearby concepts
- how to interpret the code and outputs
- what students are likely to ask about it

## Overall Judgment

`Course 09` has a usable structure and several strong notebooks, but it is not
yet fully aligned at the teaching level.

The main problems are:

1. Some concepts are used or assessed before they are explicitly explained well.
2. Some unit `README.md` files promise more than the numbered student notebooks
   actually teach.
3. Some notebooks explain implementation steps without fully unpacking the
   concept in plain language.
4. Some quizzes ask about concepts that are only lightly mentioned, not taught
   at the depth expected by the assessment.

## Strong Parts Worth Preserving

- `unit1-rl-fundamentals/examples/01_mdp_example.ipynb`
- `unit1-rl-fundamentals/examples/02_mdp_solving.ipynb`
- `unit1-rl-fundamentals/examples/03_value_iteration.ipynb`
- `unit3-deep-rl/examples/01_dqn_implementation.ipynb`
- `unit4-exploration-exploitation/examples/02_balancing_exploration.ipynb`
- `DOCS/ALGORITHM_CHEAT_SHEET.md`
- `DOCS/FINAL_REVIEW_GUIDE.md`

## Critical Gaps

### Unit 1

- `QUIZZES/quiz_01.md`
  asks about concepts such as the meaning of `gamma` in a way that is not
  always taught explicitly enough in the numbered Unit 1 path.

- `unit1-rl-fundamentals/examples/01_mdp_example.ipynb`
- `unit1-rl-fundamentals/examples/02_mdp_solving.ipynb`
- `unit1-rl-fundamentals/examples/03_value_iteration.ipynb`

  These notebooks are good, but some classroom-risk concepts still need more
  direct teacher-ready explanation:

  - Bellman thinking
  - why policy evaluation exists
  - why policy improvement comes after evaluation
  - what `gamma` changes in practice
  - how value and policy differ in decision making

### Unit 3

- `unit3-deep-rl/examples/03_ppo_algorithm.ipynb`

  The notebook title and framing imply PPO, but the executable teaching core is
  closer to REINFORCE plus PPO intuition than to a real PPO lesson. This is a
  classroom risk because students may leave thinking they learned PPO
  implementation when they did not.

- `unit3-deep-rl/README.md`

  The README claims practical scope around DDPG, Atari-style DQN, and other
  advanced deep RL coverage that is not fully present in the numbered student
  path.

### Unit 4

- `QUIZZES/quiz_04.md`

  The quiz asks about `RND` and count-based exploration, but the required
  numbered notebooks do not teach those methods at matching depth.

- `unit4-exploration-exploitation/README.md`

  The README claims intrinsic motivation, RND, Bayesian optimization, and other
  advanced exploration ideas more strongly than the numbered notebooks support.

### Unit 5

- `unit5-applications/README.md`

  The unit claims student-facing coverage for meta-learning / few-shot RL and
  deeper ethics/safety scope that the numbered notebooks do not yet teach
  strongly enough.

## Medium Gaps

### Unit 2

- `unit2-policy-value/README.md`

  The required study order introduces `Q-learning` and `SARSA` before the Monte
  Carlo and TD framing is fully built. This creates a formula-first risk for
  students.

- `unit2-policy-value/examples/01_q_learning.ipynb`
- `unit2-policy-value/examples/02_sarsa_algorithm.ipynb`
- `unit2-policy-value/examples/04_monte_carlo_value_estimation.ipynb`
- `unit2-policy-value/examples/05_td_algorithms_td0_nstep.ipynb`

  These notebooks are useful, but the course-level flow should explain more
  explicitly:

  - why model-free methods are needed
  - how Monte Carlo differs from TD
  - what bootstrapping means
  - why Q-learning is off-policy
  - why SARSA is on-policy

### Unit 4

- The numbered notebooks often teach exploration through bandit-style examples.
  That is not wrong, but the unit framing should make the bridge to full RL/MDP
  exploration more explicit so students do not think bandits and RL exploration
  are the same thing.

### Unit 5

- Ethics, safety, and fairness are present more as discussion prompts than as a
  structured teaching block.
- Multi-agent and advanced topics are introduced, but in some places the
  notebooks risk becoming concept catalogs rather than deeply taught lessons.

## Low Gaps

- Repeated boilerplate sections across notebooks reduce signal and can dilute the
  main idea of each lesson.
- Some quiz headers do not clearly reflect the full numbered path needed for
  preparation.
- `DOCS/GLOSSARY.md` is useful but can better support assessed concepts such as:
  - Boltzmann / softmax exploration
  - intrinsic motivation
  - RND
  - count-based exploration

## Root Causes

The main root causes appear to be:

1. The course was merged from more than one source set.
2. Some notebooks were improved structurally, but the course was not fully
   re-aligned at the README and assessment level afterward.
3. Some topics are currently documented at the intended-scope level rather than
   the actual-student-path level.
4. Some lessons still prioritize showing the algorithm over teaching the mental
   model behind it.

## Classroom Risk Ranking

### Critical

- Unit 1 conceptual depth vs `quiz_01`
- Unit 3 PPO mismatch
- Unit 4 README and `quiz_04` overreach
- Unit 5 meta-learning / ethics overclaim

### Medium

- Unit 2 teaching order and model-free scaffolding
- Unit 4 bandit-to-RL bridge weakness
- Unit 5 advanced-topic depth consistency

### Low

- Repeated notebook scaffolding text
- Support-doc terminology gaps
- Minor mapping and wording inconsistencies

## Recommended Immediate Priorities

1. Fix fairness and scope alignment in quizzes before expanding content.
2. Make Unit 3, Unit 4, and Unit 5 READMEs match the real numbered path.
3. Deepen Unit 1 and Unit 2 concept teaching before touching advanced additions.
4. Only after that, decide whether to:
   - add missing advanced notebooks, or
   - reduce documented scope to match the real course.

## Decision Rule Going Forward

For each unit, every important concept should be checked against this rule:

- Is it explicitly taught in the numbered path?
- Is it explained in plain language?
- Is the reason for using it made clear?
- Is it connected to previous concepts?
- Is it assessed only after that teaching exists?

If the answer is no, the course is not yet ready at classroom level for that
concept.
