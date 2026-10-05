import json
from pathlib import Path

from dataset_analyzer.models import AnalysisReport


def save_report(
    report: AnalysisReport,
    output_path: Path
) -> None:

    report_dict = {
        "rows": report.rows,
        "columns": report.columns,
        "missing_values": report.missing_values,
        "numeric_summary": report.numeric_summary
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as file:
        json.dump(
            report_dict,
            file,
            indent=4,
            allow_nan=False
        )
