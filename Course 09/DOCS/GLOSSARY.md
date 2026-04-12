# Reinforcement Learning Glossary

## Purpose

Use this glossary when a notebook uses a term that feels familiar but still not
fully clear. Read the definition, then go back to the notebook example and find
where that idea appears in code or output.

## Core Foundations

### Agent

The learner or decision-maker that chooses actions.

### Environment

The world the agent interacts with. It receives the action and returns the next
state, reward, and whether the episode ended.

### State

The information the agent uses to describe the current situation.

### Action

One choice the agent is allowed to make in the current state.

### Reward

Immediate feedback after an action. It tells the agent whether the last step was
good, bad, or neutral.

### Episode

One full run from a starting state until termination or truncation.

### Policy

The rule the agent uses to choose actions in states.

### Deterministic Policy

A policy that chooses one fixed action for each state.

### Stochastic Policy

A policy that chooses actions according to probabilities.

### Return

The total future reward from a point onward, usually discounted.

### Discount Factor (`gamma`)

Controls how much future rewards matter compared with immediate rewards.

### Markov Decision Process (MDP)

A decision-making framework with states, actions, transitions, and rewards.

### Transition

The move from one state to the next after an action.

## Value-Based Learning

### Value Function

An estimate of how good it is to be in a state.

### Q-Value

An estimate of how good it is to take a specific action in a specific state.

### Bellman Equation

An update relationship that connects a value to reward plus future value.

### Value Iteration

A method that repeatedly updates state values toward the optimal values.

### Policy Iteration

A method that alternates between evaluating a policy and improving it.

### Policy Evaluation

Measuring how good a fixed policy is.

### Policy Improvement

Changing the policy after evaluation to choose better actions.

## Model-Free Learning

### Q-Learning

An off-policy method that learns Q-values by updating toward the best next
action value.

### SARSA

An on-policy method that learns from the next action actually chosen by the
current policy.

### Monte Carlo Method

A method that learns from full episode returns after the episode ends.

### Temporal Difference (TD) Learning

A family of methods that update estimates using reward plus another estimate,
without waiting for the full episode return.

### TD Error

The gap between the current estimate and the new target estimate.

### Bootstrapping

Learning from an estimate of the future instead of waiting for all future
rewards to be observed directly.

## Exploration and Decision Balance

### Exploration

Trying uncertain or less-tested actions to gather information.

### Exploitation

Choosing the action that currently looks best.

### Epsilon-Greedy

Choose a random action with probability `epsilon`; otherwise choose the current
best action.

### Epsilon Decay

Reducing `epsilon` over time so the agent explores more early in training and
acts more greedily later.

### Upper Confidence Bound (UCB)

A method that adds an uncertainty bonus so rarely tried actions get more
attention.

### Boltzmann Exploration (Softmax Exploration)

An exploration method that samples actions according to probabilities based on
their estimated values. Higher temperature means more exploration; lower
temperature makes the policy more greedy.

### Thompson Sampling

An exploration method that samples from uncertainty-aware action beliefs.

### Intrinsic Motivation / Curiosity

An exploration idea where the agent gets an extra internal reward for novelty,
surprise, or prediction error, not only for the external task reward.

### Multi-Armed Bandit

A simplified decision problem where the agent repeatedly chooses among actions
with uncertain rewards, without a full state-transition structure like an MDP.

### Regret

The performance lost because the agent did not always choose the best possible
action.

## Deep Reinforcement Learning

### Function Approximation

Using a model, often a neural network, to estimate values or policies instead
of storing everything in a table.

### Deep Q-Network (DQN)

A value-based deep RL method that uses a neural network to estimate Q-values.

### Replay Buffer

A memory of past transitions that can be sampled randomly during training.

### Target Network

A slower-changing network used in DQN to stabilize targets.

### Policy Gradient

A method that updates policy parameters directly to increase expected return.

### Actor-Critic

A method with two parts: an actor that chooses actions and a critic that
evaluates them.

### Proximal Policy Optimization (PPO)

A policy-gradient-based method that limits updates so the policy does not change
too much at once.

### Reward Shaping

Adjusting rewards to guide learning more clearly. Helpful when done carefully,
dangerous when it changes the true objective.

## Advanced Topics and Applications

### Multi-Agent Reinforcement Learning

RL with more than one agent acting in the same environment.

### Hierarchical Reinforcement Learning

RL that breaks a large task into smaller sub-tasks or options.

### Option

A higher-level action that may last for several primitive steps.

### Model-Based Reinforcement Learning

RL that learns or uses a model of environment dynamics for planning.

### World Model

A learned predictive model of how the environment changes.

### Goal-Conditioned RL

RL where the policy takes both the current state and the desired goal as input.

### Sim-to-Real Transfer

Training in simulation, then adapting or deploying the learned behavior in the
real world.

## Student Tip

If a term still feels abstract, ask three questions:

1. Where does it appear in the notebook?
2. What object or variable represents it?
3. How does the output show that it changed?
