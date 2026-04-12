# Quiz 05 Solution
## AIAT 123 - Reinforcement Learning

## Answer Key

**Teaching Notes**: Focus on conceptual transfer from the Unit 5 notebooks.
Students should show they can frame RL application problems, explain
trade-offs, and use correct terminology without overstating what a simple
notebook demo proves.

**Grading**: Use the point values from the quiz. For open questions, award
partial credit for correct framing even if the wording is not identical to
the sample answer.

## Detailed Answers

### Question 1
- Correct answer: `b`
- Explanation: In a cooperative multi-agent setting, agents work toward a
  shared objective and may share rewards, observations, or coordination
  signals. The key idea is that success is judged at the team level, not only
  by one agent's individual reward.

### Question 2
- Correct answer: `b`
- Explanation: Model-based RL learns or uses a model of transitions and/or
  rewards, which allows planning or simulated rollouts. That often improves
  sample efficiency, but it does not guarantee the highest final reward in
  every problem.

### Question 3
- Correct answer: `b`
- Explanation: Hierarchical RL helps with long-horizon problems by decomposing
  behavior into higher-level choices and lower-level actions. Options are not
  just single actions; they are temporally extended behaviors.

### Question 4
- Correct answer: `a`
- Explanation: Robotics is a real RL application area. A common pattern is to
  train in simulation, then transfer the learned policy to real hardware with
  extra care for robustness and safety.

### Question 5 (Code)
Accept equivalent pseudocode if it clearly models a joint state, updates both
agents, uses a shared team reward, and ends when both agents reach the goal.

```python
class MultiAgentGridWorld:
    def __init__(self, size=5):
        self.size = size
        self.goal = (4, 4)
        self.reset()

    def reset(self):
        self.agent1_pos = (0, 0)
        self.agent2_pos = (0, 0)
        return (self.agent1_pos, self.agent2_pos)

    def _move(self, position, action):
        row, col = position

        if action == "up":
            row = max(0, row - 1)
        elif action == "down":
            row = min(self.size - 1, row + 1)
        elif action == "left":
            col = max(0, col - 1)
        elif action == "right":
            col = min(self.size - 1, col + 1)

        return (row, col)

    def step(self, actions):
        action1, action2 = actions
        self.agent1_pos = self._move(self.agent1_pos, action1)
        self.agent2_pos = self._move(self.agent2_pos, action2)

        joint_state = (self.agent1_pos, self.agent2_pos)
        both_at_goal = (
            self.agent1_pos == self.goal and self.agent2_pos == self.goal
        )

        if both_at_goal:
            reward = 10
            done = True
        else:
            reward = -1
            done = False

        observations = {
            "agent1": self.agent1_pos,
            "agent2": self.agent2_pos,
            "joint_state": joint_state,
        }
        rewards = {"agent1": reward, "agent2": reward}

        return observations, rewards, done
```

What to look for in grading:
- Joint state represented as both positions together.
- Both agents move inside `step(actions)`.
- Reward reflects cooperation, not independent selfish rewards.
- Episode ends when both agents reach the goal.

### Question 6
Expected points:
- Goal-conditioned RL conditions behavior on a goal input, not only on the
  current state.
- Standard RL usually learns behavior for one task objective at a time, while
  goal-conditioned RL can reuse one policy across many goals.
- A valid application example: navigation to different target locations,
  robot reaching different objects, or moving an agent to different desired
  states.

Sample answer:
Goal-conditioned RL adds the goal as part of the input to the policy or value
function. Instead of learning only "what should I do in this state?", the
agent learns "what should I do in this state for this goal?". That makes it
useful when the same system must solve many related targets, such as a robot
that must reach different positions on demand.

### Question 7
Expected points:
- Model-based RL may be more sample efficient because it can plan with a model.
- Model-free RL may be simpler and avoid errors caused by a bad learned model.
- Students should name one setting where sample efficiency/planning matters.
- Students should name one setting where robustness/simplicity matters.

Sample answer:
One major trade-off is sample efficiency versus model error risk. Model-based
RL can be preferred when real data is expensive, such as robotics or a
resource-constrained system, because planning with a model can reduce the
amount of real interaction needed. Model-free RL can be preferred when the
environment is too complex to model accurately and we want a simpler learning
loop, even if it needs more direct experience.

### Question 8
Expected points:
- State may include user context, page context, time, prior clicks, or session
  features.
- Action is which ad or ad layout to show.
- Reward may be click-through, conversion, revenue, or a longer-term quality
  metric.
- A reasonable framing may be contextual bandits for one-step recommendation
  or full RL if long-term user effects matter.
- Ethical issue examples: manipulation, unfair targeting, filter bubbles, or
  optimizing short-term clicks at the expense of user well-being.

Sample answer:
State could include user profile features, current page category, device type,
and recent interaction history. Action is the ad to display or which ad slot
configuration to choose. Reward could be click-through, conversion value, or
long-term engagement if repeated exposure matters. A contextual bandit may be
a reasonable starting point if each page view is treated as a mostly one-step
decision, while fuller RL becomes more appropriate if current ad choices
affect future behavior. One ethical risk is optimizing attention in a way
that becomes manipulative or unfairly targets vulnerable users.

## Common Mistakes
- Treating cooperative multi-agent RL as if each agent has completely separate
  objectives.
- Saying model-based RL is always better instead of describing a trade-off.
- Describing options as single primitive actions rather than temporally
  extended behaviors.
- Mixing up goal-conditioned RL with meta-learning.
- Proposing rewards that only capture short-term clicks without mentioning the
  risk of reward misspecification.

## Additional Resources
- Unit 5 example notebooks and slides.
- The glossary and algorithm cheat sheet in `DOCS/`.
