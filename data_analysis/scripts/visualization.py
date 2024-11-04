# scripts/visualization.py

import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def plot_brent_oil_prices(df):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Price'], marker='o')
    plt.title('Brent Oil Prices Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price (USD per barrel)')
    plt.grid()
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.boxplot(df['Price'])
    plt.title('Boxplot of Brent Oil Prices')
    plt.ylabel('Price (USD per barrel)')
    plt.show()

def decompose_time_series(df):
    decomposition = seasonal_decompose(df['Price'], model='additive')
    decomposition.plot()
    plt.show()
