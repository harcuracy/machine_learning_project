import sys

from src.config.configuration import ConfigurationManager
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation


STAGE_NAME = "Data Transformation"

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.transform_data()
            logging.info(f"{STAGE_NAME} stage completed successfully.")
        except Exception as e:
            logging.info(f"Error in {STAGE_NAME} stage: {e}")
            raise CustomException(e, sys)