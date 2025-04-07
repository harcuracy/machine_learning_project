from src.exception import CustomException
from src.entity.config_entity import DataValidationConfig
from src.logger import logging


import pandas as pd
import os
import sys

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_data(self):
        try:
            logging.info("Data Validation started")
            data = pd.read_csv(self.config.data_file)
            data = data.drop(columns=["Id"], axis=1, errors='ignore')  
            columns = set(data.columns)
            all_schema = set(self.config.all_schema.keys())

            # Check if all required columns are present
            missing_columns = all_schema - columns
            extra_columns = columns - all_schema

            if missing_columns:
                logging.info(f"Missing columns: {missing_columns}")
                validation_status = False
            elif extra_columns:
                logging.info(f"Unexpected extra columns: {extra_columns}")
                validation_status = False  
            else:
                validation_status = True
            
            with open(self.config.status, "w") as f:
                f.write(f"validation_status:{validation_status}")

            logging.info("Data Validation completed successfully")

        except Exception as e:
            logging.error("Error in data validation")
            logging.error(e)
            raise CustomException(e, sys)