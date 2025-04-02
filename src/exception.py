import sys
from src.logger import logger
import os

def my_custom_exception(error, error_details:sys):
    _,_, exc_tb = sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in script: [{filename}] at line number: [{line_number}] with error message: [{str(error)}]"
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = my_custom_exception(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message
    
    
    
    
