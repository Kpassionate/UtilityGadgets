#!/usr/bin/python
# -*- coding:utf-8 -*-
import copy

print('############################ 1、斐波那契数列')


# 累加法
def fib(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    while n > 2:
        a, b = a + b, a
        n -= 1
    return a


print(fib(6))


# 递归法
def fib1(n):
    if n <= 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


print(fib1(6))


# 生成器法
def fib2(n):
    a, b, counter = 1, 0, 0
    while counter < n:
        yield a
        a, b = a + b, a
        counter += 1


print([i for i in fib2(6)])

print('####### 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？')


def random_num_three():
    res = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                data_set = set()
                data_set.add(i)
                data_set.add(j)
                data_set.add(k)
                if len(data_set) == 3:
                    res.append(int(str(i) + str(j) + str(k)))
    res = list(set(res))
    res.sort(reverse=True)
    print(res, len(res))


def random_num_three1():
    res = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    res.append(i * 100 + j * 10 + k)
    print(res, len(res))


random_num_three1()


def random_num_three2():
    from itertools import permutations

    res = []
    for i, j, k in permutations([1, 2, 3, 4], 3):
        res.append(int(i * 100 + j * 10 + k))
    print(res, len(res))


random_num_three2()

print('######################## 3.将一个列表的数据复制到另一个列表中。')
list1 = [1, 2, 4, 3]
list2 = list1[:]
list3 = list1.copy()  # 浅拷贝
print(list2)
list1.append(8)
print(list1, id(list1))
print(list2, id(list2))
print(list3, id(list3))

# 拓展
new_list = [[1, 2, 3], [5, 6, 7]]
list1 = new_list.copy()
list2 = new_list[:]
list3 = copy.copy(new_list)
list4 = copy.deepcopy(new_list)
new_list[0].append(4)
# id()  (CPython uses the object's memory address.)
print(new_list, id(new_list), '******')
print(list1, id(list1))
print(list2, id(list2))
print(list3, id(list3))
print(list4, id(list4))
print(id(new_list[1]), id(list1[1]))  # 内部元素的内存地址和之前一致，[:]相当于浅拷贝
print(id(new_list[1]), id(list4[1]))  # 深拷贝内部元素的内存地址和之前的不一致

# 按照字典的key,value排序
dict1 = {'a': 2, 'b': 3, 'c': 1}

print(sorted(dict1.items(), key=lambda kv: kv[0]))
print(sorted(dict1.items(), key=lambda kv: kv[1], reverse=True))

print('################################ 计算字符串出现的次数')
# str1 = input('请输入一个字符串:\n')
# str2 = input('请输入一个子字符串:\n')
# ncount = str1.count(str2)
# print(ncount)

# 计算字符串中各个字母出现的次数
str1 = 'anasnlnc'
from collections import Counter, defaultdict

print(Counter(str1))

res = {}
for i in str1:
    if i not in res:
        res[i] = 1
    else:
        res[i] += 1
print(res)

print('########################################## 列表转字典')
lista = ['a', 'b']
print(dict([list(lista)]))
print(list(zip(lista[0], lista[1])))

# 4.一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
res = []
for i in range(2, 1001):
    data_list = []
    for j in range(1, i + 1):
        if i % j == 0:
            data_list.append(j)
    data_list.pop(-1)
    if sum(data_list) == i:
        res.append({i: data_list})
print(res)

print('#################有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。')
# lista = [1, 2, 4, 6, 9]
lista = [9, 8, 6, 2]

a = 5
if lista[0] > lista[1]:
    for i in range(len(lista)):
        if lista[i] < a < lista[i - 1]:
            lista.insert(i, a)
else:
    for i in range(len(lista)):
        if lista[i] > a > lista[i - 1]:
            lista.insert(i, a)
print(lista)

print('##################################将一个数组逆序输出。')
a = [1, 4, 5, 8, 2]
a.sort(reverse=True)
print(a)

print('#####################################查找字符串。')
str1 = 'abab,ssdmmamcomov'
print(str1.find('ss'))
import re

print(re.findall('ab', str1))

print('# 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。')
a = 3
n = 5
num_list = [int(str(a) * i) for i in range(1, n + 1)]
print(num_list)
print(sum(num_list))

print('######################将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。')


def reduce_num(n):
    while n != 1:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n //= index  # n 等于n//index
                if n == 1:
                    print(index)
                else:  # index 一定是素数
                    print('{} *'.format(index), end=" ")
                break


reduce_num(90)

print('##########################菱形')
start = 1  # 开始值
i = 2  # 变量值
while start >= 0:
    print(int((7 - start) / 2) * ' ' + '*' * start)
    start += i
    if start == 7:
        i = -i

print('####################求1+2!+3!+…+20!的和。')
n = 20
num = 1
sum = 0
for i in range(1, n + 1):
    num *= i
    sum += num
print('1! + 2! + 3! + ... + 20! = %d' % sum)

print('##########一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。')
num = 12321
num_str = str(num)
if num_str[0] == num_str[-1] and num_str[1] == num_str[-2]:
    print('1')
else:
    print('0')

# 查找五位数的回文数
res = []
for i in range(10001, 100000):
    num_str = str(i)
    if num_str[0] == num_str[-1] and num_str[1] == num_str[-2]:
        res.append(i)
print(res)

print('猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上'
      '都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。')
x2 = 1
x1 = None
for day in range(9, 0, -1):
    x1 = (x2 + 1) * 2
    x2 = x1
print(x1)

print('#############################求100以内的素数')
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

print('############给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。')
num = 12345
str1 = str(num)
print('它是%d位数' % len(str1))
print('逆序打印出各位数字', str1[::-1])

print('一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？')
height = 100
for i in range(1, 11):
    height /= 2
print(height)

print('######################### 乘法口诀')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j} * {i} = {i * j}', end='  ')
    print()

