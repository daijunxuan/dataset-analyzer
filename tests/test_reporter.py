import json

import pandas as pd

from dataset_analyzer.analyzer import analyze_data
from dataset_analyzer.reporter import save_report


def test_all_missing_column_produces_portable_json(tmp_path):
    report = analyze_data(pd.DataFrame({"x": [float("nan"), float("nan")]}))
    path = tmp_path / "nested" / "report.json"
    save_report(report, path)
    def reject_constant(value):
        raise AssertionError(f"Nonstandard JSON constant: {value}")
    data = json.loads(path.read_text(), parse_constant=reject_constant)
    assert data["numeric_summary"]["x"] is None
    assert data["missing_values"] == 2
