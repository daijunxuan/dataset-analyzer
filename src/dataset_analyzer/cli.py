from pathlib import Path
import logging

from dataset_analyzer.analyzer import analyze_data, load_csv
from dataset_analyzer.logging_config import setup_logging
from dataset_analyzer.reporter import save_report
from dataset_analyzer.config import load_config

def main() -> None:

    setup_logging()

    logging.info("Starting dataset analysis")

    config = load_config(
    Path("configs/config.yaml")
)
    file_path = Path(
    config["data"]["input_file"]
)
    output_path = Path(
    config["output"]["report_file"]
)

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