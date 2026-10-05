import subprocess


def run_cli(*args, cwd=None):
    return subprocess.run(["dataset-analyzer", *map(str, args)], cwd=cwd,
                          capture_output=True, text=True)


def test_cli_help():
    result = run_cli("--help")
    assert result.returncode == 0
    assert "Analyze CSV datasets" in result.stdout


def test_cli_missing_file(tmp_path):
    result = run_cli("--input", "missing.csv", cwd=tmp_path)
    assert result.returncode != 0
    assert "Input file does not exist" in result.stderr


def test_runs_outside_checkout_and_creates_output_directory(tmp_path):
    data = tmp_path / "input.csv"
    data.write_text("x\n1\n3\n")
    output = tmp_path / "nested" / "report.json"
    result = run_cli("--input", data, "--output", output, cwd=tmp_path)
    assert result.returncode == 0, result.stderr
    assert output.is_file()


def test_config_paths_are_relative_to_config(tmp_path):
    config_dir = tmp_path / "settings"
    config_dir.mkdir()
    (config_dir / "input.csv").write_text("x\n1\n3\n")
    config = config_dir / "config.yaml"
    config.write_text("data:\n  input_file: input.csv\noutput:\n  report_file: out/report.json\n")
    result = run_cli("--config", config, cwd=tmp_path)
    assert result.returncode == 0, result.stderr
    assert (config_dir / "out/report.json").is_file()


def test_invalid_config_fails_cleanly(tmp_path):
    config = tmp_path / "config.yaml"
    config.write_text("data: []\n")
    result = run_cli("--config", config, cwd=tmp_path)
    assert result.returncode != 0
    assert "Error:" in result.stderr
    assert "Traceback" not in result.stderr