print('<<<<<<<<<<<<<<<<<<<识别2的指数幂的数字>>>>>>>>>>>>>>>>>>>>>')
"""
二进制表示2的幂次方数中只有一个1，后面跟的是n个0； 因此问题可以转化为判断1后面是否跟了n个0。
将这个数减去1后会发现，仅有的那个1会变为0，而原来的那n个0会变为1；因此将原来的数与运算上(&)减去1后的数字，结果为零。
"""


def func(n):
    return n & (n - 1) == 0


print(func(31))


def bool_power_of_two(n: int) -> bool:
    if n <= 0:
        return False
    elif n == 1:
        return True
    while n > 1:
        n /= 2
    if n == 1:
        return True
    else:
        return False


print(bool_power_of_two(9), 'dddddddddddd')

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<不用sqrt实现一个数字的二次根号值>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def my_sqrt(x):
    last_guess = x / 2.0
    while True:
        guess = (last_guess + x / last_guess) / 2
        if abs(guess - last_guess) < .000001:  # example threshold
            return guess
        last_guess = guess


print(my_sqrt(16))

import math

print(math.sqrt(8))

print('<<<<<<<<<<<<<<<<<<<<<瓶子换酒算法>>>>>>>>>>>>>>>>>>>')
"""
空瓶换酒的目标是求解最终能喝多少瓶酒？问题的版本有很多种：共有x元，y元一瓶酒，初始有x/y瓶酒，m个酒瓶可以换一瓶酒，
n个瓶盖可以换一瓶酒。其还分为不可赊账和可赊账，此处讨论的是不可赊账版本，x/y取为num，m取2，n取4.（可赊账类转换为函数求解问题）
"""
# 递归思路
num = 8


def for_wine(sum, wine, bottle, lid):
    if wine == 0 and bottle // 2 == 0 and lid // 4 == 0:  # 终止条件
        return sum
    elif wine != 0:  # 消耗酒
        sum += wine
        return for_wine(sum, 0, bottle + wine, lid + wine)
    elif bottle // 2 != 0:  # 瓶兑酒
        wine += bottle // 2
        return for_wine(sum, wine, bottle % 2, lid)
    else:
        wine += lid // 4  # 瓶盖兑酒
        return for_wine(sum, wine, bottle, lid % 4)


print(for_wine(0, num, 0, 0))


def wine_nums(sum, x, y, z):
    """
    sum: 能喝到的总数
    x:啤酒数
    y:啤酒瓶数
    z:啤酒瓶酒盖数
    """
    if x == 0 and y // 2 == 0 and z // 4 == 0:
        return sum
    elif x:
        sum += x
        return wine_nums(sum, 0, y + x, z + x)
    elif y // 2:
        x += y // 2
        return wine_nums(sum, x, y % 2, z)
    else:
        x += z // 4
        return wine_nums(sum, x, y, z % 4)


print(wine_nums(0, 8, 0, 0))

# 归纳法
num = 8
sum = 4 * num - 5 if num > 1 else 1
print(sum)
