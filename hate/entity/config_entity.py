from dataclasses import dataclass
from hate.constants import *
import os

@dataclass
class DataIngestionConfig:

    BUCKET_NAME: str = BUCKET_NAME
    ZIP_FILE_NAME: str = ZIP_FILE_NAME
    DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
    DATA_ARTIFACTS_DIR: str = os.path.join(DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_IMBALANCE_DATA_DIR)
    NEW_DATA_ARTIFACTS_DIR: str = os.path.join(DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_RAW_DATA_DIR)
    ZIP_FILE_DIR: str = DATA_INGESTION_ARTIFACTS_DIR
    ZIP_FILE_PATH: str = os.path.join(DATA_INGESTION_ARTIFACTS_DIR, ZIP_FILE_NAME)
    
    
    