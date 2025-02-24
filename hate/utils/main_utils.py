import yaml
import sys
from hate.logger import logging
from hate.exception import CustomException

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        logging.error(CustomException(e, sys))