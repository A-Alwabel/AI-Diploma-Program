# Datasets: what ships, what you download, how to load it

All twelve courses share one datasets folder. **You never write a file path.** One line
loads any dataset, from any notebook, on any machine:

```python
df = load("titanic")
```

That works whether you cloned the repository, opened a notebook from a different folder,
or are on Google Colab with no repository at all. It also tells you, out loud, whether it
gave you the full dataset or a sample.

---

## 1. The setup cell

Every notebook that reads a shared dataset starts with this cell. It is already there in
the course notebooks; you only need it if you write your own.

```python
# --- Data setup. Works from any folder, and on Google Colab. -------------------------
# WHAT: find the repository root and put it on sys.path, then import the shared loader.
# WHY:  a hard-coded '../../../Course 04/datasets/raw/titanic.csv' only resolves when the
#       kernel's working directory happens to be this notebook's folder. This does not care.
import sys, pathlib

_here = pathlib.Path.cwd().resolve()
_root = next((p for p in [_here, *_here.parents] if (p / "tools" / "data.py").exists()), None)
if _root is None:                     # Google Colab, or a stray copy of the notebook
    import urllib.request
    pathlib.Path("tools").mkdir(exist_ok=True)
    try:
        urllib.request.urlretrieve(
            "https://raw.githubusercontent.com/A-Alwabel/"
            "AI-Diploma-Program/main/tools/data.py", "tools/data.py")
    except Exception as _e:
        raise RuntimeError(
            "Could not find the AI Diploma repository from this folder, and could not "
            "download the data loader either. Open this notebook inside a clone of "
            "https://github.com/A-Alwabel/AI-Diploma-Program, or connect to the internet "
            f"and re-run this cell. (underlying error: {_e})") from None
    _root = pathlib.Path.cwd()
sys.path.insert(0, str(_root))

from tools.data import load        # load("titanic"), load("creditcard_fraud"), ...
# -------------------------------------------------------------------------------------
```

The same block lives in `tools/notebook_data_setup.py`, ready to copy.

### What else the loader gives you

```python
from tools import data

data.summary()                                   # what is on THIS machine, right now
data.catalog()                                   # the short names load() accepts
data.load("cicids2017", usecols=[" Label"])      # any pandas read_csv keyword passes through
data.load("creditcard_fraud", prefer="sample")   # force the sample: same numbers for everyone
data.path("cicids2017")                          # a Path, for chunked-reading lessons
data.note("creditcard_fraud")                    # the honesty line, as a string
data.is_sample("creditcard_fraud")               # True if a sample was used
```

If a dataset genuinely cannot be found, the error tells you where it looked, where to put
the file, and where to get it. It never fails silently.

---

## 2. What is in the repository

Total data committed: **about 23 MB**. The originals it stands in for total about 1.6 GB,
which is why they are not here.

| `load("...")` | What it is | Full file | In the repo you get | Repo size |
|---|---|---|---|---|
| `titanic` | 891 Titanic passengers, survival label | 891 rows, 0.06 MB | **the whole file** | 60 KB |
| `crime_statistics` | 1,994 communities, Murder/Assault/UrbanPop/Rape | 1,994 rows, 0.06 MB | **the whole file** | 61 KB |
| `crime_statistics_original_50` | The 50 US states of USArrests | 50 rows, 1 KB | **the whole file** | 1.3 KB |
| `crime_statistics_large` | 1,994 communities, four anonymised features | 1,994 rows, 0.04 MB | **the whole file** | 38 KB |
| `creditcard_fraud` | Card transactions, 28 PCA components, fraud label | 284,807 rows, 151 MB | 16,000-row sample | 4.66 MB |
| `montgomery_911_calls` | 911 call log, Montgomery County PA | 663,522 rows, 123 MB | 25,000-row sample | 4.64 MB |
| `border_crossing_data` | Monthly US border crossings by port | 346,733 rows, 37 MB | 43,818-row sample | 4.68 MB |
| `cicids2017` | Labelled network flows, 78 features + attack label | 2,300,825 rows, 708 MB | 14,015-row sample | 4.30 MB |
| `unsw_nb15` | Network flows, 49 columns, attack_cat + label | 2,540,047 rows, 586 MB | 20,148-row sample | 4.64 MB |
| `global_terrorism_database` | 181,691 incidents, 1970-2017 | 181,691 rows, 163 MB | nothing (no lesson reads it) | - |

Samples live in `Course 04/datasets/samples/`. Full files, when you download them, go in
`Course 04/datasets/raw/`. The loader looks in both and prefers the full file.

---

## 3. Every dataset, honestly

### `titanic` - the whole file ships

