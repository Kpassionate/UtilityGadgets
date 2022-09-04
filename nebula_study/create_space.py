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
        if not hasattr(resp, 'data'):
            continue
        for _data in line['data']:
            result.append(_data['row'])
    return result


def extract_edge(resp):
    print(resp.col_size(), resp.row_size())
    i = 0
    result = []
    while i < resp.row_size():
        for line in resp.row_values(i):
            result.append(line)
        i += 1
    return result


def extract_path(resp):
    i = 0
    while i < resp.row_size():
        path = resp.row_values(i)[0].as_path()
        # 获取到所有的点
        nodes = path.nodes()
        print(nodes)
        # 获取到点到点列表
        p_list = path.relationships()
        for p in p_list:
            # 获取到边的名称
            edge_name = p.edge_name()
            print(edge_name)
            # 获取到边的属性
            properties = p.properties()
            print(properties)
            # 获取到边的起点
            start_ver = p.start_vertex_id()
            print(start_ver)
            # 获取到边的终点
            end_ver = p.end_vertex_id()
            print(end_ver)
        i += 1


def prepare_data(_client, _sql):
    resp = _client.execute_json(_sql)
    return handle_json(resp)


if __name__ == '__main__':
    a = time.time()
    config = Config()
    config.max_connection_pool_size = 1
    connection_pool = ConnectionPool()
    assert connection_pool.init([('127.0.0.1', 9669)], config)
    client = connection_pool.get_session('root', 'soft')
    client.execute('use company_overview')
    sql = """
      DROP SPACE IF EXISTS company_overview;
      CREATE SPACE IF NOT EXISTS company_overview(partition_num=60, replica_factor=1, vid_type=fixed_string(60));
      USE company_overview;
      CREATE TAG IF NOT EXISTS company(ent_id int not null, ent_name string);
      CREATE TAG IF NOT EXISTS person(person_id int, person_name string);
      CREATE TAG IF NOT EXISTS contact(contact_info string);
      CREATE TAG IF NOT EXISTS bid(mid int, title string, amount string);
      CREATE TAG IF NOT EXISTS cases(mid string, case_num string, title string, case_type string);
      CREATE EDGE faren_company(edge_type int default 1);
      CREATE EDGE manager_company(position string, edge_type int default 2);
      CREATE EDGE inv_company(edge_type int default 3);
      CREATE EDGE lx_company(contact string, contact_type int, edge_type int default 4);
      CREATE EDGE invest(amount string, radio string, edge_type int default 5);
      CREATE EDGE branch(edge_type int default 6);
      CREATE EDGE case_company(role_type string, edge_type int default 8);
      CREATE EDGE bid_company(role_type string, edge_type int default 9);
    """
    data = prepare_data(client, sql)
    client.release()
    connection_pool.close()
    print(time.time() - a)

