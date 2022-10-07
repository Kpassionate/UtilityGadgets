#!/usr/bin/python
# -*- coding:utf-8 -*-

from elasticsearch import Elasticsearch

es = Elasticsearch('127.0.0.1', port=9200, http_auth=('elastic', 'elastic'), timeout=60)
es_query = {
    "query": {
        "term": {
            "DestCountry": {
                "value": "AU"
            }
        }
    }
}
response = es.search(index='kibana_sample_data_flights', body=es_query)
values = response['hits']['hits']
print([item['_id'] for item in values])
