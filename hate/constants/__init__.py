import os
from datetime import datetime


ARTIFACTS_DIR=os.path.join("artifact")
BUCKET_NAME="hate_speech_detection_live"
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")
ZIP_FILE_NAME = 'dataset.zip'
LABEL = 'label'
TWEET = 'tweet'

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"

# Data validation constants
DATA_VALIDATION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_VALIDATION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_VALIDATION_RAW_DATA_DIR = "raw_data.csv"