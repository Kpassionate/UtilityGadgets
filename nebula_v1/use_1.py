# coding: utf-8
import time

from nebula3.Config import Config
from nebula3.gclient.net import ConnectionPool


def get_path_nodes(nebula_resp, _list: list, is_mut=False, is_direct=True):
    node_list = []
    i = 0
    while i < nebula_resp.row_size():
        path = nebula_resp.row_values(i)[0].as_path()
        p_list = path.relationships()
        # print(p_list)
        for p in p_list:
            if is_direct:
                start_ver = p.start_vertex_id()._value.value
                node_list.append(start_ver)
            end_ver = p.end_vertex_id()._value.value
            node_list.append(end_ver)
        i += 1
    _nodes = [item for item in node_list if item not in _list]
    return _nodes if is_mut else list(set(_nodes))


def count_score(result_dict: dict, node_list: list, score: int):
    for ent_id in node_list:
        code = result_dict.get(ent_id, 0)
        result_dict.update({
            ent_id: code + score
        })
    return result_dict


def get_level(score: int):
    if score >= 15:
        return 'A'
    elif score >= 8:
        return 'B'
    elif score >= 3:
        return 'C'
    else:
        return 'D'


def main(_client, _list):
    result_dict = {}
    # 企业分支
    branch_sql = f"""MATCH p=(v)-[e:`branch`]-(v2) WHERE id(v) IN {_list} return p;"""
    resp = _client.execute(branch_sql)
    node_list = get_path_nodes(resp, _list)
    result_dict = count_score(result_dict, node_list, 15)
    # 投资关系
    invest_sql = f"""MATCH p=(v)-[e:`invest`]-(v2) WHERE id(v) IN {_list} return p;"""
    resp = _client.execute(invest_sql)
    node_list = get_path_nodes(resp, _list)
    result_dict = count_score(result_dict, node_list, 10)
    # 知识产权代理
    ipr_sql = f"""MATCH p=(v)-[e:`ipr`]-(v2) WHERE id(v) IN {_list} return p;"""
    resp = _client.execute(ipr_sql)
    node_list = get_path_nodes(resp, _list, True)
    result_dict = count_score(result_dict, node_list, 3)
    # 招投标关系
    bid_sql = f"""MATCH p=(v)-[e:`bid_company`]-()-[:`bid_company`]-() WHERE id(v) IN {_list} RETURN p;"""
    resp = _client.execute(bid_sql)
    node_list = get_path_nodes(resp, _list, True, False)
    result_dict = count_score(result_dict, node_list, 8)
    # 企业风险关系
    case_sql = f"""MATCH p=(v)-[e:`case_company`]-()-[:`case_company`]-() WHERE id(v) IN {_list} RETURN p;"""
    resp = _client.execute(case_sql)
    node_list = get_path_nodes(resp, _list, True, False)
    result_dict = count_score(result_dict, node_list, -1)
    # 企业董监高、法人、股东关系
    fr_inv_sql = f"""MATCH p=(v)-[e:`faren_company`|:`inv_company`]-()-[:`faren_company`|:`inv_company`]-()
                    WHERE id(v) IN {_list} RETURN p;"""
    resp = _client.execute(fr_inv_sql)
    node_list = get_path_nodes(resp, _list, True, False)
    result_dict = count_score(result_dict, node_list, 20)
    lx_sql = f"""MATCH p=(v)-[e:`lx_company`]-()-[:`lx_company`]-() WHERE id(v) IN {_list} RETURN p"""
    resp = _client.execute(lx_sql)
    node_list = get_path_nodes(resp, _list, True, False)
    result_dict = count_score(result_dict, node_list, 10)
    print(result_dict)
    result_dict = {k: get_level(v) for k, v in result_dict.items()}
    return result_dict


if __name__ == '__main__':
    config = Config()
    config.max_connection_pool_size = 1
    connection_pool = ConnectionPool()
    assert connection_pool.init([('xx.xx.xx.xx', 0000)], config)
    client = connection_pool.get_session('xx', 'xxx')
    client.execute('use xxxx')
    data = main(client, [1739082])
    client.release()
    connection_pool.close()
