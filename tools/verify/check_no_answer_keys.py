#!/usr/bin/env python3
"""Gate: no answer keys / solutions on the student path.

Fails if any tracked file under Course */ (student tree):
- lives in a solutions/ or SOLUTION/ directory,
- has 'solution' in its filename,
- or contains an inline answer-key marker in markdown
  ('## Answer Key', '**Answer:**' with content, 'INSTRUCTOR USE ONLY',
   '**Model Answer', '**Sample Answer').
"""
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

MARKER = re.compile(
    r"^#{1,3}\s*.{0,3}Answer Key"
    r"|\*\*(Answer|Sample Answer|Model Answer|Expected Answer)[:：]\*\*\s*\S"
    r"|INSTRUCTOR (USE ONLY|SOLUTION)",
    re.M,
)

def main():
    all_files = subprocess.run(["git", "-C", str(REPO), "ls-files"],
                               capture_output=True, text=True).stdout.splitlines()
    files = [f for f in all_files if f.startswith("Course ")]
    bad = []
    for f in files:
        low = f.lower()
        if "/solutions/" in low or "/solution/" in low or "solution" in Path(f).name.lower():
            bad.append((f, "solution file on student path"))
            continue
        if f.endswith(".md") and ("quiz" in low or "exam" in low or "test" in low or "assessment" in low):
            txt = (REPO / f).read_text(encoding="utf-8", errors="ignore")
            m = MARKER.search(txt)
            if m:
                bad.append((f, f"inline marker: {m.group(0)[:40]!r}"))
            # An odd number of ``` fences means one opener was lost (bilingual strips ate a few),
            # which leaves the solution code below a question visible to students.
            if txt.count("```") % 2:
                bad.append((f, "unbalanced code fences — a solution block may be exposed"))
    if bad:
        print(f"ANSWER-KEY GATE: {len(bad)} violation(s)")
        for f, why in bad:
            print(f"  {f}: {why}")
        return 1
    print(f"Answer-key gate: clean ({len(files)} tracked student files scanned). ✓")
    return 0

if __name__ == "__main__":
    sys.exit(main())
