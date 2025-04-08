import sys
import mlflow
import dagshub


from src.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.pipeline.stage_02_data_validation import DataValidationPipeline
from src.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from src.exception import CustomException
from src.logger import logging


dagshub.init(repo_owner='harcuracy', repo_name='machine_learning_project', mlflow=True)


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


STAGE_NAME = 'model trainer'
try:
    logging.info(f'========================> starting {STAGE_NAME} stage  <=================================')
    data_transformation_pipeline = ModelTrainerPipeline()
    data_transformation_pipeline.main()
    logging.info(f'========================> completed {STAGE_NAME} stage  <=================================')
    
except Exception as e:
    logging.info(f'========================> failed {STAGE_NAME} stage  <=================================')
    raise CustomException(e, sys)


STAGE_NAME = 'model evaluation'
try:
    logging.info(f'========================> starting {STAGE_NAME} stage  <=================================')
    data_transformation_pipeline = ModelEvaluationPipeline()
    data_transformation_pipeline.main()
    logging.info(f'========================> completed {STAGE_NAME} stage  <=================================')
    
except Exception as e:
    logging.info(f'========================> failed {STAGE_NAME} stage  <=================================')
    raise CustomException(e, sys)