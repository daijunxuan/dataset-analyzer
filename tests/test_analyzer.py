from pathlib import Path

from dataset_analyzer.analyzer import load_csv, analyze_data


def test_load_csv():

    file_path = Path("data/sample.csv")

    data = load_csv(file_path)

    assert len(data) == 3


def test_analyze_data():

    file_path = Path("data/sample.csv")

    data = load_csv(file_path)

    report = analyze_data(data)

    assert report.rows == 3
    assert report.columns == 3
    assert report.missing_values == 0
    