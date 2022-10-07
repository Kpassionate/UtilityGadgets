import itertools
import time
from functools import reduce
from collections import Counter

"""
新式类、经典类
python3.x的所有类都会自动转换为一个新式类，不论是否有继承object对象。
python2.x必须显式地指定类继承object父类才表示新式类。
新式类：方法属性查找链 - 广度优先
经典类：...............深度优先
"""

"""
# 笛卡尔集
"""
print('<<<<<<<<<<<<<<<<<<笛卡尔集>>>>>>>>>>>>>>>>>>>>>>>')
for p in itertools.product([1, 2, 3], [4, 5]):
    print(p)

import keylp as kp

res = kp.build([1, 2], [3, 4])
print(res)

"""
Iterators 库的使用
"""
print('<<<<<<<<<<<<<<<<<<<<Iterators>>>>>>>>>>>>>>>>>>>>')
res = itertools.compress([1, 2, 4], [4, 2])
print([i for i in res])
res = itertools.count()
print(res)

"""
Counter
"""
print('<<<<<<<<<<<<<<<<<<collections Counter>>>>>>>>>>>>>>>>>>>>>')

print(Counter('112'))
res = Counter('abracadabra').most_common(3)
print(res)

res = Counter('abracadabra').elements()
print([i for i in res])
"""
单例模式
是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在
1.实例化一个的对象，要用时直接import导如这个对象，而不是再实例化一个，这样就做到了单例模式了

2、当实例化一个对象时，是先执行了类的__new__方法（没写时，默认调用object.new），实例化对象；
然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式。
"""
print('<<<<<<<<<<<<<<<<<<<<<<单例模式>>>>>>>>>>>>>>>>>>>>')


class SampleSignal(object):
    signal = None

    def __init__(self):
        print('初始化对象')

    def __new__(cls, *args, **kwargs):
        print('new一个对象')
        if cls.signal is None:
            cls.obj = object.__new__(cls)
            return cls.obj
        else:
            return cls.signal


sig_obj = SampleSignal()

"""
迭代器、生成器
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串、列表、元组、集合、字典对象都可用于创建迭代器
// 可用iter() 创建迭代器对象 用next()取值或者遍历取值

创建一个迭代器
把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
__iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
__next__() 方法会返回下一个迭代器对象。
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。


在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
调用一个生成器函数，返回的是一个迭代器对象。
"""

print('<<<<<<<<<<<<<<<<<<<<<迭代器、生成器>>>>>>>>>>>>>>>>>>>>>>>')

# list1 = {'a': 1, 'b': 2}  # dict_keyiterator
# list1 = {1, 2}  # set_iterator
# list1 = (1, 2)  # tuple_iterator
# list1 = [1, 2]  # list_iterator
list1 = '123'  # str_iterator

res = iter(list1)
print(res)
print(res.__next__())
print(next(res))


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


numb_obj = MyNumbers()
my_iter = iter(numb_obj)

for x in my_iter:
    print(x)

print('《《《《《《《《《《《《《《《《》》》》》》》》》》》》》》》》')


# yield 生成器方式实现斐波那契数列
def fib3(n):
    a, b, counter = 1, 0, 0
    while n > counter:
        yield a
        a, b = a + b, a
        counter += 1


print([i for i in fib3(5)])


def func1(n):
    for i in range(n):
        yield i


res = func1(7)
print(res)
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(next(res))
print(next(res))

"""
匿名函数
"""
print('<<<<<<<<<<<<<<<<<<<<<<匿名函数>>>>>>>>>>>>>>>')
data_list = [1, 2, 3]
sum_data = reduce(lambda a, b: a + b, data_list)
print(sum_data)

mul_fun = lambda a, b: a * b
print(mul_fun(2, 4))

"""
斐波那契数列
1 1 2 3 5 8 ...
"""

print('<<<<<<<<<<<<<<<<<<<<<<斐波那契数列>>>>>>>>>>>>>>>')


# 递归法
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print([fib(i) for i in range(1, 10)])


# 背包函数
def script_time(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        fun = func(*args, **kwargs)
        print(time.time() - start_time)
        return fun

    return inner


# 累加法
@script_time
def fib2(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    while n > 2:
        a, b = a + b, a
        n -= 1
    return a


print(fib2(10))
# print([fib2(i) for i in range(1, 10)])
