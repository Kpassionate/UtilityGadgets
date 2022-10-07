#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
对可变对象中 元素的修改
拓展：可变对象（列表list、字典dict、集合set）
     不可变对象（数字类型number、字符串string、元组tuple）
"""
import os

res_list = []
for i in range(3):
    res_list.append({'num': i})
print(res_list)

res_list = []
a = {'num': 0}
for i in range(3):
    a['num'] = i
    res_list.append(a)
print("dict", res_list)

res_list = []
for i in range(3):
    a = {'num': i}
    res_list.append(a)
print(res_list)

res_list = []
a = {6, 5, 4}
for i in range(3):
    a.add(i)
    res_list.append(a)
print("set", res_list)

res_list = []
a = [6, 5, 4]
for i in range(3):
    a.append(i)
    res_list.append(a)
print("list", res_list)

"""
取字典中最大的value 对应的key
"""
salary = {
    'a': 1000,
    'b': 2890,
    'c': 2222
}

res = max(salary, key=lambda k: salary[k])
print(res)

"""
取字典中value值大于某一值的 keys
"""
res = filter(lambda kv: kv[1] > 1000, salary.items())
print([k for k, v in list(res)])

"""
遍历某一路径下所有文件
如果是文件就直接打印，如果是文件夹就继续遍历（递归）
"""


def get_all_file(lj):
    lj_list = os.listdir(lj)
    for item_lj in lj_list:
        new_lj = os.path.join(lj, item_lj)
        if os.path.isfile(new_lj):
            print(new_lj)
        else:
            get_all_file(new_lj)


path = '/Users/akai/ME/github/UtilityGadgets'
get_all_file(path)

"""
登录的装饰器
"""


def login_fun(func):
    def wrapper_func(user, pas, msg):
        if user == 'root' and pas == 'admin':
            print('登录成功')
            return func(msg)
        else:
            print('账号密码有误')

    return wrapper_func


@login_fun
def execute(msg):
    print('aaaaa')
    return {'msg': f'successful, {msg}'}


a = execute('root', 'admin', 'Im winner')
print(a)

"""
代码实现简单的文件复制功能
"""


def file_copy():
    with open('基础1.py', 'rb') as f:
        file = f.read()
        with open('aa.py', 'wb') as f1:
            f1.write(file)


# file_copy()


class Foo(object):
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __hash__(self):
        print("%s调用了哈希方法" % self.name)
        return hash(self.count)

    def __eq__(self, other):
        print("%s调用了eq方法" % self.name)
        if self.__dict__ == other.__dict__:
            print(11111)
        else:
            print(2222222)
        return self.__dict__ == other.__dict__


f1 = Foo('f1', 1)
f2 = Foo('f1', 1)
f3 = Foo('f3', 3)
ls = [f1, f2, f3]
print(set(ls))
