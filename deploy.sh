#!/bin/bash
pipenv run pip freeze > src/requirements.txt
sam build
sam package --s3-bucket stockdog-stock-price-collector --output-template-file template.packaged.yaml
sam deploy --template-file template.packaged.yaml --stack-name StockDogStockPriceCollector --capabilities CAPABILITY_IAM --no-fail-on-empty-changeset
rm src/requirements.txt