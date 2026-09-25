import logging
from pathlib import Path


class Logger:

    @staticmethod
    def get_logger(name="automation_framework"):

        project_root = Path(__file__).resolve().parents[1]
        log_directory = project_root / "logs"

        log_directory.mkdir(exist_ok=True)

        log_file = log_directory / "automation.log"

        logger = logging.getLogger(name)

        if not logger.handlers:
            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                log_file,
                encoding="utf-8"
            )

            console_handler = logging.StreamHandler()

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
