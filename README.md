# Dataset Analyzer

[![Tests](https://github.com/daijunxuan/dataset-analyzer/actions/workflows/test.yml/badge.svg)](https://github.com/daijunxuan/dataset-analyzer/actions/workflows/test.yml)

A Python CLI for CSV inspection: row and column counts, total missing values, numerical means, logging, and portable JSON reports.

## Quick start

Python 3.11 or newer:

```bash
git clone https://github.com/daijunxuan/dataset-analyzer.git
cd dataset-analyzer
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
dataset-analyzer --input data/sample.csv --output reports/sample.json
pytest -q
```

Once installed, the CLI also works outside the checkout:

```bash
dataset-analyzer --input /path/to/input.csv --output /path/to/results/report.json
```

Output directories are created automatically. Success exits with status 0; invalid configuration, missing input, malformed CSV, or a write failure exits with status 1 and an error on stderr. `--help` lists available options.

## Configuration and path rules

Use `--config /path/to/config.yaml` to select a YAML file. If omitted, `configs/config.yaml` is loaded only when it exists in the current directory. With neither configuration nor `--input`, the CLI explains what is required.

```yaml
data:
  input_file: ../data/sample.csv
output:
  report_file: ../reports/report.json
logging:
  log_file: ../logs/app.log
```

Paths in YAML are relative to the directory containing that YAML file. Explicit `--input` and `--output` override YAML values and are relative to the working directory (absolute paths also work). Without configuration, the default output is `reports/report.json` and the default log is `logs/app.log`, both relative to the working directory.

The checked-in configuration uses `../` because it lives in `configs/`. From the repository root, `dataset-analyzer` runs the sample with those defaults.

## Example

Input:

```csv
name,age,score
Alice,20,90
Bob,21,85
Charlie,22,95
```

Output:

```json
{
  "rows": 3,
  "columns": 3,
  "missing_values": 0,
  "numeric_summary": {"age": 21.0, "score": 90.0}
}
```

`numeric_summary` contains means of numeric columns. All-missing or non-finite means become JSON `null`, never nonstandard `NaN` or `Infinity`. Non-numeric columns do not receive a mean. This tool does not infer a schema or certify dataset quality.

## Implementation and checks

`src/dataset_analyzer/` separates loading/analysis, configuration, reporting, and CLI orchestration. Tests exercise analysis, installation entry points, execution outside the checkout, configuration-relative paths, failures, new output directories, and strict JSON compatibility. GitHub Actions runs them on pushes and pull requests to `main`.

Development dependencies are in `.[dev]`; pytest is not a runtime dependency. Generated logs and reports are ignored. The tracked sample report is an example artifact.

Potential extensions: column-level missingness, medians and standard deviations, additional file formats, and visualization.

## License

MIT; see [LICENSE](LICENSE).
