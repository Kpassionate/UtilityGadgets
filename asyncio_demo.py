import datetime

import aiohttp
import asyncio
import json
from db_handler import execute_raw_sql, Database

prod_bid_host = "http:127.0.0.1:9200/bid_info/_bulk"
prod_es_user = ''
prod_es_passwd = ''

pre_bid_host = "xxxx/xxxx/_bulk"
pre_es_user = ''
pre_es_passwd = ''

db_config = {
    'default': {
        'host': '',
        'port': '3306',
        'user': '',
        'password': '',
        'database': '',
    },
}

Database.connect(**db_config)


def sql_search(mid_list):
    # 正文
    text_sql = '''SELECT mid, content FROM t_bid_quanwen_pdf WHERE mid in %s'''
    text_list = execute_raw_sql('default', text_sql, (mid_list,))
    result = {}
    for (mid, content) in text_list:
        result[mid] = {
            'bid_text': content or None
        }
    return result


async def update_bid(pre_session, prod_session, mid_list):
    if not mid_list:
        return
    sql_data = sql_search(mid_list)
    es_str = ''
    for mid, value in sql_data.items():
        es_str += '{"update": {"_id": "%s"}}\n' % mid
        doc = {
            "doc": value
        }
        es_str += json.dumps(doc, ensure_ascii=False) + '\n'
    if es_str:
        # 插入pre
        await updated_es(pre_session, pre_bid_host, es_str)
        # 插入线上
        await updated_es(prod_session, prod_bid_host, es_str)


async def updated_es(session, host, es_str):
    try:
        headers = {'Content-Type': 'application/json'}
        response = await session.post(host, data=es_str.encode('utf-8'), headers=headers, timeout=60)
        result = await response.json()
        if result["errors"]:
            items = result['items']
            error_list = filter(lambda x: x['update']['status'] not in [200, 201], items)
            error_id = [x['update']['_id'] for x in error_list]
            print(error_id)
    except Exception as e:
        print(e)


def get_mid(last_time):
    temp_list = execute_raw_sql('default', 'select mid from t_bid_quanwen_pdf where updated >= %s', (last_time,))
    mid_list = [x[0] for x in temp_list]
    return mid_list, len(mid_list)


# 异步任务数
processes = 2
# 每次处理企业数
step_count = 500


async def main():
    last_hour = datetime.datetime.now() - datetime.timedelta(days=5)
    time_str = last_hour.isoformat()
    pre_auth = aiohttp.BasicAuth(pre_es_user, pre_es_passwd)
    async with aiohttp.ClientSession(auth=pre_auth) as pre_session:
        prod_auth = aiohttp.BasicAuth(prod_es_user, prod_es_passwd)
        async with aiohttp.ClientSession(auth=prod_auth) as prod_session:
            id_list, len_i = get_mid(time_str)
            print(time_str, len_i)
            i = 0
            while i < len_i:
                print(i)
                tasks = []
                for x in range(processes):
                    p_start = i + step_count * x
                    p_end = p_start + step_count
                    id_l = id_list[p_start:p_end]
                    func = asyncio.ensure_future(update_bid(pre_session, prod_session, id_l))
                    tasks.append(func)
                await asyncio.gather(*tasks)
                i += step_count * processes


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
