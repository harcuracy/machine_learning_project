from src.constant import *
from src.utils import create_directory, read_yaml
from src.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH,):
        self.config = read_yaml(config_file_path)
                
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
        