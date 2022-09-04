# coding: utf-8

from nebula3.Config import Config
from nebula3.gclient.net import ConnectionPool


def prepare_data(_client, _sql):
    resp = _client.execute(_sql)
    return resp


if __name__ == '__main__':
    config = Config()
    config.max_connection_pool_size = 1
    connection_pool = ConnectionPool()
    assert connection_pool.init([('127.0.0.1', 9669)], config)
    client = connection_pool.get_session('root', 'soft')
    client.execute('use company_overview')
    sql = """
      show spaces;
    """
    data = prepare_data(client, sql)
    client.release()
    connection_pool.close()
    print(data)
