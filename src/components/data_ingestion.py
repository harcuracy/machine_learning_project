import requests
from zipfile import ZipFile
import sys

from src.exception import CustomException
from src.logger import logging
from src.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    
    def download_file(self):
        """
     Download a file from a URL and save it to the specified file path.
 
     Args:
         url (str): The URL to download the file from.
         file_path (str): The local path where the file will be saved.
 
     Returns:
         None
     """
        try:
            url = self.config.source_URL
            file_path = self.config.local_data_file
            response = requests.get(url)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            logging.info(f"File downloaded successfully from {url} to {file_path}")
        except Exception as e:
            logging.info(f"Failed to download file from {url}. Error: {str(e)}")
            raise CustomException(e, sys)
        
    def extract_zip_file(self):
        """
        Extract a zip file to the specified directory.
        
        Args:
            file_path (str): The path of the zip file to unzip.
            extract_to (str): The directory to extract the contents to.
        """
        try:
            file_path = self.config.local_data_file
            extract_to = self.config.unzip_dir
            with ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
            logging.info(f"Unzipped '{file_path}' to '{extract_to}'.")
        except Exception as e:
            logging.info(f"Failed to unzip file from {file_path}. Error: {str(e)}")
            raise CustomException(e, sys)
    
        
            
         
         