"""One way to load every dataset this diploma uses, from anywhere.

    from tools.data import load
    df = load("titanic")

That works from a notebook at any depth, from the repo root, from VS Code with a
different working directory, and on Google Colab where there is no repo at all.

WHAT it does, in order, for every dataset:

1. Finds the repository root by walking up from this file and from the current working
   directory, so no notebook ever needs `../../../` again.
2. Uses the FULL dataset if it is on disk.
3. Otherwise uses the SAMPLE that ships inside the repository.
4. Otherwise, if there is a network, downloads the sample (or, for the few datasets with
   a stable public URL, the full file) and caches it.
5. Prints ONE line saying exactly which of those happened, so a printed number is never
   silently a sample's number.

If a dataset cannot be found at all, the error message says where it looked, where to put
the file, and where to get it. It never fails silently and never fails vaguely.

Useful extras:

    from tools import data
    data.load("creditcard_fraud", prefer="sample")   # force the sample: same numbers for everyone
    data.path("cicids2017")                          # a Path, for chunked-reading lessons
    data.note("creditcard_fraud")                    # the honesty line, as a string
    data.is_sample("creditcard_fraud")               # True if the last load used a sample
    data.summary()                                   # what is on this machine right now
"""
from __future__ import annotations

import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Optional

import pandas as pd

__all__ = [
    "load", "path", "note", "is_sample", "catalog", "describe", "summary",
    "repo_root", "data_home", "on_colab", "DatasetNotAvailable", "CATALOG",
]

# Raw-file base for this repository on GitHub. Used only when the repo itself is not on
# disk (Google Colab) or when a file is missing. It serves whatever is on `main`, so it
# resolves once the samples are pushed.
GITHUB_RAW = "https://raw.githubusercontent.com/A-Alwabel/AI-Diploma-Program/main/"
RAW_REL = "Course 04/datasets/raw"
SAMPLES_REL = "Course 04/datasets/samples"
_TIMEOUT = 120


class DatasetNotAvailable(FileNotFoundError):
    """Raised when a dataset is neither on disk nor downloadable. The message says what to do."""


# --------------------------------------------------------------------------------------
# Where am I?
# --------------------------------------------------------------------------------------
def on_colab() -> bool:
    """True inside a Google Colab notebook."""
    return "google.colab" in sys.modules


def _is_root(p: Path) -> bool:
    """A directory is the repo root if it holds the shared datasets folder, or all courses."""
    return (p / "Course 04" / "datasets").is_dir() or (
        (p / "Course 01").is_dir() and (p / "Course 12").is_dir()
    )


_ROOT_CACHE: Optional[Path] = None


def repo_root() -> Optional[Path]:
    """The repository root, found from this file or from the working directory. None if absent.

    Set AI_DIPLOMA_ROOT to override, e.g. when the datasets live on an external drive.
    """
    global _ROOT_CACHE
    if _ROOT_CACHE is not None:
        return _ROOT_CACHE
    import os
    env = os.environ.get("AI_DIPLOMA_ROOT")
    starts = []
    if env:
        starts.append(Path(env).expanduser())
    starts.append(Path(__file__).resolve().parent)      # .../repo/tools
    starts.append(Path.cwd().resolve())                 # wherever the kernel started
    for start in starts:
        for p in [start, *start.parents]:
            if _is_root(p):
                _ROOT_CACHE = p
                return p
    return None


def data_home() -> Path:
    """Where files are read from and cached to: the repo if there is one, else a cache dir."""
    root = repo_root()
    if root is not None:
        return root
    home = Path.home() / ".cache" / "ai-diploma-data"
    home.mkdir(parents=True, exist_ok=True)
    return home


def _ensure_importable() -> None:
    """Put the repo root on sys.path so `from tools.data import load` keeps working
    in any later cell, and so sibling helper modules import without configuration."""
    root = repo_root()
    if root is not None and str(root) not in sys.path:
        sys.path.insert(0, str(root))


_ensure_importable()


