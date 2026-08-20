# Unit 5: Applications and Advanced Topics in RL

## AIAT 123 - Reinforcement Learning

**Unit training hours:** 20 (of 96 total)

## Bridge from Units 1–4

Units 1–4 built the core stack: formulation, tabular methods, deep RL, and
exploration design. Unit 5 replays that vocabulary in applied settings:
application domains, multi-agent coordination, and extension directions such as
hierarchical, model-based, and goal-conditioned RL. Treat each application
topic as a lens on the same RL loop, not a separate subject.

## Before You Start

Make sure you have completed Units 1 to 4 and are comfortable with:

- classical RL methods
- deep RL basics
- evaluation metrics and training curves
- exploration strategy trade-offs

## Learning Objectives

By the end of this unit, you should be able to:

- apply RL to problems across several domains (games, optimization, control)
- work with multi-agent RL in cooperative and competitive settings
- discuss ethical, safety, and deployment considerations in RL applications
- explain extension topics such as hierarchical, model-based, and
  goal-conditioned RL at an introductory level
- connect application notebooks back to the earlier RL foundations

## Study Order

Complete the example notebooks in file order:

1. `examples/01_rl_applications.ipynb` — survey of RL applications across
   domains such as robotics, games, finance, and optimization
2. `examples/02_game_playing_agent.ipynb` — building an RL agent for game
   playing
3. `examples/03_resource_optimization.ipynb` — RL for resource optimization
   problems
4. `examples/04_multi_agent_rl.ipynb` — multi-agent RL: cooperative and
   competitive agents
5. `examples/05_hierarchical_rl_options.ipynb` — hierarchical RL and the
   options framework
6. `examples/06_model_based_rl_world_models.ipynb` — model-based RL with
   learned world models
7. `examples/07_model_based_vs_model_free_comparison.ipynb` — comparing
   model-based and model-free RL approaches
8. `examples/08_goal_conditioned_rl.ipynb` — goal-conditioned RL for complex
   tasks

## Scope note

Meta-learning, few-shot RL, and AlphaGo-style search+RL systems are outside the
required path unless your instructor assigns extra material. Safety and ethics
are covered at discussion level within the notebooks above.

## Exercise and Quiz

1. Complete `exercises/01_rl_exercise.ipynb`
2. Take `../QUIZZES/quiz_05.md`

Solutions are released by your instructor.

## Connection to Project Work

This unit is the closest preparation stage for the course project in
`../PROJECTS/RL_Game_Agent/README.md`. As you finish this unit, you should be
ready to connect RL concepts to a complete application workflow.

## Prerequisites

Units 1–4 completion.

Next: the course project (`../PROJECTS/`), then `../ASSESSMENTS/Final_Exam.md`.
