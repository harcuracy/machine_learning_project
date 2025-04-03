import sys

from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.exception import CustomException
from src.logger import logging

STAGE_NAME = 'data ingestion'

class DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logging.info("Data ingestion completed successfully.")
        except Exception as e:
            logging.info(f"An error occurred: {str(e)}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    try:
        logging.info(f'========================> starting {STAGE_NAME} stage  <=================================')
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logging.info(f'========================> completed {STAGE_NAME} stage  <=================================')
    except Exception as e:
        logging.info(f'========================> failed {STAGE_NAME} stage  <=================================')
        raise CustomException(e, sys)
        
