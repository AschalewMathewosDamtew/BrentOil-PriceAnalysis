# scripts/data_preprocessing.py

import pandas as pd

def load_and_preprocess_data(file_path):
    # Load the data
    df = pd.read_csv(file_path, parse_dates=['Date'], infer_datetime_format=True)

    # Drop any missing values
    df.dropna(inplace=True)

    # Set 'Date' as the index
    df.set_index('Date', inplace=True)

    # Ensure daily frequency
    df = df.asfreq('D')

    # Forward fill missing prices
    df['Price'] = df['Price'].ffill()

    return df