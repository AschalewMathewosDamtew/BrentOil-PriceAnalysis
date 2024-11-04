# main.py

from scripts.data_preprocessing import load_and_preprocess_data
from scripts.visualization import plot_brent_oil_prices, decompose_time_series
from scripts.model_building import perform_adf_test, fit_arima_model

def main():
    # Specify the path to your CSV file
    file_path = 'data/BrentOilPrices.csv'

    # Load and preprocess the data
    df = load_and_preprocess_data(file_path)

    # Visualize the data
    plot_brent_oil_prices(df)

    # Decompose the time series
    decompose_time_series(df)

    # Perform the ADF test for stationarity
    adf_stat, p_value = perform_adf_test(df)
    print('ADF Statistic:', adf_stat)
    print('p-value:', p_value)

    # Fit the ARIMA model
    p, d, q = 1, 1, 1  # Adjust based on your analysis
    model_fit = fit_arima_model(df, p, d, q)

    # Print the summary of the model
    print(model_fit.summary())

if __name__ == "__main__":
    main()
