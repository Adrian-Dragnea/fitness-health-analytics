from src.utils.config import load_config
from src.utils.logger import setup_logger
from src.extract.extract_kaggle import download_kaggle_dataset

logger = setup_logger()

def main():
    logger.info("ETL pipeline started")

    config = load_config()

    logger.info(f"Environment: {config['environment']['name']}")

    dataset = config["kaggle"]["dataset"]
    raw_path = config["paths"]["raw_data"]

    download_kaggle_dataset(dataset, raw_path)

    logger.info("ETL pipeline finished successfully")

if __name__ == "__main__":
    main()