from dataclasses import dataclass


@dataclass
class AnalysisReport:
    rows: int
    columns: int
    missing_values: int
    numeric_summary: dict