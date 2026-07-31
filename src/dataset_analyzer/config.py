from pathlib import Path
import yaml


def load_config(path: Path) -> dict:
    with open(path, "r") as file:
        return yaml.safe_load(file)