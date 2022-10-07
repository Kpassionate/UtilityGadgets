import asyncio
import json
import time

import httpx


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
        sort_data = await bubble_sort()
        return count, sort_data


async def bubble_sort():
    """
    它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
    走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
    两两比较
    """
    arr = [64, 34, 25, 12, 22, 11, 90]

    # 遍历所有数组元素
    for i in range(len(arr)):
        # Last i elements are already in place
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


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
