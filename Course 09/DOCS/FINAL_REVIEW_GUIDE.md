# Final Review Guide

## Purpose

Use this guide during revision week or before the final exam. It compresses the
full course into the ideas that students should be able to explain clearly.

## The Big Story of the Course

By the end of the course, a student should be able to answer four questions:

1. How do I formulate a problem as reinforcement learning?
2. How do classic RL methods learn from rewards?
3. Why do we need deep RL for larger problems?
4. How do we judge whether an RL system is useful, safe, and deployable?

## Unit-by-Unit Review

### Unit 1: Foundations

You must understand:

- agent, environment, state, action, reward
- MDP structure
- policy and value intuition
- why problem formulation matters
- basic Gymnasium environment interaction

You should be able to explain:

- the difference between state and reward
- why the policy belongs to the agent, not the environment
- how a badly designed reward can break learning

Quick self-check:

- Can I define an MDP for GridWorld, FrozenLake, or CartPole?
- Can I explain why terminal states are handled differently?
- Can I describe one simple policy in plain English?

### Unit 2: Classical Prediction and Control

You must understand:

- Monte Carlo methods
- TD learning
- Q-learning
- SARSA
- policy iteration vs value iteration at a high level

You should be able to explain:

- off-policy vs on-policy
- bootstrapping
- why Monte Carlo waits until the episode ends
- why TD methods can update earlier

Quick self-check:

- Can I write or explain a Q-learning update?
- Can I tell the difference between SARSA and Q-learning?
- Can I explain what a Q-table means?

### Unit 3: Deep Reinforcement Learning

You must understand:

- why tabular methods are not enough for larger problems
- DQN basics
- replay buffer and target network
- policy gradient intuition
- actor-critic intuition
- PPO as a stability-focused policy method

You should be able to explain:

- why DQN still follows the Q-learning idea
- what the actor and critic each do
- why deep RL can become unstable
- why reward shaping can help or hurt

Quick self-check:

- Can I explain DQN without only repeating code terms?
- Can I say why replay and target networks matter?
- Can I describe PPO as "careful policy updating" in plain language?

### Unit 4: Exploration and Exploitation

You must understand:

- the exploration-exploitation dilemma
- epsilon-greedy
- UCB
- why tuning exploration matters
- why one exploration strategy is not best everywhere

You should be able to explain:

- what regret means
- why under-exploration is dangerous
- why over-exploration wastes learning time

Quick self-check:

- Can I compare epsilon-greedy with UCB?
- Can I explain why uncertainty matters?
- Can I interpret a reward or regret plot?

### Unit 5: Applications and Advanced Topics

You must understand:

- how RL is applied to games, optimization, recommendation, and control
- multi-agent RL
- hierarchical RL
- model-based RL
- goal-conditioned RL
- evaluation, ethics, and safety concerns

You should be able to explain:

- how to define state, action, and reward for a real-world task
- why deployment is harder than training
- one ethical or safety risk in a real RL system

Quick self-check:

- Can I formulate recommendation or resource optimization as RL?
- Can I explain the difference between model-based and model-free RL?
- Can I name one risk such as reward hacking or unsafe exploration?

## Final Exam Preparation Strategy

### The Night Before

- Review this guide once from start to end
- Review `DOCS/GLOSSARY.md`
- Review `DOCS/ALGORITHM_CHEAT_SHEET.md`
- Re-open the most difficult notebooks only for concept refresh, not for full study

### 60-Minute Fast Review Plan

1. Spend 10 minutes on Unit 1 concepts
2. Spend 15 minutes on Q-learning, SARSA, Monte Carlo, and TD
3. Spend 15 minutes on DQN, Actor-Critic, and PPO
4. Spend 10 minutes on exploration methods
5. Spend 10 minutes on applications, model-based RL, and safety

## Common Exam Mistakes

- Writing a definition without connecting it to an example
- Mixing up reward and return
- Mixing up Q-learning and SARSA
- Describing DQN as if it were unrelated to Q-learning
- Forgetting to mention stability when discussing deep RL
- Ignoring ethical or deployment risks in application questions

## What Strong Answers Usually Contain

- clear definitions
- one simple example
- correct comparison language
- one limitation or risk
- connection to a practical setting

## Final Confidence Checklist

Before the final exam, ask:

- Can I explain RL basics without looking at notes?
- Can I compare the major algorithms in plain English?
- Can I write or sketch simple update rules?
- Can I formulate a real-world RL problem?
- Can I name one safety or ethics concern?

If the answer is "not yet" for one of these, revisit the matching unit first.
