# coding: utf-8
import json
import time
from nebula3.Config import Config
from nebula3.gclient.net import ConnectionPool


def handle_json(resp):
    """
    execute_json 类型
    :param resp:
    :return:
    """
    resp = json.loads(resp)
    if resp['errors'][0]['code'] != 0:
        print(resp)
        return []
    result = []
    for line in resp['results']:
        for _data in line['data']:
            result.append(_data['row'])
    return result


def get_level(score: int):
    """
    输出分段
    :param score:
    :return:
    """
    if score >= 15:
        return 'A'
    elif score >= 8:
        return 'B'
    return 'C'


def get_types(_type):
    type_str = str(_type)
    type_len = len(type_str)
    if type_len < 5:
        type_str = '0' * (5 - type_len) + type_str
    type_list = []
    if int(type_str[0]):
        type_list.append('F')
    if int(type_str[1]):
        type_list.append('E')
    if int(type_str[2]):
        type_list.append('D')
    if int(type_str[3]):
        type_list.append('B')
    if int(type_str[4]):
        type_list.append('A')
    return type_list


def main(_client, _list):
    # 预处理
    _list = ["'ent_" + f"{i}'" for i in _list]
    company = ",".join(_list)
    result = {}
    # 数据查询
    basic_sql = f"""
        (go from {company} over branch where branch._dst not in [{company}] 
        yield distinct branch._dst AS i, 15 as score, 1 as type
        union all
        go from {company} over branch REVERSELY where branch._src not in [{company}] 
        yield distinct branch._dst AS i, 15 as score, 1 as type
        union all
        go from {company} over invest where invest._dst not in [{company}] 
        yield invest._dst AS i, 10 as score, 10 as type
        union all
        go from {company} over invest REVERSELY where invest._src not in [{company}] 
        yield invest._dst AS i, 10 as score, 10 as type
        union all
        go from {company} over bid_company REVERSELY where properties(edge).role_type=="0" yield 
        bid_company._dst AS b | go from $-.b over bid_company where bid_company._dst not in [{company}] 
        and properties(edge).role_type =="1" yield bid_company._dst as i,  8 as score, 100 as type
        union all
        go from {company} over bid_company REVERSELY where properties(edge).role_type=="1" yield 
        bid_company._dst AS b | go from $-.b over bid_company where bid_company._dst not in [{company}] 
        and properties(edge).role_type =="0" yield bid_company._dst as i,  8 as score, 100 as type
        union all
        go from {company} over case_company REVERSELY where properties(edge).role_type=="d" yield 
        case_company._dst AS b | go from $-.b over case_company where case_company._dst not in [{company}] 
        and properties(edge).role_type=="p" yield case_company._dst as i,  -1 as score, 1000 as type
        union all
        go from {company} over case_company REVERSELY where properties(edge).role_type=="p" yield 
        case_company._dst AS b | go from $-.b over case_company where case_company._dst not in [{company}] 
        and properties(edge).role_type=="d" yield case_company._dst as i,  -1 as score, 1000 as type
        union all
        go from {company} over manager_company,inv_company,faren_company REVERSELY yield 
        src(edge) as b | go from $-.b over manager_company,inv_company,faren_company 
        where manager_company._dst not in [{company}] and  inv_company._dst not in [{company}]
        and  faren_company._dst not in [{company}]
        yield  dst(edge) as  i,  20 as score, 10000 as type
        union all
        go from {company} over lx_company REVERSELY yield 
        lx_company._dst AS b | go from $-.b over lx_company where lx_company._dst not in [{company}]
        yield lx_company._dst as i, 15 as score, 10000 as type)
    """
    nebula_sql = basic_sql + """| group by $-.i yield $-.i as ent_id, sum($-.score) as sum_score, sum(distinct $-.type) 
        as type | order by $-.sum_score desc | limit 20"""
    nebula_count_sql = basic_sql + "| yield count(distinct $-.i) as total"
    count_data = _client.execute_json(nebula_count_sql)
    count_data = handle_json(count_data)
    total = count_data[0][0] if count_data else 0
    data_resp = _client.execute_json(nebula_sql)
    data_resp = handle_json(data_resp)
    for ent_id, score, _type in data_resp:
        result[ent_id.split('_')[1]] = {
            'strength': get_level(score),
            'type': get_types(_type)
        }
    return result, total


if __name__ == '__main__':
    config = Config()
    config.max_connection_pool_size = 5
    connection_pool = ConnectionPool()
    assert connection_pool.init([('172.21.28.148', 9669)], config)
    client = connection_pool.get_session('root', 'vesoft')
    client.execute('use company_overview')
    data = main(client, [15070600, 5262740])
    client.release()
    connection_pool.close()
    print(data)
