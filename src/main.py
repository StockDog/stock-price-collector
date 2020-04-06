import os

from helpers.mysql_service import get_all_owned_stocks
from helpers.iex_service import get_share_prices
from helpers.elasticsearch_service import upload_stock_values


def main():
    tickers = get_all_owned_stocks(
        os.getenv("db_host"),
        os.getenv("db_user"),
        os.getenv("db_pass"),
        os.getenv("db_name")
    )
    ticker_price_dict = get_share_prices(
        tickers, os.getenv("iex_token"))
    upload_stock_values(
        ticker_price_dict, os.getenv("elasticsearch_node"))


if __name__ == "__main__":
    main()
