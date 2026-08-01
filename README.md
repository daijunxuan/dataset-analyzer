# Dataset Analyzer

[![Tests](https://github.com/daijunxuan/dataset-analyzer/actions/workflows/test.yml/badge.svg)](https://github.com/daijunxuan/dataset-analyzer/actions/workflows/test.yml)

A production-style Python command-line tool for automated CSV dataset analysis, with configurable input and output paths, logging, automated testing, and JSON report generation.

## Features

- Load and analyze CSV datasets
- Count dataset rows and columns
- Detect and count missing values
- Calculate numerical column summaries
- Export analysis results as JSON
- Accept custom input and output paths through CLI arguments
- Use YAML-based configuration management
- Record application activity through logging
- Run automated tests with pytest
- Run continuous integration tests with GitHub Actions

## Project Structure

```text
dataset-analyzer/
├── .github/
│   └── workflows/
│       └── test.yml
├── configs/
│   └── config.yaml
├── data/
│   └── sample.csv
├── logs/
│   └── app.log
├── reports/
│   └── report.json
├── src/
│   └── dataset_analyzer/
│       ├── __init__.py
│       ├── analyzer.py
│       ├── cli.py
│       ├── config.py
│       ├── logging_config.py
│       ├── models.py
│       └── reporter.py
├── tests/
│   ├── test_analyzer.py
│   └── test_cli.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Requirements

- Python 3.11 or later
- pandas
- PyYAML
- pytest

The required dependencies are declared in `pyproject.toml` and are installed automatically with the project.

## Installation

Clone the repository:

```bash
git clone https://github.com/daijunxuan/dataset-analyzer.git
```

Enter the project directory:

```bash
cd dataset-analyzer
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```bash
source .venv/bin/activate
```

Install the project and its dependencies:

```bash
python -m pip install -e .
```

The `-e` option installs the package in editable mode, so changes made inside the `src/` directory are immediately available without reinstalling the project.

## Usage

### Display help

```bash
dataset-analyzer --help
```

Example output:

```text
usage: dataset-analyzer [-h] [--input INPUT] [--output OUTPUT]

Analyze CSV datasets

options:
  -h, --help       show this help message and exit
  --input INPUT    Path to input CSV file
  --output OUTPUT  Path to output JSON report
```

### Analyze a CSV file

```bash
dataset-analyzer --input data/sample.csv
```

The report will be saved to the default path configured in:

```text
configs/config.yaml
```

### Specify a custom output path

```bash
dataset-analyzer \
  --input data/sample.csv \
  --output reports/custom-report.json
```

### Run with configuration defaults

```bash
dataset-analyzer
```

When command-line arguments are not provided, the application reads the input and output paths from `configs/config.yaml`.

## Configuration

The default configuration is stored in:

```text
configs/config.yaml
```

Example configuration:

```yaml
data:
  input_file: data/sample.csv

output:
  report_file: reports/report.json

logging:
  log_file: logs/app.log
```

Command-line arguments take priority over values in the configuration file.

For example:

```bash
dataset-analyzer --input data/another-dataset.csv
```

uses `data/another-dataset.csv` instead of the input path defined in `config.yaml`.

## Example Input

The example CSV file is located at:

```text
data/sample.csv
```

Example:

```csv
name,age,score
Alice,20,90
Bob,21,85
Charlie,22,95
```

## Example Report

After running the analyzer, the generated JSON report may look like this:

```json
{
    "rows": 3,
    "columns": 3,
    "missing_values": 0,
    "numeric_summary": {
        "age": 21.0,
        "score": 90.0
    }
}
```

The report contains:

- Total number of rows
- Total number of columns
- Total number of missing values
- Mean values for numerical columns

## Logging

The application records its execution process in:

```text
logs/app.log
```

Example log entries:

```text
2026-08-01 18:00:00 INFO Starting dataset analysis
2026-08-01 18:00:00 INFO Loading CSV file
2026-08-01 18:00:00 INFO Dataset loaded: 3 rows
2026-08-01 18:00:00 INFO Analysis completed
2026-08-01 18:00:00 INFO Report saved
```

Log files are generated locally and are excluded from Git version control.

## Testing

Run all tests with:

```bash
pytest
```

The current test suite checks:

- CSV loading
- Dataset row and column counts
- Missing-value analysis
- CLI help output
- CLI handling of nonexistent input files
- Successful command-line execution

Example result:

```text
============================= test session starts =============================
collected 4 items

tests/test_analyzer.py ..                                           [ 50%]
tests/test_cli.py ..                                                [100%]

============================== 4 passed ==============================
```

## Continuous Integration

The project uses GitHub Actions to run the test suite automatically when:

- Code is pushed to the `main` branch
- A pull request targets the `main` branch

The workflow configuration is located at:

```text
.github/workflows/test.yml
```

The test badge at the top of this README shows the current continuous integration status.

## Development Workflow

A typical development workflow is:

```bash
git switch -c feature/new-feature
```

Make and test the changes:

```bash
pytest
```

Save the changes:

```bash
git add .
git commit -m "add new feature"
```

Push the branch:

```bash
git push -u origin feature/new-feature
```

The branch can then be reviewed and merged into `main` through a GitHub pull request.

## Technologies

- Python
- pandas
- PyYAML
- pytest
- argparse
- Git
- GitHub
- GitHub Actions

## Future Improvements

- Add column-level missing-value summaries
- Add median and standard-deviation statistics
- Support additional file formats
- Add configurable logging levels
- Improve exception handling
- Add data visualization
- Add test coverage reporting
- Integrate the analyzer into a larger machine-learning data pipeline