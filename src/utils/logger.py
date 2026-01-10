import logging
import os

def setup_logger():
    # Create logs folder if it doesn't exist
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("etl_logger")
    logger.setLevel(logging.INFO)

    # Prevent duplicate logs
    if logger.handlers:
        return logger

    # File handler (writes to file)
    file_handler = logging.FileHandler("logs/pipeline.log")
    file_handler.setLevel(logging.INFO)

    # Console handler (prints to terminal)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

