import subprocess


def test_cli_help():

    result = subprocess.run(
        ["dataset-analyzer", "--help"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Analyze CSV datasets" in result.stdout


def test_cli_missing_file():

    result = subprocess.run(
        [
            "dataset-analyzer",
            "--input",
            "not_exist.csv"
        ],
        capture_output=True,
        text=True
    )

    assert "Error: Input file does not exist" in result.stdout