from pathlib import Path

from dataset_analyzer.analyzer import load_csv


def main() -> None:
    file_path = Path("data/sample.csv")

    data = load_csv(file_path)

    print(data)


if __name__ == "__main__":
    main()