# Unit 2: Policy and Value-Based Methods
## AIAT 123 - Reinforcement Learning

## Before You Start

Make sure you have completed Unit 1 and can already:

- define an MDP
- explain states, actions, rewards, and policies
- interpret value functions
- work through simple Gym examples

## Learning Objectives

By the end of this unit, you should be able to:
- Understand why model-free methods are needed when the environment model is unknown
- Work with Dynamic Programming foundations and understand their limits
- Implement Monte Carlo and Temporal Difference (TD) methods
- Implement Q-learning and SARSA
- Compare policy iteration and value iteration in small environments

---

## Topics Covered

Based on the instructor unit materials and the notebooks included in this
folder, this unit focuses on model-free prediction and control:

1. **Dynamic Programming Foundations**
   - Bellman equations
   - Policy evaluation
   - Policy iteration
   - Value iteration
   - Why DP becomes impractical in large or unknown environments

2. **Monte Carlo Methods**
   - First-visit vs every-visit estimation
   - Monte Carlo prediction
   - Monte Carlo control
   - Sampling-based value estimation

3. **Temporal Difference (TD) Learning**
   - TD(0)
   - n-step TD methods
   - TD vs Monte Carlo
   - Bootstrapping and online updates

4. **Q-Learning**
   - Off-policy learning
   - Q-table updates
   - Temporal difference target
   - Convergence behavior in simple environments

5. **SARSA**
   - On-policy learning
   - SARSA update rule
   - Comparison with Q-learning
   - Exploration-aware learning behavior

6. **Policy Iteration vs Value Iteration**
   - Convergence comparison
   - Computational trade-offs
   - Small environment experiments

### Note

This folder also includes a short `policy_gradient` notebook as supplemental material.
The main policy-gradient treatment belongs to `unit3-deep-rl/`.

---

## Study Order

Follow these notebooks in order:

1. `examples/01_q_learning.ipynb`
2. `examples/02_sarsa_algorithm.ipynb`
3. `examples/04_monte_carlo_value_estimation.ipynb`
4. `examples/05_td_algorithms_td0_nstep.ipynb`
5. `examples/06_policy_vs_value_iteration_comparison.ipynb`

### Supplemental notebooks

You may also see longer descriptive notebook filenames and
`examples/03_policy_gradient_basics.ipynb`. Treat those as supplemental while
studying this unit. The core policy-gradient path belongs to Unit 3.

Student rule:

- The required path in this unit is the numbered notebooks listed above.
- Treat `examples/03_policy_gradient_basics.ipynb` and any
  long descriptive filenames as supplemental.
- Review the solution only after completing your own
  exercise attempt.

## Exercise and Quiz

1. Complete `exercises/01_q_learning_exercise.ipynb`
2. Review `solutions/01_q_learning_solution.ipynb`
3. Take `../QUIZZES/quiz_02.md`

**Unit Duration:** 2 weeks  
**Difficulty:** Advanced  
**Prerequisites:** Unit 1 completion

