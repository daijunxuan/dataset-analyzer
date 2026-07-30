from pathlib import Path

from dataset_analyzer.analyzer import analyze_data, load_csv


def main() -> None:
    file_path = Path("data/sample.csv")

    data = load_csv(file_path)

    report = analyze_data(data)

    print(report)


if __name__ == "__main__":
    main()