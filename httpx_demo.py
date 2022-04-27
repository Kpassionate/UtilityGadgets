import json
import httpx


def get_es_data():
    # PUT kibana_sample_data_flights/_alias/flights
    session = ('elastic', 'elastic')
    url = 'http://localhost:9200/flights/_search'
    with httpx.Client(auth=session, headers={'Content-Type': 'application/json'}, timeout=60) as client:
        body = {
            "query": {
                "match_all": {}
            },
            "track_total_hits": True
        }
        es_str = json.dumps(body, ensure_ascii=False)
        resp = client.post(url, data=es_str.encode('utf-8'))
        return resp.json()


if __name__ == '__main__':
    response = get_es_data()
    print(response['hits']['total']['value'])

