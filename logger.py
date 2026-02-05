import os
import logging
from pathlib import Path


class LoggerFactory:
    def __init__(self, project: str = "test"):
        """
        Initialize logger for a project.

        Args:
            project: Project name like 'gui', 'api', 'unit'
                    - Logger name becomes: 'GUITests', 'APITests', 'UnitTests'
                    - Log file becomes: 'gui_test_run_*.log', 'api_test_run_*.log'
        """
        self.project = project
        self.logger_name = f"{project}"
        self.logger = self._setup_logger()

    def _setup_logger(self):
        """Setup logger with console and file output."""
        logger = logging.getLogger(self.logger_name)

        if logger.handlers:
            return logger

        logger.setLevel(logging.DEBUG)
        logger.addHandler(self._create_console_handler())
        logger.addHandler(self._create_file_handler())

        return logger

    @staticmethod
    def _create_console_handler():
        """Console output - prints to terminal."""
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
        return handler

    def _create_file_handler(self):
        """File output - separate file per worker for parallel safety."""
        log_dir = Path(__file__).parent / "logs"
        log_dir.mkdir(exist_ok=True)

        # Get worker ID for parallel runs for separate log files per worker
        worker_id = os.environ.get('PYTEST_XDIST_WORKER', 'master')
        log_file = log_dir / f"{self.project}-test-run-{worker_id}.log"

        handler = logging.FileHandler(log_file, mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
        return handler

    # Convenience methods for direct fixture logging
    def info(self, message: str):
        """Log info message."""
        self.logger.info(message)

    def debug(self, message: str):
        """Log debug message."""
        self.logger.debug(message)

    def warning(self, message: str):
        """Log warning message."""
        self.logger.warning(message)

    def error(self, message: str):
        """Log error message."""
        self.logger.error(message)