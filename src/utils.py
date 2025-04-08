import requests
import os
from box import ConfigBox,Box
import yaml
import json
from pathlib import Path
from src.logger import logger,logging

def create_directory(directory_path):
    """
    Create a directory if it does not exist.
    
    Args:
        directory_path (str): The path of the directory to create.
    
    Returns:
        None
    """
    
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        logging.info(f"Directory '{directory_path}' created.")
    else:
        logging.info(f"Directory '{directory_path}' already exists.")
        
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """

    with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
   
def save_json(data: dict, filepath: str):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"json file: {filepath} saved successfully")       
