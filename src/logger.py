import logging
import os
import sys

from datetime import datetime



log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d')}.log")    

logging.basicConfig(
    filename=log_file,
    filemode='a',
    format='[%(asctime)s] : %(name)s : %(levelname)s: %(message)s',
    level=logging.INFO
)

# Create a logger instance
logger = logging.getLogger("custom_logger")





