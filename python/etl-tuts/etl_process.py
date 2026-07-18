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

def transform_data(df):
    """Transform the data"""
    try:
        df['total_price'] = df['quantity'] * df['unit_price']
        df['order_date'] = pd.to_datetime(df['order_date'])
        # Drop rows with missing values in any column
        df = df.dropna()
        logger.info("Data transformed successfully.")
        return df
    except Exception as e:
        logger.error(f"Error transforming data: {e}")
        raise