# --------------------------------------------------------------------------------------
# The catalogue
# --------------------------------------------------------------------------------------
# The official 49 UNSW-NB15 column names. The raw CSV has no header row, so the loader
# supplies them; without this the columns come back as 0..48 and nothing reads sensibly.
UNSW_COLUMNS = [
    "srcip", "sport", "dstip", "dsport", "proto", "state", "dur", "sbytes", "dbytes",
    "sttl", "dttl", "sloss", "dloss", "service", "sload", "dload", "spkts", "dpkts",
    "swin", "dwin", "stcpb", "dtcpb", "smeansz", "dmeansz", "trans_depth", "res_bdy_len",
    "sjit", "djit", "stime", "ltime", "sintpkt", "dintpkt", "tcprtt", "synack", "ackdat",
    "is_sm_ips_ports", "ct_state_ttl", "ct_flw_http_mthd", "is_ftp_login", "ct_ftp_cmd",
    "ct_srv_src", "ct_srv_dst", "ct_dst_ltm", "ct_src_ltm", "ct_src_dport_ltm",
    "ct_dst_sport_ltm", "ct_dst_src_ltm", "attack_cat", "label",
]

# full_rows / sample_rows below were MEASURED from the files, not estimated. See
# Course 04/datasets/samples/_build_report.json, written by tools/build_samples.py.
CATALOG: dict[str, dict[str, Any]] = {
    "titanic": {
        "what": "891 passengers of the RMS Titanic with survival labels.",
        "full": "titanic.csv", "full_rows": 891, "full_mb": 0.06,
        "in_repo": True,                       # small enough to commit whole
        "sample": None, "sample_rows": None,
        "full_url": "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
        "source": "Data Science Dojo mirror of the Kaggle 'Titanic - Machine Learning from "
                  "Disaster' training set (byte-identical to the copy in this repo).",
        "read": {},
    },
    "crime_statistics": {
        "what": "1,994 communities with Murder / Assault / UrbanPop / Rape columns.",
        "full": "crime_statistics.csv", "full_rows": 1994, "full_mb": 0.06,
        "in_repo": True,
        "sample": None, "sample_rows": None,
        "full_url": None,
        "source": "Ships with the repo. The 1,994 rows match the UCI 'Communities and Crime' "
                  "row count while the column names come from R's USArrests; the exact "
                  "derivation is not recorded here. Prefer crime_statistics_original_50 "
                  "when a lesson needs a dataset with checkable provenance.",
        "read": {},
    },
    "crime_statistics_original_50": {
        "what": "The 50 US states of USArrests: murder, assault, urban population, rape.",
        "full": "crime_statistics_original_50.csv", "full_rows": 50, "full_mb": 0.001,
        "in_repo": True,
        "sample": None, "sample_rows": None,
        "full_url": "https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv",
        "source": "USArrests (McNeil 1977, shipped with R). Same values as the selva86 "
                  "mirror; this copy is unquoted and puts State last.",
        "read": {},
    },
    "crime_statistics_large": {
        "what": "1,994 communities with four anonymised numeric features.",
        "full": "crime_statistics_large.csv", "full_rows": 1994, "full_mb": 0.04,
        "in_repo": True,
        "sample": None, "sample_rows": None,
        "full_url": None,
        "source": "Ships with the repo; same 1,994-row basis as crime_statistics, columns "
                  "renamed Feature_1..Feature_4.",
        "read": {},
    },
    "creditcard_fraud": {
        "what": "European card transactions, 28 PCA components + Amount, with a fraud label.",
        "full": "creditcard_fraud.csv", "full_rows": 284_807, "full_mb": 151,
        "in_repo": False,
        "sample": "creditcard_fraud.sample.csv", "sample_rows": 16_000,
        "sample_note": "stratified so the fraud rate stays 0.175% (28 fraud rows) against "
                       "0.173% in the full file; V1-V28 and Amount rounded to 6 decimals",
        "full_url": None,
        "source": "Kaggle mlg-ulb/creditcardfraud (Worldline / ULB Machine Learning Group). "
                  "Requires a free Kaggle account.",
        "get_full": 'kaggle datasets download -d mlg-ulb/creditcardfraud -p "{raw}" --unzip',
        "read": {},
    },
    "montgomery_911_calls": {
        "what": "Emergency (911) call log for Montgomery County, PA, Dec 2015 - Jul 2020.",
        "full": "montgomery_911_calls.csv", "full_rows": 663_522, "full_mb": 123,
        "in_repo": False,
        "sample": "montgomery_911_calls.sample.csv", "sample_rows": 25_000,
        "sample_note": "1 row in every 27, evenly spread, so the sample covers the same "
                       "2015-12-10 to 2020-07-29 window with all 100 call types and 68 townships",
        "full_url": None,
        "source": "Kaggle mchirico/montcoalert. Requires a free Kaggle account.",
        "get_full": 'kaggle datasets download -d mchirico/montcoalert -p "{raw}" --unzip',
        "read": {"low_memory": False},
    },
    "border_crossing_data": {
        "what": "Monthly US border crossing counts by port, border and crossing type, 1996-2019.",
        "full": "border_crossing_data.csv", "full_rows": 346_733, "full_mb": 37,
        "in_repo": False,
        "sample": "border_crossing_data.sample.csv", "sample_rows": 43_818,
        "sample_note": "stratified by (month, crossing type): all 279 months and all 12 "
                       "crossing types survive, so the seasonal shape holds, but a 'Value' "
                       "total is about 13% of the real total",
        "full_url": None,
        "source": "US Bureau of Transportation Statistics border crossing data, via Kaggle "
                  "akhilv11/us-border-crossing-data. WARNING: the live BTS download at "
                  "data.transportation.gov now uses a different schema (Date as 'Mar 2026', "
                  "Latitude/Longitude/Point instead of Location), so it is NOT a drop-in "
                  "replacement for the copy the lessons were written against.",
        "get_full": 'kaggle datasets download -d akhilv11/us-border-crossing-data -p "{raw}" --unzip',
        "read": {},
    },
    "cicids2017": {
        "what": "2.3 M labelled network flows, 78 features plus an attack Label.",
        "full": "cicids2017.csv", "full_rows": 2_300_825, "full_mb": 708,
        "in_repo": False,
        "sample": "cicids2017.sample.csv", "sample_rows": 14_015,
        "sample_note": "stratified by Label with a floor of 5 rows per class, so all 15 "
                       "attack classes survive - including Heartbleed, which has 11 rows "
                       "in the whole 2.3 M-row file",
        "full_url": None,
        "source": "Canadian Institute for Cybersecurity, CIC-IDS2017 "
                  "(https://www.unb.ca/cic/datasets/ids-2017.html). Registration required; "
                  "the single merged CSV is also mirrored at "
                  "https://huggingface.co/datasets/c01dsnap/CIC-IDS2017",
        "read": {"low_memory": False},
    },
    "unsw_nb15": {
        "what": "2.5 M network flows, 49 columns, with attack_cat and a binary label.",
        "full": "unsw_nb15.csv", "full_rows": 2_540_047, "full_mb": 586,
        "in_repo": False,
        "sample": "unsw_nb15.sample.csv", "sample_rows": 20_148,
        "sample_note": "stratified by attack_cat with a floor of 40 rows per class, so all "
                       "ten attack categories survive (Worms has 174 rows in the full file)",
        "full_url": None,
        "source": "UNSW Canberra, UNSW-NB15 "
                  "(https://research.unsw.edu.au/projects/unsw-nb15-dataset), also on Kaggle "
                  "as mrwellsdavid/unsw-nb15. The CSV has NO header row; this loader supplies "
                  "the official 49 column names.",
        "get_full": 'kaggle datasets download -d mrwellsdavid/unsw-nb15 -p "{raw}" --unzip',
        "read": {"header": None, "names": UNSW_COLUMNS, "low_memory": False,
                 "encoding": "utf-8-sig"},
    },
    "global_terrorism_database": {
        "what": "181,691 terrorist incidents, 1970-2017, 135 columns.",
        "full": "global_terrorism_database.csv", "full_rows": 181_691, "full_mb": 163,
        "in_repo": False,
        "sample": None, "sample_rows": None,      # no lesson reads it, so no sample is shipped
        "full_url": None,
        "source": "START, University of Maryland (https://www.start.umd.edu/gtd/), also on "
                  "Kaggle as START-UMD/gtd. Registration required. No lesson in this diploma "
                  "reads it, so no sample ships in the repo.",
        "get_full": 'kaggle datasets download -d START-UMD/gtd -p "{raw}" --unzip',
        "read": {"low_memory": False, "encoding": "latin-1"},
    },
}

