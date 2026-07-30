from pathlib import Path

from dataset_analyzer.analyzer import analyze_data, load_csv
from dataset_analyzer.reporter import save_report


def main() -> None:

    file_path = Path("data/sample.csv")

    output_path = Path("reports/report.json")

    data = load_csv(file_path)

    report = analyze_data(data)

    save_report(report, output_path)

    print("Report saved!")


if __name__ == "__main__":
    main()