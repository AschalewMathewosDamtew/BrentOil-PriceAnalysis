# scripts/model_building.py

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA

def perform_adf_test(df):
    result = adfuller(df['Price'])
    return result[0], result[1]  # ADF statistic, p-value

def fit_arima_model(df, p, d, q):
    model = ARIMA(df['Price'], order=(p, d, q))
    model_fit = model.fit()
    return model_fit
