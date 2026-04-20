# Unit 3: Deep Reinforcement Learning
## AIAT 123 - Reinforcement Learning

## Bridge from Unit 2

Unit 2 emphasized **tabular** updates (one entry per state or state–action pair). Unit 3 keeps the same goals—evaluation and control—but uses **function approximation** (typically neural networks) so larger or continuous observation structures stay tractable. Expect the same questions about targets, data, and stability, now in a deep learning setting.

## Before You Start

Make sure you have completed Unit 2 and are comfortable with:

- tabular RL basics
- neural networks and backpropagation
- PyTorch basics from Course 08

## Learning Objectives

By the end of this unit, you should be able to:
- Understand Deep Q-Networks (DQN)
- Explain why deep RL is needed beyond tabular methods
- Implement introductory policy-gradient style training
- Understand the actor-critic idea and why it helps stabilize learning
- Interpret training, evaluation, and optimization choices in small deep RL setups
- Explain major stability challenges in deep RL training

---

## Topics Covered

Based on the numbered student-facing notebooks in this unit, the required path
focuses on introductory deep RL using small Gym-style environments and
teacher-friendly implementations.

1. **Introduction to Deep Reinforcement Learning**
   - Why deep RL?
   - Combining deep learning with RL
   - Function approximation in RL
   - Challenges in deep RL

2. **Deep Q-Networks (DQN)**
   - Q-learning with neural networks
   - Experience replay
   - Target networks
   - Why DQN is more stable than naive neural Q-learning
   - Small-environment applications and interpretation

3. **Policy Gradient Methods**
   - REINFORCE algorithm
   - Policy-gradient intuition
   - Advantages and challenges
   - Why direct policy learning can help

4. **Actor-Critic Methods**
   - Actor-Critic architecture
   - Policy + value interaction
   - Why critics reduce variance
   - PPO as a stability-oriented extension discussed at a simplified level

5. **Training, Evaluation, and Optimization**
   - Monitoring rewards and learning curves
   - Replay, target networks, and reward shaping
   - Hyperparameter sensitivity

6. **Challenges in Deep RL**
   - Exploration vs exploitation dilemma
   - Sample efficiency
   - Stability and convergence
   - Generalization and overfitting

### Important scope note

The numbered student path in this unit does **not** provide a full dedicated
implementation lesson for:

- Atari-scale DQN training
- Double DQN or Dueling DQN
- A2C or A3C as separate implementation blocks
- DDPG for continuous control

These topics should be treated as supplemental or instructor-led extensions
unless dedicated student-facing notebooks are added later.

---

## Unit Breakdown

**Theoretical Hours:** 6  
**Practical Hours:** 13  
**Total Hours:** 19

### Theoretical Content

- Deep RL fundamentals
- DQN foundations
- Policy gradient methods
- Actor-Critic intuition
- Simplified PPO framing
- Training challenges and stability ideas

### Practical Content

- Implementing DQN from scratch
- Training DQN in small Gym-style environments
- Building introductory policy-gradient style code
- Studying actor-critic ideas through simplified examples
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

They are preserved as source/reference notebooks and should not replace the
numbered student path. They are archived under `../DOCS/REFERENCE_NOTEBOOKS/`.

### Important note

The notebook `examples/03_ppo_algorithm.ipynb` should be taught as a bridge from
policy-gradient intuition toward PPO-style stability ideas unless the lesson is
expanded into a fuller PPO implementation later.

Student rule:

- The required path in this unit is the numbered notebooks only.
- Long descriptive filenames and DDPG-related material are supplemental unless
  your instructor assigns them.
- Treat advanced variants such as Atari DQN, Double/Dueling DQN, A2C, A3C, and
  DDPG as outside the required numbered path unless explicitly assigned.

## Exercise and Quiz

1. Complete `exercises/01_deep_reinforcement_learning_exercise.ipynb`
2. Take `../QUIZZES/quiz_03.md`

**Unit Duration:** 3 weeks  
**Difficulty:** Advanced  
**Prerequisites:** Units 1-2 completion, understanding of deep learning

**Created for:** AIAT 123 - Reinforcement Learning  
**Last Updated:** 2025-01-10

