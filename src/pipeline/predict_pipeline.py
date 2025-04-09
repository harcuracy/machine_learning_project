import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        self.model_path = os.path.join('artifact', 'model_training', 'model.joblib')

    def predict(self, features):
        try:
            logging.info("Prediction Pipeline Started")
            model = load_object(self.model_path)
            pred = model.predict(features)
            logging.info("Prediction completed")
            return pred

        except Exception as e:
            logging.error("Exception occurred in prediction")
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 fixed_acidity: float,
                 volatile_acidity: float,
                 citric_acid: float,
                 residual_sugar: float,
                 chlorides: float,
                 free_sulfur_dioxide: float,
                 total_sulfur_dioxide: float,
                 density: float,
                 pH: float,
                 sulphates: float,
                 alcohol: float):
        
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density = density
        self.pH = pH
        self.sulphates = sulphates
        self.alcohol = alcohol

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'fixed acidity': [self.fixed_acidity],
                'volatile acidity': [self.volatile_acidity],
                'citric acid': [self.citric_acid],
                'residual sugar': [self.residual_sugar],
                'chlorides': [self.chlorides],
                'free sulfur dioxide': [self.free_sulfur_dioxide],
                'total sulfur dioxide': [self.total_sulfur_dioxide],
                'density': [self.density],
                'pH': [self.pH],
                'sulphates': [self.sulphates],
                'alcohol': [self.alcohol]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df

        except Exception as e:
            logging.error('Exception Occurred in prediction pipeline')
            raise CustomException(e, sys)