from src.constant import *
from src.utils import create_directory, read_yaml
from src.entity.config_entity import (DataIngestionConfig,
                                      DataValidationConfig,
                                      DataTransformationConfig,
                                      ModelTrainingConfig)



class ConfigurationManager:
    def __init__(self, 
                 config_file_path=CONFIG_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 ):
        self.config = read_yaml(config_file_path)
        self.schema = read_yaml(schema_file_path)
        self.params = read_yaml(params_file_path)
                
        create_directory(self.config.artifact_root)
        
    def get_data_ingestion_config(self):
        config = self.config.data_ingestion
        
        create_directory(config.root_dir)
        
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        all_schema = self.schema.COLUMNS
        
        create_directory(config.root_dir)
        
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            data_file=config.data_file,
            status=config.status,
            all_schema=all_schema
        )
        
        return data_validation_config
    
    def get_data_transformation_config(self):
        config = self.config.data_transformation
        
        create_directory(config.root_dir)
        
        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            input_file= config.input_file
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainingConfig:
        """
        Returns the Model Training Configuration
        """
        root_dir = self.config.model_training.root_dir
        all_params = self.params.PARAMETERS.model.params
        target_column = self.schema.TARGET_COLUMN.name
        train_data_file = self.config.model_training.train_data_file
        model_file = self.config.model_training.model_file
        
        
        create_directory(self.config.model_training.root_dir)
        
        model_training_config = ModelTrainingConfig(
            root_dir=root_dir,
            train_data_file=train_data_file,
            model_file=model_file,
            all_params=all_params,
            target_column=target_column
        )
        
        return model_training_config
        
        
        