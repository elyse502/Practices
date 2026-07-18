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

def load_data(df, output_path):
    """Load the data to a csv file"""
    try:
        df.to_csv(output_path, index=False)
        logger.info("Data loaded successfully.")
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise

def etl():
    """ETL process function"""
    try:
        input_file_path = "data/sales_data.csv"
        output_file_path = "data/transformed_data.csv"

        # Extract
        data = extract_data(input_file_path)

        # Transform
        transformed_data = transform_data(data)

        # Load
        load_data(transformed_data, output_file_path)

        logger.info("ETL process completed successfully.")
    except Exception as e:
        logger.error(f"Error ETL process failed: {e}")

if __name__ == "__main__":
    etl()