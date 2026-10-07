#!/usr/bin/env python3
"""Gate: every notebook declares one of the repo's two kernels.

Why. 218 notebooks once declared `python3`, which on a student's Mac resolves to Xcode's
Python 3.9.6 with none of the packages installed - the lesson dies on the first import. That
was fixed across 343 notebooks, and then it came back twice on 2026-10-07: a verifier's run
rewrote one notebook's kernelspec to the tfenv display name with name `python3`, and a new SQL
lesson was authored with `python3`. A kernelspec is metadata, so nothing else notices.

Allowed: `ai-diploma` (repo .venv, Python 3.14) and `tfenv` (TensorFlow/PyTorch, Python 3.13).
"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
ALLOWED = {"ai-diploma", "tfenv"}
SKIP = (".ipynb_checkpoints", "/.venv/", "/venv/", "/site-packages/", "/node_modules/")
bad, n = [], 0
for p in ROOT.glob("**/*.ipynb"):
    s = "/" + str(p.relative_to(ROOT))
    if any(k in s for k in SKIP): continue
    n += 1
    try: ks = json.load(open(p)).get("metadata", {}).get("kernelspec", {}) or {}
    except Exception as e: bad.append((s, f"unreadable: {e}")); continue
    name = ks.get("name")
    if name not in ALLOWED: bad.append((s, name or "(none)"))
for s, name in bad: print(f"  {name:<12} {s}")
print(f"Kernelspec gate: {len(bad)} of {n} notebooks on a non-repo kernel" + (" ✓" if not bad else " ✗"))
sys.exit(1 if bad else 0)
