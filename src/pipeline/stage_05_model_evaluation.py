import sys

from src.config.configuration import ConfigurationManager
from src.logger import logging
from src.exception import CustomException

from src.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            # Load configuration
            logging.info("Loading configuration for model evaluation.")
            config = ConfigurationManager()
            model_eval_config = config.get_evaluation_config()

            # Initialize ModelEvaluation class
            model_eval = ModelEvaluation(config=model_eval_config)

            # Perform model evaluation
            model_eval.log_into_mlflow()
            logging.info("Model evaluation completed successfully.")

        except Exception as e:
            raise CustomException(e, sys) 
        