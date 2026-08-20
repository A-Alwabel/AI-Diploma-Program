#!/usr/bin/env python3
"""English-only pass for student notebooks and markdown (2026-08 reorg, Phase 6).

Rules (conservative, reversible via git):
- Markdown cells / .md files:
  * 'English | العربية' heading or line  -> keep the English part
  * a line that is (almost) entirely Arabic -> dropped (they are
    translation twins of the preceding English line in this repo)
  * Arabic quiz option letters 'أ) ب) ج) د)' -> 'A) B) C) D)'
- Code cells:
  * trailing '  # ... Arabic ...' comment -> comment removed, code kept
  * whole-line Arabic comments -> dropped
  * standalone print('...Arabic...') statements -> dropped
  * every edited code cell must still compile(); otherwise the cell is
    reverted untouched (never ship a syntax break)

NEVER edits raw JSON: nbformat only. Run notebooks after batches.

Usage: strip_bilingual.py "Course 01" [more dirs...]  [--dry]
"""
import re
import sys
from pathlib import Path

import nbformat

AR = re.compile(r"[؀-ۿ]")
OPT = {"أ": "A", "ب": "B", "ج": "C", "د": "D"}

def arabic_ratio(s: str) -> float:
    letters = [ch for ch in s if ch.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for ch in letters if AR.match(ch)) / len(letters)

def clean_md_line(line: str):
    if not AR.search(line):
        return line
    # option letters
    m = re.match(r"^(\s*)([أبجد])\)\s*(.*)$", line)
    if m and arabic_ratio(m.group(3)) < 0.5:
        return f"{m.group(1)}{OPT[m.group(2)]}) {m.group(3)}"
    # 'English | Arabic' split
    if "|" in line and not line.strip().startswith("|"):
        parts = line.split("|")
        keep = [p for p in parts if arabic_ratio(p) < 0.5]
        drop = [p for p in parts if arabic_ratio(p) >= 0.5]
        if drop and keep:
            return "|".join(keep).rstrip()
    # table rows: replace Arabic cells only if entire row isn't structural
    if arabic_ratio(line) >= 0.6:
        return None  # drop pure-Arabic line
    return line

def clean_markdown(text: str) -> str:
    out = []
    for line in text.splitlines():
        new = clean_md_line(line)
        if new is not None:
            out.append(new)
    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned

def clean_code(src: str):
    if not AR.search(src):
        return src, False
    out = []
    for line in src.splitlines():
        if not AR.search(line):
            out.append(line)
            continue
        stripped = line.strip()
        # whole-line Arabic comment
        if stripped.startswith("#") and arabic_ratio(stripped) >= 0.4:
            continue
        # standalone Arabic print
        if re.match(r"^\s*print\(", stripped) and arabic_ratio(stripped) >= 0.4:
            continue
        # trailing Arabic comment on a code line
        m = re.match(r"^(.*?)(\s+#.*)$", line)
        if m and AR.search(m.group(2)) and not AR.search(m.group(1)):
            out.append(m.group(1).rstrip())
            continue
        # Arabic inside a string that also has English ('Eng | عرب')
        if "|" in line:
            new = re.sub(r"\s*\|\s*[؀-ۿ][^\"']*", "", line)
            if new != line and not AR.search(new):
                out.append(new)
                continue
        out.append(line)  # keep anything we can't handle safely
    new_src = "\n".join(out)
    try:
        compile(new_src if not new_src.lstrip().startswith(("%", "!")) else "pass",
                "<cell>", "exec")
    except SyntaxError:
        return src, False  # revert
    return new_src, new_src != src

def process_notebook(p: Path, dry: bool):
    nb = nbformat.read(p, as_version=4)
    changed = False
    for c in nb.cells:
        if c.cell_type == "markdown" and AR.search(c.source):
            new = clean_markdown(c.source)
            if new != c.source:
                c.source = new
                changed = True
        elif c.cell_type == "code":
            new, did = clean_code(c.source)
            if did:
                c.source = new
                changed = True
    if changed and not dry:
        # executed notebooks carry cell ids, legal only from nbformat 4.5
        nb.nbformat_minor = max(nb.get("nbformat_minor", 4), 5)
        nbformat.validate(nb)
        nbformat.write(nb, p)
    return changed

def process_md(p: Path, dry: bool):
    txt = p.read_text(encoding="utf-8", errors="ignore")
    if not AR.search(txt):
        return False
    new = clean_markdown(txt)
    if new != txt and not dry:
        p.write_text(new, encoding="utf-8")
    return new != txt

def main():
    args = [a for a in sys.argv[1:] if a != "--dry"]
    dry = "--dry" in sys.argv
    nb_changed = md_changed = 0
    changed_nbs = []
    for root in args:
        for p in sorted(Path(root).rglob("*.ipynb")):
            if ".ipynb_checkpoints" in str(p):
                continue
            if process_notebook(p, dry):
                nb_changed += 1
                changed_nbs.append(str(p))
        for p in sorted(Path(root).rglob("*.md")):
            if process_md(p, dry):
                md_changed += 1
    print(f"{'DRY: ' if dry else ''}changed {nb_changed} notebooks, {md_changed} markdown files")
    for p in changed_nbs:
        print("  nb:", p)

if __name__ == "__main__":
    main()
