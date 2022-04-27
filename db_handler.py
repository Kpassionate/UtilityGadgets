# coding: utf-8
import pymysql


# 数据库调用
class Database:
    conn = {}
    db_config = {}

    @classmethod
    def connect(cls, **databases):
        for db_label, db_config in databases.items():
            cls.conn[db_label] = pymysql.connect(
                host=db_config.get('host', 'localhost'),
                port=int(db_config.get('port', 3306)),
                user=db_config.get('user', 'root'),
                passwd=db_config.get('password', 'pas'),
                db=db_config.get('database', 'code'),
                charset=db_config.get('charset', 'utf8'),
                autocommit=True)
        cls.db_config.update(databases)

    @classmethod
    def get_conn(cls, db_label):
        if not cls.conn[db_label] or not cls.conn[db_label].open:
            cls.connect(**cls.db_config)
        try:
            cls.conn[db_label].ping()
        except pymysql.OperationalError:
            cls.connect(**cls.db_config)
        return cls.conn[db_label]

    @classmethod
    def execute(cls, db_label, *args):
        db_conn = cls.get_conn(db_label)
        cursor = db_conn.cursor()
        cursor.execute(*args)
        return cursor

    def __del__(self):
        for _, conn in self.conn:
            if conn and conn.open:
                conn.close()


def execute_raw_sql(db_label, sql, params=None):
    return Database.execute(db_label, sql, params) if params else Database.execute(db_label, sql)
