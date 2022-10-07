import asyncio
import json
import httpx


async def get_es_data(client, data_list):
    if not data_list:
        return
    url = 'http://localhost:9200/flights/_search'
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
    processes = 10
    step_count = 50
    session = ('elastic', 'elastic')
    async with httpx.AsyncClient(auth=session, headers={'Content-Type': 'application/json'}, timeout=60) as client:
        item_list = [i for i in range(1000000)]
        len_i = len(item_list)
        i = 0
        while i < len_i:
            print(i)
            tasks = []
            for x in range(processes):
                p_start = i + step_count * x
                p_end = p_start + step_count
                id_l = item_list[p_start:p_end]
                func = asyncio.ensure_future(get_es_data(client, id_l))
                tasks.append(func)
            await asyncio.gather(*tasks)
            i += step_count * processes


if __name__ == '__main__':
    asyncio.run(main())

