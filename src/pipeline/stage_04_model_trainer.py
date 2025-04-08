import sys

from src.config.configuration import ConfigurationManager
from src.logger import logging
from src.exception import CustomException
from src.components.model_trainer import ModelTrainer


STAGE_NAME = "Model Trainer"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            logging.info(f"{STAGE_NAME} started")
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train_model()
        except Exception as e:
            raise CustomException(e, sys) from e