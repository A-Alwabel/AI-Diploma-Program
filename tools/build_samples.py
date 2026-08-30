"""Rebuild the committed dataset samples under Course 04/datasets/samples/.

Students never run this. They read the samples through `tools/data.py`. Run it only when
a full dataset in Course 04/datasets/raw/ changes:

    python "tools/build_samples.py"            # rebuild everything whose full file is present
    python "tools/build_samples.py" titanic    # rebuild one dataset

Two properties every sampler here keeps, on purpose:

1. DETERMINISTIC - fixed seed / fixed even-allocation rule, so re-running produces a
   byte-identical file and git shows no spurious diff.
2. BYTE-EXACT ROWS - every sampler except creditcard_fraud copies whole *lines* out of the
   original file instead of round-tripping through pandas. A pandas round-trip silently
   rewrites `0` as `0.0` wherever a chunk happened to contain a NaN, which would make the
   sample's dtypes differ from the full file's. creditcard_fraud is the one exception: its
   V1..V28 are deliberately rounded to 6 decimal places to fit inside git, and that is
   stated in the loader's printed line and in DATA.md.
"""
from __future__ import annotations

import csv
import io
import json
import sys
from collections import Counter
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "Course 04" / "datasets" / "raw"
SAMPLES = ROOT / "Course 04" / "datasets" / "samples"
SEED = 73

SAMPLES.mkdir(parents=True, exist_ok=True)
report: dict[str, dict] = {}


def _record(key: str, path: Path, full_rows: int, note: str) -> None:
    with path.open("rb") as fh:
        lines = sum(1 for _ in fh)
    size = path.stat().st_size
    report[key] = {
        "file": path.name,
        "sample_rows": lines - (0 if key == "unsw_nb15" else 1),  # unsw has no header
        "full_rows": full_rows,
        "bytes": size,
        "mb": round(size / 1e6, 2),
        "note": note,
    }
    print(f"  -> {path.name}: {report[key]['sample_rows']:,} rows, "
          f"{size/1e6:.2f} MB   ({note})")


def _fields(line: str) -> list[str]:
    """Split one CSV line into fields, respecting quotes."""
    return next(csv.reader(io.StringIO(line)))


def stratified_line_sample(src: Path, dst: Path, key_fn, quota_fn, has_header: bool = True):
    """Copy whole lines out of `src` into `dst`, keeping `quota_fn(key, n)` lines per key.

    The selected lines of a key are spread evenly over every occurrence of that key in the
    file, so a chronological file keeps its full date range and an ordered file keeps its
    shape. No randomness: run it twice, get the same bytes.
    """
    # Pass 1 - how many rows does each key have?
    counts: Counter = Counter()
    with src.open("r", encoding="utf-8", errors="surrogateescape", newline="") as fh:
        if has_header:
            fh.readline()
        for line in fh:
            if line.strip():
                counts[key_fn(_fields(line))] += 1
    n_full = sum(counts.values())

    quota = {k: min(n, max(0, quota_fn(k, n, n_full))) for k, n in counts.items()}
    seen: Counter = Counter()
    kept: Counter = Counter()

    # Pass 2 - even allocation: keep row i of key k iff floor((i+1)*q/N) > floor(i*q/N).
    with src.open("r", encoding="utf-8", errors="surrogateescape", newline="") as fin, \
         dst.open("w", encoding="utf-8", errors="surrogateescape", newline="") as fout:
        header = fin.readline() if has_header else None
        if header is not None:
            fout.write(header)
        for line in fin:
            if not line.strip():
                continue
            k = key_fn(_fields(line))
            q, n, i = quota[k], counts[k], seen[k]
            seen[k] += 1
            if q and ((i + 1) * q) // n > (i * q) // n:
                fout.write(line if line.endswith("\n") else line + "\n")
                kept[k] += 1
    return counts, kept, n_full


# --------------------------------------------------------------------------------------
# creditcard_fraud - the lesson IS the class imbalance, so the sample's fraud rate must
# match the full file's fraud rate. This is the one sampler that rewrites values.
# --------------------------------------------------------------------------------------
def build_creditcard(target_rows: int = 16_000) -> None:
    src = RAW / "creditcard_fraud.csv"
    print(f"creditcard_fraud: reading {src.stat().st_size/1e6:.0f} MB ...")
    df = pd.read_csv(src)
    n_full = len(df)
    frac = target_rows / n_full
    fraud, legit = df[df["Class"] == 1], df[df["Class"] == 0]
    n_fraud = round(len(fraud) * frac)
    out = pd.concat([
        fraud.sample(n=n_fraud, random_state=SEED),
        legit.sample(n=target_rows - n_fraud, random_state=SEED),
    ]).sort_index()                       # sort_index puts the rows back in Time order
    dst = SAMPLES / "creditcard_fraud.sample.csv"
    # 6 decimal places on V1..V28 and Amount. Those columns are PCA components with a
    # standard deviation of order 1, so 1e-6 sits four orders of magnitude below anything
    # a lesson computes. It is done for one reason only: to fit the file inside git.
    out.to_csv(dst, index=False, float_format="%.6f")
    _record("creditcard_fraud", dst, n_full,
            f"fraud rate {n_fraud/target_rows:.4%} vs {len(fraud)/n_full:.4%} in the full "
            f"file; {n_fraud} fraud rows; V1-V28 and Amount rounded to 6 dp")


