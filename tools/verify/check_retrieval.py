"""Verify the 35 cumulative retrieval quizzes. Rewritten after the first version produced
three false positives: it missed a whole block whose headings read '### 1. [Course 07 ...]'
rather than '### Question 1'; it read the word 'answer' inside a question's own sentence as
an answer key; and it flagged 'keeping only 84.7% of the variance' as an 'Only X' giveaway
when that is ordinary quantitative prose. A checker that cries wolf gets ignored."""
import re, pathlib, collections
R = pathlib.Path("/Users/abdullah/Downloads/AI Diploma/RETRIEVAL")
I = pathlib.Path("/Users/abdullah/AI-Diploma-Instructor/retrieval-keys")
QH  = re.compile(r"^#{2,4}\s*(?:question|q|item)?\s*\d+\s*(?:[.):\]\u2014-]|$)", re.I)
OPT = re.compile(r"^\s*[-*]?\s*\(?([A-Da-d])[\).]\s+(.*\S)")
# A giveaway is structural: the option STARTS with 'Only', or is an all/none/both stem.
GIVEAWAY = re.compile(r"^only\b|^all of the above|^none of the above|^both [ab] and [ab]\b", re.I)
# An answer key is a standalone marker line, not the word 'answer' inside a sentence.
KEYLINE  = re.compile(r"^\s*\*{0,2}(answer|correct answer|key|solution)\*{0,2}\s*[:=]\s*\**[A-D]\b", re.I)
COURSE = re.compile(r"(?:Course|AIAT)\s*0?(\d{1,2})|\bC0?(\d{1,2})\b")

problems, weeks = [], {}
for f in sorted(R.glob("week_*.md")):
    t = f.read_text(encoding="utf-8", errors="replace")
    items, cur = [], None
    for l in t.splitlines():
        if QH.match(l): cur = []; items.append(cur)
        elif cur is not None:
            m = OPT.match(l)
            if m: cur.append((m.group(1).upper(), m.group(2)))
    weeks[f.name] = items
    if len(items) != 10: problems.append(f"{f.name}: {len(items)} items, expected 10")
    for n, it in enumerate(items, 1):
        for a, txt in it:
            if GIVEAWAY.match(txt.strip()):
                problems.append(f"{f.name} item {n}: giveaway option {a}: {txt[:60]}")
    for l in t.splitlines():
        if KEYLINE.match(l): problems.append(f"{f.name}: ANSWER KEY ON STUDENT PATH -> {l.strip()[:60]}")

tot = sum(len(v) for v in weeks.values())
print(f"weeks {len(weeks)}  keys {len(list(I.glob('*.md')))}  items {tot}  (expected 350)")

print("\nSPACING - the whole point. Courses each week draws on:")
late = tot_late = 0
for name in sorted(weeks, key=lambda n: int(re.search(r"\d+", n).group())):
    wk = int(re.search(r"\d+", name).group())
    cs = sorted({int(a or b) for a, b in COURSE.findall((R/name).read_text(errors="replace")) if (a or b) and 1 <= int(a or b) <= 12})
    if wk >= 20:
        tot_late += 1; late += (1 in cs)
    if wk in (1, 5, 10, 15, 20, 25, 30, 35): print(f"  week {wk:>2}: {cs}")
print(f"\nWeeks 20+ still asking about Course 01: {late}/{tot_late}")

# every course revisited after its teaching window?
seen = collections.Counter()
for name in weeks:
    for c in {int(a or b) for a, b in COURSE.findall((R/name).read_text(errors="replace")) if (a or b) and 1 <= int(a or b) <= 12}:
        seen[c] += 1
print("Weeks each course appears in:", {f"C{c:02d}": seen[c] for c in sorted(seen)})
print(f"\nPROBLEMS: {len(problems)}")
for p in problems[:12]: print("   ", p)
