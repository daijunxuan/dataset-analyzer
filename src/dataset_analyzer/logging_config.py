import logging
from pathlib import Path


def setup_logging(log_file: Path = Path("logs/app.log")) -> None:
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )
