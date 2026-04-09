# Unit 3: Deep Reinforcement Learning
## AIAT 123 - Reinforcement Learning

## Before You Start

Make sure you have completed Unit 2 and are comfortable with:

- tabular RL basics
- neural networks and backpropagation
- PyTorch basics from Course 08

## Learning Objectives

By the end of this unit, you should be able to:
- Understand Deep Q-Networks (DQN)
- Implement policy gradient methods
- Work with Actor-Critic algorithms
- Apply deep RL to complex environments
- Handle challenges in deep RL training

---

## Topics Covered

Based on official curriculum (AIAT 123), this unit covers:

1. **Introduction to Deep Reinforcement Learning**
   - Why deep RL?
   - Combining deep learning with RL
   - Function approximation in RL
   - Challenges in deep RL

2. **Deep Q-Networks (DQN)**
   - Q-learning with neural networks
   - Experience replay
   - Target networks
   - DQN variants (Double DQN, Dueling DQN)
   - Applications of DQN

3. **Policy Gradient Methods**
   - REINFORCE algorithm
   - Policy gradient theorem
   - Advantages and challenges
   - Improvements to REINFORCE

4. **Actor-Critic Methods**
   - Actor-Critic architecture
   - Advantage Actor-Critic (A2C)
   - Proximal Policy Optimization (PPO)
   - Asynchronous Advantage Actor-Critic (A3C)

5. **Deep Deterministic Policy Gradient (DDPG)**
   - DDPG for continuous action spaces
   - DDPG architecture
   - Exploration in DDPG
   - Applications

6. **Deep RL Applications**
   - Games and simulations
   - Robotics
   - Autonomous vehicles
   - Healthcare and optimization

7. **Challenges in Deep RL**
   - Exploration vs exploitation dilemma
   - Sample efficiency
   - Stability and convergence
   - Generalization and overfitting

---

## Unit Breakdown

**Theoretical Hours:** 6  
**Practical Hours:** 13  
**Total Hours:** 19

### Theoretical Content

- Deep RL fundamentals
- DQN algorithm and variants
- Policy gradient methods
- Actor-Critic approaches
- DDPG for continuous control
- Applications and challenges

### Practical Content

- Implementing DQN from scratch
- Training DQN on Atari games
- Building REINFORCE algorithm
- Implementing Actor-Critic methods
- Applying DDPG to continuous control
- Training and evaluation
- Hyperparameter tuning

---

## Study Order

Follow these notebooks in order:

1. `examples/01_dqn_implementation.ipynb`
2. `examples/02_actor_critic.ipynb`
3. `examples/03_ppo_algorithm.ipynb`
4. `examples/04_training_evaluation_monitoring.ipynb`
5. `examples/05_optimization_experience_replay_reward_shaping.ipynb`

### Supplemental notebooks

This unit also contains long descriptive notebook filenames that expand on the
same themes. Treat them as supplemental unless your instructor assigns them.

### Important note

This README includes DDPG in the intended scope of the unit. Use the numbered
notebooks as the core student path first; any DDPG-specific material should be
treated as advanced or supplemental until a dedicated student-facing notebook is
provided in the main sequence.

Student rule:

- The required path in this unit is the numbered notebooks only.
- Long descriptive filenames and DDPG-related material are supplemental
  unless your instructor assigns them.
- Review the solution only after completing your own
  exercise attempt.

## Exercise and Quiz

1. Complete `exercises/01_deep_reinforcement_learning_exercise.ipynb`
2. Review `solutions/01_deep_reinforcement_learning_solution.ipynb`
3. Take `../QUIZZES/quiz_03.md`

**Unit Duration:** 3 weeks  
**Difficulty:** Advanced  
**Prerequisites:** Units 1-2 completion, understanding of deep learning

**Created for:** AIAT 123 - Reinforcement Learning  
**Last Updated:** 2025-01-10