_LAST_KIND: dict[str, str] = {}     # name -> "full" | "sample", set by the last load/path


# --------------------------------------------------------------------------------------
# Finding, downloading, reporting
# --------------------------------------------------------------------------------------
def _entry(name: str) -> dict[str, Any]:
    if name not in CATALOG:
        import difflib
        close = ([k for k in CATALOG if name.lower() in k or k in name.lower()]
                 or difflib.get_close_matches(name.lower(), CATALOG, n=1, cutoff=0.6))
        hint = f" Did you mean {close[0]!r}?" if close else ""
        raise KeyError(
            f"Unknown dataset {name!r}.{hint}\n"
            f"Known datasets: {', '.join(sorted(CATALOG))}\n"
            f"See Course 04/datasets/DATA.md."
        )
    return CATALOG[name]


def _local_paths(name: str) -> tuple[Path, Optional[Path]]:
    """(full path, sample path) under the repo, or under the cache when there is no repo."""
    e = _entry(name)
    home = data_home()
    if repo_root() is not None:
        raw_dir, samp_dir = home / RAW_REL, home / SAMPLES_REL
    else:
        raw_dir, samp_dir = home / "raw", home / "samples"
    sample = samp_dir / e["sample"] if e["sample"] else None
    return raw_dir / e["full"], sample


