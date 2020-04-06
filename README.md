# stock-price-collector

Collects stock values of tickers that are in all active leagues and stores them into the "stockdog-stock" elasticsearch index.

## Running locally

1. `cp .env.example .env`
1. Fill in the `.env` values
1. `pipenv install`
1. `pipenv run python src/main.py`

## Deploying

1. `chmod +x deploy.sh`
1. `./deploy.sh`

or

1. `pipenv run pip freeze > src/requirements.txt`
1. `sam build`
1. `sam package --s3-bucket stockdog-stock-price-collector --output-template-file template.packaged.yaml`
1. `sam deploy --template-file template.packaged.yaml --stack-name StockDogStockPriceCollector --capabilities CAPABILITY_IAM --no-fail-on-empty-changeset`
1. `rm src/requirements.txt`
1. Make sure the lambda function has the required environment variables spelled out in `.env.example`