891 passengers of the RMS Titanic with a survival label. Source: the Data Science Dojo
mirror of the Kaggle *Titanic - Machine Learning from Disaster* training set,
<https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv> - verified
byte-identical to the copy in this repo. Nothing to download.

### `crime_statistics_original_50` - the whole file ships

The classic USArrests table: murder, assault, urban population and rape rates for the 50
US states (McNeil 1977; ships with R). Same values as
<https://raw.githubusercontent.com/selva86/datasets/master/USArrests.csv>; this copy is
unquoted and puts `State` last. This is the crime file with checkable provenance - prefer
it when a lesson needs one.

### `crime_statistics` and `crime_statistics_large` - the whole files ship

1,994 rows each. The row count matches the UCI *Communities and Crime* dataset, while
`crime_statistics` carries USArrests-style column names and `crime_statistics_large`
carries `Feature_1..Feature_4`. **The exact derivation is not recorded in this repository**,
so treat them as teaching tables rather than as citable statistics.

### `creditcard_fraud` - 16,000-row sample ships

Anonymised European card transactions: `Time`, 28 PCA components `V1..V28`, `Amount`, and
`Class` (1 = fraud). Source: Kaggle `mlg-ulb/creditcardfraud` (Worldline and the ULB
Machine Learning Group). A free Kaggle account is needed for the full file.

The whole point of this dataset is the class imbalance, so the sample is drawn to keep it:

- **0.175 % fraud in the sample (28 rows of 16,000) against 0.173 % in the full file.**
- `V1..V28` and `Amount` are rounded to 6 decimal places, purely so the file fits in git.
  Those columns are PCA components with a standard deviation of order 1, so 1e-6 is four
  orders of magnitude below anything a lesson computes.
- Rows keep their original `Time` order.
- Column names and pandas dtypes are identical to the full file.

What changes if you use the sample: with 28 fraud rows a train/test split leaves single
digits of fraud in the test set, so precision and recall move in visible jumps. The lesson
- that accuracy is useless here - is unaffected. Absolute counts are not comparable to
published numbers for this dataset.

### `montgomery_911_calls` - 25,000-row sample ships

Emergency call log for Montgomery County, Pennsylvania. Source: Kaggle
`mchirico/montcoalert`.

The sample keeps **1 row in every 27, evenly spread through the file**, which is in
chronological order. So it covers **2015-12-10 to 2020-07-29 - the same window as the full
file** - with all 100 distinct call types and all 68 townships still present. Every kept
row is a byte-exact copy of the original line.

What changes if you use the sample: daily and hourly *counts* are about 1/27 of the real
counts. Proportions, seasonality, the hour-of-day cycle and the category mix hold.

### `border_crossing_data` - 43,818-row sample ships

Monthly counts of vehicles, pedestrians, containers and passengers entering the US by
port, border and crossing type. Source: US Bureau of Transportation Statistics, via Kaggle
`akhilv11/us-border-crossing-data`.

Seasonality is the phenomenon here, so the sample is stratified **within each (month,
crossing type) group**, at least one row per group: **all 279 months and all 12 crossing
types survive**. Every kept row is a byte-exact copy of the original line.

What changes if you use the sample: a `Value` total is roughly **13 %** of the real total.
The seasonal shape, the port mix and the month coverage hold.

> **Warning about re-downloading this one.** The live BTS file at `data.transportation.gov`
> now uses a *different schema* - `Date` as `"Mar 2026"` instead of
> `"03/01/2019 12:00:00 AM"`, and `Latitude`/`Longitude`/`Point` instead of `Location`. It
> is **not** a drop-in replacement for the file the lessons were written against. Use the
> Kaggle copy.

### `cicids2017` - 14,015-row sample ships

2.3 million labelled network flows, 78 numeric features plus a ` Label` column. Source:
Canadian Institute for Cybersecurity, <https://www.unb.ca/cic/datasets/ids-2017.html>
(registration required); the merged CSV is also mirrored at
<https://huggingface.co/datasets/c01dsnap/CIC-IDS2017>.

The sample is stratified by `Label` with a floor of 5 rows per class, so **all 15 classes
survive** - including Heartbleed, which has 11 rows in the entire 2.3 M-row file. Common
classes keep their proportions (BENIGN 10,607; DoS Hulk 1,406; PortScan 967; DDoS 779);
the four rarest are over-represented by that floor, deliberately, so they exist at all.
Every kept row is a byte-exact copy of the original line.

What changes if you use the sample: the four rarest classes (Heartbleed, Infiltration,
Web Attack Sql Injection, Web Attack XSS) are a larger share of the sample than of the
full file. Everything else keeps its proportion.

### `unsw_nb15` - 20,148-row sample ships

