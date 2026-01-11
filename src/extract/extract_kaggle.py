import os
import subprocess
from src.utils.logger import setup_logger

logger = setup_logger()

def download_kaggle_dataset(dataset, output_path):
    """
    Downloads a Kaggle dataset into the raw data folder
    """
    os.makedirs(output_path, exist_ok=True)

    logger.info(f"Downloading Kaggle dataset: {dataset}")
    logger.info(f"Target folder: {output_path}")

    command = [
        "kaggle",
        "datasets",
        "download",
        "-d",
        dataset,
        "-p",
        output_path,
        "--unzip"
    ]

    try:
        subprocess.run(command, check=True)
        logger.info("Kaggle dataset downloaded successfully")
    except subprocess.CalledProcessError as e:
        logger.error(f"Kaggle download failed: {e}")
        raise
