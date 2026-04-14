import logging
import os
from datetime import datetime


# Create logs directory
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)
os.makedirs(LOG_DIR, exist_ok=True)


# Create log file name with timestamp
CURRENT_TIME_STAMP = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
LOG_FILE = f"log_{CURRENT_TIME_STAMP}.log"


# Full log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)


# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='a',   # append mode
    format='[%(asctime)s] %(levelname)s - %(message)s',
    level=logging.INFO
)


# Create logger object
logger = logging.getLogger()


# ALSO print logs on console (IMPORTANT 🔥)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)