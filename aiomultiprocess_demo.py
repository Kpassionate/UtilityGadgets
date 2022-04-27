import asyncio
import json
import time
import httpx
from aiomultiprocess import Pool


async def get_es_data(url):
    session = ('elastic', 'elastic')
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
    urls = ['http://localhost:9200/flights/_search'] * 10000
    async with Pool() as pool:
        print(pool.process_count)
        index = 0
        async for result in pool.map(get_es_data, urls):  # 多核异步 CPU直接打满 快就一个字
            index += 1
            print(result, index)  # 每一个URL返回的内容


# async def main():
#     urls = ['http://localhost:9200/flights/_search'] * 10000
#     async with Pool() as pool:
#         print(pool.process_count)
#         index = 0
#         for url in urls:
#             index += 1
#             # res = await pool.apply(func=get_es_data, args=(url,))  # 及其慢
#             res = await get_es_data(url) # 单核异步 一般
#             print(res, index)


if __name__ == '__main__':
    a = time.time()
    asyncio.run(main())
    print(time.time() - a)
