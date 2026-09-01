"""Find model answers that sit under open-response questions with NO 'Answer:' label.
The marker-based gate cannot see these: they are disguised as ordinary headings
(e.g. '**PCA Steps:**') so nothing on the line says 'answer'."""
import re, sys, pathlib

ROOT = pathlib.Path("/Users/abdullah/Downloads/AI Diploma")
OPEN_PROMPT = re.compile(r"\b(explain|describe|compare|discuss|why |what happens|derive|justify|"
                         r"outline|list the steps|walk through|how does|how do you)\b", re.I)
QHEAD = re.compile(r"^#{2,4}\s*(question|q)\s*\d+", re.I)
MCQ_OPT = re.compile(r"^\s*[-*]?\s*\(?[A-Da-d][\).]\s+\S", re.M)

def blocks(text):
    lines = text.splitlines()
    idx = [i for i, l in enumerate(lines) if QHEAD.match(l)]
    for n, s in enumerate(idx):
        e = idx[n + 1] if n + 1 < len(idx) else len(lines)
        yield s + 1, lines[s], lines[s + 1:e]

hits = []
for quiz in sorted(ROOT.glob("Course */QUIZZES/*.md")) + sorted(ROOT.glob("Course */*/quizzes/*.md")):
    text = quiz.read_text(encoding="utf-8", errors="replace")
    for lineno, head, body in blocks(text):
        joined = "\n".join(body)
        if MCQ_OPT.search(joined):          # multiple choice: options are meant to be there
            continue
        if not OPEN_PROMPT.search(joined):  # not an open-response question
            continue
        # strip the question sentence itself, separators and blank lines
        content = [l for l in body if l.strip() and not l.strip().startswith("---")
                   and not OPEN_PROMPT.search(l)]
        # a clean student quiz leaves nothing (or a blank answer space) after the prompt
        substantive = [l for l in content if len(l.strip()) > 12]
        if len(substantive) >= 4:
            hits.append((quiz.relative_to(ROOT), lineno, head.strip(), len(substantive)))

by_course = {}
for p, ln, head, n in hits:
    by_course.setdefault(p.parts[0], []).append((p, ln, head, n))
for c in sorted(by_course):
    print(f"\n{c}: {len(by_course[c])} leaked open-response answers")
    for p, ln, head, n in by_course[c]:
        print(f"   {p}:{ln}  {head}  ({n} content lines)")
print(f"\nTOTAL: {len(hits)} unlabelled model answers on the student path")
