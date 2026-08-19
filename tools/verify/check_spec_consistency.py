#!/usr/bin/env python3
"""Consistency gate for the curriculum spec docs.

Authoritative numbers come from the official TVTC/Tuwaiq PDF (see
AI-Diploma-Instructor/OFFICIAL_SPEC.md). This script asserts that the
in-repo spec docs agree with them:

1. docs/DETAILED_UNIT_DESCRIPTIONS.md — per-course header totals match the
   official table, and each course's five unit-hour headings sum to it.
2. docs/COMPLETE_COURSE_STRUCTURE_AND_CLOS.md — each course's five
   unit-hour lines sum to the official total.
3. Grand total = 944.

Exit 0 = consistent; exit 1 = any mismatch (printed).
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

OFFICIAL = {  # code -> (total hours, [unit totals])
    "111": (64, [12, 12, 12, 14, 14]),
    "112": (96, [18, 19, 19, 20, 20]),
    "113": (64, [12, 12, 12, 14, 14]),
    "114": (96, [18, 19, 19, 20, 20]),
    "115": (96, [18, 19, 19, 20, 20]),
    "116": (64, [12, 12, 12, 14, 14]),
    "121": (64, [12, 12, 12, 14, 14]),
    "122": (64, [12, 12, 12, 14, 14]),
    "123": (96, [18, 19, 19, 20, 20]),
    "124": (64, [12, 12, 12, 14, 14]),
    "125": (96, [18, 19, 19, 20, 20]),
    "126": (80, [14, 15, 17, 17, 17]),
}

errors = []

def check_detailed():
    text = (REPO / "docs/DETAILED_UNIT_DESCRIPTIONS.md").read_text()
    # split into course sections
    parts = re.split(r"^## 📘 COURSE \d+: AIAT (\d{3})", text, flags=re.M)
    it = iter(parts[1:])
    for code, body in zip(it, it):
        total_off, units_off = OFFICIAL[code]
        m = re.search(r"\| Total Training Hours \| (\d+)", body)
        if not m:
            errors.append(f"DETAILED {code}: no Total Training Hours line")
            continue
        if int(m.group(1)) != total_off:
            errors.append(f"DETAILED {code}: header total {m.group(1)} != official {total_off}")
        units = [int(x) for x in re.findall(r"#### 📖 Unit \d+: .*?\((\d+) hours:", body)]
        if len(units) != 5:
            errors.append(f"DETAILED {code}: found {len(units)} unit headings, expected 5")
        elif units != units_off:
            errors.append(f"DETAILED {code}: unit hours {units} != official {units_off}")

def check_clos():
    text = (REPO / "docs/COMPLETE_COURSE_STRUCTURE_AND_CLOS.md").read_text()
    parts = re.split(r"^### Course \d+: AIAT (\d{3})", text, flags=re.M)
    it = iter(parts[1:])
    for code, body in zip(it, it):
        total_off, units_off = OFFICIAL[code]
        units = [int(x) for x in re.findall(r"\*\*Unit \d+: .*?= (\d+) hours\)", body)]
        if len(units) != 5:
            errors.append(f"CLOS {code}: found {len(units)} unit lines, expected 5")
        elif units != units_off:
            errors.append(f"CLOS {code}: unit hours {units} != official {units_off}")

def main():
    check_detailed()
    check_clos()
    grand = sum(t for t, _ in OFFICIAL.values())
    if grand != 944:
        errors.append(f"official table sums to {grand}, expected 944")
    for course, (t, u) in OFFICIAL.items():
        if sum(u) != t:
            errors.append(f"official table {course}: units sum {sum(u)} != total {t}")
    if errors:
        print("SPEC INCONSISTENT:")
        for e in errors:
            print(" -", e)
        return 1
    print("Spec docs consistent with the official table (944h). ✓")
    return 0

if __name__ == "__main__":
    sys.exit(main())
