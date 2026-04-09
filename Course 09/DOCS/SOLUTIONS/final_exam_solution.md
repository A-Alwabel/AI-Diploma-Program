# Final Exam Solution Guide
## AIAT 123 - Reinforcement Learning

## Instructor Use Only

## Part 1: Multiple Choice

1. B
2. B
3. B
4. B

## Part 2: Short Answer Guidance

### Question 5

Strong answers define:

- **state** as what the agent observes
- **action** as a valid choice the agent can take
- **reward** as the feedback signal
- **policy** as the mapping from state to action

The answer should include one concrete environment example.

### Question 6

Strong answers should note:

- Q-learning learns action values and is off-policy
- SARSA learns action values and is on-policy
- Policy Gradient learns policy parameters directly
- Each has different trade-offs for stability, action spaces, and exploration

### Question 7

Strong answers should explain:

- why always exploiting is risky
- why always exploring is inefficient
- how epsilon-greedy works
- how UCB or Thompson Sampling uses uncertainty more explicitly

## Part 3: Practical / Coding

### Question 8

Look for:

- loop over non-terminal states
- evaluation of all actions
- Bellman optimality update
- special handling of terminal states

### Question 9

Look for:

- Q-table initialization
- epsilon-greedy action selection
- environment step
- Q-update rule
- episode loop

## Part 4: Application and Judgment

### Question 10

Strong answers should define a coherent RL problem:

- state
- action
- reward
- one challenge such as delayed reward, sparse reward, or reward
  hacking

### Question 11

Strong answers should mention at least one real risk and one evaluation
method, for example:

- unsafe exploration
- manipulation or unfair exposure
- offline evaluation
- held-out environments
- simulation before deployment
- reward and regret tracking
