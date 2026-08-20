# Unit 2: Prediction and Control without a Model

## AIAT 123 - Reinforcement Learning

**Unit training hours:** 19 (of 96 total)

This folder is named `unit2-policy-value`; the official unit title is
**Prediction and Control without a Model**.

## Bridge from Unit 1

Unit 1 established MDPs, Bellman-style thinking, Gymnasium interaction, and
problem formulation. Unit 2 uses the same agent–environment loop but focuses on
model-free learning: sampling trajectories, estimating values from data, and
control with methods such as Q-learning and SARSA without assuming a small
closed-form world model.

## Before You Start

Make sure you have completed Unit 1 and can already:

- define an MDP
- explain states, actions, rewards, and policies
- interpret value functions
- work through simple Gymnasium examples

## Learning Objectives

By the end of this unit, you should be able to:

- explain why model-free methods are needed when the environment model is
  unknown
- implement Monte Carlo and Temporal Difference (TD) methods for prediction
- implement Q-learning and SARSA for control
- compare on-policy and off-policy learning behavior
- compare policy iteration and value iteration in small environments

## Study Order

The notebooks are numbered in study order — follow the numbers:

1. `examples/01_monte_carlo_value_estimation.ipynb` — Monte Carlo methods for
   estimating value functions from sampled episodes
2. `examples/02_td_algorithms_td0_nstep.ipynb` — TD(0) and n-step TD:
   bootstrapping and online updates
3. `examples/03_q_learning.ipynb` — Q-learning: off-policy control with a
   Q-table
4. `examples/04_sarsa_algorithm.ipynb` — SARSA: on-policy control and how it
   differs from Q-learning
5. `examples/05_policy_vs_value_iteration_comparison.ipynb` — comparing policy
   iteration and value iteration in small environments

## Exercise and Quiz

1. Complete `exercises/01_q_learning_exercise.ipynb`
2. Take `../QUIZZES/quiz_02.md`

Solutions are released by your instructor.

## Prerequisites

Unit 1 completion.

Next: `../unit3-deep-rl/README.md`
