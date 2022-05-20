# -*- coding:utf-8 -*-

import difflib
import re
from collections import defaultdict
import jieba
from django.template.defaultfilters import striptags
from pymysql.converters import escape_string

from db_handler import execute_raw_sql, Database

db_config = {
    'default': {
        'host': '127.0.0.1',
        'port': '3306',
        'user': 'root',
        'password': '1234',
        'database': 'qk_dict',
    },
}

Database.connect(**db_config)


def region_db():
    _region_dict = defaultdict(dict)
    region_code = {}
    sql = """select code, name, level, fulltitle from code_region"""
    for (code, name, level, fulltitle) in execute_raw_sql('default', sql):
        _region_dict[name] = {
            'code': code,
            'name': name,
            'fulltitle': fulltitle
        }
        _region_dict[fulltitle] = {
            'code': code,
            'name': name,
            'fulltitle': fulltitle
        }
        region_code[code] = (name, fulltitle)
    return _region_dict, region_code


region_dict, region_code = region_db()
# 获取到地区列表
region_name = region_dict.keys()

# 添加动态词典（亦可添加自定义词库）
[jieba.add_word(fulltitle) for (name, fulltitle) in region_code.values()]
error_words = ['城区', '东区', '西区', '朝阳区']
[jieba.del_word(item) for item in error_words]


# 获取两个字符串的相似度
def string_similar(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()


def get_region_ratio(address):
    # 获取到分词数据
    seg_list = jieba.lcut(address, cut_all=False)
    # 去重
    seg_list = list(set(seg_list))
    ratio_dict = defaultdict(list)
    for key in seg_list:
        for name in region_name:
            similar_ratio = string_similar(key, name)
            if similar_ratio > 0.7:
                ratio_dict[similar_ratio].append(name)
    return ratio_dict


def get_region_code_by_similar(address):
    address = escape_string(address)
    if not address:
        return None
    redio_dict = get_region_ratio(address)
    if not redio_dict:
        return None
    max_index = max(redio_dict.keys())
    name_list = redio_dict[max_index]
    code_list = []
    for name in name_list:
        code = region_dict.get(name, {}).get('code', 0)
        code_list.append(int(code))
    return str(max(code_list)) if code_list else 0


def get_region_code_by_re(address):
    address = escape_string(address)
    if not address:
        return None
    # 获取到分词数据
    seg_list = jieba.lcut(address, cut_all=False)
    # 去重
    seg_list = list(set(seg_list))
    str_content = ' '.join(seg_list)
    lof_terms = region_name
    rx = r"(?=\b({})\b)".format("|".join(map(re.escape, sorted(lof_terms, key=len, reverse=True))))
    pattern = re.compile(rx)
    found_terms = re.findall(pattern, str_content)

    code_list = []
    for name in found_terms:
        code = region_dict.get(name, {}).get('code', 0)
        code_list.append(int(code))
    return str(max(code_list)) if code_list else 0


def re_code(title, content=None):
    code = get_region_code_by_re(striptags(title))
    if not code and content:
        code = get_region_code_by_re(striptags(content))
    return code


def similar_code(title, content=None):
    code = get_region_code_by_similar(striptags(title))
    if not code and content:
        code = get_region_code_by_similar(striptags(content))
    return code


# 主函数
def main(title, content=None):
    """
    优先使用正则匹配。
    """
    code = re_code(title, content)
    if not code:
        # 增加name分词
        [jieba.add_word(item) for item in region_dict.keys()]
        code = re_code(title, content)
    if not code:
        code = similar_code(title, content)
    return code or -1


if __name__ == "__main__":
    resp = main('北京市朝阳区')
    print(resp)
    print(region_code[resp])
