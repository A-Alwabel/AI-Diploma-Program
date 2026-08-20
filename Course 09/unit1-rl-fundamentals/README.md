# Unit 1: Introduction to Reinforcement Learning

## AIAT 123 - Reinforcement Learning

**Unit training hours:** 18 (of 96 total)

## Where this unit sits in the course

You are at the foundation: MDPs, value-style reasoning, Gymnasium
`reset`/`step`, and how to formulate states, actions, and rewards before
leaning on large learning loops. For how Unit 1 connects to Units 2–5, read
[`../RL_LEARNING_JOURNEY.md`](../RL_LEARNING_JOURNEY.md).

## Before You Start

Make sure you are comfortable with:

- Python basics and probability basics (Semester 1, AIAT 111–116)
- Markov process intuition
- The environment setup from `../START_HERE.md`

## Learning Goals

By the end of this unit, you should be able to:

- explain the core reinforcement learning setup
- define an MDP in simple environments
- interpret states, actions, rewards, and policies
- understand value functions and Bellman-style reasoning
- use value and policy iteration at an introductory level
- formulate simple RL problems before moving to larger algorithms

## Study Order

Complete the example notebooks in file order:

1. `examples/01_mdp_example.ipynb` — the MDP framework: states, actions,
   rewards, and transitions in a small worked example
2. `examples/02_mdp_solving.ipynb` — solving a small MDP with policy
   evaluation and improvement
3. `examples/03_value_iteration.ipynb` — the value iteration algorithm and
   Bellman updates in practice
4. `examples/04_openai_gym_setup.ipynb` — setting up Gymnasium environments
   and the `reset`/`step` interaction loop
5. `examples/05_exploration_strategies_epsilon_greedy.ipynb` — epsilon-greedy
   action selection as a first exploration strategy
6. `examples/06_solving_rl_problems_states_actions_rewards.ipynb` — how to
   define states, actions, and rewards for new RL problems
7. `examples/07_mini_projects_cartpole_frozenlake_qlearning_dqn.ipynb` — mini
   projects on CartPole and FrozenLake previewing Q-learning and DQN

## Exercise and Quiz

After the examples:

1. Complete `exercises/01_rl_fundamentals_and_mdps_exercise.ipynb`
2. Take `../QUIZZES/quiz_01.md`

Solutions are released by your instructor.

## Expected Outcome

After Unit 1, you should be able to read a simple RL problem, define its MDP,
reason about rewards and policies, and follow a basic Gymnasium workflow
without guessing what each step is doing.

Next: `../unit2-policy-value/README.md`
