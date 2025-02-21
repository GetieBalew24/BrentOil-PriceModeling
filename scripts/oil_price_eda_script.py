# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from datetime import datetime
import ruptures as rpt
from statsmodels.tsa.seasonal import seasonal_decompose
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BrentOilPricesEDA:
    """
    A class for performing exploratory data analysis (EDA) on Brent oil price data.
    
    Parameters
    ----------
    file_path : str
        Path to the CSV file containing the Brent oil price data with 'Date' and 'Price' columns.
    """
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    
    def load_data(self):
        """
        Loads the CSV file into a DataFrame.
        
        Returns
        -------
        pd.DataFrame
            The loaded data.
        """
        start_time = datetime.now()
        try:
            self.data = pd.read_csv(self.file_path)
            logging.info("Data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            raise
        end_time = datetime.now()
        logging.info(f"Data loading completed in {end_time - start_time}.")
        return self.data
    def format_date(self):
        """
        Converts the 'Date' column to datetime, handles invalid dates, and sets 'Date' as the index.
        Returns
        -------
        pd.DataFrame
            DataFrame with 'Date' as the index.
        """
        if self.data is None:
            logging.warning("Data not loaded. Please load data before calling format_date.")
            return None
        
        start_time = datetime.now()
        # Convert Date column to datetime format with error handling
        self.data['Date'] = pd.to_datetime(self.data['Date'], infer_datetime_format=True, errors='coerce')
        
        # Drop rows with invalid dates
        invalid_dates = self.data[self.data['Date'].isna()]
        if not invalid_dates.empty:
            logging.warning(f"Found {len(invalid_dates)} rows with invalid dates. Dropping these rows.")
            self.data = self.data.dropna(subset=['Date'])
        
        # Sort by date and reset index
        self.data = self.data.sort_values('Date').reset_index(drop=True)
        self.data.set_index('Date', inplace=True)
        
        end_time = datetime.now()
        logging.info(f"Date formatting completed in {end_time - start_time}.")
        return self.data