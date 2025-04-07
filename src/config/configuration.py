from src.constant import *
from src.utils import create_directory, read_yaml
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import DataValidationConfig


class ConfigurationManager:
    def __init__(self, 
                 config_file_path=CONFIG_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH,
                 ):
        self.config = read_yaml(config_file_path)
        self.schema = read_yaml(schema_file_path)
                
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
        
        