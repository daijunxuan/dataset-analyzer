from pathlib import Path
import yaml


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as file:
        config = yaml.safe_load(file)
    if not isinstance(config, dict):
        raise ValueError("Configuration must be a YAML mapping")
    for section, key in (("data", "input_file"), ("output", "report_file")):
        value = config.get(section)
        if not isinstance(value, dict) or not isinstance(value.get(key), str):
            raise ValueError(f"Configuration requires {section}.{key} as a path string")
    logging = config.get("logging", {})
    if not isinstance(logging, dict) or not isinstance(logging.get("log_file", "logs/app.log"), str):
        raise ValueError("logging.log_file must be a path string")
    return config
