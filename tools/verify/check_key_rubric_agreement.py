#!/usr/bin/env python3
"""Gate: an exam's solution key and its rubric must state the SAME answers.

Why this exists. On 2026-09-01 four courses were found where the two documents
disagreed. Course 04 was the worst: the key read D,B,A,C,C,A and the rubric read
D,A,B,B,A,B, so an instructor grading Part 1 from the rubric marked a fully correct
paper 25 of 30 WRONG. Course 09 showed the mechanism: commit b999ba64 permuted the
answer letters on the student paper, the paired instructor commit updated the key,
and nobody touched the rubric - which went on saying 'all four are B'. The fix for
clustered letters created a worse defect than the one it fixed.

Run from the repo root. Reads the instructor repo, which is not public.
"""
import re, sys, pathlib, collections

INSTR = pathlib.Path("/Users/abdullah/AI-Diploma-Instructor")

# "Key: C, A, D, B, C, A"  /  "Answers: 1-B, 2-D, 3-A"  /  "Q1 C · Q2 A · Q3 D"
SEQ = re.compile(r"(?:key|answers?)\s*[:\-]\s*((?:\**(?:Q?\d+\s*[-.:]?\s*)?[A-D]\**\s*[,;·|]\s*){3,}"
                 r"\**(?:Q?\d+\s*[-.:]?\s*)?[A-D]\**)", re.I)
LETTER = re.compile(r"\b([A-D])\b")
# A bare sequence with no "Key:" label, e.g. a paragraph ending "**B, D, A, C, B, D**".
BARE = re.compile(r"\*\*([A-D](?:\s*,\s*[A-D]){3,})\*\*")
# Per-question headings: "### Q1 - **B**" or "### Question 3 ... **A**". These are the
# second place a key states its answers, and the place Course 09 forgot to update.
PERQ = re.compile(r"^#{2,4}\s*(?:Q|Question)\s*(\d+)\b[^\n]*?\*\*\(?([A-D])\)?\*\*", re.I)

# A revision note that honestly records the OLD key spans several lines:
# "The previous Final_Exam_Solution.md gave the MCQ key as **C, B, A, D, A, B**".
# Looking at one line alone flags those as live disagreements, so look back two lines.
HISTORY = re.compile(r"superseded|old key|previously|the previous|originally|pre-permutation|"
                     r"\bmoved from\b|\bwas\b|\bwere\b|disagreed|corrected|first pass|"
                     r"as originally printed|prior to|\bbefore\b|letter distribution", re.I)

def sequences(path):
    out = []
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    for n, line in enumerate(lines, 1):
        if any(HISTORY.search(l) for l in lines[max(0, n - 3):n]):
            continue                       # explicitly-labelled historical lines
        # A search course states node-visit orders as "Answer: A, B, C, D". Those are
        # traversal sequences, not option letters. Excluding them stops a false alarm
        # that would train everyone to ignore this gate.
        if re.search(r"\border|visit|travers|path|sequence|neighbou?r|depending on", line, re.I):
            continue
        m = SEQ.search(line) or BARE.search(line)
        if m:
            out.append((n, "".join(LETTER.findall(m.group(1))), line.strip()[:90]))
    # Rebuild the sequence a second, independent way: from the per-question headings.
    perq = {}
    for line in lines:
        h = PERQ.match(line)
        if h:
            perq.setdefault(int(h.group(1)), h.group(2).upper())
    if len(perq) >= 4:
        out.append((0, "".join(perq[k] for k in sorted(perq)), "per-question headings"))
    return out

bad = clean = nokey = 0
for course in sorted(INSTR.glob("Course *")):
    # Only the documents an instructor actually grades from.
    files = sorted(course.glob("exam-keys/**/*.md")) + sorted(course.glob("quiz-keys/**/*.md"))
    found = {f: sequences(f) for f in files}
    found = {f: s for f, s in found.items() if s}
    if not found:
        print(f"{course.name}: no answer line found in any key file  — cannot verify"); nokey += 1; continue
    seqs = collections.defaultdict(list)
    for f, ss in found.items():
        for n, letters, raw in ss:
            seqs[letters].append(f"{f.relative_to(INSTR)}:{n}")
    if len(seqs) == 1:
        letters = next(iter(seqs))
        print(f"{course.name}: OK  {','.join(letters)}  (stated in {sum(len(v) for v in seqs.values())} place(s))")
        clean += 1
    else:
        print(f"{course.name}: *** DISAGREEMENT — {len(seqs)} different answer lines ***")
        for letters, where in sorted(seqs.items(), key=lambda kv: -len(kv[1])):
            print(f"      {','.join(letters) or '(none)'}   <- {'; '.join(where)}")
        bad += 1

print(f"\n{clean} course(s) agree, {bad} disagree, {nokey} unverifiable.")
sys.exit(1 if bad else 0)
