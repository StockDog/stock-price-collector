# stock-price-collector

Collects stock values of tickers that are in all active leagues and stores them into the "stockdog-stock" elasticsearch index.

## Running locally

1. `cp .env.example .env`
1. Fill in the `.env` values
1. `pipenv install`
1. `pipenv run python main.py`
