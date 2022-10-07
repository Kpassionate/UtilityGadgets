#!/usr/bin/python
# -*- coding:utf-8 -*-

import xmltodict as xmltodict

with open('pay.xml', 'r') as f:
    content = f.read()
dict_xml = xmltodict.parse(content)
print("****xml 转 字典****", dict_xml)

dict_xml['MSG']['BUSI']['RISKS'] = {
    'RISK': [
        {
            'BLUE_ID': '1111', 'BLUE_TYPE': '0000', 'PREMIUM': '111'
        },
        {
            'BLUE_ID': '1111', 'BLUE_TYPE': '0000', 'PREMIUM': '111'
        }]
}

with open('new_pay.xml', 'w') as f:
    f.write(xmltodict.unparse(dict_xml, encoding="gbk"))
