import argparse
import logging
import sys
from pathlib import Path

import pandas as pd
import yaml

from dataset_analyzer.analyzer import analyze_data, load_csv
from dataset_analyzer.config import load_config
from dataset_analyzer.logging_config import setup_logging
from dataset_analyzer.reporter import save_report


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Analyze CSV datasets")
    parser.add_argument("--input", type=Path, help="Path to input CSV file")
    parser.add_argument("--output", type=Path, help="Path to output JSON report")
    parser.add_argument("--config", type=Path, help="Optional YAML configuration file")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        config_path = args.config
        default_config = Path("configs/config.yaml")
        if config_path is None and default_config.is_file():
            config_path = default_config
        config = load_config(config_path) if config_path else {}
        base = config_path.resolve().parent if config_path else Path.cwd()
        file_path = args.input
        if file_path is None and config:
            file_path = base / config["data"]["input_file"]
        if file_path is None:
            raise ValueError("Provide --input or --config (no local configs/config.yaml found)")
        output_path = args.output or (
            base / config["output"]["report_file"] if config else Path("reports/report.json")
        )
        setup_logging(base / config.get("logging", {}).get("log_file", "logs/app.log"))
        if not file_path.is_file():
            raise FileNotFoundError(f"Input file does not exist: {file_path}")
        logging.info("Loading CSV file: %s", file_path)
        report = analyze_data(load_csv(file_path))
        save_report(report, output_path)
        logging.info("Report saved to %s", output_path)
        print(f"Report saved: {output_path}")
        return 0
    except (OSError, ValueError, yaml.YAMLError, pd.errors.ParserError) as exc:
        logging.error("Analysis failed: %s", exc)
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
