# Unit 3: Deep Reinforcement Learning

## AIAT 123 - Reinforcement Learning

**Unit training hours:** 19 (of 96 total)

## Bridge from Unit 2

Unit 2 emphasized tabular updates (one entry per state or state–action pair).
Unit 3 keeps the same goals — evaluation and control — but uses function
approximation (neural networks) so larger or continuous observation structures
stay tractable. Expect the same questions about targets, data, and stability,
now in a deep learning setting.

## Before You Start

Make sure you have completed Unit 2 and are comfortable with:

- tabular RL basics (Q-learning, SARSA)
- neural networks and backpropagation
- PyTorch basics from AIAT 122 - Deep Learning

## Learning Objectives

By the end of this unit, you should be able to:

- explain why deep RL is needed beyond tabular methods
- implement a Deep Q-Network (DQN) with experience replay and a target network
- implement introductory policy-gradient training (REINFORCE style)
- explain the actor-critic idea and why critics reduce variance
- describe PPO at an introductory level as a stability-oriented extension
- interpret training curves and optimization choices in small deep RL setups

## Study Order

Complete the example notebooks in file order:

1. `examples/01_dqn_implementation.ipynb` — Deep Q-Networks: Q-learning with a
   neural network, experience replay, and a target network
2. `examples/02_policy_gradient_basics.ipynb` — policy gradient basics:
   learning a policy directly (REINFORCE intuition)
3. `examples/03_actor_critic.ipynb` — actor-critic methods: combining a policy
   with a learned value baseline
4. `examples/04_ppo_algorithm.ipynb` — PPO: from policy-gradient intuition to
   clipped, stability-oriented updates
5. `examples/05_training_evaluation_monitoring.ipynb` — training and
   evaluation: monitoring learning curves, rewards, and stability
6. `examples/06_optimization_experience_replay_reward_shaping.ipynb` —
   optimization: experience replay, reward shaping, and hyperparameter tuning

## Scope note

The numbered path uses small Gymnasium-style environments. Advanced variants
such as Atari-scale DQN, Double/Dueling DQN, A2C/A3C, and DDPG are outside the
required path unless your instructor assigns extra material.

## Exercise and Quiz

1. Complete `exercises/01_deep_reinforcement_learning_exercise.ipynb`
2. Take `../QUIZZES/quiz_03.md`

Solutions are released by your instructor.

## Prerequisites

Units 1–2 completion, plus neural network basics.

Next: `../unit4-exploration-exploitation/README.md`
