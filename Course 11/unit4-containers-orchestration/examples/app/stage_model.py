# WHAT: copy YOUR portfolio artifact and its card into app/model/.
# WHY: Docker can only copy files that live inside the build context (the app/
# folder). Your model lives in your home directory, so "staging" it into the
# context is a real build step - in a production pipeline this same step is an
# `aws s3 cp` or `mlflow artifacts download` from a model registry.
"""Stage the AIAT 125 portfolio model into the Docker build context."""
import json
import os
import shutil
from pathlib import Path

PORTFOLIO = Path(os.environ.get("AI_DIPLOMA_PORTFOLIO",
                                str(Path.home() / "ai-diploma-portfolio")))
DEST = Path(__file__).parent / "model"


def stage(portfolio: Path = PORTFOLIO, dest: Path = DEST) -> dict:
    """Copy model_card.json + the artifact it names into dest/. Returns the card."""
    card_path = portfolio / "model_card.json"
    if not card_path.exists():
        raise FileNotFoundError(
            f"No model_card.json in {portfolio}. Export a model first - see "
            "Course 11/PORTFOLIO_MODEL.md - or run any Unit 1 notebook to build "
            "the named fallback."
        )
    card = json.loads(card_path.read_text())
    dest.mkdir(parents=True, exist_ok=True)
    shutil.copy2(card_path, dest / "model_card.json")
    shutil.copy2(portfolio / card["artifact"], dest / card["artifact"])
    return card


if __name__ == "__main__":
    staged = stage()
    print(f"Staged '{staged['name']}' ({staged['artifact']}) into {DEST}")
