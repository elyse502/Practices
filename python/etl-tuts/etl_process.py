# Automating ETL Process with Python
import pandas as pd
import logging

# Setup the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_data(file_path):
    """Extract the data from csv file"""

    try:
        df = pd.read_csv(file_path)
        logger.info("Data extracted successfully.")
        return df
    except Exception as e:
        logger.error(f"Error extracting data: {e}")
        raise