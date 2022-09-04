#!/usr/bin/env python
# coding=utf8
import multiprocessing
import datetime
import time


class HandleData(object):
    def __init__(self):
        self.start_time = time.time()

    @staticmethod
    def handle(data):
        print(data ** 2)

    def read_data(self):
        pool = multiprocessing.Pool(50)
        data_list = [i for i in range(100)]
        for data in data_list:
            pool.apply_async(func=self.handle, args=(data,))
        pool.close()
        pool.join()


if __name__ == "__main__":
    start_time = time.time()
    print('<<<<<<<<<<<<', datetime.datetime.now(), flush=True)
    ver = HandleData()
    ver.read_data()
    import sys

    sys.exit()
