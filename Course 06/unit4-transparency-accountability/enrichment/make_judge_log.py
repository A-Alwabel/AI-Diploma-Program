#!/usr/bin/env python3
"""Generate the bundled judge-score artifacts used by E13_llm_as_a_judge_disagreement.ipynb.

READ THIS BEFORE YOU TRUST A NUMBER IN judge_log.csv
====================================================
The three "judges" in this file are NOT language models. Nothing in this script calls a model, an API
or a network. It is a **simulator**: each judge is three numbers (a first-position bonus, a leniency
offset, and a noise level) applied to a latent quality score, then rounded to an integer 1-5.

That is deliberate, and it is the point of the lesson rather than a shortcut around it. With a real
judge log you can measure position bias but you can never check your measurement, because nobody knows
the true value. Here the true value is written down in `generator_parameters.csv`, so the notebook can
ask the only question that matters about an evaluation method: **does it recover the answer we already
know?**

Consequences you must respect:
  * No number produced by this script is evidence about any real model, vendor or judge configuration.
    Do not quote them as such. For measured magnitudes from real judges, read the papers cited in the
    notebook's references (arXiv:2306.05685, arXiv:2509.21117).
  * The magnitudes below were chosen by hand to make three distinct failure modes visible in 120 items.
    They are not calibrated to any published measurement.

Run it with:  python make_judge_log.py
Outputs (all written next to this script, and all checked into the repository):
  items.csv                 - 120 response pairs: latent quality, true preference, one human label
  judge_log.csv             - 1440 rows: 120 items x 3 judges x 2 presentation orders x 2 passes
  generator_parameters.csv  - the true per-judge parameters the notebook tries to recover
"""
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
SEED = 20260829          # fixed: re-running this script reproduces the checked-in files byte for byte
N_ITEMS = 120
TIE_MARGIN = 0.25        # latent quality gap below which the two responses are genuinely equivalent
HUMAN_ERROR_RATE = 0.08  # human annotators disagree with the latent truth this often

# The three judge configurations. Each one is a caricature of a documented failure mode:
#   judge_A - a strong first-position preference, otherwise a careful scorer
#   judge_B - almost no position preference, but very noisy: it disagrees with itself
#   judge_C - lenient (marks everything high, which compresses the scale) with a mild position bias
JUDGES = {
    "judge_A": {"first_position_bonus": 0.50, "leniency": 0.30, "score_noise_sd": 0.15},
    "judge_B": {"first_position_bonus": 0.08, "leniency": -0.20, "score_noise_sd": 0.40},
    "judge_C": {"first_position_bonus": 0.30, "leniency": 0.60, "score_noise_sd": 0.10},
}


def preference(q_r1: float, q_r2: float, margin: float = TIE_MARGIN) -> str:
    """R1, R2 or tie, from a latent quality gap."""
    if q_r1 - q_r2 > margin:
        return "R1"
    if q_r2 - q_r1 > margin:
        return "R2"
    return "tie"


def main() -> None:
    rng = np.random.default_rng(SEED)

    # --- the items -----------------------------------------------------------------------------
    # Two candidate responses per question, on a latent 1-5 quality scale. R1 is given a small real
    # edge (-0.30 on R2) so that "which response is better?" has a true answer that is not 50/50.
    q_r1 = rng.uniform(1.5, 4.5, N_ITEMS)
    q_r2 = np.clip(q_r1 - 0.30 + rng.normal(0.0, 1.5, N_ITEMS), 1.0, 5.0)

    items = pd.DataFrame({
        "item_id": [f"Q{i + 1:03d}" for i in range(N_ITEMS)],
        "latent_quality_r1": q_r1.round(3),
        "latent_quality_r2": q_r2.round(3),
    })
    items["true_preference"] = [preference(a, b) for a, b in zip(q_r1, q_r2)]

    # A human annotator: right most of the time, wrong HUMAN_ERROR_RATE of the time. Ties stay ties,
    # because an annotator who calls two responses equivalent is not making an error.
    flip = rng.random(N_ITEMS) < HUMAN_ERROR_RATE
    swap = {"R1": "R2", "R2": "R1", "tie": "tie"}
    items["human_label"] = [swap[p] if f and p != "tie" else p
                            for p, f in zip(items["true_preference"], flip)]

    # --- the judge log -------------------------------------------------------------------------
    # Every judge sees every item twice in each presentation order. Independent noise is drawn on
    # every pass, which is where self-inconsistency comes from: no separate "inconsistency" knob is
    # needed, it falls out of noise plus rounding to an integer score.
    rows = []
    for judge, cfg in JUDGES.items():
        for i, row in items.iterrows():
            for order in ("AB", "BA"):
                # "AB" = R1 shown first; "BA" = R2 shown first.
                q_first, q_second = ((row.latent_quality_r1, row.latent_quality_r2) if order == "AB"
                                     else (row.latent_quality_r2, row.latent_quality_r1))
                for pass_no in (1, 2):
                    raw_first = (q_first + cfg["leniency"] + cfg["first_position_bonus"]
                                 + rng.normal(0.0, cfg["score_noise_sd"]))
                    raw_second = (q_second + cfg["leniency"]
                                  + rng.normal(0.0, cfg["score_noise_sd"]))
                    rows.append({
                        "item_id": row.item_id,
                        "judge": judge,
                        "presentation_order": order,
                        "pass": pass_no,
                        "score_first": int(np.clip(round(raw_first), 1, 5)),
                        "score_second": int(np.clip(round(raw_second), 1, 5)),
                    })
    log = pd.DataFrame(rows)

    params = (pd.DataFrame(JUDGES).T.rename_axis("judge").reset_index()
              .assign(note="TRUE simulator settings - the notebook tries to recover these"))

    items.to_csv(HERE / "items.csv", index=False)
    log.to_csv(HERE / "judge_log.csv", index=False)
    params.to_csv(HERE / "generator_parameters.csv", index=False)

    print(f"items.csv                {len(items):4d} rows")
    print(f"judge_log.csv            {len(log):4d} rows "
          f"({N_ITEMS} items x {len(JUDGES)} judges x 2 orders x 2 passes)")
    print(f"generator_parameters.csv {len(params):4d} rows")
    print("\nTrue R1 win rate over decisive items: "
          f"{(items.loc[items.true_preference != 'tie', 'true_preference'] == 'R1').mean():.1%}")


if __name__ == "__main__":
    main()
