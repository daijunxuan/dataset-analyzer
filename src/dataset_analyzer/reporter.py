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
        "missing_values": report.missing_values
    }

    with open(output_path, "w") as file:
        json.dump(
            report_dict,
            file,
            indent=4
        )