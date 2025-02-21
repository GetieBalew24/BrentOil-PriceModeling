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