# --------------------------------------------------------------------------------------
# montgomery_911_calls - chronological file. One key, evenly spread, so the sample spans
# the same first-call-to-last-call window and keeps the hour-of-day and category mix.
# --------------------------------------------------------------------------------------
def build_911(target_rows: int = 25_000) -> None:
    src = RAW / "montgomery_911_calls.csv"
    print(f"montgomery_911_calls: scanning {src.stat().st_size/1e6:.0f} MB ...")
    dst = SAMPLES / "montgomery_911_calls.sample.csv"
    counts, kept, n_full = stratified_line_sample(
        src, dst, key_fn=lambda f: "all", quota_fn=lambda k, n, N: target_rows)
    s = pd.read_csv(dst, low_memory=False)
    ts = pd.to_datetime(s["timeStamp"], errors="coerce")
    _record("montgomery_911_calls", dst, n_full,
            f"1 row in every {n_full/max(1,sum(kept.values())):.0f}, evenly spread; "
            f"covers {ts.min():%Y-%m-%d} to {ts.max():%Y-%m-%d} - the same window as the "
            f"full file; {s['title'].nunique()} distinct call types, "
            f"{s['twp'].nunique()} townships")


# --------------------------------------------------------------------------------------
# border_crossing_data - seasonality is the phenomenon, so sample inside each
# (month, crossing-type) group. Every month and every Measure in the full file survives.
# --------------------------------------------------------------------------------------
def build_border(target_rows: int = 44_000) -> None:
    src = RAW / "border_crossing_data.csv"
    print(f"border_crossing_data: scanning {src.stat().st_size/1e6:.0f} MB ...")
    dst = SAMPLES / "border_crossing_data.sample.csv"
    counts, kept, n_full = stratified_line_sample(
        src, dst,
        key_fn=lambda f: (f[4], f[5]),                      # (Date, Measure)
        quota_fn=lambda k, n, N: max(1, round(n * target_rows / N)))
    s = pd.read_csv(dst)
    full_months = len({k[0] for k in counts})
    _record("border_crossing_data", dst, n_full,
            f"stratified by (month, crossing type), at least 1 row per group; "
            f"{s['Date'].nunique()}/{full_months} months and "
            f"{s['Measure'].nunique()}/{len({k[1] for k in counts})} crossing types kept; "
            f"'Value' totals are roughly {sum(kept.values())/n_full:.0%} of the real totals")


# --------------------------------------------------------------------------------------
# cicids2017 - 675 MB. Stratify by the Label column so the attack mix survives, with a
# floor so the rare attack classes (Heartbleed has 11 rows in 2.3 M) do not disappear.
# --------------------------------------------------------------------------------------
def build_cicids(target_rows: int = 14_000, min_per_label: int = 5) -> None:
    src = RAW / "cicids2017.csv"
    print(f"cicids2017: scanning {src.stat().st_size/1e6:.0f} MB ...")
    dst = SAMPLES / "cicids2017.sample.csv"
    counts, kept, n_full = stratified_line_sample(
        src, dst,
        key_fn=lambda f: f[-1].strip(),                     # ' Label' is the last column
        quota_fn=lambda k, n, N: max(min_per_label, round(n * target_rows / N)))
    mix = "; ".join(f"{k} {kept[k]}/{n:,}" for k, n in counts.most_common())
    _record("cicids2017", dst, n_full,
            f"stratified by Label, at least {min_per_label} rows per class -> {mix}")


# --------------------------------------------------------------------------------------
# unsw_nb15 - 586 MB and NO header row. Stratify by attack_cat (column 47): the labelled
# attacks are a ~13% minority and a plain stride would leave the rare ones with 2 rows.
# --------------------------------------------------------------------------------------
def build_unsw(target_rows: int = 20_000, min_per_label: int = 40) -> None:
    src = RAW / "unsw_nb15.csv"
    print(f"unsw_nb15: scanning {src.stat().st_size/1e6:.0f} MB ...")
    dst = SAMPLES / "unsw_nb15.sample.csv"

    def cat(f):
        v = f[47].strip() if len(f) > 47 else ""
        return v or "(unlabelled)"

    counts, kept, n_full = stratified_line_sample(
        src, dst, key_fn=cat,
        quota_fn=lambda k, n, N: max(min_per_label, round(n * target_rows / N)),
        has_header=False)                                   # the full file has no header
    mix = "; ".join(f"{k} {kept[k]}/{n:,}" for k, n in counts.most_common())
    _record("unsw_nb15", dst, n_full,
            f"headerless, exactly like the full file; stratified by attack_cat, "
            f"at least {min_per_label} rows per class -> {mix}")


BUILDERS = {
    "creditcard_fraud": build_creditcard,
    "montgomery_911_calls": build_911,
    "border_crossing_data": build_border,
    "cicids2017": build_cicids,
    "unsw_nb15": build_unsw,
}

if __name__ == "__main__":
    for key in (sys.argv[1:] or list(BUILDERS)):
        if key not in BUILDERS:
            print(f"unknown dataset: {key}")
        elif not (RAW / f"{key}.csv").exists():
            print(f"{key}: full file not present in {RAW} - skipped")
        else:
            BUILDERS[key]()
    out = SAMPLES / "_build_report.json"
    prev = json.loads(out.read_text()) if out.exists() else {}
    prev.update(report)
    out.write_text(json.dumps(prev, indent=2) + "\n")
    print(f"\nwrote {out}")
