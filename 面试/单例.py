#!/usr/bin/python
# -*- coding:utf-8 -*-


import itertools
import time


class Sample(object):
    signal = None

    def __init__(self):
        self.start_time = time.time()

    def __new__(cls, *args, **kwargs):
        if cls.signal is None:
            cls.obj = object.__new__(cls)
            return cls.obj
        else:
            return cls.signal

    @staticmethod
    def build(first_list, second_list):
        res_list = [p for p in itertools.product(first_list, second_list)]
        return res_list
