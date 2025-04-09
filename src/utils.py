import requests
import os
from box import ConfigBox,Box
import yaml
from src.exception import CustomException
import json
from pathlib import Path
from src.logger import logger,logging
import joblib
import sys

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

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return joblib.load(file_obj)
    except Exception as e:
        logging.error("Exception Occurred in load_object function utils")
        raise CustomException(e, sys)
