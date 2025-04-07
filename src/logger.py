import logging
import os
import sys
from datetime import datetime

# Set log filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Setup logging configuration
logging.basicConfig(
    format='[%(asctime)s] : %(name)s : %(levelname)s: %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create a logger instance
logger = logging.getLogger("custom_logger")
