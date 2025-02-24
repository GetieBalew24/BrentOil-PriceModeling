import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import adfuller

class ModelBuilder:
    """
    A class for building and evaluating time series models.
    """
    def __init__(self):
        """
        Initializes the ModelBuilder class.
        """
        self.model = None

    def split_data(self, data, train_size=0.8):
        """
        Splits the data into training and testing sets.

        Parameters:
        - data (array-like): The complete dataset.
        - train_size (float): Proportion of data to be used for training. Default is 0.8.

        Returns:
        - train_data (array-like): Training dataset.
        - test_data (array-like): Testing dataset.
        """
        try:
            train_size = int(len(data) * train_size)
            train_data = data[:train_size]
            test_data = data[train_size:]
            return train_data, test_data
        except Exception as e:
            logging.error(f"Error in splitting data: {e}")
            return None, None
    def adf_test(self,series):
        """
        Performs the Augmented Dickey-Fuller (ADF) test on a time series to check for stationarity.

        Args:
        series (pandas.Series): The time series data to be tested for stationarity.

        Returns:
        dict: A dictionary containing the ADF Statistic and p-value of the test.
            - 'ADF Statistic' (float): The test statistic for the ADF test.
            - 'p-value' (float): The p-value corresponding to the test statistic.

        The ADF test checks the null hypothesis that a unit root is present in the time series.
        A low p-value (typically below 0.05) suggests rejecting the null hypothesis, indicating
        that the series is likely stationary.
        """
        result = adfuller(series)
        return {'ADF Statistic': result[0], 'p-value': result[1]}

