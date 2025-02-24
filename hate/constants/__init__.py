import os
from datetime import datetime

TIMESTMAP=datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACTS_DIR=os.path.join("artifact",TIMESTMAP)
BUCKET_NAME="hate_speech_detection_live"
ZIP_FILE_NAME = 'dataset.zip'
LABEL = 'label'
TWEET = 'tweet'

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"