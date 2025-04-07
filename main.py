import sys

from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_data_validation import DataValidationPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.exception import CustomException
from src.logger import logging


STAGE_NAME = 'data ingestion'




try:
    logging.info(f'========================> starting {STAGE_NAME} stage  <=================================')
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logging.info(f'========================> completed {STAGE_NAME} stage  <=================================')
except Exception as e:
    logging.info(f'========================> failed {STAGE_NAME} stage  <=================================')
    raise CustomException(e, sys)

    

STAGE_NAME = 'data validation'
try:
    logging.info(f'========================> starting {STAGE_NAME} stage  <=================================')
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logging.info(f'========================> completed {STAGE_NAME} stage  <=================================')

except Exception as e:
    logging.info(f'========================> failed {STAGE_NAME} stage  <=================================')
    raise CustomException(e, sys)



STAGE_NAME = 'data transformation'
try:
    logging.info(f'========================> starting {STAGE_NAME} stage  <=================================')
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logging.info(f'========================> completed {STAGE_NAME} stage  <=================================')
    
except Exception as e:
    logging.info(f'========================> failed {STAGE_NAME} stage  <=================================')
    raise CustomException(e, sys)
        
    