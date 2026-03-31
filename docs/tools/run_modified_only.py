#!/usr/bin/env python3
"""Execute only the notebooks we recently modified (syntax fixes)."""

import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent.parent
OUT = BASE / "artifacts" / "execution_modified_report.json"
TIMEOUT = 90

# Notebooks we modified in the syntax-fix commit
MODIFIED = [
    "Course 03/unit2-calculus/examples/04_backpropagation_neural_networks.ipynb",
    "Course 04/unit1-data-processing/examples/05_polynomial_regression.ipynb",
    "Course 04/unit2-regression/examples/01_ridge_lasso_regression.ipynb",
    "Course 04/unit3-classification/examples/01_logistic_regression.ipynb",
    "Course 04/unit3-classification/examples/03_svm.ipynb",
    "Course 07/unit1-nlp-fundamentals/exercises/01_text_preprocessing_exercise.ipynb",
    "Course 07/unit2-tokenization-morphology/examples/04_word_embeddings_glove_fasttext.ipynb",
    "Course 07/unit5-applications-ethics/exercises/01_nlp_applications_ethics_exercise.ipynb",
    "Course 08/unit3-rnns-transformers/examples/03_gpt_text_generation.ipynb",
    "Course 08/unit3-rnns-transformers/exercises/01_rnn_exercise.ipynb",
    "Course 09/unit1-rl-fundamentals/examples/mini_projects_applying_rl_in_games_like_cartpole_and_frozenlake_implementing_q_l.ipynb",
    "Course 09/unit1-rl-fundamentals/examples/setting_up_rl_environment_installing_openai_gym_and_using_python_based_framework.ipynb",
    "Course 09/unit2-policy-value/examples/applying_q_learning_and_sarsa_in_openai_gym_cartpole_frozenlake.ipynb",
    "Course 09/unit2-policy-value/examples/running_td0_and_n_step_td_algorithms_in_simple_rl_environments.ipynb",
    "Course 09/unit3-deep-rl/examples/02_actor_critic.ipynb",
    "Course 09/unit4-exploration-exploitation/exercises/02_exploration_exercise.ipynb",
    "Course 09/unit5-applications/examples/02_game_playing_agent.ipynb",
    "Course 09/unit5-applications/examples/implementing_multi_agent_rl_environments_and_training_cooperativecompetitive_age.ipynb",
    "Course 10/unit2-text-generation/examples/05_fine_tuning_language_models.ipynb",
    "Course 10/unit2-text-generation/examples/05_finetuning_language_models.ipynb",
    "Course 10/unit3-image-generation/examples/03_vae_advanced_topics.ipynb",
    "Course 10/unit3-image-generation/exercises/01_vae_exercise.ipynb",
    "Course 10/unit5-future-trends/examples/03_music_generation.ipynb",
]


def run_one(rel_path):
    nb_path = BASE / rel_path
    if not nb_path.exists():
        return {"path": rel_path, "status": "skipped", "error": "file not found"}
    res = {"path": rel_path, "status": "unknown", "error": None}
    out_dir = BASE / "artifacts" / "executed_modified" / Path(rel_path).parent
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        proc = subprocess.run(
            [sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook",
             "--execute", f"--ExecutePreprocessor.timeout={TIMEOUT}", str(nb_path),
             "--output-dir", str(out_dir)],
            capture_output=True, text=True, timeout=TIMEOUT + 15, cwd=str(BASE),
        )
        res["status"] = "passed" if proc.returncode == 0 else "failed"
        if proc.returncode != 0:
            err = (proc.stderr or proc.stdout or "")[:3000]
            res["error"] = err
    except subprocess.TimeoutExpired:
        res["status"] = "failed"
        res["error"] = "Timeout"
    except Exception as e:
        res["status"] = "failed"
        res["error"] = str(e)[:3000]
    return res


def main():
    print(f"Executing {len(MODIFIED)} modified notebooks (timeout={TIMEOUT}s)...")
    results = []
    for i, rel in enumerate(MODIFIED, 1):
        print(f"  [{i}/{len(MODIFIED)}] {rel[:65]}...")
        r = run_one(rel)
        results.append(r)
        if r["status"] == "failed":
            print(f"    FAILED")

    out_data = {
        "total": len(results),
        "passed": sum(1 for r in results if r["status"] == "passed"),
        "failed": sum(1 for r in results if r["status"] == "failed"),
        "skipped": sum(1 for r in results if r["status"] == "skipped"),
        "results": results,
        "timestamp": datetime.now().isoformat(),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out_data, f, indent=2, ensure_ascii=False)
    print(f"\nReport: {OUT}")
    print(f"Passed: {out_data['passed']}, Failed: {out_data['failed']}, Skipped: {out_data['skipped']}")


if __name__ == "__main__":
    main()
