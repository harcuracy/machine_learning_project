from sklearn.linear_model import ElasticNet
import pandas as pd
import sys
from joblib import dump



from src.exception import CustomException
from src.entity.config_entity import ModelTrainingConfig
from src.logger import logging


class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        
    def train_model(self):
        try:
            logging.info("Loading data")
            df = pd.read_csv(self.config.train_data_file)
            
            X = df.drop(columns=[self.config.target_column])
            y = df[self.config.target_column]
            model = ElasticNet(
                alpha=self.config.all_params.alpha,
                l1_ratio=self.config.all_params.l1_ratio,
                random_state=42
            )
            model.fit(X, y)
            logging.info("Model training completed")
            
            logging.info("Saving the trained model")
            # Save the model to the specified path
            dump(model, self.config.model_file)
            logging.info(f"Model saved at {self.config.model_file}")
            
        except Exception as e:
            raise CustomException(e, sys)