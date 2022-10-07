#!/usr/bin/python
# -*- coding:utf-8 -*-

print('<<<<<<<<<<<<<<<<<<不用内置函数取开方>>>>>>>>>>>>>>>>>>>>>>')


def my_sqrt(n):
    num = n / 2.0
    while True:
        guess_num = (num + n / num) / 2
        if abs(guess_num - num) < 0.00001:
            return num
        num = guess_num


print(my_sqrt(8))

print('<<<<<<<<<<<<<<<<<<<查询数据是否是2的N次方>>>>>>>>>>>>>>>>>>>>>')


def bool_power_of_two(n):
    if n <= 0:
        return False
    while n > 1:
        n /= 2
    if n == 1:
        return True
    else:
        return False


print(bool_power_of_two(3))


def bool_power_of_two1(n):
    return n & (n - 1) == 0


print(bool_power_of_two1(4))

print('<<<<<<<<<<<<<<<<<<<<<<<啤酒（啤酒瓶、瓶盖）换酒算法>>>>>>>>>>>>>>>>>>>>>>>>>>')


def wine_all(sum, x, y, z):
    """
    sum:总数
    x:啤酒数
    y:啤酒瓶数
    z:啤酒瓶盖数
    """
    if x == 0 and y // 2 == 0 and z // 4 == 0:
        return sum
    elif x:
        sum += x
        return wine_all(sum, 0, y + x, z + x)
    elif y // 2:
        x = y // 2
        return wine_all(sum, x, y % 2, z)
    else:
        x = z // 4
        return wine_all(sum, x, y, z % 4)


print(wine_all(0, 8, 0, 0))

print('<<<<<<<<<<<<<<<<<<<<<斐波那契数列>>>>>>>>>>>>>>')


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(5))


def fib1(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    while n > 2:
        a, b = a + b, a
        n -= 1
    return a


print(fib1(6))
