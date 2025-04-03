import sys

from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.exception import CustomException
from src.logger import logging


STAGE_NAME = 'data ingestion'

def main():
    try:
        logging.info(f'========================> starting {STAGE_NAME} stage  <=================================')
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.main()
        logging.info(f'========================> completed {STAGE_NAME} stage  <=================================')
    except Exception as e:
        logging.info(f'========================> failed {STAGE_NAME} stage  <=================================')
        raise CustomException(e, sys)
    
if __name__ == "__main__":
    main()
        
    