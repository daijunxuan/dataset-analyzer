from pathlib import Path

import pandas as pd

from dataset_analyzer.models import AnalysisReport


def load_csv(file_path: Path) -> pd.DataFrame:
    return pd.read_csv(file_path)


def analyze_data(data: pd.DataFrame) -> AnalysisReport:
    return AnalysisReport(
        rows=len(data),
        columns=len(data.columns),
        missing_values=int(data.isnull().sum().sum())
    )