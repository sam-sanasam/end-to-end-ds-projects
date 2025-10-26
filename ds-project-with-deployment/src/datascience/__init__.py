import os
import logging
import sys

# logging format as String
logging_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Logging file directory and file management

log_dir = "log"
os.makedirs(log_dir,exist_ok=True)

log_file = os.path.join(log_dir, "logging.log")

# Custom logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stderr)
    ]
)


# Define the logging

logger = logging.getLogger("The DS Project with Deployment")