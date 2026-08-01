import argparse
import logging
from pathlib import Path

from dataset_analyzer.analyzer import analyze_data, load_csv
from dataset_analyzer.logging_config import setup_logging
from dataset_analyzer.reporter import save_report
from dataset_analyzer.config import load_config


def parse_args():

    parser = argparse.ArgumentParser(
        description="Analyze CSV datasets"
    )

    parser.add_argument(
        "--input",
        type=str,
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--output",
        type=str,
        help="Path to output JSON report"
    )

    return parser.parse_args()


def main() -> None:

    args = parse_args()

    setup_logging()

    logging.info("Starting dataset analysis")

    config = load_config(
        Path("configs/config.yaml")
    )

    if args.input:
        file_path = Path(args.input)
    else:
        file_path = Path(
            config["data"]["input_file"]
        )

    if args.output:
        output_path = Path(args.output)
    else:
        output_path = Path(
            config["output"]["report_file"]
        )

    if not file_path.exists():
        logging.error(
            f"Input file does not exist: {file_path}"
        )
        print(
            f"Error: Input file does not exist: {file_path}"
        )
        return

    logging.info("Loading CSV file")

    data = load_csv(file_path)

    logging.info(
        f"Dataset loaded: {len(data)} rows"
    )

    report = analyze_data(data)

    logging.info("Analysis completed")

    save_report(report, output_path)

    logging.info("Report saved")

    print("Report saved!")


if __name__ == "__main__":
    main()