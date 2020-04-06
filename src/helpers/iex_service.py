import requests


def get_share_prices(tickers, iex_token):
    """Retreives prices from iex and returns a dict (ticker - price)."""
    tickers_delimited = ','.join(tickers)
    request_url = f'https://cloud.iexapis.com/stable/stock/market/quote?symbols={tickers_delimited}&token={iex_token}&filter=symbol,latestPrice'
    raw_response = requests.get(request_url)

    if (raw_response.status_code != 200):
        raw_response.raise_for_status()

    response = raw_response.json()

    # Converting to dictionary because it is better
    ticker_price_dict = {}
    for stock in response:
        ticker_price_dict[stock['symbol']] = stock['latestPrice']

    return ticker_price_dict