def _download(url: str, dest: Path) -> bool:
    """Fetch `url` into `dest`. Returns False (quietly) if there is no network or no file."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_name(dest.name + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": "ai-diploma-loader"})
    try:
        with urllib.request.urlopen(req, timeout=_TIMEOUT) as r, part.open("wb") as out:
            while chunk := r.read(1 << 20):
                out.write(chunk)
    except (urllib.error.URLError, urllib.error.HTTPError, OSError, TimeoutError):
        part.unlink(missing_ok=True)
        return False
    part.replace(dest)
    return True


def _github_url(rel: str) -> str:
    """Raw-file URL for a repo-relative path. 'Course 04' contains a space, so quote it."""
    return GITHUB_RAW + urllib.parse.quote(rel)


def _unavailable(name: str) -> DatasetNotAvailable:
    e = _entry(name)
    full_p, sample_p = _local_paths(name)
    raw_dir = full_p.parent
    lines = [
        f"Dataset {name!r} is not available on this machine.",
        "",
        f"  What it is : {e['what']}",
        f"  Looked for : {full_p}",
    ]
    if sample_p is not None:
        lines.append(f"               {sample_p}")
    options = []
    step = f"Put the full file at: {full_p}"
    if e.get("get_full"):
        step += f"\n       e.g.  {e['get_full'].format(raw=raw_dir)}"
    options.append(step)
    if e["sample"]:
        options.append(
            f"Or download the {e['sample_rows']:,}-row sample that ships with the repo:\n"
            f"       curl -L -o \"{sample_p}\" \"{_github_url(SAMPLES_REL + '/' + e['sample'])}\""
        )
        options.append(
            "Or clone the repository, which already contains that sample:\n"
            "       git clone --depth 1 https://github.com/A-Alwabel/AI-Diploma-Program.git"
        )
    lines += ["", "  To fix it, do ONE of these:"]
    lines += [f"    {i}. {o}" for i, o in enumerate(options, 1)]
    lines += [
        "",
        f"  Original source: {e['source']}",
        "",
        f"  Then re-run:  load({name!r})",
    ]
    return DatasetNotAvailable("\n".join(lines))


def _resolve(name: str, prefer: str) -> tuple[Path, str, bool]:
    """Return (path, kind, downloaded). kind is 'full' or 'sample'."""
    e = _entry(name)
    full_p, sample_p = _local_paths(name)

    if prefer in ("auto", "full") and full_p.exists():
        return full_p, "full", False
    if prefer in ("auto", "sample") and sample_p is not None and sample_p.exists():
        return sample_p, "sample", False

    # Nothing on disk. Try the network, cheapest useful thing first.
    if prefer in ("auto", "full") and e.get("full_url"):
        if _download(e["full_url"], full_p):
            return full_p, "full", True
    if prefer in ("auto", "sample") and e["sample"] and sample_p is not None:
        if _download(_github_url(SAMPLES_REL + "/" + e["sample"]), sample_p):
            return sample_p, "sample", True
    if e.get("in_repo") and prefer in ("auto", "sample", "full"):
        # small file that is committed whole: fetch it from the repo on GitHub
        if _download(_github_url(RAW_REL + "/" + e["full"]), full_p):
            return full_p, "full", True
    if prefer == "sample" and full_p.exists():
        return full_p, "full", False            # asked for the sample, only the full file is here
    raise _unavailable(name)


def _line(name: str, p: Path, kind: str, rows: Optional[int], downloaded: bool) -> str:
    """The single honest line printed on every load. It must never overstate what was read."""
    e = _entry(name)
    got = " (downloaded just now)" if downloaded else ""
    if kind == "full":
        n = f"{rows:,}" if rows is not None else f"{e['full_rows']:,}"
        return f"{name}: full file, {n} rows{got}."
    n = f"{rows:,}" if rows is not None else f"{e['sample_rows']:,}"
    full_p, _ = _local_paths(name)
    why = ("the full file is on this machine but was not used, because prefer='sample'"
           if full_p.exists() else "the full file is not on this machine")
    detail = f" How it was drawn: {e['sample_note']}." if e.get("sample_note") else ""
    return (f"{name}: bundled {n}-row sample{got} of the {e['full_rows']:,}-row original "
            f"({why}) — every number below is for the sample, not the full file."
            f"{detail}")


# --------------------------------------------------------------------------------------
# Public API
# --------------------------------------------------------------------------------------
def path(name: str, *, prefer: str = "auto", quiet: bool = False) -> Path:
    """Path to the best available copy of `name`, downloading it if it is missing.

    Use this for lessons that read a file in chunks instead of loading it whole.
    """
    p, kind, downloaded = _resolve(name, prefer)
    _LAST_KIND[name] = kind
    if not quiet:
        print(_line(name, p, kind, None, downloaded))
    return p


def load(name: str, *, prefer: str = "auto", quiet: bool = False, **read_kwargs) -> pd.DataFrame:
    """Load a dataset by short name and say honestly which copy was used.

        df = load("titanic")
        df = load("creditcard_fraud", prefer="sample")     # same numbers for everyone
        df = load("cicids2017", usecols=[" Label"])        # any read_csv keyword works

    `prefer`: "auto" (full file if present, else the bundled sample), "full", or "sample".
    Returns a DataFrame; `df.attrs` records "dataset", "source" ("full"/"sample"),
    "path" and "note", so a notebook can print the provenance next to its results.
    """
    p, kind, downloaded = _resolve(name, prefer)
    e = _entry(name)
    kwargs = {**e["read"], **read_kwargs}
    df = pd.read_csv(p, **kwargs)
    _LAST_KIND[name] = kind
    line = _line(name, p, kind, len(df), downloaded)
    if not quiet:
        print(line)
    df.attrs.update({"dataset": name, "source": kind, "path": str(p), "note": line})
    return df


def note(name: str, *, prefer: str = "auto") -> str:
    """The same honest line `load` prints, as a string - handy for figure captions."""
    p, kind, downloaded = _resolve(name, prefer)
    return _line(name, p, kind, None, downloaded)


def is_sample(name: str) -> bool:
    """True if the copy this session used (or would use) is a sample rather than the full file."""
    if name not in _LAST_KIND:
        try:
            _, kind, _ = _resolve(name, "auto")
        except DatasetNotAvailable:
            return False
        _LAST_KIND[name] = kind
    return _LAST_KIND[name] == "sample"


def describe(name: str) -> dict[str, Any]:
    """Everything the catalogue knows about one dataset, plus where it is on this machine."""
    e = dict(_entry(name))
    full_p, sample_p = _local_paths(name)
    e.update({"full_path": str(full_p), "full_present": full_p.exists(),
              "sample_path": str(sample_p) if sample_p else None,
              "sample_present": bool(sample_p and sample_p.exists())})
    return e


def catalog() -> list[str]:
    """The short names `load` accepts."""
    return sorted(CATALOG)


def summary() -> None:
    """Print what is on this machine right now. Good as a first 'is my setup OK?' cell."""
    root = repo_root()
    print(f"repo root : {root if root else 'not found - running outside the repository'}")
    print(f"data home : {data_home()}")
    print(f"colab     : {on_colab()}")
    print(f"{'dataset':<30} {'full file':<12} {'sample':<12} what you would get")
    print("-" * 96)
    for name in catalog():
        d = describe(name)
        full = "on disk" if d["full_present"] else "-"
        samp = "on disk" if d["sample_present"] else ("-" if d["sample"] else "n/a")
        if d["full_present"]:
            got = f"full file, {d['full_rows']:,} rows"
        elif d["sample_present"]:
            got = f"sample, {d['sample_rows']:,} rows"
        elif d["sample"] or d.get("full_url") or d.get("in_repo"):
            got = "download on first use (needs a network)"
        else:
            got = "nothing - see DATA.md"
        print(f"{name:<30} {full:<12} {samp:<12} {got}")
