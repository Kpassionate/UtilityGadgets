#!/usr/bin/python
# -*- coding:utf-8 -*-


from elasticsearch_dsl import connections as es_connections
from elasticsearch_dsl import Search, Q as es_Q

from config import es_config


class ESDslStudy(object):
    def __init__(self):
        self.es_index = None
        self.es_host = None
        for self.es_index, config_dict in es_config.items():
            self.es_host = config_dict['es_host']
            if self.es_host:
                es_connections.create_connection(alias=self.es_index, hosts=self.es_host, timeout=20)

    def es_count(self, es_query=None):
        """
        获取查询总数
        :return:
        """
        search = Search(using='flights')
        if es_query:
            search = search.query(es_query)
        count = search.count()
        return count

    def es_search(self, es_query: dict):
        """
        获取查询总数
        :return:
        """
        if not es_query:
            return
        search = Search(using='flights')
        search = search.extra(track_total_hits=True)
        query = es_Q('bool', should=es_query.get('should'))
        search = search.query(query)
        print(search.to_dict())
        response = search.execute()
        result = response.to_dict()
        return result


if __name__ == "__main__":
    es = ESDslStudy()
    query = {
        "term": {
            "DestCountry": {
                "value": "AU"
            }
        }
    }
    print(es.es_count(query))
    d = {
        "should": [
            {"term": {
                "FlightNum": {
                    "value": "9HY9SWR"
                }
            }}
        ]
    }
    print(es.es_search(d))
