#!/usr/bin/env python3
"""
Re-scan Course 08–11 notebooks for curriculum keywords (text search inside .ipynb JSON).
Run from repo root: python3 DOCS/curriculum_traceability_scan.py

Output: prints keyword → matching notebook paths (up to 8 per keyword).
Used to refresh evidence in DOCS/CURRICULUM_TRACEABILITY_COURSES_08_11.md.
"""
from __future__ import annotations

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# (course_dir_name, keyword) — keyword searched case-insensitively in notebook source strings
SCAN: list[tuple[str, str]] = [
    ("Course 08", "roc_curve"),
    ("Course 08", "roc_auc"),
    ("Course 08", "U-Net"),
    ("Course 08", "Mask R-CNN"),
    ("Course 09", "DDPG"),
    ("Course 09", "Thompson"),
    ("Course 09", "curriculum learning"),
    ("Course 09", "intrinsic motivation"),
    ("Course 10", "CycleGAN"),
    ("Course 10", "Pix2Pix"),
    ("Course 10", "CLIP"),
    ("Course 10", "AlphaFold"),
    ("Course 10", "OpenAI"),
    ("Course 11", "Kafka"),
    ("Course 11", "RabbitMQ"),
    ("Course 11", "gRPC"),
    ("Course 11", "PMML"),
]


def notebook_text(nb_path: Path) -> str:
    try:
        data = json.loads(nb_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return ""
    parts: list[str] = []
    for cell in data.get("cells", []):
        src = cell.get("source", [])
        if isinstance(src, list):
            parts.append("".join(src))
        elif isinstance(src, str):
            parts.append(src)
    return "\n".join(parts)


def main() -> None:
    results: dict[tuple[str, str], list[str]] = {}
    for course, kw in SCAN:
        key = (course, kw)
        results[key] = []
        base = REPO / course
        if not base.is_dir():
            continue
        kwl = kw.lower()
        for nb in sorted(base.rglob("*.ipynb")):
            if "checkpoint" in nb.name.lower():
                continue
            text = notebook_text(nb)
            if kwl in text.lower():
                rel = nb.relative_to(REPO)
                results[key].append(str(rel))
                if len(results[key]) >= 8:
                    break

    for (course, kw), paths in sorted(results.items()):
        print(f"\n## {course} — «{kw}»")
        if not paths:
            print("  (no matches)")
        else:
            for p in paths:
                print(f"  - {p}")


if __name__ == "__main__":
    main()
