#!/usr/bin/env python3
"""Gate: no model answer may sit under a quiz question on the student path.

check_no_answer_keys.py looks for the WORD 'answer' and reported 'clean, 1050 files
scanned' while 26 complete model answers sat under Course 03's questions, formatted as
ordinary headings like '**PCA Steps:**'.

The first version of THIS checker missed 11 of those 26. It only fired when the prompt
matched a verb list, so 'What is the relationship between...', 'How are optimization and
statistics used together...' and - worst - every 'Write NumPy code to:' followed by the
working solution were invisible to it. So the verb list is gone. A student quiz question
carries a prompt and, sometimes, data to work on; it never carries paragraphs of exposition.
That is what this looks for, whatever the wording.
"""
import re, sys, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
QHEAD   = re.compile(r"^#{2,4}\s*(?:question|q)\s*\d+", re.I)
ANYHEAD = re.compile(r"^#{1,6}\s+\S")          # a block also ends at "## Grading Rubric"
MCQ_OPT = re.compile(r"^\s*[-*]?\s*\(?[A-Da-d][\).]\s+\S", re.M)
# Space left for the student, not content: these do not count as exposition.
PLACEHOLDER = re.compile(r"answer key|released by your instructor|show your working|"
                         r"your answer|write your|^\s*```\s*$|^\s*-{3,}\s*$|^\s*\|[\s\-:|]+\|\s*$", re.I)

def leaks(path):
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    starts = [i for i, l in enumerate(lines) if QHEAD.match(l)]
    out = []
    for n, s in enumerate(starts):
        e = len(lines)
        for j in range(s + 1, len(lines)):
            if ANYHEAD.match(lines[j]):
                e = j; break
        body = lines[s + 1:e]
        if MCQ_OPT.search("\n".join(body)):     # options belong to the question
            continue
        # paragraph 1 after the heading is the prompt; anything past it is suspect
        para, seen_blank = [], False
        for l in body:
            if not l.strip():
                seen_blank = True; continue
            if seen_blank:
                para.append(l)
        rest = [l for l in para if len(l.strip()) > 12 and not PLACEHOLDER.search(l)]
        if len(rest) >= 3:
            out.append((s + 1, lines[s].strip(), len(rest), rest[0].strip()[:70]))
    return out

hits = collections.defaultdict(list)
for quiz in sorted(ROOT.glob("Course */QUIZZES/*.md")) + sorted(ROOT.glob("Course */*/quizzes/*.md")):
    for item in leaks(quiz):
        hits[quiz.parts[len(ROOT.parts)]].append((quiz.relative_to(ROOT),) + item)

total = 0
for course in sorted(hits):
    print(f"\n{course}: {len(hits[course])} question block(s) carrying content past the prompt")
    for p, ln, head, n, first in hits[course]:
        print(f"   {p}:{ln}  {head}  ({n} lines)  first: {first}")
    total += len(hits[course])
print(f"\nTOTAL: {total} block(s) to review. Legitimate question data (a matrix to multiply, a\n"
      f"snippet to trace, a scenario) also lands here - judge each; do not delete mechanically.")
sys.exit(1 if total else 0)
