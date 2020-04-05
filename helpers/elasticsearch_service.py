from datetime import datetime

from elasticsearch import Elasticsearch


def upload_stock_values(ticker_price_dict, elastic_host):
    es = Elasticsearch(elastic_host)

    now = datetime.utcnow()

    bulk_data = []
    for ticker in ticker_price_dict:
        bulk_data.append({"index": {
            "_index": "stockdog-stock",
            "_type": "document",
        }})
        bulk_data.append({
            "ticker": ticker,
            "price": ticker_price_dict[ticker],
            "timestamp": now
        })

    es.bulk(body=bulk_data)
