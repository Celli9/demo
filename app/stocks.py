
import os

from dotenv import load_dotenv
from pandas import read_csv
import plotly.express as px

load_dotenv() # read env vars from the ".env" file

# use environment variable to make API key secure (it is stored in .env file), do not hard code it in a file for security reasons
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


# usually put this in the function, mine was giving me a bug, this is a docstring (documentation string)
"""Fetches stock data from the AlphaVantage API.

    Params:
        symbol (str) like "NFLX"

    Return a pandas DataFrame with the time series data.
    """
def fetch_stocks_data(symbol):
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&outputsize=full&datatype=csv"
    return read_csv(request_url)

# do this if statement so your tests can be run and passed
# When a test comes in and imports the file, it won't have to run the entire file, we just want to test the function above
if __name__ == "__main__":

    selected_symbol = input("Please input a stock symbol (e.g. 'GOOGL'): ") or "GOOGL"
    df = fetch_stocks_data(selected_symbol)
    print(df.head())

    # todo: answer some questions about the data
    latest_close = df["adjusted_close"][0]
    print(f"LATEST CLOSE: ${latest_close:.2f}")

    # make a dataviz:
    title = f"Stock Prices over Time ({selected_symbol})"
    fig = px.line(df, x="timestamp", y="adjusted_close",
                  title=title, height=400,
    )
    fig.show()
