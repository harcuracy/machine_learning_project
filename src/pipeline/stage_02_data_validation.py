import sys

from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation
from src.exception import CustomException
from src.logger import logging

STAGE_NAME = "Data Validation"

class DataValidationPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_data()
        
if __name__ == "__main__":
    try:
        logging.info(f'========================> starting {STAGE_NAME} stage  <=================================')
        logging.info("Data Validation started")
        data_validation_pipeline = DataValidationPipeline()
        data_validation_pipeline.main()
        logging.info("Data validation completed successfully.")
        logging.info(f'========================> completed {STAGE_NAME} stage  <=================================')
    except Exception as e:
        logging.info(f'========================> failed {STAGE_NAME} stage  <=================================')
        raise CustomException(e, sys)
        logging.info("Data Validation failed")
    
        