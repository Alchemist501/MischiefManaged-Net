# File: src/utils/logger.py

import logging
import sys

def setup_logger():
    """Sets up the main logger for the application."""
    # Create a logger object
    logger = logging.getLogger("MaraudersMap")
    logger.setLevel(logging.INFO)

    # Prevent logs from being propagated to the root logger
    logger.propagate = False

    # Create a handler to write to the console (stdout)
    stdout_handler = logging.StreamHandler(sys.stdout)
    
    # Create a handler to write to a log file
    file_handler = logging.FileHandler("logs/app.log")

    # Define the format for the log messages
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stdout_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger, but only if they haven't been added before
    if not logger.handlers:
        logger.addHandler(stdout_handler)
        logger.addHandler(file_handler)
        
    return logger