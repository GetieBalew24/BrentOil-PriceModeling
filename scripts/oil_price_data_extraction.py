# Step 2: Import the libraries
import wbdata
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class WorldDataAnalysis:
    def __init__(self):
        # Updated indicators dictionary with new indicators
        self.indicators = {
            "NY.GDP.MKTP.KD.ZG": "GDP Growth (%)",
            "FP.CPI.TOTL.ZG": "Inflation Rate (%)",
            "SL.UEM.TOTL.ZS": "Unemployment Rate (%)",
            "PA.NUS.FCRF": "Exchange Rate (USD)"
        }
        self.start_date = datetime(1986, 5, 20)
        self.end_date = datetime(2024, 9, 30)
        self.world_data = None

    def fetch_world_data(self):
        """Fetch world data for selected indicators from the World Bank API."""
        try:
            print("Fetching world data...")
            self.world_data = wbdata.get_dataframe(self.indicators, country="WLD")
            print("Fetch complete. Data type:", type(self.world_data))

            if isinstance(self.world_data, pd.DataFrame):
                self.world_data.reset_index(inplace=True)
                
                # Convert the 'date' column to datetime
                self.world_data['date'] = pd.to_datetime(self.world_data['date'])
                
                # Filter based on the date column
                self.world_data = self.world_data[(self.world_data['date'] >= self.start_date) & 
                                                (self.world_data['date'] <= self.end_date)]
                print("World data fetched and filtered by date successfully.")
                print(self.world_data.head())  # Preview the filtered data

                # Save to CSV
                self.world_data.to_csv('../data/world_data.csv', index=False)
                print("Data saved to 'world_data.csv'.")

            else:
                print("Unexpected output format:", type(self.world_data))
                print("Response content:", self.world_data)

        except Exception as e:
            print("Error fetching world data:", e)
    def resample_to_daily(self):
        """Resample annual world data to daily frequency and forward-fill."""
        if self.world_data is not None:
            self.world_data.set_index('date', inplace=True)  # Set date as index for resampling
            self.world_data_daily = self.world_data.resample('D').ffill()
            print("World data resampled to daily frequency.")
            print(self.world_data_daily.head())  # Display the first few rows for inspection
        else:
            print("World data not loaded. Run fetch_world_data() first.")
    def load_oil_prices_from_csv(self, file_path):
        """Load daily oil price data from a CSV file."""
        try:
            self.oil_prices = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')
            print("Oil prices loaded successfully.")
            print(self.oil_prices.head())  # Display the first few rows for inspection
        except Exception as e:
            print("Error loading oil prices from CSV:", e)