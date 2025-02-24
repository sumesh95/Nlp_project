import os
import sys
import pandas as pd
from hate.logger import logging
from hate.exception import CustomException
from hate.entity.artifact_entity import DataValidationArtifacts,DataIngestionArtifacts
from hate.constants import *
from hate.utils import main_utils


class DataValidation:
    
    def __init__(self,data_ingestion_artifact:DataIngestionArtifacts):
        self.data_validation_artifact=DataValidationArtifacts(imbalance_data_file_path=data_ingestion_artifact.imbalance_data_file_path,
                                                              raw_data_file_path=data_ingestion_artifact.raw_data_file_path)
        self.schmea_file_path=main_utils.read_yaml_file(SCHEMA_FILE_PATH)
        pass
    
    @staticmethod
    def read_csv_file(filePath):
         try:
             return pd.read_csv(filePath)
         except Exception as e:
             logging.error(CustomException(sys,e))


    def validate_total_number_of_columns(self,dataframe:pd.DataFrame,schemaFile:list):
        
        try:
            if len(dataframe.columns)==len(schemaFile):
                return True
            return False
        except Exception as e:
            logging.error(CustomException(sys,e))
            
    def validate_data_types(self,dataframe: pd.DataFrame, schemaFile) -> bool:

        try:
            schema_data_types = schemaFile["dataTypes"]  # Extract data types from schema

            for column, expected_dtype in schema_data_types.items():
                actual_dtype = str(dataframe[column].dtype).lower()
                expected_dtype = expected_dtype.lower()

                if actual_dtype != expected_dtype:
                    logging.error(f"Data type mismatch for '{column}': Expected {expected_dtype}, Found {actual_dtype}")
                    return False

            return True  
        except Exception as e:
            logging.error(f"Error in data type validation: {e}")
            return False
            
            
    def initiate_data_validation(self):
        
        try:
            raw_data_csv=DataValidation.read_csv_file(self.data_validation_artifact.raw_data_file_path)
            imbalance_data_csv=DataValidation.read_csv_file(self.data_validation_artifact.imbalance_data_file_path)
            raw_data_schema_columns=self.schmea_file_path['rawData']['columns']
            raw_data_schema=self.schmea_file_path['rawData']
            imbalance_data_schema_columns=self.schmea_file_path['imbalanceData']['columns']
            imbalance_data_schema=self.schmea_file_path['imbalanceData']
            self.validate_total_number_of_columns(raw_data_csv,raw_data_schema_columns)
            self.validate_total_number_of_columns(imbalance_data_csv,imbalance_data_schema_columns)
            self.validate_data_types(raw_data_csv,raw_data_schema)
            self.validate_data_types(imbalance_data_csv,imbalance_data_schema)
            
        except Exception as e:
            
            logging.error(CustomException(e,sys))
        
        
        