2.5 million network flows, 49 columns, with `attack_cat` and a binary `label`. Source:
UNSW Canberra, <https://research.unsw.edu.au/projects/unsw-nb15-dataset>; on Kaggle as
`mrwellsdavid/unsw-nb15`.

**The CSV has no header row.** `load("unsw_nb15")` supplies the official 49 column names
for you; if you read the file yourself you must pass them, or your columns come back as
`0..48`. The sample is headerless too, exactly like the original.

Stratified by `attack_cat` with a floor of 40 rows per class, so **all ten attack
categories survive** - Worms has 174 rows in the full file. Every kept row is a byte-exact
copy of the original line.

What changes if you use the sample: the rarest attack categories are over-represented by
the floor. The unlabelled majority and the common categories keep their proportions.

### `global_terrorism_database` - nothing ships

181,691 incidents, 1970-2017, 135 columns. Source: START, University of Maryland,
<https://www.start.umd.edu/gtd/>; on Kaggle as `START-UMD/gtd`. Registration required.
**No lesson in this diploma reads it**, so no sample is committed. `load()` knows about it
and will tell you how to get it if you ask for it.

---

## 4. Getting the full files

You do not need them to run any lesson. Get them when you want the real numbers.

Most are on Kaggle, which needs a free account and an API token:

1. Create an account, then go to <https://www.kaggle.com/settings> and click
   **Create New API Token**. That downloads `kaggle.json`.
2. Put it at `~/.kaggle/kaggle.json` (Windows: `C:\Users\<you>\.kaggle\kaggle.json`) and
   `chmod 600 ~/.kaggle/kaggle.json`.
3. `pip install kaggle`, then, from the repository root:

```bash
RAW="Course 04/datasets/raw"
kaggle datasets download -d mlg-ulb/creditcardfraud        -p "$RAW" --unzip
kaggle datasets download -d mchirico/montcoalert           -p "$RAW" --unzip
kaggle datasets download -d akhilv11/us-border-crossing-data -p "$RAW" --unzip
kaggle datasets download -d mrwellsdavid/unsw-nb15         -p "$RAW" --unzip
kaggle datasets download -d START-UMD/gtd                  -p "$RAW" --unzip
```

CIC-IDS2017 is not on Kaggle: register at <https://www.unb.ca/cic/datasets/ids-2017.html>
or take the merged CSV from the Hugging Face mirror above.

Rename each downloaded file to the name in the table in section 2, put it in
`Course 04/datasets/raw/`, and **change nothing else**. The next `load(...)` finds it,
prefers it, and prints `full file, N rows`. Those files are in `.gitignore`, so they will
never be committed by accident.

If your datasets live somewhere else - an external drive, a shared network folder - set
`AI_DIPLOMA_ROOT` to a folder that contains `Course 04/datasets/` and the loader will use
it instead.

---

## 5. The honesty rule

Every call prints one line, and that line is the truth about what was read:

```
titanic: full file, 891 rows.

creditcard_fraud: bundled 16,000-row sample of the 284,807-row original (the full file is
not on this machine) - every number below is for the sample, not the full file. How it was
drawn: stratified so the fraud rate stays 0.175% (28 fraud rows) against 0.173% in the full
file; V1-V28 and Amount rounded to 6 decimals.
```

If you are writing up results, keep that line in the output. `df.attrs["source"]` is
`"full"` or `"sample"`, and `df.attrs["note"]` is the printed line, so you can put the
provenance straight into a figure caption.

If everyone in a class must see identical numbers regardless of who downloaded what, pass
`prefer="sample"`.

---

## 6. For maintainers

- `tools/data.py` - the loader and the catalogue. One entry per dataset; add a dataset by
  adding an entry.
- `tools/build_samples.py` - rebuilds the committed samples from the full files. Run it
  only when a full file changes:
  `python "tools/build_samples.py"` or `python "tools/build_samples.py" cicids2017`.
  Every sampler is deterministic (fixed seed or fixed even-allocation rule), so re-running
  produces byte-identical output and git shows no spurious diff. Every sampler except
  `creditcard_fraud` copies whole *lines* out of the original, so the samples are exact
  subsets; `creditcard_fraud` is the one that rewrites values, and only to round them.
- `Course 04/datasets/samples/_build_report.json` - measured row counts, byte sizes and the
  sampling note for each sample. The numbers in this file and in `tools/data.py` come from
  there, not from estimates.
- `.gitignore` still ignores `*.csv` by default. The samples and the small real files are
  un-ignored by name, so a new multi-hundred-megabyte CSV dropped into `raw/` still cannot
  be committed by accident.
- The older files in this folder (`README.md`, `DOWNLOAD_INSTRUCTIONS.md`,
  `KAGGLE_DOWNLOAD_GUIDE.md`, ...) are download recipes from before the loader existed.
  This file is the one to trust for how data is loaded.
