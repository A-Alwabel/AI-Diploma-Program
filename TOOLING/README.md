# Tooling — being handed a repository and being useful

Six two-hour lessons, 12 contact hours, costed in the teaching plan against four named sessions
(C02 U4, C02 U5, C05 U4, C11 U1). Not a block: each lesson is delivered at the week the student
first hits the problem it answers. Kernel: `ai-diploma` for all six.

| # | Lesson | Delivered at | The problem it answers |
|---|--------|--------------|------------------------|
| 01 | [The shell: where your files actually are](examples/01_shell_and_filesystem.ipynb) | Week 2, inside Course 01 | "My notebook can't find the file." |
| 03 | [Environments: why it works on your machine and not on theirs](examples/03_environments_and_dependencies.ipynb) | Week 3, before Course 02's libraries | "It works for you and not for me." |
| 04 | [Reading a traceback](examples/04_reading_a_traceback.ipynb) | Week 6, after the first real failures | The largest gap measured in this diploma: until it was written, no notebook here showed a student an error. |
| 02 | [Git: undo, history, and working with another person](examples/02_git_for_one_and_for_two.ipynb) | Week 12, before peer review starts | Peer review is undeliverable without it. |
| 05 | [Profiling: measure before you optimise](examples/05_measuring_before_optimising.ipynb) | Week 15, inside Course 05 | "It's slow" becomes a measurement. |
| 06 | [Handing over a repository](examples/06_handing_over_a_repository.ipynb) | Week 31, before the Course 12 capstone | The capstone is itself a handover. |

Every lesson ends with the student having done the thing on a scratch directory the notebook
creates and removes. Anything that touches git runs in a scratch repository, never in this one.

**Honest note.** This strand has no outcome evidence behind it; the research pass ranked it sixth
for that reason and then observed that peer review, code review and repository handover are all
undeliverable without it. It is here as a prerequisite, not as a proven intervention. Market
evidence does exist: about 16% of junior European AI/data postings name git or CI/CD.
