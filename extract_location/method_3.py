# -*- coding:utf-8 -*-

import re
import jieba
from pymysql.converters import escape_string
import redis
from db_handler import execute_raw_sql, Database

pool = redis.ConnectionPool(host='127.0.0.1', port=6379)

catch = redis.Redis(connection_pool=pool)
db_config = {
    'default': {
        'host': '...',
        'port': '3306',
        'user': 'root',
        'password': '...',
        'database': 'qk_dict',
    },
}

Database.connect(**db_config)


def region_db():
    _region_name_dict = {}
    sql1 = """SELECT a.NAME,a.CODE,count(1) FROM qk_dict.code_region a GROUP BY a.NAME HAVING count(1)< 2;"""
    sql2 = """SELECT a.fulltitle,a.CODE FROM qk_dict.code_region a;"""
    sql3 = """SELECT SUBSTR(a.NAME,1,CHAR_LENGTH(a.NAME)-1) AS new_name,a.CODE,count(1) FROM qk_dict.code_region a 
        GROUP BY new_name HAVING count(1)< 2 AND CHAR_LENGTH(new_name)> 1; """
    for (name, code, count) in execute_raw_sql('default', sql1):
        _region_name_dict[name] = code
    for (fulltitle, code) in execute_raw_sql('default', sql2):
        _region_name_dict[fulltitle] = code
    for (new_name, code, count) in execute_raw_sql('default', sql3):
        _region_name_dict[new_name] = code
    return _region_name_dict


def get_region_code_by_re(address):
    address = escape_string(address)
    if not address:
        return None
    region_dict = catch.get('region_dict2')
    if region_dict:
        region_dict = eval(region_dict.decode('utf8'))
    else:
        region_dict = region_db()
        catch.set('region_dict2', region_dict, 365*24*3600)
    region_code = {v: k for k, v in region_dict.items()}
    # 获取到地区列表
    region_name = region_dict.keys()
    # 添加动态词典
    [jieba.add_word(name) for name in region_name]
    # 获取到分词数据
    seg_list = jieba.lcut(address, cut_all=False)
    str_content = ' '.join(seg_list)
    lof_terms = region_name
    rx = r"(?=\b({})\b)".format("|".join(map(re.escape, sorted(lof_terms, key=len, reverse=True))))
    pattern = re.compile(rx)
    found_terms = re.findall(pattern, str_content)
    code_list = []
    for name in found_terms:
        code = region_dict.get(name)
        if not code:
            continue
        code_list.append(code)
    first = code_list[0][:2] if code_list else 0
    new_code_list = []
    for item in code_list:
        if first != item[:2]:
            return 0
        new_code_list.append(int(item))
    print(region_code.get(str(max(new_code_list))))
    return str(max(new_code_list)) if code_list else 0


# 主函数
def main(content):
    code = get_region_code_by_re(content)
    return code or -1


if __name__ == "__main__":
    import time
    i = time.time()
    resp = main('河南省')
    print(resp)
    print(time.time() - i)
