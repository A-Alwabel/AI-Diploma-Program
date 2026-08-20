#!/usr/bin/env python3
"""Gate: every relative markdown link in tracked .md files resolves,
and student-facing docs do not reference instructor-internal material.

Checks:
- [text](relative/path) links resolve on disk (anchors/#fragments and
  http(s)/mailto links are skipped)
- bare-file mentions of known ghost files (SAFETY_PROCEDURES.md,
  MASTER_NOTEBOOK_INDEX.md, COURSE_SUMMARY.md, CURRICULUM_SUMMARY_REPORT.md)
- student files referencing instructor-internal docs
  (DETAILED_UNIT_DESCRIPTIONS.md, COMPLETE_COURSE_STRUCTURE_AND_CLOS.md,
  SOLUTIONS_ALL, DOCS/SOLUTIONS)
"""
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
GHOSTS = ["SAFETY_PROCEDURES.md", "MASTER_NOTEBOOK_INDEX.md", "COURSE_SUMMARY.md",
          "CURRICULUM_SUMMARY_REPORT.md"]
INTERNAL = ["DETAILED_UNIT_DESCRIPTIONS.md", "COMPLETE_COURSE_STRUCTURE_AND_CLOS.md",
            "SOLUTIONS_ALL", "DOCS/SOLUTIONS"]

def main():
    files = subprocess.run(["git", "-C", str(REPO), "ls-files", "*.md"],
                           capture_output=True, text=True).stdout.splitlines()
    errors = []
    for f in files:
        p = REPO / f
        txt = p.read_text(encoding="utf-8", errors="ignore")
        for m in LINK.finditer(txt):
            target = m.group(1).split("#")[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            t = (p.parent / target).resolve()
            if not t.exists():
                errors.append(f"{f}: dead link -> {m.group(1)}")
        is_student = f.startswith("Course ") or f.startswith("README")
        if is_student:
            for g in GHOSTS:
                if g in txt:
                    errors.append(f"{f}: references ghost file {g}")
            for i in INTERNAL:
                if i in txt:
                    errors.append(f"{f}: references instructor-internal {i}")
    if errors:
        print(f"LINK GATE: {len(errors)} problem(s)")
        for e in errors:
            print(" ", e)
        return 1
    print(f"Link gate: clean ({len(files)} markdown files). ✓")
    return 0

if __name__ == "__main__":
    sys.exit(main())
