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
    
    
@dataclass
class DataTransformationConfig:

    DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS_DIR,DATA_TRANSFORMATION_ARTIFACTS_DIR)
    TRANSFORMED_FILE_PATH = os.path.join(DATA_TRANSFORMATION_ARTIFACTS_DIR,TRANSFORMED_FILE_NAME)
    ID = ID
    AXIS = AXIS
    INPLACE = INPLACE 
    DROP_COLUMNS = DROP_COLUMNS
    CLASS = CLASS 
    LABEL = LABEL
    TWEET = TWEET
    
    
    
@dataclass
class ModelTrainerConfig: 
   
        TRAINED_MODEL_DIR: str = os.path.join(os.getcwd(),ARTIFACTS_DIR,MODEL_TRAINER_ARTIFACTS_DIR) 
        TRAINED_MODEL_PATH = os.path.join(TRAINED_MODEL_DIR,TRAINED_MODEL_NAME)
        X_TEST_DATA_PATH = os.path.join(TRAINED_MODEL_DIR, X_TEST_FILE_NAME)
        Y_TEST_DATA_PATH = os.path.join(TRAINED_MODEL_DIR, Y_TEST_FILE_NAME)
        X_TRAIN_DATA_PATH = os.path.join(TRAINED_MODEL_DIR, X_TRAIN_FILE_NAME)
        MAX_WORDS = MAX_WORDS
        MAX_LEN = MAX_LEN
        LOSS = LOSS
        METRICS = METRICS
        ACTIVATION = ACTIVATION
        LABEL = LABEL
        TWEET = TWEET
        RANDOM_STATE = RANDOM_STATE
        EPOCH = EPOCH
        BATCH_SIZE = BATCH_SIZE
        VALIDATION_SPLIT = VALIDATION_SPLIT
        
        
@dataclass
class ModelEvaluationConfig: 
    def __init__(self):
        self.MODEL_EVALUATION_MODEL_DIR: str = os.path.join(os.getcwd(),ARTIFACTS_DIR, MODEL_EVALUATION_ARTIFACTS_DIR)
        self.BEST_MODEL_DIR_PATH: str = os.path.join(self.MODEL_EVALUATION_MODEL_DIR,BEST_MODEL_DIR)
        self.BUCKET_NAME = BUCKET_NAME 
        self.MODEL_NAME = MODEL_NAME 
        
        
@dataclass
class ModelPusherConfig:

    def __init__(self):
        self.TRAINED_MODEL_PATH = os.path.join(os.getcwd(),ARTIFACTS_DIR, MODEL_TRAINER_ARTIFACTS_DIR)
        self.BUCKET_NAME = BUCKET_NAME
        self.MODEL_NAME = MODEL_NAME