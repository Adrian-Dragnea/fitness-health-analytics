import yaml
import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    config_path = os.getenv("CONFIG_PATH", "config/local.yaml")

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    return config
