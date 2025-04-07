import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split


from src.entity.config_entity import DataTransformationConfig
from src.exception import CustomException
from src.logger import logging

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def transform_data(self):
        try:
            logging.info("Data Transformation started")
            df = pd.read_csv(self.config.input_file)
            df.drop(columns=['Id'], inplace=True)
            train_df,test_df = train_test_split(df, random_state=42, test_size=0.2)
            train_df.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test_df.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
            logging.info("Data Transformation completed successfully.")
            return train_df, test_df
        except Exception as e:
            raise CustomException(e, sys)
         
            
        