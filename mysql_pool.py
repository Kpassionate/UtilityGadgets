#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pandas as pd
import pymysql
from dbutils.pooled_db import PooledDB

CONNECTION_CONFIG = {
    "DATA_WAREHOUSE": {
        "host": '',
        "port": 3306,
        "user": '',
        "passwd": '',
        "db": ''
    }
}


class MysqlPool:
    """
    数据库连接池
    """

    def __init__(self, pool=None):
        self.POOL = pool

    def __new__(cls, *args, **kw):
        """
        启用单例模式
        :param args:
        :param kw:
        :return:
        """
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    def end(self):
        self.POOL.close()

    def connect(self):
        """
        启动连接
        :return:
        """
        conn = self.POOL.connection()
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        return conn, cursor

    def connect_close(self, conn, cursor):
        """
        关闭连接
        :param conn:
        :param cursor:
        :return:
        """
        cursor.close()
        conn.close()

    def fetch_all(self, sql, *args):
        """
        批量查询
        :param sql:
        :param args:
        :return:
        """
        conn, cursor = self.connect()
        try:
            cursor.execute(sql, args)
            record_list = cursor.fetchall()
        finally:
            self.connect_close(conn, cursor)

        return record_list

    def fetch_one(self, sql, *args):
        """
        查询单条数据
        :param sql:
        :param args:
        :return:
        """
        conn, cursor = self.connect()
        try:
            cursor.execute(sql, args)
            result = cursor.fetchone()
        finally:
            self.connect_close(conn, cursor)

        return result

    def insert(self, sql, args):
        """
        插入数据
        :param sql:
        :param args:
        :return:
        """
        conn, cursor = self.connect()
        try:
            row = cursor.execute(sql, args)
            conn.commit()
        finally:
            self.connect_close(conn, cursor)
        return row

    def sql_procedure(self, sql):
        conn = self.POOL.connection()
        try:
            return pd.read_sql(sql, conn)
        finally:
            conn.close()


class GetLink(MysqlPool):
    def __init__(self):
        super().__init__(pool=PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=0,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=0,  # 链接池中最多闲置的链接，0和None不限制
            maxshared=0,
            # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1
            # ，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never,
            # 1 = default = whenever it is requested, 2 = when a cursor is created,
            # 4 = when a query is executed, 7 = always
            host=CONNECTION_CONFIG.get("RISK_CONTROL").get('host'),
            port=CONNECTION_CONFIG.get("RISK_CONTROL").get('port'),
            user=CONNECTION_CONFIG.get("RISK_CONTROL").get('user'),
            password=CONNECTION_CONFIG.get("RISK_CONTROL").get('passwd'),
            database=CONNECTION_CONFIG.get("RISK_CONTROL").get('db'),
            charset='utf8'
        ))

    def get_link(self, product):
        sql = f"""
        select `hostname`, `database`, `username`,`password`, `hostport` from xxxx where product = '{product}'
        """
        return self.fetch_one(sql)


class ProductMysqlPool(MysqlPool):
    """
    数据库连接池
    """

    def __init__(self, product):
        g = GetLink()
        link = g.get_link(product)
        super().__init__(pool=PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=10,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=2,  # 链接池中最多闲置的链接，0和None不限制
            maxshared=0,
            # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，
            # 所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=["set time_zone='+5:30';"],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested,
            # 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host=link.get('hostname'),
            port=int(link.get('hostport')),
            user=link.get('username'),
            password=link.get('password'),
            database=link.get('database'),
            charset='utf8'
        ))
        g.end()


class IKH(object):
    def __init__(self, product):
        self.A = ProductMysqlPool(product)
        self.pmp = self.A

    def __del__(self):
        print('to end')
        self.A.end()

    def get_data(self):
        sql = "select * from customer limit 10"
        tmp = self.pmp.fetch_all(sql)
        print(len(tmp))


if __name__ == '__main__':
    ikh = IKH('IKH')
    ikh.get_data()
