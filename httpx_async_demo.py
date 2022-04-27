import asyncio
import json
import time

import httpx


async def get_es_data(url):
    session = ('elastic', 'elastic')
    # url = 'http://localhost:9200/flights/_search'
    async with httpx.AsyncClient(auth=session, headers={'Content-Type': 'application/json'}, timeout=60) as client:
        body = {
            "query": {
                "match_all": {}
            },
            "track_total_hits": True
        }
        es_str = json.dumps(body, ensure_ascii=False)
        response = await client.post(url, data=es_str.encode('utf-8'))
        resp = response.json()
        count = resp['hits']['total']['value']
        return count


async def main():
    index = 0
    for url in ['http://localhost:9200/flights/_search'] * 10000:
        res = await get_es_data(url)
        index += 1
        print(res, index)


if __name__ == '__main__':
    a = time.time()
    asyncio.run(main())
    print(time.time() - a)
